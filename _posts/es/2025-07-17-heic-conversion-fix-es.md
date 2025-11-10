---
audio: false
generated: true
lang: es
layout: post
title: Corrección del Error de Soporte HEIC en Almohadas
translated: true
type: note
---

El error `cannot identify image file` indica que Pillow no puede leer los archivos HEIC, probablemente debido a una de las siguientes razones:
1. **Falta la librería `libheif`**: Pillow requiere `libheif` para manejar archivos HEIC, y puede que no esté instalada o configurada correctamente en tu sistema.
2. **Archivos HEIC corruptos o incompatibles**: Los archivos HEIC pueden estar corruptos o en un formato que Pillow no puede procesar.
3. **Problema de versión de Pillow**: Aunque Pillow 9.0.0+ soporta HEIC, podría haber un problema de configuración o una versión desactualizada.

Como estás en macOS (basado en tu salida anterior), proporcionaré un script de Python corregido que incluye manejo de errores adicional y registro para diagnosticar el problema. También te guiaré a través de la instalación de `libheif` y la verificación del soporte HEIC de Pillow. Si Pillow sigue fallando, el script incluye un respaldo para usar `ImageMagick` (si está instalado) para la conversión HEIC.

### Pasos para Solucionar el Problema

#### 1. Instalar `libheif`
Pillow depende de `libheif` para el soporte HEIC. Instálalo usando Homebrew:
```bash
brew install libheif
```
Después de instalar, reinstala Pillow para asegurarte de que se enlace con `libheif`:
```bash
pip uninstall pillow
pip install pillow
```

#### 2. Verificar el Soporte HEIC de Pillow
Comprueba si Pillow puede manejar archivos HEIC:
```bash
python -c "from PIL import features; print(features.check_feature('heic'))"
```
- Si devuelve `True`, Pillow tiene soporte HEIC.
- Si devuelve `False` o un error, `libheif` no está configurado correctamente, o Pillow fue compilado sin soporte HEIC.

#### 3. Verificar la Integridad de los Archivos
Asegúrate de que los archivos HEIC no estén corruptos. Intenta abrir uno de los archivos (por ejemplo, `IMG_5988.HEIC`) en un visor como Vista Previa en macOS. Si no se abre, los archivos pueden estar corruptos y necesitarás reexportarlos u obtener nuevas copias.

#### 4. Script de Python Actualizado
El script actualizado:
- Usa Pillow para la conversión HEIC con mejor manejo de errores.
- Recurre a `ImageMagick` (si está instalado) cuando Pillow no puede leer un archivo HEIC.
- Registra errores detallados en un archivo (`conversion_errors.log`) para depuración.
- Soporta extensiones `.heic` y `.heif`.
- Comprime los JPG de salida a ~500KB.

