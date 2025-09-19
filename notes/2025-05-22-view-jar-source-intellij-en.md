---
title: View JAR Source in IntelliJ IDEA
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

In IntelliJ IDEA, you can easily view the source code of a JAR file. There are a few approaches depending on whether the JAR contains source files or just compiled `.class` files:

---

### 1. Open the JAR in IDEA

* Go to **File > Open…**
* Select the JAR file.
* IDEA will open it in the **Project view** like a regular archive.
* If the JAR contains `.java` source files, you can browse them directly.
* If it contains only `.class` files, IDEA will decompile them automatically into readable Java code.

---

### 2. Attach Sources to a Library JAR

If the JAR is part of a library (like Maven or Gradle dependencies):

* Go to **File > Project Structure > Libraries** (or **Modules > Dependencies** if it’s module-specific).
* Select the JAR.
* Click **Attach Sources…** and point IDEA to the `-sources.jar` (if available).
* Now IDEA will show the real source instead of just decompiled bytecode.

---

### 3. Quick Navigation

* Hold **Ctrl (Cmd on macOS)** and click a class or method that comes from the JAR.
* If no sources are attached, IDEA shows the decompiled version.
* If sources are attached, you’ll see the original Java code.

---

### 4. External Decompiler Plugins (Optional)

IDEA already has a built-in decompiler, but you can install plugins like **Fernflower** or **CFR** if you want alternative decompilation.

---

👉 Usually, if it’s a dependency managed by Maven/Gradle, IDEA can automatically download and attach the `-sources.jar` from the repository. If it’s a standalone JAR, you’ll need to attach sources manually or rely on the decompiler.

Do you want me to also explain **how to extract the JAR’s source code outside IDEA** (using tools like `jd-gui` or `jar xf`), or do you mainly want to stick to working inside IDEA?