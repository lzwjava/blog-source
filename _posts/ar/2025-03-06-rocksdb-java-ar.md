---
audio: false
generated: true
lang: ar
layout: post
title: واجهة برمجة تطبيقات جافا لروكس دي بي
translated: true
type: note
---

لاستخدام مكتبة `org.rocksdb`، وهي واجهة برمجة تطبيقات جافا لـ RocksDB—قاعدة بيانات مضمنة عالية الأداء للبيانات من نوع مفتاح-قيمة—ستحتاج إلى اتباع هذه الخطوات. تم تحسين RocksDB للتخزين السريع واسترجاع البيانات، مما يجعلها مثالية للتطبيقات التي تتطلب وصولاً سريعًا للبيانات باستخدام مفاتيح معروفة. فيما يلي دليل شامل لمساعدتك على البدء:

---

### 1. **إضافة الاعتمادية**
لاستخدام `org.rocksdb` في مشروع جافا الخاص بك، تحتاج إلى تضمين اعتمادية RocksDB JNI. إذا كنت تستخدم Maven، أضف هذا إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

أما إذا كنت تستخدم Gradle، فاضف هذا إلى ملف `build.gradle` الخاص بك:

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**ملاحظة**: تحقق من [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) للحصول على أحدث إصدار، حيث أن `7.10.2` قد لا يكون الإصدار الحالي.

---

### 2. **تحميل المكتبة الأصلية**
تعتمد RocksDB على كود C++ أصلي، لذا يجب عليك تحميل المكتبة الأصلية قبل استخدامها. أضف هذا السطر في بداية الكود الخاص بك:

```java
RocksDB.loadLibrary();
```

سيؤدي الفشل في القيام بذلك إلى حدوث أخطاء أثناء وقت التشغيل.

---

### 3. **فتح قاعدة بيانات**
للبدء في استخدام RocksDB، تحتاج إلى فتح مثيل قاعدة بيانات عن طريق تحديد مسار ملف حيث سيتم تخزين قاعدة البيانات. استخدم فئة `Options` لضبط الإعدادات، مثل إنشاء قاعدة البيانات إذا لم تكن موجودة:

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/path/to/db");
```

- **`options`**: يضبط سلوك قاعدة البيانات (مثال: `setCreateIfMissing(true)` يضمن إنشاء قاعدة البيانات إذا لم تكن موجودة).
- **`/path/to/db`**: استبدل هذا بمسار دليل صالح على نظامك حيث ستوجد ملفات قاعدة البيانات.

---

### 4. **إجراء العمليات الأساسية**
RocksDB هي مخزن من نوع مفتاح-قيمة، وعملياتها الأساسية هي `put`، و`get`، و`delete`. يتم تخزين المفاتيح والقيم كمصفوفات بايت، لذا ستحتاج إلى تحويل البيانات (مثل السلاسل النصية) إلى بايت.

- **Put**: أدخل أو حدّث زوج مفتاح-قيمة.
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**: استرجع القيمة المرتبطة بمفتاح.
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // يطبع "value"
  } else {
      System.out.println("Key not found");
  }
  ```

- **Delete**: احذف زوج مفتاح-قيمة.
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **إغلاق قاعدة البيانات**
إغلاق قاعدة البيانات بشكل صحيح أمر ضروري لتحرير الموارد. أسهل طريقة هي استخدام كتلة try-with-resources، والتي تغلق قاعدة البيانات تلقائيًا عند الانتهاء:

```java
try (RocksDB db = RocksDB.open(options, "/path/to/db")) {
    // قم بإجراء العمليات هنا
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **معالجة الاستثناءات**
يمكن أن تطرح عمليات RocksDB استثناء `RocksDBException`، لذا قم دائمًا بتضمين معالجة الاستثناءات لمنع تسرب الموارد أو تلف البيانات:

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **خيارات التهيئة**
يمكنك ضبط أداء RocksDB بدقة باستخدام فئة `Options`. على سبيل المثال:

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // ذاكرة مؤقتة للكتابة بسعة 64 ميجابايت
```

تشمل الخيارات الشائعة:
- `setWriteBufferSize`: يتحكم في الذاكرة المستخدمة للكتابة.
- `setMaxOpenFiles`: يحد من عدد الملفات المفتوحة.
- `setCompactionStyle`: يضبط كيفية ضغط البيانات على القرص.

استكشف [توثيق RocksDB](https://github.com/facebook/rocksdb/wiki) للمزيد من الخيارات.

---

### 8. **مثال بسيط**
إليك مثالاً كاملاً يوضح فتح قاعدة بيانات، وتخزين زوج مفتاح-قيمة، واسترجاعه:

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // تحميل المكتبة الأصلية
        Options options = new Options().setCreateIfMissing(true);
        
        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // وضع زوج مفتاح-قيمة
            db.put("hello".getBytes(), "world".getBytes());
            
            // الحصول على القيمة
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // يطبع "world"
            } else {
                System.out.println("Key not found");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**الناتج**: `world`

---

### اعتبارات رئيسية
- **الطبيعة المضمنة**: تعمل RocksDB داخل عملية التطبيق الخاص بك، وليس كخادم منفصل.
- **مصفوفات البايت**: المفاتيح والقيم هي `byte[]`، لذا ستحتاج إلى التعامل مع التسلسل/إلغاء التسلسل للكائنات المعقدة.
- **الأداء**: تتفوق RocksDB مع التخزين السريع (مثل أقراص SSD) وتستخدم في الأنظمة عالية الأداء مثل تلك المستخدمة في Facebook، حيث تم تطويرها.
- **ليست علائقية**: إنها مخزن مفتاح-قيمة، وليست قاعدة بيانات علائقية—لا تدعم SQL أو عمليات الربط.

---

### الأخطاء الشائعة
- **نسيان `RocksDB.loadLibrary()`**: يؤدي إلى `UnsatisfiedLinkError`.
- **إدارة الموارد غير الصحيحة**: عدم إغلاق قاعدة البيانات يمكن أن يسبب مشاكل، خاصة على الأنظمة محدودة الموارد.
- **أخطاء نوع البيانات**: تمرير سلاسل نصية أو كائنات مباشرة بدلاً من تحويلها إلى `byte[]`.

---

### التوسع أكثر
- **الميزات المتقدمة**: استكشف المعاملات، اللقطات، أو عائلات الأعمدة لحالات الاستخدام الأكثر تعقيدًا.
- **المصادر**: تحقق من [RocksDB Java API](https://github.com/facebook/rocksdb/tree/main/java) و [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki) للحصول على توثيق وأمثلة مفصلة.

يوفر هذا الدليل أساسًا متينًا لاستخدام `org.rocksdb`. إذا كنت بحاجة إلى مساعدة بخصوص ميزات أو حالات استخدام محددة، فلا تتردد في السؤال