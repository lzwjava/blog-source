---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的 JSON 處理
translated: true
type: note
---

若要在 Java 專案中使用 `com.fasterxml.jackson` 套件進行 JSON 處理，您可以利用廣泛用於 Java 物件與 JSON 互相轉換的 Jackson 函式庫。以下是以 Maven 專案為基礎的逐步指南，重點介紹提供 JSON 資料綁定高階功能的 `jackson-databind` 模組。

---

### 1. 將 Jackson 相依性加入專案
要使用 `com.fasterxml.jackson` 套件，您需要在專案中加入 Jackson 函式庫。若使用 Maven，請在 `pom.xml` 檔案中加入以下相依性：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- 請替換為最新版本 -->
</dependency>
```

- **注意**：請查閱 [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) 取得最新版本，可能較 2.12.5 更新。
- `jackson-databind` 模組依賴 `jackson-core` 與 `jackson-annotations`，因此除非有特殊需求，否則無需單獨添加。

加入相依性後，執行 `mvn install` 或在 IDE 中重新整理專案以下載函式庫。

---

### 2. 建立 `ObjectMapper` 實例
來自 `com.fasterxml.jackson.databind` 套件的 `ObjectMapper` 類別是進行 JSON 操作的主要工具。它具備執行緒安全性且實例化耗費資源，建議建立單個可重複使用的實例：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

將此程式碼置於執行 JSON 操作的類別中。

---

### 3. 將 Java 物件轉換為 JSON（序列化）
使用 `writeValueAsString` 方法將 Java 物件轉換為 JSON 字串。以下為範例：

#### 定義 Java 類別
建立包含需序列化欄位的類別。請確保包含 getter 與 setter 方法，因 Jackson 預設透過這些方法存取私有欄位：

```java
public class MyClass {
    private String field1;
    private int field2;

    public MyClass(String field1, int field2) {
        this.field1 = field1;
        this.field2 = field2;
    }

    public String getField1() {
        return field1;
    }

    public void setField1(String field1) {
        this.field1 = field1;
    }

    public int getField2() {
        return field2;
    }

    public void setField2(int field2) {
        this.field2 = field2;
    }
}
```

#### 序列化為 JSON
使用 `ObjectMapper` 將物件轉換為 JSON：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        MyClass obj = new MyClass("value1", 123);
        String json = mapper.writeValueAsString(obj);
        System.out.println(json);
    }
}
```

**輸出**：
```json
{"field1":"value1","field2":123}
```

---

### 4. 將 JSON 轉換為 Java 物件（反序列化）
使用 `readValue` 方法將 JSON 字串轉換回 Java 物件：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // 輸出 "value1"
    }
}
```

- **錯誤處理**：若 JSON 格式錯誤或與類別結構不匹配，`readValue` 方法會拋出 `JsonProcessingException`（受檢異常）。請使用 try-catch 區塊處理或在方法簽名中宣告：

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. 使用註解自訂 JSON 處理
Jackson 提供註解以自訂欄位的序列化或反序列化方式。將來自 `com.fasterxml.jackson.annotation` 的這些註解加入您的類別：

#### 重新命名欄位
使用 `@JsonProperty` 將 Java 欄位映射至不同的 JSON 欄位名稱：

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // 建構子、getter、setter
}
```

**輸出**：
```json
{"name":"value1","field2":123}
```

#### 忽略欄位
使用 `@JsonIgnore` 排除序列化中的欄位：

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // 建構子、getter、setter
}
```

**輸出**：
```json
{"field1":"value1"}
```

#### 格式化日期
使用 `@JsonFormat` 指定日期的序列化方式：

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // 建構子、getter、setter
}
```

**輸出**（範例）：
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. 處理進階情境
以下是一些可能實用的進階功能：

#### 美化 JSON 輸出
使用 `writerWithDefaultPrettyPrinter` 產生可讀性高的 JSON 輸出：

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**輸出**：
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### 忽略未知屬性
若 JSON 包含 Java 類別中不存在的欄位，可設定 `ObjectMapper` 忽略它們：

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### 處理檔案
讀取或寫入檔案：

```java
// 寫入檔案
mapper.writeValue(new File("output.json"), obj);

// 從檔案讀取
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### 處理清單或泛型
對於集合，使用 `TypeReference` 保留泛型型別資訊：

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. 使用 `JsonNode` 進行動態 JSON 操作
若不想將 JSON 映射至特定類別，可使用 `JsonNode` 進行樹狀結構操作：

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // 傳回 "value1"
```

亦可動態建立 JSON：

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### 總結
使用 `com.fasterxml.jackson` 套件的步驟：
1. 將 `jackson-databind` 相依性加入 `pom.xml`
2. 建立單個可重複使用的 `ObjectMapper` 實例
3. 使用 `writeValueAsString` 將 Java 物件轉為 JSON，使用 `readValue` 將 JSON 轉為 Java 物件
4. 透過 `@JsonProperty`、`@JsonIgnore` 與 `@JsonFormat` 等註解自訂行為
5. 處理異常（例如 `JsonProcessingException`）並根據需求設定 `ObjectMapper`（例如忽略未知屬性）
6. 探索進階功能如美化輸出、檔案 I/O 或使用 `JsonNode` 進行動態 JSON 處理

透過這些步驟，您即可使用 Jackson 函式庫在 Java 應用程式中有效處理 JSON。