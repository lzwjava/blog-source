---
audio: false
generated: true
lang: hant
layout: post
title: Python 模組導入錯誤
translated: true
type: note
---

### 解答

當你使用以下指令執行 Python 腳本時：

```bash
lzwjava@anonymous lzwjava.github.io % python scripts/nytimes/nytimes.py
```

你遇到了以下錯誤：

```
Traceback (most recent call last):
  File "/Users/lzwjava/projects/lzwjava.github.io/scripts/nytimes/nytimes.py", line 5, in <module>
    from ..llm.test_mistral import call_mistral_api
ImportError: attempted relative import with no known parent package
```

這個錯誤的發生原因在於你執行腳本的方式以及 Python 處理相對導入（relative import）的方式。讓我們來分析問題並提供解決方案。

---

#### 問題理解

錯誤 `ImportError: attempted relative import with no known parent package` 的出現，是因為你在一個 Python 無法識別為套件（package）一部分的腳本中使用了**相對導入**（例如 `from ..llm.test_mistral import call_mistral_api`）。在 Python 中：

- **相對導入**使用點記法（例如 `..`）來導入相對於當前模組在套件層級結構中位置的模組。此處的 `..llm.test_mistral` 意為「從當前模組向上兩層，然後進入 `llm` 套件，並從 `test_mistral` 導入 `call_mistral_api`」。
- 當你直接使用 `python scripts/nytimes/nytimes.py` 執行腳本時，Python 會將其視為**主模組**（`__name__ = "__main__"`）並且不會為其分配套件上下文。沒有套件上下文，Python 就無法解析相對導入，因為它不知道「父套件」是什麼。

在你的情況中：
- 腳本 `nytimes.py` 位於 `/Users/lzwjava/projects/lzwjava.github.io/scripts/nytimes/nytimes.py`。
- 相對導入 `from ..llm.test_mistral import call_mistral_api` 暗示了如下的目錄結構：

```
lzwjava.github.io/
    scripts/
        nytimes/
            nytimes.py
        llm/
            test_mistral.py
```

- 然而，由於你直接執行 `nytimes.py`，Python 並未將 `scripts` 或 `nytimes` 識別為套件，導致導入失敗。

---

#### 解決方案

要修復這個問題，你需要使用 Python 的 `-m` 標誌，將腳本作為其套件結構內的一個模組來執行。這樣可以保留套件層級結構，並讓相對導入正常運作。方法如下：

1. **導航至 `scripts` 的父目錄**：
   - 根據你的指令，你已經在包含 `scripts` 資料夾的 `lzwjava.github.io` 目錄中。

2. **使用 `-m` 標誌執行腳本**：
   - 使用以下指令：

   ```bash
   python -m scripts.nytimes.nytimes
   ```

   - **解釋**：
     - `scripts.nytimes.nytimes` 指的是 `scripts` 套件內 `nytimes` 子套件中的 `nytimes.py` 模組。
     - `-m` 標誌告訴 Python 在維持其套件上下文的情況下，將指定的模組作為腳本執行。
     - 這使得相對導入 `from ..llm.test_mistral import call_mistral_api` 能夠正確解析到 `scripts.llm.test_mistral`。

---

#### 必要條件

為了讓此解決方案生效，你的目錄結構應該如下所示：

```
lzwjava.github.io/
    scripts/
        __init__.py       # 將 'scripts' 標記為套件
        nytimes/
            __init__.py   # 將 'nytimes' 標記為子套件
            nytimes.py    # 你的腳本
        llm/
            __init__.py   # 將 'llm' 標記為子套件
            test_mistral.py  # 包含 call_mistral_api
```

- **`__init__.py` 檔案**：這些檔案（可以是空的）是 Python 中將目錄定義為套件所必需的。如果缺少任何一個，請添加它們：
  - 建立一個空的 `scripts/__init__.py`
  - 建立一個空的 `scripts/nytimes/__init__.py`
  - 建立一個空的 `scripts/llm/__init__.py`

如果這些檔案已經存在，那麼指令 `python -m scripts.nytimes.nytimes` 應該能解決問題。

---

#### 原始指令失敗的原因

當你執行：

```bash
python scripts/nytimes/nytimes.py
```

- Python 將 `nytimes.py` 作為獨立腳本執行。
- 目錄 `scripts/nytimes`（`nytimes.py` 所在位置）被添加到 `sys.path` 中，但 `scripts` 本身並未被視為一個套件。
- 因此，相對導入 `from ..llm.test_mistral` 失敗，因為 Python 沒有套件層級結構可供導航。

使用 `python -m` 可以通過在 `scripts` 套件結構內明確執行腳本來解決這個問題。

---

#### 替代解決方法（不推薦）

如果由於某些原因你無法使用 `-m` 標誌，你可以通過調整 Python 路徑來修改 `nytimes.py`，使其使用**絕對導入**。在 `nytimes.py` 的頂部添加以下程式碼：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from scripts.llm.test_mistral import call_mistral_api
```

- 這會將 `lzwjava.github.io` 添加到 `sys.path` 中，從而讓絕對導入能夠運作。
- **缺點**：與使用 `-m`（Python 中處理套件的標準方式）相比，這種方法可移植性較差，被認為是一種取巧的方式。

---

#### 代理設定註記

你的輸出包含了：

```
🚀 **Proxy Settings Detected:**
   - HTTP_PROXY: http://127.0.0.1:7890
   - HTTPS_PROXY: http://127.0.0.1:7890
```

這表示你的腳本或其使用的某個函式庫偵測到了代理設定，可能是用於 HTTP 請求。這與導入錯誤無關，目前可以暫時忽略。一旦導入問題解決，腳本應該會繼續執行到任何與網路相關的程式碼。

---

#### 最終步驟

1. **嘗試解決方案**：
   - 從 `lzwjava.github.io` 目錄執行：
     ```bash
     python -m scripts.nytimes.nytimes
     ```

2. **如果仍然失敗**：
   - 檢查 `scripts`、`nytimes` 和 `llm` 目錄中是否缺少 `__init__.py` 檔案，並在必要時添加它們。
   - 確認 `test_mistral.py` 檔案存在於 `scripts/llm/` 目錄中，並且包含 `call_mistral_api` 函式。

這應該能解決 `ImportError` 並讓你的腳本成功執行。