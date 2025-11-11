---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Coincidencia de Archivos con el Módulo Glob de Python
translated: true
type: note
---

### Importar Glob
Para usar glob en Python, importa el módulo de la biblioteca estándar:
```python
import glob
```

### Funcionalidad Básica
La función `glob.glob()` toma una cadena de patrón y devuelve una lista de rutas de archivos o directorios que coinciden. Utiliza comodines al estilo de shell de Unix:

- `*`: Coincide con cualquier secuencia de caracteres (excepto separadores de ruta).
- `?`: Coincide con cualquier carácter individual.
- `[seq]`: Coincide con cualquier carácter en seq (por ejemplo, `[0-9]` para dígitos).
- `**`: Coincide con directorios recursivamente (requiere `recursive=True`).

Los patrones son relativos al directorio actual a menos que se especifique una ruta absoluta.

### Ejemplos de Uso

#### 1. Encontrar todos los archivos .txt en el directorio actual
```python
import glob

files = glob.glob("*.txt")
print(files)  # Salida: ['file1.txt', 'file2.txt', ...]
```

#### 2. Encontrar archivos con extensiones específicas en un subdirectorio
```python
files = glob.glob("documents/*.pdf")
print(files)  # Salida: ['documents/doc1.pdf', ...]
```

#### 3. Coincidir patrones específicos (por ejemplo, archivos que comienzan con 'log' y terminan con números)
```python
files = glob.glob("log[0-9].txt")
print(files)  # Salida: ['log1.txt', 'log2.txt', ...] si tales archivos existen
```

#### 4. Búsqueda recursiva en subdirectorios
Usa `**` con `recursive=True` para buscar en directorios y subdirectorios:
```python
files = glob.glob("**/*.py", recursive=True)
print(files)  # Salida: ['script1.py', 'subdir/script2.py', ...]
```

### Notas Importantes
- Los resultados no están ordenados por defecto; usa `sorted()` si necesitas orden: `sorted(glob.glob("*.txt"))`.
- Para coincidencias que no distingan entre mayúsculas y minúsculas en sistemas de archivos que sí lo hacen, considera combinar con `fnmatch` o manejarlo en el código, ya que glob distingue entre mayúsculas y minúsculas.
- Glob no sigue enlaces simbólicos a menos que se maneje explícitamente; usa `os.walk()` para recorridos más complejos.
- Para una coincidencia a la vez, usa `glob.iglob()` que devuelve un iterador para ahorrar memoria en resultados grandes: `for file in glob.iglob("*.txt"): print(file)`.

Esto cubre lo esencial; consulta la [documentación de Python](https://docs.python.org/3/library/glob.html) para más detalles.