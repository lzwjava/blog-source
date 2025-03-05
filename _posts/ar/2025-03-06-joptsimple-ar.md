---
audio: false
generated: true
lang: ar
layout: post
title: تحليل خيارات السطر الأوامر في جاڤا
translated: true
---

JOptSimple هو مكتبة Java مصممة لتسهيل تحليل خيارات السطر الأوامر في تطبيقاتك. تسمح لك بتحديد وتحليل الخيارات مثل الأعلام (مثل `-v` للوضع الصريح) وخيارات مع حجج (مثل `--file input.txt`) بطريقة مرنة ومفيدة. أدناه دليل خطوة بخطوة على كيفية استخدام JOptSimple بشكل فعال.

---

### **الخطوة 1: إضافة JOptSimple إلى مشروعك**
لاستخدام JOptSimple، عليك أولاً تضمينه في مشروعك Java. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

تأكد من التحقق من أحدث الإصدار على Maven Central، حيث قد لا يكون `5.0.4` هو أحدث الإصدار. بالنسبة لأدوات البناء الأخرى مثل Gradle، يمكنك تعديل التبعية بشكل مناسب (مثل `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`).

---

### **الخطوة 2: إنشاء OptionParser**
القلب من JOptSimple هو فئة `OptionParser` التي تستخدمها لتحديد وتحليل خيارات السطر الأوامر. ابدأ بإنشاء مثيل منها في طريقة `main` الخاصة بك:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // تحديد الخيارات هنا (انظر الخطوة 3)
    }
}
```

---

### **الخطوة 3: تحديد خيارات السطر الأوامر**
يمكنك تحديد الخيارات باستخدام طرق `accepts` أو `acceptsAll`. يمكن أن تكون الخيارات أعلام (بدون حجج) أو خيارات تتطلب حجج (مثل اسم ملف أو عدد). إليك كيفية إعدادها:

- **الأعلام**: استخدم `accepts` لأسم خيار واحد أو `acceptsAll` لتحديد أسماء بديلة (مثل `-v` و `--verbose`):
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "تفعيل الوضع الصريح");
  ```

- **خيارات مع حجج**: استخدم `withRequiredArg()` لإشارة إلى أن خيار يحتاج إلى قيمة، واختياري تحديد نوعها باستخدام `ofType()`:
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "تحديد ملف المدخل").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "تحديد العدد").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` يحدد قيمة افتراضية (مثل `0`) إذا لم يتم توفير الخيار.
  - `ofType(Integer.class)` يضمن أن يتم تحليل الحجة كعدد صحيح.

- **خيار المساعدة**: أضف علم المساعدة (مثل `-h` أو `--help`) لعرض معلومات الاستخدام:
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "عرض هذه الرسالة المساعدة");
  ```

---

### **الخطوة 4: تحليل حجج السطر الأوامر**
قم بتحويل مصفوفة `args` من طريقة `main` إلى المحلل لتحليل المدخلات السطر الأوامر. هذا يعيد كائن `OptionSet` يحتوي على الخيارات المحللة:

```java
OptionSet options = parser.parse(args);
```

قم بتغليف هذا في كتلة `try-catch` لمعالجة أخطاء التحليل (مثل الخيارات غير الصالحة أو الحجج المفقودة):

```java
try {
    OptionSet options = parser.parse(args);
    // معالجة الخيارات (انظر الخطوة 5)
} catch (Exception e) {
    System.err.println("خطأ: " + e.getMessage());
    try {
        parser.printHelpOn(System.err);
    } catch (IOException ex) {
        ex.printStackTrace();
    }
    System.exit(1);
}
```

---

### **الخطوة 5: الوصول إلى الخيارات المحللة**
استخدم `OptionSet` للتحقق من الأعلام، استرجاع قيم الخيارات، واسترجاع الحجج غير المرتبطة بالخيارات:

- **تحقق من الأعلام**: استخدم `has()` لرؤية إذا كان علم موجود:
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("تم تفعيل الوضع الصريح");
  }
  ```

- **استرجاع قيم الخيارات**: استخدم `valueOf()` لاسترجاع حجة خيار، قم بتحويلها إلى النوع المناسب إذا لزم الأمر:
  ```java
  String fileName = (String) options.valueOf("f"); // يعيد `null` إذا لم يتم تحديده
  int count = (Integer) options.valueOf("c");     // يعيد `0` بسبب `defaultsTo(0)`
  ```

  إذا قمت بتحديد `ofType()` و `defaultsTo()`، يعيد `valueOf()` القيمة المحدد نوعها أو القيمة الافتراضية.

- **حجج غير مرتبطة بالخيارات**: استرجاع الحجج التي ليست مرتبطة بالخيارات (مثل قائمة من الملفات) باستخدام `nonOptionArguments()`:
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("الملفات: " + files);
  ```

- **معالجة المساعدة**: طباعة معلومات الاستخدام إذا كان خيار المساعدة موجود:
  ```java
  if (options.has("h")) {
      parser.printHelpOn(System.out);
      System.exit(0);
  }
  ```

---

### **مثال: جمع كل شيء**
إليك مثال كامل لبرنامج يقبل علم صريح، خيار عدد، وقائمة من الملفات:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        parser.acceptsAll(Arrays.asList("v", "verbose"), "تفعيل الوضع الصريح");
        parser.acceptsAll(Arrays.asList("c", "count"), "تحديد العدد")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "عرض هذه الرسالة المساعدة");

        try {
            OptionSet options = parser.parse(args);

            if (options.has("h")) {
                parser.printHelpOn(System.out);
                System.exit(0);
            }

            boolean verbose = options.has("v");
            int count = (Integer) options.valueOf("c");
            List<String> files = options.nonOptionArguments();

            if (verbose) {
                System.out.println("تم تفعيل الوضع الصريح");
            }
            System.out.println("العدد: " + count);
            System.out.println("الملفات: " + files);

        } catch (Exception e) {
            System.err.println("خطأ: " + e.getMessage());
            try {
                parser.printHelpOn(System.err);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            System.exit(1);
        }
    }
}
```

قم بتشغيل هذا مع: `java MyApp -v -c 5 file1 file2`، وسيخرج:
```
تم تفعيل الوضع الصريح
العدد: 5
الملفات: [file1, file2]
```

قم بتشغيله مع `-h`، وسيعرض رسالة الاستخدام مع جميع الخيارات المحددة.

---

### **ميزات إضافية**
- **قيم متعددة**: السماح لخيار أن يظهر مرات متعددة (مثل `-I dir1 -I dir2`):
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // يعيد قائمة
  ```

- **حجج اختيارية**: استخدم `withOptionalArg()` بدلاً من `withRequiredArg()` إذا لم تكن الحجة مطلوبة:
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **معالجة الأخطاء**: يرمي JOptSimple استثناء `OptionException` لأخطاء التحليل، يمكنك القبض عليه لتقديم ردود فعل مستخدمية.

---

### **ملخص**
JOptSimple يجعل من السهل التعامل مع خيارات السطر الأوامر في Java. يمكنك:
1. إضافة المكتبة إلى مشروعك.
2. إنشاء `OptionParser` وتحديد الخيارات (الأعلام، الحجج، القيم الافتراضية).
3. تحليل مصفوفة `args` إلى `OptionSet`.
4. استخدام `OptionSet` للوصول إلى الأعلام، القيم، والحجج غير المرتبطة بالخيارات.
5. معالجة الأخطاء وتقديم المساعدة حسب الحاجة.

مع هذه الأساسيات، يمكنك بناء واجهات السطر الأوامر قوية مخصصة لحاجات تطبيقك!