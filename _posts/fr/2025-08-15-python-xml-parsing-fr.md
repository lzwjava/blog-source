---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Analyse XML avec xml.etree en Python
translated: true
type: note
---

### Présentation de xml.etree en Python

`xml.etree` est un module intégré à Python (plus précisément `xml.etree.ElementTree`) pour analyser et manipuler des données XML. Il fournit une structure arborescente permettant de lire, écrire, modifier et naviguer efficacement dans les éléments XML. Il est léger et ne nécessite pas de bibliothèques externes, ce qui le rend idéal pour les tâches XML de base. Importez-le avec `import xml.etree.ElementTree as ET`.

### Analyse d'un document XML

Pour charger du XML en mémoire, utilisez les méthodes d'analyse :

- **À partir d'une chaîne** : `ET.fromstring(xml_string)` renvoie un objet Element représentant la racine.
- **À partir d'un fichier** : `ET.parse(filename)` renvoie un objet ElementTree, auquel vous pouvez accéder via `.getroot()`.

```python
import xml.etree.ElementTree as ET

# Analyser à partir d'une chaîne
xml_data = "<root><child>text</child></root>"
root = ET.fromstring(xml_data)

# Analyser à partir d'un fichier
tree = ET.parse('example.xml')
root = tree.getroot()
```

### Navigation parmi les éléments

Une fois analysé, vous pouvez parcourir l'arbre XML :

- **Accéder aux enfants** : Utilisez `root[0]` pour un accès indexé ou itérez avec `for child in root:`.
- **Trouver des éléments** :
  - `root.find('tag')` récupère le premier enfant correspondant.
  - `root.findall('tag')` récupère tous les enfants correspondants.
- **Accéder au texte et aux attributs** :
  - Contenu textuel : `element.text`
  - Attributs : `element.attrib` (un dictionnaire)

```python
# Exemple XML : <bookstore><book id="1"><title>Python</title></book></bookstore>
for book in root.findall('book'):
    title = book.find('title').text
    book_id = book.attrib['id']
    print(f"Livre {book_id} : {title}")
```

### Modification du XML

Modifiez les éléments dynamiquement :

- **Ajouter des éléments** : `ET.SubElement(parent, 'new_tag')` crée et attache un nouvel enfant.
- **Définir le texte/les attributs** : `element.text = 'nouveau texte'` ; `element.set('attr', 'valeur')`.
- **Supprimer des éléments** : `root.remove(child)`.

```python
new_child = ET.SubElement(root, 'new_element')
new_child.text = 'Contenu ajouté'
new_child.set('attr', 'valeur')
```

### Écriture du XML

Pour enregistrer les modifications dans un fichier XML :

- **Vers une chaîne** : `ET.tostring(root, encoding='unicode')`.
- **Vers un fichier** : `tree.write('output.xml')`.

```python
xml_output = ET.tostring(root, encoding='unicode')
with open('output.xml', 'w') as f:
    f.write(xml_output)

# Ou directement
tree.write('output.xml')
```

### Exemple complet

Voici un script complet pour analyser, modifier et écrire du XML :

```python
import xml.etree.ElementTree as ET

# Chaîne XML d'entrée
xml_str = """<library>
  <book id="1"><title>1984</title><author>Orwell</author></book>
</library>"""

root = ET.fromstring(xml_str)

# Ajouter un nouveau livre
new_book = ET.SubElement(root, 'book', id="2")
ET.SubElement(new_book, 'title').text = 'Le Meilleur des mondes'
ET.SubElement(new_book, 'author').text = 'Huxley'

# Afficher tous les livres
for book in root:
    title = book.find('title').text
    author = book.find('author').text
    print(f"{title} par {author}")

# Écrire dans un fichier
ET.tostring(root, encoding='unicode')
# Ou root.write('library.xml')
```

### Notes
- Gérez les espaces de noms avec `xmlns='{namespace}'` dans les requêtes find, par exemple `root.find('{http://example.com}tag')`.
- Pour les gros fichiers, envisagez l'analyse itérative avec `ET.iterparse()`.
- Soyez prudent avec le XML provenant de l'utilisateur pour éviter les vulnérabilités XML comme l'injection.
- Pour des besoins complexes, des bibliothèques comme lxml offrent des fonctionnalités étendues.