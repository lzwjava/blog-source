---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: تمكين تصحيح أخطاء بروتوكول أمان النقل لـ Java
translated: true
type: note
---

### تمكين تصحيح SSL/TLS في Java

لتمكين التسجيل التفصيلي للأنشطة المتعلقة بـ SSL/TLS في Java (مثل المصافحات، والتحقق من الشهادات، وتبادل المفاتيح)، تستخدم خاصية نظام JVM `-Djavax.net.debug`. هذا يخرج معلومات التصحيح إلى وحدة التحكم (stdout/stderr) عند تشغيل تطبيق Java الخاص بك.

#### التعليمات خطوة بخطوة

1. **اختر مستوى التصحيح**:
   - استخدم `ssl` للحصول على تفاصيل مصافحة SSL/TLS الأساسية.
   - استخدم `ssl:handshake` للحصول على رسائل مصافحة مطولة (بما في ذلك مجموعات التشفير والشهادات).
   - استخدم `all` للتصحيح الشامل (يتضمن SSL بالإضافة إلى بروتوكولات الشبكة الأخرى - استخدمه باعتدال لأنه مطول جدًا).
   - التوصية الشائعة: ابدأ بـ `ssl:handshake:verbose,keymanager:trustmanager` للحصول على رؤى موجهة لـ SSL.

2. **عيّن الخاصية عند تشغيل تطبيق Java الخاص بك**:
   - **التنفيذ عبر سطر الأوامر** (على سبيل المثال، عبر أمر `java`):
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar
     ```
     استبدل `your-app.jar` بتطبيقك الفعلي أو الفئة (مثل `com.example.Main`).

   - **في بيئة التطوير المتكاملة (IDE) (مثل IntelliJ IDEA، Eclipse)**:
     - انتقل إلى Run/Debug Configurations.
     - أضف `-Djavax.net.debug=ssl:handshake` إلى حقل **VM options**.
     - شغّل التكوين أو صححه.

   - **في أداة بناء (مثل Maven أو Gradle)**:
     - **Maven** (في `pom.xml` تحت `<build><plugins><plugin>` لـ surefire):
       ```xml
       <configuration>
         <argLine>-Djavax.net.debug=ssl:handshake</argLine>
       </configuration>
       ```
     - **Gradle** (في `build.gradle`):
       ```groovy
       test {
         jvmArgs '-Djavax.net.debug=ssl:handshake'
       }
       ```

3. **التقاط السجلات**:
   - يظهر الناتج في وحدة التحكم/الطرفية الخاصة بك.
   - إعادة التوجيه إلى ملف لسهولة المراجعة:
     ```
     java -Djavax.net.debug=ssl:handshake -jar your-app.jar > ssl-debug.log 2>&1
     ```
   - ابحث عن الأسطر التي تبدأ بـ `***` (مثل `*** ClientHello` لبدء المصافحة) أو البادئات `javax.net.ssl`.

4. **تعطيله**:
   - ما عليك سوى إ移除 علم `-D` عند الانتهاء - فهو غير مضبوط افتراضيًا لتجنب عبء الأداء.

#### مقتطف مثال للناتج
عند التمكين، سترى شيئًا مثل:
```
*** ServerHello, TLSv1.2
RandomCookie:  GMT: 1731000000 bytes = { ... }
Cipher Suite: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
Compression Method: 0
***
```

#### نصائح
- هذا يعمل مع Java 8+ (بما في ذلك 11، 17، 21). في الإصدارات الأحدث، يمكنك أيضًا تمكين `-Djdk.tls.client.protocols=TLSv1.2,TLSv1.3` للحصول على سجلات محددة للبروتوكول.
- الإسهاب الشديد يمكن أن يبطئ تطبيقك ويفيض السجلات - اختبر في بيئة تطوير.
- إذا كنت تستخدم إطار عمل مثل Spring Boot، أضفه إلى `application.properties`: `debug=true` (للعام) أو عبر وسائط سطر الأوامر.

لمزيد من التفاصيل، انظر وثائق Oracle الرسمية: [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html#jsse-cipher-suite-names).