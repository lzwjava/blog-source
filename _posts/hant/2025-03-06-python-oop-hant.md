---
audio: false
generated: true
lang: hant
layout: post
title: Python 物件導向程式設計指南
translated: true
type: note
---

這是一份關於 Python 物件導向程式設計（OOP）的完整指南。本指南涵蓋核心概念——類別、物件、繼承、多型、封裝與抽象化——並透過實際範例逐一說明。

---

### 1. 類別與物件
**類別**是建立物件的藍圖，定義物件的屬性（資料）與方法（函式）。**物件**是類別的實例，擁有各自特定的屬性值。

**範例：**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# 建立物件
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # 輸出：Buddy says woof!
```

---

### 2. 繼承
**繼承**讓類別（子類別）能繼承另一個類別（父類別）的屬性和方法，促進程式碼重用。

**範例：**
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
print(dog.speak())  # 輸出：Buddy says woof!
print(cat.speak())  # 輸出：Whiskers says meow!
```

---

### 3. 多型
**多型**讓不同類別的物件能被視為共同父類別的實例，使方法可以互換使用。

**範例：**
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # 輸出：Buddy says woof!
animal_sound(cat)  # 輸出：Whiskers says meow!
```

---

### 4. 封裝
**封裝**限制直接存取物件的部分組件，促進資料隱藏。在 Python 中，私有屬性通常以 `_`（慣例）或 `__`（名稱改寫）作為前綴。

**範例：**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 私有屬性

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("資金不足")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # 輸出：1300
```

---

### 5. 抽象化
**抽象化**隱藏複雜的實作細節，僅暴露必要功能。在 Python 中，可透過 `abc` 模組的抽象基礎類別（ABC）強制實作抽象化。

**範例：**
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
print(rect.area())  # 輸出：15
```

---

### 6. 特殊方法（魔術方法）
特殊方法（例如 `__init__`、`__str__`、`__add__`）為內建操作定義行為，如初始化、字串表示與運算子重載。

**範例：**
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
print(p3)  # 輸出：Point(4, 6)
```

---

### 7. 類別方法與靜態方法
- **類別方法**（`@classmethod`）綁定於類別，可存取類別層級資料。
- **靜態方法**（`@staticmethod`）是不存取實例或類別資料的工具函式。

**範例：**
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathUtils.add(5, 3))       # 輸出：8
print(MathUtils.multiply(5, 3))  # 輸出：15
```

---

### 8. 屬性（Getter 與 Setter）
**屬性**透過 `@property` 裝飾器提供對屬性的受控存取，通常會搭配 getter 與 setter 使用。

**範例：**
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
            raise ValueError("姓名不能為空")
        self._name = value

p = Person("Alice")
print(p.name)  # 輸出：Alice
p.name = "Bob"
print(p.name)  # 輸出：Bob
```

---

本指南為理解 Python 物件導向程式設計奠定了堅實基礎，每個概念均配有清晰實用的範例。如需更多詳細資訊，請參閱官方 Python 文件或進一步探索進階 OOP 主題。編程愉快！