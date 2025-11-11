---
audio: false
generated: true
lang: es
layout: post
title: Analizar Dependencias de Java
translated: true
type: note
---

Para abordar tu consulta, modificaré el script Python proporcionado para generar un gráfico de dependencias para clases Java, donde las dependencias se agrupan por un "nivel" especificado de la jerarquía del paquete. Por ejemplo, si `level=1`, los paquetes se agrupan en el nivel superior (ej. "org"), y si `level=2`, se agrupan en el segundo nivel (ej. "org.springframework"). Esto significa que antes de analizar las dependencias, acumulamos las clases en grupos basados en las primeras `level` partes de sus nombres de paquete, y el gráfico mostrará las dependencias entre estos grupos en lugar de entre clases individuales.

A continuación se muestra el script modificado, seguido de una explicación de los cambios y cómo cumple con tus requisitos.

### Script Modificado

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
        print(f"Warning: Could not read {file_path}: {e}")
    return None

def get_specific_imports(file_path):
    """
    Extrae importaciones específicas de clases de un archivo .java, excluyendo importaciones comodín.

    Args:
        file_path (str): Ruta al archivo .java.

    Returns:
        list: Lista de nombres de clase importados completamente calificados.
    """
    imports = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'^\s*import\s+([\w.]+);', line)
                if match:
                    imp = match.group(1)
                    # Excluir importaciones comodín (ej., import java.util.*;)
                    if not imp.endswith('.*'):
                        imports.append(imp)
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
    return imports

def get_package_group(full_class_name, level):
    """
    Obtiene el grupo del paquete basado en las primeras 'level' partes del nombre del paquete.

    Args:
        full_class_name (str): Nombre de clase completamente calificado (ej., "org.springframework.boot.App").
        level (int): Número de niveles de paquete a incluir (ej., 1 para "org", 2 para "org.springframework").

    Returns:
        str: El grupo del paquete (ej., "org" o "org.springframework").
    """
    package = '.'.join(full_class_name.split('.')[:-1])  # Extrae el paquete, excluyendo el nombre de la clase
    parts = package.split('.')
    if len(parts) <= level:
        return package  # Usa el paquete completo si tiene menos o igual partes que el nivel
    else:
        return '.'.join(parts[:level])  # Usa las primeras 'level' partes

if __name__ == '__main__':
    # Verificar los argumentos de la línea de comandos: root_directory y level
    if len(sys.argv) != 3:
        print("Usage: python script.py <root_directory> <level>")
        sys.exit(1)

    root_dir = sys.argv[1]
    try:
        level = int(sys.argv[2])
        if level < 1:
            raise ValueError
    except ValueError:
        print("Error: level must be a positive integer")
        sys.exit(1)

    all_classes = set()

    # Primer paso: Recopilar todos los nombres de clase completamente calificados en el proyecto
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    all_classes.add(full_class_name)

    # Almacenar dependencias entre grupos de paquetes
    group_dependencies = set()

    # Segundo paso: Analizar dependencias basadas en grupos de paquetes
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.java'):
                file_path = os.path.join(root, file)
                package = get_package(file_path)
                if package:
                    class_name = file.replace('.java', '')
                    full_class_name = f"{package}.{class_name}"
                    importer_group = get_package_group(full_class_name, level)
                    imports = get_specific_imports(file_path)
                    for imp in imports:
                        # Solo incluir dependencias en clases dentro del proyecto
                        # Excluir auto-dependencias
                        if imp in all_classes and imp != full_class_name:
                            imported_group = get_package_group(imp, level)
                            if imported_group != importer_group:
                                group_dependencies.add((importer_group, imported_group))

    # Salida del gráfico de dependencias en formato DOT
    print('digraph G {')
    for from_group, to_group in sorted(group_dependencies):
        print(f'  "{from_group}" -> "{to_group}";')
    print('}')
