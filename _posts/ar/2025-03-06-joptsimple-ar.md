---
audio: false
generated: true
lang: ar
layout: post
title: تحليل خيارات سطر الأوامر في جافا
translated: true
type: note
---

JOptSimple هي مكتبة جافا مصممة لتبسيط تحليل خيارات سطر الأوامر في تطبيقاتك. تتيح لك تعريف ومعالجة خيارات مثل الأعلام (مثل `-v` لوضع التفصيل) والخيارات ذات الوسائط (مثل `--file input.txt`) بطريقة مرنة وبديهية. فيما يلي دليل خطوة بخطوة حول كيفية استخدام JOptSimple بفعالية.

---

### **الخطوة 1: إضافة JOptSimple إلى مشروعك**
لاستخدام JOptSimple، تحتاج أولاً إلى تضمينها في مشروع الجافا الخاص بك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

تأكد من التحقق من أحدث إصدار على Maven Central، حيث أن `5.0.4` قد لا يكون الأحدث. لأدوات بناء أخرى مثل Gradle، يمكنك تكييف التبعية وفقًا لذلك (مثال: `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`).

---

### **الخطوة 2: إنشاء OptionParser**
جوهر JOptSimple هو فئة `OptionParser`، التي تستخدمها لتعريف وتحليل خيارات سطر الأوامر. ابدأ بإنشاء مثيل منها في طريقة `main` الخاصة بك:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // قم بتعريف الخيارات هنا (انظر الخطوة 3)
    }
}
```

---

### **الخطوة 3: تعريف خيارات سطر الأوامر**
يمكنك تعريف الخيارات باستخدام طريقي `accepts` أو `acceptsAll`. يمكن أن تكون الخيارات أعلامًا (بدون وسائط) أو خيارات تتطلب وسائط (مثل اسم ملف أو رقم). إليك كيفية إعدادها:

- **الأعلام**: استخدم `accepts` لاسم خيار مفرد أو `acceptsAll` لتحديد أسماء بديلة (مثل `-v` و `--verbose`):
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "تفعيل وضع التفصيل");
  ```

- **الخيارات ذات الوسائط**: استخدم `withRequiredArg()` للإشارة إلى أن الخيار يحتاج إلى قيمة، ويمكنك تحديد نوعه اختياريًا باستخدام `ofType()`:
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "تحديد ملف الإدخال").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "تحديد العدد").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` يحدد قيمة افتراضية (مثل `0`) إذا لم يتم توفير الخيار.
  - `ofType(Integer.class)` يضمن تحليل الوسيط كعدد صحيح.

- **خيار المساعدة**: أضف علم مساعدة (مثل `-h` أو `--help`) لعرض معلومات الاستخدام:
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "عرض رسالة المساعدة هذه");
  ```

---

### **الخطوة 4: تحليل وسائط سطر الأوامر**
مرر مصفوفة `args` من طريقة `main` الخاصة بك إلى المحلل لمعالجة إدخال سطر الأوامر. هذا يُرجع كائن `OptionSet` يحتوي على الخيارات التي تم تحليلها:

```java
OptionSet options = parser.parse(args);
```

لف هذا في كتلة `try-catch` للتعامل مع أخطاء التحليل (مثل الخيارات غير الصالحة أو الوسائط المفقودة):

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

### **الخطوة 5: الوصول إلى الخيارات التي تم تحليلها**
استخدم `OptionSet` للتحقق من وجود الأعلام، واسترداد قيم الخيارات، والحصول على الوسائط غير المرتبطة بخيارات:

- **التحقق من الأعلام**: استخدم `has()` لمعرفة ما إذا كان العلم موجودًا:
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("تم تفعيل وضع التفصيل");
  }
  ```

- **الحصول على قيم الخيارات**: استخدم `valueOf()` لاسترداد وسيط الخيار، مع تحويله إلى النوع المناسب إذا لزم الأمر:
  ```java
  String fileName = (String) options.valueOf("f"); // يُرجع null إذا لم يتم التحديد
  int count = (Integer) options.valueOf("c");     // يُرجع 0 بسبب defaultsTo(0)
  ```

  إذا حددت `ofType()` و `defaultsTo()`، فإن `valueOf()` يُرجع القيمة المكتوبة أو القيمة الافتراضية.

- **الوسائط غير المرتبطة بخيارات**: احصل على الوسائط غير المرتبطة بخيارات (مثل قائمة الملفات) باستخدام `nonOptionArguments()`:
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("الملفات: " + files);
  ```

- **معالجة المساعدة**: اطبع معلومات الاستخدام إذا كان خيار المساعدة موجودًا:
  ```java
  if (options.has("h")) {
      parser.printHelpOn(System.out);
      System.exit(0);
  }
  ```

---

### **مثال: جمع كل شيء معًا**
إليك مثالاً كاملاً لبرنامج يقبل علم تفصيل، وخيار عد، وقائمة ملفات:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        parser.acceptsAll(Arrays.asList("v", "verbose"), "تفعيل وضع التفصيل");
        parser.acceptsAll(Arrays.asList("c", "count"), "تحديد العدد")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "عرض رسالة المساعدة هذه");

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
                System.out.println("تم تفعيل وضع التفصيل");
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

شغّل هذا باستخدام: `java MyApp -v -c 5 file1 file2`، وسيخرج الناتج:
```
تم تفعيل وضع التفصيل
العدد: 5
الملفات: [file1, file2]
```

شغّله باستخدام `-h`، وسيعرض رسالة الاستخدام مع جميع الخيارات المعرفة.

---

### **ميزات إضافية**
- **قيم متعددة**: اسمح بظهور خيار عدة مرات (مثل `-I dir1 -I dir2`):
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // يُرجع قائمة
  ```

- **وسائط اختيارية**: استخدم `withOptionalArg()` بدلاً من `withRequiredArg()` إذا كان الوسيط غير إلزامي:
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **معالجة الأخطاء**: تلقى JOptSimple استثناء `OptionException` لأخطاء التحليل، والذي يمكنك التقاطه لتقديم ملاحظات صديقة للمستخدم.

---

### **الخلاصة**
JOptSimple يسهل التعامل مع خيارات سطر الأوامر في جافا. أنت:
1. تضيف المكتبة إلى مشروعك.
2. تنشئ `OptionParser` وتُعرف الخيارات (أعلام، وسائط، قيم افتراضية).
3. تحلل مصفوفة `args` إلى `OptionSet`.
4. تستخدم `OptionSet` للوصول إلى الأعلام والقيم والوسائط غير المرتبطة بخيارات.
5. تتعامل مع الأخطاء وتوفر المساعدة حسب الحاجة.

بهذه الأساسيات، يمكنك بناء واجهات سطر أوامر قوية ومصممة خصيصًا لاحتياجات تطبيقك!