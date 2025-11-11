---
audio: false
generated: true
lang: ar
layout: post
title: ترميز وفك ترميز الأحرف في جافا
translated: true
type: note
---

يوفر حزمة `java.nio.charset` في Java أدوات للتعامل مع ترميز وفك تشفير الأحرف، وهو أمر أساسي عند العمل مع بيانات النص بتنسيقات مختلفة أو عبر أنظمة متنوعة. فيما يلي دليل شامل حول كيفية استخدام هذه الحزمة بفعالية.

---

#### **ما هي حزمة `java.nio.charset`؟**
تحتوي حزمة `java.nio.charset` على فئات تدير مجموعات الأحرف (charsets)، والتي تحدد كيفية ترميز الأحرف إلى بايتات وفك تشفيرها مرة أخرى إلى أحرف. هذا أمر بالغ الأهمية لمهام مثل قراءة وكتابة الملفات، والاتصال عبر الشبكة، أو معالجة النص بلغات مختلفة، حيث قد يتم استخدام ترميزات مثل UTF-8 أو ISO-8859-1 أو غيرها.

الفئة الأساسية في هذه الحزمة هي `Charset`، مدعومة بفئات إضافية مثل `CharsetEncoder` و `CharsetDecoder` لحالات الاستخدام المتقدمة.

---

#### **الفئات الرئيسية في `java.nio.charset`**
1. **`Charset`**  
   تمثل ترميزًا للأحرف (مثل UTF-8، ISO-8859-1). تستخدم هذه الفئة لتحديد الترميز للتحويلات بين البايتات والأحرف.

2. **`StandardCharsets`**  
   فئة أدوات توفر ثوابت لمجموعات الأحرف شائعة الاستخدام، مثل `StandardCharsets.UTF_8` أو `StandardCharsets.ISO_8859_1`. إنها تلغي الحاجة للبحث يدويًا عن أسماء مجموعات الأحرف.

3. **`CharsetEncoder` و `CharsetDecoder`**  
   تقدم هذه الفئات تحكمًا دقيقًا في عملية الترميز (تحويل الأحرف إلى بايتات) وفك التشفير (تحويل البايتات إلى أحرف)، وتُستخدم عادةً مع buffers الخاصة بـ NIO مثل `ByteBuffer` و `CharBuffer`.

---

#### **كيفية استخدام `java.nio.charset`**

##### **1. الحصول على كائن `Charset`**
للبدء في استخدام `java.nio.charset`، تحتاج إلى كائن `Charset`. هناك طريقتان رئيسيتان للحصول عليه:

- **استخدام `StandardCharsets`** (مُوصى به لمجموعات الأحرف الشائعة):
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // مجموعة أحرف UTF-8 محددة مسبقًا
  ```

- **استخدام `Charset.forName()`** (لأي مجموعة أحرف مدعومة):
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // مجموعة أحرف UTF-8
  ```
  ملاحظة: إذا كان اسم مجموعة الأحرف غير صالح، فإن هذا يرمي استثناء `UnsupportedCharsetException`، لذا تعامل معه بشكل مناسب:
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("Charset not supported: " + e.getMessage());
  }
  ```

---

##### **2. الاستخدام الأساسي: التحويل بين الـ Strings والبايتات**
في معظم التطبيقات، يمكنك استخدام `Charset` مع فئة `String` لترميز النص أو فك تشفيره.

- **فك تشفير البايتات إلى String**:
  تحويل مصفوفة بايتات إلى `String` باستخدام مجموعة أحرف محددة:
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // "Hello" بترميز UTF-8
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // الناتج: Hello
  ```

- **ترميز String إلى بايتات**:
  تحويل `String` إلى مصفوفة بايتات باستخدام مجموعة أحرف محددة:
  ```java
  String text = "Hello, world!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

هذه الطرق بسيطة وكافية لمعظم حالات الاستخدام، مثل إدخال/إخراج الملفات أو معالجة النص الأساسية.

---

##### **3. استخدام الـ Readers و الـ Writers**
عند العمل مع الـ streams (مثل `InputStream` أو `OutputStream`)، يمكنك استخدام `InputStreamReader` و `OutputStreamWriter` مع `Charset` للتعامل مع بيانات النص.

- **القراءة من InputStream**:
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  InputStream inputStream = new FileInputStream("file.txt");
  InputStreamReader reader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
  int data;
  while ((data = reader.read()) != -1) {
      System.out.print((char) data);
  }
  reader.close();
  ```

