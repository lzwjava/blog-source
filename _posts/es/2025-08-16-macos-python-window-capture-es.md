---
audio: false
generated: true
image: false
lang: es
layout: post
title: Métodos de Captura de Ventanas de Python en MacOS
translated: true
type: note
---

Buena pregunta 👍 — `pygetwindow` es un wrapper ligero, pero hay varias otras bibliotecas de Python que puedes usar en macOS para obtener la geometría de la ventana activa para capturas de pantalla:

---

## 1. **PyObjC + Quartz (API nativa de macOS)**

Esta es la forma más directa y confiable en macOS, ya que `Quartz` te da información de la ventana a nivel del sistema. Ejemplo:

```bash
python3 -m pip install pyobjc
```

```python
import Quartz
from PIL import ImageGrab

# Obtener los límites de la ventana activa
window_info = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID
)

active_app = Quartz.CGWindowListCopyWindowInfo(
    Quartz.kCGWindowListOptionOnScreenOnly | Quartz.kCGWindowListOptionOnScreenAbove,
    Quartz.kCGNullWindowID,
)

if active_app:
    bounds = active_app[0]['kCGWindowBounds']
    x, y = int(bounds['X']), int(bounds['Y'])
    w, h = int(bounds['Width']), int(bounds['Height'])
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save("active-window.png")
    print(f"Saved active-window.png size={img.size}")
```

Esto evita depender de `pygetwindow` y se comunica directamente con CoreGraphics.

---

## 2. **AppKit (vía PyObjC)**

También de PyObjC, pero a través de AppKit:

```python
from AppKit import NSWorkspace

ws = NSWorkspace.sharedWorkspace()
active_app = ws.frontmostApplication()
print("Active App:", active_app.localizedName())
```

Todavía necesitarías `Quartz` para las coordenadas, pero AppKit te da el proceso en primer plano de forma más limpia.

---

## 3. **PyWinCtl**

Reemplazo multiplataforma para `pygetwindow` (Windows, macOS, Linux):

```bash
python3 -m pip install pywinctl
```

```python
import pywinctl
from PIL import ImageGrab

active = pywinctl.getActiveWindow()
if active:
    x, y, w, h = active.left, active.top, active.width, active.height
    img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    img.save("active-window.png")
    print("Saved active-window.png")
```

Esta es probablemente la alternativa más cercana a "drop-in" para pygetwindow, pero con un soporte más consistente para macOS.

---

## 4. **PyAutoGUI**

Aunque PyAutoGUI en sí mismo no proporciona manejadores de ventanas, puedes capturar la pantalla completa o definir una región manualmente una vez que sepas las coordenadas (desde Quartz/AppKit).

---

✅ Si quieres un **reemplazo puramente multiplataforma** para `pygetwindow`: usa **`pywinctl`**.
✅ Si quieres **precisión nativa de macOS y más control**: usa **PyObjC + Quartz**.

¿Quieres que te muestre un script listo para usar que **solo depende de PyObjC (Quartz)** (sin wrappers de terceros), para que puedas dejar `pygetwindow` por completo?