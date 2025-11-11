---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide d'utilisation du module tarfile de Python
translated: true
type: note
---

### Importation du module tarfile

Pour utiliser la bibliothèque `tarfile` en Python, importez-la d'abord :

```python
import tarfile
```

Ce module fait partie de la bibliothèque standard de Python, donc aucune installation n'est nécessaire. Il est basé sur le format tar POSIX et prend en charge la lecture et l'écriture d'archives tar compressées ou non compressées.

### Ouverture et création d'archives tar

- **Ouvrir un fichier tar existant** : Utilisez `tarfile.open()` avec un mode. Les modes incluent `'r'` (lecture), `'w'` (écriture vide), `'a'` (ajout), ou des variantes avec compression comme `'r:gz'` pour gzip.
  ```python
  import tarfile
  
  # Ouvrir en lecture (non compressé)
  with tarfile.open('example.tar', 'r') as tar:
      # Travailler avec tar ici
      pass
  ```
- **Créer un nouveau fichier tar** : Utilisez le mode `'w'` pour créer une archive vide. Ajoutez des préfixes de compression comme `'w:gz'` pour gzip ou `'w:bz2'` pour bzip2.
  ```python
  # Créer un fichier tar.gz compressé
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      pass
  ```

### Ajout de fichiers à une archive

- **Ajouter un seul fichier** : Appelez `add()` sur l'objet fichier tar, en passant le chemin du fichier. Vous pouvez spécifier un arcname pour un nom différent dans l'archive.
  ```python
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      tar.add('file.txt')  # Ajoute file.txt tel quel
      tar.add('data.csv', arcname='renamed_data.csv')  # Renomme dans l'archive
  ```
- **Ajouter plusieurs fichiers ou un répertoire** : Utilisez `add()` dans une boucle ou ajoutez des répertoires entiers récursivement.
  ```python
  import os
  
  with tarfile.open('backup.tar', 'w') as tar:
      for root, dirs, files in os.walk('my_folder'):
          for file in files:
              tar.add(os.path.join(root, file))
  ```

### Extraction de fichiers d'une archive

- **Extraire tous les fichiers** : Utilisez `extractall()` pour extraire vers un répertoire spécifié (par défaut le répertoire courant).
  ```python
  with tarfile.open('archive.tar.gz', 'r:gz') as tar:
      tar.extractall(path='extracted_folder')  # Crée le dossier si nécessaire
  ```
- **Extraire des fichiers spécifiques** : Listez d'abord les membres avec `getmembers()`, puis utilisez `extract()`.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      members = tar.getmembers()
      for member in members:
          if 'important' in member.name:  # Exemple de filtre
              tar.extract(member, path='output_dir')
  ```
- Remarque : Pour des raisons de sécurité, filtrez les chemins (par exemple, évitez `..`) pour prévenir les attaques par traversée de répertoire. `tarfile` effectue quelques vérifications, mais un filtrage manuel est conseillé pour les archives non fiables.

### Liste du contenu d'une archive

- **Itérer sur les fichiers** : Utilisez `getmembers()` ou itérez directement sur l'objet tar pour obtenir des objets TarInfo.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      for member in tar.getmembers():
          print(f"{member.name}: {member.size} bytes")
  ```

### Modes clés et compression

- `'r'` : Lire un tar non compressé.
- `'r:gz'`, `'r:bz2'`, `'r:xz'` : Lire les variantes compressées.
- `'w'` : Écrire un nouveau tar non compressé (écrase).
- `'a'` : Ajouter à un tar existant.
- Détection automatique de la compression à la lecture ; spécifiez à l'écriture.

### Conseils et bonnes pratiques

- Utilisez toujours des gestionnaires de contexte (instructions `with`) pour garantir une fermeture correcte des fichiers.
- Pour les grandes archives, envisagez de filtrer ou d'extraire de manière sélective pour économiser la mémoire.
- `tarfile` ne gère pas directement les archives chiffrées — utilisez des outils externes ou combinez avec `gzip` manuellement si nécessaire.
- Gestion des erreurs : Interceptez `tarfile.TarError` pour les problèmes d'archive.
- Documentation complète : Reportez-vous à la [documentation officielle tarfile de Python](https://docs.python.org/3/library/tarfile.html) pour les fonctionnalités avancées comme les filtres personnalisés.