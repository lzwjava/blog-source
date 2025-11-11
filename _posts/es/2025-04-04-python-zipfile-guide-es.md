---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía del Paquete ZipFile de Python
translated: true
type: note
---

### Descripción general del paquete ZipFile
El módulo `zipfile` de Python permite leer y escribir archivos de archivo ZIP sin herramientas externas. Es parte de la biblioteca estándar, por lo que no requiere instalación (desde Python 2.3+). Úsalo para comprimir, descomprimir o manipular archivos ZIP mediante programación. Admite varios métodos de compresión como DEFLATE.

Impórtalo con: `import zipfile`

### Lectura de archivos ZIP
Para extraer o inspeccionar archivos ZIP existentes:

1. **Abrir un archivo ZIP para lectura**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       # 'r' es para modo lectura
   ```

2. **Listar contenidos**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       file_list = zip_ref.namelist()  # Devuelve una lista de nombres de archivo
       print(file_list)
   ```

3. **Extraer archivos**:
   - Extraer todo: `zip_ref.extractall('carpeta_destino')`
   - Extraer uno: `zip_ref.extract('archivo_dentro.zip', 'ruta')`

4. **Leer el contenido del archivo sin extraer**:
   ```python
   with zipfile.ZipFile('example.zip', 'r') as zip_ref:
       with zip_ref.open('archivo_dentro.zip') as file:
           content = file.read()
           print(content.decode())  # Si es texto
   ```

Nota: Siempre usa `with` para un cierre automático. Para ZIP protegidos con contraseña, añade `pwd=b'contraseña'` a `ZipFile()`.

### Escritura de archivos ZIP
Para crear o añadir a archivos ZIP nuevos o existentes:

1. **Crear un nuevo archivo ZIP**:
   ```python
   with zipfile.ZipFile('nuevo_archivo.zip', 'w') as zip_ref:
       # 'w' es para modo escritura (sobrescribe si existe)
   ```

2. **Añadir archivos**:
   - Añadir uno: `zip_ref.write('archivo_fuente.txt', 'nombre_arco.txt')` (el parámetro opcional `arcname` lo renombra dentro)
   - Añadir múltiples: Itera sobre una lista de archivos y llama a `write()`.

3. **Comprimir mientras escribes** (por defecto es DEFLATE):
   ```python
   with zipfile.ZipFile('archivo.zip', 'w', zipfile.ZIP_DEFLATED) as zip_ref:
       zip_ref.write('archivo_grande.txt')
   ```
   Opciones: `ZIP_STORED` (sin compresión), `ZIP_DEFLATED`, `ZIP_BZIP2`, etc.

4. **Añadir a un ZIP existente** (usa el modo 'a' en lugar de 'w').

### Operaciones comunes y consejos
- **Verificar si un archivo es un ZIP válido**: Usa `zipfile.is_zipfile('archivo.zip')`.
- **Obtener información del archivo**: `zip_ref.getinfo('archivo.txt')` devuelve un objeto ZipInfo con detalles como tamaño, fecha.
- **Manejar archivos grandes**: Leer/extraer archivos grandes puede consumir memoria; usa el método `open()` para streaming.
- **Manejo de errores**: Captura las excepciones `BadZipFile` o `LargeZipFile`.
- **Multiplataforma**: Funciona en Windows, macOS, Linux, pero ten cuidado con los separadores de ruta (usa `/`).
- **Cifrado**: Se admite protección básica con contraseña, pero es débil—usa herramientas más robustas para seguridad.
- **Nivel superior**: Para más características (ej., integración con shutil), combínalo con `shutil.make_archive()` para crear ZIPs.

Ejemplo de script completo para comprimir una carpeta:
```python
import zipfile
import os

def zip_folder(source_dir, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file), os.path.join(source_dir, '..')))

zip_folder('mi_carpeta', 'salida.zip')
```

Para la documentación completa, consulta la [documentación oficial de Python](https://docs.python.org/3/library/zipfile.html). ¡Si tienes una tarea específica (ej., "cómo extraer a memoria"), proporciona más detalles!