---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Pyperclip：Python 剪貼簿管理指南
translated: true
type: note
---

### 什麼是 Pyperclip？
Pyperclip 是一個輕量級的 Python 函式庫，用於存取和操作系統剪貼簿（複製貼上功能）。它支援跨平台（Windows、macOS、Linux）操作，能夠將文字複製到剪貼簿，並從剪貼簿貼上文字。請注意：它僅處理文字；如需處理檔案或圖像，請使用其他函式庫。

### 安裝
透過 pip 安裝 Pyperclip：
```
pip install pyperclip
```

在 Linux 系統上，您可能需要額外的依賴項才能存取剪貼簿（例如 `xclip` 或 `xsel`）。請使用您的套件管理器安裝（例如在 Ubuntu 上使用 `sudo apt-get install xclip`）。

### 基本用法
1. **匯入函式庫**：
   ```python
   import pyperclip
   ```

2. **將文字複製到剪貼簿**：
   ```python
   pyperclip.copy("Hello, world!")
   ```
   這會將字串 "Hello, world!" 放入剪貼簿。

3. **從剪貼簿貼上文字**：
   ```python
   text = pyperclip.paste()
   print(text)  # 輸出當前剪貼簿內容
   ```
   這會擷取並列印剪貼簿中的文字。

### 範例：將使用者輸入複製到剪貼簿
```python
import pyperclip

user_input = input("請輸入要複製的文字：")
pyperclip.copy(user_input)
print("文字已複製到剪貼簿！")
```

### 範例：貼上並修改
```python
import pyperclip

pyperclip.copy("原始文字")
modified = pyperclip.paste().upper()  # 貼上後修改（例如轉為大寫）
pyperclip.copy(modified)
print("已複製修改後的文字。")
```

### 額外提示
- **錯誤處理**：在某些系統上（例如無頭伺服器或特定 Linux 發行版），剪貼簿存取可能會失敗。請使用 try-except 包裝：
  ```python
  try:
      pyperclip.copy("text")
  except pyperclip.PyperclipException as e:
      print(f"剪貼簿錯誤：{e}")
  ```
- **檢查可用性**：在腳本執行後立即使用 `pyperclip.paste()`，因為剪貼簿內容會在多次執行之間保留。
- **限制**：不適用於二進位資料；僅支援文字。進階用法請參閱[官方文件](https://github.com/asweigart/pyperclip)。

以上涵蓋了基本知識——先從複製和貼上簡單字串開始測試。若遇到平台特定問題，請查閱該函式庫的 GitHub 儲存庫。