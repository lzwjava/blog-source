---
audio: false
generated: true
lang: ja
layout: post
title: Pythonガイド
translated: true
type: note
---

Pythonの文字列操作、数学演算、テキスト処理、I/O、ファイル操作、ネットワーク、コレクション、マルチスレッドについて簡潔にまとめたガイドです。各セクションには概要と実践的な例が含まれており、学習を始めたり知識をリフレッシュしたりするのに役立ちます。

---

## Pythonガイド：主要トピック

### 1. 文字列操作
Pythonの文字列は不変な文字シーケンスです。連結、繰り返し、スライスなどの操作や、組み込みメソッドを使用した操作が可能です。

**例:**
```python
# 連結と繰り返し
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # 出力: Hello World
print(s1 * 3)         # 出力: HelloHelloHello

# スライス
print(s1[1:4])        # 出力: ell

# 組み込みメソッド
print(s1.upper())     # 出力: HELLO
print(s2.lower())     # 出力: world
print("  hi  ".strip())  # 出力: hi
print("a,b,c".split(','))  # 出力: ['a', 'b', 'c']
print(','.join(['a', 'b', 'c']))  # 出力: a,b,c

# f-stringを使った文字列フォーマット
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # 出力: My name is Alice and I am 30 years old.
```

---

### 2. 数学演算
`math`モジュールは一般的な計算のための数学関数と定数を提供します。

**例:**
```python
import math

print(math.sqrt(16))    # 出力: 4.0
print(math.pow(2, 3))   # 出力: 8.0
print(math.sin(math.pi / 2))  # 出力: 1.0
print(math.pi)          # 出力: 3.141592653589793
```

---

### 3. テキスト処理（正規表現）
`re`モジュールは正規表現を使用したパターンマッチングとテキスト操作を可能にします。

**例:**
```python
import re

text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())  # 出力: Found: rain

# 4文字の単語をすべて検索
print(re.findall(r"\b\w{4}\b", text))  # 出力: ['rain', 'Spain']
```

---

### 4. I/O（入力と出力）
基本的な入力出力操作により、ユーザーとの対話が可能です。

**例:**
```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

---

### 5. ファイル操作
Pythonは`open()`関数を使用したファイルの読み書きを簡素化し、`with`文を使用するとファイルの自動クローズが推奨されます。

**例:**
```python
# ファイルへの書き込み
with open("example.txt", "w") as f:
    f.write("Hello, World!\n")

# ファイルからの読み込み
with open("example.txt", "r") as f:
    content = f.read()
    print(content)  # 出力: Hello, World!
```

---

### 6. ネットワーク
`requests`ライブラリ（`pip install requests`でインストール）によりHTTPリクエストが簡単になります。

**例:**
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 出力: 200
print(response.json())       # 出力: GitHub APIからのJSONデータ
```

---

### 7. コレクション
`collections`モジュールは`Counter`、`deque`、`namedtuple`などの特殊なデータ構造を提供します。以下は`Counter`の例です。

**例:**
```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry"]
word_count = Counter(words)
print(word_count)  # 出力: Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

**その他のコレクション:**
- `namedtuple`: 名前付きフィールドを持つタプルのサブクラスを作成
- `deque`: 両端からの効率的な追加/取り出しのための両端キュー
- `OrderedDict`: 挿入順序を記憶する辞書
- `defaultdict`: 存在しないキーに対してデフォルト値を返す辞書

---

### 8. マルチスレッド
`threading`モジュールは並行タスク実行を可能にし、I/Oバウンドな操作に理想的です。

**例:**
```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

# スレッドの作成と開始
t = threading.Thread(target=print_numbers)
t.start()

# メインスレッドの継続
print("Main thread finished")
```

---

このガイドは各トピックの出発点として実践的な例を提供しています。より深く学ぶには、公式Pythonドキュメントや専門的なリソースを参照してください。Happy coding!