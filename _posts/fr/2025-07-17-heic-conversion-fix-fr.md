---
audio: false
generated: true
lang: fr
layout: post
title: Correction de l'Erreur de Prise en Charge HEIC pour les Oreillers
translated: true
type: note
---

L'erreur `cannot identify image file` indique que Pillow est incapable de lire les fichiers HEIC, probablement pour l'une des raisons suivantes :
1. **Bibliothèque `libheif` manquante** : Pillow nécessite `libheif` pour traiter les fichiers HEIC, et il se peut qu'elle ne soit pas installée ou correctement configurée sur votre système.
2. **Fichiers HEIC corrompus ou incompatibles** : Les fichiers HEIC peuvent être corrompus ou dans un format que Pillow ne peut pas traiter.
3. **Problème de version de Pillow** : Bien que Pillow 9.0.0+ prenne en charge HEIC, il peut y avoir un problème de configuration ou une version obsolète.

Étant donné que vous êtes sur macOS (d'après votre sortie précédente), je vais fournir un script Python corrigé qui inclut une gestion d'erreur supplémentaire et une journalisation pour diagnostiquer le problème. Je vais également vous guider pour installer `libheif` et vérifier la prise en charge HEIC de Pillow. Si Pillow continue d'échouer, le script inclut une solution de repli pour utiliser `ImageMagick` (s'il est installé) pour la conversion HEIC.

### Étapes pour Corriger le Problème

#### 1. Installer `libheif`
Pillow dépend de `libheif` pour la prise en charge HEIC. Installez-le en utilisant Homebrew :
```bash
brew install libheif
```
Après l'installation, réinstallez Pillow pour vous assurer qu'il se lie avec `libheif` :
```bash
pip uninstall pillow
pip install pillow
```

#### 2. Vérifier la Prise en Charge HEIC de Pillow
Vérifiez si Pillow peut gérer les fichiers HEIC :
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- Si la sortie est `True`, Pillow a la prise en charge HEIC.
- Si la sortie est `False` ou une erreur, `libheif` n'est pas correctement configuré, ou Pillow a été compilé sans la prise en charge HEIC.

#### 3. Vérifier l'Intégrité des Fichiers
Assurez-vous que les fichiers HEIC ne sont pas corrompus. Essayez d'ouvrir l'un des fichiers (par exemple, `IMG_5988.HEIC`) dans un visualiseur comme Aperçu sur macOS. S'il ne s'ouvre pas, les fichiers sont peut-être corrompus, et vous devrez les réexporter ou en obtenir de nouvelles copies.

#### 4. Script Python Mis à Jour
Le script mis à jour :
- Utilise Pillow pour la conversion HEIC avec une meilleure gestion des erreurs.
- Utilise `ImageMagick` en repli (s'il est installé) lorsque Pillow échoue à lire un fichier HEIC.
- Journalise les erreurs détaillées dans un fichier (`conversion_errors.log`) pour le débogage.
- Prend en charge les extensions `.heic` et `.heif`.
- Compresse les JPG de sortie à ~500 Ko.

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# Configurer la journalisation
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Analyser les arguments de ligne de commande
parser = argparse.ArgumentParser(description="Convertir les images HEIC en JPG et les compresser à ~500 Ko.")
parser.add_argument("input_dir", help="Répertoire contenant les fichiers HEIC")
args = parser.parse_args()

# Définir les répertoires d'entrée et de sortie
input_dir = args.input_dir.rstrip(os.sep)
output_dir = input_dir + "_compressed"
target_size_kb = 500  # Taille de fichier cible en Ko

# Créer le répertoire de sortie s'il n'existe pas
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_file_size(file_path):
    """Retourne la taille du fichier en Ko."""
    return os.path.getsize(file_path) / 1024

def convert_with_imagemagick(heic_path, jpg_path):
    """Repli vers ImageMagick pour la conversion HEIC en JPG."""
    try:
        subprocess.run(
            ["magick", heic_path, "-quality", "85", jpg_path],
            check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"ImageMagick a échoué pour {heic_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ImageMagick n'est pas installé. Installez-le avec 'brew install imagemagick'.")
        return False

def convert_heic_to_jpg(heic_path, jpg_path, quality=85):
    """Convertir HEIC en JPG et compresser pour approcher la taille cible."""
    try:
        # Essayer Pillow d'abord
        image = Image.open(heic_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Sauvegarder en JPG avec une qualité initiale
        image.save(jpg_path, "JPEG", quality=quality)
        
        # Ajuster la qualité pour approcher la taille cible
        current_size = get_file_size(jpg_path)
        low, high = 10, 100
        while low <= high and abs(current_size - target_size_kb) > 10:
            quality = (low + high) // 2
            image.save(jpg_path, "JPEG", quality=quality)
            current_size = get_file_size(jpg_path)
            if current_size > target_size_kb:
                high = quality - 1
            else:
                low = quality + 1
        return True
    except Exception as e:
        logging.error(f"Pillow a échoué pour {heic_path}: {e}")
        # Repli vers ImageMagick
        return convert_with_imagemagick(heic_path, jpg_path)

# Traiter tous les fichiers HEIC dans le répertoire d'entrée
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".heic", ".heif")):
        heic_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_filename)

        try:
            if convert_heic_to_jpg(heic_path, jpg_path):
                print(f"Converti {filename} en {jpg_filename}, taille: {get_file_size(jpg_path):.2f} Ko")
            else:
                print(f"Erreur lors du traitement de {filename}: La conversion a échoué (voir conversion_errors.log)")
        except Exception as e:
            print(f"Erreur lors du traitement de {filename}: {e}")
            logging.error(f"Erreur générale pour {heic_path}: {e}")

