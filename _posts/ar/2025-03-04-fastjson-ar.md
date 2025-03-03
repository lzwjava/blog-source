---
audio: false
generated: true
lang: ar
layout: post
title: استخدام FastJson
translated: true
---

FastJSON هي مكتبة معالجة JSON عالية الأداء لجاڤا، تم تطويرها بواسطة Alibaba. يتم استخدامها على نطاق واسع لتحليل strings JSON إلى objects جاڤا، وSerialization objects جاڤا إلى JSON، وHandling البيانات JSON بشكل فعال. أدناه دليل على كيفية استخدام FastJSON بناءً على ميزاتها الأساسية.

### الخطوة 1: إضافة FastJSON إلى مشروعك
لتستخدم FastJSON، عليك تضمينه في مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml`:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- استخدم أحدث الإصدار المتاح -->
</dependency>
```

للمباني، أضف هذا إلى ملف `build.gradle`:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

تحقق من [مستودع Maven Central](https://mvnrepository.com/artifact/com.alibaba/fastjson) للحصول على أحدث الإصدار.

### الخطوة 2: الاستخدام الأساسي
هنا كيفية استخدام FastJSON لمهام شائعة مثل Serialization وDeserialization.

#### 1. **Serialization objects جاڤا إلى JSON**
يمكنك تحويل object جاڤا إلى string JSON باستخدام `JSON.toJSONString()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // إنشاء object نموذج
        User user = new User("Alice", 25);

        // Serialization إلى string JSON
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// class User النموذج
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getters وSetters (مطلوب للعمل بشكل صحيح مع FastJSON)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**الخروج:**
```json
{"age":25,"name":"Alice"}
```

#### 2. **Deserialization JSON إلى objects جاڤا**
يمكنك تحليل string JSON إلى object جاڤا باستخدام `JSON.parseObject()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";

        // Deserialization إلى object User
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**الخروج:**
```
Name: Alice, Age: 25
```

#### 3. **تحليل JSON إلى قائمة**
إذا كان JSON يمثل قائمة من objects، استخدم `JSON.parseArray()`.

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";

        // Deserialization إلى List<User>
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**الخروج:**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### الخطوة 3: الميزات المتقدمة
يقدم FastJSON خيارات تخصيص إضافية:

#### 1. **تخصيص Serialization**
يمكنك التحكم في كيفية Serialization الحقول باستخدام خيارات `SerializerFeature`.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);

        // استخدام PrettyFormat للحصول على خروجية قابلة للقراءة
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**الخروج:**
```json
{
	"age":25,
	"name":"Alice"
}
```

خيارات `SerializerFeature` الشائعة:
- `WriteNullListAsEmpty`: يتم كتابة القوائم الفارغة ك `[]` بدلاً من `null`.
- `WriteMapNullValue`: تضمين الحقول التي لها قيم `null` في الخرج.

#### 2. **Handling objects معقدة**
لobjects المضمنة، تأكد من أن classes الداخلية لديها getters/setters مناسبة.

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

**الخروج:**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### الخطوة 4: ملاحظات و أفضل الممارسات
- **الأمان**: كان FastJSON لديه تعرّضات في الإصدارات القديمة (مثل تنفيذ الكود عن بُعد). استخدم دائمًا أحدث الإصدار وتجنب تمكين `Feature.SupportAutoType` إلا إذا كان ذلك ضروريًا.
- **الأداء**: تم تحسين FastJSON للسرعةت، ولكن اختبره مع حالة الاستخدام الخاصة بك للبيانات الكبيرة.
- **التوثيق**: استعرض الصفحة الرسمية [FastJSON GitHub](https://github.com/alibaba/fastjson) للحصول على مزيد من التفاصيل.

أعلمني إذا كنت تحتاج إلى مساعدة في حالة استخدام معينة أو حل مشاكل!