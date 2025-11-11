---
audio: false
generated: true
lang: de
layout: post
title: Ein XML-Regex-Skript
translated: true
type: note
---

Ich werde das Skript so ändern, dass es `argparse` zur Verarbeitung von Kommandozeilenargumenten verwendet. Dies ermöglicht es, den Dateipfad direkt beim Ausführen des Skripts zu übergeben:

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # Read the XML file content
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # Find all <c:look> tags using regex
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # Print the numbers
    for number in matches:
        print(number)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract numbers from <c:look> tags in an XML file')
    parser.add_argument('file_path', help='Path to the XML file')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the file
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()
```

Jetzt können Sie das Skript von der Kommandozeile wie folgt ausführen:

```
python script_name.py path/to/your/xml_file.xml
```

Das Skript wird:
1. `argparse` zur Verarbeitung des Kommandozeilenarguments für den Dateipfad verwenden
2. Die XML-Datei parsen, um alle `<c:look>`-Tags zu finden
3. Die Zahlen innerhalb dieser Tags extrahieren und ausgeben

Dieser Ansatz macht das Skript benutzerfreundlicher und geeignet für Scripting oder Batch-Verarbeitung.