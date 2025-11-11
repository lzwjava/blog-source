---
audio: false
generated: true
lang: fr
layout: post
title: Script Regex XML
translated: true
type: note
---

Je vais modifier le script pour utiliser `argparse` pour gérer les arguments de ligne de commande. Cela vous permettra de passer le chemin du fichier directement lors de l'exécution du script :

```python
import xml.etree.ElementTree as ET
import re
import argparse

def extract_look_tags(xml_file):
    # Lire le contenu du fichier XML
    with open(xml_file, 'r') as file:
        xml_content = file.read()
    
    # Trouver toutes les balises <c:look> en utilisant les expressions régulières
    pattern = r'<c:look>(\d+)</c:look>'
    matches = re.findall(pattern, xml_content)
    
    # Afficher les nombres
    for number in matches:
        print(number)

def main():
    # Configurer l'analyseur d'arguments
    parser = argparse.ArgumentParser(description='Extraire les nombres des balises <c:look> dans un fichier XML')
    parser.add_argument('file_path', help='Chemin vers le fichier XML')
    
    # Analyser les arguments
    args = parser.parse_args()
    
    # Traiter le fichier
    extract_look_tags(args.file_path)

if __name__ == "__main__":
    main()
```

Maintenant vous pouvez exécuter le script depuis la ligne de commande comme ceci :

```
python nom_du_script.py chemin/vers/votre/fichier.xml
```

Le script va :
1. Utiliser `argparse` pour gérer l'argument de ligne de commande pour le chemin du fichier
2. Analyser le fichier XML pour trouver toutes les balises `<c:look>`
3. Extraire et afficher les nombres à l'intérieur de ces balises

Cette approche rend le script plus convivial et adapté au scripting ou au traitement par lots.