---
audio: false
generated: true
lang: hant
layout: post
title: Python 指南
translated: true
type: note
---

這是一份簡明的 Python 指南，涵蓋字串操作、數學運算、文字處理、輸入輸出、檔案處理、網路通訊、集合與多執行緒。每個章節都包含簡要概述與實用範例，幫助您快速入門或複習相關知識。

---

## Python 指南：核心主題

### 1. 字串操作
Python 中的字串是不可變的字元序列。您可以進行連接、重複、切片等操作，並使用內建方法進行處理。

**範例：**
```python
# 連接與重複
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # 輸出：Hello World
print(s1 * 3)         # 輸出：HelloHelloHello

# 切片
print(s1[1:4])        # 輸出：ell

# 內建方法
print(s1.upper())     # 輸出：HELLO
print(s2.lower())     # 輸出：world
print("  hi  ".strip())  # 輸出：hi
print("a,b,c".split(','))  # 輸出：['a', 'b', 'c']
print(','.join(['a', 'b', 'c']))  # 輸出：a,b,c

# 使用 f-strings 進行字串格式化
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # 輸出：My name is Alice and I am 30 years old.
```

---

### 2. 數學運算
`math` 模組提供常見計算所需的數學函數與常數。

**範例：**
```python
import math

print(math.sqrt(16))    # 輸出：4.0
print(math.pow(2, 3))   # 輸出：8.0
print(math.sin(math.pi / 2))  # 輸出：1.0
print(math.pi)          # 輸出：3.141592653589793
```

---

### 3. 文字處理（正規表示式）
`re` 模組透過正規表示式實現模式匹配與文字處理功能。

**範例：**
```python
import re

text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())  # 輸出：Found: rain

# 尋找所有 4 字母單詞
print(re.findall(r"\b\w{4}\b", text))  # 輸出：['rain', 'Spain']
```

---

### 4. 輸入輸出
基礎的輸入輸出操作可實現與使用者的互動。

**範例：**
```python
name = input("請輸入您的姓名：")
print("Hello, " + name + "!")
```

---

### 5. 檔案處理
Python 透過 `open()` 函數簡化檔案讀寫，建議使用 `with` 語句實現自動關閉檔案。

**範例：**
```python
# 寫入檔案
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")

# 讀取檔案
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # 輸出：Hello, World!
```

---

### 6. 網路通訊
使用 `requests` 程式庫（透過 `pip install requests` 安裝）可輕鬆處理 HTTP 請求。

**範例：**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 輸出：200
print(response.json())       # 輸出：來自 GitHub API 的 JSON 資料
```

---

### 7. 集合
`collections` 模組提供特化資料結構，例如 `Counter`、`deque`、`namedtuple` 等。以下為 `Counter` 使用範例。

**範例：**
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry"]
word_count = Counter(words)
print(word_count)  # 輸出：Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

**其他集合類型：**
- `namedtuple`：建立具名字段的 tuple 子類別
- `deque`：雙端隊列，可高效進行兩端的添加/刪除操作
- `OrderedDict`：記住插入順序的字典
- `defaultdict`：為缺失鍵提供預設值的字典

---

### 8. 多執行緒
`threading` 模組可實現並行任務執行，特別適用於 I/O 密集型操作。

**範例：**
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# 建立並啟動執行緒
t = threading.Thread(target=print_numbers)
t.start()

# 主執行緒繼續執行
print("主執行緒執行完畢")
```

---

本指南透過實用範例為各主題提供入門指引。如需深入學習，請參閱官方 Python 文檔或專業學習資源。編程愉快！