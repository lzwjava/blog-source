---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python 套件導入提取器
translated: true
type: note
---

### Python 腳本：擷取所有導入的套件

此腳本會遍歷指定目錄及其子目錄，找出所有 Python 檔案（`.py`），並使用 Python 的 `ast` 模組（用於安全且語法感知的解析）解析其導入語句，累積所有獨特的基礎模組名稱（例如從 `import os` 中取得 `os`，或從 `from collections import defaultdict` 中取得 `collections`）。它會忽略內建模組，專注於外部模組。

將此腳本儲存為 `.py` 檔案（例如 `extract_imports.py`），並以目錄路徑作為參數執行，例如 `python extract_imports.py /path/to/directory`。

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    解析 Python 檔案並擷取導入的模組名稱。
    處理 'import mod' 和 'from mod import item' 兩種形式。
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # 取得基礎模組（例如 'import os.path' -> 'os'）
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # 從 'from mod.sub import ...' 取得基礎模組
    except Exception as e:
        print(f"解析 {file_path} 時發生錯誤：{e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    遍歷目錄及子目錄，收集所有獨特的導入模組。
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # 排除常見內建模組（可選，因為它們很少是外部套件）
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法：python extract_imports.py <目錄路徑>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"錯誤：{directory} 不是有效的目錄。")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("所有獨特的導入套件：")
    for mod in modules:
        print(mod)
```

### 運作原理
- **目錄遍歷**：使用 `os.walk` 遞迴訪問所有子目錄和檔案。
- **檔案篩選**：僅處理 `.py` 檔案。
- **導入解析**：使用 `ast` 安全解析原始碼，識別 `Import` 和 `ImportFrom` 節點。透過 `.` 分割以捕獲頂層模組（例如從 `import numpy.linalg` 中取得 `numpy`）。
- **累積收集**：將模組收集到集合中以確保唯一性，然後排序並輸出。
- **邊界情況處理**：跳過內建模組（可自定義 `excluded` 集合）、優雅處理語法錯誤，並支援 Unicode 檔案。
- **輸出結果**：排序後的獨特套件名稱列表。如果在您自己的專案目錄中執行，它將列出您需要安裝的套件，例如 `requests`、`pandas` 等。

此方法對於程式碼庫分析非常高效，且避免執行可能不安全的程式碼。如果您需要改進（例如以不同方式處理相對導入或生成 requirements.txt），請提供更多詳細資訊！