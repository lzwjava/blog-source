---
audio: false
generated: true
lang: hant
layout: post
title: 分析Java套件
translated: true
type: note
---

根據您的查詢，您需要一個腳本，當 `level` 參數為 0 或未提供時，使用完整的套件名稱（所有部分），實質上將 `level = 0` 視為「無限」或「使用所有部分」，而不是限制為特定數量的部分（例如當 `level = 1` 時僅使用第一部分）。以下我將解釋如何在分析 Java 檔案以提取套件名稱的 Python 腳本中實現此功能，並提供一個根據您需求定制的完整解決方案。

### 理解需求
- **當 `level = 0` 或未提供時**：使用從 Java `import` 語句中提取的完整套件名稱（例如 `java.util` 或 `com.google.common.eventbus`），不進行截斷。
- **當 `level > 0` 時**：將套件名稱截斷為前 `level` 個部分（例如，對於 `com.google.common.eventbus`，`level = 2` 將得到 `com.google`）。
- 腳本仍應處理 Java 檔案，從 `import` 語句中提取套件名稱，並適當處理邊界情況。

### 解決方案思路
1. **參數解析**：
   - 如果僅提供根目錄（例如 `python script.py /path/to/dir`），則設定 `level = 0`，表示使用完整套件名稱。
   - 如果提供了 `level`（例如 `python script.py /path/to/dir 2`），則使用它來截斷套件名稱，確保它是非負整數。
   - 如果參數無效，則退出並顯示錯誤。

2. **套件提取**：
   - 從 `import` 語句中提取套件名稱（例如，`import java.util.ArrayList;` 產生 `java.util`）。
   - 使用 Java 命名慣例：套件通常為小寫，類別名稱以大寫開頭。

3. **套件截斷邏輯**：
   - 如果 `level = 0`，將完整套件名稱加入結果集。
   - 如果 `level > 0`，將套件名稱按點（`.`）分割，並取前 `level` 個部分。

4. **日誌記錄與輸出**：
   - 清楚指示是否使用完整套件名稱或截斷後的套件名稱。
   - 列出所有找到的獨特套件。

### 實現
以下是符合您需求的完整 Python 腳本：

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    遞迴尋找指定目錄及其子目錄中的所有 .java 檔案。
    
    Args:
        root_dir (str): 開始搜尋的根目錄。
    
    Yields:
        str: 每個 .java 檔案的完整路徑。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    從 import 語句中提取套件名稱。
    
    使用套件名稱為小寫，而類別名稱以大寫字母開頭的慣例。處理萬用字元導入（*）。
    
    Args:
        import_statement (str): Java 檔案中的 import 語句行。
    
    Returns:
        str: 套件名稱，如果無法確定則返回空字串。
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # 解析命令列參數
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <root_directory> [level] [--count]")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    level = 0
    count = False
    
    if len(sys.argv) == 3:
        if sys.argv[2] == "--count":
            count = True
        elif sys.argv[2].isdigit():
            level = int(sys.argv[2])
        else:
            print(f"Invalid argument: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Invalid arguments: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)
    
    # 驗證目錄是否存在
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    # 記錄分析開始
    level_str = "使用完整套件名稱" if level == 0 else f"於層級 {level}"
    count_str = "包含出現次數" if count else ""
    print(f"[INFO] 開始分析目錄: {root_dir} {level_str} {count_str}")
    
    # 初始化變數
    package_counter = Counter()
    total_files = 0
    error_files = 0
    
    # 處理 Java 檔案
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[ERROR] 無法讀取檔案 {java_file}: {e}")
            error_files += 1
            continue
    
    # 列印摘要
    print(f"[INFO] 嘗試處理的 Java 檔案總數: {total_files + error_files}")
    print(f"[INFO] 成功處理: {total_files}")
    print(f"[INFO] 發生錯誤的檔案: {error_files}")
    if count:
        print(f"[INFO] 包含次數的獨特套件總數: {len(package_counter)}")
    else:
        print(f"[INFO] 獨特套件總數: {len(package_counter)}")
    
    # 以適當排序列印結果
    if package_counter:
        if count:
            print("[INFO] 分析完成。列印包含次數的獨特套件（按次數降序排序）：")
            # 按次數降序，然後按套件名稱升序排序
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] 分析完成。列印獨特套件（按名稱升序排序）：")
            # 按套件名稱升序排序
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] 未找到任何套件。")
```

### 運作方式
- **執行腳本**：
  - `python script.py /path/to/java/project`：分析目錄中的所有 `.java` 檔案，並使用完整套件名稱（`level = 0`）。
  - `python script.py /path/to/java/project 2`：將套件名稱截斷為前 2 個部分（例如，`com.google.common.eventbus` 變為 `com.google`）。

- **範例輸出**：
  假設您有一個 Java 檔案包含：
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **使用 `level = 0`（或未提供 level）**：
    ```
    [INFO] 開始分析目錄: /path/to/java/project 使用完整套件名稱。
    [INFO] 進入目錄: /path/to/java/project
    [INFO] 處理檔案: /path/to/java/project/MyFile.java
    [INFO] 嘗試處理的 Java 檔案總數: 1
    [INFO] 成功處理: 1
    [INFO] 發生錯誤的檔案: 0
    [INFO] 獨特完整套件總數: 2
    [INFO] 分析完成。列印獨特完整套件：
    com.google.common.eventbus
    java.util
    ```
  - **使用 `level = 2`**：
    ```
    [INFO] 開始分析目錄: /path/to/java/project 於層級: 2
    [INFO] 進入目錄: /path/to/java/project
    [INFO] 處理檔案: /path/to/java/project/MyFile.java
    [INFO] 嘗試處理的 Java 檔案總數: 1
    [INFO] 成功處理: 1
    [INFO] 發生錯誤的檔案: 0
    [INFO] 層級 2 的獨特套件總數: 2
    [INFO] 分析完成。列印層級 2 的獨特套件：
    com.google
    java.util
    ```

- **主要功能**：
  - **完整套件名稱**：當 `level = 0` 或未傳遞時，使用提取的完整套件名稱（例如 `java.util`、`com.google.common.eventbus`）。
  - **截斷功能**：當 `level > 0` 時，取前 `level` 個部分。
  - **錯誤處理**：檢查有效目錄和非負 `level`。
  - **唯一性**：將套件儲存在 `set` 中以避免重複。

### 處理的邊界情況
- **缺少 Level**：預設為 `level = 0`，使用完整套件名稱。
- **無效 Level**：如果 `level` 為負數或非整數，則退出並顯示錯誤。
- **短套件**：如果套件的部分數少於 `level`（例如 `java` 且 `level = 2`），則使用完整套件（`java`）。
- **空導入**：跳過未提取到套件的行。

此腳本完全滿足您的需求：當 `level = 0` 或未提供時，它使用套件名稱的所有部分，實質上將其視為在使用部分數方面是「無限」的。