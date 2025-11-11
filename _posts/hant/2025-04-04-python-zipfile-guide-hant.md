---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python ZipFile 套件指南
translated: true
type: note
---

### ZipFile 套件概覽
Python 的 `zipfile` 模組讓你能夠讀取和寫入 ZIP 壓縮檔，無需使用外部工具。它屬於標準函式庫的一部分，因此不需要額外安裝（從 Python 2.3+ 開始）。你可以透過它來程式化地壓縮、解壓縮或操作 ZIP 檔案。它支援多種壓縮方法，例如 DEFLATE。

導入方式：`import zipfile`

### 讀取 ZIP 檔案
要解壓縮或檢查現有的 ZIP 檔案：

1. **開啟 ZIP 檔案進行讀取**：
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' 代表讀取模式
   ```

2. **列出內容**：
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # 回傳檔案名稱列表
       print(file_list)
   ```

3. **解壓縮檔案**：
   - 解壓縮全部：`zip_ref.extractall('destination_folder')`
   - 解壓縮單一檔案：`zip_ref.extract('file_inside.zip', 'path')`

4. **讀取檔案內容而不解壓縮**：
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('file_inside.zip') as file:
           content = file.read()
           print(content.decode())  # 如果是文字檔案
   ```

注意：請始終使用 `with` 以自動關閉檔案。對於受密碼保護的 ZIP 檔案，請在 `ZipFile()` 中加入 `pwd=b'password'`。

### 寫入 ZIP 檔案
要建立新的 ZIP 檔案或添加到現有的 ZIP 檔案：

1. **建立新的 ZIP 檔案**：
   ```python
   with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
       # 'w' 代表寫入模式（如果檔案已存在則覆寫）
   ```

2. **添加檔案**：
   - 添加單一檔案：`zip_ref.write('source_file.txt', 'arcname.txt')`（可選的 arcname 參數可在壓縮檔內重新命名）
   - 添加多個檔案：遍歷檔案列表並呼叫 `write()`。

3. **寫入時壓縮**（預設為 DEFLATE）：
   ```python
   with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('large_file.txt')
   ```
   選項：`ZIP_STORED`（無壓縮）、`ZIP_DEFLATED`、`ZIP_BZIP2` 等。

4. **附加到現有 ZIP 檔案**（使用 'a' 模式而非 'w'）。

### 常見操作與提示
- **檢查檔案是否為有效的 ZIP**：使用 `zipfile.is_zipfile('file.zip')`。
- **取得檔案資訊**：`zip_ref.getinfo('file.txt')` 回傳 ZipInfo 物件，包含詳細資訊如大小、日期。
- **處理大型檔案**：讀取/解壓縮大型檔案可能消耗記憶體；使用 `open()` 方法進行串流處理。
- **錯誤處理**：捕捉 `BadZipFile` 或 `LargeZipFile` 例外。
- **跨平台**：可在 Windows、macOS、Linux 上運行，但需注意路徑分隔符號（使用 `/`）。
- **加密**：支援基本密碼保護，但強度較弱 — 如需更高安全性請使用更強大的工具。
- **更高層級**：如需更多功能（例如 shutil 整合），可結合 `shutil.make_archive()` 來建立 ZIP 檔案。

完整腳本範例，用於壓縮資料夾：
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('my_folder', 'output.zip')
```

如需完整文件，請查閱 [官方 Python 文件](https://docs.python.org/3/library/zipfile.html)。如果你有特定任務（例如「如何解壓縮到記憶體」），請提供更多細節！