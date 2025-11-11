---
audio: false
generated: true
lang: ja
layout: post
title: 行を複製するPythonスクリプト
translated: true
type: note
---

以下は、.xlsファイルではなく.xlsxファイルで動作するように更新されたPythonスクリプトです。このスクリプトは.xlsxファイルを扱うために`openpyxl`を使用し、指定されたパラメータに基づいて3行目の値を繰り返す同じ機能を保持し、元のファイル名に"_plus.xlsx"を追加した新しい.xlsxファイルに出力を保存します。これは以前の成果物の更新であるため、artifact_idは再利用されています。

```python
import pandas as pd
import argparse
import os

def repeat_value(value, n):
    return str(value) * n

def process_excel(input_file, n):
    df = pd.read_excel(input_file, engine='openpyxl')
    if len(df) < 3:
        raise ValueError("Excelファイルには少なくとも3行必要です")
    third_row = df.iloc[2].apply(lambda x: repeat_value(x, n))
    df.iloc[2] = third_row
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_plus.xlsx"
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"処理されたファイルは次の名前で保存されました: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Excelファイルの3行目の値を繰り返します")
    parser.add_argument("input_file", help="入力Excelファイル（.xlsx）へのパス")
    parser.add_argument("-n", type=int, default=1, help="各値を繰り返す回数（デフォルト: 1）")
    args = parser.parse_args()
    process_excel(args.input_file, args.n)

if __name__ == "__main__":
    main()
```