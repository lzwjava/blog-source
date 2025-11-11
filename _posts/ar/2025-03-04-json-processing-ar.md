---
audio: false
generated: true
lang: ar
layout: post
title: معالجة JSON في جافا
translated: true
type: note
---

لاستخدام حزمة `com.fasterxml.jackson` في مشروع جافا لمعالجة JSON، يمكنك الاستفادة من مكتبة Jackson، التي تُستخدم على نطاق واسع لتحويل كائنات جافا إلى JSON والعكس. فيما يلي دليل خطوة بخطوة لمساعدتك على البدء، بافتراض أنك تعمل في مشروع يستخدم Maven. يركز هذا الدليل على وحدة `jackson-databind`، التي توفر وظائف عالية المستوى لربط البيانات JSON.

---

### 1. أضف تبعية Jackson إلى مشروعك
لاستخدام حزمة `com.fasterxml.jackson`، تحتاج إلى تضمين مكتبة Jackson في مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.12.5</version> <!-- استبدل بأحدث إصدار -->
</dependency>
```

- **ملاحظة**: تحقق من [مستودع Maven المركزي](https://mvnrepository.com/artifact/com.fasterxml.jackson.core/jackson-databind) للحصول على أحدث إصدار، لأنه قد يكون أحدث من 2.12.5.
- تعتمد وحدة `jackson-databind` على `jackson-core` و `jackson-annotations`، لذلك لا تحتاج إلى إضافتهما بشكل منفصل إلا إذا كانت لديك متطلبات محددة.

بعد إضافة التبعية، شغّل `mvn install` أو حدّث مشروعك في بيئة التطوير المتكاملة (IDE) لتنزيل المكتبة.

---

### 2. أنشئ نسخة من `ObjectMapper`
فئة `ObjectMapper` من الحزمة `com.fasterxml.jackson.databind` هي الأداة الأساسية لعمليات JSON. إنها آمنة للاستخدام في بيئات الخيوط المتعددة (thread-safe) ومكلفة من حيث الموارد عند إنشاء نسخة منها، لذا من الأفضل إنشاء نسخة واحدة قابلة لإعادة الاستخدام:

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonExample {
    private static final ObjectMapper mapper = new ObjectMapper();
}
```

ضع هذا الكود في فئة حيث ستقوم بإجراء عمليات JSON.

---

### 3. حوّل كائن جافا إلى JSON (التسلسل)
لتحويل كائن جافا إلى سلسلة نصية JSON، استخدم الدالة `writeValueAsString`. إليك مثالاً:

#### عرّف فئة جافا
أنشئ فئة تحتوي على الحقول التي تريد تسلسلها. تأكد من أن لديها دوال `getters` و `setters`، لأن Jackson يستخدمها افتراضيًا للوصول إلى الحقول الخاصة:

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

#### قم بالتسلسل إلى JSON
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

**الناتج**:
```json
{"field1":"value1","field2":123}
```

---

### 4. حوّل JSON إلى كائن جافا (إلغاء التسلسل)
لتحويل سلسلة نصية JSON مرة أخرى إلى كائن جافا، استخدم الدالة `readValue`:

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

- **معالجة الأخطاء**: تطرح الدالة `readValue` استثناء `JsonProcessingException` (استثناء مُتحقَّق منه - checked exception) إذا كان تنسيق JSON معطوبًا أو لا يتطابق مع هيكل الفئة. عالجه باستخدام كتلة try-catch أو اعلنه في توقيع الدالة:

```java
try {
    MyClass obj = mapper.readValue(json, MyClass.class);
} catch (JsonProcessingException e) {
    e.printStackTrace();
}
```

---

### 5. خصّص معالجة JSON باستخدام التعليقات التوضيحية (Annotations)
توفر Jackson تعليقات توضيحية لتخصيص كيفية تسلسل الحقول أو إلغاء تسلسلها. أضف هذه التعليقات التوضيحية من الحزمة `com.fasterxml.jackson.annotation` إلى فئتك:

