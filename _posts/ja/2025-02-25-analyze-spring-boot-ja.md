---
audio: false
generated: true
lang: ja
layout: post
title: Spring Bootプロジェクトの解析
translated: true
type: note
---

Spring Bootプロジェクト（複数のモジュールで構成されている可能性がある）を分析し、`@GetMapping`または`@PostMapping`アノテーションで定義されたすべてのAPIを抽出するには、プロジェクトディレクトリを走査し、コントローラクラスを特定し、APIパスを抽出し、指定された形式で出力する必要があります。以下は、このタスクを達成する完全なPythonスクリプトです。提供されたコードの構造に触発されていますが、新しい要件に合わせて調整されています。出力では、各コントローラに関連するGETおよびPOSTパスが「XXController: get path post path」の形式でリストされます。

### アプローチ

1. **ディレクトリの走査**: プロジェクトディレクトリとそのサブディレクトリ内のすべての`.java`ファイルを再帰的に見つけます。
2. **コントローラの特定**: 各Javaファイルに`@Controller`または`@RestController`アノテーションがあるか確認し、コントローラクラスであることを確認します。
3. **クラスレベルのパスの抽出**: クラスレベルでの`@RequestMapping`アノテーションを探し、ベースパスを決定します。
4. **メソッドレベルのAPIの抽出**: `@GetMapping`または`@PostMapping`でアノテーションが付けられたメソッドを見つけ、それらのパスを抽出し、存在する場合はベースパスと結合します。
5. **整理と出力**: コントローラごとにGETおよびPOSTパスを収集し、指定された形式で出力します。

### Pythonスクリプト

```python
import os
import sys
import re
from collections import defaultdict

def find_java_files(root_dir):
    """
    指定されたディレクトリとそのサブディレクトリ内のすべての.javaファイルを再帰的に検索します。
    
    Args:
        root_dir (str): 検索を開始するルートディレクトリ。
    
    Yields:
        str: 各.javaファイルへのフルパス。
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_paths(line, annotation_type):
    """
    Springアノテーション（@GetMapping、@PostMapping、または@RequestMapping）からパス値を抽出します。
    
    Args:
        line (str): アノテーションを含む行。
        annotation_type (str): アノテーションのタイプ（'GetMapping'、'PostMapping'、または'RequestMapping'）。
    
    Returns:
        list: アノテーションから抽出されたパス文字列のリスト。
    """
    if annotation_type in ['GetMapping', 'PostMapping']:
        match = re.search(rf'@{annotation_type}\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # 引用符内のすべての文字列リテラルを抽出
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []
    elif annotation_type == 'RequestMapping':
        match = re.search(r'@RequestMapping\\((.*)\\)', line)
        if match:
            content = match.group(1)
            # 'value'または'path'属性を探す
            value_match = re.search(r'(value|path)\s*=\s*({[^}]*}|"[^"]*")', content)
            if value_match:
                value = value_match.group(2)
                if value.startswith('{'):
                    paths = re.findall(r'"([^"]*)"', value)
                else:
                    paths = [value.strip('"')]
                return paths
            # 'value'または'path'がない場合、直接パス指定と仮定
            paths = re.findall(r'"([^"]*)"', content)
            return paths
        return []

if __name__ == '__main__':
    # コマンドライン引数の解析
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_directory>")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    if not os.path.isdir(root_dir):
        print(f"[ERROR] The specified path is not a directory: {root_dir}")
        sys.exit(1)
    
    print(f"[INFO] Starting analysis of directory: {root_dir}")
    
    # コントローラマッピングを格納する辞書を初期化
    controllers = defaultdict(lambda: {'GET': [], 'POST': []})
    total_files = 0
    error_files = 0
    
    # すべてのJavaファイルを処理
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # ファイルがコントローラかどうかをチェック
            if any('@Controller' in line or '@RestController' in line for line in lines):
                controller_name = os.path.basename(java_file).replace('.java', '')
                
                # クラス宣言行を見つけてクラスレベルとメソッドレベルのアノテーションを分離
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
                
                # ユニークなパスを格納
                get_paths = sorted(list(set(get_paths)))
                post_paths = sorted(list(set(post_paths)))
                
                if get_paths or post_paths:
                    controllers[controller_name]['GET'] = get_paths
                    controllers[controller_name]['POST'] = post_paths
            
            total_files += 1
        except Exception as e:
            print(f"[ERROR] Could not read file {java_file}: {e}")
            error_files += 1
    
    # サマリーを出力
    print(f"[INFO] Total Java files attempted: {total_files + error_files}")
    print(f"[INFO] Successfully processed: {total_files}")
    print(f"[INFO] Files with errors: {error_files}")
    print(f"[INFO] Total controllers found: {len(controllers)}")
    
    # 指定された形式で結果を出力
    for controller, mappings in sorted(controllers.items()):
        print(f"{controller}:")
        for path in mappings['GET']:
            print(f"get {path}")
        for path in mappings['POST']:
            print(f"post {path}")
```

