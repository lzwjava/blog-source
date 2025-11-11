---
audio: false
generated: true
lang: hant
layout: post
title: 比較兩個單行CSV檔案
translated: true
type: note
---

以下是一個 Python 腳本，用於比較兩個包含字串（例如 "P0001"）的單行 CSV 檔案，並識別：
- 共同項目（同時存在於兩個檔案中）
- 僅存在於第一個檔案中的項目
- 僅存在於第二個檔案中的項目

該腳本使用 `argparse` 來接收兩個 CSV 檔案路徑，讀取每個檔案的第一行，執行基於集合的比較，並將結果寫入 `comparison.txt`。

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # 設定參數解析器
    parser = argparse.ArgumentParser(description='比較兩個單行 CSV 檔案中的共同和獨有項目')
    parser.add_argument('file1_path', help='第一個 CSV 檔案的路徑')
    parser.add_argument('file2_path', help='第二個 CSV 檔案的路徑')
    
    # 解析參數
    args = parser.parse_args()
    
    try:
        # 讀取第一個 CSV 檔案的第一行
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # 讀取第二個 CSV 檔案的第一行
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # 轉換為集合以進行比較
        set1 = set(values1)
        set2 = set(values2)
        
        # 找出共同和獨有項目
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # 確定輸出目錄（使用第一個檔案的目錄）
        output_dir = os.path.dirname(args.file1_path) or '.'
        output_file = os.path.join(output_dir, 'comparison.txt')
        
        # 將結果寫入輸出檔案
        with open(output_file, 'w') as file:
            file.write("比較結果：\n\n")
            
            file.write("共同項目（存在於兩個檔案中）：\n")
            if common_items:
                for item in sorted(common_items):
                    file.write(f"{item}\n")
            else:
                file.write("無\n")
                
            file.write("\n僅存在於第一個檔案中的項目：\n")
            if unique_to_file1:
                for item in sorted(unique_to_file1):
                    file.write(f"{item}\n")
            else:
                file.write("無\n")
                
            file.write("\n僅存在於第二個檔案中的項目：\n")
            if unique_to_file2:
                for item in sorted(unique_to_file2):
                    file.write(f"{item}\n")
            else:
                file.write("無\n")
        
        print(f"比較完成。結果已儲存至 {output_file}")
        
    except FileNotFoundError as e:
        print(f"錯誤：找不到檔案 - {e}")
    except Exception as e:
        print(f"錯誤：{e}")

if __name__ == "__main__":
    main()
```

### 運作方式：
1. **輸入**：透過命令列參數接收兩個 CSV 檔案路徑。
2. **讀取**：僅讀取每個 CSV 檔案的第一行。
3. **比較**：
   - 將行轉換為集合以進行高效比較。
   - 找出：
     - **共同項目**：同時存在於兩行中的項目（集合交集）。
     - **僅存在於第一個檔案**：僅存在於第一行中的項目（集合差集：file1 - file2）。
     - **僅存在於第二個檔案**：僅存在於第二行中的項目（集合差集：file2 - file1）。
4. **輸出**：將結果寫入第一個檔案所在目錄中的 `comparison.txt`，列出：
   - 共同項目
   - 僅存在於第一個檔案中的項目
   - 僅存在於第二個檔案中的項目
   - 每個部分按字母順序排序；如果某部分為空，則寫入「無」。
5. **錯誤處理**：捕獲檔案未找到錯誤和其他異常。

### 使用範例：
將腳本儲存為 `compare_csv.py`。建立兩個 CSV 檔案，例如：
- `file1.csv`：`P0001,P0002,P0003`
- `file2.csv`：`P0001,P0004,P0003`

執行腳本：
```
python compare_csv.py file1.csv file2.csv
```

**輸出**（`comparison.txt`）：
```
比較結果：

共同項目（存在於兩個檔案中）：
P0001
P0003

僅存在於第一個檔案中的項目：
P0002

僅存在於第二個檔案中的項目：
P0004
```

### 注意事項：
- 該腳本忽略項目的位置，僅關注存在與否。
- 行中的重複項目會自動處理（集合會移除重複項）。
- 輸出寫入第一個輸入檔案所在目錄中的 `comparison.txt`。
- 如果檔案為空或沒有行，腳本會將其視為空集合。

您是否需要我修改腳本（例如，更改輸出格式或添加更多詳細資訊）？