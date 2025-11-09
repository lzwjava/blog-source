---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ar
layout: post
model: google/gemini-2.5-flash
title: مقدمة إلى أمثلة كود بايثون
translated: true
type: note
---

حسنًا، "بعض كود بايثون" يمكن أن يعني الكثير من الأشياء! لغة بايثون متعددة الاستخدامات بشكل لا يصدق. سأقدم لك بعض الأمثلة الشائعة، من الأمور الأساسية جدًا إلى الأمور الأكثر تعقيدًا قليلًا، والتي تغطي مفاهيم مختلفة.

---

### 1. Hello World (البداية الكلاسيكية)

هذا هو أبسط برنامج ممكن بلغة بايثون.

```python
# هذا تعليق. بايثون تتجاهل التعليقات.
print("Hello, World!")
```

**الشرح:**
*   `print()` هي دالة مضمنة تُخرج الوسيط المعطى إلى وحدة التحكم.
*   `"Hello, World!"` هو string (نص).

---

### 2. المتغيرات، العمليات الحسابية الأساسية، وإدخال المستخدم

يعرض هذا الكود كيفية تخزين البيانات في المتغيرات، وإجراء عمليات حسابية بسيطة، والحصول على مدخلات من المستخدم.

```python
# متغيرات لتخزين البيانات
name = input("What is your name? ") # الحصول على مدخلات من المستخدم
age_str = input("How old are you? ")

# تحويل العمر من string إلى integer لإجراء العمليات الحسابية
age = int(age_str)

# عمليات حسابية أساسية
year_of_birth = 2023 - age # بافتراض أن السنة الحالية هي 2023 للتبسيط
# يمكنك أيضًا استخدام: import datetime; year_of_birth = datetime.date.today().year - age

# طباعة المخرجات المُنسقة باستخدام f-string (Formatted String Literal)
print(f"Hello, {name}! You are {age} years old.")
print(f"You were likely born in {year_of_birth}.")

# فحص شرطي بسيط
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
```

**الشرح:**
*   `input()`: تطلب من المستخدم إدخال نص وتعيده كـ string.
*   `name`, `age_str`, `age`, `year_of_birth`: هذه متغيرات تخزن أنواعًا مختلفة من البيانات (string, integer).
*   `int()`: تحول string إلى integer. هذا ضروري لأن `input()` تُرجع دائمًا string، ولا يمكنك إجراء عمليات حسابية مباشرة باستخدام strings.
*   `f-strings`: طريقة ملائمة لتضمين التعبيرات داخل نص string. لاحظ `f` قبل علامة الاقتباس الافتتاحية.
*   `if/else`: عبارات تحكم في التدفق تنفذ كتلًا مختلفة من الكود بناءً على شرط.

---

### 3. القوائم (Lists) والحلقات (Loops)

القوائم هي مجموعات مرتبة من العناصر. الحلقات تُستخدم لتكرار كتلة من الكود عدة مرات.

```python
# قائمة من الفواكه
fruits = ["apple", "banana", "cherry", "date"]

print("\nMy favorite fruits:")

# التكرار خلال القائمة باستخدام حلقة 'for'
for fruit in fruits:
    print(f"- {fruit.capitalize()}") # .capitalize() تجعل الحرف الأول كبيرًا

# الوصول إلى العناصر بواسطة الفهرس (الفهارس تبدأ من الصفر)
print(f"\nThe first fruit is: {fruits[0]}")
print(f"The last fruit is: {fruits[-1]}") # الفهرس السالب يصل إلى العناصر من النهاية

# إضافة عنصر
fruits.append("elderberry")
print(f"Updated list: {fruits}")

# إزالة عنصر
fruits.remove("banana")
print(f"List after removing banana: {fruits}")

# التكرار باستخدام 'range' للحصول على الفهارس
print("\nFruits with their indices:")
for i in range(len(fruits)): # len() تعطي عدد العناصر في القائمة
    print(f"Index {i}: {fruits[i]}")
```

**الشرح:**
*   `[]`: تُستخدم لتعريف قائمة.
*   `for ... in ...`: حلقة `for` تتكرر خلال كل عنصر في تسلسل (مثل قائمة).
*   `fruit.capitalize()`: دالة string تُرجع نسخة من string بحرفها الأول كبير.
*   `fruits[0]`: تصل إلى العنصر الأول (الفهرس 0).
*   `fruits[-1]`: تصل إلى العنصر الأخير.
*   `list.append()`: تُضيف عنصرًا إلى نهاية القائمة.
*   `list.remove()`: تزيل أول ظهور للعنصر المحدد.
*   `range(len(fruits))`: يُنشئ تسلسلًا من الأرقام من 0 إلى (ولكن لا يشمل) طول القائمة، مفيد للوصول إلى العناصر بواسطة فهارسها.

