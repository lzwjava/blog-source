---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python tarfile 模組使用指南
translated: true
type: note
---

### 匯入 tarfile 模組
要在 Python 中使用 `tarfile` 函式庫，首先需匯入它：
```python
import tarfile
```
此模組是 Python 標準函式庫的一部分，無需額外安裝。它基於 POSIX tar 格式，支援讀取和寫入壓縮或未壓縮的 tar 歸檔文件。

### 開啟與建立 Tar 歸檔文件
- **開啟現有 tar 檔案**：使用 `tarfile.open()` 並指定模式。模式包括 `'r'`（讀取）、`'w'`（寫入空檔案）、`'a'`（追加），或帶壓縮的變體如 `'r:gz'` 用於 gzip。
  ```python
  import tarfile
  
  # 開啟讀取（未壓縮）
  with tarfile.open('example.tar', 'r') as tar:
      # 在此處操作 tar
      pass
  ```
- **建立新 tar 檔案**：使用 `'w'` 模式建立空歸檔。可添加壓縮前綴如 `'w:gz'` 用於 gzip 或 `'w:bz2'` 用於 bzip2。
  ```python
  # 建立壓縮的 tar.gz 檔案
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      pass
  ```

### 將檔案加入歸檔
- **加入單一檔案**：在 tar 檔案物件上呼叫 `add()`，傳入檔案路徑。可指定 arcname 以在歸檔內使用不同名稱。
  ```python
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      tar.add('file.txt')  # 原樣加入 file.txt
      tar.add('data.csv', arcname='renamed_data.csv')  # 在歸檔內重新命名
  ```
- **加入多個檔案或目錄**：在迴圈中使用 `add()` 或遞迴加入整個目錄。
  ```python
  import os
  
  with tarfile.open('backup.tar', 'w') as tar:
      for root, dirs, files in os.walk('my_folder'):
          for file in files:
              tar.add(os.path.join(root, file))
  ```

### 從歸檔中提取檔案
- **提取所有檔案**：使用 `extractall()` 提取到指定目錄（預設為當前目錄）。
  ```python
  with tarfile.open('archive.tar.gz', 'r:gz') as tar:
      tar.extractall(path='extracted_folder')  # 需要時建立資料夾
  ```
- **提取特定檔案**：先使用 `getmembers()` 列出成員，再使用 `extract()`。
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      members = tar.getmembers()
      for member in members:
          if 'important' in member.name:  # 範例篩選條件
              tar.extract(member, path='output_dir')
  ```
- 注意：為安全起見，請過濾路徑（例如避免 `..`）以防範路徑遍歷攻擊。`tarfile` 會進行部分檢查，但對於不受信任的歸檔建議手動過濾。

### 列出歸檔內容
- **迭代檔案列表**：使用 `getmembers()` 或直接迭代 tar 物件以獲取 TarInfo 物件。
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      for member in tar.getmembers():
          print(f"{member.name}: {member.size} bytes")
  ```

### 主要模式與壓縮格式
- `'r'`：讀取未壓縮 tar
- `'r:gz'`、`'r:bz2'`、`'r:xz'`：讀取壓縮格式
- `'w'`：寫入新未壓縮 tar（覆蓋現有）
- `'a'`：追加至現有 tar
- 讀取時自動檢測壓縮格式；寫入時需明確指定

### 技巧與最佳實踐
- 始終使用情境管理器（`with` 語句）以確保檔案正確關閉
- 對於大型歸檔，建議進行篩選或選擇性提取以節省記憶體
- `tarfile` 不直接處理加密歸檔——如需此功能請使用外部工具或手動結合 `gzip`
- 錯誤處理：捕獲 `tarfile.TarError` 以處理歸檔問題
- 完整文件：請參閱 Python 官方 [tarfile 文件](https://docs.python.org/3/library/tarfile.html) 了解進階功能（如自訂篩選器）