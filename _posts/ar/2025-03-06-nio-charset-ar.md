---
audio: false
generated: true
lang: ar
layout: post
title: تشفير و فك تشفير الرموز في جاڤا
translated: true
---

العبارة `java.nio.charset` في جافا توفر أدواتًا للتعامل مع تشفير وتشفير الحروف، وهو أمر حاسم عند العمل مع بيانات النص في صيغ مختلفة أو عبر أنظمة مختلفة. أدناه دليل شامل على كيفية استخدام هذه العبارة بشكل فعال.

---

#### **ما هو `java.nio.charset`?**
تحتوي العبارة `java.nio.charset` على فئات تدير مجموعات الحروف (charsets)، والتي تحدد كيفية تشفير الحروف إلى بايتات وتشفيرها إلى حروف مرة أخرى. هذا هو أمر حاسم لمهام مثل قراءة وكتابة الملفات، أو التواصل عبر الشبكة، أو معالجة النص في لغات مختلفة، حيث يمكن استخدام تشفيرات مثل UTF-8، ISO-8859-1، أو غيرها.

الفئة الرئيسية في هذه العبارة هي `Charset`، مدعومة بفئات إضافية مثل `CharsetEncoder` و `CharsetDecoder` لمواقف استخدام متقدمة.

---

#### **الفئات الرئيسية في `java.nio.charset`**
1. **`Charset`**
   يمثل تشفير الحروف (مثل UTF-8، ISO-8859-1). تستخدم هذه الفئة لتحديد التشفير للتحويلات بين البايتات والحروف.

2. **`StandardCharsets`**
   فئة مساعدة تقدم ثوابتًا لمجموعات الحروف المستخدمة بشكل شائع، مثل `StandardCharsets.UTF_8` أو `StandardCharsets.ISO_8859_1`. إنها تقليل الحاجة إلى البحث عن أسماء مجموعات الحروف يدويًا.

3. **`CharsetEncoder` و `CharsetDecoder`**
   هذه الفئات تقدم تحكمًا دقيقًا على التشفير (الحروف إلى البايتات) والتشفير (البايتات إلى الحروف)، وتستخدم عادةً مع حاويات NIO مثل `ByteBuffer` و `CharBuffer`.

---

#### **كيفية استخدام `java.nio.charset`**

##### **1. الحصول على مثال من `Charset`**
لبدء استخدام `java.nio.charset`، تحتاج إلى مثال من `Charset`. هناك طريقتان رئيسيتان للحصول على واحد:

- **استخدام `StandardCharsets`** (موصى به لمجموعات الحروف الشائعة):
  ```java
  import java.nio.charset.StandardCharsets;

  Charset charset = StandardCharsets.UTF_8; // مجموعة الحروف UTF-8 المحدد مسبقًا
  ```

- **استخدام `Charset.forName()`** (لمجموعات الحروف المدعومة أيًا):
  ```java
  import java.nio.charset.Charset;

  Charset charset = Charset.forName("UTF-8"); // مجموعة الحروف UTF-8
  ```
  ملاحظة: إذا كانت اسم المجموعة غير صالح، فإن هذا يرمي `UnsupportedCharsetException`، لذا قم بمعالجته بشكل مناسب:
  ```java
  try {
      Charset charset = Charset.forName("UTF-8");
  } catch (UnsupportedCharsetException e) {
      System.err.println("مجموعة الحروف غير مدعومة: " + e.getMessage());
  }
  ```

---

##### **2. الاستخدام الأساسي: التحويل بين النصوص والبايتات**
لأغلبية التطبيقات، يمكنك استخدام `Charset` مع فئة `String` لتشفير أو تشفير النص.

- **تشفير البايتات إلى نص**:
  تحويل مجموعة بايتات إلى `String` باستخدام مجموعة حروف محددة:
  ```java
  byte[] bytes = {72, 101, 108, 108, 111}; // "مرحبًا" في UTF-8
  Charset charset = StandardCharsets.UTF_8;
  String text = new String(bytes, charset);
  System.out.println(text); // يخرج: مرحبا
  ```

- **تشفير نص إلى بايتات**:
  تحويل `String` إلى مجموعة بايتات باستخدام مجموعة حروف محددة:
  ```java
  String text = "مرحبًا، عالم!";
  Charset charset = StandardCharsets.UTF_8;
  byte[] bytes = text.getBytes(charset);
  ```

هذه الطرق بسيطة وكافية لأغلبية المواقف، مثل إدخال/إخراج الملفات أو معالجة النص الأساسية.

---

##### **3. استخدام القراء والكاتبين**
عند العمل مع التدفقات (مثل `InputStream` أو `OutputStream`)، يمكنك استخدام `InputStreamReader` و `OutputStreamWriter` مع `Charset` للتعامل مع بيانات النص.

