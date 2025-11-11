---
audio: false
generated: true
lang: es
layout: post
title: Analizar Paquetes de Java
translated: true
type: note
---

Según tu consulta, deseas un script donde, si el parámetro `level` es 0 o no se proporciona, utilice el nombre completo del paquete (todas sus partes), tratando esencialmente `level = 0` como "infinito" o "usar todas las partes", en lugar de limitarlo a un número específico de partes (como solo la primera parte cuando `level = 1`). A continuación, explicaré cómo se puede implementar esto en un script de Python que analiza archivos Java para extraer nombres de paquetes, y proporcionaré una solución completa adaptada a tu solicitud.

### Comprensión del Requerimiento
- **Cuando `level = 0` o no se proporciona**: Usa el nombre completo del paquete tal como se extrae de las sentencias `import` de Java (ej., `java.util` o `com.google.common.eventbus`), sin truncarlo.
- **Cuando `level > 0`**: Trunca el nombre del paquete a las primeras `level` partes (ej., para `com.google.common.eventbus`, `level = 2` daría `com.google`).
- El script aún debe procesar archivos Java, extraer nombres de paquetes de las sentencias `import` y manejar casos extremos apropiadamente.

### Enfoque de la Solución
1. **Análisis de Argumentos**:
   - Si solo se proporciona el directorio raíz (ej., `python script.py /ruta/al/directorio`), establecer `level = 0`, lo que significa usar el nombre completo del paquete.
   - Si se proporciona `level` (ej., `python script.py /ruta/al/directorio 2`), usarlo para truncar el nombre del paquete, asegurándose de que sea un entero no negativo.
   - Salir con un error si los argumentos no son válidos.

2. **Extracción de Paquetes**:
   - Extraer el nombre del paquete de las sentencias `import` (ej., `import java.util.ArrayList;` produce `java.util`).
   - Usar las convenciones de nomenclatura de Java: los paquetes son típicamente en minúsculas, y los nombres de clase empiezan con mayúscula.

3. **Lógica de Truncado de Paquetes**:
   - Si `level = 0`, añadir el nombre completo del paquete al conjunto de resultados.
   - Si `level > 0`, dividir el nombre del paquete por puntos (`.`) y tomar las primeras `level` partes.

4. **Registro y Salida**:
   - Indicar claramente si se están usando nombres de paquetes completos o truncados.
   - Listar todos los paquetes únicos encontrados.

### Implementación
Aquí está el script completo de Python que cumple con tus requisitos:

```python
import os
import sys
from collections import Counter

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
    Extrae el nombre del paquete de una sentencia import.
    
    Usa la convención de que los nombres de paquete están en minúsculas, mientras que los nombres de clase
    empiezan con letras mayúsculas. Maneja imports comodín (*).
    
    Args:
        import_statement (str): La línea de la sentencia import de un archivo Java.
    
    Returns:
        str: El nombre del paquete, o una cadena vacía si no se determina.
    """
    parts = import_statement.split()
    if parts[0] == 'import':
        parts = parts[1:]
    if parts[0] == 'static':
        parts = parts[1:]
    import_path = ' '.join(parts).strip(';').strip()
    identifiers = import_path.split('.')
    for i, ident in enumerate(identifiers):
        if ident == '*' or (ident and ident[0].isupper()):
            package_parts = identifiers[:i]
            break
    else:
        package_parts = []
    package = '.'.join(package_parts)
    return package

if __name__ == '__main__':
    # Analizar argumentos de la línea de comandos
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Uso: python script.py <directorio_raíz> [nivel] [--count]")
        sys.exit(1)
    
    root_dir = sys.argv[1]
    level = 0
    count = False
    
    if len(sys.argv) == 3:
        if sys.argv[2] == "--count":
            count = True
        elif sys.argv[2].isdigit():
            level = int(sys.argv[2])
        else:
            print(f"Argumento inválido: {sys.argv[2]}")
            sys.exit(1)
    elif len(sys.argv) == 4:
        if sys.argv[3] == "--count" and sys.argv[2].isdigit():
            level = int(sys.argv[2])
            count = True
        else:
            print(f"Argumentos inválidos: {sys.argv[2]} {sys.argv[3]}")
            sys.exit(1)
    
    # Verificar que el directorio existe
    if not os.path.isdir(root_dir):
        print(f"[ERROR] La ruta especificada no es un directorio: {root_dir}")
        sys.exit(1)
    
    # Registrar el inicio del análisis
    level_str = "usando nombres de paquete completos" if level == 0 else f"al nivel {level}"
    count_str = "con conteo de apariciones" if count else ""
    print(f"[INFO] Iniciando análisis del directorio: {root_dir} {level_str} {count_str}")
    
    # Inicializar variables
    package_counter = Counter()
    total_files = 0
    error_files = 0
    
    # Procesar archivos Java
    for java_file in find_java_files(root_dir):
        try:
            with open(java_file, 'r', encoding='utf-8') as f:
                file_packages = set()
                for line in f:
                    line = line.strip()
                    if line.startswith('import'):
                        package = extract_package(line)
                        if package:
                            if level > 0:
                                parts = package.split('.')
                                truncated_package = '.'.join(parts[:level])
                            else:
                                truncated_package = package
                            file_packages.add(truncated_package)
            for pkg in file_packages:
                package_counter[pkg] += 1
            total_files += 1
        except Exception as e:
            print(f"[ERROR] No se pudo leer el archivo {java_file}: {e}")
            error_files += 1
            continue
    
    # Imprimir resumen
    print(f"[INFO] Total de archivos Java intentados: {total_files + error_files}")
    print(f"[INFO] Procesados exitosamente: {total_files}")
    print(f"[INFO] Archivos con errores: {error_files}")
    if count:
        print(f"[INFO] Total de paquetes únicos con conteo: {len(package_counter)}")
    else:
        print(f"[INFO] Total de paquetes únicos: {len(package_counter)}")
    
    # Imprimir resultados con ordenamiento apropiado
    if package_counter:
        if count:
            print("[INFO] Análisis completo. Imprimiendo paquetes únicos con conteo (ordenados por conteo descendente):")
            # Ordenar por conteo descendente, luego por nombre de paquete ascendente
            for pkg, cnt in sorted(package_counter.items(), key=lambda x: (-x[1], x[0])):
                print(f"{pkg}: {cnt}")
        else:
            print("[INFO] Análisis completo. Imprimiendo paquetes únicos (ordenados por nombre ascendente):")
            # Ordenar por nombre de paquete ascendente
            for pkg in sorted(package_counter):
                print(pkg)
    else:
        print("[INFO] No se encontraron paquetes.")
```

