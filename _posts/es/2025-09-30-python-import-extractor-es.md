---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Extractor de Importación de Paquetes Python
translated: true
type: note
---

### Script de Python para Extraer Todos los Paquetes Importados

Este script recorre un directorio especificado y sus subdirectorios, encuentra todos los archivos Python (`.py`), analiza sus sentencias de importación utilizando el módulo `ast` de Python (para un análisis seguro y consciente de la sintaxis), y acumula todos los nombres únicos de módulos base (por ejemplo, `os` de `import os`, o `collections` de `from collections import defaultdict`). Ignora los módulos integrados y se centra en módulos externos.

Guarda esto como un archivo `.py` (por ejemplo, `extract_imports.py`) y ejecútalo con una ruta de directorio como argumento, como `python extract_imports.py /ruta/al/directorio`.

```python
import os
import ast
import sys

def extract_imports_from_file(file_path):
    """
    Parsea un archivo Python y extrae los nombres de los módulos importados.
    Maneja los estilos 'import mod' y 'from mod import item'.
    """
    modules = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = ast.parse(f.read(), filename=file_path)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    modules.add(alias.name.split('.')[0])  # Obtener el módulo base (ej., 'import os.path' -> 'os')
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split('.')[0])  # Obtener el módulo base de 'from mod.sub import ...'
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
    
    return modules

def get_all_imported_modules(directory):
    """
    Recorre el directorio y subdirectorios, recopilando todos los módulos importados únicos.
    """
    all_modules = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                modules = extract_imports_from_file(file_path)
                all_modules.update(modules)
    
    # Excluir builtins comunes (opcional, ya que rara vez son paquetes externos)
    excluded = {'sys', 'os', 're', 'math', 'random', 'json', 'time', 'datetime', 'collections', 'itertools', 'functools'}
    all_modules -= excluded
    
    return sorted(all_modules)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_imports.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    modules = get_all_imported_modules(directory)
    print("All unique imported packages:")
    for mod in modules:
        print(mod)
```

### Cómo Funciona
- **Recorrido de Directorios**: Utiliza `os.walk` para visitar recursivamente todos los subdirectorios y archivos.
- **Filtrado de Archivos**: Solo procesa archivos `.py`.
- **Análisis de Importaciones**: Emplea `ast` para analizar de forma segura el código fuente e identificar nodos `Import` e `ImportFrom`. Divide en `.` para capturar el módulo de nivel superior (por ejemplo, `numpy` de `import numpy.linalg`).
- **Acumulación**: Recopila módulos en un conjunto para garantizar unicidad, luego los ordena y los imprime.
- **Casos Extremos**: Omite los módulos integrados (puedes personalizar el conjunto `excluded`), maneja errores de sintaxis de forma elegante y admite archivos Unicode.
- **Salida**: Una lista ordenada de nombres de paquetes únicos. Si se ejecuta en el directorio de tu propio proyecto, listará paquetes como `requests`, `pandas`, etc., que necesitarías instalar.

Este enfoque es eficiente para el análisis de bases de código y evita ejecutar código potencialmente inseguro. Si necesitas refinamientos (por ejemplo, manejar importaciones relativas de manera diferente o generar un requirements.txt), ¡proporciona más detalles!