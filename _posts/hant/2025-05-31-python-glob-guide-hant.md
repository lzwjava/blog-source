---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python Glob 模組檔案匹配指南
translated: true
type: note
---

### 導入 Glob
要在 Python 中使用 glob，請從標準函式庫中導入該模組：
```python
import glob
```

### 基本功能
`glob.glob()` 函數接受一個模式字串，並返回符合條件的檔案或目錄路徑列表。它使用 Unix shell 風格的萬用字元：

- `*`：匹配任意字符序列（路徑分隔符除外）。
- `?`：匹配任意單個字符。
- `[seq]`：匹配 seq 中的任意字符（例如 `[0-9]` 匹配數字）。
- `**`：遞歸匹配目錄（需設定 `recursive=True`）。

除非指定絕對路徑，否則模式會相對於當前目錄進行匹配。

### 使用範例

#### 1. 尋找當前目錄中的所有 .txt 檔案
```python
import glob

files = glob.glob("*.txt")
print(files)  # 輸出：['file1.txt', 'file2.txt', ...]
```

#### 2. 在子目錄中尋找特定副檔名的檔案
```python
files = glob.glob("documents/*.pdf")
print(files)  # 輸出：['documents/doc1.pdf', ...]
```

#### 3. 匹配特定模式（例如以 'log' 開頭並以數字結尾的檔案）
```python
files = glob.glob("log[0-9].txt")
print(files)  # 輸出：['log1.txt', 'log2.txt', ...]（如果存在此類檔案）
```

#### 4. 在子目錄中進行遞歸搜尋
使用 `**` 並設定 `recursive=True` 來搜尋目錄及其子目錄：
```python
files = glob.glob("**/*.py", recursive=True)
print(files)  # 輸出：['script1.py', 'subdir/script2.py', ...]
```

### 重要注意事項
- 預設情況下結果未排序；如需排序可使用 `sorted()`：`sorted(glob.glob("*.txt"))`。
- 在區分大小寫的檔案系統上進行不區分大小寫的匹配時，可考慮結合使用 `fnmatch` 或在程式碼中處理，因為 glob 是區分大小寫的。
- Glob 不會跟隨符號連結，除非明確處理；對於更複雜的遍歷，請使用 `os.walk()`。
- 如需逐個匹配，可使用 `glob.iglob()`，它返回一個迭代器以在大量結果時節省記憶體：`for file in glob.iglob("*.txt"): print(file)`。

以上涵蓋了基本要點；更多詳細資訊請參閱 [Python 官方文件](https://docs.python.org/3/library/glob.html)。