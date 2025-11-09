---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Empaquetado de Python PEP 517
translated: true
type: note
---

PEP 517, aceptada en 2016, define una interfaz estandarizada para construir paquetes Python que desacopla el backend de compilación (la lógica para crear distribuciones) del frontend (herramientas como pip que orquestan el proceso). Esto permite a los desarrolladores usar herramientas de compilación modernas sin quedar atrapados en sistemas heredados como `setup.py` de setuptools. Combinada con PEP 518 (que especifica las dependencias de compilación), permite compilaciones confiables y aisladas desde árboles de código fuente o distribuciones de origen (sdists). En 2025, PEP 517 es la base para el empaquetado moderno de Python, soportada por pip (desde la versión 10 para PEP 518 y 19 para PEP 517 completa) y herramientas como Poetry, Flit y PDM.

Esta guía cubre la motivación, conceptos clave, especificación, flujos de trabajo, implementación y mejores prácticas.

## Motivación y Antecedentes

El empaquetado de Python evolucionó de `distutils` (introducido en Python 1.6, 2000) a `setuptools` (2004), que añadió gestión de dependencias pero introdujo problemas:
- **Imperativo y Frágil**: Las compilaciones dependían de ejecutar `python setup.py`, un script arbitrario que podía fallar debido a suposiciones del entorno (por ejemplo, falta de Cython para extensiones).
- **Sin Dependencias de Compilación**: Las herramientas necesarias para compilar (por ejemplo, compiladores, Cython) no se declaraban, lo que llevaba a instalaciones manuales y conflictos de versiones.
- **Acoplamiento Estrecho**: Pip invocaba `setup.py` de forma fija, bloqueando sistemas de compilación alternativos como Flit o Bento.
- **Contaminación del Entorno Anfitrión**: Las compilaciones usaban el entorno global de Python del usuario, arriesgando efectos secundarios.

Estos problemas frenaron la innovación y causaron errores durante las instalaciones desde código fuente (por ejemplo, desde Git). PEP 517 resuelve esto estandarizando una interfaz mínima: los frontends llaman a hooks del backend en entornos aislados. Las wheels (binarios precompilados, introducidos en 2014) simplifican la distribución—los backends solo necesitan producir wheels/sdists compatibles. PEP 518 complementa declarando los requisitos de compilación en `pyproject.toml`, permitiendo el aislamiento.

El resultado: Un ecosistema declarativo y extensible donde `setup.py` es opcional, y herramientas como pip pueden compilar cualquier proyecto compatible sin recurrir a métodos heredados.

## Conceptos Clave

### Árboles de Código Fuente y Distribuciones
- **Árbol de Código Fuente**: Un directorio (por ejemplo, una descarga de VCS) que contiene el código del paquete y `pyproject.toml`. Herramientas como `pip install .` compilan desde él.
- **Distribución de Origen (Sdist)**: Un archivo comprimido tar.gz (`.tar.gz`) como `package-1.0.tar.gz`, que se descomprime en un directorio `{nombre}-{versión}` con `pyproject.toml` y metadatos (PKG-INFO). Se usa para lanzamientos y empaquetado descendente (por ejemplo, Debian).
- **Wheel**: Una distribución binaria `.whl`—precompilada, específica de la plataforma y que se puede instalar sin compilación. PEP 517 exige wheels para la reproducibilidad.

Las sdists heredadas (pre-PEP 517) se descomprimen en árboles ejecutables pero ahora deben incluir `pyproject.toml` para ser compatibles.

### pyproject.toml
Este archivo TOML centraliza la configuración. La sección `[build-system]` (de PEP 518/517) especifica:
- `requires`: Lista de dependencias PEP 508 para la compilación (por ejemplo, `["setuptools>=40.8.0", "wheel"]`).
- `build-backend`: Punto de entrada al backend (por ejemplo, `"setuptools.build_meta"` o `"poetry.masonry.api"`).
- `backend-path` (opcional): Rutas internas añadidas a `sys.path` para backends auto-alojados (por ejemplo, `["src/backend"]`).

