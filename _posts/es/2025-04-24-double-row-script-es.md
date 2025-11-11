---
audio: false
generated: true
lang: es
layout: post
title: Script de Python para Duplicar Filas
translated: true
type: note
---

Aquí está el script Python actualizado modificado para trabajar con archivos .xlsx en lugar de archivos .xls. Utiliza `openpyxl` para manejar archivos .xlsx, mantiene la misma funcionalidad de repetir valores en la tercera fila basándose en el parámetro proporcionado, y guarda la salida en un nuevo archivo .xlsx con "_plus.xlsx" añadido al nombre de archivo original. El artifact_id se reutiliza ya que esta es una actualización del artifact anterior.

```python
import pandas as pd
import argparse
import os

def repeat_value(value, n):
    return str(value) * n

def process_excel(input_file, n):
    df = pd.read_excel(input_file, engine='openpyxl')
    if len(df) < 3:
        raise ValueError("El archivo Excel debe tener al menos 3 filas")
    third_row = df.iloc[2].apply(lambda x: repeat_value(x, n))
    df.iloc[2] = third_row
    base, ext = os.path.splitext(input_file)
    output_file = f"{base}_plus.xlsx"
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Archivo procesado guardado como: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Duplica valores en la tercera fila de un archivo Excel")
    parser.add_argument("input_file", help="Ruta al archivo Excel de entrada (.xlsx)")
    parser.add_argument("-n", type=int, default=1, help="Número de veces a repetir cada valor (por defecto: 1)")
    args = parser.parse_args()
    process_excel(args.input_file, args.n)

if __name__ == "__main__":
    main()
```