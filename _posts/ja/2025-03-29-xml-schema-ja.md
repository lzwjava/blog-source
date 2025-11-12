---
audio: false
generated: true
lang: ja
layout: post
title: XMLガイド
translated: true
type: note
---

では、XML（Extensible Markup Language）に関する包括的なガイドを詳しく見ていきましょう。仕様、`<sequence>`要素の動作、そして`minOccurs`と`maxOccurs`の意味について説明します。

## XML完全ガイド

**XMLとは？**

XMLはデータを運ぶために設計されたマークアップ言語です。人間が読みやすく、機械でも読み取り可能です。その主な目的は、データを構造化し、保存し、転送することです。データを表示するように設計されたHTMLとは異なり、XMLはデータそのものを記述することに焦点を当てています。

**XMLの主な特徴:**

*   **拡張可能:** データを記述する独自のタグを定義できます。
*   **自己記述的:** 使用されるタグがデータの意味を記述します。
*   **階層構造:** XML文書は単一のルート要素を持つツリー状の構造です。
*   **プラットフォーム非依存:** XML形式を理解する任意のシステムで処理できます。
*   **テキストベース:** XML文書はプレーンテキストファイルなので、作成、読み取り、編集が容易です。
*   **整形式:** XML文書は整形式と見なされるために、厳密な構文規則に従わなければなりません。

**XMLの核心概念:**

