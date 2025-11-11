---
audio: false
generated: true
lang: ar
layout: post
title: ميزات الأمان في جافا
translated: true
type: note
---

توفّر حزمة `java.security` في جافا أصنافًا وواجهات لتنفيذ ميزات الأمان في تطبيقاتك. وهي جزء من المكتبة القياسية لجافا وتشمل أدوات لعمليات التشفير، وإدارة المفاتيح، وتوليد أرقام عشوائية آمنة، والتوقيعات الرقمية، والتحكم في الوصول. نظرًا لأن الحزمة واسعة النطاق، سيعطيك هذا الجواب نظرة عامة على هدفها وسيوضح كيفية استخدامها بمثال عملي.

### ما هو استخدام `java.security`؟
تعد حزمة `java.security` مكونًا أساسيًا من Java Cryptography Architecture (JCA). فهي تقدم مجموعة متنوعة من الوظائف المتعلقة بالأمان، مثل:
- **عمليات التشفير**: تجزئة البيانات (على سبيل المثال، باستخدام `MessageDigest`)، وتوقيع البيانات (على سبيل المثال، باستخدام `Signature`).
- **إدارة المفاتيح**: توليد المفاتيح (على سبيل المثال، `KeyPairGenerator`، `KeyGenerator`) وإدارة الشهادات (على سبيل المثال، `KeyStore`).
- **أرقام عشوائية آمنة**: توليد أرقام عشوائية قوية من الناحية التشفيرية (على سبيل المثال، `SecureRandom`).
- **التحكم في الوصول**: تحديد وتطبيق سياسات الأمان (على سبيل المثال، `Permission`، `AccessController`).

لاستخدام `java.security`، تقوم عادةً باستيراد الأصناف المحددة التي تحتاجها والاستفادة من واجهات برمجة التطبيقات (APIs) الخاصة بها لأداء مهام الأمان هذه.

### كيفية استخدام `java.security`: مثال خطوة بخطوة
لنستعرض حالة استخدام شائعة: حساب تجزئة SHA-256 لسلسلة نصية باستخدام صنف `MessageDigest` من `java.security`. سيظهر لك هذا مثالاً عمليًا على كيفية تطبيق الحزمة.

#### مثال: حساب تجزئة SHA-256
إليك مقتطف كود كامل يقوم بتجزئة السلسلة "Hello, World!" باستخدام SHA-256 وعرض النتيجة كسلسلة نصية سداسية عشرية:

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.nio.charset.StandardCharsets;

public class HashExample {
    public static void main(String[] args) {
        try {
            // الخطوة 1: الحصول على نسخة من MessageDigest لـ SHA-256
            MessageDigest digest = MessageDigest.getInstance("SHA-256");

            // الخطوة 2: حساب تجزئة السلسلة المدخلة
            byte[] hashBytes = digest.digest("Hello, World!".getBytes(StandardCharsets.UTF_8));

            // الخطوة 3: تحويل مصفوفة البايتات إلى سلسلة سداسية عشرية
            String hash = bytesToHex(hashBytes);

            // الخطوة 4: طباعة النتيجة
            System.out.println("SHA-256 Hash: " + hash);
        } catch (NoSuchAlgorithmException e) {
            System.err.println("SHA-256 algorithm not available.");
        }
    }

