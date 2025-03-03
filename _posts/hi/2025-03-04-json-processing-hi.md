---
audio: false
generated: true
lang: hi
layout: post
title: JSON प्रोसेसिंग इन जावा
translated: true
---

`com.fasterxml.jackson` पैकेज का उपयोग करने के लिए एक Java प्रोजेक्ट में JSON प्रोसेसिंग के लिए, आप Jackson लाइब्रेरी का उपयोग कर सकते हैं, जो Java ऑब्जेक्ट्स को JSON में और इसके विपरीत बदलने के लिए व्यापक रूप से उपयोग किया जाता है। नीचे एक चरण-दर-चरण गाइड दिया गया है, जो आपको शुरू करने में मदद करेगा, मानते हुए कि आप एक Maven आधारित प्रोजेक्ट पर काम कर रहे हैं। यह गाइड `jackson-databind` मॉड्यूल पर केंद्रित है, जो JSON डेटाबाइंडिंग के लिए उच्च स्तरीय कार्यक्षमता प्रदान करता है।

---

### 1. प्रोजेक्ट में Jackson डिपेंडेंसी जोड़ें
`com.fasterxml.jackson` पैकेज का उपयोग करने के लिए, आपको प्रोजेक्ट में Jackson लाइब्रेरी शामिल करनी होगी। अगर आप Maven का उपयोग कर रहे हैं, तो नीचे दिए गए डिपेंडेंसी को अपने `pom.xml` फ़ाइल में जोड़ें:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- नए संस्करण से बदलें -->
</dependency>
```

- **नोट**: [Maven Central Repository](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) पर नए संस्करण की जांच करें, क्योंकि यह 2.12.5 से नया हो सकता है।
- `jackson-databind` मॉड्यूल `jackson-core` और `jackson-annotations` पर निर्भर करता है, इसलिए आपको उनको अलग से जोड़ने की आवश्यकता नहीं है, जब तक कि आपके पास विशेष आवश्यकताएं नहीं हैं।

डिपेंडेंसी जोड़ने के बाद, `mvn install` चलाएं या अपने आईडीई में प्रोजेक्ट को रिफ्रेश करें ताकि लाइब्रेरी डाउनलोड हो सके।

---

### 2. एक `ObjectMapper` इंस्टेंस बनाएं
`com.fasterxml.jackson.databind` पैकेज से `ObjectMapper` क्लास JSON ऑपरेशंस के लिए प्राथमिक औजार है। यह थ्रेड-सेफ और संसाधन-गहन है, इसलिए इसे एकल, पुन: उपयोग करने योग्य इंस्टेंस बनाना सबसे अच्छा है:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

इसे उस क्लास में रखें जहाँ आप JSON ऑपरेशंस करेंगे।

---

### 3. एक Java ऑब्जेक्ट को JSON में बदलें (Serialization)
एक Java ऑब्जेक्ट को JSON स्ट्रिंग में बदलने के लिए, `writeValueAsString` विधि का उपयोग करें। यहाँ एक उदाहरण है:

#### एक Java क्लास परिभाषित करें
एक क्लास बनाएं जिसमें आप सीरियलाइज़ करना चाहते हैं, और सुनिश्चित करें कि इसमें गेटर्स और सेटर्स हों, क्योंकि Jackson इनका उपयोग प्राइवेट फ़ील्ड्स तक पहुंचने के लिए करता है:

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
`ObjectMapper` का उपयोग करके ऑब्जेक्ट को JSON में बदलें:

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

### 4. JSON को एक Java ऑब्जेक्ट में बदलें (Deserialization)
एक JSON स्ट्रिंग को वापस एक Java ऑब्जेक्ट में बदलने के लिए, `readValue` विधि का उपयोग करें:

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

- **एरर हैंडलिंग**: अगर JSON गलत है या क्लास संरचना से मेल नहीं खाता है, तो `readValue` विधि `JsonProcessingException` (एक चेक्ड एक्सेप्शन) फेंकती है। इसे एक ट्राई-कैच ब्लॉक के साथ या विधि सिग्नेचर में घोषित करें:

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. एनोटेशन के साथ JSON प्रोसेसिंग को अनुकूलित करें
Jackson एनोटेशन प्रदान करता है ताकि आप फ़ील्डों को सीरियलाइज़ या डिसीरियलाइज़ करने का तरीका अनुकूलित कर सकें। इन एनोटेशन को `com.fasterxml.jackson.annotation` से अपने क्लास में जोड़ें:

#### एक फ़ील्ड का नाम बदलें
`@JsonProperty` का उपयोग करके एक Java फ़ील्ड को अलग JSON फ़ील्ड नाम से मैप करें:

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // कंस्ट्रक्टर, गेटर्स, सेटर्स
}
```

