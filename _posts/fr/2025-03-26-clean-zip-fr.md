---
audio: false
generated: true
lang: fr
layout: post
title: Fichier Zip Propre
translated: true
type: note
---

1. **Lit un fichier ZIP** en utilisant `zipfile.ZipFile` et obtient une listes de tous les fichiers à l'intérieur.
2. **Filtre les fichiers sans extensions**, tout en conservant les répertoires (entrées se terminant par `/`).
3. **Enregistre les fichiers supprimés** pour informer l'utilisateur de ceux qui ont été exclus.
4. **Crée un nouveau fichier ZIP** contenant uniquement les fichiers valides (ceux avec des extensions ou les répertoires).
5. **Utilise `argparse` pour accepter un chemin de fichier ZIP** comme argument de ligne de commande.

Cela garantit que seuls les fichiers appropriés restent tout en préservant les structures de répertoires. 🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # Séparer les fichiers valides et les fichiers sans extensions (en excluant les répertoires)
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("No valid files with extensions found. Exiting.")
            return
        
        # Enregistrer les fichiers supprimés
        if removed_files:
            print("Removing the following files (no extensions detected):")
            for f in removed_files:
                print(f" - {f}")
        
        # Créer un nouveau fichier zip en excluant les fichiers invalides
        with zipfile.ZipFile(output_path, 'w') as clean_zip:
            for file in valid_files:
                with zip_ref.open(file) as source:
                    clean_zip.writestr(file, source.read())

    print(f"Cleaned ZIP file created: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean a ZIP file by removing files without extensions.")
    parser.add_argument("zip_path", help="Path to the input ZIP file")
    args = parser.parse_args()
    clean_zip(args.zip_path)

```