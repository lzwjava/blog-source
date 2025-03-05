---
audio: false
generated: true
lang: ar
layout: post
title: تحليل أركان السطر الأوامر في جافا
translated: true
---

لاستخدام `net.sourceforge.argparse4j`، مكتبة Java لتحليل حجج السطر الأوامر مستوحاة من `argparse` في Python، اتبع هذه الخطوات:

---

### 1. **إضافة التبعية**
لإضافة `argparse4j` إلى مشروعك، أضفها كتعبية. إذا كنت تستخدم Maven، قم بتحديث ملف `pom.xml` الخاص بك بالآتي:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

لأدوات بناء أخرى مثل Gradle، تحقق من [مستودع Maven Central](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) للحصول على التكوين المتوافق.

---

### 2. **إنشاء كائن `ArgumentParser`**
ابدأ بإنشاء كائن `ArgumentParser` باستخدام `ArgumentParsers.newFor("prog").build()`, حيث `"prog"` هو اسم برنامجك. يمكنك أيضًا إضافة وصف وتمكين إنشاء المساعدة تلقائيًا.

**مثال:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // تمكين خيار -h/--help
    .description("حساب قيمة التحقق من الملفات المحدد.");
```

---

### 3. **إضافة حجج**
حدد حجج السطر الأوامر التي سيقبلها برنامجك باستخدام `parser.addArgument()`. يمكنك تحديد:
- **حجج اختيارية** (مثل `-t`, `--type`) مع علامات، خيارات، قيم افتراضية، ونص المساعدة.
- **حجج موقعة** (مثل `file`) مع دعم طول متغير اختياري باستخدام `.nargs("*")`.

**مثال:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // قيود على هذه الخيارات
    .setDefault("SHA-256")                  // القيمة الافتراضية إذا لم يتم توفيرها
    .help("حدد دالة التشفير المستخدمة");  // وصف للرسالة المساعدة

parser.addArgument("file")
    .nargs("*")                             // يقبل صفر أو أكثر من الحجج
    .help("ملف لحساب قيمة التحقق");    // وصف للرسالة المساعدة
```

---

### 4. **تحليل حجج السطر الأوامر**
تحليل حجج السطر الأوامر (عادة ما يتم تمريرها ك `String[] args` من طريقة `main` الخاصة بك) باستخدام `parser.parseArgs()`. احاط هذا بالكتلة `try-catch` لتعامل مع أخطاء التحليل بشكل لطيف.

**مثال:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("حساب قيمة التحقق من الملفات المحدد.");

        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("حدد دالة التشفير المستخدمة");
        parser.addArgument("file").nargs("*")
            .help("ملف لحساب قيمة التحقق");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // تحليل الحجج
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // طباعة الخطأ والرسالة المساعدة
            System.exit(1);               // الخروج عند الخطأ
        }
    }
}
```

---

### 5. **الوصول إلى القيم المحللة**
يرجع طريقة `parseArgs()` كائن `Namespace` يحتوي على قيم الحجج المحللة. استخدم طرقًا مثل `getString()` أو `getList()` لاسترجاعها.

**مثال:**
```java
String hashType = ns.getString("type");  // مثل "SHA-256"
List<String> files = ns.getList("file"); // قائمة بأسماء الملفات

System.out.println("نوع التشفير: " + hashType);
System.out.println("الملفات: " + files);
```

---

### جمع كل شيء معًا
هنا مثال كامل:

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // الخطوة 2: إنشاء المحلل
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("حساب قيمة التحقق من الملفات المحدد.");

        // الخطوة 3: إضافة حجج
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("حدد دالة التشفير المستخدمة");
        parser.addArgument("file").nargs("*")
            .help("ملف لحساب قيمة التحقق");

        // الخطوة 4: تحليل الحجج
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // الخطوة 5: الوصول إلى القيم المحللة
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // مثال على الإخراج
        System.out.println("نوع التشفير: " + hashType);
        System.out.println("الملفات: " + files);
    }
}
```

---

### ميزات إضافية
- **المساعدة التلقائية**: قم بتشغيل برنامجك مع `-h` أو `--help` لرؤية رسالة مساعدة مولدة.
- **الأوامر الفرعية**: استخدم `parser.addSubparsers()` لأوامر معقدة (مثل `git commit`, `git push`).
- **التعليقات**: ربط الحجج بحقول الفئة باستخدام التعليقات (انظر دليل المستخدم للحصول على التفاصيل).

لاستخدام متقدم، استشِر [دليل المستخدم Argparse4j](https://argparse4j.github.io/userguide.html).

---

يتيح لك هذا السيل العمل على تحليل وعلاج حجج السطر الأوامر في تطبيقك باستخدام `net.sourceforge.argparse4j` بسهولة.