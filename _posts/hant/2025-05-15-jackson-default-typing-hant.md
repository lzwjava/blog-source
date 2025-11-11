---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Jackson 預設類型設定詳解與停用方法
translated: true
type: note
---

在 Jackson（`com.fasterxml.jackson.databind` 函式庫）中，**預設型別標記**是 `ObjectMapper` 的一項功能，會自動在序列化的 JSON 中包含型別元數據（如 `@class` 或 `@type`），以便能將物件反序列化回其原始的多型型別。

舉例來說，如果你序列化一個包含 `Dog` 和 `Cat` 的 `List<Animal>`，預設型別標記會添加額外的 JSON 欄位，讓 Jackson 知道之後要重新實例化哪個子類別。

---

### 停用機制說明

當你**停用預設型別標記**時，Jackson 會停止注入那些額外的型別元數據欄位。這意味著：

* JSON 輸出將更「整潔」，不帶有 `@class`/`@type` 提示。
* 在反序列化時，Jackson 只能使用宣告的靜態型別（你傳入的目標型別）重建物件，而非原始的執行時期型別。
* 除非你明確配置 `@JsonTypeInfo`、`@JsonSubTypes` 或自訂模組，否則任何多型使用情境都會失效。

---

### 相關方法

* **啟用**（2.10 之前版本樣式）：

  ```java
  objectMapper.enableDefaultTyping();
  ```

  （已棄用，因其過於寬鬆且會帶來安全風險。）

* **停用**：

  ```java
  objectMapper.disableDefaultTyping();
  ```

  或在較新版本（2.10+）中，你可以呼叫：

  ```java
  objectMapper.activateDefaultTyping(PolymorphicTypeValidator, ObjectMapper.DefaultTyping.NON_FINAL);
  ```

  若要*停用*，你只需**不呼叫**此方法（除非你啟用，否則不會有預設型別標記），或者可以呼叫：

  ```java
  objectMapper.deactivateDefaultTyping();
  ```

---

### 安全性與原理

* 在現代 Jackson 版本中，**預設型別標記預設為停用**，因為它可能被惡意利用（攻擊者可能構造會實例化危險類別的 JSON）。
* 如果你停用它，Jackson 會以「更安全」的模式運行，反序列化僅對你明確綁定的型別有效，而非任意的執行時期型別。
* 如果你需要多型支援，你應該使用 `@JsonTypeInfo` 註解你的類別，而非依賴全域的預設型別標記。

---

✅ **簡而言之：**
停用預設型別標記是告訴 Jackson **不要**在 JSON 中包含型別元數據，這意味著它不會在反序列化時自動重建多型子類別。這會降低靈活性，但更安全且能保持 JSON 的簡潔。

需要我展示**啟用與停用預設型別標記的 JSON 前後對照範例**嗎？