### 説明

- **インポート**: ディレクトリ走査に`os`、コマンドライン引数に`sys`、正規表現に`re`、コントローラデータの整理に`defaultdict`を使用します。
- **`find_java_files`**: この関数は、プロジェクトディレクトリ内のすべての`.java`ファイルを`os.walk`を使用して再帰的に取得し、複数のモジュールを自然に処理します。
- **`extract_paths`**: この関数は、`@GetMapping`、`@PostMapping`、または`@RequestMapping`アノテーションを解析してパス値を抽出します。以下を処理します：
  - 単一のパス（例：`@GetMapping("/path")`）。
  - 複数のパス（例：`@GetMapping({"/path1", "/path2"})`）。
  - 名前付き属性（例：`@RequestMapping(value = "/path")`）。
- **メインロジック**:
  - **コマンドライン処理**: 提供されたスクリプトと同様に、ルートディレクトリを入力として受け取ります。
  - **コントローラ検出**: ファイル内容に`@Controller`または`@RestController`があるかチェックします。
  - **ベースパス**: クラス宣言前のクラスレベルの`@RequestMapping`パスを抽出します。
  - **API抽出**: クラス宣言後の行を`@GetMapping`および`@PostMapping`について処理し、パスをベースパスと結合します。
  - **出力**: 各コントローラとそのGETおよびPOSTパスを、「get」または「post」を接頭辞として1行ずつ出力します。
- **エラーハンドリング**: ファイル読み込み中の例外をキャッチして報告し、提供されたコードの堅牢性を反映しています。

### サンプル出力

`UserController.java`ファイルを含むSpring Bootプロジェクトの場合：

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

`python script.py /path/to/project`を実行すると、以下のように出力される可能性があります：

```
[INFO] Starting analysis of directory: /path/to/project
[INFO] Total Java files attempted: 10
[INFO] Successfully processed: 10
[INFO] Files with errors: 0
[INFO] Total controllers found: 1
UserController:
get /users/all
post /users/create
```

### 注意点

- **簡略化**: このスクリプトは、アノテーションが単一行にあり、パスが複雑な式を含まない文字列リテラルであると仮定しています。本番環境での使用には、Javaパーサーの方がより堅牢かもしれません。
- **GETおよびPOSTのみ**: 要求に応じて、`@GetMapping`および`@PostMapping`に焦点を当て、PUTやDELETEなどの他のメソッドは無視します（ただし、思考トレースではメソッドを持つ`@RequestMapping`を考慮しました）。
- **パスの連結**: クラスレベルとメソッドレベルのパスを直接結合します（例：`/users` + `/all` = `/users/all`）。Springは複数のスラッシュを正規化するため、表示目的ではこれで十分です。

このスクリプトは、クエリの要件を満たしながら、提供されたコードと同様の構造を維持し、親しみやすさと信頼性を確保します。