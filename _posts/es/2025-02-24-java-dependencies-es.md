---
audio: false
lang: es
layout: post
title: Análisis de Dependencias de Java
translated: true
---

A continuación se presenta un script de Python que escanea todos los archivos `.java` en un proyecto, analiza sus dependencias en función de las declaraciones de importación y genera un gráfico de dependencias en formato DOT como "texto de dependencia". Este script se centra en las dependencias internas entre clases dentro del proyecto, proporcionando una representación clara que puede visualizarse utilizando herramientas como Graphviz.

### Descripción del Script
El script:
1. **Escanea el directorio del proyecto** de manera recursiva para encontrar todos los archivos `.java`.
2. **Analiza las dependencias** extrayendo declaraciones de paquete e importaciones de cada archivo `.java`.
3. **Genera un texto de dependencia** en formato DOT, mostrando aristas dirigidas entre clases donde una clase importa a otra dentro del proyecto.

Aquí está el script completo:

```python
import os
import sys
import re
from collections import defaultdict

def get_package(file_path):
    """
    Extrae el nombre del paquete de un archivo .java.

    Args:
        file_path (str): Ruta al archivo .java.

    Returns:
        str: El nombre del paquete, o None si no se encuentra.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*package\s+([\w.]+);', line)
                if match:
                    return match.group(1)
    except Exception as e:
        print(f"Advertencia: No se pudo leer {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    Extrae importaciones de clases específicas de un archivo .java, excluyendo importaciones genéricas.

    Args:
        file_path (str): Ruta al archivo .java.

    Returns:
        list: Lista de nombres de clases importadas completamente calificadas.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # Excluir importaciones genéricas (por ejemplo, import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Advertencia: No se pudo leer {file_path}: {e}")
    return imports

if __name__ == '__main__':
    # Verificar argumento de línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python script.py <directorio_raíz>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_classes = set()

    # Primera pasada: Recopilar todos los nombres de clases completamente calificadas en el proyecto
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Almacenar dependencias: clase -> conjunto de clases de las que depende
    dependencies = defaultdict(set)

    # Segunda pasada: Analizar dependencias basadas en importaciones específicas
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # Solo incluir dependencias en clases dentro del proyecto
                        # Excluir auto-dependencias
                        if imp in all_classes and imp != full_class_name:
                            dependencies[full_class_name].add(imp)

    # Salida del gráfico de dependencias en formato DOT
    print('digraph G {')
    for class_name in sorted(dependencies):
        for dep in sorted(dependencies[class_name]):
            print(f'  "{class_name}" -> "{dep}";')
    print('}')
```

### Cómo Funciona
#### 1. **Entrada de Línea de Comandos**
- El script espera un solo argumento: el directorio raíz del proyecto Java.
- Ejemplo de uso: `python script.py /ruta/al/proyecto`
- Si no se proporciona ningún argumento, imprime las instrucciones de uso y sale.

#### 2. **Encontrar Archivos `.java`**
- Usa `os.walk()` para recorrer recursivamente el directorio especificado e identificar todos los archivos que terminan con `.java`.

#### 3. **Extraer Información de Clases**
- **Extracción de Paquete**: La función `get_package` lee cada archivo `.java` y usa una expresión regular (`^\s*package\s+([\w.]+);`)` para encontrar la declaración de paquete (por ejemplo, `package com.mycompany.myproject;`).
  - Devuelve `None` si no se encuentra ningún paquete o si el archivo no se puede leer.
- **Nombre de Clase**: Asume que el nombre de la clase coincide con el nombre del archivo (por ejemplo, `MyClass.java` define `MyClass`).
- **Nombre Completamente Calificado**: Combina el paquete y el nombre de la clase (por ejemplo, `com.mycompany.myproject.MyClass`).

#### 4. **Recopilar Todas las Clases**
- En la primera pasada, construye un conjunto de todos los nombres de clases completamente calificadas en el proyecto para una búsqueda rápida más tarde.

#### 5. **Analizar Dependencias**
- **Extracción de Importaciones**: La función `get_specific_imports` extrae declaraciones de importación usando una expresión regular (`^\s*import\s+([\w.]+);`), excluyendo importaciones genéricas (por ejemplo, `import java.util.*;`).
  - Ejemplo: De `import com.mycompany.myproject.utils.Helper;`, extrae `com.mycompany.myproject.utils.Helper`.
- **Mapeo de Dependencias**: Para cada archivo `.java`:
  - Obtiene su nombre de clase completamente calificado.
  - Verifica sus importaciones específicas.
  - Si una clase importada está en el conjunto de clases del proyecto y no es la clase misma, agrega una dependencia.

#### 6. **Generar Texto de Dependencia**
- Genera un gráfico dirigido en formato DOT:
  - Comienza con `digraph G {`.
  - Para cada clase con dependencias, imprime aristas como `"ClassA" -> "ClassB";`.
  - Termina con `}`.
- Las clases y dependencias se ordenan para una salida consistente.
- Ejemplo de salida:
  ```
  digraph G {
    "com.mycompany.myproject.ClassA" -> "com.mycompany.myproject.utils.Helper";
    "com.mycompany.myproject.ClassB" -> "com.mycompany.myproject.ClassA";
  }
  ```

### Ejemplo de Uso
1. Guarda el script como `analyze_deps.py`.
2. Ejecútalo:
   ```bash
   python analyze_deps.py /ruta/al/proyecto/java
   ```
3. Redirige la salida a un archivo:
   ```bash
   python analyze_deps.py /ruta/al/proyecto/java > dependencias.dot
   ```
4. Visualiza con Graphviz:
   ```bash
   dot -Tpng dependencias.dot -o dependencias.png
   ```
   Esto genera una imagen PNG mostrando el gráfico de dependencias.

### Suposiciones y Limitaciones
- **Una Clase Pública por Archivo**: Asume que cada archivo `.java` contiene una clase pública nombrada después del archivo, según la convención de Java.
- **Dependencias Basadas en Importaciones**: Solo considera dependencias indicadas por declaraciones de importación específicas (por ejemplo, `import com.example.SomeClass;`), ignorando importaciones genéricas (`import com.example.*;`) y referencias dentro del mismo paquete (que no requieren importaciones).
- **Enfoque Interno**: Solo rastrea dependencias entre clases dentro del proyecto, ignorando bibliotecas externas.
- **Análisis Básico**: Usa expresiones regulares por simplicidad, lo que puede perder casos extremos (por ejemplo, importaciones dentro de comentarios). Un analizador de Java completo sería más robusto pero complejo.

### Personalización
- **Formato de Salida**: Modifica las declaraciones de impresión para cambiar el formato del texto de dependencia (por ejemplo, una lista simple en lugar de DOT).
- **Manejo de Errores**: Mejorado con bloques try-except para omitir archivos no legibles de manera elegante.
- **Alcance**: Podría extenderse para incluir dependencias externas o dependencias dentro del mismo paquete con un análisis de código más profundo.

Este script proporciona un punto de partida práctico para el análisis de dependencias, adecuado para entender la estructura de un proyecto Java a través de sus relaciones internas de clases.