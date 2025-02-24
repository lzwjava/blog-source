---
audio: true
lang: ja
layout: post
title: プロジェクトのJavaパッケージの分析
translated: true
---

ディレクトリを再帰的に分析し、`.java` ファイルで使用されているすべての Java パッケージを検索し、重複を削除し、プロジェクトで使用されているすべての一意のパッケージをリスト表示する Python スクリプトです。このスクリプトは `.java` ファイルにのみ焦点を当て、モジュールを持つプロジェクトを処理するためにすべてのサブディレクトリをトラバースします。

### Python スクリプト:

```python
import os
import sys

def find_java_files(root_dir):
    """
    指定されたディレクトリとそのサブディレクトリ内のすべての .java ファイルを再帰的に検索します。

    引数:
        root_dir (str): 検索を開始するルートディレクトリ。

    返却値:
        str: 各 .java ファイルのフルパス。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    インポートステートメントからパッケージ名を抽出します。

    パッケージ名は通常小文字で、クラス名は大文字で始まるという規約を使用します。ワイルドカードインポート (*) の場合、パッケージは '*' の前にあります。

    引数:
        import_statement (str): Java ファイルからのインポートステートメント行。

    返却値:
        str: パッケージ名、または決定できない場合は空の文字列。
    """
    # 'import' と 'static' を削除
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]

    # 残りの部分を結合し、末尾の ';' を削除
    import_path = ' '.join(parts).strip(';').strip()

    # インポートパスを '.' で分割
    identifiers = import_path.split('.')

    # 最初の識別子が大文字で始まるか '*' であるインデックスを検索
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []

    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # コマンドライン引数でルートディレクトリを確認
    if len(sys.argv) < 2:
        print("使用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    packages = set()

    # ディレクトリとサブディレクトリ内のすべての .java ファイルをトラバース
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:  # 空でないパッケージ名のみ追加
                            packages.add(package)
        except Exception as e:
            print(f"警告: ファイル {java_file} を読み取れませんでした: {e}")
            continue

    # 一意のパッケージのソートされたリストを出力
    for package in sorted(packages):
        print(package)
```

### スクリプトの使用方法:

1. スクリプトをファイルに保存します。例: `analyze_java_packages.py`。
2. コマンドラインからスクリプトを実行し、Java プロジェクトのルートディレクトリのパスを指定します:
   ```
   python analyze_java_packages.py /path/to/your/java/project
   ```
3. スクリプトは、`.java` ファイルでインポートされている一意のパッケージ名のソートされたリストを出力します。

### スクリプトの機能:

- **`.java` ファイルの検索:**
  - `os.walk()` を使用してディレクトリとそのサブディレクトリを再帰的にトラバースします。
  - `.java` で終わるすべてのファイルを特定します。

- **パッケージ名の抽出:**
  - 各 `.java` ファイルを行ごとに分析します。
  - `import` で始まる行を特定します。
  - インポートステートメントからパッケージ名を抽出し、以下を処理します:
    - 通常のインポート (例: `import java.util.List;`)
    - ワイルドカードインポート (例: `import java.util.*;`)
    - 静的インポート (例: `import static java.util.Collections.sort;`)
  - Java の命名規約に基づくヒューリスティックを使用します:
    - パッケージ名は通常小文字 (例: `java.util`)。
    - クラス名は通常大文字で始まります (例: `List`, `Collections`)。
    - ワイルドカードインポートは `*` で終わる。

- **重複の削除:**
  - すべてのパッケージ名を `set` に収集して、自動的に重複を削除します。

- **結果の出力:**
  - `set` をソートされたリストに変換し、各パッケージ名を新しい行に出力します。

### 假定と制限:

- **インポートステートメント:**
  - インポートステートメントは独自の行にあり、コメントや文字列に埋め込まれていないと仮定します。
  - 通常のインポートと静的インポート、ワイルドカードインポートを処理します。

- **命名規約:**
  - パッケージ名は小文字で、クラス名は大文字で始まるという規約に依存します。
  - 非標準的な命名 (例: 大文字のパッケージ名) は正しく処理できない場合がありますが、これは実践上稀です。

- **ファイルのエンコーディング:**
  - `.java` ファイルは UTF-8 でエンコードされていると仮定します。必要に応じて `encoding` パラメータを調整してください。

- **エラーハンドリング:**
  - 読み取れないファイルに対する基本的なエラーハンドリングを含み、警告を表示して続行します。

### 例:

Java プロジェクトに以下の `.java` ファイルがある場合:

- **File1.java:**
  ```java
  import java.util.List;
  import java.util.*;
  import java.lang.String;
  ```

- **File2.java:**
  ```java
  import java.util.Collections;
  import static java.util.Collections.sort;
  import com.example.myapp.*;
  ```

スクリプトを実行すると、以下のように出力されます:
```
com.example.myapp
java.lang
java.util
```

これは、プロジェクトでインポートされているすべての一意のパッケージをアルファベット順にリスト表示します。

### 注意点:

- スクリプトは `import` ステートメントを介してインポートされたパッケージに焦点を当てています。これらはプロジェクトが使用する外部および内部パッケージを表します。
- `.java` ファイル自体のパッケージ宣言 (例: `package com.mycompany.myapp;`) は含まれません。これらはファイルが属するパッケージを定義し、使用するパッケージではありません。
- プロジェクトにモジュールがある場合、スクリプトはすべてのサブディレクトリを再帰的に分析して、すべての `.java` ファイルが処理されるようにします。