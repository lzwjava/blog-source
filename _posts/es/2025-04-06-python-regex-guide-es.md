---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Guía de Expresiones Regulares en Python
translated: true
type: note
---

### Importar el módulo `re`
El módulo `re` (abreviatura de expresiones regulares) es parte de la biblioteca estándar de Python. No es un "paquete regex" separado, sino un módulo integrado. Impórtalo al inicio de tu script:

```python
import re
```

### Conceptos Básicos
Las expresiones regulares (regex) son patrones utilizados para buscar, coincidir y manipular cadenas de texto. Utilizan caracteres especiales como:
- `.` (cualquier carácter)
- `*` (cero o más ocurrencias)
- `+` (una o más ocurrencias)
- `[]` (clases de caracteres, ej. `[a-z]` para letras minúsculas)
- `^` (inicio de cadena), `$` (fin de cadena)

Los ejemplos están basados en la documentación de `re` de Python. Siempre compila patrones complejos para mayor eficiencia con `re.compile()`.

### Funciones Clave y Uso

#### 1. **Coincidir un Patrón al Inicio**
   - `re.match(pattern, string)`: Verifica si el patrón coincide desde el principio de la cadena.
   - Retorna un objeto match o `None`.

   Ejemplo:
   ```python
   import re
   result = re.match(r"Hello", "Hello world")
   print(result.group())  # Salida: Hello
   ```

#### 2. **Buscar en Cualquier Parte de la Cadena**
   - `re.search(pattern, string)`: Encuentra la primera ocurrencia del patrón en cualquier lugar.
   - Retorna un objeto match o `None`.

   Ejemplo:
   ```python
   result = re.search(r"world", "Hello world")
   print(result.group())  # Salida: world
   ```

#### 3. **Encontrar Todas las Coincidencias**
   - `re.findall(pattern, string)`: Retorna una lista de todas las coincidencias no superpuestas.

   Ejemplo:
   ```python
   matches = re.findall(r"\d+", "I have 3 cats and 42 dogs")
   print(matches)  # Salida: ['3', '42']
   ```

#### 4. **Dividir Cadenas**
   - `re.split(pattern, string)`: Divide la cadena en las ocurrencias del patrón.

   Ejemplo:
   ```python
   parts = re.split(r"\s+", "Hello    world   example")
   print(parts)  # Salida: ['Hello', 'world', 'example']
   ```

#### 5. **Reemplazar Coincidencias**
   - `re.sub(pattern, replacement, string)`: Reemplaza las coincidencias con la cadena de reemplazo.

   Ejemplo:
   ```python
   new_string = re.sub(r"bad", "good", "This is bad")
   print(new_string)  # Salida: This is good
   ```

#### 6. **Compilar Patrones para Reutilizar**
   - Para uso repetido, compila la regex en un objeto pattern para mejor rendimiento.

   Ejemplo:
   ```python
   pattern = re.compile(r"\d+")
   matches = pattern.findall("Room 101 and 102")
   print(matches)  # Salida: ['101', '102']
   ```

### Mejores Prácticas
- Usa cadenas crudas (`r""`) para los patrones regex y evitar problemas de escape de barras invertidas.
- Maneja objetos match: Usa `.group()` para obtener la coincidencia, `.span()` para los índices.
- Para tareas complejas, prueba los patrones con herramientas en línea o el shell interactivo de Python.
- Consulta la documentación oficial de Python: https://docs.python.org/3/library/re.html para más ejemplos y flags (ej. `re.IGNORECASE`).

¡Si tienes un caso de uso específico o un error, proporciona más detalles!