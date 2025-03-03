---
audio: false
generated: true
lang: zh
layout: post
title: Javax Json 处理
translated: true
---

我将解释如何使用 `javax.json` 包，它是 Java API for JSON Processing (JSON-P) 的一部分，用于在 Java 中处理 JSON 数据。以下是一个全面的指南：

1. 首先，将依赖项添加到您的项目中（如果使用 Maven）：
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- 实现（如 GlassFish） -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. 使用 `javax.json` 的基本示例：

a) 创建 JSON 对象：
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // 创建 JSON 对象
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

b) 创建 JSON 数组：
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) 从字符串解析 JSON：
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// 访问值
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) 将 JSON 写入字符串：
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

3. 关键类和接口：
- `Json`：用于创建 JSON 构建器和读取器的工厂类
- `JsonObject`：表示 JSON 对象
- `JsonArray`：表示 JSON 数组
- `JsonObjectBuilder`：构建 JSON 对象
- `JsonArrayBuilder`：构建 JSON 数组
- `JsonReader`：从输入源读取 JSON
- `JsonWriter`：将 JSON 写入输出源

4. 处理不同的 JSON 值类型：
```java
JsonObject obj = // ... 某个 JSON 对象
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// 检查键是否存在并处理 null
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. 流 API 示例（用于大型 JSON）：
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
- 完成后始终关闭 `JsonReader`、`JsonWriter` 和 `JsonParser`
- 处理 `javax.json.JsonException` 以应对潜在的解析错误
- 对于大型 JSON 文档，使用流 API（`JsonParser`）
- API 是不可变的 - 构建器创建新实例

这涵盖了 `javax.json` 的基本用法。如果您需要更具体的示例或有特定的用例，请告诉我！