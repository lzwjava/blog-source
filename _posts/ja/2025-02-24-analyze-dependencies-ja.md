---
audio: false
lang: ja
layout: post
title: Java 依存関係の分析
translated: true
---

あなたの質問に対応するために、提供されたPythonスクリプトを修正し、Javaクラスの依存関係グラフを生成するようにしました。依存関係は、指定された「レベル」のパッケージ階層でグループ化されます。例えば、`level=1`の場合、パッケージはトップレベル（例："org"）でグループ化され、`level=2`の場合は、2番目のレベル（例："org.springframework"）でグループ化されます。これにより、依存関係を分析する前に、クラスをパッケージ名の最初の`level`部分に基づいてグループにまとめ、グラフはこれらのグループ間の依存関係を示すことになります。

以下に、修正されたスクリプトとその変更点、そしてあなたの要件を満たす方法についての説明を示します。

### 修正されたスクリプト

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    .javaファイルからパッケージ名を抽出します。

    引数:
        file_path (str): .javaファイルへのパス。

    戻り値:
        str: パッケージ名、または見つからない場合はNone。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"警告: {file_path}を読み取れませんでした: {e}")
    return None

def get_specific_imports(file_path):
    """
    .javaファイルから特定のクラスのインポートを抽出します。ワイルドカードインポートは除外します。

    引数:
        file_path (str): .javaファイルへのパス。

    戻り値:
        list: 完全修飾されたインポートされたクラス名のリスト。
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # ワイルドカードインポート（例：import java.util.*;）を除外
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"警告: {file_path}を読み取れませんでした: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    パッケージ名の最初の'level'部分に基づいてパッケージグループを取得します。

    引数:
        full_class_name (str): 完全修飾されたクラス名（例："org.springframework.boot.App"）。
        level (int): 含めるパッケージレベルの数（例：1は"org"、2は"org.springframework"）。

    戻り値:
        str: パッケージグループ（例："org"または"org.springframework"）。
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # クラス名を除くパッケージを抽出
    parts = package.split('.')
    if len(parts) <= level:
        return package  # パッケージがlevel以下の部分を持つ場合は、全パッケージを使用
    else:
        return '.'.join(parts[:level])  # 最初の'level'部分を使用

if __name__ == '__main__':
    # コマンドライン引数の確認: root_directoryとlevel
    if len(sys.argv) != 3:
        print("使用法: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("エラー: levelは正の整数でなければなりません")
        sys.exit(1)

    all_classes = set()

    # 第一回目のパス: プロジェクト内のすべての完全修飾されたクラス名を収集
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

    # 第二回目のパス: パッケージグループに基づいて依存関係を分析
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
                        # プロジェクト内のクラスに対する依存関係のみを含める
                        # 自依存関係を除外
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
   - **元**: `python script.py <root_directory>`
   - **修正**: `python script.py <root_directory> <level>`
   - `level`という2番目の引数をサポートするようにしました。この引数はパッケージ階層レベルを指定します。スクリプトは正確に2つの引数が提供されていることを確認し、`level`が正の整数であることを確認します。

2. **新しい関数: `get_package_group`**:
   - 指定された`level`に基づいてクラスのパッケージグループを計算するための関数を追加しました。
   - 完全修飾されたクラス名（例："org.springframework.boot.App"）に対して、パッケージ（"org.springframework.boot"）を抽出し、部分（"org", "springframework", "boot"）に分割し、最初の`level`部分を取得します：
     - `level=1`の場合: "org"を返します。
     - `level=2`の場合: "org.springframework"を返します。
     - パッケージが`level`より少ない部分を持つ場合（例："com.example"で`level=3`）、全パッケージ（"com.example"）を返します。

3. **依存関係のグループ化**:
   - **元**: 個々のクラス間の依存関係を`defaultdict(set)`で保存。
   - **修正**: パッケージグループ間の有向エッジをタプル（`from_group`, `to_group`）として`set`（`group_dependencies`）で保存。
   - 各クラスに対して:
     - `get_package_group`を使用してそのパッケージグループ（`importer_group`）を計算。
     - プロジェクト内の特定のインポート（`imp in all_classes`）で、クラス自身ではない（`imp != full_class_name`）場合:
       - インポートされたクラスのパッケージグループ（`imported_group`）を計算。
       - グループが異なる場合（`imported_group != importer_group`）、エッジを`group_dependencies`に追加。
   - `set`は一意性を保証するため、同じグループ間の複数の依存関係は1つのエッジにまとめられます。

4. **DOT出力**:
   - **元**: 個々のクラス間のエッジ（例："org.springframework.boot.App" -> "org.apache.commons.IOUtils"）を出力。
   - **修正**: パッケージグループ間のエッジ（例："org.springframework" -> "org.apache"で`level=2`）を出力。
   - エッジは一貫した出力のためにソートされます。

### あなたの要件を満たす方法

- **レベルのサポート**: スクリプトは依存関係を分析する前にパッケージをグループ化するための`level`パラメータを受け入れるようになりました。
- **レベル = 1**: すべてのクラスをトップレベルパッケージ（例："org"）でグループ化します。例えば、"org.springframework.boot.App"と"org.apache.commons.IOUtils"はともに"org"グループに属するため、"org"内のインポート間のエッジは表示されません。
- **レベル = 2**: クラスを最初の2つのパッケージレベル（例："org.springframework"）でグループ化します。例えば、"org.springframework.boot.App"から"org.apache.commons.IOUtils"へのインポートは、"org.springframework"から"org.apache"へのエッジを作成します。
- **依存関係分析前にパッケージをまとめる**: スクリプトは`level`に基づいて各クラスのパッケージグループを決定し、インポートを分析する前に依存関係をグループ間にすることで、依存関係を個々のクラス間ではなくグループ間にします。
- **例の準拠**: あなたの例のエッジ:
  - 元: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - `level=2`の場合: 両方のクラスは"org.springframework"に属するため、エッジは追加されません（同じグループ）。
  - `level=3`の場合: "org.springframework.boot.web" -> "org.springframework.boot.convert"、これらの異なるグループ間にエッジを追加。

### 使用例

- **コマンド**: `python script.py /path/to/project 1`
  - グループ: "org", "com"など。
  - 出力には、"org"パッケージのクラスが"com"パッケージのクラスをインポートする場合、"org" -> "com"が含まれる可能性があります。

- **コマンド**: `python script.py /path/to/project 2`
  - グループ: "org.springframework", "org.apache"など。
  - 出力には、"org.springframework"パッケージのクラスが"org.apache"パッケージのクラスをインポートする場合、"org.springframework" -> "org.apache"が含まれる可能性があります。

### 注意点

- スクリプトは、プロジェクト内の依存関係（`all_classes`内のインポート）のみを含め、ワイルドカードインポートと自依存関係を除外する、元の動作を維持しています。
- パッケージ宣言がないクラスはスキップされ、元のスクリプトと一貫しています。
- 出力は、Graphvizなどのツールで表示できるDOT形式の有向グラフです。

この修正されたスクリプトは、パッケージ階層レベルで依存関係をグループ化するためのあなたの要件を完全に満たすはずです。