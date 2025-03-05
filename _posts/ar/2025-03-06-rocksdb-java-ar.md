---
audio: false
generated: true
lang: ar
layout: post
title: API Java ل RocksDB
translated: true
---

لاستخدام مكتبة `org.rocksdb`، والتي هي واجهة برمجة تطبيقات Java لـ RocksDB — قاعدة بيانات محبسة ذات أداء عالي للبيانات المفتاحية — عليك اتباع الخطوات التالية. RocksDB مخصص لتخزين و استرجاع سريع، مما يجعله مثاليًا للتطبيقات التي تتطلب الوصول السريع إلى البيانات من خلال مفاتيح معروفة. أدناه دليل شامل للحصول على البدء:

---

### 1. **إضافة التبعية**
لاستخدام `org.rocksdb` في مشروع Java الخاص بك، عليك إضافة التبعية RocksDB JNI (Java Native Interface). إذا كنت تستخدم Maven، أضف هذا إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.rocksdb</groupId>
    <artifactId>rocksdbjni</artifactId>
    <version>7.10.2</version>
</dependency>
```

للمستخدمين Gradle، أضف هذا إلى ملف `build.gradle`:

```groovy
implementation 'org.rocksdb:rocksdbjni:7.10.2'
```

**ملاحظة**: تحقق من [Maven Central](https://search.maven.org/search?q=g:org.rocksdb%20AND%20a:rocksdbjni) للحصول على أحدث الإصدار، حيث قد لا يكون `7.10.2` هو الإصدار الحالي.

---

### 2. **تحميل المكتبة الأصلية**
RocksDB يعتمد على الكود الأصلي C++، لذا عليك تحميل المكتبة الأصلية قبل استخدامها. أضف هذه السطر في بداية كودك:

```java
RocksDB.loadLibrary();
```

فشل في القيام بذلك سيؤدي إلى أخطاء في وقت التشغيل.

---

### 3. **فتح قاعدة بيانات**
لبدء استخدام RocksDB، عليك فتح مثيل قاعدة بيانات عن طريق تحديد مسار ملف حيث سيتم تخزين قاعدة البيانات. استخدم فئة `Options` لتكوين الإعدادات مثل إنشاء قاعدة البيانات إذا لم تكن موجودة:

```java
import org.rocksdb.Options;
import org.rocksdb.RocksDB;

Options options = new Options().setCreateIfMissing(true);
RocksDB db = RocksDB.open(options, "/path/to/db");
```

- **`options`**: يحدد سلوك قاعدة البيانات (على سبيل المثال، `setCreateIfMissing(true)` يضمن إنشاء قاعدة البيانات إذا لم تكن موجودة).
- **`/path/to/db`**: استبدل هذا بمسار مجلد صالح على نظامك حيث سيتم تخزين ملفات قاعدة البيانات.

---

### 4. **إجراء عمليات أساسية**
RocksDB هي مخزن مفاتيح-قيم، وعملياتها الأساسية هي `put`، `get`، و `delete`. يتم تخزين المفاتيح والقيم كمصفوفات بايت، لذا عليك تحويل البيانات (على سبيل المثال، الأسلوب) إلى بايت.

- **Put**: إدخال أو تحديث زوج مفاتيح-قيم.
  ```java
  db.put("key".getBytes(), "value".getBytes());
  ```

- **Get**: استرجاع القيمة المرتبطة بمفتاح.
  ```java
  byte[] value = db.get("key".getBytes());
  if (value != null) {
      System.out.println(new String(value));  // يطباع "value"
  } else {
      System.out.println("لم يتم العثور على المفتاح");
  }
  ```

- **Delete**: إزالة زوج مفاتيح-قيم.
  ```java
  db.delete("key".getBytes());
  ```

---

### 5. **إغلاق قاعدة البيانات**
إغلاق قاعدة البيانات بشكل صحيح هو ضروري لتحرير الموارد. الطريقة الأيسر هي استخدام كتلة `try-with-resources` التي تغلق قاعدة البيانات تلقائيًا عندما تنتهي:

```java
try (RocksDB db = RocksDB.open(options, "/path/to/db")) {
    // إجراء العمليات هنا
} catch (Exception e) {
    e.printStackTrace();
}
```

---

### 6. **معالجة الاستثناءات**
عمليات RocksDB يمكن أن تطرح `RocksDBException`، لذا دائمًا تضمين معالجة الاستثناءات لمنع تسرب الموارد أو تدهور البيانات:

```java
try {
    db.put("key".getBytes(), "value".getBytes());
} catch (RocksDBException e) {
    e.printStackTrace();
}
```

---

### 7. **خيارات التكوين**
يمكنك ضبط أداء RocksDB باستخدام فئة `Options`. على سبيل المثال:

```java
Options options = new Options()
    .setCreateIfMissing(true)
    .setWriteBufferSize(64 * 1024 * 1024);  // 64MB write buffer
