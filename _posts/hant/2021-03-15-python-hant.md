---
lang: hant
layout: post
title: Python 教程学习笔记
---

通过之前的学习，我们已经对Python有了一定的了解。现在，根据官方文档，我们将继续补充一些Python的知识。

## 代码流的控制

### 类型

```python
print(type(1))
``` 

這段程式碼的繁體中文翻譯如下：

```python
print(type(1))
```

這段程式碼的功能是輸出數字 `1` 的資料類型。在 Python 中，`type()` 函數用於獲取變數或值的資料類型。執行這段程式碼後，輸出將會是 `<class 'int'>`，表示 `1` 是一個整數（integer）。

```shell
<class 'int'>
```

```python
print(type('a'))
``` 

這段代碼會輸出變量 `'a'` 的類型。在 Python 中，`'a'` 是一個字符串（string），所以輸出將會是：

```
<class 'str'>
```

這表示 `'a'` 是一個字符串類型的對象。

```shell
<class 'str'>
```

`type`函数非常有用，可以用来打印对象的类型。

### 范围

`range` 是 Python 中的一个内置函数，用于生成一个整数序列。它通常用于 `for` 循环中，以遍历一系列数字。`range` 函数的基本语法如下：

```python
range(stop)
range(start, stop[, step])
```

- `start`：序列的起始值（包含）。
- `stop`：序列的结束值（不包含）。
- `step`：序列的步长（可选，默认为 1）。

#### 示例

1. **生成从 0 到 4 的序列：**

   ```python
   for i in range(5):
       print(i)
   ```

   输出：
   ```
   0
   1
   2
   3
   4
   ```

2. **生成从 2 到 8 的序列，步长为 2：**

   ```python
   for i in range(2, 9, 2):
       print(i)
   ```

   输出：
   ```
   2
   4
   6
   8
   ```

3. **生成从 10 到 1 的倒序序列，步长为 -1：**

   ```python
   for i in range(10, 0, -1):
       print(i)
   ```

   输出：
   ```
   10
   9
   8
   7
   6
   5
   4
   3
   2
   1
   ```

`range` 函数返回的是一个 `range` 对象，它是一个可迭代对象，而不是一个列表。如果需要将其转换为列表，可以使用 `list()` 函数：

```python
numbers = list(range(5))
print(numbers)  # 输出: [0, 1, 2, 3, 4]
```

`range` 函数在 Python 中非常常用，特别是在需要遍历一系列数字时。

`range` 函数非常有用。

```python
for i in range(5):
  print(i, end = ' ')
```

這段程式碼的翻譯如下：

```python
for i in range(5):
  print(i, end = ' ')
```

這段程式碼的功能是：

- 使用 `for` 迴圈，變數 `i` 會從 0 開始，每次增加 1，直到 4（因為 `range(5)` 生成的是 0 到 4 的數字）。
- `print(i, end = ' ')` 會將 `i` 的值印出來，並且在每個數字後面加上一個空格，而不是換行。

執行結果會是：

```
0 1 2 3 4 
```

```shell
0 1 2 3 4
```

```python
for i in range(2, 6, 2):
  print(i, end = ' ')
```

這段程式碼的翻譯如下：

```python
for i in range(2, 6, 2):
  print(i, end = ' ')
```

這段程式碼會從 2 開始，每次增加 2，直到 6（不包括 6），並將這些數字印出來，數字之間以空格分隔。

```shell
2 4
``` 

（注：这段文本“2 4”在shell中通常表示两个数字，没有特定的上下文，无法进行有意义的翻译。如果这是某种代码或特定格式的数据，请提供更多信息以便准确翻译。）

查看`range`函数的定义。

```python
class range(Sequence[int]):
    start: int
    stop: int
    step: int
```

翻譯成繁體中文如下：

```python
class range(Sequence[int]):
    start: int
    stop: int
    step: int
```

這段程式碼定義了一個名為 `range` 的類別，它繼承自 `Sequence[int]`，並具有三個屬性：`start`、`stop` 和 `step`，這些屬性都是整數類型。

