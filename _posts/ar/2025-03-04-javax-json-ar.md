---
audio: false
generated: true
lang: ar
layout: post
title: معالجة جافا سون
translated: true
type: note
---

سأشرح كيفية استخدام حزمة `javax.json`، والتي هي جزء من Java API لمعالجة JSON (JSON-P) للعمل مع بيانات JSON في جافا. إليك دليل شامل:

1. أولاً، أضف الاعتماد إلى مشروعك (إذا كنت تستخدم Maven):
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

أ) إنشاء كائن JSON:
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

ب) إنشاء مصفوفة JSON:
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

ج) تحليل JSON من سلسلة نصية:
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

د) كتابة JSON إلى سلسلة نصية:
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

3. الفئات والواجهات الرئيسية:
- `Json`: فئة المصنع لإنشاء بائعي JSON والقراء
- `JsonObject`: تمثل كائن JSON
- `JsonArray`: تمثل مصفوفة JSON
- `JsonObjectBuilder`: تبني كائنات JSON
- `JsonArrayBuilder`: تبني مصفوفات JSON
- `JsonReader`: تقرأ JSON من مصدر الإدخال
- `JsonWriter`: تكتب JSON إلى مصدر الإخراج

4. التعامل مع أنواع قيم JSON المختلفة:
```java
JsonObject obj = // ... بعض كائن JSON
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// التحقق من وجود المفتاح والتعامل مع القيمة الفارغة
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. مثال على واجهة برمجة التطبيقات المتدفقة (لـ JSON كبير):
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
- أغلق دائمًا `JsonReader` و`JsonWriter` و`JsonParser` عند الانتهاء
- تعامل مع `javax.json.JsonException` للأخطاء المحتملة في التحليل
- استخدم واجهة برمجة التطبيقات المتدفقة (`JsonParser`) لمستندات JSON الكبيرة
- واجهة برمجة التطبيقات غير قابلة للتغيير - البائعون ينشئون مثيلات جديدة

هذا يغطي أساسيات استخدام `javax.json`. أعلمني إذا كنت بحاجة إلى أمثلة أكثر تحديدًا أو إذا كان لديك حالة استخدام معينة في ذهنك!