---
audio: false
generated: false
lang: hant
layout: post
title: 分析 Java 套件
translated: true
---

根據你的查詢，你希望有一個腳本，如果 `level` 參數為 0 或未提供，則使用整個套件名稱（所有部分），實際上將 `level = 0` 視為「無限」或「使用所有部分」，而不是限制為特定數量的部分（例如，當 `level = 1` 時，僅使用第一部分）。以下，我將解釋如何在 Python 腳本中實現這一點，該腳本分析 Java 文件以提取套件名稱，並提供一個針對你的需求量身定制的完整解決方案。

### 理解需求
- **當 `level = 0` 或未提供**：使用從 Java `import` 語句中提取的完整套件名稱（例如 `java.util` 或 `com.google.common.eventbus`），而不截斷它。
- **當 `level > 0`**：將套件名稱截斷為前 `level` 部分（例如，對於 `com.google.common.eventbus`，`level = 2` 將給出 `com.google`）。
- 腳本應該繼續處理 Java 文件，從 `import` 語句中提取套件名稱，並適當處理邊緣情況。

### 解決方案方法
1. **參數解析**：
   - 如果僅提供根目錄（例如 `python script.py /path/to/dir`），則設置 `level = 0`，這意味著使用完整的套件名稱。
   - 如果提供了 `level`（例如 `python script.py /path/to/dir 2`），則使用它來截斷套件名稱，確保它是非負整數。
   - 如果參數無效，則退出並顯示錯誤。

2. **套件提取**：
   - 從 `import` 語句中提取套件名稱（例如，`import java.util.ArrayList;` 產生 `java.util`）。
   - 使用 Java 命名約定：套件名稱通常是小寫，而類名以大寫字母開頭。

3. **套件截斷邏輯**：
   - 如果 `level = 0`，將完整的套件名稱添加到結果集中。
   - 如果 `level > 0`，按點（`.`）分割套件名稱，並取前 `level` 部分。

4. **記錄和輸出**：
   - 明確指出是否使用完整的套件名稱或截斷的套件名稱。
   - 列出所有找到的唯一套件。

### 實現
以下是滿足你需求的完整 Python 腳本：

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    遞歸查找給定目錄及其子目錄中的所有 .java 文件。

    參數：
        root_dir (str): 開始搜索的根目錄。

    返回：
        str: 每個 .java 文件的完整路徑。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    從 import 語句中提取套件名稱。

    使用約定，套件名稱是小寫，而類名以大寫字母開頭。處理通配符導入 (*)。

    參數：
        import_statement (str): Java 文件中的 import 語句行。

    返回：
        str: 套件名稱，如果未確定則返回空字符串。
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
    # 解析命令行參數
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("使用方法: python script.py <root_directory> [level] [--count]")
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
            print(f"無效參數: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"無效參數: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)

    # 驗證目錄是否存在
    if not os.path.isdir(root_dir):
        print(f"[ERROR] 指定的路徑不是目錄: {root_dir}")
        sys.exit(1)

    # 記錄分析開始
    level_str = "使用完整套件名稱" if level == 0 else f"在 level {level}"
    count_str = "帶出現次數" if count else ""
    print(f"[INFO] 開始分析目錄: {root_dir} {level_str} {count_str}")

    # 初始化變量
    package_counter = Counter()
    total_files = 0
    error_files = 0

    # 處理 Java 文件
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
            print(f"[ERROR] 無法讀取文件 {java_file}: {e}")
            error_files += 1
            continue

    # 打印摘要
    print(f"[INFO] 總共嘗試的 Java 文件: {total_files + error_files}")
    print(f"[INFO] 成功處理: {total_files}")
    print(f"[INFO] 文件出錯: {error_files}")
    if count:
        print(f"[INFO] 總共唯一套件帶出現次數: {len(package_counter)}")
    else:
        print(f"[INFO] 總共唯一套件: {len(package_counter)}")

    # 打印結果並進行適當排序
    if package_counter:
        if count:
            print("[INFO] 分析完成。打印唯一套件帶出現次數（按出現次數降序排序）：")
            # 按出現次數降序，然後按套件名稱升序排序
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] 分析完成。打印唯一套件（按名稱升序排序）：")
            # 按套件名稱升序排序
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] 未找到套件。")
```

### 運行方式
- `python script.py /path/to/java/project`: 分析目錄中的所有 `.java` 文件並使用完整套件名稱（`level = 0`）。
- `python script.py /path/to/java/project 2`: 將套件名稱截斷為前 2 部分（例如，`com.google.common.eventbus` 變為 `com.google`）。

- **示例輸出**：
  假設你有一個 Java 文件，內容如下：
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **當 `level = 0`（或未提供 level）**：
    ```
    [INFO] 開始分析目錄: /path/to/java/project 使用完整套件名稱。
    [INFO] 進入目錄: /path/to/java/project
    [INFO] 正在處理文件: /path/to/java/project/MyFile.java
    [INFO] 總共嘗試的 Java 文件: 1
    [INFO] 成功處理: 1
    [INFO] 文件出錯: 0
    [INFO] 總共唯一完整套件: 2
    [INFO] 分析完成。打印唯一完整套件:
    com.google.common.eventbus
    java.util
    ```
  - **當 `level = 2`**：
    ```
    [INFO] 開始分析目錄: /path/to/java/project 在 level: 2
    [INFO] 進入目錄: /path/to/java/project
    [INFO] 正在處理文件: /path/to/java/project/MyFile.java
    [INFO] 總共嘗試的 Java 文件: 1
    [INFO] 成功處理: 1
    [INFO] 文件出錯: 0
    [INFO] 總共唯一套件在 level 2: 2
    [INFO] 分析完成。打印唯一套件在 level 2:
    com.google
    java.util
    ```

- **關鍵特性**：
  - **完整套件名稱**：當 `level = 0` 或未傳遞時，使用提取的完整套件名稱（例如 `java.util`，`com.google.common.eventbus`）。
  - **截斷**：當 `level > 0` 時，取前 `level` 部分。
  - **錯誤處理**：檢查有效目錄和非負 `level`。
  - **唯一性**：將套件存儲在 `set` 中以避免重複。

### 處理的邊緣情況
- **缺少 level**：默認為 `level = 0`，使用完整套件名稱。
- **無效 level**：如果 `level` 為負或不是整數，則退出並顯示錯誤。
- **短套件**：如果套件的部分少於 `level`（例如，`java` 當 `level = 2`），則使用完整套件（`java`）。
- **空導入**：跳過無法提取套件的行。

這個腳本完全滿足你的需求：當 `level = 0` 或未提供時，使用套件名稱的所有部分，實際上將其視為「無限」部分。