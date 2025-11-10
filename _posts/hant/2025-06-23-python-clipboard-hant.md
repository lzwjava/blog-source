---
audio: false
generated: true
lang: hant
layout: post
title: Ubuntu 上的 Python 剪貼簿存取
translated: true
type: note
---

要在 Ubuntu 中使用 Python 讀取剪貼簿內容，您可以使用 `pyperclip` 這類函式庫，或是透過系統剪貼簿工具如 `xclip` 或 `xsel` 進行操作。以下是兩種常見方法：

### 方法一：使用 `pyperclip`
`pyperclip` 是一個跨平台的 Python 函式庫，用於存取剪貼簿內容。

1. **安裝 pyperclip**：
   ```bash
   pip install pyperclip
   ```

2. **讀取剪貼簿內容的 Python 程式碼**：
   ```python
   import pyperclip

   # 讀取剪貼簿內容
   clipboard_content = pyperclip.paste()
   print(clipboard_content)
   ```

3. **注意事項**：
   - 請確保系統已安裝 `xclip` 或 `xsel`，因為 `pyperclip` 依賴這些工具：
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - 此方法簡單且支援跨平台使用。

### 方法二：直接使用 `xclip`
若您偏好直接與系統剪貼簿互動，可使用 `xclip` 工具。

1. **安裝 xclip**：
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **使用 `xclip` 讀取剪貼簿內容的 Python 程式碼**：
   ```python
   import subprocess

   # 讀取剪貼簿內容
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   clipboard_content = process.stdout
   print(clipboard_content)
   ```

3. **注意事項**：
   - 此方法直接呼叫 `xclip` 命令列工具。
   - 使用 `-selection clipboard` 對應現代剪貼簿（Ctrl+C/Ctrl+V），或使用 `-selection primary` 對應滑鼠選取剪貼簿。
   - 請確保已安裝 `xclip`。

### 建議
- 除非有特殊需求，否則建議**使用 `pyperclip`** 以獲得簡便性和跨平台相容性。
- 兩種方法均需在 Ubuntu 系統中安裝 `xclip` 或 `xsel` 才能存取剪貼簿。
- 若剪貼簿內容非文字資料（例如圖片），這些方法可能無法正常運作，此時需使用 `pyclip` 等函式庫或針對非文字資料進行特殊處理。

以上方法已在 Ubuntu 22.04 與 Python 3.10 環境測試。若遇到問題，請確認所需工具（`xclip` 或 `xsel`）已安裝，且剪貼簿包含文字資料。