Ejemplo de configuración mínima:
```
[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"
```

Los requisitos forman un DAG (sin ciclos; los frontends los detectan y fallan). Otras secciones como `[project]` (PEP 621) o `[tool.poetry]` contienen metadatos/dependencias.

### Backends y Frontends de Compilación
- **Backend**: Implementa la lógica de compilación mediante hooks (funciones invocables). Se ejecuta en un subproceso para aislamiento.
- **Frontend**: Orquesta (por ejemplo, pip). Configura el aislamiento, instala los requisitos, llama a los hooks.
- **Desacoplamiento**: Los frontends invocan hooks estandarizados, no `setup.py`. Esto soporta diversos backends sin cambios en pip.

Los hooks usan `config_settings` (dict para banderas, por ejemplo, `{"--debug": true}`) y pueden enviar salida a stdout/stderr (UTF-8).

## La Especificación

### Detalles de [build-system]
- `requires`: Cadenas PEP 508 (por ejemplo, `">=1.0; sys_platform == 'win32'"`).
- `build-backend`: `módulo:objeto` (por ejemplo, `flit_core.buildapi` importa `flit_core; backend = flit_core.buildapi`).
- Sin contaminación de sys.path—los backends importan mediante aislamiento.

### Hooks
Los backends exponen estos como atributos:

**Obligatorios:**
- `build_wheel(directorio_wheel, config_settings=None, directorio_metadatos=None) -> str`: Construye una wheel en `directorio_wheel`, devuelve el nombre base (por ejemplo, `"myproj-1.0-py3-none-any.whl"`). Usa metadatos previos si se proporcionan. Maneja fuentes de solo lectura mediante temporales.
- `build_sdist(directorio_sdist, config_settings=None) -> str`: Construye una sdist en `directorio_sdist` (formato pax, UTF-8). Lanza `UnsupportedOperation` si es imposible (por ejemplo, sin VCS).

**Opcionales (valores por defecto `[]` o alternativos):**
- `get_requires_for_build_wheel(config_settings=None) -> list[str]`: Dependencias extra para wheel (por ejemplo, `["cython"]`).
- `prepare_metadata_for_build_wheel(directorio_metadatos, config_settings=None) -> str`: Escribe metadatos `{pkg}-{ver}.dist-info` (según especificación de wheel, sin RECORD). Devuelve el nombre base; los frontends extraen de la wheel si falta.
- `get_requires_for_build_sdist(config_settings=None) -> list[str]`: Dependencias extra para sdist.

Los hooks lanzan excepciones para errores. Los frontends los llaman en entornos aislados (por ejemplo, venv con solo stdlib + requisitos).

### Entorno de Compilación
- Venv aislado: Bootstrap para `get_requires_*`, completo para compilaciones.
- Herramientas CLI (por ejemplo, `flit`) en PATH.
- Sin stdin; subprocesos por hook.

## Cómo Funciona el Proceso de Compilación

### Flujo de Trabajo Paso a Paso
Para `pip install .` (árbol de código fuente) o instalación desde sdist:

1. **Descubrimiento**: El frontend lee `pyproject.toml`.
2. **Configuración del Aislamiento**: Crea un venv; instala `requires`.
3. **Consulta de Requisitos**: Llama `get_requires_for_build_wheel` (instala extras).
4. **Preparación de Metadatos**: Llama `prepare_metadata_for_build_wheel` (o construye la wheel y extrae).
5. **Compilación de la Wheel**: Llama `build_wheel` en entorno aislado; instala la wheel resultante.
6. **Alternativas**: Si la sdist no es soportada, construye la wheel; si no hay hooks, usa `setup.py` heredado.

Para sdists: Desempaqueta, trata como árbol de código fuente. Flujo de trabajo del desarrollador (por ejemplo, `pip wheel .`):
1. Aísla el entorno.
2. Llama a los hooks del backend para wheel/sdist.

### Aislamiento de Compilación (PEP 518)
Crea un venv temporal para compilaciones, evitando la contaminación del anfitrión. La opción `--no-build-isolation` de pip lo desactiva (usar con precaución). Herramientas como tox usan aislamiento por defecto.

