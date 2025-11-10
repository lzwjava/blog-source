---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Procesamiento de Imágenes con PIL Pillow
translated: true
type: note
---

### ¿Qué es PIL/Pillow?
PIL originalmente significaba Python Imaging Library, pero ahora se mantiene como el paquete Pillow (un fork moderno). Lo importas como `PIL` en el código, pero necesitas instalar Pillow via pip. Se utiliza para abrir, manipular y guardar archivos de imagen en Python. Soporta formatos como JPEG, PNG, GIF, BMP y más.

### Instalación
Para usar PIL, instala Pillow:
```bash
pip install pillow
```

### Importación y Uso Básico
Después de instalar, impórtalo así en tu script de Python:
```python
from PIL import Image
```
No es necesario usar `import PIL.Image`—esto importa directamente el módulo Image.

### Operaciones Comunes con Imágenes
Aquí se explica cómo realizar tareas básicas. Supón que tienes un archivo de imagen llamado `example.jpg` en tu directorio.

#### 1. Abrir una Imagen
```python
image = Image.open('example.jpg')  # Abre el archivo de imagen
image.show()  # La muestra (funciona en sistemas con un visor de imágenes)
```

#### 2. Obtener Información de la Imagen
```python
print(image.format)  # ej., 'JPEG'
print(image.size)    # Tupla: (ancho, alto)
print(image.mode)    # ej., 'RGB' para imágenes a color
```

#### 3. Redimensionar una Imagen
```python
resized = image.resize((800, 600))  # Redimensiona a 800x600 píxeles
resized.save('resized_example.jpg')  # Guarda la imagen redimensionada
```

#### 4. Convertir Formatos
```python
image.convert('L').save('grayscale_example.png')  # Convierte a escala de grises y guarda como PNG
```

#### 5. Rotar una Imagen
```python
rotated = image.rotate(90)  # Rota 90 grados en sentido horario
rotated.save('rotated_example.jpg')
```

#### 6. Recortar una Imagen
```python
left, top, right, bottom = 100, 100, 300, 300  # Define el cuadro de recorte (x1, y1, x2, y2)
cropped = image.crop((left, top, right, bottom))
cropped.save('cropped_example.jpg')
```

#### 7. Aplicar Filtros (Requiere Importaciones Adicionales)
Para los filtros, importa `ImageFilter`:
```python
from PIL import ImageFilter
blurred = image.filter(ImageFilter.BLUR)  # Aplica el filtro de desenfoque
blurred.save('blurred_example.jpg')
```

### Ejemplo Avanzado: Procesamiento por Lotes de Múltiples Imágenes
```python
import os
from PIL import Image

# Redimensiona todas las imágenes JPEG en una carpeta a 200x200
input_folder = 'images/'
output_folder = 'resized_images/'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(input_folder, filename))
        resized = image.resize((200, 200))
        resized.save(os.path.join(output_folder, filename))
```

### Consejos y Notas
- **Manejo de Errores**: Usa try-except para archivos inválidos, ej., `try: image = Image.open('file.jpg')`.
- **Eficiencia de Memoria**: Para imágenes grandes, usa `image.close()` después de las operaciones para liberar memoria.
- **Documentación**: Consulta la documentación completa de Pillow en [pillow.readthedocs.io](https://pillow.readthedocs.io/en/stable/) para más funciones como dibujo, adición de texto o manejo de datos EXIF.
- **Dependencias**: Pillow podría necesitar librerías del sistema (ej., libjpeg) en algunas configuraciones; consulta la guía de instalación si surgen problemas.

¡Si tienes una tarea específica o un error, proporciona más detalles para una ayuda personalizada!