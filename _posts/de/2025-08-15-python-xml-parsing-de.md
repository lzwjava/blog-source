---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Python XML-Parsing mit xml.etree
translated: true
type: note
---

### Übersicht von xml.etree in Python

`xml.etree` ist ein eingebautes Python-Modul (speziell `xml.etree.ElementTree`) zum Parsen und Manipulieren von XML-Daten. Es bietet eine baumartige Struktur, in der Sie XML-Elemente effizient lesen, schreiben, ändern und navigieren können. Es ist leichtgewichtig und erfordert keine externen Bibliotheken, was es ideal für grundlegende XML-Aufgaben macht. Importieren Sie es mit `import xml.etree.ElementTree as ET`.

### XML parsen

Um XML in den Speicher zu laden, verwenden Sie Parsing-Methoden:

- **Aus einem String**: `ET.fromstring(xml_string)` gibt ein Element-Objekt zurück, das die Wurzel darstellt.
- **Aus einer Datei**: `ET.parse(filename)` gibt ein ElementTree-Objekt zurück, auf das Sie über `.getroot()` zugreifen können.

```python
import xml.etree.ElementTree as ET

# Aus String parsen
xml_data = "<root><child>text</child></root>"
root = ET.fromstring(xml_data)

# Aus Datei parsen
tree = ET.parse('example.xml')
root = tree.getroot()
```

### Navigation durch Elemente

Nach dem Parsen können Sie durch den XML-Baum navigieren:

- **Auf Kinder zugreifen**: Verwenden Sie `root[0]` für den indizierten Zugriff oder iterieren Sie mit `for child in root:`.
- **Elemente finden**:
  - `root.find('tag')` holt das erste passende Kindelement.
  - `root.findall('tag')` holt alle passenden Kindelemente.
- **Auf Text und Attribute zugreifen**:
  - Textinhalt: `element.text`
  - Attribute: `element.attrib` (ein Dictionary)

```python
# Beispiel XML: <bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Book {book_id}: {title}")
```

### XML ändern

Bearbeiten Sie Elemente dynamisch:

- **Elemente hinzufügen**: `ET.SubElement(parent, 'new_tag')` erstellt ein neues Kindelement und hängt es an.
- **Text/Attribute setzen**: `element.text = 'new text'`; `element.set('attr', 'value')`.
- **Elemente entfernen**: `root.remove(child)`.

```python
new_child = ET.SubElement(root, 'new_element')
new_child.text = 'Added content'
new_child.set('attr', 'value')
```

### XML schreiben

Um Änderungen zurück in XML zu speichern:

- **In einen String**: `ET.tostring(root, encoding='unicode')`.
- **In eine Datei**: `tree.write('output.xml')`.

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('output.xml', 'w') as f:
    f.write(xml_output)

# Oder direkt
tree.write('output.xml')
```

### Vollständiges Beispiel

Hier ist ein vollständiges Skript zum Parsen, Ändern und Schreiben von XML:

```python
import xml.etree.ElementTree as ET

# Eingabe-XML-String
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# Ein neues Buch hinzufügen
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Brave New World'
ET.SubElement(new_book, 'author').text = 'Huxley'

# Alle Bücher ausgeben
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} by {author}")

# In Datei schreiben
ET.tostring(root, encoding='unicode')
# Oder root.write('library.xml')
```

### Hinweise

- Behandeln Sie Namensräume mit `xmlns='{namespace}'` in Find-Abfragen, z.B. `root.find('{http://example.com}tag')`.
- Für große Dateien sollten Sie iteratives Parsen mit `ET.iterparse()` in Betracht ziehen.
- Seien Sie vorsichtig mit XML aus Benutzereingaben, um XML-Schwachstellen wie Injection zu vermeiden.
- Für komplexe Anforderungen bieten Bibliotheken wie lxml erweiterte Funktionen.