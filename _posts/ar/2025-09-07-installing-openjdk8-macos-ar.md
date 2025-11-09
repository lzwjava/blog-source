---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ar
layout: post
title: تثبيت OpenJDK 8 على نظام macOS
translated: true
type: note
---

إليك كيفية تثبيت **OpenJDK 8** (Java SE 8) على نظام macOS في **2025**، مع طرق تغطي Homebrew وSDKMAN والمثبتات اليدوية وMacPorts. لا توجد جداول—فقط تدفقات واضحة وسهلة:

---

## 1. استخدام Homebrew (`openjdk@8`)

لا تزال هذه واحدة من أسهل الطرق لتثبيت OpenJDK 8 على macOS.

### الخطوات:

1. افتح Terminal.

2. شغِّل:

   ```bash
   brew install openjdk@8
   ```

   ([Homebrew Formulae][1])

3. بعد التثبيت، قم بربط JDK حتى تتمكن أدوات macOS من اكتشافه:

   ```bash
   sudo ln -sfn $(brew --prefix)/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-8.jdk
   ```

   ([Homebrew Formulae][1])

4. اختياريًا، أضف OpenJDK 8 إلى مسار PATH في ملف إعدادات shell الخاص بك (مثل `.zshrc`):

   ```bash
   export PATH="$(brew --prefix openjdk@8)/bin:$PATH"
   ```

**ملاحظة لمستخدمي Apple Silicon (سلسلة M):**
إذا واجهت مشاكل في البنية، قد تحتاج إلى تشغيل Homebrew تحت Rosetta 2:

```bash
env /usr/bin/arch -x86_64 /bin/zsh --login
brew install openjdk@8
```

ثم تابع مع إعداد الرابط الرمزي ومسار PATH ([Stack Overflow][2]).

---

## 2. عبر SDKMAN (مدير إصدارات Java)

SDKMAN هو أداة مرنة لتثبيت والتبديل بين إصدارات Java متعددة.

### تثبيت سريع:

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk list java
sdk install java 8.xxx-tem
```

استبدل `8.xxx-tem` بالمعرف الظاهر في `sdk list java`. ([Stack Overflow][2])

---

## 3. التثبيت اليدوي (Oracle / Adoptium / AdoptOpenJDK)

### الخيار أ: مثبت .dmg / .pkg من Oracle

1. حمِّل المثبت الصحيح لبنية نظامك من صفحة تحميل Java SE 8 من Oracle.
2. افتح ملف `.dmg`، وشغِّل مثبت `.pkg`، واتبع التعليمات. ([Oracle Documentation][3])
3. بعد التثبيت، استخدم أدوات مثل `java_home` لاختيار الإصدار:

   ```bash
   /usr/libexec/java_home -v 1.8 --exec java -version
   ```

### الخيار ب: AdoptOpenJDK أو إصدارات مشابهة

توفر AdoptOpenJDK (الآن تحت Eclipse Adoptium) إصدارات—مع خيارات كل من المثبت والأرشيف.

* على سبيل المثال، تشير وثائق Salesforce في أغسطس 2025 إلى استخدام موقع AdoptOpenJDK، واختيار OpenJDK 8 (LTS) مع HotSpot JVM، والمتابعة عبر مثبته. ([Salesforce][4])

بعد التثبيت، اضبط متغير JAVA\_HOME الخاص بك، مثال:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 1.8)
export PATH=$JAVA_HOME/bin:$PATH
```

---

## 4. MacPorts

إذا كنت تستخدم MacPorts بدلاً من Homebrew، فإن تثبيت OpenJDK 8 هو عملية مباشرة:

```bash
sudo port install openjdk8
```

لرؤية المحتويات المثبتة:

```bash
port contents openjdk8
```

للتحديث لاحقًا:

```bash
sudo port selfupdate && sudo port upgrade openjdk8
```

([MacPorts][5])

---

## اختيار الطريقة المناسبة لك

| الهدف                                              | أفضل طريقة                                      |
| -------------------------------------------------- | ----------------------------------------------- |
| تثبيت سريع وصيانة سهلة                             | **Homebrew (`brew install openjdk@8`)**         |
| إدارة إصدارات Java متعددة متزامنة                  | **SDKMAN**                                      |
| تحكم كامل ومثبت رسمي (ملائم لواجهة المستخدم الرسومية) | **المثبت اليدوي `.dmg` أو `.pkg`** عبر Oracle/Adoptium |
| تفضيل نظام MacPorts                                | **MacPorts**                                    |

---

## التحقق من التثبيت

بعد التثبيت، تحقق منه باستخدام:

```bash
java -version
```

توقع شيئًا مثل `"1.8.0_xxx"` لتأكيد أن Java 8 نشط. للتحكم الدقيق:

```bash
/usr/libexec/java_home -v 1.8 --exec javac -version
```

---

## الأفكار الختامية

خلاصة القول:

* **Homebrew** هو الخيار الأكثر شيوعًا في 2025—فقط `brew install openjdk@8`، ثم رابط وضبط مسار PATH.
* **SDKMAN** يمنحك المرونة إذا كنت تقوم بتبديل إصدارات Java بشكل متكرر.
* **المثبتات اليدوية** (Oracle, Adoptium) تظل خيارًا احتياطيًا قويًا يعتمد على واجهة المستخدم الرسومية.
* **MacPorts** يعمل إذا كان هذا هو مدير الحزم المفضل لديك.

دعني أعلم إذا كنت تريد المساعدة في الإعداد في shell الخاص بك، أو التبديل بين إصدارات Java، أو أي شيء آخر على طول الطريق!

[1]: https://formulae.brew.sh/formula/openjdk%408?utm_source=chatgpt.com "openjdk@8"
[2]: https://stackoverflow.com/questions/24342886/how-to-install-java-8-on-mac?utm_source=chatgpt.com "How to install Java 8 on Mac"
[3]: https://docs.oracle.com/javase/8/docs/technotes/guides/install/mac_jdk.html?utm_source=chatgpt.com "JDK 8 Installation for macOS"
[4]: https://help.salesforce.com/s/articleView?id=001117155&language=en_US&type=1&utm_source=chatgpt.com "How to Install OpenJDK 8 on macOS to Work with Anypoint ..."
[5]: https://ports.macports.org/port/openjdk8/?utm_source=chatgpt.com "Install openjdk8 on macOS with MacPorts"