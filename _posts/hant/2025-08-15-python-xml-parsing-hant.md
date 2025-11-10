---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python XML 解析：使用 xml.etree
translated: true
type: note
---

### Python 中的 xml.etree 概述

`xml.etree` 是 Python 的內建模組（具體為 `xml.etree.ElementTree`），用於解析和操作 XML 資料。它提供樹狀結構，可高效讀取、寫入、修改和導覽 XML 元素。它輕量且無需外部函式庫，非常適合基礎 XML 任務。透過 `import xml.etree.ElementTree as ET` 導入使用。

### 解析 XML

要將 XML 載入記憶體，可使用以下解析方法：

- **從字串解析**：`ET.fromstring(xml_string)` 會返回代表根節點的 Element 物件。
- **從檔案解析**：`ET.parse(filename)` 會返回 ElementTree 物件，可透過 `.getroot()` 存取。

```python
import xml.etree.ElementTree as ET

# 從字串解析
xml_data = "<root><child>text</child></root>"
root = ET.fromstring(xml_data)

# 從檔案解析
tree = ET.parse('example.xml')
root = tree.getroot()
```

### 導覽元素

解析後，可遍歷 XML 樹狀結構：

- **存取子元素**：使用 `root[0]` 進行索引存取，或透過 `for child in root:` 迭代。
- **尋找元素**：
  - `root.find('tag')` 獲取第一個匹配的子元素。
  - `root.findall('tag')` 獲取所有匹配的子元素。
- **存取文字與屬性**：
  - 文字內容：`element.text`
  - 屬性：`element.attrib`（字典格式）

```python
# 範例 XML：<bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Book {book_id}: {title}")
```

### 修改 XML

可動態編輯元素：

- **新增元素**：`ET.SubElement(parent, 'new_tag')` 會建立並附加新的子元素。
- **設定文字/屬性**：`element.text = 'new text'`；`element.set('attr', 'value')`。
- **移除元素**：`root.remove(child)`。

```python
new_child = ET.SubElement(root, 'new_element')
new_child.text = '新增內容'
new_child.set('attr', 'value')
```

### 寫入 XML

要將修改儲存回 XML：

- **輸出為字串**：`ET.tostring(root, encoding='unicode')`。
- **輸出至檔案**：`tree.write('output.xml')`。

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('output.xml', 'w') as f:
    f.write(xml_output)

# 或直接寫入
tree.write('output.xml')
```

### 完整範例

以下是解析、修改和寫入 XML 的完整腳本：

```python
import xml.etree.ElementTree as ET

# 輸入 XML 字串
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# 新增書籍
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Brave New World'
ET.SubElement(new_book, 'author').text = 'Huxley'

# 顯示所有書籍
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} by {author}")

# 寫入檔案
ET.tostring(root, encoding='unicode')
# 或使用 root.write('library.xml')
```

### 注意事項
- 處理命名空間時，在查詢中使用 `xmlns='{namespace}'`，例如 `root.find('{http://example.com}tag')`。
- 對於大型檔案，可考慮使用 `ET.iterparse()` 進行迭代解析。
- 處理使用者輸入的 XML 時需謹慎，以避免 XML 注入等安全性漏洞。
- 若需進階功能，可考慮使用 lxml 等函式庫。