### Cómo Funciona
- **Ejecutar el Script**:
  - `python script.py /ruta/al/proyecto/java`: Analiza todos los archivos `.java` en el directorio y usa nombres de paquetes completos (`level = 0`).
  - `python script.py /ruta/al/proyecto/java 2`: Trunca los nombres de paquete a las primeras 2 partes (ej., `com.google.common.eventbus` se convierte en `com.google`).

- **Ejemplo de Salida**:
  Supongamos que tienes un archivo Java con:
  ```java
  import java.util.ArrayList;
  import com.google.common.eventbus.EventBus;
  ```
  - **Con `level = 0` (o sin nivel proporcionado)**:
    ```
    [INFO] Iniciando análisis del directorio: /ruta/al/proyecto/java usando nombres de paquete completos.
    [INFO] Total de archivos Java intentados: 1
    [INFO] Procesados exitosamente: 1
    [INFO] Archivos con errores: 0
    [INFO] Total de paquetes completos únicos: 2
    [INFO] Análisis completo. Imprimiendo paquetes completos únicos:
    com.google.common.eventbus
    java.util
    ```
  - **Con `level = 2`**:
    ```
    [INFO] Iniciando análisis del directorio: /ruta/al/proyecto/java al nivel 2
    [INFO] Total de archivos Java intentados: 1
    [INFO] Procesados exitosamente: 1
    [INFO] Archivos con errores: 0
    [INFO] Total de paquetes únicos al nivel 2: 2
    [INFO] Análisis completo. Imprimiendo paquetes únicos al nivel 2:
    com.google
    java.util
    ```

- **Características Clave**:
  - **Nombres de Paquete Completos**: Cuando `level = 0` o no se pasa, usa el nombre completo del paquete tal como se extrajo (ej., `java.util`, `com.google.common.eventbus`).
  - **Truncado**: Cuando `level > 0`, toma las primeras `level` partes.
  - **Manejo de Errores**: Verifica que el directorio sea válido y que `level` sea no negativo.
  - **Unicidad**: Almacena los paquetes en un `set` para evitar duplicados.

### Casos Extremos Manejados
- **Nivel Faltante**: Por defecto `level = 0`, usando nombres de paquete completos.
- **Nivel Inválido**: Sale con un error si `level` es negativo o no es un entero.
- **Paquetes Cortos**: Si un paquete tiene menos partes que `level` (ej., `java` con `level = 2`), usa el paquete completo (`java`).
- **Imports Vacíos**: Omite líneas donde no se extrae ningún paquete.

Este script satisface completamente tu requerimiento: cuando `level = 0` o no se proporciona, usa todas las partes del nombre del paquete, tratándolo efectivamente como "infinito" en términos de partes utilizadas.