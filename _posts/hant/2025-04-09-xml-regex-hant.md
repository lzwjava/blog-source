---
audio: false
generated: true
lang: hant
layout: post
title: XML 正則表達式腳本
translated: true
type: note
---

我將修改腳本，使用 `argparse` 來處理命令行參數。這將允許您在運行腳本時直接傳入文件路徑：

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # 讀取 XML 文件內容
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # 使用正則表達式查找所有 <c:look> 標籤
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # 輸出數字
    for number in matches:
        print(number)

def main():
    # 設置參數解析器
    parser = argparse.ArgumentParser(description='從 XML 文件的 <c:look> 標籤中提取數字')
    parser.add_argument('file_path', help='XML 文件的路徑')
    
    # 解析參數
    args = parser.parse_args()
    
    # 處理文件
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()
```

現在您可以通過以下方式從命令行運行腳本：

```
python script_name.py path/to/your/xml_file.xml
```

該腳本將：
1. 使用 `argparse` 處理文件路徑的命令行參數
2. 解析 XML 文件以查找所有 `<c:look>` 標籤
3. 提取並輸出這些標籤內的數字

這種方法使腳本更易於使用，並適用於腳本處理或批次處理。