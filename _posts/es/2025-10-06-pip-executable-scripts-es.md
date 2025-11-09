---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Agregar Scripts Ejecutables a Paquetes Pip
translated: true
type: note
---

### Crear scripts ejecutables en un paquete Pip de Python

Para incluir scripts ejecutivos (es decir, herramientas de línea de comandos) en un paquete de Python que se pueda instalar mediante `pip`, defines **puntos de entrada** en el archivo de configuración de tu paquete. Esto permite a los usuarios ejecutar tus scripts directamente después de la instalación (por ejemplo, `my-script` desde la terminal).

Usaremos un ejemplo simple: un paquete llamado `mytools` con un script `greet` que imprime un saludo.

#### Paso 1: Configurar la estructura de tu paquete
Crea una estructura de directorios como esta:

```
mytools/
├── pyproject.toml          # Archivo de configuración moderno (recomendado sobre setup.py)
├── README.md
└── src/
    └── mytools/
        ├── __init__.py     # Lo convierte en un paquete
        └── greet.py        # La lógica de tu script
```

En `src/mytools/__init__.py` (puede estar vacío o con información de versión):
```python
__version__ = "0.1.0"
```

En `src/mytools/greet.py` (la función que llamará tu script):
```python
import sys

def main():
    name = sys.argv[1] if len(sys.argv) > 1 else "World"
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
```

#### Paso 2: Configurar los puntos de entrada en `pyproject.toml`
Usa la sección `[project.scripts]` para definir scripts de consola. Esto le indica a pip que cree envoltorios ejecutables.

```toml
[build-system]
requires = ["hatchling"]  # O "setuptools", "flit", etc.
build-backend = "hatchling.build"

[project]
name = "mytools"
version = "0.1.0"
description = "Un paquete de herramientas simple"
readme = "README.md"
requires-python = ">=3.8"
dependencies = []  # Añade tus dependencias aquí, por ejemplo, "requests"

[project.scripts]
greet = "mytools.greet:main"  # Formato: nombre_script = paquete.modulo:función
```

- `greet` es el comando que los usuarios ejecutarán (por ejemplo, `greet Alice`).
- `mytools.greet:main` apunta a la función `main()` en `greet.py`.

Si prefieres el antiguo `setup.py` (todavía funciona pero menos recomendado):
```python
from setuptools import setup, find_packages

setup(
    name="mytools",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "greet = mytools.greet:main"
        ]
    },
    # ... otros campos como description, install_requires
)
```

#### Paso 3: Construir e instalar el paquete
1. Instala las herramientas de construcción: `pip install build twine` (o `hatchling` si usas ese backend).

2. Construye el paquete:
   ```
   python -m build
   ```
   Esto crea `dist/` con archivos `.tar.gz` y `.whl`.

3. Instala localmente para probar:
   ```
   pip install -e .  # Modo editable (los cambios se reflejan inmediatamente)
   ```
   O para una instalación limpia: `pip install dist/mytools-0.1.0-py3-none-any.whl`.

4. Prueba: Ejecuta `greet Alice` en tu terminal. Debería mostrar "Hello, Alice!".

#### Paso 4: Distribuir (Opcional)
- Sube a PyPI: `twine upload dist/*` (requiere cuenta de PyPI).
- Los usuarios pueden entonces hacer `pip install mytools` y ejecutar `greet`.

#### Consejos
- **Múltiples scripts**: Añade más líneas a `[project.scripts]`, por ejemplo, `another-script = mytools.other:main`.
- **Argumentos**: Usa `argparse` en tu función `main()` para un mejor manejo de CLI.
- **Dependencias**: Lista las dependencias en `[project.dependencies]` (por ejemplo, `click` para frameworks CLI).
- **Entorno virtual**: Siempre usa uno (`python -m venv env; source env/bin/activate`) para evitar conflictos.
- **¿Errores?** Revisa `pip install --verbose` para más detalles. Asegúrate de que tu función no tome argumentos (o maneje `sys.argv`).

Para configuraciones más avanzadas (por ejemplo, con Poetry o Flit), consulta la documentación oficial.

#### Referencias
- [Python Packaging User Guide: Entry Points](https://packaging.python.org/en/latest/guides/writing-entry-points/)
- [PyPI: Building and Publishing](https://packaging.python.org/en/latest/tutorials/packaging-projects/)