#### أعيد تسمية حقل
استخدم `@JsonProperty` لتعيين حقل جافا إلى اسم حقل JSON مختلف:

```java
import com.fasterxml.jackson.annotation.JsonProperty;

public class MyClass {
    @JsonProperty("name")
    private String field1;
    private int field2;
    // المُنشئ، دوال getters، دوال setters
}
```

**الناتج**:
```json
{"name":"value1","field2":123}
```

#### تجاهل حقل
استخدم `@JsonIgnore` لاستبعاد حقل من عملية التسلسل:

```java
import com.fasterxml.jackson.annotation.JsonIgnore;

public class MyClass {
    private String field1;
    @JsonIgnore
    private int field2;
    // المُنشئ، دوال getters، دوال setters
}
```

**الناتج**:
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
    // المُنشئ، دوال getters، دوال setters
}
```

**الناتج** (مثال):
```json
{"field1":"value1","date":"2023-10-25"}
```

---

### 6. تعامل مع السيناريوهات المتقدمة
فيما يلي بعض الميزات الإضافية التي قد تجدها مفيدة:

#### طباعة JSON بشكل منسق (Pretty-Print)
للحصول على ناتج JSON مقروء، استخدم `writerWithDefaultPrettyPrinter`:

```java
String prettyJson = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
```

**الناتج**:
```json
{
  "field1" : "value1",
  "field2" : 123
}
```

#### تجاهل الخصائص غير المعروفة
إذا كان JSON يحتوي على حقول غير موجودة في فئة جافا الخاصة بك، اضبط `ObjectMapper` لتجاهلها:

```java
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
```

#### العمل مع الملفات
اقرأ من ملف أو اكتب إلى ملف:

```java
// اكتب إلى ملف
mapper.writeValue(new File("output.json"), obj);

// اقرأ من ملف
MyClass obj = mapper.readValue(new File("input.json"), MyClass.class);
```

#### تعامل مع القوائم (Lists) أو الأنواع العامة (Generics)
للمجموعات، استخدم `TypeReference` للحفاظ على معلومات النوع العام (generic type):

```java
import com.fasterxml.jackson.core.type.TypeReference;
import java.util.List;

List<MyClass> list = mapper.readValue(json, new TypeReference<List<MyClass>>() {});
```

---

### 7. معالجة JSON الديناميكية باستخدام `JsonNode`
إذا كنت لا تريد تعيين JSON إلى فئة محددة، استخدم `JsonNode` لنهج قائم على الشجرة (tree-based):

```java
import com.fasterxml.jackson.databind.JsonNode;

JsonNode node = mapper.readTree("{\"field1\":\"value1\",\"field2\":123}");
String value = node.get("field1").asText(); // تُرجع "value1"
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

### الملخص
لاستخدام حزمة `com.fasterxml.jackson`:
1. أضف تبعية `jackson-databind` إلى ملف `pom.xml` الخاص بك.
2. أنشئ نسخة واحدة من `ObjectMapper` لإعادة الاستخدام.
3. استخدم `writeValueAsString` لتحويل كائنات جافا إلى JSON واستخدم `readValue` لتحويل JSON إلى كائنات جافا.
4. خصّص السلوك باستخدام تعليقات توضيحية مثل `@JsonProperty` و `@JsonIgnore` و `@JsonFormat`.
5. عالج الاستثناءات (مثل `JsonProcessingException`) و اضبط `ObjectMapper` للاحتياجات المحددة (مثل تجاهل الخصائص غير المعروفة).
6. استكشف الميزات المتقدمة مثل الطباعة المنسقة ومدخلات/مخرجات الملفات أو `JsonNode` للمعالجة الديناميكية لـ JSON.

بهذه الخطوات، يمكنك معالجة JSON بشكل فعال في تطبيق جافا الخاص بك باستخدام مكتبة Jackson.