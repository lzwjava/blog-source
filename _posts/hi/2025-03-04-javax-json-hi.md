---
audio: false
generated: true
lang: hi
layout: post
title: Javax Json Processing का अनुवाद
translated: true
---

मैं `javax.json` पैकेज का उपयोग करने की व्याख्या करूँगा, जो Java API for JSON Processing (JSON-P) का हिस्सा है, ताकि Java में JSON डेटा के साथ काम किया जा सके। यहाँ एक व्यापक मार्गदर्शिका है:

1. पहले, अपने प्रोजेक्ट में निर्भरता जोड़ें (Maven का उपयोग करने पर):
```xml
<dependency>
    <groupId>javax.json</groupId>
    <artifactId>javax.json-api</artifactId>
    <version>1.1.4</version>
</dependency>
<!-- Implementation (like GlassFish) -->
<dependency>
    <groupId>org.glassfish</groupId>
    <artifactId>javax.json</artifactId>
    <version>1.1.4</version>
</dependency>
```

2. `javax.json` का उपयोग करने के कुछ मूल उदाहरण:

a) एक JSON ऑब्जेक्ट बनाना:
```java
import javax.json.Json;
import javax.json.JsonObject;
import javax.json.JsonArray;

public class JsonExample {
    public static void main(String[] args) {
        // एक JSON ऑब्जेक्ट बनाएं
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

b) एक JSON एर्रे बनाना:
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) स्ट्रिंग से JSON पर्स करना:
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// मानों तक पहुंचें
String name = parsedObject.getString("name");
int age = parsedObject.getInt("age");
```

d) JSON को स्ट्रिंग में लिखना:
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

3. मुख्य क्लास और इंटरफेस:
- `Json`: JSON बिल्डर और रीडर बनाने के लिए फैक्टरी क्लास
- `JsonObject`: एक JSON ऑब्जेक्ट का प्रतिनिधित्व करता है
- `JsonArray`: एक JSON एर्रे का प्रतिनिधित्व करता है
- `JsonObjectBuilder`: JSON ऑब्जेक्ट बनाता है
- `JsonArrayBuilder`: JSON एर्रे बनाता है
- `JsonReader`: इनपुट स्रोत से JSON पढ़ता है
- `JsonWriter`: आउटपुट स्रोत में JSON लिखता है

4. विभिन्न JSON मान प्रकारों का हैंडल करना:
```java
JsonObject obj = // ... कोई JSON ऑब्जेक्ट
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// चेक करें कि की है और नल का हैंडल करें
if (obj.containsKey("key") && !obj.isNull("key")) {
    String value = obj.getString("key");
}
```

5. स्ट्रीमिंग API उदाहरण (बड़े JSON के लिए):
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

टिप्स:
- हमेशा `JsonReader`, `JsonWriter`, और `JsonParser` को खत्म होने पर बंद करें
- `javax.json.JsonException` को संभालें संभव पर्सिंग त्रुटियों के लिए
- बड़े JSON दस्तावेज़ों के लिए स्ट्रीमिंग API (`JsonParser`) का उपयोग करें
- API अचल है - बिल्डर नए इंस्टेंस बनाते हैं

यह `javax.json` का उपयोग करने के मूल तत्वों को कवर करता है। मुझे बताएं अगर आपको अधिक विशिष्ट उदाहरण चाहिए या कोई विशेष उपयोग मामला है!