- **الكتابة إلى OutputStream**:
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("Hello, world!");
  writer.close();
  ```

ملاحظة: تقبل هذه الفئات إما اسم مجموعة الأحرف (مثل `"UTF-8"`) أو كائن `Charset`.

---

##### **4. عمليات الملفات المبسطة مع `java.nio.file.Files`**
منذ Java 7، توفر حزمة `java.nio.file` طرقًا ملائمة لقراءة وكتابة الملفات باستخدام `Charset`:

- **قراءة ملف إلى String**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **كتابة String إلى ملف**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "Hello, world!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

تتعامل هذه الطرق مع الترميز وفك التشفير داخليًا، مما يجعلها مثالية لعمليات الملفات المباشرة.

---

##### **5. الاستخدام المتقدم: `CharsetEncoder` و `CharsetDecoder`**
بالنسبة للسيناريوهات التي تتطلب تحكمًا أكبر (مثل العمل مع قنوات NIO أو معالجة البيانات الجزئية)، استخدم `CharsetEncoder` و `CharsetDecoder`.

- **الترميز باستخدام `CharsetEncoder`**:
  تحويل الأحرف إلى بايتات باستخدام buffers الخاصة بـ NIO:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetEncoder encoder = charset.newEncoder();
  CharBuffer charBuffer = CharBuffer.wrap("Hello");
  ByteBuffer byteBuffer = encoder.encode(charBuffer);
  byte[] bytes = byteBuffer.array();
  ```

- **فك التشفير باستخدام `CharsetDecoder`**:
  تحويل البايتات إلى أحرف:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetDecoder decoder = charset.newDecoder();
  ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[]{72, 101, 108, 108, 111});
  CharBuffer charBuffer = decoder.decode(byteBuffer);
  String text = charBuffer.toString();
  System.out.println(text); // الناتج: Hello
  ```

هذه الفئات مفيدة عند العمل مع `SocketChannel` أو `FileChannel` أو مكونات NIO أخرى حيث تصل البيانات على شكل أجزاء.

---

#### **أفضل الممارسات**
- **حدد مجموعة الأحرف دائمًا**: تجنب الاعتماد على `Charset.defaultCharset()`، لأن الافتراضي يختلف باختلاف النظام الأساسي (مثل UTF-8 على Linux، windows-1252 على Windows). يضمن تحديد مجموعة الأحرف بشكل صريح سلوكًا متسقًا:
  ```java
  // تجنب هذا:
  byte[] bytes = "Hello".getBytes(); // يستخدم مجموعة الأحرف الافتراضية للنظام الأساسي

  // افعل هذا:
  byte[] bytes = "Hello".getBytes(StandardCharsets.UTF_8);
  ```

- **استخدم `StandardCharsets`**: إنه أكثر نظافة ويتجنب الاستثناءات أثناء التشغيل الناتجة عن أسماء مجموعات أحرف غير صالحة.

- **تعامل مع الاستثناءات**: عند استخدام `Charset.forName()`، التقط `UnsupportedCharsetException` لمجموعات الأحرف غير المدعومة.

---

#### **الخلاصة**
لاستخدام `java.nio.charset`:
1.  **احصل على `Charset`** باستخدام `StandardCharsets` أو `Charset.forName()`.
2.  **نفذ التحويلات**:
    - استخدم طرق `String` (`getBytes()`، المُنشئ) للتحويلات البسيطة بين البايتات والأحرف.
    - استخدم `InputStreamReader`/`OutputStreamWriter` للـ streams.
    - استخدم `Files.readString()`/`writeString()` لعمليات الملفات.
    - استخدم `CharsetEncoder`/`CharsetDecoder` لسيناريوهات NIO المتقدمة.
3.  **ضمن إمكانية النقل** من خلال تحديد مجموعات الأحرف بشكل صريح.

توفر هذه الحزمة أدوات مرنة وقوية لإدارة ترميز الأحرف، مما يجعل تطبيقات Java الخاصة بك قوية ومتوافقة مع بيانات النص المتنوعة.