---
audio: false
generated: true
lang: es
layout: post
title: Corrección del Error ModuleNotFoundError en distutils de Python
translated: true
type: note
---

El error ocurre porque el módulo `distutils`, parte de la librería estándar de Python, falta en tu entorno. Esto es común en instalaciones mínimas de Python. Aquí se explica cómo solucionarlo:

### Solución:
1. **Instala las herramientas de desarrollo de Python** (incluye `distutils`):
   ```bash
   sudo apt update && sudo apt install python3-distutils python3-dev
   ```

2. **Reinstala `setuptools`** (para garantizar la funcionalidad correcta):
   ```bash
   pip install --upgrade --force-reinstall setuptools
   ```

3. **Reintenta instalar tus requirements**:
   ```bash
   pip install -r requirements.local.txt
   ```

### Por qué funciona esto:
- `python3-distutils` proporciona el módulo `distutils` que falta.
- `python3-dev` incluye las herramientas y cabeceras necesarias para compilación.
- Reinstalar `setuptools` resuelve cualquier problema de configuración persistente.

Si estás en un entorno virtual, recréalo después de instalar los paquetes del sistema para asegurar que el entorno tenga acceso a los módulos requeridos.