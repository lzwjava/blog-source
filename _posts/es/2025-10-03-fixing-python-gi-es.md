---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast:free
title: Arreglar Los Enlaces De Python GI Rotos
translated: true
type: note
---

### Diagnóstico Actualizado
Basándome en los nuevos detalles, tu instalación de Python 3.13.7 (probablemente manual o mediante PPA/código fuente) ha dañado los enlaces GObject Introspection (GI) del sistema. La extensión C `_gi` del módulo `gi` está compilada para la versión predeterminada de Python de tu distribución (probablemente 3.10 o 3.11, dados los directorios en `/usr/lib/python`), no para la 3.13. Esto provoca el error de importación circular cuando `gnome-terminal` (un script de Python) intenta cargarlo. La configuración multi-versión en `/usr/lib/python` confirma esta discrepancia—los paquetes del sistema como `python3-gi` aún no están construidos para 3.13 (es demasiado nueva para la mayoría de distribuciones a fecha de 2025).

Los registros de UFW siguen siendo ruido irrelevante.

### Solución Recomendada: Revertir al Python Predeterminado del Sistema
La solución más limpia es cambiar `/usr/bin/python3` de nuevo a la versión predeterminada de tu distribución (ej. 3.10), y luego reinstalar los enlaces GI. Esto evita trucos como copiar archivos .so, que pueden causar inconsistencias.

1.  **Identificar y cambiar a la versión predeterminada de Python** (usa `update-alternatives` si está configurado; si no, un enlace simbólico manual):
    ```
    # Comprobar si hay alternativas configuradas
    sudo update-alternatives --config python3
    ```
    - Si muestra opciones, selecciona la de menor prioridad (normalmente la predeterminada de la distribución, como 3.10).
    - Si no hay alternativas (común en Ubuntu estándar), revierte manualmente:
      ```
      # Suponiendo que la predeterminada es 3.10 (común para Ubuntu 22.04; cámbialo a 3.11 si esa es tu base)
      sudo rm /usr/bin/python3
      sudo ln -s /usr/bin/python3.10 /usr/bin/python3
      ```
    - Verifica: `python3 --version` debería mostrar ahora 3.10.x (o tu versión predeterminada).

2.  **Reinstalar los paquetes GI y GNOME Terminal**:
    ```
    sudo apt update
    sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
    ```

3.  **Probar**:
    ```
    python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
    gnome-terminal
    ```
    - Si la prueba de Python funciona pero el terminal sigue fallando, restablece su configuración: `dconf reset -f /org/gnome/terminal/`.

### Si Quieres Mantener Python 3.13
- Esto es más complicado, ya que oficialmente `python3-gi` no existirá aún para 3.13. Necesitarías compilar PyGObject desde el código fuente:
  1. Instala las dependencias de compilación: `sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`.
  2. Descarga y compila PyGObject: Sigue la [guía oficial](https://pygobject.gnome.org/install.html) con `--prefix=/usr/local`.
  3. Pero esto arriesga a romper otras herramientas del sistema—revierte si surgen problemas.
- O, de forma poco elegante, copia la extensión `_gi` (no recomendado a largo plazo):
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # Ajusta '3[01]' a tu versión predeterminada (3.10 o 3.11)
  ```
  Luego reinstala `python3-gi` como se indicó arriba.

### Prevención
- No anules manualmente `/usr/bin/python3`—usa entornos virtuales (`python3 -m venv myenv`) para proyectos que necesiten 3.13.
- Si instalaste 3.13 mediante el PPA deadsnakes, elimínalo y mantente con el Python de la distribución.

Si esto no lo soluciona, ejecuta `ls -l /usr/bin/python*` y `dpkg -l | grep python3 | grep -E 'gi|default'` y comparte la salida.

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)