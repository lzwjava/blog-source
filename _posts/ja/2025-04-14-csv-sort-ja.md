---
audio: false
generated: true
lang: ja
layout: post
title: CSVソータースクリプト
translated: true
type: note
---

CSVファイルのパスを解析するためにargparseを使用し、カンマ区切りの単一行の値をアルファベット順にソートし、結果を「name_sorted.csv」というファイルに出力するPythonスクリプトを作成します。

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # 引数パーサーの設定
    parser = argparse.ArgumentParser(description='単一行のCSVファイルをアルファベット順にソートします')
    parser.add_argument('file_path', help='入力CSVファイルのパス')
    
    # 引数の解析
    args = parser.parse_args()
    
    try:
        # ディレクトリとファイル名を取得
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # 出力ファイル名を作成
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # 入力CSVファイルを読み込む
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # 最初の行のみを取得
            for row in reader:
                values = row
                break
        
        # 値をアルファベット順にソート
        sorted_values = sorted(values)
        
        # 出力ファイルに書き込む
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"値をソートし、{output_file}に保存しました")
        
    except FileNotFoundError:
        print(f"エラー: ファイル '{args.file_path}' が見つかりません")
    except Exception as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    main()
```

このスクリプトは以下のことを行います：
1. argparseを使用して入力ファイルのパスを取得
2. CSVファイルを開き、最初の行のみを読み込み
3. 値をアルファベット順にソート
4. ソートされた値を「name_sorted.csv」に書き込み

スクリプトを実行するには、ファイル（例：「sort_csv.py」）に保存し、必要に応じて実行可能にして、CSVファイルのパスを指定して実行します：

```
python sort_csv.py path/to/your/file.csv
```