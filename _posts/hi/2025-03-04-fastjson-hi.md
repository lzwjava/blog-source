---
audio: false
generated: true
lang: hi
layout: post
title: FastJson का उपयोग
translated: true
---

FastJSON एक उच्च-प्रदर्शन JSON प्रोसेसिंग लाइब्रेरी है जो Java के लिए Alibaba द्वारा विकसित की गई है। यह JSON स्ट्रिंग्स को Java ऑब्जेक्ट्स में पार्स करने, Java ऑब्जेक्ट्स को JSON में सीरियलाइज़ करने और JSON डेटा को दक्षता से हैंडल करने के लिए व्यापक रूप से उपयोग की जाती है। नीचे FastJSON के कोर फीचर्स के आधार पर इसका उपयोग करने के लिए एक गाइड है।

### चरण 1: FastJSON को आपकी प्रोजेक्ट में जोड़ें
FastJSON का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट में शामिल करना होगा। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- उपलब्ध नएतम संस्करण का उपयोग करें -->
</dependency>
```

Gradle के लिए, अपने `build.gradle` में यह जोड़ें:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

नएतम संस्करण के लिए [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) की जांच करें।

### चरण 2: बेसिक उपयोग
यहाँ FastJSON का उपयोग करने के लिए सामान्य कार्यों जैसे सीरियलाइज़ेशन और डिसीरियलाइज़ेशन के लिए है।

#### 1. **Java ऑब्जेक्ट्स को JSON में सीरियलाइज़ करने**
आप `JSON.toJSONString()` का उपयोग करके एक Java ऑब्जेक्ट को JSON स्ट्रिंग में बदल सकते हैं।

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // एक सैम्पल ऑब्जेक्ट बनाएं
        User user = new User("Alice", 25);

        // JSON स्ट्रिंग में सीरियलाइज़ करें
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// सैम्पल User क्लास
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters और setters (FastJSON के लिए सही तरह से काम करने के लिए आवश्यक)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**आउटपुट:**
```json
{"age":25,"name":"Alice"}
```

#### 2. **JSON को Java ऑब्जेक्ट्स में डिसीरियलाइज़ करने**
आप `JSON.parseObject()` का उपयोग करके एक JSON स्ट्रिंग को वापस एक Java ऑब्जेक्ट में पार्स कर सकते हैं।

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";

        // User ऑब्जेक्ट में डिसीरियलाइज़ करें
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**आउटपुट:**
```
Name: Alice, Age: 25
```

#### 3. **JSON को एक सूची में पार्स करने**
अगर आपका JSON एक ऑब्जेक्ट्स की सूची को दर्शाता है, तो `JSON.parseArray()` का उपयोग करें।

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";

        // List<User> में डिसीरियलाइज़ करें
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**आउटपुट:**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### चरण 3: उन्नत फीचर्स
FastJSON अतिरिक्त कस्टमाइज़ेशन विकल्प प्रदान करता है:

#### 1. **सीरियलाइज़ेशन को कस्टमाइज़ करने**
आप `SerializerFeature` विकल्पों का उपयोग करके फील्डों को सीरियलाइज़ करने का नियंत्रण कर सकते हैं।

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);

        // पढ़ने के लिए पढ़ने के लिए PrettyFormat का उपयोग करें
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**आउटपुट:**
```json
{
	"age":25,
	"name":"Alice"
}
```

सामान्य `SerializerFeature` विकल्प:
- `WriteNullListAsEmpty`: खाली सूचियाँ `[]` के रूप में लिखी जाती हैं, `null` के बजाय।
- `WriteMapNullValue`: आउटपुट में `null` मान वाले फील्ड शामिल करें।

#### 2. **जटिल ऑब्जेक्ट्स को हैंडल करने**
नेटेड ऑब्जेक्टों के लिए, सुनिश्चित करें कि इनर क्लासेस में सही तरह से getters/setters हैं।

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        Address address = new Address("123 Main St", "NY");
        User user = new User("Alice", 25, address);

        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);

        User parsedUser = JSON.parseObject(jsonString, User.class);
        System.out.println(parsedUser.getAddress().getCity());
    }
}

class User {
    private String name;
    private int age;
    private Address address;

    public User(String name, int age, Address address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public Address getAddress() { return address; }
    public void setAddress(Address address) { this.address = address; }
}

class Address {
    private String street;
    private String city;

    public Address(String street, String city) {
        this.street = street;
        this.city = city;
    }

    public String getStreet() { return street; }
    public void setStreet(String street) { this.street = street; }
    public String getCity() { return city; }
    public void setCity(String city) { this.city = city; }
}
```

**आउटपुट:**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### चरण 4: नोट्स और बेस्ट प्रैक्टिस
- **सुरक्षा**: FastJSON में पुराने संस्करणों में कमजोरियां थीं (जैसे, रिमोट कोड एक्सिक्यूशन)। हमेशा नएतम संस्करण का उपयोग करें और `Feature.SupportAutoType` को सक्षम करने से बचें जब तक कि आवश्यक नहीं हो।
- **प्रदर्शन**: FastJSON को गति के लिए ऑप्टिमाइज़ किया गया है, लेकिन इसे अपने विशिष्ट उपयोग केस के लिए बड़े डेटासेट के साथ टेस्ट करें।
- **डॉक्यूमेंटेशन**: अधिक विवरण के लिए [FastJSON GitHub पेज](https://github.com/alibaba/fastjson) पर जाकर देखें।

किसी विशिष्ट उपयोग केस या ट्रबलशूटिंग के लिए मदद चाहिए तो मुझे बता दें!