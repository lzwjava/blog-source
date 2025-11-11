---
audio: false
generated: true
lang: hi
layout: post
title: पायथन ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग गाइड
translated: true
type: note
---

यहाँ पायथन में ऑब्जेक्ट-ओरिएंटेड प्रोग्रामिंग (OOP) का एक व्यापक मार्गदर्शक है। यह मार्गदर्शक मूलभूत अवधारणाओं—क्लासेस, ऑब्जेक्ट्स, इनहेरिटेंस, पॉलीमॉर्फिज्म, एनकैप्सुलेशन, और एब्स्ट्रक्शन—को कवर करता है, साथ ही प्रत्येक को समझाने के लिए व्यावहारिक उदाहरण भी प्रस्तुत करता है।

---

### 1. क्लासेस और ऑब्जेक्ट्स
एक **क्लास** ऑब्जेक्ट्स बनाने के लिए एक ब्लूप्रिंट होती है, जो उनकी विशेषताओं (डेटा) और मेथड्स (फंक्शन्स) को परिभाषित करती है। एक **ऑब्जेक्ट** क्लास का एक उदाहरण (इंस्टेंस) होता है, जिसकी विशेषताओं के लिए अपने स्वयं के विशिष्ट मान होते हैं।

**उदाहरण:**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

# एक ऑब्जेक्ट बनाना
my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # आउटपुट: Buddy says woof!
```

---

### 2. इनहेरिटेंस (विरासत)
**इनहेरिटेंस** एक क्लास (चाइल्ड क्लास) को दूसरी क्लास (पैरेंट क्लास) से विशेषताएँ और मेथड्स प्राप्त करने की अनुमति देती है, जिससे कोड का पुन: उपयोग बढ़ता है।

**उदाहरण:**
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
print(dog.speak())  # आउटपुट: Buddy says woof!
print(cat.speak())  # आउटपुट: Whiskers says meow!
```

---

### 3. पॉलीमॉर्फिज्म (बहुरूपता)
**पॉलीमॉर्फिज्म** विभिन्न क्लासेस के ऑब्जेक्ट्स को एक सामान्य सुपरक्लास के उदाहरणों के रूप में व्यवहार करने में सक्षम बनाता है, जिससे मेथड्स को आपस में बदले जाने की अनुमति मिलती है।

**उदाहरण:**
```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # आउटपुट: Buddy says woof!
animal_sound(cat)  # आउटपुट: Whiskers says meow!
```

---

### 4. एनकैप्सुलेशन (पैकेजिंग)
**एनकैप्सुलेशन** कुछ ऑब्जेक्ट घटकों तक सीधी पहुँच को प्रतिबंधित करता है, जिससे डेटा छुपाने को बढ़ावा मिलता है। पायथन में, प्राइवेट विशेषताओं को आमतौर पर `_` (परंपरा) या `__` (नेम मैंगलिंग) के साथ उपसर्गित किया जाता है।

**उदाहरण:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # प्राइवेट विशेषता

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
print(account.get_balance())  # आउटपुट: 1300
```

---

### 5. एब्स्ट्रक्शन (अमूर्तन)
**एब्स्ट्रक्शन** जटिल कार्यान्वयन विवरणों को छुपाता है और केवल आवश्यक सुविधाओं को ही प्रकट करता है। पायथन में, `abc` मॉड्यूल से एब्स्ट्रक्ट बेस क्लासेस (ABCs) एब्स्ट्रक्शन को लागू करती हैं।

**उदाहरण:**
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
print(rect.area())  # आउटपुट: 15
```

---

### 6. स्पेशल मेथड्स (मैजिक मेथड्स)
स्पेशल मेथड्स (जैसे, `__init__`, `__str__`, `__add__`) बिल्ट-इन ऑपरेशन्स जैसे इनिशियलाइज़ेशन, स्ट्रिंग रिप्रेजेंटेशन, और ऑपरेटर ओवरलोडिंग के लिए व्यवहार को परिभाषित करते हैं।

**उदाहरण:**
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
print(p3)  # आउटपुट: Point(4, 6)
```

---

### 7. क्लास और स्टैटिक मेथड्स
- **क्लास मेथड्स** (`@classmethod`) क्लास से बंधे होते हैं और क्लास-लेवल डेटा तक पहुँच सकते हैं।
- **स्टैटिक मेथड्स** (`@staticmethod`) उपयोगिता फंक्शन्स होते हैं जो इंस्टेंस या क्लास डेटा तक नहीं पहुँचते हैं।

**उदाहरण:**
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return a * b

print(MathUtils.add(5, 3))       # आउटपुट: 8
print(MathUtils.multiply(5, 3))  # आउटपुट: 15
```

---

### 8. प्रॉपर्टीज (गेटर्स और सेटर्स)
**प्रॉपर्टीज** `@property` डेकोरेटर का उपयोग करके विशेषताओं तक नियंत्रित पहुँच प्रदान करती हैं, जिसमें अक्सर गेटर्स और सेटर्स शामिल होते हैं।

**उदाहरण:**
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
print(p.name)  # आउटपुट: Alice
p.name = "Bob"
print(p.name)  # आउटपुट: Bob
```

---

यह मार्गदर्शक पायथन में OOP को समझने के लिए एक मजबूत आधार प्रदान करता है। प्रत्येक अवधारणा को स्पष्ट, व्यावहारिक उदाहरणों के साथ प्रदर्शित किया गया है। अधिक जानकारी के लिए, आधिकारिक पायथन डॉक्यूमेंटेशन देखें या उन्नत OOP विषयों का पता लगाएं। हैप्पी कोडिंग!