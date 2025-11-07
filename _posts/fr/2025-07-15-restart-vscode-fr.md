---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Gestion automatisée des brouillons de blog avec redémarrage de VSCode
translated: true
type: post
---

Le script que vous avez fourni est conçu pour automatiser le processus de publication de brouillons d'articles de blog de manière structurée. Il est particulièrement utile pour les blogueurs ou les créateurs de contenu qui gèrent leurs articles sous forme de brouillons avant qu'ils ne soient prêts à être publiés. Voici une introduction étendue pour donner plus de contexte sur le script :

## Introduction

Gérer un blog ou tout site web axé sur le contenu implique souvent de créer et de stocker des brouillons avant qu'ils ne soient prêts à être publiés. Ce script est conçu pour rationaliser le processus de déplacement des articles en brouillon vers un répertoire de publication désigné, spécifiquement pour une configuration de générateur de site statique, comme ceux utilisant Jekyll ou des frameworks similaires.

Le script effectue les tâches clés suivantes :

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """Vérifie les fichiers de brouillons créés aujourd'hui et les déplace vers le répertoire _posts/en."""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"Le répertoire de brouillons '{drafts_dir}' n'existe pas. Aucun fichier à publier.")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # Modèle pour trouver les fichiers dans le répertoire de brouillons commençant par la date d'aujourd'hui et se terminant par -en.md
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"Aucun fichier de brouillon trouvé dans '{drafts_dir}' commençant par '{date_str}' à publier.")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"Déplacé '{file_name}' de '{drafts_dir}' vers '{posts_en_dir}'.")
        except Exception as e:
            print(f"Erreur lors du déplacement de '{file_name}' : {e}")

    restart_vscode()

def restart_vscode():
    print("Redémarrage de VSCode de manière élégante pour éviter la recréation accidentelle de fichiers de brouillons...")
    try:
        if sys.platform == 'win32':
            # Fermeture élégante sans /f
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # Délai pour le nettoyage
            subprocess.Popen(['code', '.'])  # Réouverture
        elif sys.platform == 'darwin':
            # Utilisation d'AppleScript pour une fermeture élégante
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # SIGTERM pour une terminaison élégante
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("Plateforme non prise en charge pour le redémarrage de VSCode.")
    except Exception as e:
        print(f"Erreur lors du redémarrage : {e}. Veuillez redémarrer manuellement VSCode.")

if __name__ == "__main__":
    publish_drafts_to_posts()
```