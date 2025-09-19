---
audio: false
generated: false
image: false
lang: es
layout: post
title: Gestión automatizada de borradores de blogs con reinicio de VSCode
translated: true
---

El script que has proporcionado está diseñado para automatizar el proceso de publicación de borradores de entradas de blog de manera estructurada. Es especialmente útil para blogueros o creadores de contenido que gestionan sus entradas como borradores antes de que estén listas para ser publicadas. Aquí tienes una introducción extendida para dar más contexto sobre el script:

## Introducción

Gestionar un blog o cualquier sitio web basado en contenido suele implicar crear y almacenar borradores antes de que estén listos para ser publicados. Este script está diseñado para agilizar el flujo de trabajo de mover las entradas de borrador a un directorio de publicación designado, específicamente para una configuración de generador de sitios estáticos, como aquellos que utilizan Jekyll o marcos similares.

El script realiza las siguientes tareas clave:

```python
import os
import datetime
import glob
import shutil
import sys
import subprocess
import time

def publish_drafts_to_posts():
    """Verifica los archivos de borrador creados hoy y los mueve al directorio _posts/en."""
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')

    drafts_dir = '_drafts'
    posts_en_dir = "original"

    if not os.path.exists(drafts_dir):
        print(f"El directorio de borradores '{drafts_dir}' no existe. No hay archivos para publicar.")
        return

    if not os.path.exists(posts_en_dir):
        os.makedirs(posts_en_dir)

    # Patrón para encontrar archivos en el directorio de borradores que comienzan con la fecha de hoy y terminan con -en.md
    pattern = os.path.join(drafts_dir, f"{date_str}-*-en.md")

    found_files = glob.glob(pattern)

    if not found_files:
        print(f"No se encontraron archivos de borrador en '{drafts_dir}' que comiencen con '{date_str}' para publicar.")
        return

    for file_path in found_files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(posts_en_dir, file_name)

        try:
            shutil.move(file_path, destination_path)
            print(f"Movido '{file_name}' desde '{drafts_dir}' a '{posts_en_dir}'.")
        except Exception as e:
            print(f"Error al mover '{file_name}': {e}")

    restart_vscode()

def restart_vscode():
    print("Reiniciando VSCode de manera elegante para evitar la recreación accidental de archivos de borrador...")
    try:
        if sys.platform == 'win32':
            # Cierre elegante sin /f
            os.system('taskkill /im Code.exe /t')
            time.sleep(3)  # Retraso para la limpieza
            subprocess.Popen(['code', '.'])  # Reabrir
        elif sys.platform == 'darwin':
            # Usar AppleScript para salir de manera elegante
            os.system('osascript -e \'quit app "Visual Studio Code"\'')
            time.sleep(3)
            subprocess.call(['open', '-a', 'Visual Studio Code', '.'])
        elif sys.platform.startswith('linux'):
            # SIGTERM para terminación elegante
            os.system('killall code')
            time.sleep(3)
            subprocess.Popen(['code', '.'])
        else:
            print("Plataforma no soportada para reiniciar VSCode.")
    except Exception as e:
        print(f"Error durante el reinicio: {e}. Por favor, reinicia VSCode manualmente.")

if __name__ == "__main__":
    publish_drafts_to_posts()
```