---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: google/gemini-2.5-flash
title: Pythonコード例の入門
translated: true
type: note
---

「Pythonコード」と言っても様々な意味があります！Pythonは非常に多目的な言語です。ここでは、基本的なものからやや複雑なものまで、異なる概念をカバーする一般的な例をいくつか紹介します。

---

### 1. Hello World (古典的な始まり)

これは最もシンプルなPythonプログラムです。

```python
# これはコメントです。コメントはPythonによって無視されます。
print("Hello, World!")
```

**説明:**
*   `print()` は、与えられた引数をコンソールに出力する組み込み関数です。
*   `"Hello, World!"` は文字列（テキスト）です。

---

### 2. 変数、基本的な算術演算、ユーザー入力

このコードは、データを変数に格納する方法、簡単な計算を実行する方法、ユーザーからの入力を受け取る方法を示しています。

```python
# データを格納する変数
name = input("お名前を入力してください: ") # ユーザーからの入力を受け取る
age_str = input("年齢を入力してください: ")

# 計算のために年齢を文字列から整数に変換
age = int(age_str)

# 基本的な算術演算
year_of_birth = 2023 - age # 説明を簡単にするため、現在の年を2023と仮定
# 以下のようにも書けます: import datetime; year_of_birth = datetime.date.today().year - age

# f-string（フォーマット済み文字列リテラル）を使用してフォーマットされた出力を表示
print(f"こんにちは、{name}さん！あなたは{age}歳です。")
print(f"あなたはおそらく{year_of_birth}年に生まれました。")

# 簡単な条件チェック
if age < 18:
    print("あなたは未成年です。")
else:
    print("あなたは成人です。")
```

**説明:**
*   `input()`: ユーザーにテキスト入力を促し、それを文字列として返します。
*   `name`, `age_str`, `age`, `year_of_birth`: これらは異なる種類のデータ（文字列、整数）を格納する変数です。
*   `int()`: 文字列を整数に変換します。`input()` は常に文字列を返すため、文字列で直接計算することはできません。この変換は必要です。
*   `f-strings`: 文字列リテラル内に式を埋め込む便利な方法です。開始引用符の前の `f` に注目してください。
*   `if/else`: 条件に基づいて異なるコードブロックを実行する制御フローステートメントです。

---

### 3. リストとループ

リストはアイテムの順序付きコレクションです。ループはコードブロックを複数回繰り返し実行するために使用されます。

```python
# フルーツのリスト
fruits = ["apple", "banana", "cherry", "date"]

print("\n私の好きなフルーツ:")

# 'for'ループを使用してリストをループ処理
for fruit in fruits:
    print(f"- {fruit.capitalize()}") # .capitalize() は最初の文字を大文字にします

# インデックスによる要素へのアクセス（リストは0から始まります）
print(f"\n最初のフルーツは: {fruits[0]}")
print(f"最後のフルーツは: {fruits[-1]}") # 負のインデックスは末尾からアクセスします

# 要素の追加
fruits.append("elderberry")
print(f"更新されたリスト: {fruits}")

# 要素の削除
fruits.remove("banana")
print(f"bananaを削除した後のリスト: {fruits}")

# インデックスを取得するために 'range' を使用してループ
print("\nインデックス付きのフルーツ:")
for i in range(len(fruits)): # len() はリスト内のアイテム数を返します
    print(f"インデックス {i}: {fruits[i]}")
```

**説明:**
*   `[]`: リストを定義するために使用します。
*   `for ... in ...`: シーケンス（リストなど）内の各アイテムを反復処理する `for` ループです。
*   `fruit.capitalize()`: 最初の文字を大文字にした文字列のコピーを返す文字列メソッドです。
*   `fruits[0]`: 最初の要素（インデックス0）にアクセスします。
*   `fruits[-1]`: 最後の要素にアクセスします。
*   `list.append()`: リストの末尾にアイテムを追加します。
*   `list.remove()`: 指定されたアイテムの最初の出現を削除します。
*   `range(len(fruits))`: 0からリストの長さ（を含まない）までの数字のシーケンスを生成します。インデックスによる要素へのアクセスに便利です。

---

### 4. 関数

関数は特定のタスクを実行する再利用可能なコードのブロックです。

```python
# 引数を受け取る関数を定義
def greet_person(name, age):
    """
    この関数は人物に挨拶し、年齢を伝えます。
    このようなdocstringを含めることは良い習慣です。
    """
    return f"こんにちは、{name}さん！あなたは{age}歳です。"

# 関数を呼び出す
message1 = greet_person("Alice", 30)
print(message1)

# 異なる引数で再度呼び出す
message2 = greet_person("Bob", 25)
print(message2)

# デフォルトパラメータを持つ関数を定義
def calculate_area(length, width=10):
    """長方形の面積を計算します。"""
    return length * width

print(f"\n5x10の長方形の面積: {calculate_area(5)}") # デフォルトの幅を使用
print(f"5x7の長方形の面積: {calculate_area(5, 7)}") # デフォルトの幅を上書き
```

**説明:**
*   `def`: 関数を定義するキーワードです。
*   `greet_person(name, age)`: 関数名とそのパラメータ（入力）です。
*   `return`: 関数から値を返します。
*   Docstrings (`"""Docstring goes here"""`): 関数の動作を説明します。ドキュメント化に適しています。
*   `calculate_area(length, width=10)`: デフォルトパラメータを示しています。関数を呼び出す際に `width` が提供されない場合、デフォルトで10になります。

---

### 5. 辞書

辞書はキーと値のペアでデータを格納します。これらは順序付けられていません（古いPythonバージョンでは。Python 3.7+では順序付けられています）。

```python
# 人物を表す辞書
person = {
    "first_name": "Charlie",
    "last_name": "Smith",
    "age": 40,
    "city": "London",
    "occupations": ["Engineer", "Teacher"] # リストを値にできます
}

print("\n人物の詳細:")

# キーによる値へのアクセス
print(f"名前: {person['first_name']} {person['last_name']}")
print(f"居住地: {person.get('city', '不明')}") # .get() はより安全で、キーが見つからない場合None/デフォルト値を返します
print(f"最初の職業: {person['occupations'][0]}")

# 値の変更
person["age"] = 41
print(f"新しい年齢: {person['age']}")

# 新しいキーと値のペアの追加
person["email"] = "charlie.smith@example.com"
print(f"メールアドレス: {person['email']}")

# 辞書のループ処理
print("\nすべてのキー:")
for key in person: # デフォルトでキーをループ処理します
    print(key)

print("\nすべての値:")
for value in person.values():
    print(value)

print("\nすべてのキーと値のペア:")
for key, value in person.items():
    print(f"{key}: {value}")
```

**説明:**
*   `{}`: 辞書を定義するために使用します。
*   `"key": value`: キーと値のペアです。キーは一意で不変（文字列や数値など）である必要があります。値は任意のデータ型にできます。
*   `person['key']`: `key` に関連付けられた値にアクセスします。
*   `person.get('key', 'default_value')`: より安全なアクセス方法で、キーが存在しない場合 `KeyError` を回避し、代わりに `default_value` を返します。
*   `dict.values()`: 辞書内のすべての値のリストを表示するビューオブジェクトを返します。
*   `dict.items()`: 辞書のキーと値のタプルのペアのリストを表示するビューオブジェクトを返します。

---

これはほんの表面をなぞったに過ぎませんが、これらの例は頻繁に使用する多くの基本的なPythonの概念をカバーしています！