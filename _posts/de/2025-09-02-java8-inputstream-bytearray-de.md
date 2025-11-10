---
audio: false
generated: true
image: false
lang: de
layout: post
title: Java 8 InputStream zu Byte-Array
translated: true
type: note
---

Gut erkannt 👍 — in **Java 8** existiert `InputStream.readAllBytes()` nicht (das wurde erst in Java 9 hinzugefügt).
Sie müssen den Request-Body manuell in ein `byte[]` einlesen.

Hier sind einige gängige Methoden:

---

### 1. Verwendung von `ByteArrayOutputStream` (am gebräuchlichsten)

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

In Ihrem Wrapper-Konstruktor:

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. Verwendung von Apache Commons IO (`IOUtils`)

Falls Sie bereits **Apache Commons IO** in Ihrem Classpath haben:

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. Verwendung von Guava (`ByteStreams`)

Falls Sie Guava verwenden:

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### Finaler Feinschliff für das Logging

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ In Java 8 ist also Option **#1 mit ByteArrayOutputStream** die portabelste.
Option **#2 oder #3** ist eleganter, wenn Sie Commons IO oder Guava hinzufügen können.

---

Möchten Sie, dass ich den vollständigen `CachedBodyHttpServletRequest`-Code in eine **Java 8–kompatible Version** umwandele (eigenständig, ohne `readAllBytes()`)?