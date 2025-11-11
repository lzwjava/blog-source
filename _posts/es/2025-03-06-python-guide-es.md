---
audio: false
generated: true
lang: es
layout: post
title: Guía de Python
translated: true
type: note
---

Aquí tienes una guía concisa de Python que cubre operaciones con cadenas, matemáticas, procesamiento de texto, E/S, manejo de archivos, redes, colecciones y multihilo. Cada sección incluye una breve descripción general y ejemplos prácticos para ayudarte a comenzar o refrescar tus conocimientos.

---

## Guía de Python: Temas Esenciales

### 1. Operaciones con Cadenas
Las cadenas en Python son secuencias inmutables de caracteres. Puedes realizar operaciones como concatenación, repetición, segmentación y usar métodos integrados para su manipulación.

**Ejemplos:**
```python
# Concatenación y repetición
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Salida: Hello World
print(s1 * 3)         # Salida: HelloHelloHello

# Segmentación (slicing)
print(s1[1:4])        # Salida: ell

# Métodos integrados
print(s1.upper())     # Salida: HELLO
print(s2.lower())     # Salida: world
print("  hi  ".strip())  # Salida: hi
print("a,b,c".split(','))  # Salida: ['a', 'b', 'c']
print(','.join(['a', 'b', 'c']))  # Salida: a,b,c

# Formateo de cadenas con f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Salida: My name is Alice and I am 30 years old.
```

---

### 2. Matemáticas
El módulo `math` proporciona funciones y constantes matemáticas para cálculos comunes.

**Ejemplo:**
```python
import math

print(math.sqrt(16))    # Salida: 4.0
print(math.pow(2, 3))   # Salida: 8.0
print(math.sin(math.pi / 2))  # Salida: 1.0
print(math.pi)          # Salida: 3.141592653589793
```

---

### 3. Procesamiento de Texto (Expresiones Regulares)
El módulo `re` permite la búsqueda de patrones y la manipulación de texto usando expresiones regulares.

**Ejemplo:**
```python
import re

text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())  # Salida: Found: rain

# Encontrar todas las palabras de 4 letras
print(re.findall(r"\b\w{4}\b", text))  # Salida: ['rain', 'Spain']
```

---

### 4. E/S (Entrada y Salida)
Las operaciones básicas de entrada y salida permiten la interacción con el usuario.

**Ejemplo:**
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

### 5. Manejo de Archivos
Python simplifica la lectura y escritura de archivos usando la función `open()`, recomendándose el uso de la sentencia `with` para el cierre automático del archivo.

**Ejemplo:**
```python
# Escribir en un archivo
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")

# Leer de un archivo
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # Salida: Hello, World!
```

---

### 6. Redes
La librería `requests` (instalar con `pip install requests`) facilita la realización de peticiones HTTP.

**Ejemplo:**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Salida: 200
print(response.json())       # Salida: datos JSON de la API de GitHub
```

---

### 7. Colecciones
El módulo `collections` ofrece estructuras de datos especializadas como `Counter`, `deque`, `namedtuple`, etc. Aquí un ejemplo con `Counter`.

**Ejemplo:**
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry"]
word_count = Counter(words)
print(word_count)  # Salida: Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

**Otras Colecciones:**
- `namedtuple`: Crea subclases de tupla con campos con nombre.
- `deque`: Cola de doble extremo para inserciones y extracciones eficientes por ambos extremos.
- `OrderedDict`: Diccionario que recuerda el orden de inserción.
- `defaultdict`: Diccionario con un valor por defecto para claves faltantes.

---

### 8. Multihilo
El módulo `threading` permite la ejecución concurrente de tareas, ideal para operaciones limitadas por E/S.

**Ejemplo:**
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# Crear e iniciar un hilo
t = threading.Thread(target=print_numbers)
t.start()

# El hilo principal continúa
print("Main thread finished")
```

---

Esta guía proporciona un punto de partida para cada tema con ejemplos prácticos. Para un aprendizaje más profundo, consulta la documentación oficial de Python o recursos especializados. ¡Feliz codificación!