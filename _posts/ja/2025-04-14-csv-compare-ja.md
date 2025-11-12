---
audio: false
generated: true
lang: ja
layout: post
title: 単一行CSVの比較
translated: true
type: note
---

以下は、文字列（例："P0001"）を含む2つの単一行CSVファイルを比較し、以下を識別するPythonスクリプトです：
- 共通アイテム（両方のファイルに存在）
- 最初のファイルにのみ存在するアイテム
- 2番目のファイルにのみ存在するアイテム

このスクリプトは`argparse`を使用して2つのCSVファイルパスを受け取り、それぞれから最初の行を読み取り、セットベースの比較を実行し、結果を`comparison.txt`に書き込みます。

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # 引数パーサーの設定
    parser = argparse.ArgumentParser(description='2つの単一行CSVファイルを比較し、共通アイテムと固有アイテムを識別します')
    parser.add_argument('file1_path', help='最初のCSVファイルへのパス')
    parser.add_argument('file2_path', help='2番目のCSVファイルへのパス')
    
    # 引数の解析
    args = parser.parse_args()
    
    try:
        # 最初のCSVファイルの最初の行を読み取る
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # 2番目のCSVファイルの最初の行を読み取る
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # 比較のためにセットに変換
        set1 = set(values1)
        set2 = set(values2)
        
        # 共通アイテムと固有アイテムを検索
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # 出力ディレクトリの決定（最初のファイルのディレクトリを使用）
        output_dir = os.path.dir