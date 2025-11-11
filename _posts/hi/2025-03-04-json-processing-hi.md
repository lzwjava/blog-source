---
audio: false
generated: true
lang: hi
layout: post
title: जावा में जेसन प्रोसेसिंग
translated: true
type: note
---

`com.fasterxml.jackson` पैकेज का उपयोग JSON प्रोसेसिंग के लिए Java प्रोजेक्ट में करने के लिए, आप Jackson लाइब्रेरी का लाभ उठा सकते हैं, जिसका व्यापक रूप से Java ऑब्जेक्ट्स को JSON में और इसके विपरीत कनवर्ट करने के लिए उपयोग किया जाता है। नीचे आरंभ करने के लिए एक चरण-दर-चरण मार्गदर्शिका दी गई है, यह मानते हुए कि आप एक Maven-आधारित प्रोजेक्ट के साथ काम कर रहे हैं। यह मार्गदर्शिका `jackson-databind` मॉड्यूल पर केंद्रित है, जो JSON डेटाबाइंडिंग के लिए उच्च-स्तरीय कार्यक्षमता प्रदान करता है।

---

### 1. अपने प्रोजेक्ट में Jackson डिपेंडेंसी जोड़ें
`com.fasterxml.jackson` पैकेज का उपयोग करने के लिए, आपको अपने प्रोजेक्ट में Jackson लाइब्रेरी को शामिल करना होगा। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` फ़ाइल में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- नवीनतम संस्करण के साथ प्रतिस्थापित करें -->
</dependency>
```

- **नोट**: नवीनतम संस्करण के लिए [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) जांचें, क्योंकि यह 2.12.5 से नया हो सकता है।
- `jackson-databind` मॉड्यूल `jackson-core` और `jackson-annotations` पर निर्भर करता है, इसलिए जब तक आपकी कोई विशिष्ट आवश्यकता न हो, आपको उन्हें अलग से जोड़ने की आवश्यकता नहीं है।

डिपेंडेंसी जोड़ने के बाद, लाइब्रेरी डाउनलोड करने के लिए `mvn install` चलाएं या अपने IDE में अपना प्रोजेक्ट रीफ्रेश करें।

---

### 2. एक `ObjectMapper` इंस्टेंस बनाएँ
`com.fasterxml.jackson.databind` पैकेज से `ObjectMapper` क्लास JSON ऑपरेशन्स के लिए प्राथमिक उपकरण है। यह थ्रेड-सुरक्षित है और इंस्टेंटिएट करने के लिए संसाधन-गहन है, इसलिए एक एकल, पुन: प्रयोज्य इंस्टेंस बनाना सर्वोत्तम है:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

इसे एक क्लास में रखें जहाँ आप JSON ऑपरेशन्स करेंगे।

---

### 3. एक Java ऑब्जेक्ट को JSON में कनवर्ट करें (सीरियलाइज़ेशन)
किसी Java ऑब्जेक्ट को JSON स्ट्रिंग में बदलने के लिए, `writeValueAsString` मेथड का उपयोग करें। यहाँ एक उदाहरण दिया गया है:

#### एक Java क्लास परिभाषित करें
उन फ़ील्ड्स के साथ एक क्लास बनाएँ जिन्हें आप सीरियलाइज़ करना चाहते हैं। सुनिश्चित करें कि इसमें गेटर्स और सेटर्स हैं, क्योंकि Jackson डिफ़ॉल्ट रूप से प्राइवेट फ़ील्ड्स तक पहुँचने के लिए इनका उपयोग करता है:

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

#### JSON में सीरियलाइज़ करें
ऑब्जेक्ट को JSON में बदलने के लिए `ObjectMapper` का उपयोग करें:

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

**आउटपुट**:
```json
{"field1":"value1","field2":123}
```

---

