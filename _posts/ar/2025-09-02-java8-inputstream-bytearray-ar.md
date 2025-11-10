---
audio: false
generated: true
image: false
lang: ar
layout: post
title: 'جافا 8: تحويل InputStream إلى مصفوفة بايت'
translated: true
type: note
---

ملاحظة جيدة 👍 — في **Java 8** الدالة `InputStream.readAllBytes()` غير موجودة (تمت إضافتها في Java 9).
أنت بحاجة لقراءة body الطلب يدويًا إلى `byte[]`.

إليك بعض الطرق الشائعة:

---

### 1. استخدام `ByteArrayOutputStream` (الأكثر شيوعًا)

```java
public static byte[] toByteArray(InputStream input) throws IOException {
    ByteArrayOutputStream buffer = new ByteArrayOutputStream();
    byte[] data = new byte[1024];
    int nRead;
    while ((nRead = input.read(data, 0, data.length)) != -1) {
        buffer.write(data, 0, nRead);
    }
    buffer.flush();
    return buffer.toByteArray();
}
```

في مُنشئ الـ wrapper الخاص بك:

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. استخدام Apache Commons IO (`IOUtils`)

إذا كان لديك **Apache Commons IO** مُضافًا إلى classpath:

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. استخدام Guava (`ByteStreams`)

إذا كان لديك Guava:

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### لمسة أخيرة للتسجيل (Logging)

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ إذن في Java 8، الخيار **#1 باستخدام ByteArrayOutputStream** هو الأكثر قابلية للنقل.
الخيار **#2 أو #3** أكثر أناقة إذا كنت لا تمانع في إضافة Commons IO أو Guava.

---

هل تريد مني إعادة هيكلة كود `CachedBodyHttpServletRequest` بالكامل ليكون **جاهزًا لـ Java 8** (مكتفي ذاتيًا، بدون `readAllBytes()`)؟