**आउटपुट**:
```json
{"name":"value1","field2":123}
```

#### एक फ़ील्ड को नजरअंदाज करें
`@JsonIgnore` का उपयोग करके एक फ़ील्ड को सीरियलाइज़ से बाहर रखें:

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // कंस्ट्रक्टर, गेटर्स, सेटर्स
}
```

**आउटपुट**:
```json
{"field1":"value1"}
```

#### तारीखों को फ़ॉर्मेट करें
`@JsonFormat` का उपयोग करके तारीखों को सीरियलाइज़ करने का तरीका निर्दिष्ट करें:

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // कंस्ट्रक्टर, गेटर्स, सेटर्स
}
```

**आउटपुट** (उदाहरण):
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. उन्नत सीनारियो का सामना करें
यहाँ कुछ अतिरिक्त विशेषताएं हैं जो आप उपयोगी पा सकते हैं:

#### JSON को सुंदर प्रिंट करें
पढ़ने योग्य JSON आउटपुट के लिए, `writerWithDefaultPrettyPrinter` का उपयोग करें:

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

#### अज्ञात गुणों को नजरअंदाज करें
अगर JSON में आपके Java क्लास में मौजूद नहीं होने वाले गुण हों, तो `ObjectMapper` को उन्हें नजरअंदाज करने के लिए कॉन्फ़िगर करें:

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### फ़ाइलों के साथ काम करें
एक फ़ाइल से पढ़ें या लिखें:

```java
// फ़ाइल में लिखें
mapper.writeValue(new File("output.json"), obj);

// फ़ाइल से पढ़ें
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### सूची या जनरिक्स के साथ काम करें
संग्रहों के लिए, `TypeReference` का उपयोग करके जनरिक टाइप जानकारी को संरक्षित करें:

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. `JsonNode` के साथ डायनामिक JSON हैंडलिंग
अगर आप JSON को किसी विशेष क्लास में मैप नहीं करना चाहते, तो एक ट्री आधारित तरीके के लिए `JsonNode` का उपयोग करें:

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // "value1" लौटाता है
```

आप JSON को डायनामिक रूप से भी बना सकते हैं:

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
1. `jackson-databind` डिपेंडेंसी को अपने `pom.xml` में जोड़ें।
2. पुन: उपयोग करने योग्य एकल `ObjectMapper` इंस्टेंस बनाएं।
3. `writeValueAsString` का उपयोग करके Java ऑब्जेक्ट्स को JSON में बदलें और `readValue` का उपयोग करके JSON को Java ऑब्जेक्ट्स में बदलें।
4. `@JsonProperty`, `@JsonIgnore`, और `@JsonFormat` जैसे एनोटेशन का उपयोग करके व्यवहार को अनुकूलित करें।
5. एक्सेप्शन (जैसे `JsonProcessingException`) का सामना करें और `ObjectMapper` को विशेष आवश्यकताओं के लिए कॉन्फ़िगर करें (जैसे अज्ञात गुणों को नजरअंदाज करना)।
6. उन्नत विशेषताओं जैसे सुंदर प्रिंटिंग, फ़ाइल आई/ओ, या `JsonNode` के लिए डायनामिक JSON हैंडलिंग का पता लगाएं।

इन चरणों के साथ, आप Jackson लाइब्रेरी का उपयोग करके अपने Java एप्लिकेशन में JSON को प्रभावी रूप से प्रोसेस कर सकते हैं।