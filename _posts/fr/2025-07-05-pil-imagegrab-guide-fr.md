---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Capture d'Écran avec PIL ImageGrab
translated: true
type: note
---

### Prérequis
Pour utiliser `ImageGrab` de la bibliothèque PIL (Pillow), assurez-vous d'avoir Pillow installé. Sur Windows, installez-le via pip :
```
pip install Pillow
```
Aucune configuration supplémentaire n'est généralement nécessaire pour Windows, car `ImageGrab` utilise les API Windows natives.

### Utilisation de base
`ImageGrab.grab()` capture l'écran entier (tous les moniteurs) sous la forme d'un objet PIL Image. Voici un exemple simple pour prendre une capture d'écran et l'enregistrer en tant que fichier PNG :

```python
from PIL import ImageGrab

# Capturer l'écran entier
screenshot = ImageGrab.grab()

# Sauvegarder l'image dans un fichier
screenshot.save("screenshot.png")
```

Ceci enregistrera un fichier nommé `screenshot.png` dans votre répertoire de travail actuel.

### Options supplémentaires
- **Capturer une région spécifique** : Spécifiez une boîte englobante (gauche, haut, droite, bas) sous la forme d'un tuple de coordonnées en pixels.
  ```python
  # Capturer une zone de 300x300 pixels commençant à (100, 100)
  region = (100, 100, 400, 400)  # Ajustez les coordonnées selon vos besoins
  screenshot = ImageGrab.grab(bbox=region)
  screenshot.save("region_screenshot.png")
  ```
- **Inclure le curseur de la souris** (si pris en charge ; vérifiez la documentation Pillow pour les détails de version) :
  ```python
  # Remarque : Ceci peut nécessiter include_layered_windows=True sur certains systèmes
  screenshot = ImageGrab.grab(include_layered_windows=True)
  ```
- **Afficher l'image** : Utilisez `screenshot.show()` pour l'ouvrir dans votre visionneuse d'images par défaut (pour les tests).

### Notes
- Les coordonnées sont en pixels, avec (0, 0) en haut à gauche du moniteur principal.
- Pour les configurations multi-moniteurs, `grab()` capture tous les écrans en une seule image composite.
- Si vous rencontrez des problèmes (par exemple, des erreurs de permission sur les versions récentes de Windows), assurez-vous que votre script a les permissions de capture d'écran ou essayez de l'exécuter avec les privilèges d'administrateur.
- Documentation complète : [Pillow ImageGrab docs](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html). Pour les particularités spécifiques à Windows, consultez les problèmes GitHub si nécessaire.