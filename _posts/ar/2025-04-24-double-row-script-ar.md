---
audio: false
generated: true
lang: ar
layout: post
title: برنامج بايثون لمضاعفة الصفوف
translated: true
type: note
---

إليك النص البرمجي المحدث بلغة Python المُعدل للعمل مع ملفات .xlsx بدلاً من ملفات .xls. يستخدم `openpyxl` للتعامل مع ملفات .xlsx، ويحافظ على الوظيفة نفسها المتمثلة في تكرار القيم في الصف الثالث بناءً على المعامل المُقدم، ويحفظ المخرجات في ملف .xlsx جديد مع إلحاق "_plus.xlsx" باسم الملف الأصلي. تم إعادة استخدام `artifact_id` نظرًا لأن هذا تحديث للقطعة السابقة.

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