---
audio: false
generated: true
lang: fr
layout: post
title: Guide POO Python
translated: true
type: note
---

Voici un guide complet sur la Programmation Orientée Objet (POO) en Python. Ce guide couvre les concepts fondamentaux — classes, objets, héritage, polymorphisme, encapsulation et abstraction — ainsi que des exemples pratiques pour illustrer chacun d'eux.

---

### 1. Classes et Objets
Une **classe** est un plan pour créer des objets, définissant leurs attributs (données) et méthodes (fonctions). Un **objet** est une instance d'une classe, avec ses propres valeurs spécifiques pour les attributs.

**Exemple :**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} dit ouaf !")

# Création d'un objet
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # Sortie : Buddy dit ouaf !
```

---

### 2. Héritage
L'**héritage** permet à une classe (classe enfant) d'hériter des attributs et des méthodes d'une autre classe (classe parent), favorisant la réutilisation du code.

**Exemple :**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} dit ouaf !"

class Cat(Animal):
    def speak(self):
        return f"{self.name} dit miaou !"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Sortie : Buddy dit ouaf !
print(cat.speak())  # Sortie : Whiskers dit miaou !
```

---

### 3. Polymorphisme
Le **polymorphisme** permet de traiter des objets de différentes classes comme des instances d'une superclasse commune, permettant d'utiliser les méthodes de manière interchangeable.

**Exemple :**
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # Sortie : Buddy dit ouaf !
animal_sound(cat)  # Sortie : Whiskers dit miaou !
```

---

### 4. Encapsulation
L'**encapsulation** restreint l'accès direct à certains composants de l'objet, favorisant la dissimulation des données. En Python, les attributs privés sont généralement préfixés par `_` (convention) ou `__` (name mangling).

**Exemple :**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Attribut privé

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Fonds insuffisants")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Sortie : 1300
```

---

### 5. Abstraction
L'**abstraction** masque les détails d'implémentation complexes et n'expose que les fonctionnalités essentielles. En Python, les classes de base abstraites (ABC) du module `abc` imposent l'abstraction.

**Exemple :**
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
print(rect.area())  # Sortie : 15
```

---

### 6. Méthodes Spéciales (Méthodes Magiques)
Les méthodes spéciales (par exemple, `__init__`, `__str__`, `__add__`) définissent le comportement des opérations intégrées comme l'initialisation, la représentation sous forme de chaîne et la surcharge d'opérateurs.

**Exemple :**
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
print(p3)  # Sortie : Point(4, 6)
```

---

### 7. Méthodes de Classe et Méthodes Statiques
- Les **méthodes de classe** (`@classmethod`) sont liées à la classe et peuvent accéder aux données au niveau de la classe.
- Les **méthodes statiques** (`@staticmethod`) sont des fonctions utilitaires qui n'accèdent pas aux données d'instance ou de classe.

**Exemple :**
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathUtils.add(5, 3))       # Sortie : 8
print(MathUtils.multiply(5, 3))  # Sortie : 15
```

---

### 8. Propriétés (Accesseurs et Mutateurs)
Les **propriétés** fournissent un accès contrôlé aux attributs en utilisant le décorateur `@property`, souvent avec des accesseurs (getters) et des mutateurs (setters).

**Exemple :**
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
            raise ValueError("Le nom ne peut pas être vide")
        self._name = value

p = Person("Alice")
print(p.name)  # Sortie : Alice
p.name = "Bob"
print(p.name)  # Sortie : Bob
```

---

Ce guide fournit une base solide pour comprendre la POO en Python. Chaque concept est démontré avec des exemples pratiques et clairs. Pour plus de détails, consultez la documentation officielle de Python ou explorez des sujets avancés de POO. Bon codage !