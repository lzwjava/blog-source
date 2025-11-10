---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Java 8 InputStream vers Tableau d'Octets
translated: true
type: note
---

Bien vu 👍 — dans **Java 8** `InputStream.readAllBytes()` n'existe pas (cette méthode a été ajoutée dans Java 9).
Vous devez lire manuellement le corps de la requête dans un `byte[]`.

Voici quelques méthodes courantes :

---

### 1. Utilisation de `ByteArrayOutputStream` (plus standard)

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

Dans votre constructeur de wrapper :

```java
public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = toByteArray(request.getInputStream());
}
```

---

### 2. Utilisation d'Apache Commons IO (`IOUtils`)

Si vous avez déjà **Apache Commons IO** dans votre classpath :

```java
import org.apache.commons.io.IOUtils;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = IOUtils.toByteArray(request.getInputStream());
}
```

---

### 3. Utilisation de Guava (`ByteStreams`)

Si vous avez Guava :

```java
import com.google.common.io.ByteStreams;

public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
    super(request);
    this.cachedBody = ByteStreams.toByteArray(request.getInputStream());
}
```

---

### Dernière touche pour le logging

```java
public String getBody() {
    return new String(this.cachedBody, StandardCharsets.UTF_8);
}
```

---

✅ Donc en Java 8, l'option **#1 avec ByteArrayOutputStream** est la plus portable.
L'option **#2 ou #3** est plus propre si vous acceptez d'ajouter Commons IO ou Guava.

---

Voulez-vous que je refactorise le code complet de `CachedBodyHttpServletRequest` en une **version compatible Java 8** (autonome, sans `readAllBytes()`) ?