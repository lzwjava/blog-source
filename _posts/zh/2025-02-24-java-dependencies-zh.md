---
audio: true
lang: zh
layout: post
title: 分析 Java 依赖
translated: true
---

以下是一个Python脚本，它扫描项目中的所有`.java`文件，根据导入语句分析它们的依赖关系，并以DOT格式输出依赖图作为“依赖文本”。该脚本专注于项目内部类之间的依赖关系，提供了一种可以使用Graphviz等工具可视化的清晰表示。

### 脚本概述
脚本：
1. **递归扫描项目目录** 以查找所有`.java`文件。
2. **分析依赖关系** 通过从每个`.java`文件中提取包声明和导入语句。
3. **输出依赖文本** 以DOT格式显示项目内部一个类导入另一个类的有向边。

以下是完整的脚本：

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    从 .java 文件中提取包名。

    参数:
        file_path (str): .java 文件的路径。

    返回:
        str: 包名，如果未找到则返回 None。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"警告：无法读取 {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    从 .java 文件中提取特定的类导入，排除通配符导入。

    参数:
        file_path (str): .java 文件的路径。

    返回:
        list: 完全限定的导入类名列表。
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # 排除通配符导入（例如，import java.util.*;）
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"警告：无法读取 {file_path}: {e}")
    return imports

if __name__ == '__main__':
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # 第一遍：收集项目中所有完全限定的类名
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # 存储依赖关系：类 -> 它依赖的类集合
    dependencies = defaultdict(set)

    # 第二遍：基于特定导入分析依赖关系
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
                        # 仅包括项目内部类的依赖关系
                        # 排除自依赖
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # 以DOT格式输出依赖图
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### 使用方法
#### 1. **命令行输入**
- 脚本期望一个参数：Java项目的根目录。
- 示例用法：`python script.py /path/to/project`
- 如果没有提供参数，则打印使用说明并退出。

#### 2. **查找 `.java` 文件**
- 使用 `os.walk()` 递归遍历指定目录并识别所有以 `.java` 结尾的文件。

#### 3. **提取类信息**
- **包提取**：`get_package` 函数读取每个 `.java` 文件并使用正则表达式（`^\s*package\s+([\w.]+);`）查找包声明（例如，`package com.mycompany.myproject;`）。
  - 如果未找到包或无法读取文件，则返回 `None`。
- **类名**：假设类名与文件名匹配（例如，`MyClass.java` 定义 `MyClass`）。
- **完全限定名**：组合包和类名（例如，`com.mycompany.myproject.MyClass`）。

#### 4. **收集所有类**
- 在第一遍中，构建项目中所有完全限定类名的集合，以便稍后快速查找。

#### 5. **分析依赖关系**
- **导入提取**：`get_specific_imports` 函数使用正则表达式（`^\s*import\s+([\w.]+);`）提取导入语句，排除通配符导入（例如，`import java.util.*;`）。
  - 示例：从 `import com.mycompany.myproject.utils.Helper;` 中提取 `com.mycompany.myproject.utils.Helper`。
- **依赖映射**：对于每个 `.java` 文件：
  - 获取其完全限定类名。
  - 检查其特定导入。
  - 如果导入的类在项目的类集中且不是该类本身，则添加依赖。

#### 6. **输出依赖文本**
- 以DOT格式输出有向图：
  - 以 `digraph G {` 开头。
  - 对于每个有依赖的类，打印边如 `"ClassA" -> "ClassB";`。
  - 以 `}` 结尾。
- 类和依赖关系按字母顺序排序以保持一致的输出。
- 示例输出：
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### 使用示例
1. 将脚本保存为 `analyze_deps.py`。
2. 运行它：
   ```bash
   python analyze_deps.py /path/to/java/project
   ```
3. 将输出重定向到文件：
   ```bash
   python analyze_deps.py /path/to/java/project > dependencies.dot
   ```
4. 使用Graphviz可视化：
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   这将生成一个显示依赖图的PNG图像。

### 假设和限制
- **每个文件一个公共类**：假设每个 `.java` 文件包含一个公共类，类名与文件名匹配，符合Java惯例。
- **基于导入的依赖**：仅考虑特定导入语句（例如，`import com.example.SomeClass;`）表示的依赖关系，忽略通配符导入（`import com.example.*;`）和同包引用（不需要导入）。
- **内部关注**：仅跟踪项目内部类之间的依赖关系，忽略外部库。
- **基本解析**：使用正则表达式以简化，可能会遗漏边缘情况（例如，注释中的导入）。完整的Java解析器将更加健壮但复杂。

### 自定义
- **输出格式**：修改打印语句以更改依赖文本格式（例如，普通列表而不是DOT）。
- **错误处理**：使用try-except块增强，以优雅地跳过无法读取的文件。
- **范围**：可以扩展以包括外部依赖或同包依赖，进行更深入的代码分析。

该脚本为依赖分析提供了一个实用的起点，适用于通过其内部类关系了解Java项目的结构。