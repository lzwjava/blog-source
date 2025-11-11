---
audio: false
generated: true
lang: ja
layout: post
title: Maven POMの解析
translated: true
type: note
---

あなたのクエリに対応するため、ディレクトリ内のすべての `pom.xml` ファイルを再帰的に見つけ、それらの依存関係を分析して DOT 形式の依存関係グラフを生成するソリューションを提供します。このスクリプトは、例 (`project/module1/pom.xml` など) のような固定された Maven マルチモジュールプロジェクト構造を前提とせず、まずすべての `pom.xml` ファイルを収集し、それらを分析してモジュール間の依存関係を特定し、グラフを出力することに焦点を当てます。

---

## ソリューション概要

このスクリプトが行うこと:
1.  **`pom.xml` ファイルの再帰的収集**: 指定されたルートディレクトリを走査し、その場所や構造に関係なくすべての `pom.xml` ファイルを見つけます。
2.  **モジュール情報の解析**: 各 `pom.xml` から `groupId`、`artifactId`、および依存関係を抽出します。
3.  **`groupId` 継承の処理**: `pom.xml` が `groupId` を指定していない場合、存在すれば `<parent>` 宣言から継承します。
4.  **プロジェクト内依存関係の特定**: 依存関係を `groupId` と `artifactId` に基づいてプロジェクト内のモジュールと照合します。
5.  **DOT 出力の生成**: モジュール間の依存関係の有向グラフを作成します。

このアプローチは、事前に定義されたディレクトリ階層に依存せず、親 `pom.xml` ファイルが親ディレクトリにあることも前提としません。

---

## Python スクリプト

以下は、あなたの要件に合わせた Python スクリプトです:

```python
import os
import sys
import xml.etree.ElementTree as ET

# Maven POM 名前空間を定義
NS = "{http://maven.apache.org/POM/4.0.0}"

# 冗長なパースを避けるための groupId キャッシュ
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    pom.xml ファイルから groupId を抽出します。親からの継承も考慮します。

    Args:
        pom_path (str): pom.xml ファイルへのパス。
        pom_map (dict): pom.xml のパスとその解析済みデータのマッピング。

    Returns:
        str: モジュールの groupId。
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # 親宣言を確認
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
                # relativePath が省略されている場合は親ディレクトリをデフォルトとする
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
    pom.xml ファイルから artifactId を抽出します。

    Args:
        pom_path (str): pom.xml ファイルへのパス。

    Returns:
        str: モジュールの artifactId。
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xml must specify artifactId: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    pom.xml ファイルから依存関係のリストを抽出します。

    Args:
        pom_path (str): pom.xml ファイルへのパス。

    Returns:
        list: 各依存関係に対する (groupId, artifactId) のタプルのリスト。
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
    # コマンドライン引数をチェック
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"Error: {root_dir} is not a directory")
        sys.exit(1)

    # ステップ 1: すべての pom.xml ファイルを再帰的に検索
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"No pom.xml files found in {root_dir}")
        sys.exit(1)

    # ステップ 2: 親参照用にすべての POM の辞書を構築
    pom_map = {pom_file: None for pom_file in pom_files}

    # ステップ 3: モジュール情報を抽出
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"Warning: Skipping {pom_file} due to error: {e}")
            continue

    # ステップ 4: 依存関係を分析
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
                    # 依存関係を (importer, imported) タプルとして追加 (単純化のため artifactId を使用)
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"Warning: Error processing dependencies in {pom_file}: {e}")
            continue

    # ステップ 5: DOT 形式で出力
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## 動作説明

### 1. **コマンドライン入力**
- 単一の引数 `<root_directory>` を取ります。これは再帰的検索の開始点です。
- それがディレクトリであることを検証します。

### 2. **`pom.xml` ファイルの検索**
- `os.walk` を使用してディレクトリツリーを再帰的に走査し、すべての `pom.xml` ファイルをリストに収集します。

### 3. **モジュール情報の解析**
- **グループ ID (`groupId`)**:
  - 各 `pom.xml` から抽出されます。
  - 存在しない場合は、`<parent>` セクションを探し、`relativePath` (または省略されている場合は親ディレクトリ) を使用して参照される親 POM から `groupId` を解決します。
  - 結果をキャッシュして再パースを防ぎます。
- **アーティファクト ID (`artifactId`)**: 各 `pom.xml` に存在する必要があります。
- **依存関係**: `<dependencies>` セクションから `(groupId, artifactId)` のペアを抽出します。

### 4. **依存関係分析**
- すべてのモジュールに対して `(groupId, artifactId)` から `pom_path` へのマップを構築します。
- 各 `pom.xml` について、その依存関係をモジュールマップに対してチェックし、プロジェクト内の依存関係を特定します。
- 自己依存 (モジュールが自身に依存する場合) を除外します。
- 依存関係を `(importer_artifactId, imported_artifactId)` のペアとして記録します。

### 5. **DOT 出力**
- DOT 形式で有向グラフを出力し、単純化のためノードラベルに `artifactId` を使用します。

---

## 使用例

ディレクトリ構造が不規則であると仮定します:

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", depends on "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", depends on "core")
```

スクリプトを実行:

```bash
python script.py myproject
```

**出力:**

```
digraph G {
  "app" -> "core";
  "util" -> "core";
}
```

これは、`app` と `util` の両方が `core` に依存していることを示しています。

---

## 注意点と制限事項

-   **ディレクトリによるグループ化なし**: 思考トレースの元のスクリプトとは異なり、このバージョンはディレクトリ構造によるモジュールのグループ化を行いません。グラフでは直接 `artifactId` を使用します。
-   **親の解決**: `<parent>` セクション内の `relativePath`、または省略された場合は親ディレクトリ内の親 POM に依存します。親 POM が収集されたセット内にない場合、エラーを発生させます。
-   **単純な照合**: 依存関係を `groupId` と `artifactId` のみで照合し、バージョンは無視します。
-   **プロパティ置換なし**: `${project.groupId}` のような Maven プロパティを処理しません。
-   **エラーハンドリング**: 問題のある `pom.xml` ファイルは完全に失敗するのではなく、警告を出してスキップします。

このスクリプトは、「再帰的に反復処理し、まずすべての POM を取得し、その後分析する」というあなたの要件を満たし、固定されたファイル構造を前提としません。調整が必要な場合はお知らせください！