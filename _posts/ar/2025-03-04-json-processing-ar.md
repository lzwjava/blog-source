---
audio: false
generated: true
lang: ar
layout: post
title: معالجة JSON في جاڤا
translated: true
---

لاستخدام حزمة `com.fasterxml.jackson` في مشروع Java لمعالجة JSON، يمكنك الاستفادة من مكتبة جاكسون، التي تُستخدم على نطاق واسع لتحويل الكائنات Java إلى JSON و العكس. أدناه دليل خطوة بخطوة للحصول على البدء، مع افتراض أنك تعمل مع مشروع قائم على Maven. يركز هذا الدليل على وحدة `jackson-databind`، التي توفر وظائف عالية المستوى لتربط البيانات JSON.

---

### 1. إضافة التبعية جاكسون إلى مشروعك
لاستخدام حزمة `com.fasterxml.jackson`، عليك إضافة مكتبة جاكسون إلى مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- استبدل بالنسخة الأخيرة -->
</dependency>
```

- **ملاحظة**: تحقق من [مستودع Maven المركزي](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) للحصول على أحدث نسخة، قد تكون أحدث من 2.12.5.
- تعتمد وحدة `jackson-databind` على `jackson-core` و `jackson-annotations`، فلا تحتاج إلى إضافةهما بشكل منفصل إلا إذا كان لديك متطلبات محددة.

بعد إضافة التبعية، قم بتشغيل `mvn install` أو تحديث مشروعك في بيئة التطوير المتكاملة (IDE) لتنزيل المكتبة.

---

### 2. إنشاء مثيل `ObjectMapper`
فئة `ObjectMapper` من حزمة `com.fasterxml.jackson.databind` هي الأداة الرئيسية لعمليات JSON. إنها آمنة للخطوط المتعددة وتستهلك الموارد بشكل كبير عند إنشاءها، لذا من الأفضل إنشاء مثيل واحد يمكن إعادة استخدامه:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

ضع هذا في فئة حيث ستقوم بعمليات JSON.

---

### 3. تحويل كائن Java إلى JSON (التسلسل)
لتحويل كائن Java إلى سلسلة JSON، استخدم طريقة `writeValueAsString`. إليك مثال:

#### تعريف فئة Java
إنشاء فئة مع الحقول التي تريد تسلسلها. تأكد من أن لديها طرق الوصول (getters) و الإعداد (setters)، لأن جاكسون يستخدمها بشكل افتراضي للوصول إلى الحقول الخاصة:

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

#### تسلسل إلى JSON
استخدم `ObjectMapper` لتحويل الكائن إلى JSON:

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

**الخرج**:
```json
{"field1":"value1","field2":123}
```

---

### 4. تحويل JSON إلى كائن Java (الترميز)
لتحويل سلسلة JSON إلى كائن Java، استخدم طريقة `readValue`:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static void main(String[] args) throws Exception {
        String json = "{\"field1\":\"value1\",\"field2\":123}";
        MyClass obj = mapper.readValue(json, MyClass.class);
        System.out.println(obj.getField1()); // يطبع "value1"
    }
}
```

- **معالجة الأخطاء**: طريقة `readValue` تثير استثناء `JsonProcessingException` (استثناء محقق) إذا كان JSON غير صحيح أو لا يتطابق مع بنية الفئة. قم بمعالجته باستخدام كتلة try-catch أو إعلانها في توقيع الطريقة:

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. تخصيص معالجة JSON باستخدام التعليقات
يوفر جاكسون تعليقات لتخصيص كيفية تسلسل الحقول أو ترميزها. أضف هذه التعليقات من `com.fasterxml.jackson.annotation` إلى فئةك:

#### تغيير اسم الحقل
استخدم `@JsonProperty` لتخزين حقل Java إلى اسم حقل JSON مختلف:

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // البناء، طرق الوصول، الإعداد
}
```

**الخرج**:
```json
{"name":"value1","field2":123}
```

#### تجاهل حقل
استخدم `@JsonIgnore` لتفادي حقل من التسلسل:

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // البناء، طرق الوصول، الإعداد
}
```

**الخرج**:
```json
{"field1":"value1"}
```

#### تنسيق التواريخ
استخدم `@JsonFormat` لتحديد كيفية تسلسل التواريخ:

```java
import com.fasterxml.jackson.annotation.JsonFormat;
import java.util.Date;

public class MyClass {
    private String field1;
    @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd")
    private Date date;
    // البناء، طرق الوصول، الإعداد
}
```

**الخرج** (مثال):
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. معالجة السيناريوهات المتقدمة
هنا بعض الميزات الإضافية التي قد تجدها مفيدة:

#### طباعة JSON جميلة
للخرج JSON قابل للقراءة، استخدم `writerWithDefaultPrettyPrinter`:

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**الخرج**:
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### تجاهل الخصائص المجهولة
إذا كان JSON يحتوي على حقول غير موجودة في فئة Java، قم بتكوين `ObjectMapper` لتجاهلها:

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### العمل مع الملفات
قراءة من أو كتابة إلى ملف:

```java
// كتابة إلى ملف
mapper.writeValue(new File("output.json"), obj);

// قراءة من ملف
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### التعامل مع القوائم أو الأنواع العامة
للمجموعات، استخدم `TypeReference` للحفاظ على معلومات النوع العام:

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. معالجة JSON الديناميكي باستخدام `JsonNode`
إذا لم ترغب في خريطة JSON إلى فئة محددة، استخدم `JsonNode` لمقاربة الشجرة:

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // يرجع "value1"
```

يمكنك أيضًا بناء JSON بشكل ديناميكي:

```java
import com.fasterxml.jackson.databind.node.ObjectNode;

ObjectNode node = mapper.createObjectNode();
node.put("field1", "value1");
node.put("field2", 123);
String json = mapper.writeValueAsString(node);
```

---

### ملخص
لاستخدام حزمة `com.fasterxml.jackson`:
1. أضف التبعية `jackson-databind` إلى ملف `pom.xml`.
2. إنشاء مثيل واحد من `ObjectMapper` لإعادة الاستخدام.
3. استخدم `writeValueAsString` لتحويل الكائنات Java إلى JSON و `readValue` لتحويل JSON إلى الكائنات Java.
4. تخصيص السلوك باستخدام التعليقات مثل `@JsonProperty` و `@JsonIgnore` و `@JsonFormat`.
5. معالجة الاستثناءات (مثل `JsonProcessingException`) وتكوين `ObjectMapper` حسب الحاجة (مثل تجاهل الخصائص المجهولة).
6. استكشاف الميزات المتقدمة مثل طباعة جميلة، إدخال/إخراج الملفات، أو `JsonNode` لمعالجة JSON الديناميكي.

بهذه الخطوات، يمكنك معالجة JSON في تطبيق Java الخاص بك باستخدام مكتبة جاكسون بشكل فعال.