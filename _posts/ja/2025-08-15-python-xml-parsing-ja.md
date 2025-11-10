---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Pythonによるxml.etreeを使ったXML解析
translated: true
type: note
---

### Pythonにおけるxml.etreeの概要

`xml.etree`はPythonに組み込まれたモジュール（具体的には`xml.etree.ElementTree`）で、XMLデータの解析と操作を行います。XML要素を読み取り、書き込み、変更し、効率的にナビゲートするためのツリー構造を提供します。軽量で外部ライブラリが不要なため、基本的なXMLタスクに理想的です。`import xml.etree.ElementTree as ET`でインポートします。

### XMLの解析

XMLをメモリに読み込むには、以下の解析メソッドを使用します：

- **文字列から**: `ET.fromstring(xml_string)`はルートを表すElementオブジェクトを返します。
- **ファイルから**: `ET.parse(filename)`はElementTreeオブジェクトを返し、`.getroot()`でアクセスできます。

```python
import xml.etree.ElementTree as ET

# 文字列から解析
xml_data = "<root><child>text</child></root>"
root = ET.fromstring(xml_data)

# ファイルから解析
tree = ET.parse('example.xml')
root = tree.getroot()
```

### 要素のナビゲーション

解析後、XMLツリーを走査できます：

- **子要素へのアクセス**: インデックスアクセスには`root[0]`を、反復処理には`for child in root:`を使用します。
- **要素の検索**:
  - `root.find('tag')`は最初に一致する子要素を取得します。
  - `root.findall('tag')`は一致するすべての子要素を取得します。
- **テキストと属性へのアクセス**:
  - テキスト内容: `element.text`
  - 属性: `element.attrib`（辞書型）

```python
# 例 XML: <bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Book {book_id}: {title}")
```

### XMLの変更

要素を動的に編集します：

- **要素の追加**: `ET.SubElement(parent, 'new_tag')`は新しい子要素を作成して追加します。
- **テキスト/属性の設定**: `element.text = 'new text'`; `element.set('attr', 'value')`。
- **要素の削除**: `root.remove(child)`。

```python
new_child = ET.SubElement(root, 'new_element')
new_child.text = '追加された内容'
new_child.set('attr', 'value')
```

### XMLの書き出し

変更をXMLに保存するには：

- **文字列へ**: `ET.tostring(root, encoding='unicode')`。
- **ファイルへ**: `tree.write('output.xml')`。

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('output.xml', 'w') as f:
    f.write(xml_output)

# または直接
tree.write('output.xml')
```

### 完全な例

XMLを解析、変更、書き出す完全なスクリプト例：

```python
import xml.etree.ElementTree as ET

# 入力XML文字列
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# 新しい本を追加
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Brave New World'
ET.SubElement(new_book, 'author').text = 'Huxley'

# すべての本を表示
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} by {author}")

# ファイルに書き出し
ET.tostring(root, encoding='unicode')
# または root.write('library.xml')
```

### 注意点
- 名前空間は`find`クエリで`xmlns='{namespace}'`を使用して扱います（例: `root.find('{http://example.com}tag')`）。
- 大きなファイルには`ET.iterparse()`を使った反復解析を検討してください。
- XMLの脆弱性（インジェクションなど）を避けるため、ユーザー入力のXMLには注意してください。
- 複雑な要件には、lxmlなどの拡張機能を提供するライブラリを検討してください。