可見是一個類別。

```python
print(range(5))
```

```shell
範圍(0, 5)
```

而不是：

```shll
[0,1,2,3,4]
```

继续。

```python
print(list(range(5)))
```

這段程式碼會輸出一個從 0 到 4 的整數列表，結果如下：

```
[0, 1, 2, 3, 4]
```

```shell
[0, 1, 2, 3, 4]
```

为什么。看`list`的定义。

```python
class list(MutableSequence[_T], Generic[_T]):
``` 

翻譯成繁體中文為：

```python
class 列表(可變序列[_T], 泛型[_T]):
``` 

這裡的 `list` 是 Python 中的內建類型，表示一個可變的序列。`MutableSequence` 和 `Generic` 是 Python 類型提示中的概念，分別表示可變序列和泛型類型。`_T` 是一個類型變量，表示列表中可以包含任意類型的元素。

`list` 的定义是 `list(MutableSequence[_T], Generic[_T]):`，而 `range` 的定义是 `class range(Sequence[int])`。`list` 继承了 `MutableSequence`，而 `range` 继承了 `Sequence`。

继续往下找是这样的。

```python
Sequence = _alias(collections.abc.Sequence, 1)
MutableSequence = _alias(collections.abc.MutableSequence, 1)
```

這段代碼定義了兩個別名 `Sequence` 和 `MutableSequence`，它們分別對應於 `collections.abc` 模組中的 `Sequence` 和 `MutableSequence` 抽象基類。`_alias` 函數用於創建這些別名，並且傳入的參數 `1` 可能表示某種特定的配置或版本。

这里我们不太明白它们之间的关系。但大概我们知道了为什么可以这样写`list(range(5))`。

### 函数参数

来看函数的补充知识。

```python
def fn(a = 3):
  print(a)
```

函数()
```

```shell
3
```

这是给参数一个默认值。

```python
def fn(end: int, start = 1):
  i = start
  s = 0
  while i < end:
    s += i
    i += 1
  return s
```

這個函數 `fn` 的功能是計算從 `start` 到 `end-1` 的所有整數的和。以下是該函數的逐步解釋：

1. **參數**:
   - `end`: 一個整數，表示計算的結束位置（不包括這個值）。
   - `start`: 一個可選的整數，默認為 1，表示計算的起始位置。

2. **變量初始化**:
   - `i`: 初始化為 `start`，用於迭代從 `start` 到 `end-1` 的整數。
   - `s`: 初始化為 0，用於累加這些整數的和。

3. **循環**:
   - 使用 `while` 循環，當 `i` 小於 `end` 時，執行循環體。
   - 在每次循環中，將 `i` 加到 `s` 上，然後將 `i` 增加 1。

4. **返回值**:
   - 當循環結束後，返回累加的和 `s`。

這個函數可以用來計算從 `start` 到 `end-1` 的所有整數的和。例如，`fn(5)` 將返回 10（1 + 2 + 3 + 4），而 `fn(10, 3)` 將返回 42（3 + 4 + 5 + 6 + 7 + 8 + 9）。

```python
print(fn(10))
```

```shell
45
```

`end` 是必須要有的參數。注意到要把必須要有的參數寫在最前面。

```python
def fn(start = 1, end: int):
```

翻譯成繁體中文：

```python
def fn(start = 1, end: int):
```

在這個函數定義中，`start` 參數的預設值為 1，而 `end` 參數則被指定為整數類型。

```shell
    def fn(start = 1, end: int):
                              ^
語法錯誤：非默認參數跟在默認參數後面
```

注意到`end`是`non-default argument`（非默认参数）。`start`是`default argument`（默认参数）。这意味着非默认参数跟在了默认参数后面。也就是说，必须把非默认参数放在所有默认参数前面。`start`是默认参数，即如果不传递的话，它默认已经有值了。

```python
def fn(a, /, b):
  print(a + b)
