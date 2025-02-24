---
audio: true
lang: ja
layout: post
title: Java 依存関係の分析
translated: true
---

以下は、プロジェクト内のすべての `.java` ファイルをスキャンし、インポートステートメントに基づいて依存関係を分析し、DOT形式の「依存テキスト」として依存関係グラフを出力するPythonスクリプトです。このスクリプトは、プロジェクト内のクラス間の内部依存関係に焦点を当て、Graphvizなどのツールを使用して視覚化できる明確な表現を提供します。

### スクリプト概要
スクリプトは以下の手順で動作します：
1. **プロジェクトディレクトリをスキャン**し、再帰的にすべての `.java` ファイルを検索します。
2. **依存関係を分析**し、各 `.java` ファイルからパッケージ宣言とインポートステートメントを抽出します。
3. **依存テキストを出力**し、プロジェクト内で1つのクラスが他のクラスをインポートする場合に、クラス間の有向エッジを示すDOT形式の依存関係グラフを出力します。

以下に、完全なスクリプトを示します：

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    .java ファイルからパッケージ名を抽出します。

    引数:
        file_path (str): .java ファイルへのパス。

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
        print(f"警告: {file_path} を読み取れませんでした: {e}")
    return None

def get_specific_imports(file_path):
    """
    .java ファイルから特定のクラスインポートを抽出し、ワイルドカードインポートを除外します。

    引数:
        file_path (str): .java ファイルへのパス。

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
        print(f"警告: {file_path} を読み取れませんでした: {e}")
    return imports

if __name__ == '__main__':
    # コマンドライン引数を確認
    if len(sys.argv) != 2:
        print("使用法: python script.py <ルートディレクトリ>")
        sys.exit(1)

    root_dir = sys.argv[1]
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

    # 依存関係を保存: クラス -> そのクラスが依存するクラスのセット
    dependencies = defaultdict(set)

    # 第二パス: 特定のインポートに基づいて依存関係を分析
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
                        # プロジェクト内のクラスに対する依存関係のみを含める
                        # 自依存を除外
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # DOT形式で依存関係グラフを出力
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### 使用方法
#### 1. **コマンドライン入力**
- スクリプトは1つの引数を期待します: Javaプロジェクトのルートディレクトリ。
- 使用例: `python script.py /path/to/project`
- 引数が提供されない場合、使用方法を表示して終了します。

#### 2. **`.java` ファイルの検索**
- `os.walk()` を使用して指定されたディレクトリを再帰的にトラバースし、`.java` で終わるすべてのファイルを特定します。

#### 3. **クラス情報の抽出**
- **パッケージの抽出**: `get_package` 関数は各 `.java` ファイルを読み取り、正規表現 (`^\s*package\s+([\w.]+);`）を使用してパッケージ宣言（例: `package com.mycompany.myproject;`）を検索します。
  - パッケージが見つからない場合またはファイルが読み取れない場合は `None` を返します。
- **クラス名**: ファイル名とクラス名が一致していると仮定します（例: `MyClass.java` は `MyClass` を定義）。
- **完全修飾名**: パッケージとクラス名を組み合わせます（例: `com.mycompany.myproject.MyClass`）。

#### 4. **すべてのクラスの収集**
- 第一パスで、プロジェクト内のすべての完全修飾クラス名のセットを構築し、後で迅速に参照できます。

#### 5. **依存関係の分析**
- **インポートの抽出**: `get_specific_imports` 関数は、正規表現 (`^\s*import\s+([\w.]+);`）を使用してインポートステートメントを抽出し、ワイルドカードインポート（例: `import java.util.*;`）を除外します。
  - 例: `import com.mycompany.myproject.utils.Helper;` から `com.mycompany.myproject.utils.Helper` を抽出します。
- **依存関係のマッピング**: 各 `.java` ファイルに対して:
  - 完全修飾クラス名を取得します。
  - 特定のインポートを確認します。
  - インポートされたクラスがプロジェクトのクラスセットに含まれており、自身のクラスでない場合、依存関係を追加します。

#### 6. **依存テキストの出力**
- DOT形式の有向グラフを出力します:
  - `digraph G {` で始まります。
  - 各依存関係を持つクラスに対して、エッジを出力します（例: `"ClassA" -> "ClassB";`）。
  - `}` で終了します。
- クラスと依存関係は一貫した出力のためにソートされます。
- 出力例:
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### 使用例
1. スクリプトを `analyze_deps.py` として保存します。
2. 実行します:
   ```bash
   python analyze_deps.py /path/to/java/project
   ```
3. 出力をファイルにリダイレクトします:
   ```bash
   python analyze_deps.py /path/to/java/project > dependencies.dot
   ```
4. Graphvizで視覚化します:
   ```bash
   dot -Tpng dependencies.dot -o dependencies.png
   ```
   これにより、依存関係グラフを示すPNG画像が生成されます。

### 假定と制限
- **ファイルごとに1つのパブリッククラス**: 各 `.java` ファイルが1つのパブリッククラスを含み、ファイル名と同じ名前であると仮定します。
- **インポートに基づく依存関係**: 特定のインポートステートメント（例: `import com.example.SomeClass;`）に基づく依存関係のみを考慮し、ワイルドカードインポート（`import com.example.*;`）や同一パッケージ内の参照（インポートが不要）を無視します。
- **内部依存関係に焦点**: プロジェクト内のクラス間の依存関係のみを追跡し、外部ライブラリは無視します。
- **基本的なパース**: 簡単さのために正規表現を使用していますが、これはエッジケース（例: コメント内のインポート）を抜け落ちる可能性があります。完全なJavaパーサはより強力ですが複雑です。

### カスタマイズ
- **出力形式**: 出力形式を変更するために、print文を変更できます（例: DOT形式ではなく、プレーンリスト）。
- **エラーハンドリング**: 試行-例外ブロックを使用して、読み取れないファイルをスキップするように強化されています。
- **範囲**: 外部依存関係や同一パッケージ内の依存関係を含めるために、より深いコード解析で拡張できます。

このスクリプトは、プロジェクトの内部クラス関係を通じてJavaプロジェクトの構造を理解するための実用的な出発点を提供します。