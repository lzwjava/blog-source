---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Pythonが見つからないエラーを簡単に修正
translated: true
type: note
---

はい — `"python not found"` エラーは、ログインシェルが通常 `python` を入力する対話型シェルと同じ `PATH` 環境変数を持っていない場合に発生します。`subprocess.run(..., shell=True)` を呼び出すと、サブシェルは `$PATH` 上に `python` がない場合、またはシステムに `python3` しかない場合、`python` を見つけられない可能性があります。

これを修正する確実な方法を以下に示します：

---

### 1. `sys.executable` を使用する

`python` が見つかることに依存する代わりに、常に現在実行中の Python インタープリタを呼び出します：

```python
import os
import subprocess
import platform
import sys

def gpa():
    python_exec = sys.executable  # 現在の Python インタープリタへのフルパス

    system = platform.system()
    if system == "Linux":
        shell_command = f"bash -l -c '{python_exec} ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    elif system == "Darwin":
        shell_command = f"zsh -l -c '{python_exec} ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    else:  # Windows
        shell_command = f'cmd.exe /c "{python_exec} %USERPROFILE%\\bin\\gitmessageai.py --api deepseek --allow-pull-push"'

    subprocess.run(shell_command, shell=True)
```

これにより、スクリプトの実行に使用したのと同じ Python が `gitmessageai.py` も実行することが保証されます。

---

### 2. `python` と `python3` の両方を試す

一部のシステムには `python3` しかない場合があります。可用性を検出できます：

```python
import shutil

python_exec = shutil.which("python") or shutil.which("python3")
```

そして、この値をコマンド文字列に代入します。

---

### 3. 既知のパスをハードコードする

絶対パス（例：`/usr/bin/python3` や `/opt/homebrew/bin/python3`）が分かっている場合は、それをコマンドで直接使用できます。

---

👉 最も堅牢な解決策は **オプション 1 (`sys.executable`)** です。これはスクリプトをすでに実行しているインタープリタを使用するため、`$PATH` に依存することが一切なくなります。

`"python not found"` エラーが二度と発生しないように、`sys.executable` を完全に統合してあなたの関数をリファクタリングしましょうか？