```

### Explicación de los Cambios

1. **Argumentos de Línea de Comandos**:
   - **Original**: `python script.py <root_directory>`
   - **Modificado**: `python script.py <root_directory> <level>`
   - Se añadió soporte para un segundo argumento, `level`, que especifica el nivel de la jerarquía del paquete. El script verifica que se proporcionen exactamente dos argumentos y que `level` sea un entero positivo.

2. **Nueva Función: `get_package_group`**:
   - Se añadió una función para calcular el grupo del paquete para una clase basado en el `level` especificado.
   - Para un nombre de clase completamente calificado (ej., "org.springframework.boot.App"), extrae el paquete ("org.springframework.boot"), lo divide en partes ("org", "springframework", "boot"), y toma las primeras `level` partes:
     - Si `level=1`: Retorna "org".
     - Si `level=2`: Retorna "org.springframework".
     - Si el paquete tiene menos partes que `level` (ej., "com.example" con `level=3`), retorna el paquete completo ("com.example").

3. **Agrupación de Dependencias**:
   - **Original**: Usaba `defaultdict(set)` para almacenar dependencias entre clases individuales.
   - **Modificado**: Usa un `set` (`group_dependencies`) para almacenar aristas dirigidas entre grupos de paquetes como tuplas `(from_group, to_group)`.
   - Para cada clase:
     - Calcula su grupo de paquete (`importer_group`) usando `get_package_group`.
     - Para cada importación específica que esté dentro del proyecto (`imp in all_classes`) y no sea la clase misma (`imp != full_class_name`):
       - Calcula el grupo de paquete de la clase importada (`imported_group`).
       - Si los grupos difieren (`imported_group != importer_group`), añade una arista a `group_dependencies`.
   - El `set` asegura unicidad, por lo que múltiples dependencias entre los mismos grupos resultan en una sola arista.

4. **Salida DOT**:
   - **Original**: Imprimía aristas entre clases individuales (ej., "org.springframework.boot.App" -> "org.apache.commons.IOUtils").
   - **Modificado**: Imprime aristas entre grupos de paquetes (ej., "org.springframework" -> "org.apache" para `level=2`).
   - Las aristas se ordenan para una salida consistente.

### Cómo Cumple con Tus Requisitos

- **Soporte para Niveles**: El script ahora acepta un parámetro `level` para agrupar paquetes antes de analizar las dependencias.
- **Nivel = 1**: Agrupa todas las clases por su paquete de nivel superior (ej. "org"). Por ejemplo, "org.springframework.boot.App" y "org.apache.commons.IOUtils" pertenecen ambos al grupo "org", por lo que las importaciones entre ellos dentro de "org" no se muestran como aristas.
- **Nivel = 2**: Agrupa clases por los dos primeros niveles de paquete (ej. "org.springframework"). Por ejemplo, una importación de "org.springframework.boot.App" a "org.apache.commons.IOUtils" crea una arista de "org.springframework" a "org.apache".
- **Acumular Paquetes Antes del Análisis de Dependencias**: El script determina el grupo de paquete de cada clase basado en `level` antes de analizar sus importaciones, asegurando que las dependencias sean entre grupos, no entre clases individuales.
- **Cumplimiento del Ejemplo**: Para tu arista de ejemplo:
  - Original: `"org.springframework.boot.web.servlet.server.Session" -> "org.springframework.boot.convert.DurationUnit"`
  - Con `level=2`: Ambas clases están en "org.springframework", por lo que no se añade arista (mismo grupo).
  - Con `level=3`: "org.springframework.boot.web" -> "org.springframework.boot.convert", añadiendo una arista entre estos grupos distintos.

### Ejemplos de Uso

- **Comando**: `python script.py /ruta/al/proyecto 1`
  - Grupos: "org", "com", etc.
  - La salida podría incluir: `"org" -> "com"` si una clase en un paquete "org" importa una clase en un paquete "com".

- **Comando**: `python script.py /ruta/al/proyecto 2`
  - Grupos: "org.springframework", "org.apache", etc.
  - La salida podría incluir: `"org.springframework" -> "org.apache"`.

### Notas

- El script mantiene el comportamiento original de solo incluir dependencias intra-proyecto (importaciones dentro de `all_classes`) y excluir importaciones comodín y auto-dependencias.
- Las clases sin una declaración de paquete se omiten, consistente con el script original.
- La salida es un gráfico dirigido en formato DOT, visualizable con herramientas como Graphviz.

Este script modificado debería satisfacer completamente tu solicitud de agrupar dependencias por nivel de jerarquía de paquete.