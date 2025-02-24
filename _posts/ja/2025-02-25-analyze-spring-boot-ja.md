---
audio: false
lang: ja
layout: post
title: Spring Bootプロジェクトの分析
translated: true
---

Spring Boot プロジェクト（複数のモジュールから構成される場合も含む）を分析し、`@GetMapping`または`@PostMapping`アノテーションで定義されたすべてのAPIを抽出するには、プロジェクトディレクトリをトラバースし、コントローラークラスを特定し、APIパスを抽出し、指定された形式で表示する必要があります。以下は、提供されたコードの構造に基づきながら新しい要件に合わせて調整された、このタスクを実行する完全なPythonスクリプトです。出力は、各コントローラーとその関連するGETおよびPOSTパスを「XXController: get path post path」形式でリストします。

### 手法

1. **ディレクトリのトラバース**: プロジェクトディレクトリとそのサブディレクトリ内のすべての`.java`ファイルを再帰的に検索します。
2. **コントローラーの特定**: 各Javaファイルを`@Controller`または`@RestController`アノテーションを確認し、コントローラークラスであることを確認します。
3. **クラスレベルのパスの抽出**: クラスレベルの`@RequestMapping`アノテーションを検索して、ベースパスを決定します。
4. **メソッドレベルのAPIの抽出**: `@GetMapping`または`@PostMapping`でアノテーションされたメソッドを検索し、そのパスを抽出し、ベースパスが存在する場合はそれを組み合わせます。
5. **整理と表示**: 各コントローラーのGETおよびPOSTパスを収集し、指定された形式で表示します。

### Pythonスクリプト

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    指定されたディレクトリとそのサブディレクトリ内のすべての.javaファイルを再帰的に検索します。

    引数:
        root_dir (str): 検索を開始するルートディレクトリ。

    返り値:
        str: 各.javaファイルのフルパス。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    Springアノテーション(@GetMapping, @PostMapping, または @RequestMapping)からパス値を抽出します。

    引数:
        line (str): アノテーションを含む行。
        annotation_type (str): アノテーションの種類('GetMapping', 'PostMapping', または 'RequestMapping'）。

    返り値:
        list: アノテーションから抽出されたパス文字列のリスト。
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\((.*)\)', line)
        if match:
            content = match.group(1)
            # クォート内のすべての文字列リテラルを抽出
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\((.*)\)', line)
        if match:
            content = match.group(1)
            # 'value'または'path'属性を検索
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # 'value'または'path'がなければ、直接のパス指定を仮定
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # コマンドライン引数の解析
    if len(sys.argv) != 2:
        print("使用法: python script.py <root_directory>")
        sys.exit(1)

    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] 指定されたパスはディレクトリではありません: {root_dir}")
        sys.exit(1)

    print(f"[INFO] ディレクトリの分析を開始: {root_dir}")

    # コントローラーマッピングを保存するための辞書を初期化
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0

    # すべてのJavaファイルを処理
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            # ファイルがコントローラーであるかどうかを確認
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')

                # クラス宣言行を検索して、クラスレベルとメソッドレベルのアノテーションを分離
                class_line_index = None
                for i, line in enumerate(lines):
                    if re.search(r'public\s+(class|abstract\s+class|interface)\s+\w+', line):
                        class_line_index = i
                        break
                if class_line_index is None:
                    continue

                # クラスレベルの@RequestMappingをベースパスとして抽出
                base_paths = []
                for line in lines[:class_line_index]:
                    if re.search(r'\s*@RequestMapping', line):
                        base_paths = extract_paths(line, 'RequestMapping')
                        break
                if not base_paths:
                    base_paths = ['']

                # メソッドレベルの@GetMappingと@PostMappingを抽出
                get_paths = []
                post_paths = []
                for line in lines[class_line_index:]:
                    if re.search(r'\s*@GetMapping', line):
                        paths = extract_paths(line, 'GetMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                get_paths.append(full_path)
                    elif re.search(r'\s*@PostMapping', line):
                        paths = extract_paths(line, 'PostMapping')
                        for base in base_paths:
                            for path in paths:
                                full_path = base + path
                                post_paths.append(full_path)

                # 一意のパスを保存
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))

                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths

            total_files += 1
        except Exception as e:
            print(f"[ERROR] ファイル {java_file} を読み取ることができませんでした: {e}")
            error_files += 1

    # サマリーを表示
    print(f"[INFO] 試行されたJavaファイルの合計: {total_files + error_files}")
    print(f"[INFO] 成功した処理: {total_files}")
    print(f"[INFO] エラーが発生したファイル: {error_files}")
    print(f"[INFO] 見つかったコントローラーの合計: {len(controllers)}")

    # 指定された形式で結果を表示
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### 説明

