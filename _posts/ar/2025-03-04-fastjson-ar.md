---
audio: false
generated: true
lang: ar
layout: post
title: استخدام FastJson
translated: true
type: note
---

FastJSON هي مكتبة عالية الأداء لمعالجة JSON في لغة Java، تم تطويرها بواسطة Alibaba. تُستخدم على نطاق واسع لتحليل سلاسل JSON إلى كائنات Java، وتجميع كائنات Java إلى JSON، والتعامل مع بيانات JSON بكفاءة. فيما يلي دليل حول كيفية استخدام FastJSON بناءً على ميزاتها الأساسية.

### الخطوة 1: إضافة FastJSON إلى مشروعك
لاستخدام FastJSON، تحتاج إلى تضمينها في مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>2.0.51</version> <!-- استخدم أحدث إصدار متاح -->
</dependency>
```

أما إذا كنت تستخدم Gradle، فأضف هذا إلى ملف `build.gradle` الخاص بك:

```gradle
implementation 'com.alibaba:fastjson:2.0.51'
```

تحقق من [Maven Central Repository](https://mvnrepository.com/artifact/com.alibaba/fastjson) للحصول على أحدث إصدار.

### الخطوة 2: الاستخدام الأساسي
إليك كيفية استخدام FastJSON للمهام الشائعة مثل التجميع وإلغاء التجميع.

#### 1. **تجميع كائنات Java إلى JSON**
يمكنك تحويل كائن Java إلى سلسلة JSON باستخدام `JSON.toJSONString()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        // إنشاء كائن نموذجي
        User user = new User("Alice", 25);
        
        // التجميع إلى سلسلة JSON
        String jsonString = JSON.toJSONString(user);
        System.out.println(jsonString);
    }
}

// نموذج لفئة User
class User {
    private String name;
    private int age;

    public User(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // وسائل الجلب والتعيين (مطلوبة لكي تعمل FastJSON بشكل صحيح)
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
}
```

**الناتج:**
```json
{"age":25,"name":"Alice"}
```

#### 2. **إلغاء تجميع JSON إلى كائنات Java**
يمكنك تحليل سلسلة JSON مرة أخرى إلى كائن Java باستخدام `JSON.parseObject()`.

```java
import com.alibaba.fastjson.JSON;

public class Main {
    public static void main(String[] args) {
        String jsonString = "{\"age\":25,\"name\":\"Alice\"}";
        
        // إلغاء التجميع إلى كائن User
        User user = JSON.parseObject(jsonString, User.class);
        System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
    }
}
```

**الناتج:**
```
Name: Alice, Age: 25
```

#### 3. **تحليل JSON إلى قائمة**
إذا كان JSON يمثل قائمة من الكائنات، فاستخدم `JSON.parseArray()`.

```java
import com.alibaba.fastjson.JSON;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String jsonArray = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]";
        
        // إلغاء التجميع إلى List<User>
        List<User> users = JSON.parseArray(jsonArray, User.class);
        for (User user : users) {
            System.out.println("Name: " + user.getName() + ", Age: " + user.getAge());
        }
    }
}
```

**الناتج:**
```
Name: Alice, Age: 25
Name: Bob, Age: 30
```

### الخطوة 3: الميزات المتقدمة
تقدم FastJSON خيارات تخصيص إضافية:

#### 1. **تخصيص التجميع**
يمكنك التحكم في كيفية تجميع الحقول باستخدام خيارات `SerializerFeature`.

```java
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.serializer.SerializerFeature;

public class Main {
    public static void main(String[] args) {
        User user = new User("Alice", 25);
        
        // استخدام PrettyFormat للحصول على ناتج مقروء
        String jsonString = JSON.toJSONString(user, SerializerFeature.PrettyFormat);
        System.out.println(jsonString);
    }
}
```

**الناتج:**
```json
{
	"age":25,
	"name":"Alice"
}
```

من خيارات `SerializerFeature` الشائعة:
- `WriteNullListAsEmpty`: يتم كتابة القوائم الفارغة كـ `[]` بدلاً من `null`.
- `WriteMapNullValue`: تضمين الحقول ذات القيم `null` في الناتج.

#### 2. **معالجة الكائنات المعقدة**
بالنسبة للكائنات المتداخلة، تأكد من أن الفئات الداخلية تحتوي على وسائل جلب وتعيين مناسبة.

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

**الناتج:**
```json
{"address":{"city":"NY","street":"123 Main St"},"age":25,"name":"Alice"}
NY
```

### الخطوة 4: ملاحظات وأفضل الممارسات
- **الأمان**: واجهت FastJSON ثغرات أمنية في الإصدارات القديمة (مثل تنفيذ التعليمات البرمجية عن بُعد). استخدم دائمًا أحدث إصدار وتجنب تمكين `Feature.SupportAutoType` إلا إذا كان ضروريًا.
- **الأداء**: FastJSON مُحسَّنة للسرعة، لكن اختبرها مع حالة الاستخدام المحددة لديك لمجموعات البيانات الكبيرة.
- **التوثيق**: راجع [صفحة FastJSON الرسمية على GitHub](https://github.com/alibaba/fastjson) لمزيد من التفاصيل.

أعلمني إذا كنت بحاجة إلى مساعدة في حالة استخدام محددة أو استكشاف الأخطاء وإصلاحها!