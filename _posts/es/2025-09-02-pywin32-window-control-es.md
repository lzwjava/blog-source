---
audio: false
generated: true
image: false
lang: es
layout: post
title: Esenciales del Control de Ventanas con PyWin32
translated: true
type: note
---

Aquí tienes una guía para trabajar con **ventanas de PyWin32**—centrándose en sus propiedades, activación y manejo del área inferior.

---

## 1. ¿Qué es una ventana en PyWin32?

En PyWin32, una "ventana" se refiere a cualquier elemento de interfaz gráfica gestionado por la API de Windows que tiene un **identificador (HWND)**. Esto puede ser una ventana de aplicación de nivel superior, un cuadro de diálogo o incluso un control dentro de un formulario.

Normalmente interactúas con las ventanas mediante:

* `win32gui` – funciones de bajo nivel para identificadores de ventana, propiedades y mensajes.
* `win32con` – constantes para mensajes y estilos de Windows.
* `win32api` – funciones generales de la API de Windows.

---

## 2. Propiedades comunes de una ventana

Una ventana tiene muchos atributos que puedes consultar o modificar:

* **Identificador (HWND)**: Identificador único de la ventana.
* **Título (Caption)**: Texto que se muestra en la barra de título (`win32gui.GetWindowText(hwnd)`).
* **Nombre de clase**: Clase registrada de la ventana (`win32gui.GetClassName(hwnd)`).
* **Estilos**: Define cómo se comporta y se ve la ventana (`GetWindowLong` con `GWL_STYLE`).
* **Posición y tamaño**: Coordenadas del rectángulo mediante `GetWindowRect(hwnd)` o `MoveWindow`.
* **Visibilidad**: Si la ventana se muestra o no (`IsWindowVisible`).
* **Estado habilitado**: Si acepta entrada de datos o no (`IsWindowEnabled`).
* **Padre/Propietario**: Jerarquía de ventanas (`GetParent(hwnd)`).

---

## 3. Activación de ventanas

Para traer una ventana al frente o hacerla activa:

* **SetForegroundWindow(hwnd)** – convierte la ventana en la activa.
* **SetActiveWindow(hwnd)** – la activa pero no garantiza que esté encima de todo.
* **BringWindowToTop(hwnd)** – la eleva por encima de las demás.
* **ShowWindow(hwnd, flag)** – la muestra/oculta/minimiza/maximiza dependiendo de `flag` (como `SW_SHOW`, `SW_MINIMIZE`, `SW_RESTORE`).

---

## 4. "Área inferior" (Orden Z y Ubicación)

Las ventanas se organizan en capas en un orden Z:

* **Siempre encima (Topmost)** – siempre por encima de las demás (`SetWindowPos` con `HWND_TOPMOST`).
* **Fondo (Bottom)** – puedes enviar una ventana detrás de todas las demás usando `SetWindowPos(hwnd, win32con.HWND_BOTTOM, …)`.
* **Sin activar (NoActivate)** – puedes mostrar o posicionar una ventana sin activarla (usando flags como `SWP_NOACTIVATE`).

Esto suele ser útil si quieres que una ventana de utilidad en segundo plano permanezca abierta pero no robe el foco.

---

## 5. Funciones típicas que usarás

Aquí hay algunas funciones clave de PyWin32 con ejemplos:

```python
import win32gui
import win32con

# Encontrar ventana por título
hwnd = win32gui.FindWindow(None, "Untitled - Notepad")

# Obtener propiedades
title = win32gui.GetWindowText(hwnd)
rect = win32gui.GetWindowRect(hwnd)  # (left, top, right, bottom)

# Activar ventana
win32gui.SetForegroundWindow(hwnd)

# Mover al fondo (detrás de otras)
win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, 0, 0,
                      win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Mostrar/restaurar
win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
```

---

## 6. Manejo de eventos/mensajes

También puedes conectarte a eventos de ventana (activación, cambio de tamaño, cierre) usando:

* `SetWindowLong` para crear una subclase.
* `SendMessage` / `PostMessage` para simular acciones.
* Mensajes como `WM_ACTIVATE`, `WM_SIZE`, etc.

---

✅ En resumen:

* **Propiedades**: título, clase, tamaño, estilo, visibilidad, estado habilitado.
* **Activación**: usa `SetForegroundWindow`, `BringWindowToTop`.
* **Área inferior**: gestiona el orden Z con `SetWindowPos` y `HWND_BOTTOM`.

¿Te gustaría que también incluyera un **script práctico** que liste todas las ventanas de nivel superior con sus propiedades (título, posición, orden z) y te permita activarlas o enviarlas al fondo de forma interactiva?