### 4. JSON को Java ऑब्जेक्ट में कनवर्ट करें (डी-सीरियलाइज़ेशन)
JSON स्ट्रिंग को वापस Java ऑब्जेक्ट में बदलने के लिए, `readValue` मेथड का उपयोग करें:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // "value1" प्रिंट करता है
    }
}
```

- **एरर हैंडलिंग**: यदि JSON खराब संरचित है या क्लास संरचना से मेल नहीं खाती है, तो `readValue` मेथड `JsonProcessingException` (एक checked exception) थ्रो करती है। इसे try-catch ब्लॉक से हैंडल करें या मेथड सिग्नेचर में डिक्लेयर करें:

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. एनोटेशन्स के साथ JSON प्रोसेसिंग को कस्टमाइज़ करें
Jackson यह कस्टमाइज़ करने के लिए एनोटेशन्स प्रदान करता है कि फ़ील्ड्स कैसे सीरियलाइज़ या डी-सीरियलाइज़ होते हैं। इन एनोटेशन्स को `com.fasterxml.jackson.annotation` से अपनी क्लास में जोड़ें:

#### एक फ़ील्ड का नाम बदलें
किसी Java फ़ील्ड को एक अलग JSON फ़ील्ड नाम से मैप करने के लिए `@JsonProperty` का उपयोग करें:

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // Constructor, getters, setters
}
```

**आउटपुट**:
```json
{"name":"value1","field2":123}
```

#### एक फ़ील्ड को अनदेखा करें
किसी फ़ील्ड को सीरियलाइज़ेशन से बाहर करने के लिए `@JsonIgnore` का उपयोग करें:

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // Constructor, getters, setters
}
```

**आउटपुट**:
```json
{"field1":"value1"}
```

#### डेट्स को फॉर्मेट करें
यह निर्दिष्ट करने के लिए कि डेट्स कैसे सीरियलाइज़ होते हैं, `@JsonFormat` का उपयोग करें:

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // Constructor, getters, setters
}
```

**आउटपुट** (उदाहरण):
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. उन्नत परिदृश्यों को हैंडल करें
यहाँ कुछ अतिरिक्त फीचर्स दिए गए हैं जो आपके लिए उपयोगी हो सकते हैं:

#### सुंदर-प्रिंटेड JSON
पठनीय JSON आउटपुट के लिए, `writerWithDefaultPrettyPrinter` का उपयोग करें:

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**आउटपुट**:
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### अज्ञात प्रॉपर्टीज़ को अनदेखा करें
यदि JSON में ऐसे फ़ील्ड्स हैं जो आपकी Java क्लास में मौजूद नहीं हैं, तो उन्हें अनदेखा करने के लिए `ObjectMapper` को कॉन्फ़िगर करें:

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### फ़ाइलों के साथ काम करें
किसी फ़ाइल से पढ़ें या किसी फ़ाइल में लिखें:

```java
// फ़ाइल में लिखें
mapper.writeValue(new File("output.json"), obj);

// फ़ाइल से पढ़ें
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### लिस्ट्स या जेनेरिक्स को हैंडल करें
कलेक्शन्स के लिए, जेनेरिक टाइप जानकारी को संरक्षित रखने के लिए `TypeReference` का उपयोग करें:

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. `JsonNode` के साथ डायनामिक JSON मैनिपुलेशन
यदि आप JSON को किसी विशिष्ट क्लास से मैप नहीं करना चाहते हैं, तो ट्री-आधारित दृष्टिकोण के लिए `JsonNode` का उपयोग करें:

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // "value1" रिटर्न करता है
```

आप डायनामिक रूप से JSON भी बना सकते हैं:

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### सारांश
`com.fasterxml.jackson` पैकेज का उपयोग करने के लिए:
1. अपनी `pom.xml` में `jackson-databind` डिपेंडेंसी जोड़ें।
2. पुन: उपयोग के लिए एक एकल `ObjectMapper` इंस्टेंस बनाएँ।
3. Java ऑब्जेक्ट्स को JSON में बदलने के लिए `writeValueAsString` और JSON को Java ऑब्जेक्ट्स में बदलने के लिए `readValue` का उपयोग करें।
4. `@JsonProperty`, `@JsonIgnore`, और `@JsonFormat` जैसे एनोटेशन्स के साथ व्यवहार को कस्टमाइज़ करें।
5. एक्सेप्शन्स (जैसे, `JsonProcessingException`) को हैंडल करें और विशिष्ट आवश्यकताओं (जैसे, अज्ञात गुणों को अनदेखा करना) के लिए `ObjectMapper` को कॉन्फ़िगर करें।
6. उन्नत फीचर्स जैसे सुंदर-प्रिंटिंग, फ़ाइल I/O, या डायनामिक JSON हैंडलिंग के लिए `JsonNode` का अन्वेषण करें।

इन चरणों के साथ, आप Jackson लाइब्रेरी का उपयोग करके अपने Java एप्लिकेशन में प्रभावी ढंग से JSON प्रोसेस कर सकते हैं।