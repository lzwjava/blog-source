---
audio: false
generated: true
lang: hant
layout: post
title: 在 Python 中解壓縮檔案
translated: true
type: note
---

在 Python 中解壓縮檔案：

```python
import zipfile
import os
import argparse

# 設定參數解析
parser = argparse.ArgumentParser(description="將壓縮檔解壓至同名資料夾")
parser.add_argument('zip_file', help="壓縮檔案路徑")

# 解析命令列參數
args = parser.parse_args()

# 取得壓縮檔案路徑及其所在目錄
zip_file_path = args.zip_file
directory = os.path.dirname(zip_file_path)

# 移除 .zip 副檔名以取得新資料夾名稱
folder_name = os.path.splitext(os.path.basename(zip_file_path))[0]
destination_folder = os.path.join(directory, folder_name)

# 確保目標資料夾存在
os.makedirs(destination_folder, exist_ok=True)

# 解壓縮檔案
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(destination_folder)

print(f'內容已解壓至 {destination_folder}')

```