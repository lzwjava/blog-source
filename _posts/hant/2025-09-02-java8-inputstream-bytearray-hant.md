---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Java 8 輸入流轉換為位元組陣列
translated: true
type: note
---

好發現 👍 — 在 **Java 8** 中 `InputStream.readAllBytes()` 並不存在（該方法是 Java 9 才加入的）。
你需要手動將請求主體讀取到 `byte[]` 中。

以下是幾種常見方法：

---

### 1. 使用 `ByteArrayOutputStream`（最標準）

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

在你的包裝構造函數中：

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. 使用 Apache Commons IO (`IOUtils`)

如果你的 classpath 中已有 **Apache Commons IO**：

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. 使用 Guava (`ByteStreams`)

如果你有 Guava：

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### 用於記錄的最後調整

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ 因此在 Java 8 中，選項 **#1 使用 ByteArrayOutputStream** 是最便攜的。
如果你不介意加入 Commons IO 或 Guava，選項 **#2 或 #3** 會更簡潔。

---

需要我將完整的 `CachedBodyHttpServletRequest` 代碼重構為 **Java 8 適用版本**（自包含，不使用 `readAllBytes()`）嗎？