    // دالة مساعدة لتحويل مصفوفة البايتات إلى سلسلة سداسية عشرية
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
1. **جمل الاستيراد**:
   - `java.security.MessageDigest`: يوفر وظيفة التجزئة.
   - `java.security.NoSuchAlgorithmException`: استثناء يُرمى إذا كانت الخوارزمية المطلوبة (مثل "SHA-256") غير متوفرة.
   - `java.nio.charset.StandardCharsets`: يضمن ترميز أحرف متسق (UTF-8) عند تحويل السلسلة إلى بايتات.

2. **إنشاء نسخة من MessageDigest**:
   - `MessageDigest.getInstance("SHA-256")` ينشئ كائن `MessageDigest` مهيأ لاستخدام خوارزمية SHA-256.

3. **تجزئة البيانات**:
   - تأخذ الدالة `digest` مصفوفة بايتات (تم تحويلها من السلسلة باستخدام `getBytes(StandardCharsets.UTF_8)`) وتحسب التجزئة، مع إرجاعها كمصفوفة بايتات.

4. **التحويل إلى السداسي عشر**:
   - تقوم الدالة المساعدة `bytesToHex` بتحويل مصفوفة البايتات الخام إلى سلسلة نصية سداسية عشرية قابلة للقراءة.

5. **معالجة الاستثناءات**:
   - تم تغليف الكود داخل كتلة `try-catch` لمعالجة `NoSuchAlgorithmException`، والذي قد يحدث إذا لم تكن SHA-256 مدعومة في وقت تشغيل جافا (رغم أن هذا نادر مع الخوارزميات القياسية).

عند تشغيل هذا الكود، يخرج بناتج مشابه لما يلي:
```
SHA-256 Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```
هذه التجزئة هي بصمة فريدة لـ "Hello, World!" تم إنشاؤها بواسطة SHA-256.

### الخطوات العامة لاستخدام `java.security`
بينما يركز المثال أعلاه على `MessageDigest`، فإن النهج المتبع لاستخدام الأصناف الأخرى في `java.security` يتبع نمطًا مشابهًا:
1. **استيراد الصنف**: قم باستيراد الصنف المحدد الذي تحتاجه (مثل `java.security.KeyPairGenerator`، `java.security.SecureRandom`).
2. **إنشاء الخدمة**: استخدم دالة مصنع مثل `getInstance` لإنشاء نسخة (مثل `KeyPairGenerator.getInstance("RSA")`).
3. **التكوين والاستخدام**: قم بإعداد الكائن حسب الحاجة (مثل التهيئة بحجم مفتاح) واستدعِ دواله (مثل `generateKeyPair()`).
4. **معالجة الاستثناءات**: قم بتغليف عمليات الأمان في كتل `try-catch` لإدارة استثناءات مثل `NoSuchAlgorithmException` أو `InvalidKeyException`.
5. **تأمين البيانات الحساسة**: تأكد من التعامل مع البيانات الحساسة (مثل المفاتيح، وكلمات المرور) بعناية، مثل مسحها من الذاكرة بعد الاستخدام.

### أصناف شائعة أخرى في `java.security`
إليك بعض الأصناف المفيدة الأخرى واستخداماتها النموذجية:
- **`SecureRandom`**: يولد أرقامًا عشوائية آمنة من الناحية التشفيرية.
  - مثال: `SecureRandom random = new SecureRandom(); byte[] bytes = new byte[16]; random.nextBytes(bytes);`
- **`KeyPairGenerator`**: يولد أزواج مفاتيح عامة/خاصة للتشفير غير المتماثل (مثل RSA).
  - مثال: `KeyPairGenerator gen = KeyPairGenerator.getInstance("RSA"); gen.initialize(2048); KeyPair pair = gen.generateKeyPair();`
- **`KeyStore`**: يدير منشأة تخزين للمفاتيح التشفيرية والشهادات.
  - مثال: `KeyStore ks = KeyStore.getInstance("JKS"); ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());`
- **`Signature`**: ينشئ ويتحقق من التوقيعات الرقمية.
  - مثال: `Signature sig = Signature.getInstance("SHA256withRSA"); sig.initSign(privateKey); sig.update(data); byte[] signature = sig.sign();`

### اعتبارات رئيسية
- **التوفر**: تم تضمين حزمة `java.security` في المكتبة القياسية لجافا (جزء من وحدة `java.base` منذ جافا 9)، لذا لا توجد حاجة لاعتماديات خارجية.
- **أفضل ممارسات الأمان**: استخدم دائمًا خوارزميات آمنة (مثل SHA-256 بدلاً من MD5)، وتعامل مع الاستثناءات دون تسريب معلومات حساسة، وامسح البيانات الحساسة من الذاكرة عند الانتهاء.
- **القدرة على التوسع**: للميزات المتقدمة، قد تقوم بدمج `java.security` مع `javax.crypto` (مثل التشفير/فك التشفير) أو مكتبات خارجية مثل Bouncy Castle.

هذه النظرة العامة والمثال يجب أن يمنحك نقطة انطلاق قوية لاستخدام `java.security` في مشاريع جافا الخاصة بك!