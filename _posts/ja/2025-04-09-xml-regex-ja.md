---
audio: false
generated: true
lang: ja
layout: post
title: XML正規表現スクリプト
translated: true
type: note
---

スクリプトを`argparse`を使用してコマンドライン引数を処理するように修正します。これにより、スクリプト実行時にファイルパスを直接渡せるようになります：

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # XMLファイルの内容を読み込む
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # 正規表現を使用して全ての<c:look>タグを検索
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # 数値を出力
    for number in matches:
        print(number)

def main():
    # 引数パーサーを設定
    parser = argparse.ArgumentParser(description='XMLファイルから<c:look>タグ内の数値を抽出')
    parser.add_argument('file_path', help='XMLファイルへのパス')
    
    # 引数を解析
    args = parser.parse_args()
    
    # ファイルを処理
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()
```

これで、以下のようにコマンドラインからスクリプトを実行できます：

```
python script_name.py path/to/your/xml_file.xml
```

このスクリプトは以下の処理を行います：
1. `argparse`を使用してファイルパスのコマンドライン引数を処理
2. XMLファイルを解析して全ての`<c:look>`タグを検索
3. これらのタグ内の数値を抽出して表示

このアプローチにより、スクリプトはよりユーザーフレンドリーになり、スクリプト処理やバッチ処理に適したものになります。