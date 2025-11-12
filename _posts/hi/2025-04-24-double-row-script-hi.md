---
audio: false
generated: true
lang: hi
layout: post
title: पायथन स्क्रिप्ट से पंक्ति दोगुना करें
translated: true
type: note
---

यहाँ .xls फ़ाइलों के बजाय .xlsx फ़ाइलों के साथ काम करने के लिए संशोधित अद्यतन Python स्क्रिप्ट दी गई है। यह .xlsx फ़ाइलों को हैंडल करने के लिए `openpyxl` का उपयोग करती है, प्रदान किए गए पैरामीटर के आधार पर तीसरी पंक्ति में मानों को दोहराने का वही कार्यक्षमता रखती है, और आउटपुट को मूल फ़ाइलनाम में "_plus.xlsx" जोड़कर एक नई .xlsx फ़ाइल में सहेजती है। artifact_id का पुन: उपयोग किया गया है क्योंकि यह पिछले artifact का एक अद्यतन है।

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