```

خيارات شائعة تشمل:
- `setWriteBufferSize`: يسيطر على الذاكرة المستخدمة للكتابة.
- `setMaxOpenFiles`: يحدد عدد الملفات المفتوحة.
- `setCompactionStyle`: يعدل كيفية ضغط البيانات على القرص.

استكشف [وثائق RocksDB](https://github.com/facebook/rocksdb/wiki) للحصول على مزيد من الخيارات.

---

### 8. **مثال بسيط**
هنا مثال كامل يوضح فتح قاعدة بيانات، تخزين زوج مفاتيح-قيم، واسترجاعه:

```java
import org.rocksdb.RocksDB;
import org.rocksdb.Options;

public class SimpleRocksDBExample {
    public static void main(String[] args) {
        RocksDB.loadLibrary();  // تحميل المكتبة الأصلية
        Options options = new Options().setCreateIfMissing(true);

        try (RocksDB db = RocksDB.open(options, "/tmp/rocksdb_example")) {
            // وضع زوج مفاتيح-قيم
            db.put("hello".getBytes(), "world".getBytes());

            // استرجاع القيمة
            byte[] value = db.get("hello".getBytes());
            if (value != null) {
                System.out.println(new String(value));  // يطباع "world"
            } else {
                System.out.println("لم يتم العثور على المفتاح");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

**الخروج**: `world`

---

### ملاحظات مهمة
- **طبيعة المحبسة**: RocksDB يعمل داخل عملية تطبيقك، وليس كخادم منفصل.
- **مصفوفات البايت**: المفاتيح والقيم هي `byte[]`، لذا عليك التعامل مع التسلسل/الترميز للأشياء المعقدة.
- **الأداء**: RocksDB يبرز في التخزين السريع (على سبيل المثال، SSDs) ويستخدم في أنظمة الأداء العالي مثل تلك في Facebook، حيث تم تطويرها.
- **غير علاقة**: إنها مخزن مفاتيح-قيم، وليس قاعدة بيانات علاقة — لا SQL أو اندماج.

---

### الأخطاء الشائعة
- **نسيان `RocksDB.loadLibrary()`**: يؤدي إلى `UnsatisfiedLinkError`.
- **إدارة الموارد غير مناسبة**: عدم إغلاق قاعدة البيانات يمكن أن يسبب مشاكل، خاصة على الأنظمة المحدودة الموارد.
- **خطأ في أنواع البيانات**: تمرير الأسلوب أو الكائنات مباشرة بدلاً من تحويلها إلى `byte[]`.

---

### الذهاب أبعد
- **الميزات المتقدمة**: استكشف المعاملات، الفواصل الزمنية، أو عائلات الأعمدة لمزيد من الحالات المعقدة.
- **الموارد**: تحقق من [Java API RocksDB](https://github.com/facebook/rocksdb/tree/main/java) و [RocksDB Wiki](https://github.com/facebook/rocksdb/wiki) للحصول على وثائق و أمثلة مفصلة.

يوفر هذا الدليل أساسًا صلبًا لاستخدام `org.rocksdb`. إذا كنت تحتاج إلى مساعدة في خصائص أو حالات استخدام معينة، فلا تتردد في طلب المساعدة!