---
audio: false
generated: true
lang: ar
layout: post
title: الترقية إلى OpenJDK 21 على نظام macOS
translated: true
type: note
---

نظرًا لأن لديك حاليًا OpenJDK 17 مثبتًا عبر Homebrew على نظام macOS الخاص بك، إليك دليلًا موجزًا لتثبيت OpenJDK 21، وهو أحدث إصدار دعم طويل الأمد (LTS) اعتبارًا من تاريخك الحالي، 1 يوليو 2025. يمكنك تثبيت OpenJDK 21 بجانب OpenJDK 17 والتبديل بينهما حسب الحاجة. الطريقة الأبسط هي استخدام Homebrew، لكنني سأوفر أيضًا خيار التثبيت اليدوي.

### الطريقة 1: تثبيت OpenJDK 21 باستخدام Homebrew (موصى بها)
Homebrew مثبت بالفعل على نظامك، كما هو موضح بإصدار Java الحالي لديك. هذه هي الطريقة الأسهل والأكثر قابلية للصيانة.

1.  **تحديث Homebrew**:
    تأكد من أن Homebrew محدث لاستلام أحدث الحزم:
    ```bash
    brew update
    ```

2.  **تثبيت OpenJDK 21**:
    يوفر Homebrew صيغة محددة لـ OpenJDK 21. قم بتنفيذ الأمر التالي:
    ```bash
    brew install openjdk@21
    ```
    يقوم هذا بتثبيت OpenJDK 21 بطريقة "keg-only"، مما يعني أنه لن يتم إنشاء روابط رمزية له في `/usr/local/bin` لتجنب التعارض مع إصدارات Java الأخرى.

3.  **إضافة OpenJDK 21 إلى المسار (PATH) الخاص بك**:
    لاستخدام OpenJDK 21، تحتاج إلى إضافته إلى PATH الخاص بنظامك. سيوفر Homebrew التعليمات بعد التثبيت، ولكن عادةً، يمكنك ربطه بشكل مؤقت أو دائم:
    - **مؤقت (لجلسة العمل الحالية)**:
      ```bash
      export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
      ```
    - **دائم (أضفه إلى ملف تهيئة Shell)**:
      افتح ملف تهيئة Shell الخاص بك (على الأرجح `~/.zshrc` لأن macOS يستخدم Zsh افتراضيًا):
      ```bash
      nano ~/.zshrc
      ```
      أضف السطر التالي:
      ```bash
      export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
      ```
      احفظ الملف وأغلقه، ثم طبق التغييرات:
      ```bash
      source ~/.zshrc
      ```

4.  **تعيين JAVA_HOME**:
    لضمان أن تطبيقات Java يمكنها تحديد موقع OpenJDK 21، قم بتعيين متغير البيئة `JAVA_HOME`:
    ```bash
    export JAVA_HOME=$(/usr/libexec/java_home -v 21)
    ```
    أضف هذا إلى ملف `~/.zshrc` لديمومة الإعداد:
    ```bash
    echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
    source ~/.zshrc
    ```

5.  **التحقق من التثبيت**:
    تحقق من تثبيت OpenJDK 21 وتفعيله:
    ```bash
    java -version
    ```
    يجب أن ترى ناتجًا مشابهًا لما يلي:
    ```
    openjdk 21.0.1 2023-10-17
    OpenJDK Runtime Environment (build 21.0.1+12)
    OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
    ```

6.  **التبديل بين إصدارات Java**:
    نظرًا لأن لديك OpenJDK 17 مثبتًا، يمكنك التبديل بين الإصدارات باستخدام `/usr/libexec/java_home`. على سبيل المثال:
    - لاستخدام OpenJDK 17:
      ```bash
      export JAVA_HOME=$(/usr/libexec/java_home -v 17)
      ```
    - لاستخدام OpenJDK 21:
      ```bash
      export JAVA_HOME=$(/usr/libexec/java_home -v 21)
      ```
    بدلاً من ذلك، فكر في استخدام أداة إدارة الإصدارات مثل `jenv` (قم بتثبيتها عبر `brew install jenv`) لتبديل أسهل:
    ```bash
    jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
    jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
    jenv enable-plugin export
    jenv global 21
    ```

### الطريقة 2: التثبيت اليدوي
إذا كنت تفضل عدم استخدام Homebrew، يمكنك تثبيت OpenJDK 21 يدويًا.

1.  **تحميل OpenJDK 21**:
    - قم بزيارة موقع OpenJDK الرسمي (jdk.java.net/21) أو موفر موثوق مثل Oracle أو Azul أو Adoptium.
    - لأجهزة Apple Silicon (M1/M2)، قم بتحميل ملف `macOS/AArch64` tar.gz. لأجهزة Mac المبنية على معالجات Intel، اختر `macOS/x64`.
    - مثال: من صفحة تحميل Oracle's JDK 21، اختر ملف ARM64 أو x64 tar.gz.

2.  **التحقق من التحميل**:
    تحقق من سلامة الملف الذي تم تحميله باستخدام checksum الخاص به SHA256:
    ```bash
    shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
    ```
    قارن الناتج مع checksum المقدم على صفحة التحميل.

3.  **استخراج الملف**:
    استخرج ملف tar.gz إلى الدليل المطلوب، مثل دليل المنزل الخاص بك:
    ```bash
    tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
    ```
    سيتم استخراج JDK إلى `~/OpenJDK/jdk-21.0.1.jdk/Contents/Home`.

4.  **نقل إلى دليل النظام** (اختياري):
    للاتساق، يمكنك نقل JDK إلى دليل Java القياسي في macOS:
    ```bash
    sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
    ```

5.  **تعيين JAVA_HOME و PATH**:
    قم بتحديث ملف `~/.zshrc` ليشمل:
    ```bash
    export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
    export PATH=$JAVA_HOME/bin:$PATH
    ```
    طبق التغييرات:
    ```bash
    source ~/.zshrc
    ```

6.  **التحقق من التثبيت**:
    تأكد من التثبيت:
    ```bash
    java -version
    ```
    تأكد من أنه يعرض OpenJDK 21.

### ملاحظات
- **التوافق مع Apple Silicon**: تأكد من تحميل إصدار AArch64 لأجهزة M1/M2 Mac لتجنب مشاكل الأداء. يختار Homeboost Architecture المناسب تلقائيًا.
- **إصدارات JDK متعددة**: يدعم macOS إصدارات JDK متعددة في `/Library/Java/JavaVirtualMachines/`. استخدم `/usr/libexec/java_home -v <version>` للتبديل بينها.
- **ميزة Homebrew**: يبسط Homebrew عملية التحديثات (`brew upgrade openjdk@21`) ويضمن التوافق مع نظامك.
- **موفرو بديلون**: يمكنك أيضًا استخدام إصدارات Azul Zulu أو Eclipse Temurin من OpenJDK 21، المتاحة من مواقعهم الإلكترونية على التوالي (مثل azul.com أو adoptium.net).

إذا واجهت أي مشاكل، أعلمني، وسأساعد في حلها.