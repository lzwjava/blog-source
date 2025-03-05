---
audio: false
generated: true
lang: ar
layout: post
title: ميزات الأمان في جافا
translated: true
---

الباقة `java.security` في جاڤا تقدم الفئات والمواضع لتنفيذ ميزات الأمان في تطبيقاتك. وهي جزء من المكتبة القياسية لجاڤا وتشمل أدوات لعملية التشفير، إدارة المفتاح، توليد أرقام عشوائية آمنة، التوقيعات الرقمية، و التحكم في الوصول. نظرًا لكون الباقة واسعة، ستقدم لك هذه الإجابة نظرة عامة على غرضها وتوضيح كيفية استخدامها مع مثال عملي.

### ما يستخدم `java.security`؟
الباقة `java.security` هي مكون أساسي من بنية التشفير في جاڤا (JCA). وتقدم مجموعة متنوعة من الوظائف المتعلقة بالأمان، مثل:
- **عمليات التشفير**: هاش البيانات (على سبيل المثال، باستخدام `MessageDigest`), التوقيع على البيانات (على سبيل المثال، باستخدام `Signature`).
- **إدارة المفتاح**: توليد المفتاح (على سبيل المثال، `KeyPairGenerator`, `KeyGenerator`) وإدارة الشهادات (على سبيل المثال، `KeyStore`).
- **أرقام عشوائية آمنة**: توليد أرقام عشوائية قوية من الناحية التشفيرية (على سبيل المثال، `SecureRandom`).
- **التحكم في الوصول**: تعريف وإجبار على سياسات الأمان (على سبيل المثال، `Permission`, `AccessController`).

لاستخدام `java.security`, عادة ما تجلب الفئات المحددة التي تحتاجها وتستفيد من واجهاتها البرمجية لتنفيذ هذه المهام الأمنية.

### كيفية استخدام `java.security`: مثال خطوة بخطوة
دعنا نمر عبر حالة استخدام شائعة: حساب هاش SHA-256 لسلسلة باستخدام فئة `MessageDigest` من `java.security`. سيوضح لك هذا المثال كيفية تطبيق الباقة في الممارسة.

#### مثال: حساب هاش SHA-256
هنا هو كود كامل يحوّل السلسلة "Hello, World!" إلى هاش باستخدام SHA-256 ويظهر النتيجة كسلسلة سداسية عشرية:

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.nio.charset.StandardCharsets;

public class HashExample {
    public static void main(String[] args) {
        try {
            // الخطوة 1: الحصول على مثيل من MessageDigest لـ SHA-256
            MessageDigest digest = MessageDigest.getInstance("SHA-256");

            // الخطوة 2: حساب هاش المدخل
            byte[] hashBytes = digest.digest("Hello, World!".getBytes(StandardCharsets.UTF_8));

            // الخطوة 3: تحويل المصفوفة الثنائية إلى سلسلة سداسية عشرية
            String hash = bytesToHex(hashBytes);

            // الخطوة 4: طباعة النتيجة
            System.out.println("SHA-256 Hash: " + hash);
        } catch (NoSuchAlgorithmException e) {
            System.err.println("SHA-256 algorithm not available.");
        }
    }