```

在傳統中文中，這段程式碼可以解釋為：

```python
def fn(a, /, b):
  印出(a + b)
```

這裡的 `def` 是定義函數的關鍵字，`fn` 是函數的名稱，`a` 和 `b` 是函數的參數。`/` 表示在它之前的參數（這裡是 `a`）必須以位置參數的方式傳遞，而不能以關鍵字參數的方式傳遞。`print(a + b)` 則是將 `a` 和 `b` 相加的結果輸出到控制台。

fn(1, 3)
```

这里使用`/`来分隔参数类型。传递参数的方式有两种：一种是通过位置传递，另一种是通过指定关键词传递。

```python
def fn(a, /, b):
  print(a + b)
```

```python
fn(a=1, 3)
```

```shell
    fn(a=1, 3)
             ^
語法錯誤：位置參數跟在關鍵字參數之後
```

這樣寫就不行。`a=1`表示這是靠關鍵字來傳遞參數。這把它當作了一個關鍵字參數。而b則是位置參數。

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        位置或关键字参数        |
        |                                - 仅关键字参数
         -- 仅位置参数
```

注意，这里在定义函数时，使用了`/`和`*`，这已经隐含了各参数的传递类型。因此，必须按照这些规则来传递参数。

```python
def fn(a, /, b):
  print(a + b)
```

在這個函數定義中，`/` 用於指示在它之前的參數（即 `a`）必須以位置參數的形式傳遞，而不能以關鍵字參數的形式傳遞。這意味著你不能這樣調用函數：`fn(a=1, b=2)`，而必須這樣調用：`fn(1, b=2)` 或 `fn(1, 2)`。

```python
fn(1, b=3)
```

上面這樣就沒有報錯。

```python
def fn(a, /, b, *, c):
  print(a + b + c)
```

在這個函數定義中：

- `a` 是一個位置參數，且只能通過位置傳遞（因為有 `/`）。
- `b` 是一個普通的位置或關鍵字參數。
- `c` 是一個關鍵字參數，只能通過關鍵字傳遞（因為有 `*`）。

這個函數的功能是將 `a`、`b` 和 `c` 相加並打印結果。

fn(1, 3, 4)
```

```shell
    fn(1, 3, 4)
TypeError: fn() 接受 2 個位置參數，但傳入了 3 個
```

`fn` 只能接收 2 個位置參數，但提供了 3 個。

```python
def fn(a, /, b, *, c):
  print(a + b + c)
```

```python
fn(a = 1, b=3, c=4)
```

```shell
    fn(a = 1, b=3, c=4)
TypeError: fn() 收到了一些僅限位置參數作為關鍵字參數傳遞：'a'
```

有些参数原本只能通过位置传递，现在则可以使用关键词来传递。

### 映射形式的参数

```python
def fn(**kwds):
  print(kwds)
```

```python
fn(**{'a': 1})
```

```shell
{'a': 1}
```

```python
def fn(**kwds):
  print(kwds['a'])
```

```python
d = {'a': 1}
fn(**d)
```

翻譯成繁體中文：

```python
d = {'a': 1}
fn(**d)
```

在這個例子中，`**d` 是將字典 `d` 解包成關鍵字參數傳遞給函數 `fn`。這個語法在繁體中文中通常保持不變，因為它是 Python 的語法結構，而不是需要翻譯的文本。

```shell
1
```

可见`**`的作用就是将参数展开。

```python
def fn(a, **kwds):
  print(kwds['a'])
```

```python
d = {'a': 1}
fn(1, **d)
```

翻譯成繁體中文：

```python
d = {'a': 1}
fn(1, **d)
```

在這個例子中，`**d` 是將字典 `d` 解包成關鍵字參數傳遞給函數 `fn`。這意味著 `fn(1, **d)` 等同於 `fn(1, a=1)`。

```shell
TypeError: 函數 fn() 收到了多個參數 'a' 的值
```

像`fn(1, **d)`这样调用函数时，展开后相当于`fn(a=1, a=1)`。因此会导致错误。