---

### 4. الدوال (Functions)

الدوال هي كتل من الكود القابل لإعادة الاستخدام تؤدي مهمة محددة.

```python
# تعريف دالة تأخذ وسيطات (arguments)
def greet_person(name, age):
    """
    هذه الدالة تُحيي شخصًا وتخبره بعمره.
    من الممارسات الجيدة تضمين وصف (docstring) مثل هذا.
    """
    return f"Hello, {name}! You are {age} years old."

# استدعاء الدالة
message1 = greet_person("Alice", 30)
print(message1)

# استدعاؤها مرة أخرى بوسيطات مختلفة
message2 = greet_person("Bob", 25)
print(message2)

# تعريف دالة بمعامل افتراضي (default parameter)
def calculate_area(length, width=10):
    """تحسب مساحة المستطيل."""
    return length * width

print(f"\nArea of a 5x10 rectangle: {calculate_area(5)}") # تستخدم العرض الافتراضي
print(f"Area of a 5x7 rectangle: {calculate_area(5, 7)}") # تتجاوز العرض الافتراضي
```

**الشرح:**
*   `def`: كلمة مفتاحية لتعريف دالة.
*   `greet_person(name, age)`: اسم الدالة ومعاملاتها (مدخلاتها).
*   `return`: تُرسل قيمة مرة أخرى من الدالة.
*   الـ Docstrings (`"""Docstring goes here"""`): تشرح ما تفعله الدالة. جيدة للتوثيق.
*   `calculate_area(length, width=10)`: تُظهر معاملًا افتراضيًا. إذا لم يتم توفير `width` عند استدعاء الدالة، فسيتم استخدام القيمة الافتراضية 10.

---

### 5. القواميس (Dictionaries)

تخزن القواميس البيانات في أزواج مفتاح-قيمة (key-value). كانت غير مرتبة في إصدارات بايثون القديمة، وأصبحت مرتبة في بايثون 3.7+.

```python
# قاموس يمثل شخصًا
person = {
    "first_name": "Charlie",
    "last_name": "Smith",
    "age": 40,
    "city": "London",
    "occupations": ["Engineer", "Teacher"] # يمكن للقائمة أن تكون قيمة
}

print("\nPerson's details:")

# الوصول إلى القيم بواسطة المفتاح
print(f"Name: {person['first_name']} {person['last_name']}")
print(f"Lives in: {person.get('city', 'Unknown')}") # .get() أكثر أمانًا، تُرجع None/القيمة الافتراضية إذا لم يُوجد المفتاح
print(f"First occupation: {person['occupations'][0]}")

# تعديل قيمة
person["age"] = 41
print(f"New age: {person['age']}")

# إضافة زوج مفتاح-قيمة جديد
person["email"] = "charlie.smith@example.com"
print(f"Email: {person['email']}")

# التكرار خلال القاموس
print("\nAll keys:")
for key in person: # يتكرر خلال المفاتيح افتراضيًا
    print(key)

print("\nAll values:")
for value in person.values():
    print(value)

print("\nAll key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
```

**الشرح:**
*   `{}`: تُستخدم لتعريف قاموس.
*   `"key": value`: أزواج مفتاح-قيمة. يجب أن تكون المفاتيح فريدة وغير قابلة للتغيير (immutable) (مثل strings أو أرقام). يمكن للقيم أن تكون من أي نوع بيانات.
*   `person['key']`: تصل إلى القيمة المرتبطة بـ `key`.
*   `person.get('key', 'default_value')`: طريقة أكثر أمانًا للوصول، تتجنب `KeyError` إذا لم يكن المفتاح موجودًا، وتُرجع `default_value` بدلاً من ذلك.
*   `dict.values()`: تُرجع كائن عرض (view object) يعرض قائمة بجميع القيم في القاموس.
*   `dict.items()`: تُرجع كائن عرض يعرض قائمة بأزواج مفتاح-قيمة (كـ tuples) في القاموس.

---

هذا مجرد غيض من فيض، لكن هذه الأمثلة تغطي العديد من مفاهيم بايثون الأساسية التي ستستخدمها بشكل متكرر!