    // طريقة مساعدة لتحويل المصفوفة الثنائية إلى سلسلة سداسية عشرية
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
```

#### شرح الكود
1. **تعليمات الاستيراد**:
   - `java.security.MessageDigest`: تقدم الوظيفة الحاشية.
   - `java.security.NoSuchAlgorithmException`: استثناء يرمي إذا كان الخوارزمية المطلوبة (على سبيل المثال، "SHA-256") غير متاحة.
   - `java.nio.charset.StandardCharsets`: يضمن التشفير الحروفي المتسق (UTF-8) عند تحويل السلسلة إلى ثنائية.

2. **إنشاء مثيل من MessageDigest**:
   - `MessageDigest.getInstance("SHA-256")` يخلق مثيل `MessageDigest` مهيأ لاستخدام خوارزمية SHA-256.

3. **حشو البيانات**:
   - طريقة `digest` تأخذ مصفوفة ثنائية (تم تحويلها من السلسلة باستخدام `getBytes(StandardCharsets.UTF_8)`) وتحسب الهاش، وتعيدها كمصفوفة ثنائية.

4. **التحويل إلى سداسية عشرية**:
   - طريقة المساعدة `bytesToHex` تحول المصفوفة الثنائية إلى سلسلة سداسية عشرية قابلة للقراءة.

5. **إدارة الاستثناءات**:
   - الكود محاط في كتلة `try-catch` لإدارة `NoSuchAlgorithmException`، والتي قد تحدث إذا لم يدعم SHA-256 من قبل Java Runtime (على الرغم من أن هذا نادر مع الخوارزميات القياسية).

عندما تنفذ هذا الكود، فإنه يخرج شيئًا مثل:
```
SHA-256 Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```
هذا الهاش هو بصمة فريدة لـ "Hello, World!" تم إنشاؤها بواسطة SHA-256.

### الخطوات العامة لاستخدام `java.security`
على الرغم من أن المثال أعلاه يركز على `MessageDigest`, يتبع استخدام الفئات الأخرى في `java.security` نمطًا مشابهًا:
1. **استيراد الفئة**: استيراد الفئة المحددة التي تحتاجها (على سبيل المثال، `java.security.KeyPairGenerator`, `java.security.SecureRandom`).
2. **إنشاء الخدمة**: استخدام طريقة مصنع مثل `getInstance` لإنشاء مثيل (على سبيل المثال، `KeyPairGenerator.getInstance("RSA")`).
3. **التكوين والاستخدام**: إعداد الكائن كما هو مطلوب (على سبيل المثال، التهيئة مع حجم المفتاح) ودعوة طرقه (على سبيل المثال، `generateKeyPair()`).
4. **إدارة الاستثناءات**: محاط العمليات الأمنية في كتلة `try-catch` لإدارة الاستثناءات مثل `NoSuchAlgorithmException` أو `InvalidKeyException`.
5. **تأمين البيانات الحساسة**: تأكد من معالجة البيانات الحساسة (على سبيل المثال، المفتاح، كلمة المرور) بعناية، مثل مسحها من الذاكرة بعد الاستخدام.

### فئات شائعة أخرى في `java.security`
هنا بعض الفئات الأخرى المفيدة واستخداماتها:
- **`SecureRandom`**: توليد أرقام عشوائية آمنة من الناحية التشفيرية.
  - مثال: `SecureRandom random = new SecureRandom(); byte[] bytes = new byte[16]; random.nextBytes(bytes);`
- **`KeyPairGenerator`**: توليد أزواج المفتاح العام/الخاص للتشفير غير المتكافئ (على سبيل المثال، RSA).
  - مثال: `KeyPairGenerator gen = KeyPairGenerator.getInstance("RSA"); gen.initialize(2048); KeyPair pair = gen.generateKeyPair();`
- **`KeyStore`**: إدارة مخزن لتخزين المفتاحات والتشفيرات.
  - مثال: `KeyStore ks = KeyStore.getInstance("JKS"); ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());`
- **`Signature`**: إنشاء وتحقق التوقيعات الرقمية.
  - مثال: `Signature sig = Signature.getInstance("SHA256withRSA"); sig.initSign(privateKey); sig.update(data); byte[] signature = sig.sign();`

### ملاحظات رئيسية
- **التوفر**: الباقة `java.security` هي جزء من المكتبة القياسية لجاڤا (جزء من وحدة `java.base` منذ جاڤا 9)، فلا تحتاج إلى اعتماد خارجي.
- **أفضل الممارسات الأمنية**: استخدم دائمًا خوارزميات آمنة (على سبيل المثال، SHA-256 بدلاً من MD5)، واسع إلى الاستثناءات دون كشف معلومات حساسة، واسح البيانات الحساسة من الذاكرة عند الانتهاء.
- **التوسع**: لخصائص متقدمة، قد تدمج `java.security` مع `javax.crypto` (على سبيل المثال، للتشفير/الفسخ) أو مكتبات ثالثة مثل Bouncy Castle.

يجب أن يوفر لك هذا التوضيح والمثال بداية قوية لاستخدام `java.security` في مشاريعك بجاڤا!