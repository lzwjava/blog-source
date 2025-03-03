---
audio: false
generated: true
lang: ar
layout: post
title: تسجيل JSON في Javax
translated: true
---

سأشرح كيفية استخدام حزمة `javax.json`، التي هي جزء من API Java لـ معالجة JSON (JSON-P) للعمل مع بيانات JSON في Java. إليك دليل شامل:

1. أولاً، أضف التبعية إلى مشروعك (إذا كنت تستخدم Maven):
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- التنفيذ (مثل GlassFish) -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. أمثلة أساسية لاستخدام `javax.json`:

a) إنشاء كائن JSON:
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // إنشاء كائن JSON
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

b) إنشاء مصفوفة JSON:
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) تحليل JSON من نص:
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// الوصول إلى القيم
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) كتابة JSON إلى نص:
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

3. الفئات والأواجه الرئيسية:
- `Json`: فئة مصنع لإنشاء مصنع JSON وقراء
- `JsonObject`: يمثل كائن JSON
- `JsonArray`: يمثل مصفوفة JSON
- `JsonObjectBuilder`: يبني كائنات JSON
- `JsonArrayBuilder`: يبني مصفوفات JSON
- `JsonReader`: يقرأ JSON من مصدر الإدخال
- `JsonWriter`: يكتب JSON إلى مصدر الإخراج

4. معالجة أنواع القيم JSON المختلفة:
```java
JsonObject obj = // ... كائن JSON ما
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// التحقق من وجود المفتاح وعلاج القيمة النول
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. مثال على API التدفق (للJSON الكبير):
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

نصائح:
- أغلق دائمًا `JsonReader` و `JsonWriter` و `JsonParser` عند الانتهاء
- معالجة `javax.json.JsonException` لخطأ تحليل محتمل
- استخدم API التدفق (`JsonParser`) للوثائق JSON الكبيرة
- API غير قابل للتعديل - مصنع إنشاء نسخ جديدة

هذا يغطي الأساسيات لاستخدام `javax.json`. أخبرني إذا كنت تحتاج إلى أمثلة أكثر تحديدًا أو لديك حالة استخدام معينة في ذهنك!