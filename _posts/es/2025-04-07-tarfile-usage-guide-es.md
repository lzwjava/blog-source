---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Uso del Módulo Tarfile de Python
translated: true
type: note
---

### Importar el módulo tarfile

Para usar la biblioteca `tarfile` en Python, primero impórtala:

```python
import tarfile
```

Este módulo es parte de la biblioteca estándar de Python, por lo que no requiere instalación. Está basado en el formato tar POSIX y soporta la lectura y escritura de archivos tar comprimidos o sin comprimir.

### Abrir y crear archivos tar

- **Abrir un archivo tar existente**: Usa `tarfile.open()` con un modo. Los modos incluyen `'r'` (lectura), `'w'` (escribir vacío), `'a'` (añadir), o variantes con compresión como `'r:gz'` para gzip.
  ```python
  import tarfile
  
  # Abrir para lectura (sin comprimir)
  with tarfile.open('example.tar', 'r') as tar:
      # Trabajar con el archivo tar aquí
      pass
  ```
- **Crear un nuevo archivo tar**: Usa el modo `'w'` para crear un archivo vacío. Añade prefijos de compresión como `'w:gz'` para gzip o `'w:bz2'` para bzip2.
  ```python
  # Crear un archivo comprimido tar.gz
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      pass
  ```

### Añadir archivos a un archivo comprimido

- **Añadir un solo archivo**: Llama a `add()` en el objeto del archivo tar, pasando la ruta del archivo. Puedes especificar un arcname para un nombre diferente dentro del archivo.
  ```python
  with tarfile.open('archive.tar.gz', 'w:gz') as tar:
      tar.add('file.txt')  # Añade file.txt tal cual
      tar.add('data.csv', arcname='renamed_data.csv')  # Renombrar dentro del archivo
  ```
- **Añadir múltiples archivos o un directorio**: Usa `add()` en un bucle o añade directorios completos de forma recursiva.
  ```python
  import os
  
  with tarfile.open('backup.tar', 'w') as tar:
      for root, dirs, files in os.walk('my_folder'):
          for file in files:
              tar.add(os.path.join(root, file))
  ```

### Extraer archivos de un archivo comprimido

- **Extraer todos los archivos**: Usa `extractall()` para extraer a un directorio especificado (por defecto, el actual).
  ```python
  with tarfile.open('archive.tar.gz', 'r:gz') as tar:
      tar.extractall(path='extracted_folder')  # Crea la carpeta si es necesario
  ```
- **Extraer archivos específicos**: Lista los miembros primero con `getmembers()`, luego usa `extract()`.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      members = tar.getmembers()
      for member in members:
          if 'important' in member.name:  # Filtro de ejemplo
              tar.extract(member, path='output_dir')
  ```
- Nota: Por seguridad, filtra las rutas (ej., evita `..`) para prevenir ataques de path traversal. `tarfile` realiza algunas comprobaciones, pero se recomienda un filtrado manual para archivos no confiables.

### Listar el contenido de un archivo comprimido

- **Iterar sobre los archivos**: Usa `getmembers()` o itera directamente sobre el objeto tar para obtener objetos TarInfo.
  ```python
  with tarfile.open('example.tar', 'r') as tar:
      for member in tar.getmembers():
          print(f"{member.name}: {member.size} bytes")
  ```

### Modos clave y compresión

- `'r'`: Leer tar sin comprimir.
- `'r:gz'`, `'r:bz2'`, `'r:xz'`: Leer variedades comprimidas.
- `'w'`: Escribir nuevo tar sin comprimir (sobrescribe).
- `'a'`: Añadir a un tar existente.
- La compresión se detecta automáticamente en lectura; se especifica en escritura.

### Consejos y mejores prácticas

- Usa siempre administradores de contexto (sentencias `with`) para asegurar que los archivos se cierren correctamente.
- Para archivos grandes, considera filtrar o extraer selectivamente para ahorrar memoria.
- `tarfile` no maneja archivos cifrados directamente—usa herramientas externas o combínalo con `gzip` manualmente si es necesario.
- Manejo de errores: Captura `tarfile.TarError` para problemas con el archivo.
- Documentación completa: Consulta la [documentación oficial de tarfile](https://docs.python.org/3/library/tarfile.html) de Python para características avanzadas como filtros personalizados.