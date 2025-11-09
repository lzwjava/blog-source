---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 解決單元測試中的Python輸出緩衝問題
translated: true
type: note
---

是的 — 這種延遲幾乎總是**輸出緩衝**造成的，而在 Windows 上使用 Git-Bash/mintty 會讓這種情況更加明顯。除非你正在進行多進程日誌記錄，否則不需要使用佇列；首先讓 stdout/stderr 取消緩衝，並避開 unittest 自身的緩衝機制。

### 執行時請這樣做

```bash
# PowerShell / CMD：
py -3.11 -u -m unittest -v

# Git-Bash：
PYTHONUNBUFFERED=1 py -3.11 -u -m unittest -v
# 或
PYTHONUNBUFFERED=1 python -u -m unittest -v
```

* `-u` = 取消 stdio 緩衝
* `PYTHONUNBUFFERED=1` = 效果相同，同時影響子進程

如果你直接使用 `xx.py`：

```bash
python -u xx.py -v
```

### 在程式碼內部實現即時輸出（直接替換）

將以下內容置於測試啟動程式碼（或 `if __name__ == "__main__":` 區塊）的最開頭：

```python
import os, sys
os.environ.setdefault("PYTHONUNBUFFERED", "1")

# Python 3.7+
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True, write_through=True)
    sys.stderr.reconfigure(line_buffering=True, write_through=True)

print("booting tests...", flush=True)
```

並且每當使用 `print(...)` 時，在關鍵位置添加 `flush=True`。

### 若使用 `logging` 模組

```python
import logging, sys
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True,  # 3.8+
)
# StreamHandler 會刷新每條記錄；這確保其指向 stdout
```

### 注意 unittest 的緩衝機制

如果你（或某個框架）啟用了緩衝，輸出會等到測試結束才顯示：

* **請避免**：`unittest.main(buffer=True)` 或 `python -m unittest -b`
* 使用預設值（不加 `-b`）以便日誌即時輸出。

### Git-Bash 專用提示

* Mintty 有時會讓程式誤以為 stdout 不是 TTY → 導致更多緩衝。最佳的兩種解決方案是上述的 **`-u`/`PYTHONUNBUFFERED`** 組合，或直接使用 **Windows Terminal/PowerShell/CMD** 進行對比測試。
* 如果你產生子進程，除非它們繼承了環境變數，否則也會進行緩衝。匯出 `PYTHONUNBUFFERED=1` 後，子 Python 進程會即時輸出。

### 何時值得使用佇列

僅當進行**多進程**日誌記錄時：使用 `logging.handlers.QueueHandler/QueueListener` 將日誌從工作進程傳送至主進程；否則子進程緩衝或輸出交叉問題可能會造成困擾。

如果你能提供執行測試的簡短程式碼片段（指令及任何 `unittest.main(...)` 參數）以及日誌記錄/輸出方式，我會為你量身定制實現即時輸出的最小改動方案。