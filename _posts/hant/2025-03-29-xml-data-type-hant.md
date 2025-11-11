---
audio: false
generated: true
lang: hant
layout: post
title: XML 結構描述資料類型
translated: true
type: note
---

XML Schema 定義了豐富的內建資料類型，可用於指定元素和屬性中允許的資料種類。這些資料類型確保 XML 內容符合預期的格式和約束條件。

XML Schema 中的內建資料類型大致分為**基本型別**和**衍生型別**。衍生型別基於基本型別，透過應用限制或其他修改而創建。

**基本資料類型（19 種內建類型）：**

這些是基礎且不可分割的資料類型，所有其他內建和使用者定義的簡單類型皆由此衍生。

* **String：** 表示字元字串
* **Boolean：** 表示邏輯值（true 或 false，也可表示為 1 或 0）
* **Decimal：** 表示任意精度的十進位數字
* **Float：** 表示單精度 32 位元浮點數
* **Double：** 表示雙精度 64 位元浮點數
* **Duration：** 表示時間間隔
* **DateTime：** 表示特定時間點，包含日期和時間
* **Time：** 表示 24 小時制內的特定時間點
* **Date：** 表示日曆日期
* **gYearMonth：** 表示特定年份和月份
* **gYear：** 表示特定年份
* **gMonthDay：** 表示特定月份和日期
* **gDay：** 表示特定月份中的某天
* **gMonth：** 表示特定年份中的某月
* **HexBinary：** 表示以十六進位值呈現的二進位資料
* **Base64Binary：** 表示以 Base64 編碼的二進位資料
* **AnyURI：** 表示統一資源標識符 (URI)
* **QName：** 表示限定名稱（帶有命名空間前綴的名稱）
* **NOTATION：** 表示 schema 中宣告的記號名稱

**衍生資料類型（約 25 種內建類型）：**

這些資料類型透過對基本型別應用約束條件（面）而衍生，例如長度、範圍、模式等。

**衍生自 `string`：**

* `normalizedString`：表示已將換行符、製表符和回車符替換為空格，且沒有前導或尾隨空格的字元字串
* `token`：表示沒有前導或尾隨空白字元，且內部沒有兩個或以上連續空白字元的正規化字串
* `language`：表示符合 RFC 3066 定義的語言標識符
* `NMTOKEN`：表示名稱符記（可包含字母、數字、點號、連字號和底線）
* `NMTOKENS`：表示以空白分隔的 `NMTOKEN` 列表
* `Name`：表示 XML 名稱（必須以字母或底線開頭，後接字母、數字、點號、連字號或底線）
* `NCName`：表示非冒號化名稱（類似 `Name` 但不能包含冒號）
* `ID`：表示 XML 文件內的唯一標識符
* `IDREF`：表示對同一文件中 `ID` 值的引用
* `IDREFS`：表示以空白分隔的 `IDREF` 值列表
* `ENTITY`：表示對 DTD 中宣告的未解析實體的引用（在 XML Schema 中較不常見）
* `ENTITIES`：表示以空白分隔的 `ENTITY` 值列表（在 XML Schema 中較不常見）

**衍生自 `decimal`：**

* `integer`：表示整數（無小數部分）
* `nonPositiveInteger`：表示小於或等於 0 的整數
* `negativeInteger`：表示嚴格小於 0 的整數
* `long`：表示 64 位元帶符號整數
* `int`：表示 32 位元帶符號整數
* `short`：表示 16 位元帶符號整數
* `byte`：表示 8 位元帶符號整數
* `nonNegativeInteger`：表示大於或等於 0 的整數
* `unsignedLong`：表示 64 位元無符號整數
* `unsignedInt`：表示 32 位元無符號整數
* `unsignedShort`：表示 16 位元無符號整數
* `unsignedByte`：表示 8 位元無符號整數
* `positiveInteger`：表示嚴格大於 0 的整數

**其他衍生類型：**

* `dateTimeStamp`（在 XML Schema 1.1 中）：類似 `dateTime` 但包含時區資訊
* `yearMonthDuration`（在 XML Schema 1.1 中）：表示以年和月為單位的持續時間
* `dayTimeDuration`（在 XML Schema 1.1 中）：表示以天、小時、分鐘和秒為單位的持續時間
* `precisionDecimal`（在 XML Schema 1.1 中）：表示保留精度的十進位數字

**使用者定義資料類型：**

除了內建類型外，XML Schema 允許您使用以下機制定義自己的簡單和複雜資料類型：

* **限制：** 透過限制現有類型（可以是內建或用戶定義）的範圍或格式來創建新類型
* **列表：** 定義其值為來自另一個簡單類型的值序列的類型
* **聯合：** 定義其值可來自兩個或多個其他簡單類型的值空間的類型

在 XML Schema 中定義元素和屬性時，您使用 `type` 屬性來指定內容應遵循的資料類型。這可確保資料有效性並促進資料處理。

例如：

```xml
<xs:element name="age" type="xs:positiveInteger"/>
<xs:element name="name" type="xs:string"/>
<xs:attribute name="status" type="xs:token"/>
```

在此程式碼片段中，`age` 元素被定義為保存正整數，`name` 元素保存字串，而 `status` 屬性保存符記（具有特定空白處理的正規化字串）。

理解這些資料類型是創建有效且定義完善的 XML Schema 的基礎。您可以在 W3C XML Schema Part 2: Datatypes 規範中找到完整的詳細資訊和正式定義。