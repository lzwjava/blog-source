---
audio: false
generated: true
lang: ja
layout: post
title: Java依存関係の分析
translated: true
type: note
---

あなたのクエリに対応するため、提供されたPythonスクリプトを修正して、依存関係がパッケージ階層の指定された「レベル」でグループ化されたJavaクラスの依存関係グラフを生成します。例えば、`level=1`の場合、パッケージはトップレベル（例：「org」）でグループ化され、`level=2`の場合、2番目のレベル（例：「org.springframework」）でグループ化されます。これは、依存関係を分析する前に、クラスをパッケージ名の最初の`level`部分に基づいてグループに集計し、グラフが個々のクラスではなくこれらのグループ間の依存関係を示すことを意味します。

以下は修正されたスクリプトと、その変更点と要件を満たす方法の説明です。

### 修正されたスクリプト

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    .javaファイルからパッケージ名を抽出します。

    Args:
        file_path (str): .javaファイルへのパス。

    Returns:
        str: パッケージ名。見つからない場合はNone。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    .javaファイルから特定のクラスインポートを抽出します（ワイルドカードインポートを除く）。

    Args:
        file_path (str): .javaファイルへのパス。

    Returns:
        list: 完全修飾インポートクラス名のリスト。
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # ワイルドカードインポートを除外（例: import java.util.*;）
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    パッケージ名の最初の'level'部分に基づいてパッケージグループを取得します。

    Args:
        full_class_name (str): 完全修飾クラス名（例: "org.springframework.boot.App"）。
        level (int): 含めるパッケージレベルの数（例: 1なら"org"、2なら"org.springframework"）。

    Returns:
        str: パッケージグループ（例: "org"または"org.springframework"）。
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # クラス名を除いたパッケージを抽出
    parts = package.split('.')
    if len(parts) <= level:
        return package  # レベルより少ないまたは等しい部分数の場合は完全なパッケージを使用
    else:
        return '.'.join(parts[:level])  # 最初の'level'部分を使用

if __name__ == '__main__':
    # コマンドライン引数の確認: root_directoryとlevel
    if len(sys.argv) != 3:
        print("Usage: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("Error: level must be a positive integer")
        sys.exit(1)

    all_classes = set()

    # 第一パス: プロジェクト内のすべての完全修飾クラス名を収集
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # パッケージグループ間の依存関係を保存
    group_dependencies = set()

    # 第二パス: パッケージグループに基づいて依存関係を分析
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
                        # プロジェクト内のクラスへの依存関係のみを含める
                        # 自己依存関係を除外
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # DOT形式で依存関係グラフを出力
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### 変更点の説明

1. **コマンドライン引数**:
   - **元のスクリプト**: `python script.py <root_directory>`
   - **修正後**: `python script.py <root_directory> <level>`
   - 2番目の引数`level`（パッケージ階層レベルを指定）のサポートを追加。スクリプトは正確に2つの引数が提供され、`level`が正の整数であることを確認します。

2. **新機能: `get_package_group`**:
   - 指定された`level`に基づいてクラスのパッケージグループを計算する関数を追加。
   - 完全修飾クラス名（例: "org.springframework.boot.App"）に対して、パッケージ（"org.springframework.boot"）を抽出し、部分（"org", "springframework", "boot"）に分割し、最初の`level`部分を取得:
     - `level=1`の場合: "org"を返す。
     - `level=2`の場合: "org.springframework"を返す。
     - パッケージの部分数が`level`より少ない場合（例: `level=3`での"com.example"）、完全なパッケージ（"com.example"）を返す。

3. **依存関係のグループ化**:
   - **元のスクリプト**: 個々のクラス間の依存関係を保存するために`defaultdict(set)`を使用。
   - **修正後**: パッケージグループ間の有向エッジをタプル`(from_group, to_group)`として保存する`set`（`group_dependencies`）を使用。
   - 各クラスについて:
     - `get_package_group`を使用してそのパッケージグループ（`importer_group`）を計算。
     - プロジェクト内（`imp in all_classes`）にあり、かつクラス自身ではない（`imp != full_class_name`）各特定のインポートについて:
       - インポートされたクラスのパッケージグループ（`imported_group`）を計算。
       - グループが異なる場合（`imported_group != importer_group`）、`group_dependencies`にエッジを追加。
   - `set`は一意性を保証するため、同じグループ間の複数の依存関係は単一のエッジになります。

4. **DOT出力**:
   - **元のスクリプト**: 個々のクラス間のエッジを出力（例: "org.springframework.boot.App" -> "org.apache.commons.IOUtils"）。
   - **修正後**: パッケージグループ間のエッジを出力（例: `level=2`の場合、"org.springframework" -> "org.apache"）。
   - エッジは一貫した出力のためにソートされます。

### 要件を満たす方法

- **レベルサポート**: スクリプトは依存関係を分析する前にパッケージをグループ化する`level`パラメータを受け入れるようになりました。
- **レベル = 1**: すべてのクラスをトップレベルパッケージ（例: "org"）でグループ化。例えば、"org.springframework.boot.App"と"org.apache.commons.IOUtils"は両方とも"org"グループに属するため、それら間の"org"内のインポートはエッジとして表示されません。
- **レベル = 2**: クラスを最初の2つのパッケージレベル（例: "org.springframework"）でグループ化。例えば、"org.springframework.boot.App"から"org.apache.commons.IOUtils"へのインポートは、"org.springframework"から"org.apache"へのエッジを作成します。
- **依存関係分析前のパッケージ累積**: スクリプトは、そのインポートを分析する前に、`level`に基づいて各クラスのパッケージグループを決定し、依存関係が個々のクラスではなくグループ間であることを保証します。
- **例への準拠**: あなたの例のエッジについて:
  - 元の状態: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - `level=2`の場合: 両方のクラスは"org.springframework"内にあるため、エッジは追加されません（同じグループ）。
  - `level=3`の場合: "org.springframework.boot.web" -> "org.springframework.boot.convert"、これらの異なるグループ間にエッジを追加。

### 使用例

- **コマンド**: `python script.py /path/to/project 1`
  - グループ: "org", "com"など。
  - 出力には、"org"パッケージのクラスが"com"パッケージのクラスをインポートする場合、`"org" -> "com"`が含まれる可能性があります。

- **コマンド**: `python script.py /path/to/project 2`
  - グループ: "org.springframework", "org.apache"など。
  - 出力には、`"org.springframework" -> "org.apache"`が含まれる可能性があります。

### 注意点

- スクリプトは、プロジェクト内の依存関係のみ（`all_classes`内のインポート）を含め、ワイルドカードインポートと自己依存関係を除外する元の動作を維持します。
- パッケージ宣言のないクラスは、元のスクリプトと同様にスキップされます。
- 出力はDOT形式の有向グラフであり、Graphvizなどのツールで表示可能です。

この修正されたスクリプトは、パッケージレベル階層による依存関係のグループ化に関するあなたのリクエストを完全に満たすはずです。