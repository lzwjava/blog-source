---
audio: false
generated: true
lang: ar
layout: post
title: إعدادات الوكيل لـ Maven
translated: true
type: note
---

بناءً على نتيجة أمر `checkproxy` الخاص بك، فإن وكيلي HTTP وHTTPS كلاهما مضبوطان على `http://127.0.0.1:7890`. أدناه snippet تكوين Maven `settings.xml` المحدث لتكوين Maven لاستخدام إعدادات الوكيل هذه.

### snippet تكوين الوكيل المحدث `settings.xml`

أضف أو حدّث قسم `<proxies>` في ملف Maven `settings.xml` الخاص بك (الموجود في `~/.m2/settings.xml` أو `/usr/share/maven/conf/settings.xml`) بما يلي:

```xml
<settings>
  <proxies>
    <proxy>
      <id>http-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>https-proxy</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>127.0.0.1</host>
      <port>7890</port>
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

### شرح الـ snippet
- **`<id>`**: معرفات فريدة (`http-proxy` و `https-proxy`) لكل تكوين وكيل.
- **`<active>true</active>`**: يُفعّل الوكيل.
- **`<protocol>`**: مضبوط على `http` لوكيل HTTP و `https` لوكيل HTTPS، بما يتطابق مع نتيجة `checkproxy` الخاصة بك.
- **`<host>127.0.0.1</host>`**: عنوان IP لخادم الوكيل، كما هو موضح في إعدادات الوكيل الخاصة بك.
- **`<port>7890</port>`**: رقم المنفذ لكلا الوكيلين، كما هو محدد.
- **`<nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>`**: يستثني `localhost` و `127.0.0.1` من التوجيه عبر الوكيل، وهو إجراء قياسي لتجنب المشاكل مع الخدمات المحلية.
- **لا يوجد `<username>` أو `<password>`**: بما أن نتيجة الوكيل الخاصة بك لا تشير إلى المصادقة، فقد حُذفت هذه الحقول. إذا كانت المصادقة مطلوبة، أضفها باستخدام بيانات الاعتماد الخاصة بك.

### خطوات التطبيق
1. **افتح `settings.xml`**:
   - إذا كان `~/.m2/settings.xml` موجودًا، قم بتحريره (مثل `nano ~/.m2/settings.xml`).
   - إذا لم يكن موجودًا، فأنشئه أو حرر الملف العام في `/usr/share/maven/conf/settings.xml` (يتطلب `sudo`).

2. **أدخل أو حدّث قسم `<proxies>`**:
   - إذا كان `<proxies>` موجودًا بالفعل، استبدل أو ادمج إدخالات `<proxy>` مع الـ snippet أعلاه.
   - إذا كان `<settings>` فارغًا أو بسيطًا، يمكنك استخدام الـ snippet بأكمله كمحتوى للملف.

3. **احفظ الملف وأغلقه**.

### التحقق من التكوين
شغّل أمر Maven الذي يتطلب الوصول إلى الإنترنت لتأكيد استخدام الوكيل:
```bash
cd ~/Projects/blog-server
mvn -X clean checkstyle:check
```

في ناتج التصحيح (`-X`)، ابحث عن الأسطر التي تشير إلى أن Maven يستخدم الوكيل (مثل اتصالات بـ `127.0.0.1:7890`). إذا قام الأمر بتنزيل التبعيات أو اكتمل دون أخطاء في الشبكة، فإن الوكيل يعمل.

### استكشاف الأخطاء وإصلاحها
- **الوكيل لا يعمل**:
  - تأكد من أن خادم الوكيل على `127.0.0.1:7890` قيد التشغيل (مثل اختباره بـ `curl -x http://127.0.0.1:7890 https://repo.maven.apache.org`).
  - تحقق من الأخطاء المطبعية في ملف `settings.xml`.
- **تم تجاهل ملف الإعدادات**:
  - تأكد من أن Maven يقرأ `~/.m2/settings.xml` عن طريق التحقق من مسار الملف في ناتج التصحيح.
  - إذا كنت تستخدم الملف العام، فتأكد من أنك قمت بتحرير `/usr/share/maven/conf/settings.xml` بشكل صحيح.
- **المصادقة مطلوبة**:
  - إذا كان الوكيل الخاص بك يتطلب اسم مستخدم وكلمة مرور، أضف:
    ```xml
    <username>yourusername</username>
    <password>yourpassword</password>
    ```
    إلى كل كتلة `<proxy>`.

### ملاحظة على السياق السابق
يجب حل مشكلتك `checkstyle:check` في مشروع `blog-server` (المتعلقة بـ `checks.xml` و `SuppressWithNearbyTextFilter`) بشكل منفصل عن طريق تحديث `pom.xml` كما تم اقتراحه سابقًا (باستخدام `maven-checkstyle-plugin:3.3.1` مع Checkstyle `10.17.0` و `<configLocation>${project.basedir}/checks.xml</configLocation>`). ستضمن إعدادات الوكيل أعلاه أن Maven يمكنه تنزيل أي قطع أثرية مطلوبة لهذا الإصلاح.

أعلمني إذا واجهت مشاكل أو إذا كنت بحاجة إلى مساعدة في `pom.xml` المحدث أو مزيد من تصحيح أخطاء الوكيل!