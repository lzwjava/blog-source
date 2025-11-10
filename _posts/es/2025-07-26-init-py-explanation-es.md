---
audio: false
generated: true
lang: es
layout: post
title: Por Qué Python Necesita `__init__.py`
translated: true
type: note
---

### Corrigiendo el Error Tipográfico
Parece que te referías a `__init__.py` (donde "init" es la abreviatura de "initialization" o inicialización) en lugar de `__int__.py`. Si no es así, ¡no dudes en aclararlo! Asumiendo que es `__init__.py`, aquí tienes la explicación.

### Por Qué Python Necesita `__init__.py` en un Directorio
En Python, un directorio no se trata automáticamente como un módulo o paquete solo porque contiene archivos Python. Para organizar el código en paquetes reutilizables (que esencialmente son directorios de módulos relacionados), Python requiere un archivo `__init__.py` en ese directorio. He aquí el porqué:

- **Marcar el Directorio como un Paquete**: La presencia de `__init__.py` le indica a Python que el directorio debe considerarse un paquete. Esto te permite importar módulos desde él usando notación de puntos, como `import mipaquete.mimodulo`. Sin él (en casos estándar), Python trataría el directorio como una carpeta normal y no permitiría importaciones desde él.

- **Prevenir Conflictos de Nombres**: Evita que se oculten módulos por accidente. Por ejemplo, si tienes un directorio llamado `string` (un nombre común), sin `__init__.py`, podría ocultar involuntariamente el módulo incorporado `string` de Python en la ruta de importación.

- **Inicialización y Personalización**: El archivo puede estar vacío (lo cual es común para paquetes simples), pero también puede contener código que se ejecuta cuando se importa el paquete. Esto es útil para tareas de configuración, como importar submódulos automáticamente. Adicionalmente, puedes definir una variable especial llamada `__all__` en `__init__.py` para controlar qué se importa cuando alguien hace `from mipaquete import *` (por ejemplo, `__all__ = ['modulo1', 'modulo2']`).

### Contexto Histórico y Específico de Versión
- Este requisito ha sido parte de Python desde sus primeros días para mantener el sistema de módulos explícito y organizado.
- A partir de Python 3.3, se introdujeron los "paquetes de espacio de nombres" (namespace packages), que no requieren `__init__.py`. Estos permiten que los paquetes se dividan en múltiples directorios (por ejemplo, para fines de distribución) sin el archivo, utilizando herramientas como `pkgutil` o `importlib`. Sin embargo, esto se considera una característica avanzada, y para la mayoría de los casos de uso cotidianos, `__init__.py` sigue siendo recomendado y ampliamente utilizado para paquetes regulares.

Si estás trabajando con Python 3.3 o superior, puedes experimentar con paquetes de espacio de nombres, pero ceñirse a `__init__.py` es más simple y directo para principiantes.

[Tutorial de Python: Módulos](https://docs.python.org/3/tutorial/modules.html#packages)