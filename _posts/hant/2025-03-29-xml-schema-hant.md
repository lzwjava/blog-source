---
audio: false
generated: true
lang: hant
layout: post
title: XML 指南
translated: true
type: note
---

好的，讓我們深入探討關於 XML（可擴展標記語言）的完整指南，涵蓋其規格、`<sequence>` 元素的工作原理，以及 `minOccurs` 和 `maxOccurs` 的含義。

## XML 完整指南

**什麼是 XML？**

XML 是一種用於承載數據的標記語言。它既可供人類閱讀，也可供機器閱讀。其主要目的是結構化、存儲和傳輸數據。與用於顯示數據的 HTML 不同，XML 專注於描述數據本身。

**XML 的主要特性：**

* **可擴展性：** 您可以定義自己的標籤來描述數據。
* **自描述性：** 使用的標籤描述了數據的含義。
* **層次結構：** XML 文件具有樹狀結構，包含單一根元素。
* **平台獨立性：** 任何理解 XML 格式的系統都可以處理 XML。
* **基於文本：** XML 文件是純文本文件，易於創建、讀取和編輯。
* **格式正確：** XML 文件必須遵守嚴格的語法規則才能被視為格式正確。

**XML 核心概念：**

* **元素：** XML 文件的基本構建塊。它們由開始和結束標籤定義（例如 `<book>`、`</book>`）。元素可以包含文本內容、其他元素或兩者的混合。
* **屬性：** 提供有關元素的附加信息。它們出現在開始標籤內，由名稱-值對組成（例如 `<book genre="fiction">`）。
* **標籤：** 括在尖括號 (`<>`) 中的關鍵字。開始標籤標記元素的開始，結束標籤（帶有正斜杠）標記元素的結束。
* **根元素：** 每個 XML 文件必須有一個單一的頂層元素，其中包含所有其他元素。
* **嵌套元素：** 元素可以嵌套在其他元素內，以創建層次結構。
* **空元素：** 沒有內容的元素可以用單個標籤表示（例如 `<br />`），或者用開始和結束標籤表示，中間沒有任何內容（`<br></br>`）。
* **XML 聲明（可選但建議使用）：** XML 文件的第一行可以是 XML 聲明，用於指定 XML 版本和編碼（例如 `<?xml version="1.0" encoding="UTF-8"?>`）。
* **註釋：** 用於在 XML 文件中添加解釋性說明。它們包含在 `<!--` 和 `-->` 之間。
* **實體：** 表示特殊字符或可重複使用的文本塊。預定義實體包括 `&lt;` (<)、`&gt;` (>)、`&amp;` (&)、`&apos;` (') 和 `&quot;` (")。

**XML 規格：**

萬維網聯盟 (W3C) 負責維護 XML 及相關技術的規格。一些關鍵的 XML 規格包括：

* **XML 1.0（和 XML 1.1）：** 定義 XML 文件語法和結構的核心規格。XML 1.0 是最廣泛採用的版本。
* **XML Schema (XSD)：** 一種用於定義 XML 文件結構和數據類型的語言。它提供了比文件類型定義 (DTD) 更強大、更具表現力的方式來驗證 XML。
* **文件類型定義 (DTD)：** 一種較舊的架構語言，用於定義 XML 文件的結構。雖然有時仍會遇到，但通常更推薦使用具有高級功能的 XSD。
* **XPath：** 一種用於查詢和選擇 XML 文件內節點的語言。
* **XSLT（可擴展樣式表語言轉換）：** 一種用於將 XML 文件轉換為其他格式（例如 HTML、純文本、其他 XML 格式）的語言。
* **XML 命名空間：** 提供了一種在合併來自不同來源的 XML 文件時避免命名衝突的方法。

**XML Schema (XSD) 與定義結構：**

XML Schema 對於定義 XML 文件的有效結構和內容至關重要。它允許您指定：

* 文件中可以出現的元素。
* 元素可以具有的屬性。
* 父元素內子元素的順序和數量。
* 元素和屬性的數據類型。
* 對元素和屬性值的約束。

**XML Schema 中的 `<sequence>`：**

`<sequence>` 元素是在 XML Schema 中複雜類型定義內使用的組合器。它表示其中的子元素**必須以指定的順序出現**。

**語法：**

```xml
<xs:complexType name="TypeName">
  <xs:sequence>
    <xs:element name="element1" type="xs:string" minOccurs="1" maxOccurs="1"/>
    <xs:element name="element2" type="xs:integer" minOccurs="0" maxOccurs="unbounded"/>
    <xs:element name="element3" type="xs:date" minOccurs="1" maxOccurs="1"/>
  </xs:sequence>
</xs:complexType>
```

在此示例中，任何符合 `TypeName` 複雜類型的 XML 元素必須具有：

1.  一個 `<element1>` 元素（字符串類型）恰好出現一次。
2.  零個或多個 `<element2>` 元素（整數類型）在 `<element1>` 之後按順序出現。
3.  一個 `<element3>` 元素（日期類型）在所有 `<element2>` 元素之後恰好出現一次。

**`minOccurs` 和 `maxOccurs` 屬性：**

`minOccurs` 和 `maxOccurs` 屬性用於 XML Schema 中的元素聲明內（通常在 `<sequence>`、`<choice>` 或 `<all>` 組合器內），以指定元素可以出現的最小和最大次數。

* **`minOccurs`：**
    * 指定元素必須出現的最小次數。
    * 默認值為 `1`。
    * 值為 `0` 表示該元素是可選的。
    * 正整數表示所需的最小出現次數。

* **`maxOccurs`：**
    * 指定元素可以出現的最大次數。
    * 默認值為 `1`。
    * 正整數表示允許的最大出現次數。
    * 值 `unbounded` 表示該元素可以出現任意次數（如果 `minOccurs` 為 0，則為零次或多次；如果 `minOccurs` 為 1，則為一次或多次，依此類推）。

**Sequence 如何與 `minOccurs` 和 `maxOccurs` 協同工作：**

當元素位於 `<sequence>` 內時，每個單獨元素上的 `minOccurs` 和 `maxOccurs` 屬性定義了*在序列中該特定位置*該特定元素允許的出現次數。XML 實例文件中必須維持 `<sequence>` 中定義的元素順序。

**示例：**

考慮以下 XML Schema 片段：

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

符合此架構的 XML 文件將具有以下結構：

1.  **恰好一個** `<orderId>` 元素。
2.  **恰好一個** `<customer>` 元素，緊接在 `<orderId>` 之後出現。
3.  **零個或多個** `<item>` 元素，在 `<customer>` 之後按順序出現。
4.  **恰好一個** `<orderDate>` 元素，在所有 `<item>` 元素之後出現。

**有效的 XML 實例：**

```xml
<order>
  <orderId>ORD123</orderId>
  <customer>John Doe</customer>
  <item>Product A</item>
  <item>Product B</item>
  <orderDate>2025-03-29</orderDate>
</order>
```

**另一個有效的 XML 實例：**

```xml
<order>
  <orderId>ORD456</orderId>
  <customer>Jane Smith</customer>
  <orderDate>2025-03-28</orderDate>
</order>
```

**無效的 XML 實例（順序錯誤）：**

```xml
<order>
  <customer>John Doe</customer>
  <orderId>ORD123</orderId>
  <orderDate>2025-03-29</orderDate>
</order>
```

**無效的 XML 實例（缺少 `orderId`）：**

```xml
<order>
  <customer>John Doe</customer>
  <item>Product A</item>
  <orderDate>2025-03-29</orderDate>
</order>
```

**總結：**

* XML 是一種用於結構化和傳輸數據的多功能標記語言。
* 它依賴於明確定義的語法和層次結構。
* XML Schema (XSD) 提供了一種強大的方式來定義 XML 文件的結構和內容。
* XSD 中的 `<sequence>` 組合器強制執行子元素的特定順序。
* `minOccurs` 和 `maxOccurs` 屬性指定了元素在其定義的上下文（通常在 `<sequence>` 內）中可以出現的最小和最大次數。

本指南為理解 XML 及其核心概念提供了堅實的基礎，特別是使用 XML Schema 定義 XML 文件結構時 `<sequence>`、`minOccurs` 和 `maxOccurs` 的作用。請記住查閱官方 W3C 規格以獲取最詳細和最新的信息。