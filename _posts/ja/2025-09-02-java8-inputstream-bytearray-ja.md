---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Java 8 InputStream からバイト配列へ
translated: true
type: note
---

良い指摘です 👍 — **Java 8** では `InputStream.readAllBytes()` は存在しません（これは Java 9 で追加されました）。
リクエストボディを手動で `byte[]` に読み込む必要があります。

以下によく使われる方法をいくつか示します：

---

### 1. `ByteArrayOutputStream` を使用する方法 (最も標準的)

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

ラッパーのコンストラクタ内では：

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. Apache Commons IO (`IOUtils`) を使用する方法

**Apache Commons IO** がクラスパス上に既にある場合：

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. Guava (`ByteStreams`) を使用する方法

Guava がある場合：

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### ロギング用の最終調整

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ したがって、Java 8 では、オプション **#1 (ByteArrayOutputStream を使用)** が最も移植性に優れています。
Commons IO や Guava を追加しても問題ない場合は、オプション **#2 または #3** の方が簡潔です。

---

`readAllBytes()` を使用せず、**Java 8 対応の自己完結型**に完全な `CachedBodyHttpServletRequest` コードをリファクタリングしましょうか？