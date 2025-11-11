---
audio: false
generated: true
lang: hant
layout: post
title: 複製數據行的Python腳本
translated: true
type: note
---

這是更新後的 Python 腳本，已修改為適用於 .xlsx 檔案而非 .xls 檔案。它使用 `openpyxl` 來處理 .xlsx 檔案，保持根據提供參數重複第三行數值的相同功能，並將輸出儲存為新的 .xlsx 檔案，在原檔案名稱後附加 "_plus.xlsx"。由於這是對先前產出物的更新，因此重用了 artifact_id。

```python
import pandas as pd
import argparse
import os

def repeat_value(value, n):
    return str(value) * n

def process_excel(input_file, n):
    df = pd.read_excel(input_file, engine='openpyxl')
    if len(df) < 3:
        raise ValueError("Excel file must have at least 3 rows")
    third_row = df.iloc[2].apply(lambda x: repeat_value(x, n))
    df.iloc[2] = third_row
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_plus.xlsx"
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Processed file saved as: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Double values in the third row of an Excel file")
    parser.add_argument("input_file", help="Path to the input Excel (.xlsx) file")
    parser.add_argument("-n", type=int, default=1, help="Number of times to repeat each value (default: 1)")
    args = parser.parse_args()
    process_excel(args.input_file, args.n)

if __name__ == "__main__":
    main()
```