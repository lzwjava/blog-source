---
audio: false
generated: true
lang: es
layout: post
title: 'Verificación de archivos en qBittorrent: Código hash SHA-1'
translated: true
type: note
---

Cuando mueves ubicaciones de archivos en qBittorrent y este verifica los archivos nuevamente antes de compartir (seeding), se está asegurando de que los archivos en la nueva ubicación sean los mismos con los que estaba trabajando originalmente. Esta verificación es crítica en la descarga de torrents para evitar compartir datos incorrectos o corruptos. Así es como funciona el proceso y qué algoritmo utiliza:

### Cómo qBittorrent Verifica los Archivos
qBittorrent no simplemente confía en que los archivos movidos sean correctos; verifica su integridad comparándolos con la información almacenada en el archivo torrent. En la descarga de torrents, los datos se dividen en fragmentos más pequeños llamados **piezas**, y cada pieza tiene un valor hash único. Estos hashes se incluyen en el archivo torrent y actúan como una huella digital para cada pieza de datos. Cuando mueves archivos a una nueva ubicación, qBittorrent utiliza estos hashes de pieza para confirmar que los archivos no han cambiado.

El proceso se puede desglosar en estos pasos:

1.  **Especificar la Nueva Ubicación**: Le indicas a qBittorrent dónde se encuentran ahora los archivos estableciendo la nueva ruta.
2.  **Mapear Archivos al Torrent**: qBittorrent empareja los archivos en la nueva ubicación con los archivos listados en el torrent, típicamente usando nombres de archivo y tamaños (ya que esta información está en el archivo torrent).
3.  **Verificar Hashes de Pieza**: qBittorrent lee los datos de los nuevos archivos pieza por pieza, calcula un hash para cada pieza y lo compara con el hash correspondiente almacenado en el archivo torrent.
4.  **Confirmar Integridad**: Si todos los hashes calculados coinciden con los hashes del torrent, se confirma que los archivos son idénticos y qBittorrent puede reanudar la distribución. Si el hash de alguna pieza no coincide, esa pieza se marca como incompleta o faltante, y qBittorrent puede necesitar volver a descargarla.

### ¿Qué Algoritmo Utiliza?
qBittorrent no utiliza una suma de comprobación (checksum) de archivo completo (como MD5 o SHA-256 para todo el archivo), ya que sería lento e ineficiente, especialmente para archivos grandes. En su lugar, se basa en los **hashes de pieza** definidos por el protocolo BitTorrent. El algoritmo utilizado para estos hashes de pieza es **SHA-1**, una función hash criptográfica ampliamente utilizada. Cada pieza de datos (que podría ser de unos pocos kilobytes a unos pocos megabytes, dependiendo del torrent) se procesa con SHA-1, y esos hashes son contra los que qBittorrent verifica.

El uso de hashes de pieza en lugar de una suma de comprobación de archivo completo tiene dos grandes ventajas:
-   **Eficiencia**: Verificar piezas más pequeñas es más rápido que procesar con hash un archivo completo.
-   **Granularidad**: Si algo sale mal, qBittorrent puede identificar exactamente qué piezas necesitan reparación, en lugar de rechazar todo el archivo.

### Por Qué Esto es Importante
Esta verificación basada en hash garantiza que los datos que estás compartiendo desde la nueva ubicación coincidan con lo que otros pares esperan, manteniendo la integridad del enjambre (swarm) de torrents. Sin esta verificación, mover archivos podría llevar a compartir datos corruptos o no coincidentes, lo que interrumpiría el proceso de descarga de torrents.

En resumen, cuando mueves ubicaciones de archivos en qBittorrent, este vuelve a verificar los archivos calculando los **hashes SHA-1** de cada pieza y comparándolos con los hashes en el archivo torrent. Así es como confirma que todo es correcto antes de que se reanude la distribución.

---

Para demostrar cómo qBittorrent verifica la integridad de los archivos utilizando hashes de pieza (específicamente hashes SHA-1) al mover ubicaciones de archivos, aquí hay un script simple de Python. qBittorrent, siguiendo el protocolo BitTorrent, divide los archivos en piezas, calcula hashes SHA-1 para cada pieza y utiliza estos hashes para garantizar que el contenido del archivo permanezca inalterado, independientemente de su ubicación. Este script simula ese proceso creando un archivo de ejemplo, calculando sus hashes de pieza, verificando una copia idéntica y luego mostrando cómo una modificación hace que la verificación falle.

