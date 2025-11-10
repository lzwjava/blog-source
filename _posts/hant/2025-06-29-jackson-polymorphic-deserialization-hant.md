---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Jackson 多態反序列化概述
translated: true
type: note
---

### Jackson 多態反序列化概述

Jackson 是一個用於 JSON 序列化與反序列化的 Java 函式庫。多態反序列化功能讓 Jackson 能根據 JSON 中嵌入的類型資訊，在反序列化過程中自動實例化基底類別的正確子類別。這在處理繼承階層時特別有用，能確保從 JSON 資料建立正確的物件類型。

關鍵組件：
- **@JsonTypeInfo**：控制類型資訊在 JSON 中儲存位置與方式的註解
- **@JsonSubTypes**：列出子類別（子類型）及其識別符的註解
- Jackson 的子類型解析機制負責處理映射關係

若未使用這些註解，Jackson 會預設將所有物件反序列化為基底類別，可能導致子類別特有資料遺失。

### 運作步驟詳解

1. **基底類別註解設定**：
   - 使用 `@JsonTypeInfo` 指定類型資訊嵌入位置（例如作為 JSON 物件中的屬性）
   - 範例：
     ```java
     @JsonTypeInfo(use = JsonTypeInfo.Id.NAME, include = JsonTypeInfo.As.PROPERTY, property = "@type")
     @JsonSubTypes({
         @JsonSubType(value = Cat.class, name = "cat"),
         @JsonSubType(value = Dog.class, name = "dog")
     })
     public abstract class Animal {
         public String name;
     }
     ```
     - `use = JsonTypeInfo.Id.NAME`：使用名稱（字串識別符）標示類型
     - `include = JsonTypeInfo.As.PROPERTY`：將類型資訊以屬性形式（"@type"）加入 JSON 物件
     - `@JsonSubTypes`：將子類別名稱映射至對應的 Java 類別（例如 "cat" → Cat.class）

2. **序列化流程**：
   - 當序列化 Cat 或 Dog 物件時，Jackson 會將類型識別符加入 JSON
   - 範例輸出：`{"@type": "cat", "name": "Whiskers", "purr": true}`（若 Cat 類別包含 "purr" 欄位）

3. **反序列化流程**：
   - Jackson 讀取 JSON 並檢查類型資訊（例如 "@type" 屬性）
   - 透過 `@JsonSubTypes` 將識別符（"cat"）映射回註冊的子類別（Cat.class）
   - 實例化正確的子類別並填入其欄位值
   - 若無匹配類型或缺少類型資訊，則預設使用基底類別或拋出例外（可透過 `defaultImpl` 配置）

4. **支援的類型資訊格式**：
   - `@JsonTypeInfo.As.PROPERTY`：類型作為欄位（例如 `{"@type": "cat", ...}`）
   - `@JsonTypeInfo.As.WRAPPER_OBJECT`：以類型為鍵值包裹物件（例如 `{"cat": {...}}`）
   - `@JsonTypeInfo.As.WRAPPER_ARRAY`：使用陣列格式
   - `@JsonTypeInfo.As.EXTERNAL_PROPERTY`：類型資訊存放於獨立欄位（進階功能，適用 XML 類結構）

### 進階配置與特殊情況

- **自訂名稱映射**：使用 `@JsonTypeInfo(use = JsonTypeInfo.Id.CLASS)` 將完整類別名稱直接嵌入 JSON（例如 `{"@class": "com.example.Cat", ...}`），但重構時可能較脆弱
- **預設實作**：添加 `defaultImpl = Animal.class` 可在缺少類型資訊時回退至預設類別
- **可見性與混入**：若無法修改原始類別，可透過 mix-in 類別應用註解
- **錯誤處理**：當類型資訊不符合已註冊子類型時，Jackson 會拋出 `JsonMappingException`，可透過自訂反序列化器處理
- **效能表現**：因高效的查找機制，反序列化時的額外開銷極小，但嵌入類型資訊會增加 JSON 負載大小

完整文件請參閱 Jackson 官方指南：[多態類型處理](https://github.com/FasterXML/jackson-docs/wiki/JacksonPolymorphicDeserialization)。此功能自 Jackson 2.x 版本起已趨穩定，其他 JSON 函式庫（如 Gson）也具備類似概念。如需進一步自訂，可擴展 `PolymorphicTypeValidator` 來強化非受信任輸入環境的安全性。