---
audio: false
generated: true
lang: es
layout: post
title: Guía de POO en Python
translated: true
type: note
---

Aquí tienes una guía completa sobre Programación Orientada a Objetos (OOP) en Python. Esta guía cubre los conceptos fundamentales—clases, objetos, herencia, polimorfismo, encapsulación y abstracción—junto con ejemplos prácticos para ilustrar cada uno.

---

### 1. Clases y Objetos
Una **clase** es un plano para crear objetos, definiendo sus atributos (datos) y métodos (funciones). Un **objeto** es una instancia de una clase, con sus propios valores específicos para los atributos.

**Ejemplo:**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# Creando un objeto
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # Salida: Buddy says woof!
```

---

### 2. Herencia
La **herencia** permite que una clase (clase hija) herede atributos y métodos de otra clase (clase padre), promoviendo la reutilización de código.

**Ejemplo:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Salida: Buddy says woof!
print(cat.speak())  # Salida: Whiskers says meow!
```

---

### 3. Polimorfismo
El **polimorfismo** permite tratar objetos de diferentes clases como instancias de una superclase común, permitiendo que los métodos se utilicen de manera intercambiable.

**Ejemplo:**
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # Salida: Buddy says woof!
animal_sound(cat)  # Salida: Whiskers says meow!
```

---

### 4. Encapsulación
La **encapsulación** restringe el acceso directo a algunos componentes del objeto, promoviendo el ocultamiento de datos. En Python, los atributos privados típicamente tienen el prefijo `_` (convención) o `__` (name mangling).

**Ejemplo:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Atributo privado

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Fondos insuficientes")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Salida: 1300
```

---

### 5. Abstracción
La **abstracción** oculta los detalles de implementación complejos y expone solo las características esenciales. En Python, las clases base abstractas (ABCs) del módulo `abc` aplican la abstracción.

**Ejemplo:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())  # Salida: 15
```

---

### 6. Métodos Especiales (Métodos Mágicos)
Los métodos especiales (por ejemplo, `__init__`, `__str__`, `__add__`) definen el comportamiento para operaciones incorporadas como la inicialización, la representación de cadena y la sobrecarga de operadores.

**Ejemplo:**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Salida: Point(4, 6)
```

---

### 7. Métodos de Clase y Métodos Estáticos
- Los **métodos de clase** (`@classmethod`) están vinculados a la clase y pueden acceder a datos a nivel de clase.
- Los **métodos estáticos** (`@staticmethod`) son funciones de utilidad que no acceden a datos de instancia o de clase.

**Ejemplo:**
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathUtils.add(5, 3))       # Salida: 8
print(MathUtils.multiply(5, 3))  # Salida: 15
```

---

### 8. Propiedades (Getters y Setters)
Las **propiedades** proporcionan acceso controlado a los atributos utilizando el decorador `@property`, a menudo con getters y setters.

**Ejemplo:**
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        self._name = value

p = Person("Alice")
print(p.name)  # Salida: Alice
p.name = "Bob"
print(p.name)  # Salida: Bob
```

---

Esta guía proporciona una base sólida para comprender la OOP en Python. Cada concepto se demuestra con ejemplos prácticos y claros. Para más detalles, consulta la documentación oficial de Python o explora temas avanzados de OOP. ¡Feliz codificación!