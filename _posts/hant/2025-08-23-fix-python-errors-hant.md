---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 輕鬆修復 Python 未發現錯誤
translated: true
type: note
---

是的 — 出現 `"python not found"` 錯誤是因為你的登入 Shell 可能與你平時輸入 `python` 的互動式 Shell 具有不同的 `PATH` 環境變數。當你呼叫 `subprocess.run(..., shell=True)` 時，如果 `python` 不在 `$PATH` 中，或者你的系統只有 `python3`，子 Shell 就可能找不到 `python`。

以下是可靠的解決方法：

---

### 1. 使用 `sys.executable`

不要依賴系統找到 `python`，而是始終呼叫當前運行的 Python 直譯器：

```python
import os
import subprocess
import platform
import sys

def gpa():
    python_exec = sys.executable  # 當前 Python 直譯器的完整路徑

    system = platform.system()
    if system == "Linux":
        shell_command = f"bash -l -c '{python_exec} ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    elif system == "Darwin":
        shell_command = f"zsh -l -c '{python_exec} ~/bin/gitmessageai.py --api deepseek --allow-pull-push'"
    else:  # Windows
        shell_command = f'cmd.exe /c "{python_exec} %USERPROFILE%\\bin\\gitmessageai.py --api deepseek --allow-pull-push"'

    subprocess.run(shell_command, shell=True)
```

這能保證執行你腳本的同一個 Python 也會用來執行 `gitmessageai.py`。

---

### 2. 嘗試 `python` 和 `python3`

有些系統只安裝了 `python3`。你可以檢測可用性：

```python
import shutil

python_exec = shutil.which("python") or shutil.which("python3")
```

然後將其代入你的命令字串中。

---

### 3. 直接指定已知路徑

如果你知道絕對路徑（例如 `/usr/bin/python3` 或 `/opt/homebrew/bin/python3`），可以直接在命令中使用。

---

👉 最穩健的解決方案是**選項 1（使用 `sys.executable`）**，因為它使用已在執行你腳本的直譯器。這樣你就不再需要依賴 `$PATH`。

需要我幫你重構函數，完整整合 `sys.executable`，讓你永遠不再看到 `"python not found"` 錯誤嗎？