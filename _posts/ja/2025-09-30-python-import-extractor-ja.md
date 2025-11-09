---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Pythonパッケージインポート抽出ツール
translated: true
type: note
---

### すべてのインポートパッケージを抽出するPythonスクリプト

このスクリプトは、指定されたディレクトリとそのサブディレクトリを走査し、すべてのPythonファイル（`.py`）を検索して、Pythonの`ast`モジュールを使用してインポート文を安全に構文解析し、すべてのユニークなベースモジュール名（例：`import os`からの`os`、または`from collections import defaultdict`からの`collections`）を蓄積します。ビルトインは無視し、外部モジュールに焦点を当てます。

これを`.py`ファイル（例：`extract_imports.py`）として保存し、`python extract_imports.py /path/to/directory`のようにディレクトリパスを引数として実行してください。

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    Pythonファイルを解析し、インポートされたモジュール名を抽出します。
    'import mod' および 'from mod import item' 形式を処理します。
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # ベースモジュールを取得 (例: 'import os.path' -> 'os')
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # 'from mod.sub import ...' からベースモジュールを取得
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    ディレクトリとサブディレクトリを走査し、すべてのユニークなインポート済みモジュールを収集します。
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # 一般的なビルトインを除外（オプション、これらは外部パッケージであることは稀なため）
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_imports.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("All unique imported packages:")
    for mod in modules:
        print(mod)
```

### 仕組み
- **ディレクトリ走査**: `os.walk`を使用して、すべてのサブディレクトリとファイルを再帰的に訪問します。
- **ファイルフィルタリング**: `.py`ファイルのみを処理します。
- **インポート解析**: `ast`を使用してソースコードを安全に解析し、`Import`ノードと`ImportFrom`ノードを識別します。`.`で分割してトップレベルモジュール（例：`import numpy.linalg`からの`numpy`）を捕捉します。
- **蓄積**: モジュールをセットで収集して一意性を確保し、ソートして表示します。
- **エッジケース**: ビルトインをスキップ（`excluded`セットはカスタマイズ可能）、構文エラーを適切に処理し、Unicodeファイルをサポートします。
- **出力**: ソートされたユニークなパッケージ名のリスト。自身のプロジェクトディレクトリで実行すると、`requests`、`pandas`など、インストールが必要なパッケージがリストされます。

このアプローチは、コードベース分析に効率的で、潜在的に安全でないコードの実行を回避します。改良が必要な場合（例：相対インポートの異なる処理やrequirements.txtの生成など）、詳細を提供してください！