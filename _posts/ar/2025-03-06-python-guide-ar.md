---
audio: false
generated: true
lang: ar
layout: post
title: دليل بايثون
translated: true
type: note
---

هذا دليل موجز لـ Python يغطي عمليات السلسلة النصية، الرياضيات، معالجة النصوص، الإدخال/الإخراج، التعامل مع الملفات، الشبكات، المجموعات، والبرمجة متعددة الخيوط. يحتوي كل قسم على نظرة عامة مختصرة وأمثلة عملية لمساعدتك على البدء أو تجديد معرفتك.

---

## دليل Python: مواضيع أساسية

### 1. عمليات السلسلة النصية (String Operations)
السلاسل النصية في Python هي تسلسلات غير قابلة للتغيير من الأحرف. يمكنك إجراء عمليات مثل التسلسل، التكرار، التقطيع، واستخدام الطرق المدمجة للتلاعب.

**أمثلة:**
```python
# التسلسل والتكرار
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # الإخراج: Hello World
print(s1 * 3)         # الإخراج: HelloHelloHello

# التقطيع
print(s1[1:4])        # الإخراج: ell

# الطرق المدمجة
print(s1.upper())     # الإخراج: HELLO
print(s2.lower())     # الإخراج: world
print("  hi  ".strip())  # الإخراج: hi
print("a,b,c".split(','))  # الإخراج: ['a', 'b', 'c']
print(','.join(['a', 'b', 'c']))  # الإخراج: a,b,c

# تنسيق السلسلة النصية باستخدام f-strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # الإخراج: My name is Alice and I am 30 years old.
```

---

### 2. الرياضيات (Math)
توفر وحدة `math` دوال وثوابت رياضية للحسابات الشائعة.

**مثال:**
```python
import math

print(math.sqrt(16))    # الإخراج: 4.0
print(math.pow(2, 3))   # الإخراج: 8.0
print(math.sin(math.pi / 2))  # الإخراج: 1.0
print(math.pi)          # الإخراج: 3.141592653589793
```

---

### 3. معالجة النصوص (التعبيرات النمطية)
تمكّن وحدة `re` من مطابقة الأنماط ومعالجة النصوص باستخدام التعبيرات النمطية.

**مثال:**
```python
import re

text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())  # الإخراج: Found: rain

# العثور على جميع الكلمات المكونة من 4 أحرف
print(re.findall(r"\b\w{4}\b", text))  # الإخراج: ['rain', 'Spain']
```

---

### 4. الإدخال والإخراج (I/O)
تسمح عمليات الإدخال والإخراج الأساسية بالتفاعل مع المستخدم.

**مثال:**
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

### 5. التعامل مع الملفات (File Handling)
تبسط Python القراءة من والكتابة إلى الملفات باستخدام الدالة `open()`، مع التوصية باستخدام عبارة `with` للإغلاق التلقائي للملف.

**مثال:**
```python
# الكتابة إلى ملف
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")

# القراءة من ملف
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # الإخراج: Hello, World!
```

---

### 6. الشبكات (Networking)
تجعل مكتبة `requests` (يتم تثبيتها بـ `pip install requests`) طلبات HTTP مباشرة.

**مثال:**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # الإخراج: 200
print(response.json())       # الإخراج: بيانات JSON من GitHub API
```

---

### 7. المجموعات (Collections)
تقدم وحدة `collections` هياكل بيانات متخصصة مثل `Counter`، `deque`، `namedtuple`، إلخ. إليك مثال باستخدام `Counter`.

**مثال:**
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry"]
word_count = Counter(words)
print(word_count)  # الإخراج: Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

**مجموعات أخرى:**
- `namedtuple`: ينشئ فئات فرعية من tuple تحتوي على حقول مسماة.
- `deque`: طابور ذو طرفين لإلحاق/إزالة فعالة من كلا الطرفين.
- `OrderedDict`: قاموس يتذكر ترتيب الإدراج.
- `defaultdict`: قاموس بقيمة افتراضية للمفاتيح المفقودة.

---

### 8. البرمجة متعددة الخيوط (Multithreading)
تمكّن وحدة `threading` من تنفيذ المهام المتزامنة، وهي مثالية للعمليات المرتبطة بـ I/O.

**مثال:**
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# إنشاء وتشغيل خيط
t = threading.Thread(target=print_numbers)
t.start()

# الخيط الرئيسي يستمر
print("Main thread finished")
```

---

يوفر هذا الدليل نقطة بداية لكل موضوع مع أمثلة عملية. لمزيد من التعلم المتعمق، استشر وثائق Python الرسمية أو المصادر المتخصصة. ترميزًا سعيدًا!