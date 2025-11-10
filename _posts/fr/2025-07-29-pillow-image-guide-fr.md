---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de traitement d'image avec PIL Pillow
translated: true
type: note
---

### Qu'est-ce que PIL/Pillow ?
PIL signifiait à l'origine Python Imaging Library, mais il est maintenant maintenu sous forme de package Pillow (un fork moderne). Vous l'importez en tant que `PIL` dans le code, mais vous devez installer Pillow via pip. Il est utilisé pour ouvrir, manipuler et sauvegarder des fichiers image en Python. Prend en charge des formats comme JPEG, PNG, GIF, BMP, et plus encore.

### Installation
Pour utiliser PIL, installez Pillow :
```bash
pip install pillow
```

### Importation de base et utilisation
Après l'installation, importez-le comme ceci dans votre script Python :
```python
from PIL import Image
```
Il n'est pas nécessaire d'utiliser `import PIL.Image` — cela importe directement le module Image.

### Opérations courantes sur les images
Voici comment effectuer des tâches de base. Supposez que vous avez un fichier image nommé `example.jpg` dans votre répertoire.

#### 1. Ouvrir une image
```python
image = Image.open('example.jpg')  # Ouvre le fichier image
image.show()  # L'affiche (fonctionne sur les systèmes avec un visualiseur d'image)
```

#### 2. Obtenir les informations de l'image
```python
print(image.format)  # Par ex., 'JPEG'
print(image.size)    # Tuple : (largeur, hauteur)
print(image.mode)    # Par ex., 'RGB' pour les images couleur
```

#### 3. Redimensionner une image
```python
resized = image.resize((800, 600))  # Redimensionne à 800x600 pixels
resized.save('resized_example.jpg')  # Sauvegarde l'image redimensionnée
```

#### 4. Convertir les formats
```python
image.convert('L').save('grayscale_example.png')  # Convertit en niveaux de gris et sauvegarde en PNG
```

#### 5. Faire pivoter une image
```python
rotated = image.rotate(90)  # Pivote de 90 degrés dans le sens horaire
rotated.save('rotated_example.jpg')
```

#### 6. Rogner une image
```python
left, top, right, bottom = 100, 100, 300, 300  # Définit la zone de rognage (x1, y1, x2, y2)
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. Appliquer des filtres (nécessite des imports supplémentaires)
Pour les filtres, importez `ImageFilter` :
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # Applique le filtre de flou
blurred.save('blurred_example.jpg')
```

### Exemple avancé : Traitement par lots de plusieurs images
```python
import os
from PIL import Image

# Redimensionne toutes les images JPEG d'un dossier en 200x200
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### Conseils et notes
- **Gestion des erreurs** : Utilisez try-except pour les fichiers invalides, par ex., `try: image = Image.open('file.jpg')`.
- **Efficacité mémoire** : Pour les grandes images, utilisez `image.close()` après les opérations pour libérer la mémoire.
- **Documentation** : Consultez la documentation complète de Pillow sur [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) pour plus de fonctions comme le dessin, l'ajout de texte ou la gestion des données EXIF.
- **Dépendances** : Pillow peut nécessiter des bibliothèques système (par ex., libjpeg) sur certaines configurations ; consultez le guide d'installation en cas de problème.

Si vous avez une tâche spécifique ou une erreur, fournissez plus de détails pour une aide personnalisée !