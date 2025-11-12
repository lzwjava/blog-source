---
audio: false
generated: true
lang: hant
layout: post
title: Javax JSON 處理
translated: true
type: note
---

我將解釋如何使用 `javax.json` 套件，這是 Java API for JSON Processing (JSON-P) 的一部分，用於在 Java 中處理 JSON 資料。以下是完整指南：

1. 首先，將依賴項添加到你的專案中（如果使用 Maven）：
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- 實作（如 GlassFish） -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. 使用 `javax.json` 的基本範例：

a) 建立 JSON 物件：
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // 建立 JSON 物件
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

b) 建立 JSON 陣列：
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) 從字串解析 JSON：
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// 存取數值
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) 將 JSON 寫入字串：
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

3. 主要類別和介面：
- `Json`：用於建立 JSON 建構器和讀取器的工廠類別
- `JsonObject`：代表 JSON 物件
- `JsonArray`：代表 JSON 陣列
- `JsonObjectBuilder`：建構 JSON 物件
- `JsonArrayBuilder`：建構 JSON 陣列
- `JsonReader`：從輸入源讀取 JSON
- `JsonWriter`：將 JSON 寫入輸出源

4. 處理不同的 JSON 數值類型：
```java
JsonObject obj = // ... 某個 JSON 物件
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

5. 串流 API 範例（適用於大型 JSON）：
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
- 完成後務必關閉 `JsonReader`、`JsonWriter` 和 `JsonParser`
- 處理 `javax.json.JsonException` 以應對可能的解析錯誤
- 對於大型 JSON 文件，使用串流 API (`JsonParser`)
- 此 API 是不可變的 - 建構器會建立新實例

這涵蓋了使用 `javax.json` 的基礎知識。如果你需要更具體的範例或有特定的使用案例，請告訴我！