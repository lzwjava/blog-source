---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Desglose del archivo setup.py de Requests
translated: true
type: note
---

### Resumen
Este es un archivo `setup.py`, que es un script estándar de Python utilizado con `setuptools` para definir y construir un paquete de Python. Específicamente, este es para la librería **Requests**—un cliente HTTP popular para Python. Maneja metadatos como el nombre del paquete, la versión, las dependencias y los clasificadores (para distribución en PyPI). Cuando ejecutas `pip install requests`, este script (o sus artefactos compilados) es lo que se ejecuta detrás de escenas para instalar el paquete.

El script está estructurado como una única llamada a la función `setup()`, pero incluye algunas protecciones, ayudas y lecturas dinámicas de otros archivos. Lo desglosaré sección por sección.

### 1. Importaciones y Verificación de Versión de Python
```python
#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 9)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    # Mensaje de error y salida
    sys.exit(1)
```
- **Shebang (`#!/usr/bin/env python`)**: Hace que el archivo sea ejecutable en sistemas tipo Unix, ejecutándolo con el intérprete de Python del sistema.
- **Importaciones**: Trae `os` y `sys` para interacciones con el sistema, `codecs.open` para lectura de archivos UTF-8 (para manejar caracteres no ASCII de forma segura), y `setup` de `setuptools` para construir el paquete.
- **Verificación de Versión**: Asegura que el usuario esté ejecutando Python 3.9 o superior. Si no, imprime un mensaje de error útil sugiriendo una actualización o fijar una versión anterior de Requests (<2.32.0), luego sale con el código 1 (fallo). Esto hace cumplir la compatibilidad, ya que Requests eliminó el soporte para versiones antiguas de Python.

### 2. Acceso Directo para Publicar
```python
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()
```
- Una conveniencia para los mantenedores: Si ejecutas `python setup.py publish`, este:
  - Construye la distribución de código fuente (`sdist`) y los archivos wheel (`bdist_wheel`) en la carpeta `dist/`.
  - Los sube a PyPI usando `twine` (un cargador seguro).
- Esta es una forma rápida de lanzar una nueva versión sin comandos manuales. Sale después de ejecutar.

### 3. Dependencias
```python
requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<3",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==2.1.0",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]
```
- **`requires`**: Dependencias principales instaladas cuando ejecutas `pip install requests`. Estas manejan la codificación (`charset_normalizer`), nombres de dominio internacionalizados (`idna`), transporte HTTP (`urllib3`) y certificados SSL (`certifi`).
- **`test_requirements`**: Solo se instalan si ejecutas tests (por ejemplo, mediante `pip install -e '.[tests]'`). Incluye herramientas de testing como variantes de `pytest` para simulación HTTP, cobertura y testing paralelo. `PySocks` es para soporte de proxy SOCKS en los tests.

### 4. Carga Dinámica de Metadatos
```python
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
```
- **Diccionario `about`**: Lee metadatos desde `src/requests/__version__.py` (por ejemplo, `__title__`, `__version__`, `__description__`, etc.) usando `exec()`. Esto mantiene la información de la versión centralizada—se actualiza una vez, y `setup.py` la extrae.
- **`readme`**: Carga todo el archivo `README.md` como una cadena para la descripción larga del paquete en PyPI.

### 5. La Llamada Principal a `setup()`
Este es el corazón del archivo. Configura el paquete para construcción/instalación:
```python
setup(
    name=about["__title__"],  # ej., "requests"
    version=about["__version__"],  # ej., "2.32.3"
    description=about["__description__"],  # Resumen corto
    long_description=readme,  # README completo
    long_description_content_type="text/markdown",  # Se renderiza como Markdown en PyPI
    author=about["__author__"],  # ej., "Kenneth Reitz"
    author_email=about["__author_email__"],
    url=about["__url__"],  # ej., repositorio GitHub
    packages=["requests"],  # Instala el paquete 'requests'
    package_data={"": ["LICENSE", "NOTICE"]},  # Incluye archivos que no son de Python
    package_dir={"": "src"},  # El código fuente está en 'src/'
    include_package_data=True,  # Incluye todos los archivos de datos
    python_requires=">=3.9",  # Refleja la verificación de versión
    install_requires=requires,  # De la sección anterior
    license=about["__license__"],  # ej., "Apache 2.0"
    zip_safe=False,  # Permite editar archivos instalados (común para librerías)
    classifiers=[  # Categorías de PyPI para descubribilidad
        "Development Status :: 5 - Production/Stable",
        # ... (lista completa incluye versiones de Python, SO, temas)
    ],
    tests_require=test_requirements,  # Para `pip install -e '.[tests]'`
    extras_require={  # Dependencias opcionales
        "security": [],  # Vacío—quizás para uso futuro
        "socks": ["PySocks>=1.5.6, !=1.5.7"],  # Soporte para proxy SOCKS
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],  # Fallback de codificación heredado
    },
    project_urls={  # Enlaces en la página de PyPI
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
```
- **Argumentos Clave**:
  - **Nombre/Versión/Descripción**: Extraídos de `__version__.py` para un mantenimiento fácil.
  - **Packages/Package Dir**: Indica a setuptools que el paquete está bajo `src/requests/` y que debe instalarse como `import requests`.
  - **Classifiers**: Una lista de cadenas que categorizan el paquete (por ejemplo, estable, Python 3.9+, licencia Apache, tema web/HTTP). Esto ayuda a los usuarios a encontrarlo en PyPI.
  - **Extras Require**: Permite a los usuarios instalar características opcionales, como `pip install requests[socks]` para soporte de proxy.
  - **Project URLs**: Añade enlaces clickeables a la documentación y al código fuente en la página de PyPI.

### Cómo Funciona en la Práctica
- **Instalación**: `pip install .` (desde el repositorio) o `pip install requests` (desde PyPI) ejecuta esto para copiar archivos, instalar dependencias y configurar el paquete.
- **Construcción**: `python setup.py sdist` crea archivos distribuibles.
- **¿Por Qué Esta Estructura?**: Es un "src layout" (código en `src/`), que es una práctica moderna recomendada para evitar importaciones accidentales durante el desarrollo. El archivo es autónomo pero delega detalles en otros archivos como `__version__.py`.

Este setup.py es del repositorio oficial de Requests y no ha cambiado mucho a lo largo de las versiones—está probado en batalla para garantizar su fiabilidad.

### Referencias
- [Documentación de Requests](https://requests.readthedocs.io/en/latest/)
- [Repositorio GitHub de Requests](https://github.com/psf/requests)
- [Guía de Usuario de Empaquetado de Python](https://packaging.python.org/en/latest/tutorials/packaging-projects/)