---
audio: false
lang: ja
layout: post
title: プロジェクト内のJavaパッケージの分析
translated: true
---

クエリに基づいて、`level`パラメータが0または指定されていない場合、パッケージ名の全部分を使用し、`level = 0`を「無限」または「すべての部分を使用」として扱うスクリプトが必要です。以下に、Javaファイルを解析してパッケージ名を抽出するPythonスクリプトの実装方法を説明し、あなたの要件に合わせた完全なソリューションを提供します。

### 要件の理解
- **`level = 0`または指定されていない場合**: Javaの`import`文から抽出したパッケージ名の全体を使用します（例: `java.util`または`com.google.common.eventbus`）、切り捨てません。
- **`level > 0`の場合**: パッケージ名を最初の`level`部分に切り捨てます（例: `com.google.common.eventbus`で`level = 2`は`com.google`になります）。
- スクリプトは、Javaファイルを処理し、`import`文からパッケージ名を抽出し、エッジケースを適切に処理する必要があります。

### ソリューションのアプローチ
1. **引数解析**:
   - ルートディレクトリのみが提供された場合（例: `python script.py /path/to/dir`）、`level = 0`として設定し、パッケージ名の全体を使用します。
   - `level`が提供された場合（例: `python script.py /path/to/dir 2`）、パッケージ名を切り捨てるために使用し、非負の整数であることを確認します。
   - 引数が無効な場合はエラーで終了します。

2. **パッケージの抽出**:
   - `import`文からパッケージ名を抽出します（例: `import java.util.ArrayList;`は`java.util`を生成します）。
   - Javaの命名規則を使用: パッケージ名は通常小文字で、クラス名は大文字で始まります。

3. **パッケージの切り捨てロジック**:
   - `level = 0`の場合、結果セットに完全なパッケージ名を追加します。
   - `level > 0`の場合、パッケージ名をドット（`.`）で分割し、最初の`level`部分を取得します。

4. **ログと出力**:
   - 完全なパッケージ名または切り捨てられたものが使用されていることを明確に示します。
   - 見つかったすべての一意のパッケージをリスト表示します。

### 実装
以下は、あなたの要件を満たす完全なPythonスクリプトです:

```python
import os
import sys

def find_java_files(root_dir):
    """
    指定されたディレクトリとそのサブディレクトリからすべての.javaファイルを再帰的に検索します。

    引数:
        root_dir (str): 検索を開始するルートディレクトリ。

    返り値:
        str: 各.javaファイルの完全なパス。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"[INFO] ディレクトリに入る: {dirpath}")
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    import文からパッケージ名を抽出します。

    パッケージ名は小文字で、クラス名は大文字またはワイルドカード（*）で終了することを前提としています。

    引数:
        import_statement (str): Javaファイルからのimport文の行。

    返り値:
        str: パッケージ名、または決定できない場合は空の文字列。
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # コマンドライン引数の解析
    if len(sys.argv) == 2:
        root_dir = sys.argv[1]
        level = 0  # レベルが提供されていない場合、完全なパッケージ名を使用
    elif len(sys.argv) == 3:
        root_dir = sys.argv[1]
        try:
            level = int(sys.argv[2])
            if level < 0:
                raise ValueError
        except ValueError:
            print("[ERROR] レベルは非負の整数でなければなりません。")
            sys.exit(1)
    else:
        print("使用法: python script.py <root_directory> [level]")
        sys.exit(1)

    # ディレクトリが存在することを確認
    if not os.path.isdir(root_dir):
        print(f"[ERROR] 指定されたパスはディレクトリではありません: {root_dir}")
        sys.exit(1)

    # 分析の開始をログに記録
    if level == 0:
        print(f"[INFO] ディレクトリの分析を開始: {root_dir}で完全なパッケージ名を使用。")
    else:
        print(f"[INFO] ディレクトリの分析を開始: {root_dir}でレベル: {level}")

    # 変数の初期化
    packages = set()
    total_files = 0
    error_files = 0

    # Javaファイルの処理
    for java_file in find_java_files(root_dir):
        print(f"[INFO] ファイルの処理: {java_file}")
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level == 0:
                                # 完全なパッケージ名を使用
                                packages.add(package)
                            else:
                                # 最初の'level'部分に切り捨て
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                                packages.add(truncated_package)
            total_files += 1
        except Exception as e:
            print(f"[ERROR] ファイル {java_file} を読み取れません: {e}")
            error_files += 1
            continue

    # サマリーの表示
    print(f"[INFO] 試行されたJavaファイルの合計: {total_files + error_files}")
    print(f"[INFO] 成功した処理: {total_files}")
    print(f"[INFO] エラーが発生したファイル: {error_files}")
    if level == 0:
        print(f"[INFO] 一意の完全なパッケージの合計: {len(packages)}")
    else:
        print(f"[INFO] レベル {level} の一意のパッケージの合計: {len(packages)}")

    # 結果の表示
    if packages:
        if level == 0:
            print("[INFO] 分析完了。一意の完全なパッケージを表示:")
        else:
            print(f"[INFO] 分析完了。レベル {level} の一意のパッケージを表示:")
        for package in sorted(packages):
            print(package)
    else:
        print("[INFO] パッケージが見つかりませんでした。")
```

