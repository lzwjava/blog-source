---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Capturas de Pantalla con PIL ImageGrab
translated: true
type: note
---

### Requisitos Previos
Para usar `ImageGrab` de la librería PIL (Pillow), asegúrate de tener Pillow instalado. En Windows, instálalo mediante pip:
```
pip install Pillow
```
Normalmente no se necesita configuración adicional en Windows, ya que `ImageGrab` utiliza APIs nativas de Windows.

### Uso Básico
`ImageGrab.grab()` captura toda la pantalla (todos los monitores) como un objeto PIL Image. Aquí tienes un ejemplo simple para tomar una captura de pantalla y guardarla como un archivo PNG:

```python
from PIL import ImageGrab

# Capturar toda la pantalla
screenshot = ImageGrab.grab()

# Guardar la imagen en un archivo
screenshot.save("screenshot.png")
```

Esto guardará un archivo llamado `screenshot.png` en tu directorio de trabajo actual.

### Opciones Adicionales
- **Capturar una región específica**: Especifica un cuadro delimitador (izquierda, arriba, derecha, abajo) como una tupla de coordenadas de píxeles.
  ```python
  # Capturar un área de 300x300 píxeles comenzando en (100, 100)
  region = (100, 100, 400, 400)  # Ajusta las coordenadas según sea necesario
  screenshot = ImageGrab.grab(bbox=region)
  screenshot.save("region_screenshot.png")
  ```
- **Incluir el cursor del ratón** (si es compatible; consulta la documentación de Pillow para detalles de la versión):
  ```python
  # Nota: Esto puede requerir include_layered_windows=True en algunos sistemas
  screenshot = ImageGrab.grab(include_layered_windows=True)
  ```
- **Mostrar la imagen**: Usa `screenshot.show()` para abrirla en tu visor de imágenes predeterminado (para pruebas).

### Notas
- Las coordenadas están en píxeles, con (0, 0) en la esquina superior izquierda del monitor principal.
- Para configuraciones con múltiples monitores, `grab()` captura todas las pantallas como una imagen compuesta.
- Si encuentras problemas (por ejemplo, errores de permisos en versiones más recientes de Windows), asegúrate de que tu script tenga permisos de captura de pantalla o intenta ejecutarlo con privilegios de administrador.
- Documentación completa: [Pillow ImageGrab docs](https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html). Para peculiaridades específicas de Windows, consulta los issues de GitHub si es necesario.