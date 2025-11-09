---
audio: false
date: 2025-09-11
generated: true
image: false
lang: hant
layout: post
model: google/gemini-2.5-flash
title: Python 程式碼範例入門
translated: true
type: note
---

好的，「一些 Python 程式碼」可以有很多意思！Python 的應用範圍非常廣泛。我將提供幾個從非常基礎到稍微複雜一些的常見範例，涵蓋不同的概念。

---

### 1. Hello World（經典入門）

這是最簡單的 Python 程式。

```python
# 這是一個註解。Python 會忽略註解。
print("Hello, World!")
```

**解釋：**
*   `print()` 是一個內建函式，會將給定的參數輸出到控制台。
*   `"Hello, World!"` 是一個字串（文字）。

---

### 2. 變數、基本算術和使用者輸入

這段程式碼展示了如何將資料儲存在變數中、執行簡單的數學運算，以及獲取使用者的輸入。

```python
# 用變數儲存資料
name = input("What is your name? ") # 獲取使用者的輸入
age_str = input("How old are you? ")

# 將年齡從字串轉換為整數以進行計算
age = int(age_str)

# 基本算術
year_of_birth = 2023 - age # 為求簡單，假設今年是 2023
# 你也可以使用：import datetime; year_of_birth = datetime.date.today().year - age

# 使用 f-string（格式化字串字面值）來輸出格式化結果
print(f"Hello, {name}! You are {age} years old.")
print(f"You were likely born in {year_of_birth}.")

# 一個簡單的條件檢查
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
```

**解釋：**
*   `input()`: 提示使用者輸入文字，並以字串形式返回。
*   `name`, `age_str`, `age`, `year_of_birth`: 這些是儲存不同類型資料（字串、整數）的變數。
*   `int()`: 將字串轉換為整數。這是必要的，因為 `input()` 總是返回字串，而你不能直接用字串進行數學運算。
*   `f-strings`: 一種將表達式嵌入字串字面值的便捷方式。請注意開頭引號前的 `f`。
*   `if/else`: 控制流程語句，根據條件執行不同的程式碼區塊。

---

### 3. 列表和迴圈

列表是有序的項目集合。迴圈用於重複執行一段程式碼多次。

```python
# 一個水果列表
fruits = ["apple", "banana", "cherry", "date"]

print("\nMy favorite fruits:")

# 使用 'for' 迴圈遍歷列表
for fruit in fruits:
    print(f"- {fruit.capitalize()}") # .capitalize() 將第一個字母轉為大寫

# 透過索引存取元素（列表的索引從 0 開始）
print(f"\nThe first fruit is: {fruits[0]}")
print(f"The last fruit is: {fruits[-1]}") # 負數索引從末端開始存取

# 新增一個元素
fruits.append("elderberry")
print(f"Updated list: {fruits}")

# 移除一個元素
fruits.remove("banana")
print(f"List after removing banana: {fruits}")

# 使用 'range' 迴圈來取得索引
print("\nFruits with their indices:")
for i in range(len(fruits)): # len() 給出列表中的項目數量
    print(f"Index {i}: {fruits[i]}")
```

**解釋：**
*   `[]`: 用於定義列表。
*   `for ... in ...`: 一個 `for` 迴圈，遍歷序列（如列表）中的每個項目。
*   `fruit.capitalize()`: 一個字串方法，返回首字母大寫的字串副本。
*   `fruits[0]`: 存取第一個元素（索引 0）。
*   `fruits[-1]`: 存取最後一個元素。
*   `list.append()`: 將一個項目添加到列表的末尾。
*   `list.remove()`: 移除第一個符合指定項目的項目。
*   `range(len(fruits))`: 生成一個從 0 到列表長度（不包括）的數字序列，用於透過索引存取元素。

---

### 4. 函式

函式是執行特定任務的可重複使用程式碼區塊。

```python
# 定義一個帶有參數的函式
def greet_person(name, age):
    """
    This function greets a person and tells them their age.
    It's a good practice to include a docstring like this.
    """
    return f"Hello, {name}! You are {age} years old."

# 呼叫函式
message1 = greet_person("Alice", 30)
print(message1)

# 使用不同的參數再次呼叫
message2 = greet_person("Bob", 25)
print(message2)

# 定義一個帶有預設參數的函式
def calculate_area(length, width=10):
    """Calculates the area of a rectangle."""
    return length * width

print(f"\nArea of a 5x10 rectangle: {calculate_area(5)}") # 使用預設寬度
print(f"Area of a 5x7 rectangle: {calculate_area(5, 7)}") # 覆蓋預設寬度
```

**解釋：**
*   `def`: 定義函式的關鍵字。
*   `greet_person(name, age)`: 函式名稱及其參數（輸入）。
*   `return`: 從函式返回一個值。
*   Docstrings (`"""Docstring goes here"""`): 解釋函式的作用。對撰寫文件很有幫助。
*   `calculate_area(length, width=10)`: 展示預設參數。如果在呼叫函式時未提供 `width`，則預設為 10。

---

### 5. 字典

字典以鍵值對的形式儲存資料。它們是無序的（在舊版 Python 中，Python 3.7+ 後為有序）。

```python
# 一個代表一個人的字典
person = {
    "first_name": "Charlie",
    "last_name": "Smith",
    "age": 40,
    "city": "London",
    "occupations": ["Engineer", "Teacher"] # 列表可以作為值
}

print("\nPerson's details:")

# 透過鍵來存取值
print(f"Name: {person['first_name']} {person['last_name']}")
print(f"Lives in: {person.get('city', 'Unknown')}") # .get() 更安全，如果找不到鍵則返回 None/預設值
print(f"First occupation: {person['occupations'][0]}")

# 修改一個值
person["age"] = 41
print(f"New age: {person['age']}")

# 新增一個鍵值對
person["email"] = "charlie.smith@example.com"
print(f"Email: {person['email']}")

# 遍歷字典
print("\nAll keys:")
for key in person: # 預設遍歷鍵
    print(key)

print("\nAll values:")
for value in person.values():
    print(value)

print("\nAll key-value pairs:")
for key, value in person.items():
    print(f"{key}: {value}")
```

**解釋：**
*   `{}`: 用於定義字典。
*   `"key": value`: 鍵值對。鍵必須是唯一且不可變的（如字串或數字）。值可以是任何資料類型。
*   `person['key']`: 存取與 `key` 關聯的值。
*   `person.get('key', 'default_value')`: 一種更安全的存取方式，如果鍵不存在，可以避免 `KeyError`，轉而返回 `default_value`。
*   `dict.values()`: 返回一個視圖物件，顯示字典中所有值的列表。
*   `dict.items()`: 返回一個視圖物件，顯示字典中所有鍵值對元組的列表。

---

這僅僅是觸及皮毛，但這些範例涵蓋了許多你將會經常使用的基本 Python 概念！