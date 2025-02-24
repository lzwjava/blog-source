---
audio: false
lang: hant
layout: post
title: 分析 Java 依賴
translated: true
---

以下是一個 Python 腳本，它會掃描項目中的所有 `.java` 文件，根據導入語句分析它們的依賴關係，並以 DOT 格式輸出依賴圖作為「依賴文本」。這個腳本專注於項目內部類之間的依賴關係，提供一個可以使用 Graphviz 等工具可視化的清晰表示。

### 腳本概述
腳本：
1. **掃描項目目錄** 遞歸地查找所有 `.java` 文件。
2. **分析依賴關係** 從每個 `.java` 文件中提取包聲明和導入語句。
3. **輸出依賴文本** 以 DOT 格式顯示項目內部一個類導入另一個類之間的有向邊。

以下是完整的腳本：

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    從 .java 文件中提取包名。

    Args:
        file_path (str): .java 文件的路徑。

    Returns:
        str: 包名，如果未找到則返回 None。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"警告：無法讀取 {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    從 .java 文件中提取特定類的導入語句，排除通配符導入。

    Args:
        file_path (str): .java 文件的路徑。

    Returns:
        list: 完全限定的導入類名列表。
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # 排除通配符導入（例如，import java.util.*;）
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"警告：無法讀取 {file_path}: {e}")
    return imports

if __name__ == '__main__':
    # 檢查命令行參數
    if len(sys.argv) != 2:
        print("用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # 第一次遍歷：收集項目中的所有完全限定類名
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # 存儲依賴關係：類 -> 它依賴的類集合
    dependencies = defaultdict(set)

    # 第二次遍歷：根據特定導入分析依賴關係
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # 只包括項目內部類的依賴關係
                        # 排除自依賴
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # 以 DOT 格式輸出依賴圖
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### 運行方式
#### 1. **命令行輸入**
- 腳本期望一個參數：Java 項目的根目錄。
- 使用範例：`python script.py /path/to/project`
- 如果沒有提供參數，則打印使用說明並退出。

#### 2. **查找 `.java` 文件**
- 使用 `os.walk()` 遞歸遍歷指定目錄並識別所有以 `.java` 結尾的文件。

#### 3. **提取類信息**
- **包提取**：`get_package` 函數讀取每個 `.java` 文件並使用正則表達式（`^\s*package\s+([\w.]+);`）查找包聲明（例如，`package com.mycompany.myproject;`）。
  - 如果未找到包或文件無法讀取，則返回 `None`。
- **類名**：假設類名與文件名匹配（例如，`MyClass.java` 定義 `MyClass`）。
- **完全限定名**：組合包和類名（例如，`com.mycompany.myproject.MyClass`）。

#### 4. **收集所有類**
- 在第一次遍歷中，構建項目中所有完全限定類名的集合，以便後續快速查找。

#### 5. **分析依賴關係**
- **導入提取**：`get_specific_imports` 函數使用正則表達式（`^\s*import\s+([\w.]+);`）提取導入語句，排除通配符導入（例如，`import java.util.*;`）。
  - 例如：從 `import com.mycompany.myproject.utils.Helper;` 中提取 `com.mycompany.myproject.utils.Helper`。
- **依賴映射**：對於每個 `.java` 文件：
  - 获取其完全限定類名。
  - 檢查其特定導入。
  - 如果導入的類在項目的類集合中且不是該類本身，則添加依賴。

#### 6. **輸出依賴文本**
- 以 DOT 格式輸出有向圖：
  - 以 `digraph G {` 開始。
  - 對於每個有依賴的類，打印邊如 `"ClassA" -> "ClassB";`。
  - 以 `}` 結束。
- 類和依賴按字母順序排序以保持輸出一致。
- 範例輸出：
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### 使用範例
1. 將腳本保存為 `analyze_deps.py`。
2. 運行它：
   ```bash
   python analyze_deps.py /path/to/java/project
   ```
3. 將輸出重定向到文件：
   ```bash
   python analyze_deps.py /path/to/java/project > dependencies.dot
   ```
4. 使用 Graphviz 可視化：
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   這將生成一個顯示依賴圖的 PNG 圖像。

### 假設和限制
- **每個文件一個公共類**：假設每個 `.java` 文件包含一個以文件命名的公共類，符合 Java 規範。
- **基於導入的依賴**：僅考慮特定導入語句（例如，`import com.example.SomeClass;`）指示的依賴，忽略通配符導入（`import com.example.*;`）和同包參考（不需要導入）。
- **內部關注**：僅跟蹤項目內部類之間的依賴，忽略外部庫。
- **基本解析**：使用正則表達式以簡化，可能會遺漏邊緣情況（例如，導入在註釋中）。完整的 Java 解析器將更加健壯但複雜。

### 自定義
- **輸出格式**：修改打印語句以更改依賴文本格式（例如，普通列表而不是 DOT）。
- **錯誤處理**：使用 try-except 塊增強，以優雅地跳過無法讀取的文件。
- **範圍**：可以擴展以包括外部依賴或同包依賴，進行更深入的代碼分析。

這個腳本提供了一個實用的依賴分析起點，適合通過其內部類關係了解 Java 項目的結構。