Antiguo vs. Nuevo:
- **Antiguo**: `python setup.py install` en el entorno anfitrión—riesgo de conflictos.
- **Nuevo**: Hooks aislados—reproducible, seguro.

## Implementando un Backend de Compilación

Para crear uno:
1. Define un módulo con hooks (por ejemplo, `mybackend.py`).
2. Apunta `build-backend` a él.

Ejemplo mínimo (paquete Python puro):
```python
# mybackend.py
from zipfile import ZipFile
import os
from pathlib import Path

def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    # Copia el código fuente al directorio de la wheel, lo comprime como .whl
    dist = Path(wheel_directory) / "myproj-1.0-py3-none-any.whl"
    with ZipFile(dist, 'w') as z:
        for src in Path('.').rglob('*'):
            z.write(src, src.relative_to('.'))
    return str(dist.relative_to(wheel_directory))

# Hooks opcionales
def get_requires_for_build_wheel(config_settings=None):
    return []

def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    # Escribe METADATA, etc.
    return "myproj-1.0.dist-info"
```

En `pyproject.toml`:
```
[build-system]
requires = []
build-backend = "mybackend:build_wheel"  # En realidad apunta al objeto del módulo
```

Usa bibliotecas como `pyproject-hooks` para código repetitivo. Para extensiones, integra compiladores C mediante `config_settings`.

## Usando PEP 517 con Herramientas

- **pip**: Detecta automáticamente `pyproject.toml`; usa `--use-pep517` (por defecto desde 19.1). Para editable: `pip install -e .` llama a los hooks.
- **Poetry**: Herramienta declarativa. Genera:
  ```
  [build-system]
  requires = ["poetry-core>=1.0.0"]
  build-backend = "poetry.core.masonry.api"
  ```
  Instala mediante `poetry build`; compatible con pip.
- **Flit**: Simple para Python puro. Usa:
  ```
  [build-system]
  requires = ["flit_core >=3.2,<4"]
  build-backend = "flit_core.buildapi"
  ```
  `flit publish` compila/sube.
- **Setuptools**: Puente para legado:
  ```
  [build-system]
  requires = ["setuptools>=40.8.0", "wheel"]
  build-backend = "setuptools.build_meta"
  ```
  Soporta `setup.cfg` para metadatos declarativos.

Migrar legado: Añadir `[build-system]`; eliminar llamadas a `setup.py`.

## Manejo de Errores y Mejores Prácticas

- **Errores**: Los hooks lanzan excepciones (por ejemplo, `ValueError` para configuración inválida). Ciclos: El frontend falla con un mensaje. Sdist no soportada: Recurrir a la wheel.
- **Mejores Prácticas**:
  - Preferir declarativo (`setup.cfg` o `[project]`).
  - Declarar dependencias de compilación exactas (por ejemplo, `cython==0.29`).
  - Probar aislamiento: `pip wheel . --no-build-isolation` para depuración.
  - Para backends internos: Usar `backend-path`; evitar ciclos.
  - Seguridad: Hooks en subprocesos; sin código arbitrario.
  - Compatibilidad: Incluir `setup.py` para herramientas antiguas.

En 2025, setuptools domina (según encuestas), pero la adopción de Poetry/Flit crece por su simplicidad.

## Referencias
- [PEP 517 – A build-system independent format for source trees](https://peps.python.org/pep-0517/)
- [PEP 517 and 518 in Plain English](https://chadsmith-software.medium.com/pep-517-and-518-in-plain-english-47208ca8b7a6)
- [Python packaging - Past, Present, Future](https://bernat.tech/posts/pep-517-518/)
- [What is PEP 517/518 compatibility?](https://pydevtools.com/handbook/explanation/what-is-pep-517/)
- [Modern pip build process (–use-pep517)](https://fromkk.com/posts/modern-pip-build-process-use-pep517/)
- [What is a build backend?](https://pydevtools.com/handbook/explanation/what-is-a-build-backend/)