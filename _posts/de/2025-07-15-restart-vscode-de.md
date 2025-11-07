---
audio: false
generated: false
image: false
lang: de
layout: post
title: Automatisierter Entwurf für Blogverwaltung mit VSCode-Neustart
translated: true
type: post
---

Das von Ihnen bereitgestellte Skript ist darauf ausgelegt, den Prozess des Veröffentlichens von Blog-Entwürfen auf strukturierte Weise zu automatisieren. Es ist besonders nützlich für Blogger oder Content-Creator, die ihre Beiträge als Entwürfe verwalten, bevor sie veröffentlicht werden. Hier ist eine erweiterte Einführung, um mehr Kontext über das Skript zu geben:

## Einführung

Die Verwaltung eines Blogs oder einer anderen inhaltsgetriebenen Website umfasst oft das Erstellen und Speichern von Entwürfen, bevor sie veröffentlicht werden. Dieses Skript ist darauf ausgelegt, den Arbeitsablauf des Verschiebens von Entwurfsposts in ein bestimmtes Veröffentlichungsverzeichnis zu vereinfachen, insbesondere für eine statische Site-Generator-Konfiguration, wie z. B. diejenigen, die Jekyll oder ähnliche Frameworks verwenden.

Das Skript führt die folgenden Hauptaufgaben aus:

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """Überprüft, ob heute erstellte Entwurfsdaten vorhanden sind und verschiebt sie in das _posts/en-Verzeichnis."""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"Das Entwurfsverzeichnis '{drafts_dir}' existiert nicht. Keine Dateien zum Veröffentlichen.")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # Muster zum Auffinden von Dateien im Entwurfsverzeichnis, die mit dem heutigen Datum beginnen und mit -en.md enden
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"Keine Entwurfsdaten gefunden in '{drafts_dir}', die mit '{date_str}' beginnen, um sie zu veröffentlichen.")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"'{file_name}' wurde von '{drafts_dir}' nach '{posts_en_dir}' verschoben.")
        except Exception as e:
            print(f"Fehler beim Verschieben von '{file_name}': {e}")

    restart_vscode()

def restart_vscode():
    print("VSCode wird sanft neu gestartet, um eine versehentliche Neuerstellung von Entwurfsdaten zu verhindern...")
    try:
        if sys.platform == 'win32':
            # Sanftes Schließen ohne /f
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # Verzögerung für die Aufräumarbeiten
            subprocess.Popen(['code', '.'])  # Wiederöffnen
        elif sys.platform == 'darwin':
            # AppleScript für sanftes Beenden
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # SIGTERM für sanftes Beenden
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("Plattform wird für das Neustarten von VSCode nicht unterstützt.")
    except Exception as e:
        print(f"Fehler beim Neustarten: {e}. Bitte starten Sie VSCode manuell neu.")

if __name__ == "__main__":
    publish_drafts_to_posts()
```