*   **要素:** XML文書の基本的な構成要素です。開始タグと終了タグ（例: `<book>`, `</book>`）で定義されます。要素は、テキストコンテンツ、他の要素、またはその両方を含むことができます。
*   **属性:** 要素に関する追加情報を提供します。開始タグ内に現れ、名前と値のペアで構成されます（例: `<book genre="fiction">`）。
*   **タグ:** 山括弧（`<>`）で囲まれたキーワードです。開始タグは要素の始まりを示し、終了タグ（スラッシュ付き）は終わりを示します。
*   **ルート要素:** すべてのXML文書は、他のすべての要素を含む単一の最上位要素を持たなければなりません。
*   **ネストされた要素:** 要素は他の要素内にネストして、階層構造を作成できます。
*   **空要素:** コンテンツを持たない要素は、単一のタグ（例: `<br />`）または開始タグと終了タグの間に何もないもの（`<br></br>`）で表現できます。
*   **XML宣言（任意だが推奨）:** XML文書の最初の行は、XMLのバージョンとエンコーディングを指定するXML宣言にすることができます（例: `<?xml version="1.0" encoding="UTF-8"?>`）。
*   **コメント:** XML文書内に説明用の注記を追加するために使用されます。`<!--` と `-->` で囲みます。
*   **エンティティ:** 特殊文字または再利用可能なテキストブロックを表します。定義済みエンティティには、`&lt;` (<)、`&gt;` (>)、`&amp;` (&)、`&apos;` (')、`&quot;` (") があります。

**XML仕様:**

World Wide Web Consortium (W3C) が、XMLおよび関連技術の仕様を維持しています。主なXML仕様には以下があります:

*   **XML 1.0 (および XML 1.1):** XML文書の構文と構造を定義するコア仕様。XML 1.0が最も広く採用されているバージョンです。
*   **XML Schema (XSD):** XML文書の構造とデータ型を定義するための言語。Document Type Definitions (DTD) よりも強力で表現豊かなXML検証方法を提供します。
*   **Document Type Definition (DTD):** XML文書の構造を定義するために使用される古いスキーマ言語。まだ使用されることもありますが、高度な機能を持つXSDが一般的に好まれます。
*   **XPath:** XML文書内のノードを照会および選択するための言語。
*   **XSLT (Extensible Stylesheet Language Transformations):** XML文書を他の形式（例: HTML、プレーンテキスト、他のXML形式）に変換するための言語。
*   **Namespaces in XML:** 異なるソースからのXML文書を組み合わせる際の名前の衝突を避ける方法を提供します。

**XML Schema (XSD) と構造の定義:**

XML Schemaは、XML文書の有効な構造と内容を定義する上で重要です。これを使用して以下を指定できます:

*   文書内に現れることができる要素。
*   要素が持つことができる属性。
*   親要素内の子要素の順序と数。
*   要素と属性のデータ型。
*   要素と属性の値に対する制約。

**XML Schemaにおける`<sequence>`:**

`<sequence>`要素は、XML Schemaの複合型定義内で使用される合成子です。これは、その内部にある子要素が**指定された順序で現れなければならない**ことを示します。

**構文:**

```xml
<xs:complexType name="TypeName">
  <xs:sequence>
    <xs:element name="element1" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="element2" type="xs:integer" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="element3" type="xs:date" minOccurs="1" maxOccurs="1"/>
  </xs:sequence>
</xs:complexType>
```

この例では、`TypeName`複合型に準拠するXML要素は、以下を持たなければなりません:

1.  `<element1>`要素（文字列型）が正確に1回現れる。
2.  0個以上の`<element2>`要素（整数型）が`<element1>`の後に順番に現れる。
3.  `<element3>`要素（日付型）がすべての`<element2>`要素の後に正確に1回現れる。

**`minOccurs`属性と`maxOccurs`属性:**

`minOccurs`属性と`maxOccurs`属性は、XML Schemaの要素宣言内（通常は`<sequence>`、`<choice>`、または`<all>`合成子内）で使用され、要素が現れることができる最小回数と最大回数を指定します。

*   **`minOccurs`:**
    *   要素が現れなければならない最小回数を指定します。
    *   デフォルト値は`1`です。
    *   値が`0`の場合、要素はオプションであることを示します。
    *   正の整数は、必要な最小出現回数を示します。

*   **`maxOccurs`:**
    *   要素が現れることができる最大回数を指定します。
    *   デフォルト値は`1`です。
    *   正の整数は、許可される最大出現回数を示します。
    *   値`unbounded`は、要素が何回でも現れることができることを示します（`minOccurs`が0の場合は0回以上、`minOccurs`が1の場合は1回以上、など）。

**Sequenceが`minOccurs`および`maxOccurs`とどのように連携するか:**

要素が`<sequence>`内にある場合、各要素の`minOccurs`属性と`maxOccurs`属性は、*シーケンス内のその特定の位置における*その特定の要素に対して許可される出現回数を定義します。`<sequence>`で定義された要素の順序は、XMLインスタンス文書で維持されなければなりません。

**例:**

以下のXML Schemaスニペットを考えてみましょう:

```xml
<xs:complexType name="OrderType">
  <xs:sequence>
    <xs:element name="orderId" type="xs:ID" minOccurs="1" maxOccurs="1"/>
    <xs:element name="customer" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="item" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="orderDate" type="xs:date" minOccurs="1" maxOccurs="1"/>
  </xs:sequence>
</xs:complexType>
```

このスキーマに準拠するXML文書は、以下の構造を持ちます:

1.  **正確に1つ**の`<orderId>`要素。
2.  **正確に1つ**の`<customer>`要素。`<orderId>`の直後に現れる。
3.  **0個以上**の`<item>`要素。`<customer>`の後に順番に現れる。
4.  **正確に1つ**の`<orderDate>`要素。すべての`<item>`要素の後に現れる。

**有効なXMLインスタンス:**

```xml
<order>
  <orderId>ORD123</orderId>
  <customer>John Doe</customer>
  <item>Product A</item>
  <item>Product B</item>
  <orderDate>2025-03-29</orderDate>
</order>
```

**別の有効なXMLインスタンス:**

```xml
<order>
  <orderId>ORD456</orderId>
  <customer>Jane Smith</customer>
  <orderDate>2025-03-28</orderDate>
</order>
```

**無効なXMLインスタンス（順序が間違っている）:**

```xml
<order>
  <customer>John Doe</customer>
  <orderId>ORD123</orderId>
  <orderDate>2025-03-29</orderDate>
</order>
```

**無効なXMLインスタンス（`orderId`が欠落している）:**

```xml
<order>
  <customer>John Doe</customer>
  <item>Product A</item>
  <orderDate>2025-03-29</orderDate>
</order>
```

**まとめ:**

*   XMLは、データを構造化し転送するための多用途なマークアップ言語です。
*   明確に定義された構文と階層構造に依存しています。
*   XML Schema (XSD) は、XML文書の構造と内容を定義する強力な方法を提供します。
*   XSDの`<sequence>`合成子は、子要素の特定の順序を強制します。
*   `minOccurs`属性と`maxOccurs`属性は、要素が定義されたコンテキスト内（多くの場合`<sequence>`内）で現れることができる最小回数と最大回数を指定します。

このガイドは、XMLとその核心概念、特にXML Schemaを使用したXML文書構造の定義における`<sequence>`、`minOccurs`、`maxOccurs`の役割を理解するための確固たる基礎を提供します。最も詳細で最新の情報については、公式のW3C仕様書を参照することを忘れないでください。