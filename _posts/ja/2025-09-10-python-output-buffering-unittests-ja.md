---
audio: false
date: 2025-09-10
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: Pythonユニットテストにおける出力バッファリングの解決
translated: true
type: note
---

はい — その遅延はほぼ常に **出力バッファリング** が原因で、Windows の Git-Bash/mintty ではそれがより顕著になります。マルチプロセスでのロギングを行っているのでなければ、キューは必要ありません。まず stdout/stderr のバッファリングを無効にし、unittest 自体のバッファリングを避けてください。

### 実行時に以下のようにする

```bash
# PowerShell / CMD:
py -3.11 -u -m unittest -v

# Git-Bash:
PYTHONUNBUFFERED=1 py -3.11 -u -m unittest -v
# または
PYTHONUNBUFFERED=1 python -u -m unittest -v
```

* `-u` = 非バッファード stdio
* `PYTHONUNBUFFERED=1` = 同上、子プロセスにも影響

`xx.py` を直接使用する場合:

```bash
python -u xx.py -v
```

### コード内で即時出力を実現する (差し替え可能)

テストのブートストラップ (または `if __name__ == "__main__":` ブロック) の先頭に以下を追加:

```python
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")

# Python 3.7+
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, write_through=True)
    sys.stderr.reconfigure(line_buffering=True, write_through=True)

print("booting tests...", flush=True)
```

また、重要な箇所で `print(...)` を使用する際は、`flush=True` を追加してください。

### `logging` モジュールを使用する場合

```python
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,  # 3.8+
)
# StreamHandler は各レコードをフラッシュします。これにより、stdout を指すことが保証されます
```

### unittest のバッファリングに注意

有効になっている場合 (またはフレームワークが有効にしている場合)、出力はテスト終了まで保持されます:

* **避けるべき設定**: `unittest.main(buffer=True)` または `python -m unittest -b`
* ログが発生した時点で出力されるように、デフォルト ( `-b` なし) を使用してください。

### Git-Bash 固有のヒント

* Mintty は、プログラムが stdout を TTY ではないと認識させることがあり、それによりバッファリングが増加することがあります。最善の解決策は、上記の **`-u`/`PYTHONUNBUFFERED`** の組み合わせを適用するか、比較のために **Windows Terminal/PowerShell/CMD** から実行することです。
* サブプロセスを生成する場合、それらが環境変数を継承しない限り、同様にバッファリングします。`PYTHONUNBUFFERED=1` をエクスポートしておくと、子の Python プロセスも非バッファードで動作します。

### キューが *価値がある* 場合

**マルチプロセッシング** でのロギングを行っている場合のみ: ワーカーからメインプロセスにログを送信するために `logging.handlers.QueueHandler/QueueListener` を使用してください。そうしないと、子プロセスのバッファリングや出力の混在が問題になる可能性があります。

テストの実行方法 (コマンドと `unittest.main(...)` の引数) と、ロギング/プリントの方法を少し記載していただければ、すべての出力を即時に行うための最小限の変更を提案します。