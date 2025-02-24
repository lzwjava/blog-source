---
audio: true
lang: ja
layout: post
title: Maven POMの解析による依存関係グラフの生成
translated: true
---

あなたの質問に対する回答として、以下の方法で、ディレクトリ内のすべての `pom.xml` ファイルを再帰的に見つけて依存関係を解析し、DOT形式の依存関係グラフを生成するソリューションを提供します。このスクリプトは、固定されたMavenマルチモジュールプロジェクト構造（例：`project/module1/pom.xml`など）を前提としないため、ディレクトリ構造に依存せずに動作します。スクリプトはまずすべての `pom.xml` ファイルを収集し、その後その依存関係を解析してグラフを出力します。

---

## ソリューションの概要

以下がスクリプトの動作内容です：
1. **再帰的に `pom.xml` ファイルを収集する**: 指定されたルートディレクトリをトラバースして、場所や構造に関係なくすべての `pom.xml` ファイルを見つけます。
2. **モジュール情報を解析する**: 各 `pom.xml` から `groupId`、`artifactId`、および依存関係を抽出します。
3. **`groupId` の継承を処理する**: `pom.xml` が `groupId` を指定していない場合、`<parent>` 宣言から継承します。
4. **プロジェクト内の依存関係を特定する**: `groupId` と `artifactId` に基づいて、プロジェクト内のモジュールに依存関係をマッチングします。
5. **DOT形式の出力を生成する**: モジュール間の依存関係の有向グラフを作成します。

このアプローチは、事前に定義されたディレクトリ階層に依存せず、親 `pom.xml` ファイルが親ディレクトリにあると仮定しません。

---

## Pythonスクリプト

以下は、あなたの要件に合わせて調整されたPythonスクリプトです：

```python
import os
import sys
import xml.etree.ElementTree as ET

# Maven POMの名前空間を定義
NS = "{http://maven.apache.org/POM/4.0.0}"

# groupIdを避けるためのキャッシュ
group_id_cache = {}

def get_group_id(pom_path, pom_map):
    """
    pom.xmlファイルからgroupIdを抽出し、親からの継承を考慮します。

    引数:
        pom_path (str): pom.xmlファイルへのパス。
        pom_map (dict): pom.xmlのパスを解析されたデータにマッピングする辞書。

    戻り値:
        str: モジュールのgroupId。
    """
    if pom_path in group_id_cache:
        return group_id_cache[pom_path]

    tree = ET.parse(pom_path)
    root = tree.getroot()
    group_id_elem = root.find(NS + 'groupId')

    if group_id_elem is not None:
        group_id = group_id_elem.text.strip()
    else:
        # 親の宣言を確認
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
                # relativePathが省略された場合は、親ディレクトリにデフォルト
                parent_pom_path = os.path.join(os.path.dirname(pom_path), '..', 'pom.xml')
                parent_pom_path = os.path.normpath(parent_pom_path)

            if parent_pom_path in pom_map:
                group_id = get_group_id(parent_pom_path, pom_map)
            else:
                raise ValueError(f"親POMが見つかりません: {pom_path}: {parent_pom_path}")
        else:
            raise ValueError(f"{pom_path}にgroupIdまたは親が指定されていません")

    group_id_cache[pom_path] = group_id
    return group_id

def get_artifact_id(pom_path):
    """
    pom.xmlファイルからartifactIdを抽出します。

    引数:
        pom_path (str): pom.xmlファイルへのパス。

    戻り値:
        str: モジュールのartifactId。
    """
    tree = ET.parse(pom_path)
    root = tree.getroot()
    artifact_id_elem = root.find(NS + 'artifactId')

    if artifact_id_elem is None:
        raise ValueError(f"pom.xmlにはartifactIdが指定されていません: {pom_path}")

    return artifact_id_elem.text.strip()

def get_dependencies(pom_path):
    """
    pom.xmlファイルから依存関係のリストを抽出します。

    引数:
        pom_path (str): pom.xmlファイルへのパス。

    戻り値:
        list: 各依存関係の(groupId, artifactId)のタプルのリスト。
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
    # コマンドライン引数を確認
    if len(sys.argv) != 2:
        print("使用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"エラー: {root_dir}はディレクトリではありません")
        sys.exit(1)

    # ステップ1: 再帰的にすべてのpom.xmlファイルを見つける
    pom_files = [
        os.path.join(root, file)
        for root, _, files in os.walk(root_dir)
        for file in files if file == 'pom.xml'
    ]

    if not pom_files:
        print(f"{root_dir}にpom.xmlファイルが見つかりません")
        sys.exit(1)

    # ステップ2: 親の参照用にすべてのPOMの辞書を構築
    pom_map = {pom_file: None for pom_file in pom_files}

    # ステップ3: モジュール情報を抽出
    modules = {}  # (groupId, artifactId) -> pom_path
    for pom_file in pom_files:
        try:
            group_id = get_group_id(pom_file, pom_map)
            artifact_id = get_artifact_id(pom_file)
            modules[(group_id, artifact_id)] = pom_file
        except ValueError as e:
            print(f"警告: エラーのため{pom_file}をスキップ: {e}")
            continue

    # ステップ4: 依存関係を解析
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
                    # 依存関係を(imported_artifactId, imported_artifactId)のタプルとして追加
                    dependencies.add((importer_artifact_id, dep_artifact_id))
        except ValueError as e:
            print(f"警告: {pom_file}の依存関係の処理中にエラーが発生: {e}")
            continue

    # ステップ5: DOT形式で出力
    print('digraph G {')
    for from_module, to_module in sorted(dependencies):
        print(f'  "{from_module}" -> "{to_module}";')
    print('}')
```

