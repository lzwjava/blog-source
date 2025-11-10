---
audio: false
generated: true
image: false
lang: es
layout: post
title: Corregir Error del Backend de Imágenes PIL
translated: true
type: note
---

Este error significa que tu instalación de PIL carece del backend binario (`_imaging`) o estás usando accidentalmente el antiguo paquete "PIL" en lugar del moderno "Pillow". Así es como solucionarlo:

1. **Asegúrate de usar Python 3**
   Si `python` apunta a Python 2, cambia a Python 3:

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **Desinstala cualquier paquete PIL obsoleto**

   ```bash
   # esto elimina el PIL antiguo si está instalado via pip
   python3 -m pip uninstall -y PIL
   ```

3. **(Re)instala Pillow**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **Instala las librerías del sistema requeridas**
   En Ubuntu necesitarás los headers de imagen para que Pillow pueda construir su extensión `_imaging`:

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # luego reinstala Pillow para que se recompile contra esas librerías
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **Usa un entorno virtual (opcional pero recomendado)**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

Después de esto, `from PIL import Image` debería funcionar sin el error de importación `_imaging`.