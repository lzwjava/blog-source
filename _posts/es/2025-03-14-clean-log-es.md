---
audio: false
generated: true
lang: es
layout: post
title: Mensajes de Registro Limpios
translated: true
type: note
---

```python
import sys
import argparse
from difflib import SequenceMatcher

def clean_log(input_path=None, output_path=None, similarity_threshold=1.0, lines_to_compare=1):
    """
    Lee un archivo de log, elimina líneas de log estándar consecutivas duplicadas basándose en similitud,
    y escribe el log limpio a un archivo especificado, por defecto sobrescribiendo el archivo de entrada.

    Args:
        input_path (str, optional): Ruta al archivo de log de entrada. Si es None, lee desde stdin.
        output_path (str, optional): Ruta al archivo de log de salida. Si es None, sobrescribe el archivo de entrada.
        similarity_threshold (float, optional): Ratio de similitud (0.0 a 1.0) para considerar líneas como duplicadas. Por defecto 1.0 (coincidencia exacta).
        lines_to_compare (int, optional): Número de líneas consecutivas a comparar. Por defecto 1.
    """

    if not isinstance(lines_to_compare, int) or lines_to_compare < 1:
        raise ValueError("lines_to_compare debe ser un entero mayor o igual a 1.")

    # Determinar la fuente de entrada
    if input_path:
        try:
            with open(input_path, 'r') as infile:
                lines = infile.readlines()
        except FileNotFoundError:
            print(f"Error: Archivo no encontrado en la ruta: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()  # Leer todas las líneas desde stdin

    # Determinar el destino de salida
    if output_path:
        try:
            outfile = open(output_path, 'w')
        except IOError:
            print(f"Error: No se puede abrir el archivo para escritura: {output_path}", file=sys.stderr)
            sys.exit(1)
    elif input_path:
        try:
            outfile = open(input_path, 'w')  # Sobrescribir el archivo de entrada
        except IOError:
            print(f"Error: No se puede abrir el archivo para escritura: {input_path}", file=sys.stderr)
            sys.exit(1)
    else:
        outfile = sys.stdout  # Por defecto stdout si no hay input_path

    num_lines = len(lines)
    i = 0
    removed_lines = 0
    while i < num_lines:
        # Recolectar 'lines_to_compare' líneas o líneas restantes si son menos que 'lines_to_compare'
        current_lines = lines[i:min(i + lines_to_compare, num_lines)]

        # Procesar solo si tenemos suficientes líneas para comparar
        if len(current_lines) == lines_to_compare:
            # Extraer información estándar del primer conjunto de líneas
            current_standards = []
            all_standard = True
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    level, _, thread, message = parts
                    current_standards.append((thread, message))
                else:
                    print(f"Línea no estándar: {line.strip()}")
                    print(line, end='', file=outfile)
                    all_standard = False
                    break  # Detener procesamiento de este grupo si se encuentra una línea no estándar

            if all_standard:
                # Extraer información estándar del segundo conjunto de líneas (si está disponible)
                next_lines_start_index = i + lines_to_compare
                next_lines_end_index = min(next_lines_start_index + lines_to_compare, num_lines)
                next_lines = lines[next_lines_start_index:next_lines_end_index]

                if len(next_lines) == lines_to_compare:
                    next_standards = []
                    for line in next_lines:
                        parts = line.split(" | ", 3)
                        if len(parts) == 4:
                            level, _, thread, message = parts
                            next_standards.append((thread, message))
                        else:
                            # Tratar las siguientes líneas como no estándar si alguna de ellas no es estándar
                            next_standards = None
                            break

                    if next_standards:
                        similarity = SequenceMatcher(None, ' '.join([' '.join(x) for x in current_standards]), ' '.join([' '.join(x) for x in next_standards])).ratio()
                        print(f"Similitud: {similarity:.4f}, Umbral: {similarity_threshold:.4f}")

                        if similarity < similarity_threshold:
                            for line in current_lines:
                                print(line, end='', file=outfile)
                        else:
                            print(f"Omitiendo líneas duplicadas: { ''.join([line.strip() for line in current_lines])}")
                            removed_lines += len(current_lines)
                    else:
                        for line in current_lines:
                            print(line, end='', file=outfile)
                else:
                    for line in current_lines:
                        print(line, end='', file=outfile)
            i += lines_to_compare  # Mover al siguiente conjunto de líneas
        else:
            # Manejar las líneas restantes (menos que 'lines_to_compare')
            for line in current_lines:
                parts = line.split(" | ", 3)
                if len(parts) == 4:
                    print(line, end='', file=outfile)
                else:
                    print(f"Línea no estándar: {line.strip()}")
                    print(line, end='', file=outfile)
            i += len(current_lines)

    if output_path or input_path:
        outfile.close()

    print(f"Se eliminaron {removed_lines} líneas duplicadas.")


def is_valid_similarity_threshold(value):
    """
    Verificar si el valor dado es un umbral de similitud válido.
    """
    try:
        value = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("El umbral de similitud debe ser un número de punto flotante.")
    if 0.0 <= value <= 1.0:
        return value
    else:
        raise argparse.ArgumentTypeError("El umbral de similitud debe estar entre 0.0 y 1.0.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Eliminar líneas de log duplicadas de un archivo o stdin y escribir a un archivo, por defecto sobrescribiendo el archivo de entrada.")
    parser.add_argument("input_path", nargs="?", type=str, help="Ruta al archivo de log de entrada (opcional, por defecto stdin)")
    parser.add_argument("-o", "--output_path", type=str, help="Ruta al archivo de log de salida (opcional, por defecto sobrescribe el archivo de entrada)")
    parser.add_argument("-s", "--similarity", type=is_valid_similarity_threshold, default=1.0, help="Umbral de similitud (0.0-1.0) para considerar líneas como duplicadas (por defecto: 1.0)")
    parser.add_argument("-l", "--lines", type=int, default=1, help="Número de líneas consecutivas a comparar (por defecto: 1)")

    args = parser.parse_args()

    clean_log(args.input_path, args.output_path, args.similarity, args.lines)
```