print("Conversion par lots terminée ! Vérifiez conversion_errors.log pour tout problème.")
```

### Comment Utiliser
1. **Sauvegarder le script** :
   Sauvegardez le code sous `photo_compress.py` dans votre répertoire `scripts/media/`.

2. **Installer les dépendances** :
   - Assurez-vous que Pillow est installé :
     ```bash
     pip install --upgrade pillow
     ```
   - Installez `libheif` :
     ```bash
     brew install libheif
     ```
   - Optionnellement, installez ImageMagick pour le repli :
     ```bash
     brew install imagemagick
     ```

3. **Exécuter le script** :
   ```bash
   python scripts/media/photo_compress.py ./assets/images/yuebei
   ```
   - Ceci traite tous les fichiers `.heic` et `.heif` dans `assets/images/yuebei`.
   - Les JPG de sortie sont sauvegardés dans `assets/images/yuebei_compressed`.
   - Les erreurs sont journalisées dans `conversion_errors.log` dans le répertoire courant.

4. **Vérifier le journal** :
   Si certains fichiers échouent à la conversion, vérifiez `conversion_errors.log` pour les messages d'erreur détaillés.

### Dépannage Supplémentaire
- **Si Pillow échoue toujours** :
  - Vérifiez que `libheif` est correctement installé et lié :
    ```bash
    pkg-config --modversion libheif
    ```
    Si cela échoue, réinstallez `libheif` et Pillow.
  - Testez un fichier manuellement :
    ```python
    from PIL import Image
    img = Image.open("./assets/images/yuebei/IMG_5988.HEIC")
    print("Image ouverte avec succès")
    ```
    Si cela échoue, le fichier est peut-être corrompu ou dans une variante HEIC non supportée.

- **Fichiers corrompus** :
  - Essayez de convertir un fichier manuellement avec ImageMagick :
    ```bash
    magick ./assets/images/yuebei/IMG_5988.HEIC test.jpg
    ```
    Si cela échoue, le fichier est probablement corrompu.

- **Repli ImageMagick** :
  - Si Pillow échoue constamment, le script tentera d'utiliser ImageMagick (s'il est installé).
  - Installez `jpegoptim` pour un meilleur contrôle de la compression :
    ```bash
    brew install jpegoptim
    ```
    Ensuite, après avoir exécuté le script, compressez la sortie :
    ```bash
    for i in ./assets/images/yuebei_compressed/*.jpg; do jpegoptim --size=500k "$i"; done
    ```

### Références
- [Documentation Pillow](https://pillow.readthedocs.io/en/stable/)
- [ImageMagick](https://imagemagick.org/)
- [libheif](https://github.com/strukturag/libheif)
- [jpegoptim](https://github.com/tjko/jpegoptim)

Si vous rencontrez toujours des problèmes, partagez le contenu de `conversion_errors.log` ou tout nouveau message d'erreur, et je pourrai fournir une assistance supplémentaire !