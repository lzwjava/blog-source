---
audio: false
generated: true
lang: ar
layout: post
title: قراءة الإدخال من الواجهة في جافا
translated: true
---

لاستخدام حزمة `org.jline.reader` في Java، والتي هي جزء من مكتبة JLine لتسجيل الإدخال من الواجهة السطرية مع ميزات متقدمة مثل تحرير السطر، التاريخ، والتكملة، اتبع هذه الخطوات. يوفر هذا الدليل نهجًا شاملًا وممارسًا للحصول على البدء.

### المتطلبات الأساسية
تأكد من إضافة مكتبة JLine إلى مشروعك. إذا كنت تستخدم Maven، أضف التبعية التالية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- استخدم أحدث الإصدار -->
</dependency>
```

### الخطوات الأساسية لاستخدام `org.jline.reader`

1. **إنشاء مثيل للواجهة السطرية**
   - استخدم فئة `TerminalBuilder` من `org.jline.terminal` لإنشاء مثيل `Terminal`. يمثل هذا الواجهة السطرية حيث سيتم قراءة الإدخال.
   - المثال:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - يخلق طريقة `build()` واجهة سطرية افتراضية مناسبة لمعظم البيئات. يمكنك تخصيصها بشكل أكبر (مثل تعيين نوع الواجهة السطرية)، ولكن الافتراضي غالبًا ما يكون كافيًا.

2. **إنشاء مثيل `LineReader`**
   - استخدم فئة `LineReaderBuilder` من `org.jline.reader` لإنشاء مثيل `LineReader`، مرسلًا إليه مثيل `Terminal`.
   - `LineReader` هو الواجهة الرئيسية لقراءة الإدخال المستخدم مع ميزات JLine.
   - المثال:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **قراءة الإدخال من المستخدم**
   - استخدم طريقة `readLine()` من `LineReader` لقراءة سطر نصي أدخله المستخدم. يمكنك تحديد تلميح عرضه بشكل اختياري.
   - المثال:
     ```java
     String line = reader.readLine("> ");
     ```
   - يعرض هذا `> ` كتلميح، ينتظر الإدخال المستخدم، ويرجع السلسلة المدخلة عندما يضغط المستخدم على Enter.

### مثال بسيط
هنا مثال كامل، بسيط، يقرأ الإدخال المستخدم في حلقة حتى يكتب المستخدم "exit":

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // إنشاء Terminal
        Terminal terminal = TerminalBuilder.builder().build();

        // إنشاء LineReader
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // قراءة الإدخال في حلقة
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("لقد أدخلت: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **الخروج**: عند تشغيل هذا، يعرض تلميح `> `. يمكنك كتابة النص، استخدام زر الحذف أو الأزرار السهمية للتحرير (ميزات غير متاحة بسهولة مع `System.in`), واضغط على Enter. كتابة "exit" تنتهي بالبرنامج.

### الميزات الاختيارية
يمكنك تحسين `LineReader` بمزيد من الوظائف:

#### 1. **تفعيل تاريخ الأوامر**
   - أضف مثيل `History` لتخزين وإعادة استدعاء الإدخالات السابقة (مثل استخدام الأزرار السهمية لأعلى/أسفل).
   - المثال:
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - الآن، يمكن للمستخدم التنقل عبر تاريخ الإدخال الخاص به.

#### 2. **إضافة التكملة التلقائية**
   - قم بتطبيق `Completer` لتقديم تكملات عندما يضغط المستخدم على Tab.
   - مثال مع تكملات نصية بسيطة:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - كتابة "f" واضغط على Tab يقدّم "foo".

#### 3. **قراءة كلمات المرور (إدخال مخفي)**
   - استخدم `readLine()` مع رمز مخفي لإخفاء الإدخال (مثل كلمات المرور).
   - المثال:
     ```java
     String password = reader.readLine("أدخل كلمة المرور: ", '*');
     ```
   - يعرض نجوم (`*`) بدلاً من الأحرف المدخلة.

### إدارة الموارد
للتطبيقات القوية، أغلق `Terminal` عند الانتهاء لتحرير الموارد. نظرًا لأن `Terminal` يدمج `Closeable`, استخدم كتلة try-with-resources:

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("لقد أدخلت: " + line);
}
```

### لماذا استخدام `org.jline.reader`؟
بخلاف الإدخال الأساسي مع `System.in` و `BufferedReader`, يوفر `org.jline.reader`:
- **تحرير السطر**: الحذف، حركة المؤشر، إلخ.
- **التاريخ**: استدعاء الإدخالات السابقة.
- **التكملة**: اقتراح الخيارات.
- **معالجة الواجهة السطرية عبر المنصات**: يعمل بشكل متساوٍ عبر بيئات مختلفة.

### ملاحظات
- إذا لم تقم بتحديد `Terminal` في `LineReaderBuilder`, فإنه يخلق واجهة سطرية افتراضية داخليًا، لذا `LineReader reader = LineReaderBuilder.builder().build();` يعمل في الحالات البسيطة.
- تجنب استدعاء `readLine()` من عدة خيوط في نفس الوقت، حيث أن `LineReader` ليس آمنًا للقراءة المتزامنة.
- لاستخدامات متقدمة (مثل الإدخال متعدد السطور، روابط المفاتيح المخصصة)، استكشف ميزات JLine الإضافية مثل المفسرين أو خريطة المفاتيح.

يغطي هذا الأساسيات لاستخدام `org.jline.reader` لقراءة الإدخال من الواجهة السطرية في Java بشكل فعال. ابدأ بالإعداد الأساسي وأضيف الميزات مثل التاريخ أو التكملة حسب الحاجة لتطبيقك!