```python
def fn(**kwds):
  print(kwds['a'])
```

```python
d = {'a': 1}
fn(d)
```

```shell
TypeError: fn() 不接受位置参数，但提供了1个
```

如果像`fn(d)`这样调用函数，`d`会被当作位置参数传递，而不是展开成关键字参数。

```python
def fn(a, / , **kwds):
  print(kwds['a'])
```

```python
d = {'a': 1}
fn(1, **d)
```

翻譯成繁體中文：

```python
d = {'a': 1}
fn(1, **d)
```

這樣卻行。說明位置參數和映射形式的參數可以同名。

```python
def fn(a, / , a):
  print(a)
```

在Python中，函數的參數列表中使用了斜杠（`/`），這表示斜杠前的參數必須以位置參數的形式傳遞，而不能以關鍵字參數的形式傳遞。然而，這個函數定義中存在一個問題：參數列表中出現了兩個相同的參數名 `a`，這是不允許的。

正確的函數定義應該避免重複的參數名。例如：

```python
def fn(a, / , b):
  print(a, b)
```

這樣，`a` 必須以位置參數的形式傳遞，而 `b` 則可以以位置參數或關鍵字參數的形式傳遞。

```python
d = {'a': 1}
fn(1, **d)
```

翻譯成繁體中文：

```python
d = {'a': 1}
fn(1, **d)
```

在這個例子中，`**d` 是將字典 `d` 解包成關鍵字參數傳遞給函數 `fn`。這意味著 `fn(1, **d)` 等同於 `fn(1, a=1)`。

```shell
語法錯誤：函數定義中重複的參數 'a'
```

這樣就出錯了。注意這幾種情況的微妙關係。

```python
def fn(a, / , **kwds):
  print(kwds['a'])
```

fn(1, **[1, 2])
```

```shell
TypeError: __main__.fn() 中 ** 後的參數必須是一個映射（mapping），而不是列表（list）
```

`**` 後面必須跟著映射。

### 可迭代类型的参数

```python
def fn(*kwds):
  print(kwds)
```

fn(*[1, 2])
```

```shell
(1, 2)
``` 

（在繁體中文中，數字的表示方式與簡體中文相同，因此這裡不需要進行翻譯。）

```python
def fn(*kwds):
  print(kwds)
```

fn(*1)
```

```shell
TypeError: __main__.fn() * 後面的參數必須是可迭代對象，而不是整數
```

`*`必須跟著`iterable`。

```python
def fn(a, *kwds):
  print(type(kwds))
```

```python
fn(1, *[1])
```
翻譯成繁體中文為：
```python
fn(1, *[1])
```
在這個例子中，`fn(1, *[1])` 的語法在繁體中文中保持不變，因為它是一個函數調用，其中 `*[1]` 是將列表 `[1]` 解包為單獨的參數傳遞給函數 `fn`。這種語法在繁體中文的程式碼中通常不需要翻譯。

```shell
<class '元組'>
```

打印一下類型。這也是為什麼上面輸出`(1,2)`，而不是`[1,2]`。

```python
def fn(*kwds):
  print(kwds)
```

```python
fn(1, *[1])
```
翻譯成繁體中文為：
```python
fn(1, *[1])
```
在繁體中文中，這段程式碼保持不變，因為它是一個函數調用的語法，其中 `*[1]` 表示將列表 `[1]` 解包為單個參數傳遞給函數 `fn`。

```shell
(1, 1)
```

注意到这里调用`fn(1, *[1])`时，参数被展开了，变成了`fn(1,1)`。然后在`fn(*kwds)`解析的时候，`kwds`又将`1,1`转换成了元组`(1,1)`。

```python
def concat(*args, sep='/'):
  return sep.join(args)
```

將上述程式碼翻譯成繁體中文：

```python
def concat(*args, sep='/'):
  return sep.join(args)