---

## その仕組み

### 1. **コマンドライン入力**
- 1つの引数を取ります: `<root_directory>`、再帰的な検索の開始点。
- ディレクトリであることを検証します。

### 2. **`pom.xml` ファイルの検索**
- `os.walk` を使用してディレクトリツリーを再帰的にトラバースし、すべての `pom.xml` ファイルをリストに収集します。

### 3. **モジュール情報の解析**
- **グループID (`groupId`)**:
  - 各 `pom.xml` から抽出します。
  - 存在しない場合、`<parent>` セクションを確認し、`relativePath` を使用して参照された親POMから `groupId` を解決します（省略された場合は親ディレクトリにデフォルト）。
  - 結果をキャッシュして再解析を避けます。
- **アーティファクトID (`artifactId`)**: 各 `pom.xml` に存在する必要があります。
- **依存関係**: `<dependencies>` セクションから `(groupId, artifactId)` ペアを抽出します。

### 4. **依存関係の解析**
- すべてのモジュールの `(groupId, artifactId)` を `pom_path` にマッピングするマップを構築します。
- 各 `pom.xml` に対して、モジュールマップに対して依存関係を確認し、プロジェクト内の依存関係を特定します。
- 自依存（モジュールが自分自身に依存する場合）を除外します。
- 依存関係を `(importer_artifactId, imported_artifactId)` ペアとして記録します。

### 5. **DOT形式の出力**
- `artifactId` をノードラベルとして使用して、有向グラフをDOT形式で出力します。

---

## 使用例

ディレクトリ構造が不規則な場合を考えてみましょう：

```
myproject/
├── app/pom.xml (groupId="com.myapp", artifactId="app", depends on "core")
├── libs/core/pom.xml (groupId="com.myapp", artifactId="core")
├── tools/util/pom.xml (groupId="com.myapp", artifactId="util", depends on "core")
```

スクリプトを実行します：

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

これは、`app` と `util` が `core` に依存していることを示しています。

---

## 注意点と制限事項

- **ディレクトリによるグループ化なし**: 元のスクリプトと異なり、このバージョンではディレクトリ構造に基づいてモジュールをグループ化しません。代わりに、グラフに `artifactId` を直接使用します。
- **親の解決**: `<parent>` セクションの `relativePath` に依存し、省略された場合は親POMが親ディレクトリにあると仮定します。収集されたセットに親POMが含まれていない場合はエラーを発生させます。
- **シンプルなマッチング**: `groupId` と `artifactId` に基づいて依存関係をマッチングし、バージョンを無視します。
- **プロパティ置換なし**: Mavenのプロパティ（例：`${project.groupId}`）を処理しません。
- **エラーハンドリング**: 問題のある `pom.xml` ファイルを警告とともにスキップし、全体的に失敗するのではなく、スキップします。

このスクリプトは、固定されたファイル構造を前提としない「再帰的に反復し、すべてのPOMを最初に取得し、その後解析する」というあなたの要件を満たします。調整が必要な場合はお知らせください！