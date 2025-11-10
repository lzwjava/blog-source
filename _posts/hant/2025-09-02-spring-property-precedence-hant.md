---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 春季屬性優先規則詳解
translated: true
type: note
---

在 Spring 中，當您的配置來源（例如 `application.properties`、`application.yml`、環境變數、命令列參數等）出現**重複的屬性鍵**時，**具有最高優先權的最後一個配置來源會生效**。

以下是詳細運作方式：

### 1. 屬性來源排序

Spring Boot 採用明確定義的**屬性來源順序**。例如：

* 命令列參數
* `application.properties` / `application.yml`（先加載特定配置檔的，然後是預設配置）
* 環境變數
* 系統屬性
* 程式碼中的預設值（`@Value("${...:default}")`）

如果相同的屬性鍵出現在多個來源中，Spring 會選取**優先權最高來源**中的值。

### 2. 在同一檔案內

如果您在**單一檔案**（如 `application.properties`）中重複定義相同的屬性鍵，Spring 會使用**最後宣告的項目**。
範例（`application.properties`）：

```properties
server.port=8080
server.port=9090
```

此處 `server.port=9090` 會生效。

### 3. 跨多個檔案

如果您在 `application.properties` 和 `application-dev.properties` 中定義了相同屬性，並且啟用了 `dev` 配置檔，則 `application-dev.properties` 中的值會覆寫預設值。

### 4. 使用 `@PropertySource`

如果您透過 `@PropertySource` 載入多個屬性檔案，宣告順序至關重要。除非標記為 `ignoreResourceNotFound` 或明確控制優先權，否則後載入的檔案可以覆寫先前的值。

---

✅ **總結：**

* Spring 透過**來源優先權**來解析屬性。
* 在**同一檔案內**，**最後定義的鍵值**會生效。
* 跨檔案/配置檔時，**啟用配置檔或後載入檔案的屬性**會覆寫先前的值。

您是否需要我展示**確切的 Spring Boot 屬性優先權層級（從最高到最低）**？這能更清晰地呈現屬性覆寫的發生位置。