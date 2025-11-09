---
audio: false
date: 2025-09-11
generated: true
image: false
lang: es
layout: post
model: google/gemini-2.5-flash
title: Introducción a Ejemplos de Código Python
translated: true
type: note
---

¡De acuerdo! "Algo de código Python" puede significar muchas cosas. Python es increíblemente versátil. Te daré algunos ejemplos comunes, desde muy básicos hasta un poco más complejos, cubriendo diferentes conceptos.

---

### 1. Hola Mundo (El Clásico Inicio)

Este es el programa Python más simple posible.

```python
# Esto es un comentario. Python ignora los comentarios.
print("¡Hola, Mundo!")
```

**Explicación:**
*   `print()` es una función incorporada que envía el argumento dado a la consola.
*   `"¡Hola, Mundo!"` es una cadena de texto.

---

### 2. Variables, Aritmética Básica y Entrada del Usuario

Este código demuestra cómo almacenar datos en variables, realizar operaciones matemáticas simples y obtener información del usuario.

```python
# Variables para almacenar datos
name = input("¿Cómo te llamas? ") # Obtener entrada del usuario
age_str = input("¿Cuántos años tienes? ")

# Convertir la edad de cadena a entero para cálculos
age = int(age_str)

# Aritmética básica
year_of_birth = 2023 - age # Asumiendo que el año actual es 2023 por simplicidad
# También podrías usar: import datetime; year_of_birth = datetime.date.today().year - age

# Imprimir salida formateada usando una f-string (cadena literal formateada)
print(f"Hola, {name}! Tienes {age} años.")
print(f"Probablemente naciste en {year_of_birth}.")

# Una verificación condicional simple
if age < 18:
    print("Eres menor de edad.")
else:
    print("Eres un adulto.")
```

**Explicación:**
*   `input()`: Solicita al usuario una entrada de texto y la devuelve como una cadena.
*   `name`, `age_str`, `age`, `year_of_birth`: Estas son variables que almacenan diferentes tipos de datos (cadena, entero).
*   `int()`: Convierte una cadena en un número entero. Esto es necesario porque `input()` siempre devuelve una cadena, y no puedes hacer matemáticas directamente con cadenas.
*   `f-strings`: Una forma conveniente de incrustar expresiones dentro de literales de cadena. Observa la `f` antes de la comilla de apertura.
*   `if/else`: Sentencias de control de flujo que ejecutan diferentes bloques de código basados en una condición.

---

### 3. Listas y Bucles

Las listas son colecciones ordenadas de elementos. Los bucles se utilizan para repetir un bloque de código varias veces.

```python
# Una lista de frutas
fruits = ["manzana", "plátano", "cereza", "dátil"]

print("\nMis frutas favoritas:")

# Recorrer la lista usando un bucle 'for'
for fruit in fruits:
    print(f"- {fruit.capitalize()}") # .capitalize() pone la primera letra en mayúscula

# Acceder a elementos por índice (las listas son indexadas desde cero)
print(f"\nLa primera fruta es: {fruits[0]}")
print(f"La última fruta es: {fruits[-1]}") # El índice negativo accede desde el final

# Añadir un elemento
fruits.append("saúco")
print(f"Lista actualizada: {fruits}")

# Eliminar un elemento
fruits.remove("plátano")
print(f"Lista después de eliminar plátano: {fruits}")

# Bucle usando 'range' para obtener índices
print("\nFrutas con sus índices:")
for i in range(len(fruits)): # len() da el número de elementos en la lista
    print(f"Índice {i}: {fruits[i]}")
```

**Explicación:**
*   `[]`: Se utiliza para definir una lista.
*   `for ... in ...`: Un bucle `for` que itera sobre cada elemento de una secuencia (como una lista).
*   `fruit.capitalize()`: Un método de cadena que devuelve una copia de la cadena con su primer carácter en mayúsculas.
*   `fruits[0]`: Accede al primer elemento (índice 0).
*   `fruits[-1]`: Accede al último elemento.
*   `list.append()`: Añade un elemento al final de la lista.
*   `list.remove()`: Elimina la primera aparición de un elemento especificado.
*   `range(len(fruits))`: Genera una secuencia de números desde 0 hasta (pero sin incluir) la longitud de la lista, útil para acceder a elementos por su índice.

