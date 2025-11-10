---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Análisis XML con Python y xml.etree
translated: true
type: note
---

### Resumen de xml.etree en Python

`xml.etree` es un módulo integrado de Python (específicamente `xml.etree.ElementTree`) para analizar y manipular datos XML. Proporciona una estructura en forma de árbol donde puedes leer, escribir, modificar y navegar por elementos XML de manera eficiente. Es liviano y no requiere bibliotecas externas, lo que lo hace ideal para tareas XML básicas. Impórtalo con `import xml.etree.ElementTree as ET`.

### Analizar XML

Para cargar XML en memoria, utiliza métodos de análisis:

- **Desde una cadena**: `ET.fromstring(xml_string)` devuelve un objeto Element que representa la raíz.
- **Desde un archivo**: `ET.parse(nombre_archivo)` devuelve un objeto ElementTree, al que puedes acceder mediante `.getroot()`.

```python
import xml.etree.ElementTree as ET

# Analizar desde una cadena
xml_data = "<root><child>texto</child></root>"
root = ET.fromstring(xml_data)

# Analizar desde un archivo
tree = ET.parse('ejemplo.xml')
root = tree.getroot()
```

### Navegar por Elementos

Una vez analizado, puedes recorrer el árbol XML:

- **Acceder a hijos**: Usa `root[0]` para acceso indexado o itera con `for child in root:`.
- **Encontrar elementos**:
  - `root.find('etiqueta')` obtiene el primer hijo coincidente.
  - `root.findall('etiqueta')` obtiene todos los hijos coincidentes.
- **Acceder a texto y atributos**:
  - Contenido de texto: `element.text`
  - Atributos: `element.attrib` (un diccionario)

```python
# Ejemplo XML: <bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Libro {book_id}: {title}")
```

### Modificar XML

Edita elementos dinámicamente:

- **Añadir elementos**: `ET.SubElement(padre, 'nueva_etiqueta')` crea y adjunta un nuevo hijo.
- **Establecer texto/atributos**: `element.text = 'nuevo texto'`; `element.set('attr', 'valor')`.
- **Eliminar elementos**: `root.remove(hijo)`.

```python
new_child = ET.SubElement(root, 'nuevo_elemento')
new_child.text = 'Contenido añadido'
new_child.set('attr', 'valor')
```

### Escribir XML

Para guardar modificaciones de nuevo en XML:

- **A una cadena**: `ET.tostring(root, encoding='unicode')`.
- **A un archivo**: `tree.write('salida.xml')`.

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('salida.xml', 'w') as f:
    f.write(xml_output)

# O directamente
tree.write('salida.xml')
```

### Ejemplo Completo

Aquí hay un script completo para analizar, modificar y escribir XML:

```python
import xml.etree.ElementTree as ET

# Cadena XML de entrada
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# Añadir un nuevo libro
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Brave New World'
ET.SubElement(new_book, 'author').text = 'Huxley'

# Imprimir todos los libros
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} by {author}")

# Escribir a archivo
ET.tostring(root, encoding='unicode')
# O root.write('biblioteca.xml')
```

### Notas
- Maneja espacios de nombres con `xmlns='{espacio_de_nombres}'` en consultas find, ej., `root.find('{http://ejemplo.com}etiqueta')`.
- Para archivos grandes, considera el análisis iterativo con `ET.iterparse()`.
- Ten cuidado con el XML de entrada del usuario para evitar vulnerabilidades XML como la inyección.
- Para necesidades complejas, bibliotecas como lxml ofrecen funciones extendidas.