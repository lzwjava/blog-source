---
audio: false
lang: es
layout: post
title: Análisis de Paquetes Java en Proyecto
translated: true
---

Aquí tienes un script de Python que analiza un directorio recursivamente, encuentra todos los paquetes de Java utilizados en los archivos `.java`, elimina duplicados y lista todos los paquetes únicos utilizados en el proyecto. El script se centra únicamente en los archivos `.java` y maneja proyectos que pueden tener módulos recorriendo todos los subdirectorios.

### Script de Python:

```python
import os
import sys

def find_java_files(root_dir):
    """
    Encuentra recursivamente todos los archivos .java en el directorio dado y sus subdirectorios.

    Args:
        root_dir (str): El directorio raíz desde donde comenzar la búsqueda.

    Yields:
        str: La ruta completa a cada archivo .java.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.java'):
                yield os.path.join(dirpath, filename)

def extract_package(import_statement):
    """
    Extrae el nombre del paquete de una declaración de importación.

    Utiliza la convención de que los nombres de los paquetes suelen estar en minúsculas, mientras que los nombres de las clases
    comienzan con letras mayúsculas. Para las importaciones comodín (*), el paquete es la parte antes de '*'.

    Args:
        import_statement (str): La línea de declaración de importación de un archivo Java.

    Returns:
        str: El nombre del paquete, o una cadena vacía si no se determina.
    """
    # Elimina 'import' y 'static' si están presentes
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]

    # Une las partes restantes y elimina el ';' final
    import_path = ' '.join(parts).strip(';').strip()

    # Divide la ruta de importación por '.'
    identifiers = import_path.split('.')

    # Encuentra el índice donde el primer identificador comienza con mayúscula o es '*'
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []

    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # Verifica el argumento de la línea de comandos para el directorio raíz
    if len(sys.argv) < 2:
        print("Uso: python script.py <directorio_raíz>")
        sys.exit(1)

    root_dir = sys.argv[1]
    packages = set()

    # Recorre todos los archivos .java en el directorio y subdirectorios
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:  # Solo añade nombres de paquetes no vacíos
                            packages.add(package)
        except Exception as e:
            print(f"Advertencia: No se pudo leer el archivo {java_file}: {e}")
            continue

    # Imprime la lista ordenada de paquetes únicos
    for package in sorted(packages):
        print(package)
```

### Cómo usar el script:

1. Guarda el script en un archivo, por ejemplo, `analyze_java_packages.py`.
2. Ejecuta el script desde la línea de comandos, proporcionando la ruta al directorio raíz del proyecto de Java:
   ```
   python analyze_java_packages.py /ruta/a/tu/proyecto/java
   ```
3. El script imprimirá una lista ordenada de nombres de paquetes únicos que se importan en los archivos `.java`.

### Qué hace el script:

- **Encuentra archivos `.java`:**
  - Usa `os.walk()` para recorrer recursivamente el directorio y sus subdirectorios.
  - Identifica todos los archivos que terminan con `.java`.

- **Extrae nombres de paquetes:**
  - Analiza cada archivo `.java` línea por línea.
  - Identifica líneas que comienzan con `import`.
  - Extrae nombres de paquetes de las declaraciones de importación, manejando:
    - Importaciones regulares (por ejemplo, `import java.util.List;`).
    - Importaciones comodín (por ejemplo, `import java.util.*;`).
    - Importaciones estáticas (por ejemplo, `import static java.util.Collections.sort;`).
  - Usa una heurística basada en las convenciones de nomenclatura de Java:
    - Los nombres de los paquetes suelen estar en minúsculas (por ejemplo, `java.util`).
    - Los nombres de las clases suelen comenzar con letras mayúsculas (por ejemplo, `List`, `Collections`).
    - Las importaciones comodín terminan con `*`.

- **Elimina duplicados:**
  - Recopila todos los nombres de paquetes en un `set` para eliminar automáticamente los duplicados.

- **Imprime los resultados:**
  - Convierte el conjunto en una lista ordenada e imprime cada nombre de paquete en una nueva línea.

### Suposiciones y limitaciones:

- **Declaraciones de importación:**
  - Supone que las declaraciones de importación están en sus propias líneas y no están incrustadas en comentarios o cadenas.
  - Maneja tanto importaciones regulares como estáticas, incluidas las importaciones comodín.

- **Convenciones de nomenclatura:**
  - Se basa en la convención de que los nombres de los paquetes están en minúsculas y los nombres de las clases comienzan con letras mayúsculas.
  - Puede no manejar correctamente la nomenclatura no estándar (por ejemplo, nombres de paquetes en mayúsculas), pero esto es raro en la práctica.

- **Codificación de archivos:**
  - Supone que los archivos `.java` están codificados en UTF-8. Ajusta el parámetro `encoding` si es necesario.

- **Manejo de errores:**
  - Incluye manejo básico de errores para archivos no legibles, imprimiendo una advertencia y continuando.

### Ejemplo:

Si tu proyecto de Java tiene los siguientes archivos `.java`:

- **File1.java:**
  ```java
  import java.util.List;
  import java.util.*;
  import java.lang.String;
  ```

- **File2.java:**
  ```java
  import java.util.Collections;
  import static java.util.Collections.sort;
  import com.example.myapp.*;
  ```

Ejecutar el script imprimirá:
```
com.example.myapp
java.lang
java.util
```

Esto lista todos los paquetes únicos importados en el proyecto, ordenados alfabéticamente.

### Notas:

- El script se centra en los paquetes importados mediante declaraciones `import`, que representan los paquetes externos e internos que el proyecto utiliza.
- No incluye las declaraciones de paquetes de los archivos `.java` mismos (por ejemplo, `package com.mycompany.myapp;`), ya que estas definen los paquetes a los que pertenecen los archivos, no los paquetes que utilizan.
- Dado que el proyecto puede tener módulos, el script analiza recursivamente todos los subdirectorios para asegurarse de que todos los archivos `.java` se procesen.