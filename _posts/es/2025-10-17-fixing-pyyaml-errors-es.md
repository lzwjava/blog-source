---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cómo Corregir Errores de Instalación de PyYAML
translated: true
type: note
---

### Comprender el Error

Esta salida parece provenir de un `python setup.py install` o `pip install pyyaml` (desde el código fuente) en un sistema Linux con Python 3.13. Hay dos problemas principales:

1. **Fallo de Compilación de la Extensión C**:
   - El proceso de compilación intenta compilar la extensión C (`yaml._yaml`) pero no puede encontrar el archivo fuente `yaml/_yaml.c`.
   - Esto sucede porque las versiones más recientes de PyYAML (a partir de la versión 4.x aproximadamente) generan el archivo `_yaml.c` dinámicamente usando Cython durante la compilación. La distribución de código fuente en PyPI no incluye el archivo `.c` pregenerado, por lo que Cython debe estar instalado previamente para crearlo.
   - Como resultado, recurre a la versión pura de Python (que funciona pero es más lenta y carece de algunas funciones como el soporte para libyaml).

2. **Permiso Denegado Durante la Instalación**:
   - La instalación intenta escribir en el directorio global del sistema de Python (`/usr/local/lib/python3.13/dist-packages`), lo que requiere privilegios de root.
   - Esto es común cuando se ejecuta sin `sudo` o sin la bandera `--user`.

### Soluciones

#### Solucionar el Problema de Compilación
Instala Cython primero, y luego reintenta la instalación de PyYAML. Esto generará el archivo `_yaml.c` faltante y permitirá que se compile la extensión C.

- **Usando pip (recomendado)**:
  ```
  pip install cython
  pip install pyyaml
  ```
  - Si quieres la extensión C más rápida con soporte para libyaml (requiere tener libyaml-dev del sistema instalado a través de tu gestor de paquetes, por ejemplo, `sudo apt install libyaml-dev` en Ubuntu/Debian):
    ```
    pip install cython libyaml
    pip install --upgrade --force-reinstall --no-cache-dir pyyaml
    ```

- **Si usas setup.py directamente** (no recomendado, prefiere pip):
  ```
  pip install cython
  python setup.py build_ext --inplace
  python setup.py install
  ```

Nota: Python 3.13 es relativamente nuevo, así que asegúrate de usar la versión más reciente de Cython (por ejemplo, 3.0.11 o superior) para compatibilidad. Si estás en una compilación de Python con hilos libres (free-threaded), pueden ser necesarios ajustes adicionales de compilación—consulta los issues de GitHub de PyYAML para ver actualizaciones.

#### Solucionar el Problema de Permisos
- **Instalar en el directorio del usuario** (más seguro, no necesita sudo):
  ```
  pip install --user cython pyyaml
  ```
  - Esto instala en `~/.local/lib/python3.13/site-packages`.

- **Usar sudo para una instalación global del sistema** (úsalo con precaución, ya que puede generar conflictos con los gestores de paquetes):
  ```
  sudo pip install cython pyyaml
  ```

- **Mejor Práctica: Usar un Entorno Virtual**:
  Para evitar completamente los problemas de permisos:
  ```
  python -m venv myenv
  source myenv/bin/activate  # En Linux/Mac
  pip install cython pyyaml
  ```
  Esto mantiene todo aislado.

Después de la instalación, prueba con `python -c "import yaml; print(yaml.__version__)"`. Si se importa sin errores, está listo.

Si esto no lo resuelve (por ejemplo, debido a un problema específico de Python 3.13), proporciona más detalles como tu comando exacto y la versión del sistema operativo.

[Building on Mac - _yaml.c not found](https://github.com/yaml/pyyaml/issues/122)
[extension _yaml is not built](https://github.com/yaml/pyyaml/issues/179)
[Installing Pyyaml with libyaml support on MacOS](https://akasurde.github.io/installing-pyyaml-with-libyaml-on-macos.html)