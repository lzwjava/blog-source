---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Gestión de Dependencias de Python con Poetry
translated: true
type: note
---

### ¿Qué es Poetry?

Poetry es una herramienta para la gestión de dependencias y empaquetado en Python. Te permite declarar las librerías de las que depende tu proyecto y se encarga de instalarlas, actualizarlas y resolverlas automáticamente, garantizando entornos reproducibles.

### Propósito Principal
Poetry simplifica los flujos de trabajo de los proyectos de Python gestionando las dependencias a través de un único archivo de configuración (`pyproject.toml`), creando un archivo de bloqueo para instalaciones consistentes en diferentes máquinas y soportando la construcción de proyectos para su distribución (por ejemplo, a PyPI). Está diseñado para reemplazar herramientas fragmentadas como `pip`, `pipenv` y `setuptools` con un enfoque unificado y fácil de usar.

### Características Principales
- **Resolución de Dependencias**: Instala y actualiza dependencias automáticamente, resolviendo conflictos de forma inteligente.
- **Archivo de Bloqueo**: Genera `poetry.lock` para fijar versiones exactas y lograr builds repetibles.
- **Entornos Virtuales**: Crea entornos aislados por proyecto para evitar la contaminación global.
- **Empaquetado**: Construye wheels o sdists para una fácil distribución.
- **Soporte Multiplataforma**: Funciona en Linux, macOS y Windows.
- **Integración con la Shell**: Autocompletado con tabulador para Bash, Fish y Zsh.
- **Compatible con Python 3.9+**: Requiere versiones modernas de Python.

### Instalación
Instala Poetry en un entorno aislado usando `pipx` (recomendado para acceso global sin conflictos):

1. Instala `pipx` si es necesario (a través del gestor de paquetes de tu sistema operativo o `python -m pip install --user pipx`).
2. Ejecuta: `pipx install poetry`.

Para actualizar: `pipx upgrade poetry`.  
Para desinstalar: `pipx uninstall poetry`.

Habilita el autocompletado para la shell (por ejemplo, para Bash: `poetry completions bash >> ~/.bash_completion`).

### Uso Básico
Inicializar un nuevo proyecto: `poetry init`.  
Añadir una dependencia: `poetry add requests`.  
Instalar desde el archivo de bloqueo: `poetry install`.  
Ejecutar scripts: `poetry run python script.py`.  
Construir el paquete: `poetry build`.

Para todos los comandos, consulta la documentación.

[Documentación de Poetry](https://python-poetry.org/docs/)