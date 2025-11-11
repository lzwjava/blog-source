---
audio: false
generated: true
lang: es
layout: post
title: Comparación de dos CSV de una sola fila
translated: true
type: note
---

A continuación se muestra un script de Python que compara dos archivos CSV de una sola fila que contienen cadenas (por ejemplo, "P0001") e identifica:
- Elementos comunes (presentes en ambos archivos)
- Elementos únicos del primer archivo
- Elementos únicos del segundo archivo

El script utiliza `argparse` para aceptar dos rutas de archivos CSV, lee la primera fila de cada uno, realiza una comparación basada en conjuntos y escribe los resultados en `comparison.txt`.

```python
#!/usr/bin/env python3
import argparse
import csv
import os

def main():
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description='Compara dos archivos CSV de una sola fila para encontrar elementos comunes y únicos')
    parser.add_argument('file1_path', help='Ruta al primer archivo CSV')
    parser.add_argument('file2_path', help='Ruta al segundo archivo CSV')
    
    # Analizar argumentos
    args = parser.parse_args()
    
    try:
        # Leer la primera fila del primer archivo CSV
        with open(args.file1_path, 'r') as file1:
            reader1 = csv.reader(file1)
            for row in reader1:
                values1 = row
                break
        
        # Leer la primera fila del segundo archivo CSV
        with open(args.file2_path, 'r') as file2:
            reader2 = csv.reader(file2)
            for row in reader2:
                values2 = row
                break
        
        # Convertir a conjuntos para la comparación
        set1 = set(values1)
        set2 = set(values2)
        
        # Encontrar elementos comunes y únicos
        common_items = set1.intersection(set2)
        unique_to_file1 = set1.difference(set2)
        unique_to_file2 = set2.difference(set1)
        
        # Determinar el directorio de salida (usar el directorio del primer archivo)
        output_dir = os.path.dirname(args.file1_path) or '.'
        output_file = os.path.join(output_dir, 'comparison.txt')
        
        # Escribir resultados en el archivo de salida
        with open(output_file, 'w') as file:
            file.write("Resultados de la Comparación:\n\n")
            
            file.write("Elementos Comunes (en ambos archivos):\n")
            if common_items:
                for item in sorted(common_items):
                    file.write(f"{item}\n")
            else:
                file.write("Ninguno\n")
                
            file.write("\nElementos solo en el primer archivo:\n")
            if unique_to_file1:
                for item in sorted(unique_to_file1):
                    file.write(f"{item}\n")
            else:
                file.write("Ninguno\n")
                
            file.write("\nElementos solo en el segundo archivo:\n")
            if unique_to_file2:
                for item in sorted(unique_to_file2):
                    file.write(f"{item}\n")
            else:
                file.write("Ninguno\n")
        
        print(f"Comparación completada. Resultados guardados en {output_file}")
        
    except FileNotFoundError as e:
        print(f"Error: Archivo no encontrado - {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Cómo funciona:
1. **Entrada**: Toma dos rutas de archivos CSV a través de argumentos de línea de comandos.
2. **Lectura**: Lee solo la primera fila de cada archivo CSV.
3. **Comparación**:
   - Convierte las filas en conjuntos para una comparación eficiente.
   - Encuentra:
     - **Elementos comunes**: Elementos presentes en ambas filas (intersección de conjuntos).
     - **Únicos al primer archivo**: Elementos solo en la primera fila (diferencia de conjuntos: archivo1 - archivo2).
     - **Únicos al segundo archivo**: Elementos solo en la segunda fila (diferencia de conjuntos: archivo2 - archivo1).
4. **Salida**: Escribe los resultados en `comparison.txt` en el directorio del primer archivo, listando:
   - Elementos comunes
   - Elementos solo en el primer archivo
   - Elementos solo en el segundo archivo
   - Cada sección está ordenada alfabéticamente; se escribe "Ninguno" si una sección está vacía.
5. **Manejo de Errores**: Captura errores de archivo no encontrado y otras excepciones.

### Ejemplo de uso:
Guarda el script como `compare_csv.py`. Crea dos archivos CSV, por ejemplo:
- `file1.csv`: `P0001,P0002,P0003`
- `file2.csv`: `P0001,P0004,P0003`

Ejecuta el script:
```
python compare_csv.py file1.csv file2.csv
```

**Salida** (`comparison.txt`):
```
Resultados de la Comparación:

Elementos Comunes (en ambos archivos):
P0001
P0003

Elementos solo en el primer archivo:
P0002

Elementos solo en el segundo archivo:
P0004
```

### Notas:
- El script ignora la posición de los elementos y se centra solo en la presencia/ausencia.
- Los elementos duplicados en una fila se manejan automáticamente (los conjuntos eliminan duplicados).
- La salida se escribe en `comparison.txt` en el directorio del primer archivo de entrada.
- Si un archivo está vacío o no tiene fila, el script lo tratará como un conjunto vacío.

¿Te gustaría que modifique el script (por ejemplo, cambiar el formato de salida o agregar más detalles)?