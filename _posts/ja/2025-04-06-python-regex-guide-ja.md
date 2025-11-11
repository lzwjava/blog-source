---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Python正規表現ガイド
translated: true
type: note
---

### `re`モジュールのインポート
`re`モジュール（正規表現を意味する）はPythonの標準ライブラリの一部です。これは別個の「正規表現パッケージ」ではなく、組み込みのモジュールです。スクリプトの先頭でインポートしてください：

```python
import re
```

### 基本概念
正規表現（regex）は、文字列の照合、検索、操作に使用されるパターンです。以下のような特殊文字を使用します：
- `.`（任意の1文字）
- `*`（0回以上の繰り返し）
- `+`（1回以上の繰り返し）
- `[]`（文字クラス、例：`[a-z]` 小文字）
- `^`（文字列の先頭）、`$`（文字列の末尾）

例はPythonの`re`ドキュメントに基づいています。複雑なパターンは効率化のために`re.compile()`でコンパイルしてください。

### 主な関数と使用方法

#### 1. **先頭でのパターンマッチ**
   - `re.match(pattern, string)`: パターンが文字列の先頭から一致するかチェックします。
   - マッチオブジェクトまたは`None`を返します。

   例：
   ```python
   import re
   result = re.match(r"Hello", "Hello world")
   print(result.group())  # 出力: Hello
   ```

#### 2. **文字列内の任意の位置を検索**
   - `re.search(pattern, string)`: 文字列内の最初のパターン出現箇所を検索します。
   - マッチオブジェクトまたは`None`を返します。

   例：
   ```python
   result = re.search(r"world", "Hello world")
   print(result.group())  # 出力: world
   ```

#### 3. **すべての一致を検索**
   - `re.findall(pattern, string)`: 重複しないすべての一致のリストを返します。

   例：
   ```python
   matches = re.findall(r"\d+", "I have 3 cats and 42 dogs")
   print(matches)  # 出力: ['3', '42']
   ```

#### 4. **文字列の分割**
   - `re.split(pattern, string)`: パターンの出現位置で文字列を分割します。

   例：
   ```python
   parts = re.split(r"\s+", "Hello    world   example")
   print(parts)  # 出力: ['Hello', 'world', 'example']
   ```

#### 5. **一致部分の置換**
   - `re.sub(pattern, replacement, string)`: 一致部分を置換文字列で置き換えます。

   例：
   ```python
   new_string = re.sub(r"bad", "good", "This is bad")
   print(new_string)  # 出力: This is good
   ```

#### 6. **再利用のためのパターンコンパイル**
   - 繰り返し使用する場合、正規表現をパターンオブジェクトにコンパイルするとパフォーマンスが向上します。

   例：
   ```python
   pattern = re.compile(r"\d+")
   matches = pattern.findall("Room 101 and 102")
   print(matches)  # 出力: ['101', '102']
   ```

### ベストプラクティス
- バックスラッシュのエスケープ問題を避けるため、正規表現パターンには生文字列（`r""`）を使用してください。
- マッチオブジェクトの処理：一致文字列の取得には`.group()`を、インデックスの取得には`.span()`を使用してください。
- 複雑なタスクの場合、オンラインツールやPythonの対話シェルでパターンをテストしてください。
- その他の例やフラグ（例：`re.IGNORECASE`）については、Pythonの公式ドキュメント（https://docs.python.org/3/library/re.html）を参照してください。

特定のユースケースやエラーがある場合は、詳細を提供してください！