---
audio: false
generated: true
image: false
lang: es
layout: post
title: Java 8 InputStream a Matriz de Bytes
translated: true
type: note
---

Buen apunte 👍 — en **Java 8** `InputStream.readAllBytes()` no existe (se añadió en Java 9).
Necesitas leer el cuerpo de la solicitud manualmente en un `byte[]`.

Aquí hay algunas formas comunes:

---

### 1. Usando `ByteArrayOutputStream` (más estándar)

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

En tu constructor del wrapper:

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. Usando Apache Commons IO (`IOUtils`)

Si ya tienes **Apache Commons IO** en tu classpath:

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. Usando Guava (`ByteStreams`)

Si tienes Guava:

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### Toque final para logging

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ Así que en Java 8, la opción **#1 con ByteArrayOutputStream** es la más portable.
La opción **#2 o #3** es más limpia si no te importa añadir Commons IO o Guava.

---

¿Quieres que refactorice el código completo de `CachedBodyHttpServletRequest` a una **versión lista para Java 8** (autocontenida, sin `readAllBytes()`)?