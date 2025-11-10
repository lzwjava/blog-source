---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía Rápida de PyGetWindow
translated: true
type: note
---

### Instalación
PyGetWindow es una biblioteca de Python para manipular y consultar ventanas en múltiples plataformas (Windows, macOS y Linux). Instálala mediante pip:

```bash
pip install pygetwindow
```

### Importar el Módulo
Comienza importando el módulo en tu script de Python:

```python
import pygetwindow as gw
```

### Obtener Objetos de Ventana
PyGetWindow representa las ventanas como objetos `Window`. Puedes recuperar ventanas por título, proceso u otros atributos.

- **Obtener todos los objetos de ventana**:  
  Usa `gw.getAllWindows()` para devolver una lista de todas las ventanas abiertas.

- **Obtener ventanas por título**:  
  Usa `gw.getWindowsWithTitle(title)` o `gw.getFirstWindowWithTitle(title)` para coincidencias parciales o exactas.

- **Obtener ventana activa**:  
  Usa `gw.getActiveWindow()` para obtener la ventana que tiene el foco actualmente.

Ejemplo:
```python
windows = gw.getAllWindows()
active = gw.getActiveWindow()
notepad = gw.getWindowsWithTitle('Notepad')  # Lista de ventanas con 'Notepad' en el título
```

### Métodos Comunes en Objetos Window
Una vez que tienes un objeto `Window`, puedes acceder a propiedades y métodos como:

- **Propiedades**: `title`, `left`, `top`, `width`, `height`, `isMinimized`, `isMaximized`, `isActive`.
- **Métodos**: 
  - `activate()`: Traer la ventana al frente y hacerla activa.
  - `maximize()` / `minimize()` / `restore()` / `close()`: Controlar el estado de la ventana.
  - `resize() / move()`: Ajustar el tamaño y la posición.

Ejemplo:
```python
if notepad:
    win = notepad[0]
    print(win.title)  # Salida: p. ej., 'Untitled - Notepad'
    win.activate()
    win.maximize()
    win.move(100, 100)  # Mover a la posición (100, 100)
    win.resize(800, 600)  # Redimensionar a 800x600
```

### Manejo de Múltiples Plataformas
- En Windows y macOS, utiliza APIs nativas.
- En Linux, depende del soporte para X11 o Wayland; asegúrate de que tu sistema lo tenga instalado (p. ej., `x11-utils` en Ubuntu).
- Si un método no es compatible con tu sistema operativo, puede generar un `NotImplementedError`.

### Ejemplos
Aquí hay algunos fragmentos de código prácticos:

1. **Imprimir todos los títulos de ventana**:
   ```python
   for win in gw.getAllWindows():
       print(win.title)
   ```

2. **Cerrar una ventana específica**:
   ```python
   firefox_wins = gw.getWindowsWithTitle('Mozilla Firefox')
   if firefox_wins:
       firefox_wins[0].close()
   ```

3. **Mover y redimensionar múltiples ventanas**:
   ```python
   windows = gw.getAllWindows()
   for i, win in enumerate(windows[:3]):  # Primeras 3 ventanas
       win.move(50 * i, 50 * i)
       win.resize(400, 400)
   ```

Para un uso avanzado, consulta la [documentación oficial](https://pygetwindow.readthedocs.io/). Si encuentras problemas específicos de la plataforma, verifica los permisos del sistema o dependencias como `xdotool` en Linux.