- **قراءة من `InputStream`**:
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

- **كتابة إلى `OutputStream`**:
  ```java
  import java.io.*;
  import java.nio.charset.StandardCharsets;

  OutputStream outputStream = new FileOutputStream("file.txt");
  OutputStreamWriter writer = new OutputStreamWriter(outputStream, StandardCharsets.UTF_8);
  writer.write("مرحبًا، عالم!");
  writer.close();
  ```

ملاحظة: هذه الفئات تقبل إما اسم مجموعة الحروف (مثل `"UTF-8"`) أو مثال من `Charset`.

---

##### **4. عمليات الملفات البسيطة مع `java.nio.file.Files`**
منذ جافا 7، توفر العبارة `java.nio.file` طرقًا مريحة لقراءة وكتابة الملفات باستخدام مجموعة حروف:

- **قراءة ملف إلى نص**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = Files.readString(path, StandardCharsets.UTF_8);
  System.out.println(content);
  ```

- **كتابة نص إلى ملف**:
  ```java
  import java.nio.file.*;
  import java.nio.charset.StandardCharsets;

  Path path = Paths.get("file.txt");
  String content = "مرحبًا، عالم!";
  Files.writeString(path, content, StandardCharsets.UTF_8);
  ```

هذه الطرق تتعامل مع تشفير وتشفير داخليًا، مما يجعلها مثالية لعمليات الملفات البسيطة.

---

##### **5. الاستخدام المتقدم: `CharsetEncoder` و `CharsetDecoder`**
للمواقف التي تتطلب تحكمًا أكبر (مثل العمل مع قنوات NIO أو معالجة البيانات الجزئية)، استخدم `CharsetEncoder` و `CharsetDecoder`.

- **تشفير مع `CharsetEncoder`**:
  تحويل الحروف إلى بايتات باستخدام حاويات NIO:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetEncoder encoder = charset.newEncoder();
  CharBuffer charBuffer = CharBuffer.wrap("مرحبًا");
  ByteBuffer byteBuffer = encoder.encode(charBuffer);
  byte[] bytes = byteBuffer.array();
  ```

- **تشفير مع `CharsetDecoder`**:
  تحويل البايتات إلى حروف:
  ```java
  import java.nio.*;
  import java.nio.charset.*;

  Charset charset = StandardCharsets.UTF_8;
  CharsetDecoder decoder = charset.newDecoder();
  ByteBuffer byteBuffer = ByteBuffer.wrap(new byte[]{72, 101, 108, 108, 111});
  CharBuffer charBuffer = decoder.decode(byteBuffer);
  String text = charBuffer.toString();
  System.out.println(text); // يخرج: مرحبا
  ```

هذه الفئات مفيدة عند العمل مع `SocketChannel`، `FileChannel`، أو مكونات NIO أخرى حيث تصل البيانات في قطع.

---

#### **أفضل الممارسات**
- **تحديد مجموعة الحروف دائمًا**: تجنب الاعتماد على `Charset.defaultCharset()`، حيث تختلف القيمة الافتراضية حسب المنصة (مثل UTF-8 في لينكس، windows-1252 في ويندوز). تحديد مجموعة الحروف بشكل صريح يضمن سلوكًا موثوقًا:
  ```java
  // تجنب هذا:
  byte[] bytes = "مرحبًا".getBytes(); // يستخدم مجموعة الحروف الافتراضية للمنصة

  // افعل هذا:
  byte[] bytes = "مرحبًا".getBytes(StandardCharsets.UTF_8);
  ```

- **استخدام `StandardCharsets`**: إنه أكثر نظافة ويقلل من استثناءات التشغيل من أسماء مجموعات الحروف غير الصالحة.

- **معالجة الاستثناءات**: عند استخدام `Charset.forName()`، قم باحتواء `UnsupportedCharsetException` لمجموعات الحروف غير المدعومة.

---

#### **ملخص**
لاستخدام `java.nio.charset`:
1. **الحصول على `Charset`** باستخدام `StandardCharsets` أو `Charset.forName()`.
2. **أداء التحويلات**:
   - استخدم طرق `String` (`getBytes()`، البناء) للتحويلات البسيطة للبايتات والحروف.
   - استخدم `InputStreamReader`/`OutputStreamWriter` للتدفقات.
   - استخدم `Files.readString()`/`writeString()` لعمليات الملفات.
   - استخدم `CharsetEncoder`/`CharsetDecoder` لمواقف NIO المتقدمة.
3. **تأكد من قابلية النقل** بتحديد مجموعات الحروف بشكل صريح.

توفر هذه العبارة أدواتًا مرنة وقوية لإدارة تشفير الحروف، مما يجعل تطبيقاتك جافا قوية ومتوافقًا مع بيانات النص المتنوعة.