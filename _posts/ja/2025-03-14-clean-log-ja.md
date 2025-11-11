---
audio: false
generated: true
lang: ja
layout: post
title: クリーンなログメッセージ
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    ログファイルを読み込み、類似性に基づいて連続する標準ログ行の重複を削除し、
    クリーンなログを指定されたファイルに書き込みます（デフォルトでは入力ファイルを上書き）。

    Args:
        input_path (str, optional): 入力ログファイルのパス。Noneの場合、stdinから読み込み。
        output_path (str, optional): 出力ログファイルのパス。Noneの場合、入力ファイルを上書き。
        similarity_threshold (float, optional): 行を重複と見なす類似度比率（0.0から1.0）。デフォルトは1.0（完全一致）。
        lines_to_compare (int, optional): 比較する連続行数。デフォルトは1。
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compareは1以上の整数でなければなりません。")

    # 入力ソースの決定
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"エラー: パスにファイルが見つかりません: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # stdinからすべての行を読み込み

    # 出力先の決定
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"エラー: 書き込み用にファイルを開けません: {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # 入力ファイルを上書き
        except IOError:
            print(f"エラー: 書き込み用にファイルを開けません: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # input_pathがない場合はstdoutをデフォルトに

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # 'lines_to_compare'行または残りの行（'lines_to_compare'より少ない場合）を収集
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # 比較する十分な行がある場合のみ処理
        if len(current_lines) == lines_to_compare:
            # 最初の行セットから標準情報を抽出
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"非標準行: {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # 非標準行が見つかった場合、このグループの処理を停止

            if all_standard:
                # 2番目の行セット（利用可能な場合）から標準情報を抽出
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # いずれかが非標準行の場合、次の行を非標準として扱う
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"類似度: {similarity:.4f}, 閾値: {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"重複行をスキップ: { ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # 次の行セットに移動
        else:
            # 残りの行（'lines_to_compare'より少ない）を処理
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"非標準行: {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"重複行を {removed_lines} 行削除しました。")


def is_valid_similarity_threshold(value):
    """
    指定された値が有効な類似度閾値かどうかをチェックします。
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("類似度閾値は浮動小数点数でなければなりません。")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("類似度閾値は0.0から1.0の間でなければなりません。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ファイルまたはstdinから重複ログ行をクリーンし、ファイルに書き込みます（デフォルトでは入力ファイルを上書き）。")
    parser.add_argument("input_path", nargs="?", type=str, help="入力ログファイルのパス（オプション、デフォルトはstdin）")
    parser.add_argument("-o", "--output_path", type=str, help="出力ログファイルのパス（オプション、デフォルトは入力ファイルの上書き）")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="行を重複と見なす類似度閾値（0.0-1.0）（デフォルト: 1.0）")
    parser.add_argument("-l", "--lines", type=int, default=1, help="比較する連続行数（デフォルト: 1）")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

このPythonスクリプト`clean_log.py`は、ファイルまたは標準入力から重複ログ行を削除するように設計されています。連続するログ行が重複と見なされるほど類似しているかどうかを判断するために類似度閾値を使用します。

コードの詳細は以下の通りです：

**1. インポート:**

- `sys`: stdinからの読み込みやstderrへの書き込みなど、Pythonインタープリタとの対話に使用
- `argparse`: コマンドラインインターフェースの作成に使用
- `difflib.SequenceMatcher`: 文字列シーケンス間の類似性比較に使用

**2. `clean_log`関数:**

- `input_path`、`output_path`、`similarity_threshold`、`lines_to_compare`を引数として取ります
- `input_path`: 入力ログファイルを指定。`None`の場合、stdinから読み込み
- `output_path`: 出力ファイルを指定。`None`で`input_path`が指定されている場合、入力ファイルを上書き。両方とも`None`の場合、stdoutに書き込み
- `similarity_threshold`: 行を重複と見なす最小類似度比率を決定する0.0から1.0の浮動小数点数。1.0は同一行のみ削除
- `lines_to_compare`: 類似性を比較する連続行数を指定する整数

- **入力処理:**
    - 入力ファイルまたはstdinから行を読み込み
    - 入力ファイルが存在しない場合の`FileNotFoundError`を処理

- **出力処理:**
    - 出力ファイルを書き込み用に開くか、stdoutを使用
    - 出力ファイルを開けない場合の`IOError`を処理

- **重複削除ロジック:**
    - ログファイルの行を`lines_to_compare`のチャンクで反復処理
    - 各チャンクについて：
        - 各行を" | "区切り文字に基づいて部分に分割し、4つの部分（レベル、タイムスタンプ、スレッド、メッセージ）を期待
        - 行に4つの部分がない場合、「非標準」行と見なされ、比較なしで出力に印刷
        - 現在のチャンク内のすべての行が標準の場合、次の`lines_to_compare`行と比較
        - `SequenceMatcher`を使用して、現在と次のチャンクのスレッドとメッセージ部分の結合文字列間の類似度比率を計算
        - 類似度比率が`similarity_threshold`より小さい場合、現在のチャンクの行が出力に印刷
        - 類似度比率が`similarity_threshold`以上の場合、現在のチャンクの行は重複と見なされスキップ
    - ファイルの最後の残りの行（`lines_to_compare`行より少ない）を処理

- **統計:**
    - 削除された行数を追跡
    - 削除された行数をコンソールに表示

- **ファイルクローズ:**
    - 開かれていた場合、出力ファイルを閉じる

**3. `is_valid_similarity_threshold`関数:**

- `argparse`によって使用されるヘルパー関数で、類似度閾値引数を検証
- 入力値が0.0から1.0の間の浮動小数点数かどうかをチェック

**4. `if __name__ == "__main__":`ブロック:**

- スクリプトがコマンドラインから実行されたときにこのブロックが実行
- `argparse`を使用してコマンドライン引数パーサーを作成
- 以下の引数を定義：
    - `input_path`: 入力ログファイルのパス（オプション）
    - `-o`または`--output_path`: 出力ログファイルのパス（オプション）
    - `-s`または`--similarity`: 類似度閾値（デフォルト: 1.0）
    - `-l`または`--lines`: 比較する行数（デフォルト: 1）
- `parser.parse_args()`を使用してコマンドライン引数を解析
- 解析された引数で`clean_log`関数を呼び出し

**要約すると、このスクリプトは、設定可能な類似度閾値と比較行数に基づいて重複行を削除することで、ログファイルをクリーンにする柔軟な方法を提供します。stdinからの読み込み、stdoutへの書き込み、入力ファイルの上書きをサポートしています。**