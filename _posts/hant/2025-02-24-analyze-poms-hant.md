---
audio: false
generated: true
lang: hant
layout: post
title: 分析 Maven POM 文件
translated: true
type: note
---

針對你的查詢，我將提供一個解決方案，用於生成 DOT 格式的依賴關係圖。此方案會遞歸地尋找目錄中的所有 `pom.xml` 文件並分析它們的依賴關係，無需像示例中的固定 Maven 多模組專案結構（例如 `project/module1/pom.xml` 等）。腳本將首先收集所有 `pom.xml` 文件，然後分析它們以確定模組依賴關係並輸出圖表。

---

## 解決方案概述

以下是腳本將執行的步驟：
1. **遞歸收集 `pom.xml` 文件**：遍歷指定的根目錄，尋找所有 `pom.xml` 文件，無論其位置或結構如何。
2. **解析模組資訊**：從每個 `pom.xml` 中提取 `groupId`、`artifactId` 和依賴項。
3. **處理 `groupId` 繼承**：如果 `pom.xml` 未指定 `groupId`，則從 `<parent>` 聲明中繼承（如果存在）。
4. **識別專案內部依賴**：根據 `groupId` 和 `artifactId` 將依賴項與專案內的模組進行匹配。
5. **生成 DOT 輸出**：建立模組之間依賴關係的有向圖。

此方法不依賴預定義的目錄層級結構，也不假設父 `pom.xml` 文件位於父目錄中。

---

## Python 腳本

以下是根據你的需求定制的 Python 腳本：

```python
import os
import sys
import xml.etree.ElementTree as ET

# 定義 Maven POM 命名空間
NS = "{http://maven.apache.org/POM/4.0.0}"

# 用於緩存 groupId 以避免重複解析
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    從 pom.xml 文件中提取 groupId，考慮從父 POM 繼承的情況。

    參數：
        pom_path (str): pom.xml 文件的路徑。
        pom_map (dict): pom.xml 路徑到其解析數據的映射。

    返回：
        str: 模組的 groupId。
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # 檢查父 POM 聲明
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
                # 如果省略 relativePath，則預設為父目錄
                parent_pom_path = os.path.join(os.path.dirname(pom_path), '..', 'pom.xml')
                parent_pom_path = os.path.normpath(parent_pom_path)

            if parent_pom_path in pom_map:
                group_id = get_group_id(parent_pom_path, pom_map)
            else:
                raise ValueError(f"Parent POM not found for {pom_path}: {parent_pom_path}")
        else:
            raise ValueError(f"No groupId or parent specified in {pom_path}")

    group_id_cache[pom_path] = group_id
    return group_id

def get_artifact_id(pom_path):
    """
    從 pom.xml 文件中提取 artifactId。

    參數：
        pom_path (str): pom.xml 文件的路徑。

    返回：
        str: 模組的 artifactId。
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xml must specify artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    從 pom.xml 文件中提取依賴項列表。

    參數：
        pom_path (str): pom.xml 文件的路徑。

    返回：
        list: 每個依賴項的 (groupId, artifactId) 元組列表。
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
    # 檢查命令行參數
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)

    # 步驟 1: 遞歸尋找所有 pom.xml 文件
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"No pom.xml files found in {root_dir}")
        sys.exit(1)

    # 步驟 2: 建立所有 POM 的字典以供父 POM 查詢
    pom_map = {pom_file: None for pom_file in pom_files}

    # 步驟 3: 提取模組資訊
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"Warning: Skipping {pom_file} due to error: {e}")
            continue

    # 步驟 4: 分析依賴關係
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
                    # 將依賴關係添加為 (導入者, 被導入者) 元組，為簡化使用 artifactId
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"Warning: Error processing dependencies in {pom_file}: {e}")
            continue

    # 步驟 5: 以 DOT 格式輸出
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## 運作方式

### 1. **命令行輸入**
- 接受單一參數：`<root_directory>`，作為遞歸搜尋的起點。
- 驗證其是否為目錄。

### 2. **尋找 `pom.xml` 文件**
- 使用 `os.walk` 遞歸遍歷目錄樹，並將所有 `pom.xml` 文件收集到列表中。

### 3. **解析模組資訊**
- **Group ID (`groupId`)**：
  - 從每個 `pom.xml` 中提取。
  - 如果不存在，則查找 `<parent>` 部分，並使用 `relativePath`（如果省略則預設為父目錄）從引用的父 POM 解析 `groupId`。
  - 緩存結果以避免重新解析。
- **Artifact ID (`artifactId`)**：必須存在於每個 `pom.xml` 中。
- **依賴項**：從 `<dependencies>` 部分提取 `(groupId, artifactId)` 對。

### 4. **依賴關係分析**
- 為所有模組建立 `(groupId, artifactId)` 到 `pom_path` 的映射。
- 對於每個 `pom.xml`，檢查其依賴項與模組映射以找到專案內部依賴。
- 排除自我依賴（模組依賴自身的情況）。
- 將依賴關係記錄為 `(importer_artifactId, imported_artifactId)` 對。

### 5. **DOT 輸出**
- 以 DOT 格式輸出有向圖，為簡化使用 `artifactId` 作為節點標籤。

---

## 使用示例

假設你的目錄結構不規則：

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", depends on "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", depends on "core")
```

運行腳本：

```bash
python script.py myproject
```

**輸出：**

```
digraph G {
  "app" -> "core";
  "util" -> "core";
}
```

這顯示 `app` 和 `util` 都依賴 `core`。

---

## 注意事項與限制

- **無目錄分組**：與思考追蹤中的原始腳本不同，此版本不按目錄結構對模組進行分組，因為你未要求此功能。它直接在圖表中使用 `artifactId`。
- **父 POM 解析**：依賴 `<parent>` 部分中的 `relativePath`，如果省略則假設父 POM 位於父目錄中。如果父 POM 不在收集的集合中，則會引發錯誤。
- **簡單匹配**：僅通過 `groupId` 和 `artifactId` 匹配依賴項，忽略版本。
- **無屬性替換**：不處理 Maven 屬性，例如 `${project.groupId}`。
- **錯誤處理**：跳過有問題的 `pom.xml` 文件並發出警告，而不是完全失敗。

此腳本滿足你的要求，即「遞歸迭代，首先獲取所有 POM，然後分析」，且不假設固定的文件結構。如果你需要調整，請告知！