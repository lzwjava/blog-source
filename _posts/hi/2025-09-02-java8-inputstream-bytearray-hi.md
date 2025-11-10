---
audio: false
generated: true
image: false
lang: hi
layout: post
title: जावा 8 इनपुट स्ट्रीम से बाइट सरणी
translated: true
type: note
---

अच्छा पकड़ा 👍 — **Java 8** में `InputStream.readAllBytes()` मौजूद नहीं है (यह Java 9 में जोड़ा गया था)।
आपको request body को मैन्युअली एक `byte[]` में पढ़ना होगा।

यहां कुछ सामान्य तरीके दिए गए हैं:

---

### 1. `ByteArrayOutputStream` का उपयोग करना (सबसे मानक)

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

आपके wrapper constructor में:

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. Apache Commons IO (`IOUtils`) का उपयोग करना

यदि आपके classpath पर पहले से ही **Apache Commons IO** मौजूद है:

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. Guava (`ByteStreams`) का उपयोग करना

यदि आपके पास Guava है:

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### लॉगिंग के लिए अंतिम स्पर्श

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ इसलिए Java 8 में, विकल्प **#1 (ByteArrayOutputStream के साथ)** सबसे पोर्टेबल है।
विकल्प **#2 या #3** साफ़ है यदि आप Commons IO या Guava जोड़ने के लिए तैयार हैं।

---

क्या आप चाहते हैं कि मैं पूरे `CachedBodyHttpServletRequest` कोड को एक **Java 8–तैयार संस्करण** (स्वयं-निहित, बिना `readAllBytes()` के) में refactor करूं?