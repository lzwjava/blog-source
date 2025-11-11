---
audio: false
generated: true
lang: ar
layout: post
title: دليل البرمجة كائنية التوجه في بايثون
translated: true
type: note
---

إليك دليلًا شاملاً للبرمجة كائنية التوجه (OOP) في Python. يغطي هذا الدليل المفاهيم الأساسية — الفئات، الكائنات، الوراثة، تعدد الأشكال، التغليف، والتجريد — مع أمثلة عملية لتوضيح كل مفهوم.

---

### 1. الفئات والكائنات
**الفئة** هي مخطط لإنشاء الكائنات، تحدد سماتها (البيانات) وطرقها (الدوال). **الكائن** هو نسخة من فئة، له قيمه الخاصة للسمات.

**مثال:**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# إنشاء كائن
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # المخرجات: Buddy says woof!
```

---

### 2. الوراثة
تسمح **الوراثة** لفئة (فئة فرعية) بأن ترث السمات والطرق من فئة أخرى (فئة أصلية)، مما يعزز إعادة استخدام الكود.

**مثال:**
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
print(dog.speak())  # المخرجات: Buddy says woof!
print(cat.speak())  # المخرجات: Whiskers says meow!
```

---

### 3. تعدد الأشكال
يسمح **تعدد الأشكال** للمتعامل مع كائنات من فئات مختلفة على أنها نسخ من فئة أصل مشتركة، مما يسمح باستخدام الطرق بالتبادل.

**مثال:**
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # المخرجات: Buddy says woof!
animal_sound(cat)  # المخرجات: Whiskers says meow!
```

---

### 4. التغليف
يقيد **التغليف** الوصول المباشر إلى بعض مكونات الكائن، مما يعزز إخفاء البيانات. في Python، عادةً تُسبق السمات الخاصة بـ `_` (اتفاقية) أو `__` (تحريف الاسم).

**مثال:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # سمة خاصة

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # المخرجات: 1300
```

---

### 5. التجريد
يخفي **التجريد** تفاصيل التنفيذ المعقدة ويعرض الميزات الأساسية فقط. في Python، تفرض الفئات الأساسية المجردة (ABCs) من وحدة `abc` التجريد.

**مثال:**
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
print(rect.area())  # المخرجات: 15
```

---

### 6. الطرق الخاصة (الطرق السحرية)
الطرق الخاصة (مثل `__init__`، `__str__`، `__add__`) تحدد السلوك للعمليات المضمنة مثل التهيئة، تمثيل السلسلة، والتحميل الزائد للعامل.

**مثال:**
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
print(p3)  # المخرجات: Point(4, 6)
```

---

### 7. طرق الفئة والطرق الساكنة
- **طرق الفئة** (`@classmethod`) ترتبط بالفئة ويمكنها الوصول إلى بيانات مستوى الفئة.
- **الطرق الساكنة** (`@staticmethod`) هي دوال مساعدة لا تصل إلى بيانات النسخة أو الفئة.

**مثال:**
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathUtils.add(5, 3))       # المخرجات: 8
print(MathUtils.multiply(5, 3))  # المخرجات: 15
```

---

### 8. الخصائص (الجامعات والمعدّلات)
توفر **الخصائص** وصولاً خاضعًا للتحكم إلى السمات باستخدام مُزخرف `@property`، غالبًا مع جامعات ومعدّلات.

**مثال:**
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
            raise ValueError("Name cannot be empty")
        self._name = value

p = Person("Alice")
print(p.name)  # المخرجات: Alice
p.name = "Bob"
print(p.name)  # المخرجات: Bob
```

---

يوفر هذا الدليل أساسًا متينًا لفهم البرمجة كائنية التوجه في Python. يتم توضيح كل مفهوم بأمثلة عملية واضحة. لمزيد من التفاصيل، راجع التوثيق الرسمي لـ Python أو استكشف مواضيع البرمجة كائنية التوجه المتقدمة. تمنياتنا بالبرمجة الممتعة!