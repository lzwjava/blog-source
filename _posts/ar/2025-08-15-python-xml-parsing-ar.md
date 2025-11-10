---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: تحليل XML باستخدام xml.etree في بايثون
translated: true
type: note
---

### نظرة عامة على xml.etree في بايثون

`xml.etree` هي وحدة بايثون مدمجة (تحديدًا `xml.etree.ElementTree`) لتحليل ومعالجة بيانات XML. توفر بنية شبيهة بالشجرة حيث يمكنك قراءة وكتابة وتعديل والتنقل بين عناصر XML بكفاءة. إنها خفيفة الوزن ولا تتطلب مكتبات خارجية، مما يجعلها مثالية للمهام الأساسية لـ XML. استوردها باستخدام `import xml.etree.ElementTree as ET`.

### تحليل XML

لتحميل XML في الذاكرة، استخدم طرق التحليل:

- **من سلسلة نصية**: `ET.fromstring(xml_string)` تُرجع كائن Element يمثل الجذر.
- **من ملف**: `ET.parse(filename)` تُرجع كائن ElementTree، والذي يمكنك الوصول إليه عبر `.getroot()`.

```python
import xml.etree.ElementTree as ET

# التحليل من سلسلة نصية
xml_data = "<root><child>text</child></root>"
root = ET.fromstring(xml_data)

# التحليل من ملف
tree = ET.parse('example.xml')
root = tree.getroot()
```

### التنقل بين العناصر

بمجرد التحليل، يمكنك اجتياز شجرة XML:

- **الوصول إلى العناصر الفرعية**: استخدم `root[0]` للوصول المفهرس أو التكرار باستخدام `for child in root:`.
- **العثور على العناصر**:
  - `root.find('tag')` يحصل على أول عنصر فرعي مطابق.
  - `root.findall('tag')` يحصل على جميع العناصر الفرعية المطابقة.
- **الوصول إلى النص والسمات**:
  - محتوى النص: `element.text`
  - السمات: `element.attrib` (قاموس)

```python
# مثال XML: <bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Book {book_id}: {title}")
```

### تعديل XML

قم بتحرير العناصر ديناميكيًا:

- **إضافة عناصر**: `ET.SubElement(parent, 'new_tag')` ينشئ ويربط عنصرًا فرعيًا جديدًا.
- **تعيين النص/السمات**: `element.text = 'new text'`; `element.set('attr', 'value')`.
- **إزالة العناصر**: `root.remove(child)`.

```python
new_child = ET.SubElement(root, 'new_element')
new_child.text = 'Added content'
new_child.set('attr', 'value')
```

### كتابة XML

لحفظ التعديلات مرة أخرى إلى XML:

- **إلى سلسلة نصية**: `ET.tostring(root, encoding='unicode')`.
- **إلى ملف**: `tree.write('output.xml')`.

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('output.xml', 'w') as f:
    f.write(xml_output)

# أو مباشرة
tree.write('output.xml')
```

### مثال كامل

إليك نصًا برمجيًا كاملاً لتحليل وتعديل وكتابة XML:

```python
import xml.etree.ElementTree as ET

# سلسلة XML المدخلة
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# إضافة كتاب جديد
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Brave New World'
ET.SubElement(new_book, 'author').text = 'Huxley'

# طباعة جميع الكتب
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} by {author}")

# الكتابة إلى ملف
ET.tostring(root, encoding='unicode')
# أو root.write('library.xml')
```

### ملاحظات
- تعامل مع مساحات الأسماء باستخدام `xmlns='{namespace}'` في استعلامات البحث، على سبيل المثال، `root.find('{http://example.com}tag')`.
- للملفات الكبيرة، فكر في التحليل التكراري باستخدام `ET.iterparse()`.
- كن حذرًا مع XML المدخل من قبل المستخدم لتجنب ثغرات XML مثل الحقن.
- للاحتياجات المعقدة، تقدم مكتبات مثل lxml ميزات موسعة.