### Explicación
-   **Hashes de Pieza**: El script divide un archivo en piezas de tamaño fijo (por ejemplo, 10 bytes) y calcula hashes SHA-1 para cada pieza, imitando cómo un archivo torrent almacena estos hashes.
-   **Verificación**: Comprueba si los hashes calculados de un archivo coinciden con los hashes esperados, asegurando la integridad.
-   **Simulación**: Crea un archivo, lo copia (simulando un movimiento), lo verifica, luego modifica la copia y verifica nuevamente para mostrar cómo se detectan los cambios.

Aquí está el script con comentarios para mayor claridad:

```python
import hashlib
import shutil
import os

def compute_piece_hashes(file_path, piece_size):
    """Compute SHA-1 hashes for each piece of the file."""
    hashes = []
    with open(file_path, 'rb') as f:
        while True:
            piece = f.read(piece_size)
            if not piece:
                break
            hash_obj = hashlib.sha1(piece)
            hashes.append(hash_obj.hexdigest())
    return hashes

def verify_file_integrity(file_path, piece_size, expected_hashes):
    """Verify the file's integrity by comparing piece hashes."""
    current_hashes = compute_piece_hashes(file_path, piece_size)
    if len(current_hashes) != len(expected_hashes):
        return False
    for current, expected in zip(current_hashes, expected_hashes):
        if current != expected:
            return False
    return True

# Create a sample file with known content
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a test file.")

piece_size = 10  # bytes, small for demonstration

# Compute expected hashes from file1.txt (simulates torrent hashes)
expected_hashes = compute_piece_hashes('file1.txt', piece_size)
print("Expected hashes:", [h[:8] for h in expected_hashes])  # Show first 8 chars for readability

# Copy file1.txt to file2.txt to simulate moving the file
shutil.copyfile('file1.txt', 'file2.txt')

# Verify file2.txt against expected hashes (should pass)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (unchanged):", "Valid" if is_valid else "Invalid")

# Modify file2.txt to simulate corruption or change
with open('file2.txt', 'a') as f:
    f.write(" Modified")

# Verify again (should fail due to changed content)
is_valid = verify_file_integrity('file2.txt', piece_size, expected_hashes)
print("Verification of file2.txt (modified):", "Valid" if is_valid else "Invalid")

# Clean up the created files
os.remove('file1.txt')
os.remove('file2.txt')
```

### Cómo Funciona
1.  **Creación de Archivo**: Escribe "Hello, this is a test file." (25 bytes) en `file1.txt`.
2.  **Cálculo de Hash**: Divide `file1.txt` en piezas de 10 bytes cada una (por ejemplo, "Hello, thi", "s is a tes", "t file."), calcula los hashes SHA-1 y los almacena como `expected_hashes`.
3.  **Simular Movimiento**: Copia `file1.txt` a `file2.txt`, representando un archivo movido a una nueva ubicación.
4.  **Verificación Inicial**: Comprueba `file2.txt` contra `expected_hashes`. Como el contenido es idéntico, imprime "Valid".
5.  **Modificación**: Añade " Modified" a `file2.txt`, alterando su contenido y tamaño (ahora 34 bytes, dividido en 4 piezas).
6.  **Segunda Verificación**: Comprueba el `file2.txt` modificado. El número de piezas o sus hashes difieren, por lo que imprime "Invalid".
7.  **Limpieza**: Elimina los archivos temporales.

### Ejemplo de Salida
```
Expected hashes: ['dffd6021', 'a2b3c4d5', 'e6f789ab']  # Example hash prefixes
Verification of file2.txt (unchanged): Valid
Verification of file2.txt (modified): Invalid
```
(Los valores hash reales variarán pero seguirán este patrón).

Este script ilustra cómo qBittorrent garantiza la integridad de los archivos comparando hashes de pieza, detectando cualquier cambio incluso después de que un archivo se mueve, lo que lo convierte en una demostración simple pero efectiva del proceso.