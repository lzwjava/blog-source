---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Notificaciones Toast de Windows con Python
translated: true
type: note
---

### ¿Qué es win10toast?
win10toast es una librería ligera de Python que te permite enviar notificaciones toast (alertas emergentes) en Windows 10 desde tus scripts de Python. Es útil para notificaciones al usuario en aplicaciones de escritorio o scripts, similar a los toasts nativos de Windows.

### Prerrequisitos
- Python 3.x instalado.
- Windows 10 (depende de APIs específicas de Windows).
- No se requieren dependencias adicionales más allá de Python.

### Instalación
Instala la librería via pip (el instalador de paquetes de Python):

```
pip install win10toast
```

Si estás usando un entorno virtual, actívalo primero.

### Uso Básico
1. Importa el módulo:
   ```python
   from win10toast import ToastNotifier
   ```

2. Crea una instancia de `ToastNotifier` y llama a su método `show_toast` para mostrar una notificación:
   ```python
   toaster = ToastNotifier()
   toaster.show_toast("Título", "Mensaje", icon_path=None, duration=5)
   ```
   - **Título**: Una cadena de texto para el encabezado de la notificación.
   - **Mensaje**: Una cadena de texto para el cuerpo de la notificación.
   - **icon_path**: Ruta opcional a un archivo .ico o .png para el icono de la notificación (ej., `"ruta/al/icono.ico"`). Omite para no usar icono.
   - **duration**: Tiempo en segundos que el toast permanecerá visible (por defecto es 5; Windows puede anular esto).

La notificación aparecerá en el Centro de actividades y como una ventana emergente.

### Uso Avanzado
- **Personalizar el Icono**: Usa un archivo de imagen (se recomienda 128x128 píxeles para la mejor calidad).
- **Manejar Eventos de Clic**: Pasa una función callback (soporte limitado; el comportamiento al hacer clic es básico).
- **Múltiples Notificaciones**: Instancia `ToastNotifier` una vez y reutilízala para enviar múltiples toasts.
- **Manejo de Errores**: Envuelve el código en try-except para manejar posibles problemas con la API de Windows, ej., si las notificaciones están deshabilitadas.

Ejemplo con icono y manejo de errores:
```python
from win10toast import ToastNotifier
import os

try:
    toaster = ToastNotifier()
    icon = "C:\\ruta\\al\\icono.ico"  # Reemplaza con la ruta real
    toaster.show_toast("¡Alerta!", "Tu script ha terminado.", icon_path=icon, duration=10)
except Exception as e:
    print(f"La notificación falló: {e}")
```

### Limitaciones y Consejos
- Las notificaciones requieren que el Centro de actividades de Windows 10 esté habilitado (Configuración > Sistema > Notificaciones y acciones).
- Para características más complejas (ej., acciones o imágenes), considera alternativas como plyer o winrt (parte del SDK moderno de Windows).
- Si las notificaciones no aparecen, verifica la configuración de Asistencia de enfoque de Windows o intenta ejecutar el script como administrador.

Para la documentación completa, consulta el [repositorio de GitHub de win10toast](https://github.com/Charnelx/win10toast). Si encuentras problemas, proporciona detalles del error para obtener ayuda específica.