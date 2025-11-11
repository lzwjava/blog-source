---
audio: false
generated: true
lang: hant
layout: post
title: 純淨壓縮檔
translated: true
type: note
---

1. **讀取 ZIP 檔案**：使用 `zipfile.ZipFile` 讀取檔案並獲取內部所有檔案列表。
2. **篩選出無副檔名的檔案**：同時保留目錄（以 `/` 結尾的項目）。
3. **記錄被移除的檔案**：讓使用者知道哪些檔案已被排除。
4. **建立新的 ZIP 檔案**：僅包含有效檔案（具有副檔名或目錄結構的檔案）。
5. **使用 `argparse` 接收 ZIP 檔案路徑**：作為命令列參數傳入。

這確保只保留符合條件的檔案，同時維持目錄結構。🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # 分離有效檔案與無副檔名檔案（排除目錄）
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("未找到具有副檔名的有效檔案。程式結束。")
            return
        
        # 記錄被移除的檔案
        if removed_files:
            print("正在移除以下檔案（偵測到無副檔名）：")
            for f in removed_files:
                print(f" - {f}")
        
        # 建立排除無效檔案後的新壓縮檔
        with zipfile.ZipFile(output_path, 'w') as clean_zip:
            for file in valid_files:
                with zip_ref.open(file) as source:
                    clean_zip.writestr(file, source.read())

    print(f"已建立清理後的 ZIP 檔案：{output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="透過移除無副檔名檔案來清理 ZIP 檔案")
    parser.add_argument("zip_path", help="輸入 ZIP 檔案的路徑")
    args = parser.parse_args()
    clean_zip(args.zip_path)

```