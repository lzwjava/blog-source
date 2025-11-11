---
audio: false
generated: true
lang: hi
layout: post
title: फास्टजेसन का उपयोग
translated: true
type: note
---

FastJSON अलीबाबा द्वारा विकसित Java के लिए एक उच्च-प्रदर्शन JSON प्रोसेसिंग लाइब्रेरी है। इसका उपयोग JSON स्ट्रिंग्स को Java ऑब्जेक्ट्स में पार्स करने, Java ऑब्जेक्ट्स को JSON में सीरियलाइज़ करने और JSON डेटा को कुशलतापूर्वक हैंडल करने के लिए व्यापक रूप से किया जाता है। नीचे इसकी मुख्य विशेषताओं के आधार पर FastJSON का उपयोग करने का मार्गदर्शक दिया गया है।

### चरण 1: अपने प्रोजेक्ट में FastJSON जोड़ें
FastJSON का उपयोग करने के लिए, आपको इसे अपने प्रोजेक्ट में शामिल करना होगा। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- उपलब्ध नवीनतम संस्करण का उपयोग करें -->
</dependency>
```

Gradle के लिए, अपनी `build.gradle` में यह जोड़ें:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

नवीनतम संस्करण के लिए [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) देखें।

### चरण 2: मूल उपयोग
यहाँ बताया गया है कि सीरियलाइज़ेशन और डी-सीरियलाइज़ेशन जैसे सामान्य कार्यों के लिए FastJSON का उपयोग कैसे करें।

#### 1. **Java ऑब्जेक्ट्स को JSON में सीरियलाइज़ करना**
आप `JSON.toJSONString()` का उपयोग करके एक Java ऑब्जेक्ट को JSON स्ट्रिंग में बदल सकते हैं।

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // एक नमूना ऑब्जेक्ट बनाएं
        User user = new User("Alice", 25);
        
        // JSON स्ट्रिंग में सीरियलाइज़ करें
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// नमूना User क्लास
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters और setters (FastJSON के ठीक से काम करने के लिए आवश्यक)
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

#### 2. **JSON को Java ऑब्जेक्ट्स में डी-सीरियलाइज़ करना**
आप `JSON.parseObject()` का उपयोग करके एक JSON स्ट्रिंग को वापस Java ऑब्जेक्ट में पार्स कर सकते हैं।

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";
        
        // User ऑब्जेक्ट में डी-सीरियलाइज़ करें
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**आउटपुट:**
```
Name: Alice, Age: 25
```

#### 3. **JSON को एक सूची में पार्स करना**
यदि आपकी JSON ऑब्जेक्ट्स की एक सूची का प्रतिनिधित्व करती है, तो `JSON.parseArray()` का उपयोग करें।

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";
        
        // List<User> में डी-सीरियलाइज़ करें
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

### चरण 3: उन्नत सुविधाएँ
FastJSON अतिरिक्त अनुकूलन विकल्प प्रदान करता है:

#### 1. **सीरियलाइज़ेशन को अनुकूलित करना**
आप `SerializerFeature` विकल्पों का उपयोग करके नियंत्रित कर सकते हैं कि फ़ील्ड्स कैसे सीरियलाइज़ होते हैं।

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);
        
        // पठनीय आउटपुट के लिए PrettyFormat का उपयोग करें
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
- `WriteNullListAsEmpty`: खाली सूचियाँ `null` के बजाय `[]` के रूप में लिखी जाती हैं।
- `WriteMapNullValue`: आउटपुट में `null` मान वाली फ़ील्ड्स शामिल करें।

#### 2. **जटिल ऑब्जेक्ट्स को हैंडल करना**
नेस्टेड ऑब्जेक्ट्स के लिए, सुनिश्चित करें कि आंतरिक क्लासेस में उचित गेटर्स/सेटर्स हों।

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

### चरण 4: नोट्स और सर्वोत्तम अभ्यास
- **सुरक्षा**: FastJSON के पुराने संस्करणों में कमजोरियाँ थीं (जैसे, रिमोट कोड एक्सिक्यूशन)। हमेशा नवीनतम संस्करण का उपयोग करें और जब तक आवश्यक न हो `Feature.SupportAutoType` को सक्षम करने से बचें।
- **प्रदर्शन**: FastJSON गति के लिए अनुकूलित है, लेकिन बड़े डेटासेट के लिए इसे अपने विशिष्ट उपयोग के मामले में परखें।
- **दस्तावेज़ीकरण**: अधिक जानकारी के लिए आधिकारिक [FastJSON GitHub पेज](https://github.com/alibaba/fastjson) देखें।

यदि आपको किसी विशिष्ट उपयोग के मामले या समस्या निवारण में सहायता की आवश्यकता है, तो मुझे बताएं!