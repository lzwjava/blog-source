---
audio: false
date: 2025-09-12
generated: true
image: false
lang: ja
layout: post
model: mistralai/mistral-medium-3.1
title: Sourcegraphコード検索ガイド
translated: true
type: note
---

Sourcegraphは強力なコード検索・ナビゲーションツールで、開発者が複数のリポジトリを横断して検索し、コードの依存関係を理解し、大規模なコードベースを効率的にナビゲートできるようにします。このガイドでは、**検索構文、ベストプラクティス、言語固有の検索（JavaとPython）** について説明します。

---

## **1. 基本検索構文**
Sourcegraphは、フィルターを伴う**リテラル検索、正規表現検索、構造的検索**をサポートしています。

### **1.1. リテラル検索**
正確なテキストを検索:
```
"def calculate_sum"
```

### **1.2. 正規表現検索**
正規表現には `/.../` を使用:
```
/def \w+_sum\(/
```

### **1.3. 構造的検索 (Beta)**
コードパターン（例: 関数定義）を検索:
```
type:func def calculate_sum
```

### **1.4. フィルター**
フィルターを使用して検索を絞り込み:
- `repo:` – 特定のリポジトリで検索
  ```
  repo:github.com/elastic/elasticsearch "def search"
  ```
- `file:` – 特定のファイルで検索
  ```
  file:src/main/java "public class"
  ```
- `lang:` – 特定の言語で検索
  ```
  lang:python "def test_"
  ```
- `type:` – シンボル（関数、クラスなど）を検索
  ```
  type:func lang:go "func main"
  ```

---

## **2. 高度な検索テクニック**
### **2.1. ブール演算子**
- `AND` (デフォルト): `def calculate AND sum`
- `OR`: `def calculate OR def sum`
- `NOT`: `def calculate NOT def subtract`

### **2.2. ワイルドカード**
- `*` – 任意の文字シーケンスに一致
  ```
  "def calculate_*"
  ```
- `?` – 単一の文字に一致
  ```
  "def calculate_?"
  ```

### **2.3. 大文字・小文字の区別**
- デフォルトでは大文字小文字を区別しない
- `case:yes` で大文字小文字を区別
  ```
  case:yes "Def Calculate"
  ```

### **2.4. コメント内の検索**
`patternType:literal` を使用してコメント内を検索:
```
patternType:literal "// TODO:"
```

---

## **3. Javaコードの検索**
### **3.1. クラスの検索**
```
type:symbol lang:java "public class"
```
### **3.2. メソッドの検索**
```
type:func lang:java "public void"
```
### **3.3. アノテーションの検索**
```
lang:java "@Override"
```
### **3.4. インポート文の検索**
```
lang:java "import org.springframework"
```
### **3.5. 例外処理の検索**
```
lang:java "try {" AND "catch (Exception"
```

---

## **4. Pythonコードの検索**
### **4.1. 関数の検索**
```
type:func lang:python "def calculate"
```
### **4.2. クラスの検索**
```
type:symbol lang:python "class Calculator"
```
### **4.3. インポート文の検索**
```
lang:python "import pandas"
```
### **4.4. デコレーターの検索**
```
lang:python "@app.route"
```
### **4.5. ドキュメント文字列の検索**
```
lang:python '"""'
```

---

## **5. ベストプラクティス**
1. 結果を絞り込むために **`lang:` を使用**する。
2. 精度を高めるためにフィルター（`repo:`, `file:`, `type:`）を**組み合わせる**。
3. 柔軟なパターンマッチングに**正規表現を使用**する。
4. 頻繁に行うクエリは**検索を保存**する。
5. 必要に応じて **`case:yes` を使用**する。

---

## **6. クエリ例**

| **目的** | **クエリ** |
|----------|-----------|
| すべてのJava `main`メソッドを検索 | `lang:java "public static void main"` |
| Pythonのテスト関数を検索 | `lang:python "def test_"` |
| GoのTODOコメントを検索 | `lang:go "// TODO:"` |
| Spring Bootコントローラーを検索 | `lang:java "@RestController"` |
| JavaScriptのすべての`if`文を検索 | `lang:javascript "if ("` |

---

## **7. まとめ**
Sourcegraphの検索は**強力で柔軟**であり、複数の言語にわたる**リテラル、正規表現、構造的検索**をサポートしています。フィルター（`lang:`, `repo:`, `type:`）をマスターすることで、大規模なコードベースを効率的にナビゲートできます。

### **次のステップ**
- 定期的に行うクエリには**保存された検索**を試す。
- **コードインテリジェンス**（ホバーツールチップ、クロスリポジトリナビゲーション）を探索する。
- **Sourcegraph拡張機能**（VS Code, JetBrains）を使用する。

特定の機能についてさらに詳しく知りたいですか？ 🚀