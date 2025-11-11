---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Lectura y Escritura de Archivos CSV
translated: true
type: note
---

### Introducción al módulo `csv` de Python

El módulo `csv` es parte de la biblioteca estándar de Python y se utiliza para leer y escribir archivos CSV (Valores Separados por Comas). Maneja el análisis de filas y columnas de manera eficiente. Para usarlo, primero importa el módulo: `import csv`. Trabajarás con objetos de archivo, típicamente abiertos en modo lectura (`'r'`) o escritura (`'w'`).

Componentes clave:
- **Reader**: Analiza datos CSV desde un archivo (por ejemplo, `csv.reader()` para acceso basado en filas).
- **Writer**: Escribe datos a un archivo CSV (por ejemplo, `csv.writer()`).
- Los archivos CSV se tratan como secuencias de filas, donde cada fila es una lista de strings (columnas).

Por seguridad y facilidad, siempre maneja los archivos con sentencias `with` para garantizar un cierre adecuado.

### Lectura básica de un archivo CSV

Para leer un CSV:
```python
import csv

with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Cada 'row' es una lista de columnas
```
- Esto lee el archivo fila por fila. Puedes acceder a columnas específicas por índice (por ejemplo, `row[0]` para la primera columna).
- Para los encabezados, lee la primera fila por separado: `headers = next(reader)`.

### Comparar dos archivos CSV: Filas y Columnas

Para comparar dos CSVs (por ejemplo, `file1.csv` y `file2.csv`), cárgalos en estructuras como listas de listas (filas), luego compara. Suposiciones: ambos CSVs tienen la misma estructura (mismo número de columnas/filas). Las comparaciones pueden verificar coincidencias exactas, diferencias o lógica específica (por ejemplo, coincidir en una columna clave).

#### Ejemplo 1: Comparar Filas (Filas Completas)
Usa diccionarios para almacenar filas (si tienen una columna de ID única) o listas para comparación directa.

```python
import csv

def compare_rows(file1, file2, key_column=0):
    # Leer file1 en un dict (usando key_column como clave, toda la fila como valor)
    data1 = {}
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        headers1 = next(reader1, None)  # Saltar encabezado si está presente
        for row in reader1:
            data1[row[key_column]] = row  # ej., clave en la primera columna

    # Leer file2 de manera similar
    data2 = {}
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        headers2 = next(reader2, None)
        for row in reader2:
            data2[row[key_column]] = row

    # Comparar
    common_keys = set(data1.keys()) & set(data2.keys())
    differing_rows = []
    for key in common_keys:
        if data1[key] != data2[key]:
            differing_rows.append((key, data1[key], data2[key]))
    
    return differing_rows  # Lista de (clave, fila_desde_file1, fila_desde_file2)

# Uso
differences = compare_rows('file1.csv', 'file2.csv', key_column=0)  # Clave en columna 0
print("Filas diferentes:", differences)
```

- **Cómo funciona**: Convierte los CSVs en diccionarios indexados por una columna (por ejemplo, ID). Compara las filas coincidentes directamente. Ajusta `key_column` para especificar en qué columna indexar.
- **Variaciones**: Para comparación fila por fila sin claves, itera ambos lectores simultáneamente (si mismo orden/longitud).

#### Ejemplo 2: Comparar Columnas
Compara columnas específicas en todo el archivo (por ejemplo, verifica si los valores de la columna 1 son idénticos en ambos archivos).

```python
import csv

def compare_columns(file1, file2, col_index=0):
    # Extraer datos de la columna como listas
    col1 = []
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        next(reader1, None)  # Saltar encabezado si es necesario
        for row in reader1:
            if len(row) > col_index:
                col1.append(row[col_index])

    col2 = []
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        next(reader2, None)
        for row in reader2:
            if len(row) > col_index:
                col2.append(row[col_index])

    # Comparar columnas
    are_equal = col1 == col2
    differences = []
    for i, (val1, val2) in enumerate(zip(col1, col2)):
        if val1 != val2:
            differences.append((i, val1, val2))
    
    return are_equal, differences  # Bool para coincidencia, lista de (índice_fila, val1, val2)

# Uso
equal, diffs = compare_columns('file1.csv', 'file2.csv', col_index=1)  # Comparar columna 1
print("¿Columnas iguales?", equal)
print("Diferencias (fila, val1, val2):", diffs)
```

- **Cómo funciona**: Extrae la columna especificada en listas, luego compara elemento por elemento. Asume que los CSVs tienen el mismo número de filas; maneja desajustes si es necesario.
- **Variaciones**: Usa `pandas` para operaciones de columna más avanzadas (por ejemplo, `df1['column'] == df2['column']`), pero usa `csv` para usar solo la biblioteca estándar.

#### Consejos y Casos Extremos
- **Encabezados**: Si los CSVs tienen encabezados, omítelos con `next(reader)`.
- **Tipos de Datos**: CSV lee como strings; convierte a int/float si es necesario (por ejemplo, `int(row[0])`).
- **Archivos Grandes**: Para CSVs grandes, usa DictReader para acceso indexado: `csv.DictReader(file)` devuelve filas como OrderedDicts.
- **Delimitador**: Usa `delimiter=';'` en reader/writer si no está separado por comas.
- **Errores**: Envuelve en try-except para problemas de archivo; valida longitudes de columna para evitar errores de índice.
- **Alternativas**: Para comparaciones complejas, considera bibliotecas como `pandas` (`df1.equals(df2)` para dataframes).

Para documentación completa, consulta la [guía oficial del módulo csv de Python](https://docs.python.org/3/library/csv.html). ¡Si tienes archivos CSV específicos o lógica de comparación, proporciona más detalles para un código personalizado!