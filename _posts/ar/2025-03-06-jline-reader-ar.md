---
audio: false
generated: true
lang: ar
layout: post
title: قراءة إدخال وحدة التحكم في جافا
translated: true
type: note
---

لاستخدام حزمة `org.jline.reader` في جافا، والتي تعد جزءًا من مكتبة JLine للتعامل مع إدخال وحدة التحكم بميزات متقدمة مثل تحرير الأسطر، والسجل، والإكمال التلقائي، اتبع هذه الخطوات. يقدم هذا الدليل نهجًا كاملاً وعمليًا لمساعدتك في البدء.

### المتطلبات الأساسية
تأكد من إضافة مكتبة JLine إلى مشروعك. إذا كنت تستخدم Maven، فقم بتضمين الاعتماد التالي في ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- استخدم أحدث إصدار -->
</dependency>
```

### الخطوات الأساسية لاستخدام `org.jline.reader`

1. **إنشاء مثيل لـ Terminal**
   - استخدم صنف `TerminalBuilder` من `org.jline.terminal` لإنشاء كائن `Terminal`. يمثل هذا بيئة وحدة التحكم حيث سيتم قراءة الإدخال.
   - مثال:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - تنشئ الدالة `build()` طرفية افتراضية مناسبة لمعظم البيئات. يمكنك تخصيصها further (مثل تعيين نوع الطرفية)، ولكن الافتراضي غالبًا ما يكون كافيًا.

2. **إنشاء مثيل لـ LineReader**
   - استخدم صنف `LineReaderBuilder` من `org.jline.reader` لإنشاء كائن `LineReader`، وتمرير مثيل `Terminal` إليه.
   - يعد `LineReader` الواجهة الرئيسية لقراءة إدخال المستخدم بميزات JLine.
   - مثال:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **قراءة الإدخال من المستخدم**
   - استخدم الدالة `readLine()` الخاصة بـ `LineReader` لقراءة سطر نصي أدخله المستخدم. يمكنك اختياريًا تحديد موجه prompt لعرضه.
   - مثال:
     ```java
     String line = reader.readLine("> ");
     ```
   - يعرض هذا `> ` كموجه، وينتظر إدخال المستخدم، ويعيد السلسلة المدخلة عندما يضغط المستخدم على Enter.

### مثال بسيط
إليك مثالاً كاملاً وبسيطًا يقرأ إدخال المستخدم في حلقة حتى يقوم المستخدم بكتابة "exit":

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

- **الإخراج**: عند تشغيل هذا، سيعرض موجه `> `. يمكنك كتابة نص، واستخدام مفتاح backspace أو مفاتيح الأسهم للتعديل (ميزات غير متاحة بسهولة مع `System.in`)، والضغط على Enter. كتابة "exit" تنهي البرنامج.

### ميزات اختيارية
يمكنك تحسين `LineReader` بوظائف إضافية:

#### 1. **تمكين سجل الأوامر History**
   - أضف كائن `History` لتخزين واستدعاء المدخلات السابقة (على سبيل المثال، استخدام مفاتيح الأسهم لأعلى/لأسفل).
   - مثال:
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - الآن، يمكن للمستخدم التنقل خلال سجل إدخاله.

#### 2. **إضافة الإكمال التلقائي Auto-Completion**
   - نفذ `Completer` لاقتراح إكمالات عندما يضغط المستخدم على Tab.
   - مثال باستخدام String completer بسيط:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - كتابة "f" والضغط على Tab ستقترح "foo".

#### 3. **قراءة كلمات المرور (إدخال مقنّع)**
   - استخدم `readLine()` مع حرف قناع لإخفاء الإدخال (على سبيل المثال، لكلمات المرور).
   - مثال:
     ```java
     String password = reader.readLine("أدخل كلمة المرور: ", '*');
     ```
   - يعرض نجومًا (`*`) بدلاً من الأحرف المكتوبة.

### إدارة الموارد
للحصول على تطبيقات قوية Robust، قم بإغلاق `Terminal` عند الانتهاء لتحرير الموارد. نظرًا لأن `Terminal` ينفذ `Closeable`، استخدم كتلة try-with-resources:

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("لقد أدخلت: " + line);
}
```

### لماذا تستخدم `org.jline.reader`؟
على عكس الإدخال الأساسي باستخدام `System.in` و `BufferedReader`، يوفر `org.jline.reader`:
- **تحرير الأسطر**: Backspace، حركة المؤشر، إلخ.
- **السجل History**: استدعاء المدخلات السابقة.
- **الإكمال Completion**: اقتراح الخيارات تلقائيًا.
- **التعامل مع الطرفيات عبر المنصات المختلفة**: يعمل بشكل متسق عبر البيئات المختلفة.

### ملاحظات
- إذا لم تحدد `Terminal` في `LineReaderBuilder`، فإنه ينشئ واحدة افتراضية داخليًا، لذا فإن `LineReader reader = LineReaderBuilder.builder().build();` يعمل في الحالات البسيطة.
- تجنب استدعاء `readLine()` من خيوط متعددة في وقت واحد، لأن `LineReader` ليس آمنًا للاستخدام في الخيوط المتزامنة للقراءات المتعددة.
- لحالات الاستخدام المتقدمة (مثل الإدخال متعدد الأسطر، ربط مفاتيح مخصص)، استكشف ميزات JLine الإضافية مثل المحللات Parsers أو خرائط المفاتيح Key maps.

يغطي هذا الأساسيات اللازمة لاستخدام `org.jline.reader` لقراءة إدخال وحدة التحكم في جافا بشكل فعال. ابدأ بالإعداد الأساسي وأضف ميزات مثل السجل أو الإكمال التلقائي حسب الحاجة لتطبيقك!