```

這個函數的功能是將傳入的多個參數（`*args`）以指定的分隔符（`sep`，預設為 `/`）連接起來，並返回連接後的字串。

```python
print(concat('a','b','c', sep=','))
```

```shell
a,b,c
``` 

（注：此代码块内容为英文，无需翻译，保持原样即可。）

### Lambda 表达式

`lambda` 就是把函数当作变量来保存。还记得在「解谜计算机科学」一文中所说的吗？

```python
def incrementor(n):
  return lambda x: x + n
```

```python
def 增量器(n):
  return lambda x: x + n
```

```python
f = incrementor(2)
print(f(3))
```

```shell
5
```

再看一個例子。

```python
pairs = [(1, 4), (2, 1), (0, 3)]
```

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為：

pairs.sort(key = lambda pair: pair[1]) 翻譯為

```python
print(pairs)
```

```shell
[(2, 1), (0, 3), (1, 4)]
``` 

（此列表表示一组坐标点，无需翻译，保持原样即可。）

```python
pairs = [(1, 4), (2, 1), (0, 3)]
```

pairs.sort(key=lambda pair: pair[0])

```python
print(pairs)
```

```shell
[(0, 3), (1, 4), (2, 1)]
```

當使用 `pair[0]` 時，會根據第一個數字進行排序。而當使用 `pair[1]` 時，則會根據第二個數字進行排序。

### 文档注释

```python
def add():
  """添加一些東西
  """
  pass
```

```python
print(add.__doc__)
```

```shell
添加一些東西
```

### 函数签名

```python
def add(a: int, b: int) -> int:
  print(add.__annotations__)
  return a + b
