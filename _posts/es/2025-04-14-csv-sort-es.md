---
audio: false
generated: true
lang: es
layout: post
title: Script de Clasificación de CSV
translated: true
type: note
---

Crearé un script de Python que utilice argparse para analizar la ruta de un archivo CSV, ordene alfabéticamente una sola línea de valores separados por comas y envíe el resultado a un archivo llamado "name_sorted.csv".

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description='Ordena alfabéticamente un archivo CSV de una sola línea')
    parser.add_argument('file_path', help='Ruta al archivo CSV de entrada')
    
    # Analizar argumentos
    args = parser.parse_args()
    
    try:
        # Obtener el directorio y el nombre del archivo
        file_dir = os.path.dirname(args.file_path)
        file_name = os.path.basename(args.file_path)
        
        # Crear el nombre del archivo de salida
        base_name, ext = os.path.splitext(file_name)
        output_file = os.path.join(file_dir, f"{base_name}_sorted{ext}")
        
        # Leer el archivo CSV de entrada
        with open(args.file_path, 'r') as file:
            reader = csv.reader(file)
            # Obtener solo la primera línea
            for row in reader:
                values = row
                break
        
        # Ordenar los valores alfabéticamente
        sorted_values = sorted(values)
        
        # Escribir en el archivo de salida
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(sorted_values)
        
        print(f"Valores ordenados exitosamente y guardados en {output_file}")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{args.file_path}'")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

Este script:
1. Utiliza argparse para obtener la ruta del archivo de entrada
2. Abre el archivo CSV y lee solo la primera línea
3. Ordena los valores alfabéticamente
4. Escribe los valores ordenados en "name_sorted.csv"

Para ejecutar el script, guárdalo en un archivo (por ejemplo, "sort_csv.py"), hazlo ejecutable si es necesario y ejecútalo con la ruta a tu archivo CSV:

```
python sort_csv.py ruta/a/tu/archivo.csv
```

¿Te gustaría que explique alguna parte del código con más detalle?