- **インポート**: ディレクトリのトラバースには`os`を、コマンドライン引数には`sys`を、正規表現には`re`を、コントローラーデータの整理には`defaultdict`を使用します。
- **`find_java_files`**: この関数は、プロジェクトディレクトリ内のすべての`.java`ファイルを再帰的に返します。`os.walk`を使用して、複数のモジュールを自然に処理します。
- **`extract_paths`**: この関数は、`@GetMapping`、`@PostMapping`、または`@RequestMapping`アノテーションからパス値を解析します。以下を処理します。
  - 単一のパス（例：`@GetMapping("/path")`）。
  - 複数のパス（例：`@GetMapping({"/path1", "/path2"})`）。
  - 名前付き属性（例：`@RequestMapping(value = "/path")`）。
- **メインロジック**:
  - **コマンドラインの処理**: ルートディレクトリを入力として取り、提供されたスクリプトと同様に処理します。
  - **コントローラーの検出**: ファイルの内容に`@Controller`または`@RestController`が含まれているかどうかを確認します。
  - **ベースパス**: クラス宣言の前にクラスレベルの`@RequestMapping`パスを抽出します。
  - **APIの抽出**: クラス宣言の後に`@GetMapping`および`@PostMapping`を処理し、パスをベースパスと組み合わせます。
  - **出力**: 各コントローラーとそのGETおよびPOSTパスを1行ずつ表示し、「get」または「post」でプレフィックスを付けます。
- **エラーハンドリング**: ファイルの読み取り中に例外をキャッチし、提供されたコードの信頼性を反映して報告します。

### サンプル出力

Spring Bootプロジェクトに`UserController.java`というファイルがある場合：

```java
@RestController
@RequestMapping("/users")
public class UserController {
    @GetMapping("/all")
    public ResponseEntity<?> getAllUsers() { ... }

    @PostMapping("/create")
    public ResponseEntity<?> createUser() { ... }
}
```

`python script.py /path/to/project`を実行すると、以下のような出力が得られます：

```
[INFO] ディレクトリの分析を開始: /path/to/project
[INFO] 試行されたJavaファイルの合計: 10
[INFO] 成功した処理: 10
[INFO] エラーが発生したファイル: 0
[INFO] 見つかったコントローラーの合計: 1
UserController:
get /users/all
post /users/create
```

### 注意点

- **簡略化**: スクリプトは、アノテーションが1行に収まっていることを前提としており、パスが文字列リテラルで複雑な式を含まないことを前提としています。生産用には、Javaパーサーがより強力です。
- **GETとPOSTのみ**: 要求に従い、`@GetMapping`および`@PostMapping`に焦点を当てています。PUTやDELETEなどの他のメソッドは無視されます（ただし、考慮された思考トレースでは、`@RequestMapping`とメソッドが含まれていました）。
- **パスの連結**: クラスレベルとメソッドレベルのパスを直接連結します（例：`/users` + `/all` = `/users/all`）。Springは複数のスラッシュを正規化するため、表示目的には十分です。

このスクリプトは、提供されたコードの構造に基づきながら、要求に応じて構造を維持し、信頼性を確保しています。