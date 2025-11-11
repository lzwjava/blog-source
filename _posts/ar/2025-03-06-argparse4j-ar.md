---
audio: false
generated: true
lang: ar
layout: post
title: تحليل وسائط سطر الأوامر في جافا
translated: true
type: note
---

لاستخدام `net.sourceforge.argparse4j`، وهي مكتبة جافا لتحليل وسيط سطر الأوامر مستوحاة من `argparse` في البايثون، اتبع الخطوات التالية:

---

### 1. **إضافة التبعية**
لتضمين `argparse4j` في مشروعك، أضفها كتبعية. إذا كنت تستخدم Maven، فحدّث ملف `pom.xml` بما يلي:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

أما بالنسبة لأدوات البناء الأخرى مثل Gradle، فتحقق من [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) للحصول على التكوين المكافئ.

---

### 2. **إنشاء كائن `ArgumentParser`**
ابدأ بإنشاء نسخة من `ArgumentParser` باستخدام `ArgumentParsers.newFor("prog").build()`، حيث `"prog"` هو اسم برنامجك. يمكنك أيضًا إضافة وصف وتمكين إنشاء رسالة المساعدة التلقائية.

**مثال:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // يمكّن خيار -h/--help
    .description("Calculate checksum of given files.");
```

---

### 3. **إضافة الوسائط**
عرّف وسيطات سطر الأوامر التي سيقبلها برنامجك باستخدام `parser.addArgument()`. يمكنك تحديد:
- **وسائط اختيارية** (مثل `-t`, `--type`) مع أعلام، خيارات، قيم افتراضية، ونص مساعدة.
- **وسائط موضعية** (مثل `file`) مع دعم اختياري لطول متغير باستخدام `.nargs("*")`.

**مثال:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // تقييد بهذه الخيارات
    .setDefault("SHA-256")                  // القيمة الافتراضية إذا لم يتم تقديمها
    .help("Specify hash function to use");  // الوصف لرسالة المساعدة

parser.addArgument("file")
    .nargs("*")                             // يقبل صفرًا أو أكثر من الوسائط
    .help("File to calculate checksum");    // الوصف لرسالة المساعدة
```

---

### 4. **تحليل وسيطات سطر الأوامر**
حلل وسيطات سطر الأوامر (التي تُمرر عادةً كـ `String[] args` من طريقة `main` الخاصة بك) باستخدام `parser.parseArgs()`. لفّ هذا في كتلة try-catch للتعامل مع أخطاء التحليل بأسلوب أنيق.

**مثال:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("Calculate checksum of given files.");
        
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Specify hash function to use");
        parser.addArgument("file").nargs("*")
            .help("File to calculate checksum");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // تحليل الوسيطات
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // طباعة الخطأ ورسالة المساعدة
            System.exit(1);               // الخروج عند الخطأ
        }
    }
}
```

---

### 5. **الوصول إلى القيم المُحلَّلة**
تُرجع طريقة `parseArgs()` كائن `Namespace` يحتوي على قيم الوسيطات التي تم تحليلها. استخدم طرقًا مثل `getString()` أو `getList()` لاستردادها.

**مثال:**
```java
String hashType = ns.getString("type");  // على سبيل المثال، "SHA-256"
List<String> files = ns.getList("file"); // قائمة بأسماء الملفات

System.out.println("Hash Type: " + hashType);
System.out.println("Files: " + files);
```

---

### جمع كل شيء معًا
إليك مثالاً كاملاً:

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
            .description("Calculate checksum of given files.");

        // الخطوة 3: إضافة الوسائط
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("Specify hash function to use");
        parser.addArgument("file").nargs("*")
            .help("File to calculate checksum");

        // الخطوة 4: تحليل الوسائط
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // الخطوة 5: الوصول إلى القيم المُحلَّلة
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // مثال على المخرجات
        System.out.println("Hash Type: " + hashType);
        System.out.println("Files: " + files);
    }
}
```

---

### ميزات إضافية
- **المساعدة التلقائية**: شغّل برنامجك باستخدام `-h` أو `--help` لرؤية رسالة المساعدة المُنشأة.
- **الأوامر الفرعية**: استخدم `parser.addSubparsers()` للأوامر المعقدة (مثل `git commit`, `git push`).
- **الشرح التوضيحي (Annotations)**: اربط الوسائط بحقول الفئة باستخدام الشرح التوضيحي (راجع دليل المستخدم للحصول على التفاصيل).

للحصول على استخدام متقدم، استشر [دليل مستخدم Argparse4j](https://argparse4j.github.io/userguide.html).

---

يمنحك هذا التدفق العملية القدرة على تحليل ومعالجة وسيطات سطر الأوامر في تطبيق الجافا الخاص بك بسهولة باستخدام `net.sourceforge.argparse4j`.