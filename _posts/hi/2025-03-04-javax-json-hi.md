---
audio: false
generated: true
lang: hi
layout: post
title: जावैक्स जेएसओएन प्रोसेसिंग
translated: true
type: note
---

मैं `javax.json` पैकेज के उपयोग के बारे में समझाऊंगा, जो JSON डेटा के साथ काम करने के लिए Java API for JSON Processing (JSON-P) का हिस्सा है। यहाँ एक व्यापक गाइड है:

1. सबसे पहले, अपने प्रोजेक्ट में डिपेंडेंसी जोड़ें (यदि Maven का उपयोग कर रहे हैं):
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

2. `javax.json` के उपयोग के बुनियादी उदाहरण:

a) JSON ऑब्जेक्ट बनाना:
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

b) JSON ऐरे बनाना:
```java
JsonArray jsonArray = Json.createArrayBuilder()
    .add("Apple")
    .add("Banana")
    .add(Json.createObjectBuilder()
        .add("name", "Orange")
        .add("price", 0.99))
    .build();
```

c) स्ट्रिंग से JSON पार्स करना:
```java
import javax.json.JsonReader;
import java.io.StringReader;

String jsonString = "{\"name\":\"Jane\",\"age\":25}";
JsonReader jsonReader = Json.createReader(new StringReader(jsonString));
JsonObject parsedObject = jsonReader.readObject();
jsonReader.close();

// वैल्यूज़ एक्सेस करें
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

3. मुख्य क्लासेस और इंटरफेस:
- `Json`: JSON बिल्डर्स और रीडर्स बनाने के लिए फैक्टरी क्लास
- `JsonObject`: एक JSON ऑब्जेक्ट को रिप्रेजेंट करता है
- `JsonArray`: एक JSON ऐरे को रिप्रेजेंट करता है
- `JsonObjectBuilder`: JSON ऑब्जेक्ट्स बनाता है
- `JsonArrayBuilder`: JSON ऐरे बनाता है
- `JsonReader`: इनपुट सोर्स से JSON पढ़ता है
- `JsonWriter`: आउटपुट सोर्स को JSON लिखता है

4. विभिन्न JSON वैल्यू टाइप्स को हैंडल करना:
```java
JsonObject obj = // ... कोई JSON ऑब्जेक्ट
String stringValue = obj.getString("key");
int intValue = obj.getInt("key");
boolean boolValue = obj.getBoolean("key");
JsonObject nestedObj = obj.getJsonObject("key");
JsonArray arrayValue = obj.getJsonArray("key");

// जाँचें कि key मौजूद है और null को हैंडल करें
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

सुझाव:
- काम पूरा होने पर `JsonReader`, `JsonWriter`, और `JsonParser` को हमेशा बंद करें
- संभावित पार्सिंग एरर के लिए `javax.json.JsonException` को हैंडल करें
- बड़े JSON डॉक्यूमेंट्स के लिए स्ट्रीमिंग API (`JsonParser`) का उपयोग करें
- API इम्यूटेबल है - बिल्डर्स नए इंस्टेंस बनाते हैं

यह `javax.json` के उपयोग की बुनियादी बातों को कवर करता है। यदि आपको अधिक विशिष्ट उदाहरणों की आवश्यकता है या आपके पास कोई विशेष उपयोग का मामला है तो मुझे बताएं!