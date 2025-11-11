---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Jackson 默認類型設定詳解
translated: true
type: note
---

### 什麼是 Jackson ObjectMapper 中的預設類型處理？

Jackson 的 `ObjectMapper` 是 Jackson JSON 函式庫中的核心類別，負責將 Java 物件序列化為 JSON，並將 JSON 反序列化回物件。「預設類型處理」是一項增強多態類型處理的功能（例如當某個欄位可容納不同子類別時）。其運作方式是在序列化過程中將類型資訊嵌入 JSON 輸出，讓映射器在反序列化時用來實例化正確的具體類別。

若未啟用預設類型處理，Jackson 會依賴宣告的類型（例如抽象基礎類別或介面），且可能需要自訂配置（如 `@JsonTypeInfo` 註解）來指定子類型。啟用預設類型處理可為多態性提供全域或半全域的後備機制，特別適用於包含混合類型的集合或映射。

### 運作原理為何？

啟用預設類型處理會修改序列化過程：
1. **序列化**：當序列化物件圖時，Jackson 會在 JSON 中加入特殊的 `@class` 欄位或類似元數據，以標示多態物件的執行時期類型。這僅發生在宣告類型未完全指定具體類別的情況下（例如包含 `String` 和 `Integer` 物件的 `List`，或抽象類別欄位）。

2. **反序列化**：在反序列化過程中，映射器會使用嵌入的類型資訊來查找並實例化確切的類別。它利用 Jackson 的 `TypeFactory` 動態解析類型。

啟用方式是在 `ObjectMapper` 實例上呼叫以下方法之一：
- `mapper.enableDefaultTyping()`：已棄用的方法，啟用固定時間的多態類型包含（易受安全性問題影響）。
- `mapper.activateDefaultTyping(ObjectMapper.DefaultTyping policy)`：Jackson 2.10 引入的更安全推薦替代方案。允許指定 `DefaultTyping` 枚舉值，例如：
  - `JAVA_LANG_OBJECT`：包含所有 `Object` 參考的類型資訊。
  - `NON_CONCRETE_AND_ARRAYS`：包含抽象/非具體類型及陣列的類型資訊。
  - `NON_FINAL`：包含非最終類別的類型資訊。

使用範例：
```java
import com.fasterxml.jackson.databind.ObjectMapper;
import static com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping;

ObjectMapper mapper = new ObjectMapper();
mapper.activateDefaultTyping(DefaultTyping.NON_CONCRETE_AND_ARRAYS);
```

若未啟用，當序列化包含混合類型的 `List<Object>` 時，JSON 可能會省略類型細節，導致反序列化錯誤。啟用後，JSON 會包含類型提示，例如：`[{"@class": "java.lang.String", "value": "hello"}, {"@class": "java.lang.Integer", "value": 42}]`。

### 安全性考量與限制

- **漏洞風險**：盲目啟用預設類型處理（特別是舊版的 `enableDefaultTyping()`）可能使系統面臨攻擊（如資料提取），因為它允許透過特製 JSON 反序列化任意類別。新版 Jackson 預設會限制此功能，僅允許常見類型除非自訂。
- **適用場景**：最適合處理多態資料的可信任環境（例如內部 API）。對於公開 API，建議使用明確的類型註解或自訂序列化器/反序列化器以提升安全性。
- **效能影響**：因嵌入類型資訊而增加輕微開銷，會擴大 JSON 體積。

若此內容涉及其他「物件映射器」（例如 Elasticsearch 或其他函式庫），請提供更多背景資料以獲取針對性說明。完整詳情請參閱 Jackson 官方文件。