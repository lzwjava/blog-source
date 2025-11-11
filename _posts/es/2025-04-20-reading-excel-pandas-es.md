---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Leer archivos de Excel con Pandas
translated: true
type: note
---

### Requisitos previos
Para leer archivos Excel en Python, necesitas la librería `pandas` y un motor de Excel. Instala pandas si aún no lo tienes:
```
pip install pandas
```
Para formatos modernos de Excel (.xlsx), instala `openpyxl`:
```
pip install openpyxl
```
Para archivos .xls, usa `xlrd`:
```
pip install xlrd
```

### Uso básico
Pandas proporciona la función `pd.read_excel()` para cargar datos de Excel en un DataFrame.

1. Importa pandas:
   ```python
   import pandas as pd
   ```

2. Lee el archivo Excel (especifica la ruta del archivo):
   ```python
   df = pd.read_excel('ruta/a/tu/archivo.xlsx')
   ```
   - Esto carga la primera hoja por defecto.
   - El resultado es un DataFrame que contiene los datos de Excel.

3. Inspecciona los datos:
   ```python
   print(df.head())  # Ver las primeras 5 filas
   print(df.info())  # Resumen de columnas y tipos de datos
   ```

### Opciones avanzadas
- **Especificar una hoja**: Usa el parámetro `sheet_name` (por defecto es 0 para la primera hoja):
  ```python
  df = pd.read_excel('archivo.xlsx', sheet_name='Hoja2')  # Por nombre
  df = pd.read_excel('archivo.xlsx', sheet_name=1)        # Por índice (base 0)
  ```
- **Leer múltiples hojas**: Pasa una lista o `None` para cargar todas las hojas como un diccionario:
  ```python
  todas_las_hojas = pd.read_excel('archivo.xlsx', sheet_name=None)  # Dict de DataFrames indexado por nombre de hoja
  ```
- **Especificar rango de datos**: Usa `usecols` para columnas (ej., `'A:C'` para columnas A a C) y `skiprows` para saltar filas iniciales:
  ```python
  df = pd.read_excel('archivo.xlsx', usecols='A,C,E', skiprows=2)
  ```
- **Manejar encabezados**: Si el encabezado no está en la fila 0, especifícalo con `header`:
  ```python
  df = pd.read_excel('archivo.xlsx', header=1)  # Encabezado en fila 1 (índice base 0)
  ```
- **Establecer índice**: Usa `index_col` para establecer una columna como el índice:
  ```python
  df = pd.read_excel('archivo.xlsx', index_col='Nombre de Columna')
  ```

### Ejemplo
Supongamos que tienes un archivo Excel `ventas.xlsx` con una hoja llamada "Datos" que contiene información de ventas.

```python
import pandas as pd

# Lee la hoja específica
df = pd.read_excel('ventas.xlsx', sheet_name='Datos')

# Muestra el DataFrame
print(df)

# Guarda a CSV si es necesario
df.to_csv('ventas.csv', index=False)
```

Para más detalles, consulta la [documentación de pandas sobre read_excel](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html). Si encuentras errores, verifica el formato del archivo Excel y asegúrate de que los paquetes requeridos estén instalados.