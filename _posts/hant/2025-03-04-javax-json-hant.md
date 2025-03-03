---
audio: false
generated: true
lang: hant
layout: post
title: Javax Json 处理
translated: true
---

我將解釋如何使用 `javax.json` 套件，這是 Java API for JSON Processing (JSON-P) 的一部分，用於在 Java 中處理 JSON 數據。以下是一個全面的指南：

1. 首先，將依賴項添加到您的項目中（如果使用 Maven）：
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- 實現（如 GlassFish） -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. 使用 `javax.json` 的基本示例：

a) 創建 JSON 對象：
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // 創建 JSON 對象
        JsonObject jsonObject = Json.createObjectBuilder()
            .add("name", "John Doe")
            .add("age", 30)
            .add("isStudent", false)
            .add("address", Json.createObjectBuilder()
                .add("street", "123 Main St")
                .add("city", "New York"))
            .build();

        System.out.println(jsonObject.toString());
    }
}
```

b) 創建 JSON 數組：
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) 從字符串解析 JSON：
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// 訪問值
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) 將 JSON 寫入字符串：
```java
import javax.json.JsonWriter;
import java.io.StringWriter;

JsonObject jsonObject = Json.createObjectBuilder()
    .add("title", "Example")
    .build();

StringWriter stringWriter = new StringWriter();
JsonWriter jsonWriter = Json.createWriter(stringWriter);
jsonWriter.writeObject(jsonObject);
jsonWriter.close();

String result = stringWriter.toString();
```

3. 關鍵類和接口：
- `Json`：用於創建 JSON 建造者和讀取器的工廠類
- `JsonObject`：表示 JSON 對象
- `JsonArray`：表示 JSON 數組
- `JsonObjectBuilder`：構建 JSON 對象
- `JsonArrayBuilder`：構建 JSON 數組
- `JsonReader`：從輸入源讀取 JSON
- `JsonWriter`：將 JSON 寫入輸出源

4. 處理不同的 JSON 值類型：
```java
JsonObject obj = // ... 某個 JSON 對象
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// 檢查鍵是否存在並處理 null
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. 流 API 示例（用於大型 JSON）：
```java
import javax.json.stream.JsonParser;
import java.io.StringReader;

String json = "{\"name\":\"John\",\"scores\":[1,2,3]}";
JsonParser parser = Json.createParser(new StringReader(json));
while (parser.hasNext()) {
    JsonParser.Event event = parser.next();
    switch (event) {
        case KEY_NAME:
            System.out.println("Key: " + parser.getString());
            break;
        case VALUE_STRING:
            System.out.println("String: " + parser.getString());
            break;
        case VALUE_NUMBER:
            System.out.println("Number: " + parser.getBigDecimal());
            break;
    }
}
parser.close();
```

提示：
- 完成後始終關閉 `JsonReader`、`JsonWriter` 和 `JsonParser`
- 為潛在的解析錯誤處理 `javax.json.JsonException`
- 使用流 API (`JsonParser`) 來處理大型 JSON 文檔
- API 是不可變的 - 建造者創建新實例

這涵蓋了使用 `javax.json` 的基本知識。如果您需要更具體的示例或有特定的使用情況，請告訴我！