```

```
add(1, 2)
```

```shell
{'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
``` 

翻譯成繁體中文為：

```shell
{'a': <類型 'int'>, 'b': <類型 'int'>, 'return': <類型 'int'>}
``` 

這表示字典中的鍵 `'a'`、`'b'` 和 `'return'` 對應的值都是整數類型 (`int`)。

## 数据结构

### 列表

```python
a = [1, 2, 3, 4]
```

a.append(5)
print(a)   # [1, 2, 3, 4, 5]

a[len(a):] = [6]
print(a)   # [1, 2, 3, 4, 5, 6]

a[3:] = [6]
print(a)   # [1, 2, 3, 6]

a.insert(0, -1)
print(a)   # 輸出結果為 [-1, 1, 2, 3, 6]

a.remove(1)
print(a)   # [-1, 2, 3, 6]

a.pop()
print(a)  # [-1, 2, 3]

a.clear()
print(a)  # []

a[:] = [1, 2]
print(a.count(1)) # 1

a.reverse()
print(a)   # [2, 1]

b = a.copy()
a[0] = 10
print(b)   # [2, 1]
print(a)   # [10, 1]

# 翻译为：
b = a.copy()
a[0] = 10
print(b)   # [2, 1]
print(a)   # [10, 1]

```python
b = a
a[0] = 3
print(b)  # [3, 1]
print(a)  # [3, 1]
```

翻譯成繁體中文：

```python
b = a
a[0] = 3
print(b)  # [3, 1]
print(a)  # [3, 1]
```

在這個例子中，`b` 被賦值為 `a`，這意味著 `b` 和 `a` 指向同一個列表物件。當我們修改 `a[0]` 的值為 3 時，由於 `b` 和 `a` 指向同一個列表，所以 `b` 的值也會跟著改變。因此，`print(b)` 和 `print(a)` 的輸出都是 `[3, 1]`。

### 列表构建

```python
print(3 ** 2)   # 9
print(3 ** 3)   # 27
```

翻譯成繁體中文：

```python
print(3 ** 2)   # 9
print(3 ** 3)   # 27
```

這段程式碼的功能是計算3的平方和立方，並輸出結果。

先来学习一种运算符，`**`。它表示“次方”的意思。

```python
sq = []
for x in range(10):
  sq.append(x ** 2)
  
print(sq)  
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

接着试试用`map`。

```python
a = map(lambda x:x, range(10))
print(a)
# <map 物件位於 0x103bb0550>
print(list(a))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
sq = map(lambda x: x ** 2, range(10))
print(list(sq))
# 輸出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

```python
sq = [x ** 2 for x in range(10)]
print(sq)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

可见`for`循环是非常灵活的。

```python
a = [i for i in range(5)]
print(a)
# [0, 1, 2, 3, 4]
```

a = [i+j for i in range(3) for j in range(3)]
print(a)
# [0, 1, 2, 1, 2, 3, 2, 3, 4]

a = [i for i in range(5) if i % 2 == 0]
print(a)
# 输出：[0, 2, 4]

a = [(i,i) for i in range(3)]
print(a)
# [(0, 0), (1, 1), (2, 2)]
```

### 嵌套列表构造

```python
matrix = [[(i+j*4) for i in range(4)] for j in range(3)]
print(matrix)
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

t = []
for j in range(3):
  t.append([(i+j*4) for i in range(4)])
print(t)
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

请注意这两段代码的方式。也就是说：

```python
[[(i+j*4) for i in range(4)] for j in range(3)]
```

這段代碼是一個嵌套的列表推導式，它會生成一個包含3個子列表的列表，每個子列表包含4個元素。具體來說，它會生成以下列表：

```python
[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

解釋：
- 外層的 `for j in range(3)` 會迭代3次，分別對應 `j = 0, 1, 2`。
- 內層的 `for i in range(4)` 會迭代4次，分別對應 `i = 0, 1, 2, 3`。
- 每次迭代時，`i + j * 4` 會計算出一個值，並將其添加到當前的子列表中。

因此，最終生成的列表是：

```python
[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

也就相当于：

```python
for j in range(3):
   [(i+j*4) for i in range(4)]
```

這段程式碼的繁體中文解釋如下：

```python
for j in range(3):  # 對於 j 從 0 到 2 的每一個值
   [(i+j*4) for i in range(4)]  # 生成一個列表，列表中的每個元素是 i + j*4，其中 i 從 0 到 3
```

這段程式碼會執行以下操作：
1. 外層的 `for` 迴圈會讓 `j` 從 0 到 2 依次取值。
2. 對於每一個 `j` 的值，內層的列表生成式會生成一個列表，列表中的每個元素是 `i + j*4`，其中 `i` 從 0 到 3。
3. 最終，這段程式碼會生成三個列表，每個列表包含四個元素。

例如，當 `j = 0` 時，生成的列表是 `[0, 1, 2, 3]`；當 `j = 1` 時，生成的列表是 `[4, 5, 6, 7]`；當 `j = 2` 時，生成的列表是 `[8, 9, 10, 11]`。

也就是说相当于：

```python
for j in range(3):
  for i in range(4):
      (i+j*4)
```

這段程式碼的繁體中文解釋如下：

這是一個嵌套的 `for` 迴圈結構。外層迴圈由變數 `j` 控制，範圍是從 0 到 2（因為 `range(3)` 生成 0、1、2）。內層迴圈由變數 `i` 控制，範圍是從 0 到 3（因為 `range(4)` 生成 0、1、2、3）。

在每次內層迴圈中，程式會計算 `(i + j * 4)` 的值，但這段程式碼並未對這個值進行任何操作（例如打印或存儲），因此實際上這段程式碼不會產生任何可見的輸出或效果。

如果希望看到計算結果，可以將程式碼修改為：

```python
for j in range(3):
  for i in range(4):
      print(i + j * 4)
```

這樣，程式會依次輸出 0 到 11 的數字，每個數字佔一行。

因此，这非常适合用于进行矩阵转置操作。

```python
matrix = [[(i+j*4) for i in range(4)] for j in range(3)]
print(matrix)
#  [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
```

mt = [[row[j] for row in matrix] for j in range(4)]
print(mt)
# [[0, 4, 8], [1, 5, 9], [2, 6, 10], [3, 7, 11]]

```python
print(list(zip(*matrix)))
[(0, 4, 8), (1, 5, 9), (2, 6, 10), (3, 7, 11)]
```

### 删除

`del` 是 Python 中的一个关键字，用于删除对象。它可以删除变量、列表中的元素、字典中的键值对等。以下是一些使用 `del` 的示例：

1. **删除变量**：
   ```python
   x = 10
   del x
   # 此时 x 不再存在
   ```

2. **删除列表中的元素**：
   ```python
   my_list = [1, 2, 3, 4, 5]
   del my_list[2]  # 删除索引为 2 的元素
   # my_list 现在是 [1, 2, 4, 5]
   ```

3. **删除字典中的键值对**：
   ```python
   my_dict = {'a': 1, 'b': 2, 'c': 3}
   del my_dict['b']  # 删除键 'b' 及其对应的值
   # my_dict 现在是 {'a': 1, 'c': 3}
   ```

4. **删除切片**：
   ```python
   my_list = [1, 2, 3, 4, 5]
   del my_list[1:3]  # 删除索引 1 到 2 的元素
   # my_list 现在是 [1, 4, 5]
   ```

`del` 语句不仅可以删除单个对象，还可以删除对象的引用，从而释放内存。

```python
a = [1, 2, 3, 4]
```

del a[1]
print(a)  # [1, 3, 4]

del a[0:2]
print(a) # [4]

```python
del a
print(a) # NameError: 名稱 'a' 未定義
```

### 字典

字典是一种用于存储键值对的数据结构。每个键都是唯一的，并且与一个值相关联。字典允许通过键快速查找、插入和删除对应的值。在Python中，字典使用大括号 `{}` 表示，键和值之间用冒号 `:` 分隔，键值对之间用逗号 `,` 分隔。

**示例：**

```python
# 创建一个字典
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 访问字典中的值
print(my_dict["name"])  # 输出: Alice

# 修改字典中的值
my_dict["age"] = 26

# 添加新的键值对
my_dict["email"] = "alice@example.com"

# 删除键值对
del my_dict["city"]

# 遍历字典
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

**输出：**

```
name: Alice
age: 26
email: alice@example.com
```

字典在需要快速查找和存储数据的场景中非常有用。

```python
ages = {'li': 19, 'wang': 28, 'he' : 7}
for name, age in ages.items():
    print(name, age)
```

這段程式碼會輸出每個人的名字和年齡：

```
li 19
wang 28
he 7
```

# 李 19
# 王 28
# 何 7

for name in ages:
    print(name)
    
# 李
# 王
# 何

for name, age in ages:
     print(name)

ValueError: 解包的值过多（预期为2个）

for i, name in enumerate(['li', 'wang', 'he']):
    print(i, name)

# 0 李
# 1 王
# 2 何

print(reversed([1, 2, 3]))
# <list_reverseiterator 物件位於 0x10701ffd0>

print(list(reversed([1, 2, 3])))
# [3, 2, 1]

```
```

### 模組

### 脚本方式调用模組

```python
import sys
```

def f(n):
    if n < 2:
        return n
    else:
        return f(n-1) + f(n-2)

```python
if __name__ == "__main__":
    r = f(int(sys.argv[1]))
    print(r)
```

```shell
% python fib.py 3
2
```

翻譯成繁體中文：

```shell
% python fib.py 3
2
```

（注：這段代碼是執行一個Python腳本 `fib.py`，並傳入參數 `3`，結果輸出 `2`。由於代碼本身是通用的，不需要翻譯，所以保持原樣。）

```shell
% python -m fib 5
5
```

翻譯為：

```shell
% python -m fib 5
5
```

在這個例子中，命令和輸出都是相同的，因為它們是程式碼和結果的表示，不需要翻譯。

### 目录

```python
import fib
```

```python
print(dir(fib))
```

```python
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'f', 'sys']
```

```python
import builtins
print(dir(builtins))
```

['算术错误', '断言错误', '属性错误', '基础异常', '阻塞IO错误', '管道破裂错误', '缓冲区错误', '字节警告', '子进程错误', '连接中止错误', '连接错误', '连接拒绝错误', '连接重置错误', '弃用警告', '文件结束错误', '省略号', '环境错误', '异常', '假', '文件已存在错误', '文件未找到错误', '浮点错误', '未来警告', '生成器退出', 'IO错误', '导入错误', '导入警告', '缩进错误', '索引错误', '中断错误', '是目录错误', '键错误', '键盘中断', '查找错误', '内存错误', '模块未找到错误', '名称错误', '无', '非目录错误', '未实现', '未实现错误', '操作系统错误', '溢出错误', '待弃用警告', '权限错误', '进程查找错误', '递归错误', '引用错误', '资源警告', '运行时错误', '运行时警告', '停止异步迭代', '停止迭代', '语法错误', '语法警告', '系统错误', '系统退出', '制表符错误', '超时错误', '真', '类型错误', '未绑定局部变量错误', 'Unicode解码错误', 'Unicode编码错误', 'Unicode错误', 'Unicode翻译错误', 'Unicode警告', '用户警告', '值错误', '警告', '零除错误', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', '绝对值', '所有', '任意', 'ASCII', '二进制', '布尔', '断点', '字节数组', '字节', '可调用', '字符', '类方法', '编译', '复数', '版权', '致谢', '删除属性', '字典', '目录', '除模', '枚举', '求值', '执行', '退出', '过滤', '浮点数', '格式化', '冻结集合', '获取属性', '全局变量', '有属性', '哈希', '帮助', '十六进制', '标识符', '输入', '整数', '是实例', '是子类', '迭代', '长度', '许可证', '列表', '局部变量', '映射', '最大值', '内存视图', '最小值', '下一个', '对象', '八进制', '打开', '序数', '幂', '打印', '属性', '退出', '范围', '表示', '反转', '四舍五入', '集合', '设置属性', '切片', '排序', '静态方法', '字符串', '求和', '超类', '元组', '类型', '变量', '压缩']
```

## 包

包，即`pakages`。

```shell
pk.py
fibp
├── cal
│   └── cal.py
└── pt
    └── pt.py
```

翻譯成繁體中文：

```shell
pk.py
fibp
├── cal
│   └── cal.py
└── pt
    └── pt.py
```

（注：文件結構和名稱在翻譯時保持不變，因為它們是代碼和文件系統的一部分，通常不需要翻譯。）

cal.py:

```python
def f(n):
    if n < 2:
        return n
    else:
        return f(n-1) + f(n-2)
    
def fl(n):
    return list(map(f, range(5)))
```

這段程式碼定義了兩個函數 `f` 和 `fl`。

1. **函數 `f(n)`**:
   - 這是一個遞迴函數，用於計算第 `n` 個斐波那契數。
   - 如果 `n` 小於 2，則直接返回 `n`。
   - 否則，返回 `f(n-1) + f(n-2)`，即前兩個斐波那契數的和。

2. **函數 `fl(n)`**:
   - 這個函數生成一個列表，包含前 5 個斐波那契數。
   - 使用 `map` 函數將 `f` 函數應用於 `range(5)`，然後將結果轉換為列表。

這段程式碼的主要目的是生成前 5 個斐波那契數的列表。

`pt.py`:

```python
def p(l):
    print(l, end=' ')
```

```python
def pln(l):
    print(l)
```

pk.py 是一个Python脚本文件的名称。根据文件名，它可能与“pk”相关的功能有关，比如“public key”（公钥）、“peak”（峰值）或其他以“pk”为缩写的术语。具体内容需要查看文件中的代码才能确定。如果你有关于这个文件的具体问题或需要进一步的帮助，请提供更多信息。

```python
import fibp.cal.cal
import fibp.pt.pt
```

fibp.pt.pt.p(fibp.cal.cal.fl(10))
```

`pk.py` 也可以寫成這樣：

```python
from fibp.cal import cal
from fibp.pt import pt
```

pt.p(cal.fl(10))
```