---

### 4. Funciones

Las funciones son bloques de código reutilizables que realizan una tarea específica.

```python
# Definir una función que toma argumentos
def greet_person(name, age):
    """
    Esta función saluda a una persona y le dice su edad.
    Es una buena práctica incluir un docstring como este.
    """
    return f"Hola, {name}! Tienes {age} años."

# Llamar a la función
message1 = greet_person("Alicia", 30)
print(message1)

# Llamarla de nuevo con diferentes argumentos
message2 = greet_person("Bob", 25)
print(message2)

# Definir una función con un parámetro por defecto
def calculate_area(length, width=10):
    """Calcula el área de un rectángulo."""
    return length * width

print(f"\nÁrea de un rectángulo 5x10: {calculate_area(5)}") # Usa el ancho por defecto
print(f"Área de un rectángulo 5x7: {calculate_area(5, 7)}") # Anula el ancho por defecto
```

**Explicación:**
*   `def`: Palabra clave para definir una función.
*   `greet_person(name, age)`: Nombre de la función y sus parámetros (entradas).
*   `return`: Envía un valor de vuelta desde la función.
*   Docstrings (`"""El docstring va aquí"""`): Explican lo que hace la función. Son buenos para la documentación.
*   `calculate_area(length, width=10)`: Muestra un parámetro por defecto. Si no se proporciona `width` al llamar a la función, por defecto será 10.

---

### 5. Diccionarios

Los diccionarios almacenan datos en pares clave-valor. No están ordenados (en versiones antiguas de Python, ordenados en Python 3.7+).

```python
# Un diccionario que representa a una persona
person = {
    "first_name": "Charlie",
    "last_name": "Smith",
    "age": 40,
    "city": "Londres",
    "occupations": ["Ingeniero", "Profesor"] # Una lista puede ser un valor
}

print("\nDetalles de la persona:")

# Acceder a valores por clave
print(f"Nombre: {person['first_name']} {person['last_name']}")
print(f"Vive en: {person.get('city', 'Desconocido')}") # .get() es más seguro, devuelve None/valor por defecto si la clave no se encuentra
print(f"Primera ocupación: {person['occupations'][0]}")

# Modificar un valor
person["age"] = 41
print(f"Nueva edad: {person['age']}")

# Añadir un nuevo par clave-valor
person["email"] = "charlie.smith@example.com"
print(f"Correo electrónico: {person['email']}")

# Recorrer un diccionario
print("\nTodas las claves:")
for key in person: # Recorre las claves por defecto
    print(key)

print("\nTodos los valores:")
for value in person.values():
    print(value)

print("\nTodos los pares clave-valor:")
for key, value in person.items():
    print(f"{key}: {value}")
```

**Explicación:**
*   `{}`: Se utilizan para definir un diccionario.
*   `"clave": valor`: Pares clave-valor. Las claves deben ser únicas e inmutables (como cadenas o números). Los valores pueden ser de cualquier tipo de dato.
*   `person['clave']`: Accede al valor asociado con `clave`.
*   `person.get('clave', 'valor_por_defecto')`: Una forma más segura de acceder, evita `KeyError` si la clave no existe, devolviendo `valor_por_defecto` en su lugar.
*   `dict.values()`: Devuelve un objeto de vista que muestra una lista de todos los valores en el diccionario.
*   `dict.items()`: Devuelve un objeto de vista que muestra una lista de los pares de tuplas clave-valor del diccionario.

---

¡Esto solo es rascar la superficie, pero estos ejemplos cubren muchos conceptos fundamentales de Python que usarás con frecuencia