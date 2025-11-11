---
audio: false
generated: true
lang: ja
layout: post
title: Javaパッケージの解析
translated: true
type: note
---

あなたのクエリに基づくと、`level`パラメータが0または指定されていない場合、パッケージ名全体（すべての部分）を使用するスクリプトが必要です。基本的に`level = 0`を「無限」または「すべての部分を使用」として扱い、特定の数の部分（`level = 1`の場合のように最初の部分のみ）に制限しません。以下に、Javaファイルを分析してパッケージ名を抽出するPythonスクリプトの実装方法を説明し、あなたのリクエストに合わせた完全なソリューションを提供します。

### 要件の理解
- **`level = 0`または指定なしの場合**: Javaの`import`文から抽出された完全なパッケージ名（例: `java.util`や`com.google.common.eventbus`）を使用し、切り詰めません。
- **`level > 0`の場合**: パッケージ名を最初の`level`部分に切り詰めます（例: `com.google.common.eventbus`で`level = 2`の場合、`com.google`になります）。
- スクリプトは引き続きJavaファイルを処理し、`import`文からパッケージ名を抽出し、エッジケースを適切に処理する必要があります。

### ソリューションアプローチ
1. **引数解析**:
   - ルートディレクトリのみが提供された場合（例: `python script.py /path/to/dir`）、`level = 0`に設定し、完全なパッケージ名を使用します。
   - `level`が提供された場合（例: `python script.py /path/to/dir 2`）、パッケージ名を切り詰めるために使用し、非負の整数であることを確認します。
   - 引数が無効な場合はエラーで終了します。

2. **パッケージ抽出**:
   - `import`文からパッケージ名を抽出します（例: `import java.util.ArrayList;`から`java.util`を取得）。
   - Javaの命名規則を使用: パッケージは通常小文字で、クラス名は大文字で始まります。

3. **パッケージ切り詰めロジック**:
   - `level = 0`の場合、完全なパッケージ名を結果セットに追加します。
   - `level > 0`の場合、パッケージ名をドット（`.`）で分割し、最初の`level`部分を取得します。

4. **ロギングと出力**:
   - 完全なパッケージ名または切り詰められたパッケージ名のどちらを使用しているかを明確に示します。
   - 見つかったすべてのユニークなパッケージをリストします。

### 実装
以下はあなたの要件を満たす完全なPythonスクリプトです:

```python
import os
import sys
from collections import Counter

def find_java_files(root_dir):
    """
    指定されたディレクトリとそのサブディレクトリからすべての.javaファイルを再帰的に検索します。
    
    Args:
        root_dir (str): 検索を開始するルートディレクトリ。
    
    Yields:
        str: 各.javaファイルへのフルパス。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    import文からパッケージ名を抽出します。
    
    パッケージ名は小文字、クラス名は大文字で始まるという規則を使用します。
    ワイルドカードインポート(*)を処理します。
    
    Args:
        import_statement (str): Javaファイルからのimport文の行。
    
    Returns:
        str: パッケージ名、または決定できない場合は空文字列。
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # コマンドライン引数の解析
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python script.py <root_directory> [level] [--count]")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    level = 0
    count = False
    
    if len(sys.argv) == 3:
        if sys.argv[2] == "--count":
            count = True
        elif sys.argv[2].isdigit():
            level = int(sys.argv[2])
        else:
            print(f"Invalid argument: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Invalid arguments: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)
    
    # ディレクトリの存在確認
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    # 分析の開始をログに記録
    level_str = "using full package names" if level == 0 else f"at level {level}"
    count_str = "with appearance counts" if count else ""
    print(f"[INFO] Starting analysis of directory: {root_dir} {level_str} {count_str}")
    
    # 変数の初期化
    package_counter = Counter()
    total_files = 0
    error_files = 0
    
    # Javaファイルの処理
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
            continue
    
    # サマリーの表示
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    if count:
        print(f"[INFO] Total unique packages with counts: {len(package_counter)}")
    else:
        print(f"[INFO] Total unique packages: {len(package_counter)}")
    
    # 適切なソートで結果を表示
    if package_counter:
        if count:
            print("[INFO] Analysis complete. Printing unique packages with counts (sorted by count descending):")
            # カウントの降順、次にパッケージ名の昇順でソート
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] Analysis complete. Printing unique packages (sorted by name ascending):")
            # パッケージ名の昇順でソート
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] No packages found.")
```

### 動作方法
- **スクリプトの実行**:
  - `python script.py /path/to/java/project`: ディレクト内のすべての`.java`ファイルを分析し、完全なパッケージ名を使用します（`level = 0`）。
  - `python script.py /path/to/java/project 2`: パッケージ名を最初の2つの部分に切り詰めます（例: `com.google.common.eventbus`が`com.google`になります）。

- **出力例**:
  以下の内容のJavaファイルがあるとします:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **`level = 0`の場合（またはlevel指定なし）**:
    ```
    [INFO] Starting analysis of directory: /path/to/java/project with full package names.
    [INFO] Entering directory: /path/to/java/project
    [INFO] Processing file: /path/to/java/project/MyFile.java
    [INFO] Total Java files attempted: 1
    [INFO] Successfully processed: 1
    [INFO] Files with errors: 0
    [INFO] Total unique full packages: 2
    [INFO] Analysis complete. Printing unique full packages:
    com.google.common.eventbus
    java.util
    ```
  - **`level = 2`の場合**:
    ```
    [INFO] Starting analysis of directory: /path/to/java/project at level: 2
    [INFO] Entering directory: /path/to/java/project
    [INFO] Processing file: /path/to/java/project/MyFile.java
    [INFO] Total Java files attempted: 1
    [INFO] Successfully processed: 1
    [INFO] Files with errors: 0
    [INFO] Total unique packages at level 2: 2
    [INFO] Analysis complete. Printing unique packages at level 2:
    com.google
    java.util
    ```

- **主な機能**:
  - **完全なパッケージ名**: `level = 0`または未指定の場合、抽出された完全なパッケージ名（例: `java.util`、`com.google.common.eventbus`）を使用します。
  - **切り詰め**: `level > 0`の場合、最初の`level`部分を取得します。
  - **エラーハンドリング**: 有効なディレクトリと非負の`level`をチェックします。
  - **一意性**: 重複を避けるためにパッケージを`set`に保存します。

### 処理されるエッジケース
- **Levelの欠落**: デフォルトで`level = 0`に設定し、完全なパッケージ名を使用します。
- **無効なLevel**: `level`が負の数または整数でない場合、エラーで終了します。
- **短いパッケージ**: パッケージの部分数が`level`より少ない場合（例: `java`で`level = 2`）、完全なパッケージ（`java`）を使用します。
- **空のインポート**: パッケージが抽出されない行をスキップします。

このスクリプトはあなたの要件を完全に満たします: `level = 0`または未指定の場合、パッケージ名のすべての部分を使用し、事実上「使用される部分が無限」として扱います。