### その仕組み
- **スクリプトの実行**:
  - `python script.py /path/to/java/project`: ディレクトリ内のすべての`.java`ファイルを分析し、完全なパッケージ名を使用します（`level = 0`）。
  - `python script.py /path/to/java/project 2`: パッケージ名を最初の2部分に切り捨てます（例: `com.google.common.eventbus`は`com.google`になります）。

- **出力例**:
  Javaファイルに以下の内容があるとします:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **`level = 0`（またはレベルが指定されていない）の場合**:
    ```
    [INFO] ディレクトリの分析を開始: /path/to/java/projectで完全なパッケージ名を使用。
    [INFO] ディレクトリに入る: /path/to/java/project
    [INFO] ファイルの処理: /path/to/java/project/MyFile.java
    [INFO] 試行されたJavaファイルの合計: 1
    [INFO] 成功した処理: 1
    [INFO] エラーが発生したファイル: 0
    [INFO] 一意の完全なパッケージの合計: 2
    [INFO] 分析完了。一意の完全なパッケージを表示:
    com.google.common.eventbus
    java.util
    ```
  - **`level = 2`の場合**:
    ```
    [INFO] ディレクトリの分析を開始: /path/to/java/projectでレベル: 2
    [INFO] ディレクトリに入る: /path/to/java/project
    [INFO] ファイルの処理: /path/to/java/project/MyFile.java
    [INFO] 試行されたJavaファイルの合計: 1
    [INFO] 成功した処理: 1
    [INFO] エラーが発生したファイル: 0
    [INFO] レベル 2 の一意のパッケージの合計: 2
    [INFO] 分析完了。レベル 2 の一意のパッケージを表示:
    com.google
    java.util
    ```

- **主要な機能**:
  - **完全なパッケージ名**: `level = 0`または指定されていない場合、抽出したパッケージ名の全体を使用します（例: `java.util`、`com.google.common.eventbus`）。
  - **切り捨て**: `level > 0`の場合、最初の`level`部分を取得します。
  - **エラーハンドリング**: 有効なディレクトリと非負の`level`を確認します。
  - **一意性**: パッケージを`set`に格納して重複を避けます。

### 取り扱うエッジケース
- **レベルが欠落**: `level = 0`としてデフォルトし、完全なパッケージ名を使用します。
- **無効なレベル**: `level`が負または整数でない場合はエラーで終了します。
- **短いパッケージ**: パッケージが`level`よりも少ない部分を持つ場合（例: `java`で`level = 2`）、完全なパッケージ（`java`）を使用します。
- **空のインポート**: パッケージが抽出できない行はスキップします。

このスクリプトは、あなたの要件を完全に満たします: `level = 0`または指定されていない場合、パッケージ名のすべての部分を使用し、効果的に「無限」として扱います。