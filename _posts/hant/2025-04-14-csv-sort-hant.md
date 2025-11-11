---
audio: false
generated: true
lang: hant
layout: post
title: CSV 排序腳本
translated: true
type: note
---

我將創建一個使用 argparse 解析 CSV 檔案路徑的 Python 腳本，將單行逗號分隔值按字母順序排序，並將結果輸出到名為「name_sorted.csv」的檔案中。

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # 設定參數解析器
    parser = argparse.ArgumentParser(description='將單行 CSV 檔案按字母順序排序')
    parser.add_argument('file_path', help='輸入 CSV 檔案的路徑')
    
    # 解析參數
    args = parser.parse_args()
    
    try:
        # 獲取目錄和檔案名稱
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # 建立輸出檔案名稱
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # 讀取輸入的 CSV 檔案
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # 僅獲取第一行
            for row in reader:
                values = row
                break
        
        # 將值按字母順序排序
        sorted_values = sorted(values)
        
        # 寫入輸出檔案
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"成功排序值並儲存至 {output_file}")
        
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{args.file_path}'")
    except Exception as e:
        print(f"錯誤：{e}")

if __name__ == "__main__":
    main()
```

此腳本：
1. 使用 argparse 獲取輸入檔案路徑
2. 開啟 CSV 檔案並僅讀取第一行
3. 將值按字母順序排序
4. 將排序後的值寫入「name_sorted.csv」

要執行此腳本，請將其儲存為檔案（例如「sort_csv.py」），如有需要請將其設為可執行，並使用您的 CSV 檔案路徑執行：

```
python sort_csv.py path/to/your/file.csv
```

您需要我詳細解釋程式碼的任何部分嗎？