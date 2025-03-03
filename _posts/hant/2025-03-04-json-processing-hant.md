---
audio: false
generated: true
lang: hant
layout: post
title: JSON 处理技巧
translated: true
---

在 Java 專案中使用 `com.fasterxml.jackson` 套件進行 JSON 處理，可以利用 Jackson 圖書館，這是一個廣泛用於將 Java 物件轉換為 JSON 以及反向操作的工具。以下是一個逐步指南，假設你正在使用基於 Maven 的專案。這個指南專注於 `jackson-databind` 模組，它提供了高級功能來進行 JSON 數據綁定。

---

### 1. 將 Jackson 依賴項添加到專案中
要使用 `com.fasterxml.jackson` 套件，你需要在專案中包含 Jackson 圖書館。如果你使用 Maven，將以下依賴項添加到你的 `pom.xml` 文件中：

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- 替換為最新版本 -->
</dependency>
```

- **注意**：檢查 [Maven 中央倉庫](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) 以獲取最新版本，因為它可能比 2.12.5 更新。
- `jackson-databind` 模組依賴於 `jackson-core` 和 `jackson-annotations`，所以除非你有特定需求，否則不需要單獨添加它們。

添加依賴項後，運行 `mvn install` 或在你的 IDE 中刷新專案以下載圖書館。

---

### 2. 創建 `ObjectMapper` 實例
`ObjectMapper` 類來自 `com.fasterxml.jackson.databind` 套件，是進行 JSON 操作的主要工具。它是線程安全的，並且資源密集型，因此最好創建一個單一、可重用的實例：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

將這段代碼放在你將執行 JSON 操作的類中。

---

### 3. 將 Java 物件轉換為 JSON（序列化）
要將 Java 物件轉換為 JSON 字符串，使用 `writeValueAsString` 方法。以下是一個範例：

#### 定義一個 Java 類
創建一個包含你想要序列化的字段的類。確保它有 getter 和 setter，因為 Jackson 默認使用它們來訪問私有字段：

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
要將 JSON 字符串轉換回 Java 物件，使用 `readValue` 方法：

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // 打印 "value1"
    }
}
```

- **錯誤處理**：`readValue` 方法在 JSON 格式不正確或不匹配類結構時會拋出 `JsonProcessingException`（一個檢查異常）。使用 try-catch 塊或在方法簽名中聲明它：

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. 使用註解自定義 JSON 處理
Jackson 提供了註解來自定義字段的序列化或反序列化方式。從 `com.fasterxml.jackson.annotation` 套件中將這些註解添加到你的類中：

#### 重命名一個字段
使用 `@JsonProperty` 將 Java 字段映射到不同的 JSON 字段名稱：

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // 构造函數、getter、setter
}
```

**輸出**：
```json
{"name":"value1","field2":123}
```

#### 忽略一個字段
使用 `@JsonIgnore` 從序列化中排除一個字段：

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // 构造函數、getter、setter
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
    // 构造函數、getter、setter
}
```

**輸出**（範例）：
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. 處理高級情況
以下是一些你可能會發現有用的附加功能：

#### 美化 JSON
為了可讀的 JSON 輸出，使用 `writerWithDefaultPrettyPrinter`：

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
如果 JSON 包含不在你的 Java 類中的字段，配置 `ObjectMapper` 以忽略它們：

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### 使用文件
從文件讀取或寫入：

```java
// 寫入文件
mapper.writeValue(new File("output.json"), obj);

// 從文件讀取
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### 處理列表或泛型
對於集合，使用 `TypeReference` 來保留泛型類型信息：

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. 使用 `JsonNode` 進行動態 JSON 操作
如果你不想將 JSON 映射到特定類，使用 `JsonNode` 進行基於樹的方法：

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // 返回 "value1"
```

你也可以動態構建 JSON：

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### 摘要
要使用 `com.fasterxml.jackson` 套件：
1. 將 `jackson-databind` 依賴項添加到你的 `pom.xml`。
2. 創建一個單一的 `ObjectMapper` 實例以重用。
3. 使用 `writeValueAsString` 將 Java 物件轉換為 JSON，使用 `readValue` 將 JSON 轉換為 Java 物件。
4. 使用註解（如 `@JsonProperty`、`@JsonIgnore` 和 `@JsonFormat`）自定義行為。
5. 處理異常（例如 `JsonProcessingException`）並配置 `ObjectMapper` 以滿足特定需求（例如忽略未知屬性）。
6. 探索高級功能，如美化、文件 I/O 或 `JsonNode` 以進行動態 JSON 處理。

通過這些步驟，你可以在 Java 應用程序中有效地處理 JSON 使用 Jackson 圖書館。