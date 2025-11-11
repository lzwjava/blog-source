---
audio: false
generated: true
lang: hi
layout: post
title: पायथन गाइड
translated: true
type: note
---

यहाँ स्ट्रिंग ऑपरेशन्स, गणित, टेक्स्ट प्रोसेसिंग, I/O, फ़ाइल हैंडलिंग, नेटवर्किंग, कलेक्शन्स और मल्टीथ्रेडिंग को कवर करने वाली एक संक्षिप्त Python गाइड दी गई है। प्रत्येक खंड में एक संक्षिप्त अवलोकन और व्यावहारिक उदाहरण शामिल हैं ताकि आपको शुरुआत करने या अपनी जानकारी ताज़ा करने में मदद मिल सके।

---

## Python गाइड: आवश्यक विषय

### 1. स्ट्रिंग ऑपरेशन्स (String Operations)
Python में स्ट्रिंग्स वर्णों के अपरिवर्तनीय अनुक्रम होते हैं। आप इनमें हेरफेर के लिए संयोजन, पुनरावृत्ति, स्लाइसिंग जैसे ऑपरेशन और बिल्ट-इन मेथड्स का उपयोग कर सकते हैं।

**उदाहरण:**
```python
# संयोजन और पुनरावृत्ति
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # आउटपुट: Hello World
print(s1 * 3)         # आउटपुट: HelloHelloHello

# स्लाइसिंग
print(s1[1:4])        # आउटपुट: ell

# बिल्ट-इन मेथड्स
print(s1.upper())     # आउटपुट: HELLO
print(s2.lower())     # आउटपुट: world
print("  hi  ".strip())  # आउटपुट: hi
print("a,b,c".split(','))  # आउटपुट: ['a', 'b', 'c']
print(','.join(['a', 'b', 'c']))  # आउटपुट: a,b,c

# f-strings के साथ स्ट्रिंग फ़ॉर्मेटिंग
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # आउटपुट: My name is Alice and I am 30 years old.
```

---

### 2. गणित (Math)
`math` मॉड्यूल सामान्य गणनाओं के लिए गणितीय फ़ंक्शन और स्थिरांक प्रदान करता है।

**उदाहरण:**
```python
import math

print(math.sqrt(16))    # आउटपुट: 4.0
print(math.pow(2, 3))   # आउटपुट: 8.0
print(math.sin(math.pi / 2))  # आउटपुट: 1.0
print(math.pi)          # आउटपुट: 3.141592653589793
```

---

### 3. टेक्स्ट प्रोसेसिंग (Regular Expressions)
`re` मॉड्यूल रेगुलर एक्सप्रेशन का उपयोग करके पैटर्न मिलान और टेक्स्ट हेरफेर सक्षम करता है।

**उदाहरण:**
```python
import re

text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())  # आउटपुट: Found: rain

# सभी 4-अक्षर वाले शब्द ढूँढें
print(re.findall(r"\b\w{4}\b", text))  # आउटपुट: ['rain', 'Spain']
```

---

### 4. I/O (इनपुट और आउटपुट)
बेसिक इनपुट और आउटपुट ऑपरेशन उपयोगकर्ता के साथ इंटरैक्शन की अनुमति देते हैं।

**उदाहरण:**
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

### 5. फ़ाइल हैंडलिंग (File Handling)
Python `open()` फ़ंक्शन का उपयोग करके फ़ाइलों को पढ़ने और लिखने को सरल बनाता है, स्वचालित फ़ाइल क्लोजर के लिए `with` स्टेटमेंट की सिफारिश की जाती है।

**उदाहरण:**
```python
# एक फ़ाइल में लिखना
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")

# एक फ़ाइल से पढ़ना
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # आउटपुट: Hello, World!
```

---

### 6. नेटवर्किंग (Networking)
`requests` लाइब्रेरी (`pip install requests` के साथ इंस्टॉल करें) HTTP रिक्वेस्ट को सीधा बनाती है।

**उदाहरण:**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # आउटपुट: 200
print(response.json())       # आउटपुट: GitHub API से JSON डेटा
```

---

### 7. कलेक्शन्स (Collections)
`collections` मॉड्यूल विशेष डेटा स्ट्रक्चर जैसे `Counter`, `deque`, `namedtuple` आदि प्रदान करता है। यहाँ `Counter` के साथ एक उदाहरण दिया गया है।

**उदाहरण:**
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry"]
word_count = Counter(words)
print(word_count)  # आउटपुट: Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

**अन्य कलेक्शन्स:**
- `namedtuple`: नामित फ़ील्ड्स वाले टपल सबक्लास बनाता है।
- `deque`: दोनों सिरों से कुशलता से एपेंड/पॉप के लिए डबल-एंडेड क्यू।
- `OrderedDict`: वह डिक्शनरी जो सम्मिलन क्रम याद रखती है।
- `defaultdict`: गायब कुंजियों के लिए डिफ़ॉल्ट मान वाला डिक्शनरी।

---

### 8. मल्टीथ्रेडिंग (Multithreading)
`threading` मॉड्यूल समवर्ती टास्क निष्पादन सक्षम करता है, जो I/O-बाउंड ऑपरेशन्स के लिए आदर्श है।

**उदाहरण:**
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# एक थ्रेड बनाएं और शुरू करें
t = threading.Thread(target=print_numbers)
t.start()

# मुख्य थ्रेड जारी रहती है
print("Main thread finished")
```

---

यह गाइड व्यावहारिक उदाहरणों के साथ प्रत्येक विषय के लिए एक प्रारंभिक बिंदु प्रदान करती है। अधिक गहन सीखने के लिए, आधिकारिक Python डॉक्यूमेंटेशन या विशेष संसाधनों से सलाह लें। हैप्पी कोडिंग!