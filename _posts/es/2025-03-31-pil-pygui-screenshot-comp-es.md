---
audio: false
generated: true
image: false
lang: es
layout: post
title: 'Comparación de Capturas de Pantalla: PIL vs PyAutoGUI'
translated: true
type: note
---

Tanto **`ImageGrab` de PIL** como **las herramientas de captura de pantalla de PyAutoGUI** te permiten capturar la pantalla, pero difieren en uso, características y soporte multiplataforma.

---

## 1. PIL (Pillow) – `ImageGrab`

`ImageGrab` es parte de **Pillow (el fork moderno de PIL)**. Te permite capturar la pantalla o una parte de ella.

### Cómo funciona

* En **Windows y macOS**, utiliza APIs nativas (GDI en Windows, Quartz en macOS) para capturar píxeles.
* En **Linux**, no es compatible por defecto (necesita bibliotecas adicionales como `xwd`).

### Ejemplo de uso

```python
from PIL import ImageGrab

# Capturar pantalla completa
screenshot = ImageGrab.grab()
screenshot.save("screenshot.png")

# Capturar una región (izquierda, superior, derecha, inferior)
region = (100, 100, 500, 500)
cropped_screenshot = ImageGrab.grab(bbox=region)
cropped_screenshot.show()
```

### Ventajas

* Sencillo, parte de Pillow (sin dependencias adicionales).
* Bueno cuando ya estás trabajando con Pillow para procesamiento de imágenes.

### Desventajas

* Sin soporte para Linux por defecto.
* Menos flexibilidad (sin conocimiento de múltiples monitores).

---

## 2. PyAutoGUI – `screenshot()`

PyAutoGUI es más genérico y está orientado a la automatización (control de ratón/teclado + captura de pantalla).

### Cómo funciona

* Utiliza **Pillow internamente**.
* Usa APIs del sistema operativo (multiplataforma: Windows, macOS, Linux).
* Puede devolver un objeto `Image` de Pillow directamente o guardarlo en un archivo.

### Ejemplo de uso

```python
import pyautogui

# Capturar pantalla completa
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

# Capturar una región (izquierda, superior, ancho, alto)
region_screenshot = pyautogui.screenshot(region=(100, 100, 400, 400))
region_screenshot.show()
```

### Ventajas

* Multiplataforma (Windows, macOS, Linux).
* Fácil de integrar con scripts de automatización (control de ratón/teclado).
* Puede capturar regiones específicas directamente.

### Desventajas

* Ligeramente más lento que `ImageGrab` ya que abstrae más funcionalidades.
* Dependencia adicional (`pip install pyautogui`).

---

## ¿Cuál deberías usar?

* **Si solo necesitas capturas de pantalla y estás en Windows/macOS** → `ImageGrab` es ligero y rápido.
* **Si también necesitas automatización o soporte para Linux** → `pyautogui` es mejor.

---

👉 ¿Quieres que también te muestre **cómo evaluar el rendimiento** de la diferencia entre `ImageGrab` y `pyautogui.screenshot()` con código Python?