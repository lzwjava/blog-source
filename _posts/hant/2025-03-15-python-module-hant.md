---
audio: false
generated: true
lang: hant
layout: post
title: Python 模組運作原理
translated: true
type: note
---

在 Python 中，**模組**是一個包含 Python 程式碼的檔案——例如函數、類別和變數——你可以將其匯入並在其他 Python 指令碼中使用。模組是 Python 的一項基本功能，能幫助你組織程式碼、促進重用並避免重複。讓我們來探討它們的工作原理以及如何在你的專案中使用其他 Python 檔案或模組。

---

#### 什麼是模組？
模組就是一個包含 Python 程式碼的 `.py` 檔案。當你將模組匯入到另一個指令碼時，Python 會執行該檔案中的程式碼，並使其內容（函數、類別、變數等）可供你使用。Python 附帶了一個豐富的內建模組標準庫（例如 `math`、`os`、`sys`），你也可以建立自己的自訂模組。

例如，如果你有一個名為 `greetings.py` 的檔案，其中包含以下程式碼：
```python
def say_hello(name):
    print(f"Hello, {name}!")
```
這個檔案就是一個名為 `greetings` 的模組。你可以將其匯入到另一個指令碼中使用 `say_hello` 函數。

---

#### 如何使用其他 Python 檔案或模組
要使用其他 Python 檔案（模組）中的程式碼，你可以使用 `import` 語句。以下是其逐步工作原理：

1. **基本匯入**
   - 如果模組與你的指令碼位於同一目錄中，你可以透過其名稱（不包含 `.py` 副檔名）來匯入它。
   - 範例：在一個名為 `main.py` 的檔案中，你可以寫：
     ```python
     import greetings
     greetings.say_hello("Alice")
     ```
   - 執行 `main.py` 將輸出：`Hello, Alice!`
   - 使用點符號（`module_name.item_name`）來存取模組的內容。

2. **匯入特定項目**
   - 如果你只需要模組中的特定函數或變數，請使用 `from ... import ...` 語法。
   - 範例：
     ```python
     from greetings import say_hello
     say_hello("Bob")
     ```
   - 這將輸出：`Hello, Bob!`
   - 現在你可以直接使用 `say_hello`，而無需在前面加上模組名稱。

3. **使用別名匯入**
   - 你可以使用 `as` 為模組指定一個更短的名稱（別名）以方便使用。
   - 範例：
     ```python
     import greetings as g
     g.say_hello("Charlie")
     ```
   - 輸出：`Hello, Charlie!`

4. **匯入所有內容**
   - 你可以使用 `from module_name import *` 來匯入模組的所有內容，但通常不建議這樣做，因為它可能會弄亂你的命名空間並導致命名衝突。
   - 範例：
     ```python
     from greetings import *
     say_hello("Dana")
     ```
   - 輸出：`Hello, Dana!`

---

#### Python 在哪裡尋找模組？
Python 會在 `sys.path` 中定義的目錄列表中搜尋模組。這包括：
- 你正在執行的指令碼的目錄（當前目錄）。
- `PYTHONPATH` 環境變數中列出的目錄（如果已設定）。
- Python 標準庫安裝的預設位置。

如果你的模組位於不同的目錄中，你可以：
- 將其移至與你的指令碼相同的目錄。
- 以程式方式將其目錄添加到 `sys.path`：
  ```python
  import sys
  sys.path.append('/path/to/directory')
  import mymodule
  ```

---

#### 內建模組
Python 的標準庫提供了許多有用的模組，你無需自己建立即可匯入。例如：
- `import math` 讓你可以使用 `math.sqrt(16)`（返回 `4.0`）或 `math.pi`（返回 `3.14159...`）。
- `import os` 提供了與作業系統互動的函數。

---

#### 套件
**套件**是一個包含多個模組和一個特殊的 `__init__.py` 檔案（可以是空的）的目錄。例如，如果你有：
```
mypackage/
    __init__.py
    greetings.py
```
你可以這樣匯入 `greetings` 模組：
```python
import mypackage.greetings
mypackage.greetings.say_hello("Eve")
```
或者：
```python
from mypackage.greetings import say_hello
say_hello("Eve")
```

---

#### 模組是如何執行的
當你匯入一個模組時，Python 會執行該模組中的所有程式碼一次並將其快取。後續的匯入會重用快取的版本。如果模組包含頂層程式碼（例如 `print` 語句），它會在匯入期間執行。例如：
```python
# mymodule.py
print("Module is being imported!")
def my_function():
    print("Function called!")
```
```python
# main.py
import mymodule
```
執行 `main.py` 輸出：`Module is being imported!`

若要包含僅在模組直接執行（而非被匯入）時才執行的程式碼，請使用：
```python
if __name__ == "__main__":
    print("This runs only if the module is run directly!")
```
這對於測試或定義模組的主要進入點非常有用。

---

#### 範例
這是一個完整的範例：
1. 建立 `math_utils.py`：
   ```python
   def add(a, b):
       return a + b
   ```
2. 在同一目錄中建立 `main.py`：
   ```python
   import math_utils
   result = math_utils.add(3, 4)
   print(result)  # 輸出：7
   ```
3. 或者：
   ```python
   from math_utils import add
   print(add(3, 4))  # 輸出：7
   ```

---

#### 關鍵要點
- 模組是你可以匯入以重用程式碼的 Python 檔案。
- 使用 `import module_name` 以點符號存取內容，或使用 `from module_name import item` 進行直接存取。
- 模組可以是自訂檔案、內建庫模組，或是套件的一部分。
- Python 使用 `sys.path` 來尋找模組，你可以使用套件來組織較大的專案。

這涵蓋了 Python 中模組的工作原理以及如何在你的指令碼中使用其他 Python 檔案或模組的基本知識！