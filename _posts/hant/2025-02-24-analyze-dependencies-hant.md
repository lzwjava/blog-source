---
audio: false
generated: true
lang: hant
layout: post
title: 分析 Java 依賴項
translated: true
type: note
---

為回應您的查詢，我將修改提供的 Python 腳本，以生成 Java 類別的依賴關係圖，其中依賴關係會按套件層級（"level"）進行分組。例如，若 `level=1`，套件將按頂層分組（如 "org"）；若 `level=2`，則按第二層分組（如 "org.springframework"）。這意味著在分析依賴關係前，我們會根據套件名稱的前 `level` 個部分將類別累積到群組中，而圖表將顯示這些群組之間的依賴關係，而非個別類別之間的依賴。

以下是修改後的腳本，隨後是變更說明及如何滿足您的需求。

### 修改後的腳本

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    從 .java 檔案中提取套件名稱。

    參數：
        file_path (str): .java 檔案的路徑。

    返回：
        str: 套件名稱，若未找到則返回 None。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"警告：無法讀取 {file_path}：{e}")
    return None

def get_specific_imports(file_path):
    """
    從 .java 檔案中提取特定的類別導入，排除萬用字元導入。

    參數：
        file_path (str): .java 檔案的路徑。

    返回：
        list: 完整限定的導入類別名稱清單。
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # 排除萬用字元導入（例如 import java.util.*;）
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"警告：無法讀取 {file_path}：{e}")
    return imports

def get_package_group(full_class_name, level):
    """
    根據套件名稱的前 'level' 個部分獲取套件群組。

    參數：
        full_class_name (str): 完整限定的類別名稱（例如 "org.springframework.boot.App"）。
        level (int): 要包含的套件層級數（例如，1 表示 "org"，2 表示 "org.springframework"）。

    返回：
        str: 套件群組（例如 "org" 或 "org.springframework"）。
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # 提取套件，排除類別名稱
    parts = package.split('.')
    if len(parts) <= level:
        return package  # 若套件部分數少於或等於 level，則使用完整套件
    else:
        return '.'.join(parts[:level])  # 使用前 'level' 個部分

if __name__ == '__main__':
    # 檢查命令列參數：root_directory 和 level
    if len(sys.argv) != 3:
        print("用法：python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("錯誤：level 必須為正整數")
        sys.exit(1)

    all_classes = set()

    # 第一輪遍歷：收集專案中所有完整限定的類別名稱
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # 儲存套件群組之間的依賴關係
    group_dependencies = set()

    # 第二輪遍歷：基於套件群組分析依賴關係
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    importer_group = get_package_group(full_class_name, level)
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # 僅包含專案內的依賴關係
                        # 排除自我依賴
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # 以 DOT 格式輸出依賴關係圖
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### 變更說明

1. **命令列參數**：
   - **原始**：`python script.py <root_directory>`
   - **修改後**：`python script.py <root_directory> <level>`
   - 新增對第二個參數 `level` 的支援，該參數指定套件層級。腳本會檢查是否提供了兩個參數，並確認 `level` 為正整數。

2. **新函數：`get_package_group`**：
   - 新增一個函數，用於根據指定的 `level` 計算類別的套件群組。
   - 對於完整限定的類別名稱（例如 "org.springframework.boot.App"），它會提取套件（"org.springframework.boot"），將其拆分為部分（"org"、"springframework"、"boot"），並取前 `level` 個部分：
     - 若 `level=1`：返回 "org"。
     - 若 `level=2`：返回 "org.springframework"。
     - 若套件的部分數少於 `level`（例如 "com.example" 且 `level=3`），則返回完整套件（"com.example"）。

3. **依賴關係分組**：
   - **原始**：使用 `defaultdict(set)` 儲存個別類別之間的依賴關係。
   - **修改後**：使用一個 `set`（`group_dependencies`）來儲存套件群組之間的有向邊，以元組 `(from_group, to_group)` 表示。
   - 對於每個類別：
     - 使用 `get_package_group` 計算其套件群組（`importer_group`）。
     - 對於每個在專案內（`imp in all_classes`）且非自身（`imp != full_class_name`）的特定導入：
       - 計算導入類別的套件群組（`imported_group`）。
       - 若群組不同（`imported_group != importer_group`），則將邊加入 `group_dependencies`。
   - `set` 確保唯一性，因此同一群組之間的多重依賴關係僅會產生一條邊。

4. **DOT 輸出**：
   - **原始**：列印個別類別之間的邊（例如 "org.springframework.boot.App" -> "org.apache.commons.IOUtils"）。
   - **修改後**：列印套件群組之間的邊（例如，對於 `level=2`，顯示 "org.springframework" -> "org.apache"）。
   - 邊經過排序以確保輸出的一致性。

### 如何滿足您的需求

- **支援層級**：腳本現在接受 `level` 參數，在分析依賴關係前將套件分組。
- **Level = 1**：將所有類別按其頂層套件分組（例如 "org"）。例如，"org.springframework.boot.App" 和 "org.apache.commons.IOUtils" 都屬於 "org" 群組，因此它們在 "org" 內的導入不會顯示為邊。
- **Level = 2**：將類別按前兩個套件層級分組（例如 "org.springframework"）。例如，從 "org.springframework.boot.App" 導入 "org.apache.commons.IOUtils" 會建立一條從 "org.springframework" 到 "org.apache" 的邊。
- **在依賴分析前累積套件**：腳本在分析導入前，根據 `level` 確定每個類別的套件群組，確保依賴關係是群組之間而非個別類別之間的。
- **範例符合性**：對於您的範例邊：
  - 原始：`"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - 使用 `level=2`：兩個類別都在 "org.springframework" 中，因此不添加邊（同一群組）。
  - 使用 `level=3`："org.springframework.boot.web" -> "org.springframework.boot.convert"，在這些不同群組之間添加一條邊。

### 使用範例

- **命令**：`python script.py /path/to/project 1`
  - 群組："org"、"com" 等。
  - 輸出可能包含：`"org" -> "com"`（若 "org" 套件中的類別導入 "com" 套件中的類別）。

- **命令**：`python script.py /path/to/project 2`
  - 群組："org.springframework"、"org.apache" 等。
  - 輸出可能包含：`"org.springframework" -> "org.apache"`。

### 注意事項

- 腳本保持原始行為，僅包含專案內的依賴關係（`all_classes` 內的導入），並排除萬用字元導入和自我依賴。
- 未包含套件宣告的類別將被跳過，與原始腳本一致。
- 輸出為 DOT 格式的有向圖，可使用 Graphviz 等工具查看。

此修改後的腳本應能完全滿足您按套件層級層次結構分組依賴關係的需求。