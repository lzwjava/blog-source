---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: TiktokenマルチプロセシングのPickleエラー修正
translated: true
type: note
---

`datasets.map(..., num_proc>1)` をカスタムトークナイザー（nanoGPTのFineWebスクリプトで使用されているTiktokenエンコーダーなど）と一緒に使用する場合、このエラーは非常に一般的です。トークナイザーがBPEファイル（`cl100k_base.tiktoken` など）を読み込むと、このファイルハンドルはLinux（フォークベースのマルチプロセシング）でサブプロセスに送信される際に **ピクル化（pickle化）できません**。

子プロセスは即座にクラッシュします → 「One of the subprocesses has abruptly died」というエラーが発生します。

### クイックフィックス (99% の場合で有効)

`data/fineweb/prepare.py` を編集し、トークナイズ処理を **メインプロセスのみ** で実行するように強制します：

```python
# 80-85行目付近で、.map() 呼び出しを探し、num_proc=8 → num_proc=1 に変更します

tokenized = raw_datasets.map(
    tokenize,
    num_proc=1,               # ← この行を変更（または引数を削除）
    desc="tokenizing the splits",
)
```

これは遅くなります（シングルコア）が、確実に動作します。FineWeb-10Bでは、CPU/ディスクに応じて約30〜60分かかります。

### より良い修正 (マルチプロセシングを維持、高速)

トークナイザーをグローバルスコープでなく、ワーカープロセス内部で遅延読み込みするようにします。

現在のトークナイザー作成部分（40-50行目付近）を以下のパターンに置き換えてください：

```python
import tiktoken

# グローバルの encoder = tiktoken.get_encoding("cl100k_base") を削除

def get_encoder():
    """各サブプロセスでトークナイザーを遅延読み込み"""
    return tiktoken.get_encoding("cl100k_base")

def tokenize(example):
    enc = get_encoder()                                   # ← プロセスごとに読み込み
    ids = enc.encode_ordinary(example["text"])
    ids.append(enc.eot_token)  # またはスクリプトが行う処理
    return {"ids": ids, "len": len(ids)}
```

そして `num_proc=8`（または任意の数）を維持します。この方法では、各ワーカーはフォーク後に自身の .tiktoken ファイルのコピーを読み込むため、ピクル化の問題が発生しません。

### さらに高速な代替案 (繰り返し実行する場合に推奨)

Hugging Faceから10B/100BのFineWeb-Eduシャードを事前にダウンロードし、巨大な .txt ファイルの代わりにparquet/arrowファイルを直接処理するKarpathyの更新されたスクリプトを使用します：

```bash
# より高速で、このバグを完全に回避します
python data/fineweb/prepare_fineweb.py --version 10B
# または 100B
```

新しいスクリプト（2024年頃に追加）は公式のHFデータセットを使用し、マルチプロセシングに対して安全です。

### まとめ

| 解決策                           | 速度      | 複雑さ     | 推奨           |
|----------------------------------|-----------|------------|----------------|
| `num_proc=1`                     | 遅い      | 1行変更    | クイックフィックス |
| tokenize() 内での遅延エンコーダー読み込み | 速い      | 少し編集   | .txt 用に最適  |
| 新しい prepare_fineweb.py スクリプトを使用 | 最速    | 新しいコマンド | 推奨           |

いずれかを選択すれば、このエラーをすぐに解決できます。どの方法を採用したか教えていただければ、必要に応じて正確なパッチをお知らせします！