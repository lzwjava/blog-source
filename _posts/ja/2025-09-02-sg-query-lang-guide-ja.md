---
audio: false
generated: true
image: false
lang: ja
layout: post
title: ソースグラフクエリ言語ガイド
translated: true
type: note
---

Sourcegraphの検索には、柔軟で強力な独自のクエリ言語があります。以下によく使われる構文の内訳を示します：

---

### 1. **基本的なキーワード検索**

* 単語を入力するだけ：

  ```
  http client
  ```

  両方の単語を含むファイルやコードを検索します。

---

### 2. **論理演算子**

* `AND`、`OR`、`NOT` (大文字である必要があります)：

  ```
  React AND useEffect
  React OR Vue
  logger NOT debug
  ```

---

### 3. **フィルター**

* `repo:` → リポジトリで絞り込む

  ```
  repo:github.com/myorg/myrepo
  ```
* `file:` → ファイルパスで一致させる (正規表現をサポート)

  ```
  file:\.java$
  ```
* `lang:` → プログラミング言語を指定する

  ```
  lang:python requests
  ```
* `content:` → テキスト検索を強制する (構造的な一致を無視)

  ```
  content:"SELECT * FROM"
  ```
* `case:yes` → 検索で大文字と小文字を区別する

---

### 4. **正規表現マッチング**

* デフォルトで、Sourcegraphは正規表現をサポートしています。

  ```
  foo(bar|baz)
  ^class\s+\w+
  ```

---

### 5. **構造的検索**

パターンホール `:[var]` を使用してコード構造をマッチさせる：

```
if (:[cond]) { :[body] }
```

---

### 6. **リビジョン / ブランチ検索**

* `@branch`、`@commit`、`@tag` を追加する：

  ```
  repo:myrepo@main lang:go fmt.Println
  ```

---

### 7. **シンボルと定義**

* `type:symbol` → シンボル名を検索
* `type:commit` → コミットメッセージを検索
* `type:diff` → コード差分を検索

---

### 8. **例**

* Goファイル内のすべての `TODO` コメントを検索：

  ```
  TODO lang:go
  ```
* `src/` フォルダ内のJavaメソッドのみを検索：

  ```
  file:^src/ lang:java "public static"
  ```
* 複数のリポジトリにまたがって検索：

  ```
  repo:github.com/org/.* file:\.ts$ "useState"
  ```

---

👉 **よく使われるSourcegraphクエリのクイックチートシート** (日常的に再利用できる一行クエリなど) を作成しましょうか、それとも **高度なパターンを含めた詳細な解説** を準備しましょうか？