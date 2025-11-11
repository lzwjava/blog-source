---
audio: false
generated: true
lang: es
layout: post
title: Script de Expresiones Regulares XML
translated: true
type: note
---

Modificaré el script para usar `argparse` y manejar argumentos de línea de comandos. Esto te permitirá pasar la ruta del archivo directamente al ejecutar el script:

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # Leer el contenido del archivo XML
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # Encontrar todas las etiquetas <c:look> usando regex
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # Imprimir los números
    for number in matches:
        print(number)

def main():
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description='Extraer números de las etiquetas <c:look> en un archivo XML')
    parser.add_argument('file_path', help='Ruta al archivo XML')
    
    # Analizar argumentos
    args = parser.parse_args()
    
    # Procesar el archivo
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()
```

Ahora puedes ejecutar el script desde la línea de comandos de esta manera:

```
python nombre_del_script.py ruta/a/tu/archivo.xml
```

El script hará lo siguiente:
1. Usará `argparse` para manejar el argumento de línea de comandos para la ruta del archivo
2. Analizará el archivo XML para encontrar todas las etiquetas `<c:look>`
3. Extraerá e imprimirá los números dentro de estas etiquetas

Este enfoque hace que el script sea más fácil de usar y adecuado para scripting o procesamiento por lotes.