Este script Python `clean_log.py` está diseñado para eliminar líneas de log duplicadas de un archivo o entrada estándar. Utiliza un umbral de similitud para determinar si líneas de log consecutivas son lo suficientemente similares para ser consideradas duplicadas.

Aquí hay un desglose del código:

**1. Importaciones:**

- `sys`: Se utiliza para interactuar con el intérprete de Python, como leer desde stdin y escribir a stderr.
- `argparse`: Se utiliza para crear una interfaz de línea de comandos.
- `difflib.SequenceMatcher`: Se utiliza para comparar la similitud entre secuencias de strings.

**2. Función `clean_log`:**

- Toma `input_path`, `output_path`, `similarity_threshold` y `lines_to_compare` como argumentos.
- `input_path`: Especifica el archivo de log de entrada. Si es `None`, lee desde stdin.
- `output_path`: Especifica el archivo de salida. Si es `None` y se da `input_path`, sobrescribe el archivo de entrada. Si ambos son `None`, escribe a stdout.
- `similarity_threshold`: Un float entre 0.0 y 1.0 que determina el ratio mínimo de similitud para que las líneas sean consideradas duplicadas. Un valor de 1.0 significa que solo se eliminan líneas idénticas.
- `lines_to_compare`: Un entero que especifica el número de líneas consecutivas a comparar para similitud.

- **Manejo de Entrada:**
    - Lee líneas desde el archivo de entrada o stdin.
    - Maneja `FileNotFoundError` si el archivo de entrada no existe.

- **Manejo de Salida:**
    - Abre el archivo de salida para escritura o usa stdout.
    - Maneja `IOError` si el archivo de salida no puede abrirse.

- **Lógica de Eliminación de Duplicados:**
    - Itera a través de las líneas del archivo de log en fragmentos de `lines_to_compare`.
    - Para cada fragmento:
        - Divide cada línea en partes basándose en el delimitador " | ", esperando cuatro partes: nivel, timestamp, thread y mensaje.
        - Si una línea no tiene cuatro partes, se considera una línea "no estándar" y se imprime a la salida sin comparación.
        - Si todas las líneas en el fragmento actual son estándar, las compara con las siguientes `lines_to_compare` líneas.
        - Usa `SequenceMatcher` para calcular el ratio de similitud entre los strings unidos de las partes de thread y mensaje de los fragmentos actual y siguiente.
        - Si el ratio de similitud es menor que el `similarity_threshold`, el fragmento actual de líneas se imprime a la salida.
        - Si el ratio de similitud es mayor o igual al `similarity_threshold`, el fragmento actual de líneas se considera duplicado y se omite.
    - Maneja las líneas restantes al final del archivo (menos de `lines_to_compare` líneas).

- **Estadísticas:**
    - Lleva un registro del número de líneas eliminadas.
    - Imprime el número de líneas eliminadas a la consola.

- **Cierre de Archivo:**
    - Cierra el archivo de salida si fue abierto.

**3. Función `is_valid_similarity_threshold`:**

- Una función auxiliar utilizada por `argparse` para validar el argumento del umbral de similitud.
- Verifica si el valor de entrada es un float entre 0.0 y 1.0.

**4. Bloque `if __name__ == "__main__":`:**

- Este bloque se ejecuta cuando el script se ejecuta desde la línea de comandos.
- Usa `argparse` para crear un analizador de argumentos de línea de comandos.
- Define los siguientes argumentos:
    - `input_path`: La ruta al archivo de log de entrada (opcional).
    - `-o` o `--output_path`: La ruta al archivo de log de salida (opcional).
    - `-s` o `--similarity`: El umbral de similitud (por defecto: 1.0).
    - `-l` o `--lines`: El número de líneas a comparar (por defecto: 1).
- Analiza los argumentos de línea de comandos usando `parser.parse_args()`.
- Llama a la función `clean_log` con los argumentos analizados.

**En resumen, el script proporciona una forma flexible de limpiar archivos de log eliminando líneas duplicadas basándose en un umbral de similitud configurable y número de líneas a comparar. Soporta lectura desde stdin, escritura a stdout y sobrescritura del archivo de entrada.**