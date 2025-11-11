---
audio: false
generated: true
lang: es
layout: post
title: Archivo Zip Limpio
translated: true
type: note
---

1. **Lee un archivo ZIP** usando `zipfile.ZipFile` y obtiene una lista de todos los archivos dentro.
2. **Filtra los archivos sin extensiones**, manteniendo los directorios (entradas que terminan con `/`).
3. **Registra los archivos eliminados** para informar al usuario cuáles fueron excluidos.
4. **Crea un nuevo archivo ZIP** solo con los archivos válidos (aquellos con extensiones o directorios).
5. **Usa `argparse` para aceptar la ruta de un archivo ZIP** como un argumento de línea de comandos.

Esto asegura que solo permanezcan los archivos apropiados mientras se preservan las estructuras de directorios. 🚀

```python
import zipfile
import os
import argparse

def clean_zip(zip_path):
    output_path = os.path.splitext(zip_path)[0] + "_output.zip"
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        
        # Separar archivos válidos y archivos sin extensiones (excluyendo directorios)
        valid_files = [f for f in file_names if os.path.splitext(os.path.basename(f))[1] or f.endswith('/')]
        removed_files = [f for f in file_names if not os.path.splitext(os.path.basename(f))[1] and not f.endswith('/')]
        
        if not valid_files:
            print("No valid files with extensions found. Exiting.")
            return
        
        # Registrar archivos eliminados
        if removed_files:
            print("Removing the following files (no extensions detected):")
            for f in removed_files:
                print(f" - {f}")
        
        # Crear un nuevo archivo zip excluyendo archivos inválidos
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