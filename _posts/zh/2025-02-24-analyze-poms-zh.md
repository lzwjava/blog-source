---
audio: true
generated: false
lang: zh
layout: post
title: 分析Maven POM文件生成依赖图
translated: true
---

要解决您的问题，我将提供一个生成依赖图的解决方案，该图以DOT格式生成，通过递归查找目录中的所有`pom.xml`文件并分析它们的依赖关系，而不假设固定的Maven多模块项目结构（例如`project/module1/pom.xml`等）。脚本将首先收集所有`pom.xml`文件，然后分析它们以确定模块依赖关系并输出图形。

---

## 解决方案概述

以下是脚本将执行的操作：
1. **递归收集`pom.xml`文件**：遍历指定的根目录以查找所有`pom.xml`文件，无论它们的位置或结构。
2. **解析模块信息**：从每个`pom.xml`中提取`groupId`、`artifactId`和依赖项。
3. **处理`groupId`继承**：如果`pom.xml`没有指定`groupId`，则从`<parent>`声明继承，如果存在。
4. **识别项目内部依赖**：根据`groupId`和`artifactId`将依赖项与项目中的模块匹配。
5. **生成DOT输出**：创建模块之间的有向依赖图。

这种方法不依赖于预定义的目录层次结构，也不假设父`pom.xml`文件在父目录中。

---

## Python脚本

以下是根据您的要求定制的Python脚本：

```python
import os
import sys
import xml.etree.ElementTree as ET

# 定义Maven POM命名空间
NS = "{http://maven.apache.org/POM/4.0.0}"

# 缓存groupId以避免冗余解析
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    从pom.xml文件中提取groupId，考虑从父级继承。

    参数:
        pom_path (str): pom.xml文件的路径。
        pom_map (dict): pom.xml路径到其解析数据的映射。

    返回:
        str: 模块的groupId。
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # 检查父级声明
        parent = root.find(NS + 'parent')
        if parent is not None:
            parent_group_id = parent.find(NS + 'groupId').text.strip()
            parent_artifact_id = parent.find(NS + 'artifactId').text.strip()
            parent_relative_path = parent.find(NS + 'relativePath')
            if parent_relative_path is not None and parent_relative_path.text:
                parent_pom_path = os.path.normpath(
                    os.path.join(os.path.dirname(pom_path), parent_relative_path.text)
                )
            else:
                # 如果省略relativePath，则默认为父目录
                parent_pom_path = os.path.join(os.path.dirname(pom_path), '..', 'pom.xml')
                parent_pom_path = os.path.normpath(parent_pom_path)

            if parent_pom_path in pom_map:
                group_id = get_group_id(parent_pom_path, pom_map)
            else:
                raise ValueError(f"未找到{pom_path}的父POM: {parent_pom_path}")
        else:
            raise ValueError(f"{pom_path}未指定groupId或父级")

    group_id_cache[pom_path] = group_id
    return group_id

def get_artifact_id(pom_path):
    """
    从pom.xml文件中提取artifactId。

    参数:
        pom_path (str): pom.xml文件的路径。

    返回:
        str: 模块的artifactId。
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xml必须指定artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    从pom.xml文件中提取依赖项列表。

    参数:
        pom_path (str): pom.xml文件的路径。

    返回:
        list: 每个依赖项的元组列表(groupId, artifactId)。
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    dependencies = []

    for dep in root.findall(NS + 'dependencies/' + NS + 'dependency'):
        dep_group_id_elem = dep.find(NS + 'groupId')
        dep_artifact_id_elem = dep.find(NS + 'artifactId')
        if dep_group_id_elem is not None and dep_artifact_id_elem is not None:
            dep_group_id = dep_group_id_elem.text.strip()
            dep_artifact_id = dep_artifact_id_elem.text.strip()
            dependencies.append((dep_group_id, dep_artifact_id))

    return dependencies

if __name__ == '__main__':
    # 检查命令行参数
    if len(sys.argv) != 2:
        print("用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"错误: {root_dir}不是目录")
        sys.exit(1)

    # 步骤1: 递归查找所有pom.xml文件
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"{root_dir}中未找到pom.xml文件")
        sys.exit(1)

    # 步骤2: 构建所有POM的字典以进行父级查找
    pom_map = {pom_file: None for pom_file in pom_files}

    # 步骤3: 提取模块信息
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"警告: 由于错误跳过{pom_file}: {e}")
            continue

    # 步骤4: 分析依赖项
    dependencies = set()
    for pom_file in pom_files:
        try:
            importer_group_id = get_group_id(pom_file, pom_map)
            importer_artifact_id = get_artifact_id(pom_file)
            importer_key = (importer_group_id, importer_artifact_id)
            deps = get_dependencies(pom_file)
            for dep_group_id, dep_artifact_id in deps:
                dep_key = (dep_group_id, dep_artifact_id)
                if dep_key in modules and dep_key != importer_key:
                    # 使用artifactId添加依赖项作为(importer, imported)元组以简化
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"警告: 处理{pom_file}中的依赖项时出错: {e}")
            continue

    # 步骤5: 输出DOT格式
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## 工作原理

### 1. **命令行输入**
- 接受一个参数：`<root_directory>`，递归搜索的起点。
- 验证它是一个目录。

### 2. **查找`pom.xml`文件**
- 使用`os.walk`递归遍历目录树并将所有`pom.xml`文件收集到列表中。

### 3. **解析模块信息**
- **组ID（groupId）**：
  - 从每个`pom.xml`中提取。
  - 如果不存在，则查找`<parent>`部分并从引用的父POM解析`groupId`，使用`relativePath`（如果省略则默认为父目录）。
  - 缓存结果以避免重新解析。
- **工件ID（artifactId）**：必须在每个`pom.xml`中存在。
- **依赖项**：从`<dependencies>`部分提取`(groupId, artifactId)`对。

### 4. **依赖项分析**
- 构建所有模块的`(groupId, artifactId)`到`pom_path`的映射。
- 对于每个`pom.xml`，检查其依赖项以查找项目内部依赖项。
- 排除自依赖（模块依赖自身）。
- 记录依赖项作为`(importer_artifactId, imported_artifactId)`对。

### 5. **DOT输出**
- 以DOT格式输出有向图，使用`artifactId`作为节点标签以简化。

---

## 示例用法

假设您的目录结构不规则：

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", 依赖于"core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", 依赖于"core")
```

运行脚本：

```bash
python script.py myproject
```

**输出：**

```
digraph G {
  "app" -> "core";
  "util" -> "core";
}
```

这显示`app`和`util`都依赖于`core`。

---

## 注意事项和限制

- **不按目录分组**：与原始脚本不同，此版本不按目录结构分组模块，因为您没有要求。它直接在图中使用`artifactId`。
- **父级解析**：依赖于`<parent>`部分中的`relativePath`，或者如果省略则假设父POM在父目录中。如果父POM不在收集的集合中，则引发错误。
- **简单匹配**：仅根据`groupId`和`artifactId`匹配依赖项，忽略版本。
- **不处理属性替换**：不处理Maven属性（例如`${project.groupId}`）。
- **错误处理**：跳过有问题的`pom.xml`文件并发出警告，而不是完全失败。

此脚本满足您的要求“递归迭代，首先获取所有POM，然后分析”，而不假设固定的文件结构。如果需要调整，请告诉我！