```python
import os
import argparse
import subprocess
import logging
from PIL import Image
from datetime import datetime

# Configurar el registro
logging.basicConfig(
    filename="conversion_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Analizar argumentos de línea de comandos
parser = argparse.ArgumentParser(description="Convertir imágenes HEIC a JPG y comprimir a ~500KB.")
parser.add_argument("input_dir", help="Directorio que contiene los archivos HEIC")
args = parser.parse_args()

# Definir directorios de entrada y salida
input_dir = args.input_dir.rstrip(os.sep)
output_dir = input_dir + "_compressed"
target_size_kb = 500  # Tamaño objetivo del archivo en KB

# Crear directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def get_file_size(file_path):
    """Devuelve el tamaño del archivo en KB."""
    return os.path.getsize(file_path) / 1024

def convert_with_imagemagick(heic_path, jpg_path):
    """Respaldo a ImageMagick para conversión HEIC a JPG."""
    try:
        subprocess.run(
            ["magick", heic_path, "-quality", "85", jpg_path],
            check=True, capture_output=True, text=True
        )
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"ImageMagick falló para {heic_path}: {e.stderr}")
        return False
    except FileNotFoundError:
        logging.error("ImageMagick no está instalado. Instálalo con 'brew install imagemagick'.")
        return False

def convert_heic_to_jpg(heic_path, jpg_path, quality=85):
    """Convertir HEIC a JPG y comprimir al tamaño objetivo aproximado."""
    try:
        # Intentar primero con Pillow
        image = Image.open(heic_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Guardar como JPG con calidad inicial
        image.save(jpg_path, "JPEG", quality=quality)
        
        # Ajustar la calidad para acercarse al tamaño objetivo
        current_size = get_file_size(jpg_path)
        low, high = 10, 100
        while low <= high and abs(current_size - target_size_kb) > 10:
            quality = (low + high) // 2
            image.save(jpg_path, "JPEG", quality=quality)
            current_size = get_file_size(jpg_path)
            if current_size > target_size_kb:
                high = quality - 1
            else:
                low = quality + 1
        return True
    except Exception as e:
        logging.error(f"Pillow falló para {heic_path}: {e}")
        # Respaldo a ImageMagick
        return convert_with_imagemagick(heic_path, jpg_path)

# Procesar todos los archivos HEIC en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".heic", ".heif")):
        heic_path = os.path.join(input_dir, filename)
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        jpg_path = os.path.join(output_dir, jpg_filename)

        try:
            if convert_heic_to_jpg(heic_path, jpg_path):
                print(f"Convertido {filename} a {jpg_filename}, tamaño: {get_file_size(jpg_path):.2f} KB")
            else:
                print(f"Error procesando {filename}: La conversión falló (revisa conversion_errors.log)")
        except Exception as e:
            print(f"Error procesando {filename}: {e}")
            logging.error(f"Error general para {heic_path}: {e}")

print("¡Conversión por lotes completada! Revisa conversion_errors.log por si hay problemas.")
```

### Cómo Usarlo
1. **Guardar el script**:
   Guarda el código como `photo_compress.py` en tu directorio `scripts/media/`.

2. **Instalar dependencias**:
   - Asegúrate de que Pillow esté instalado:
     ```bash
     pip install --upgrade pillow
     ```
   - Instala `libheif`:
     ```bash
     brew install libheif
     ```
   - Opcionalmente, instala ImageMagick como respaldo:
     ```bash
     brew install imagemagick
     ```

3. **Ejecutar el script**:
   ```bash
   python scripts/media/photo_compress.py ./assets/images/yuebei
   ```
   - Esto procesa todos los archivos `.heic` y `.heif` en `assets/images/yuebei`.
   - Los JPG de salida se guardan en `assets/images/yuebei_compressed`.
   - Los errores se registran en `conversion_errors.log` en el directorio actual.

4. **Revisar el registro**:
   Si algún archivo falla al convertirse, revisa `conversion_errors.log` para ver mensajes de error detallados.

### Solución de Problemas Adicional
- **Si Pillow sigue fallando**:
  - Verifica que `libheif` esté instalado y enlazado correctamente:
    ```bash
    pkg-config --modversion libheif
    ```
    Si esto falla, reinstala `libheif` y Pillow.
  - Prueba un archivo manualmente:
    ```python
    from PIL import Image
    img = Image.open("./assets/images/yuebei/IMG_5988.HEIC")
    print("Imagen abierta exitosamente")
    ```
    Si esto falla, el archivo puede estar corrupto o ser una variante HEIC no soportada.

- **Archivos corruptos**:
  - Intenta convertir un archivo con ImageMagick manualmente:
    ```bash
    magick ./assets/images/yuebei/IMG_5988.HEIC test.jpg
    ```
    Si esto falla, es probable que el archivo esté corrupto.

- **Respaldo de ImageMagick**:
  - Si Pillow falla consistentemente, el script intentará usar ImageMagick (si está instalado).
  - Instala `jpegoptim` para un mejor control de compresión:
    ```bash
    brew install jpegoptim
    ```
    Luego, después de ejecutar el script, comprime la salida:
    ```bash
    for i in ./assets/images/yuebei_compressed/*.jpg; do jpegoptim --size=500k "$i"; done
    ```

### Referencias
- [Documentación de Pillow](https://pillow.readthedocs.io/en/stable/)
- [ImageMagick](https://imagemagick.org/)
- [libheif](https://github.com/strukturag/libheif)
- [jpegoptim](https://github.com/tjko/jpegoptim)

Si aún encuentras problemas, comparte el contenido de `conversion_errors.log` o cualquier mensaje de error nuevo, ¡y puedo proporcionar más ayuda!