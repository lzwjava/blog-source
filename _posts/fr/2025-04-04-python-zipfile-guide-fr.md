---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide du Package ZipFile de Python
translated: true
type: note
---

### Aperçu du package ZipFile
Le module `zipfile` de Python permet de lire et d'écrire des fichiers d'archive ZIP sans outils externes. Il fait partie de la bibliothèque standard, donc aucune installation n'est nécessaire (à partir de Python 2.3+). Utilisez-le pour compresser, décompresser ou manipuler des fichiers ZIP par programme. Il prend en charge diverses méthodes de compression comme DEFLATE.

Importez-le avec : `import zipfile`

### Lecture des fichiers ZIP
Pour extraire ou inspecter des fichiers ZIP existants :

1. **Ouvrir un fichier ZIP en lecture** :
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' est pour le mode lecture
   ```

2. **Lister le contenu** :
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # Retourne une liste des noms de fichiers
       print(file_list)
   ```

3. **Extraire des fichiers** :
   - Extraire tout : `zip_ref.extractall('dossier_destination')`
   - Extraire un seul fichier : `zip_ref.extract('fichier_interne.zip', 'chemin')`

4. **Lire le contenu d'un fichier sans l'extraire** :
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('fichier_interne.zip') as file:
           content = file.read()
           print(content.decode())  # S'il s'agit d'un texte
   ```

Note : Utilisez toujours `with` pour une fermeture automatique. Pour les ZIP protégés par mot de passe, ajoutez `pwd=b'mot_de_passe'` à `ZipFile()`.

### Écriture des fichiers ZIP
Pour créer ou ajouter à de nouveaux fichiers ZIP ou existants :

1. **Créer un nouveau fichier ZIP** :
   ```python
   with zipfile.ZipFile('new_archive.zip', 'w') as zip_ref:
       # 'w' est pour le mode écriture (écrase si existe)
   ```

2. **Ajouter des fichiers** :
   - Ajouter un fichier : `zip_ref.write('fichier_source.txt', 'nom_dans_archive.txt')` (le paramètre arcname optionnel le renomme à l'intérieur)
   - Ajouter plusieurs fichiers : Bouclez sur une liste de fichiers et appelez `write()`.

3. **Compresser lors de l'écriture** (la valeur par défaut est DEFLATE) :
   ```python
   with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('fichier_volumineux.txt')
   ```
   Options : `ZIP_STORED` (pas de compression), `ZIP_DEFLATED`, `ZIP_BZIP2`, etc.

4. **Ajouter à un ZIP existant** (utilisez le mode 'a' au lieu de 'w').

### Opérations courantes et conseils
- **Vérifier si un fichier est un ZIP valide** : Utilisez `zipfile.is_zipfile('fichier.zip')`.
- **Obtenir les informations d'un fichier** : `zip_ref.getinfo('fichier.txt')` retourne un objet ZipInfo avec des détails comme la taille, la date.
- **Gérer les fichiers volumineux** : La lecture/l'extraction de fichiers volumineux peut consommer de la mémoire ; utilisez la méthode `open()` pour le streaming.
- **Gestion des erreurs** : Interceptez les exceptions `BadZipFile` ou `LargeZipFile`.
- **Multiplateforme** : Fonctionne sur Windows, macOS, Linux, mais soyez attentif aux séparateurs de chemin (utilisez `/`).
- **Chiffrement** : La protection par mot de passe basique est prise en charge, mais elle est faible — utilisez des outils plus robustes pour la sécurité.
- **Niveau supérieur** : Pour plus de fonctionnalités (par exemple, l'intégration de shutil), combinez avec `shutil.make_archive()` pour créer des ZIP.

Exemple de script complet pour zipper un dossier :
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('mon_dossier', 'output.zip')
```

Pour la documentation complète, consultez la [documentation officielle de Python](https://docs.python.org/3/library/zipfile.html). Si vous avez une tâche spécifique (par exemple, "comment extraire en mémoire"), fournissez plus de détails !