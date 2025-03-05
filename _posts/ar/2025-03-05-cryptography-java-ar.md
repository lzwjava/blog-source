---
audio: false
generated: true
lang: ar
layout: post
title: تشفير في جاڤا
translated: true
---

العبارة `javax.crypto` في جاڤا توفر مجموعة من الفئات والأدوات لتنفيذ العمليات التشفيرية مثل التشفير، الفك التشفير، توليد المفتاح، والتحقق من الرسالة. أدناه دليل شامل على كيفية استخدام `javax.crypto`، بما في ذلك الشرحات والأمثلة العملية للحالات الشائعة مثل التشفير المتساوي، التشفير غير المتساوي، والتحقق من الرسالة.

---

### **ما هو javax.crypto؟**
العبارة `javax.crypto` جزء من بنية التشفير في جاڤا (JCA) وتوفر الأدوات لتنفيذ التواصل الآمن عبر التشفير. تدعم:
- **التشفير المتساوي**: يستخدم المفتاح نفسه للتشفير والفك التشفير (مثل AES، DES).
- **التشفير غير المتساوي**: يستخدم زوج المفتاح العام/الخاص (مثل RSA).
- **التحقق من الرسالة**: يضمن سلامة البيانات والصدق (مثل HMAC).
- **توليد المفتاح وإدارتها**: الأدوات لإنشاء وإدارة المفتاح التشفيري.

لاستخدام `javax.crypto`، عليك:
1. اختيار خوارزمية تشفيرية.
2. توليد أو الحصول على المفتاحات اللازمة.
3. استخدام الفئات الموفرة (مثل `Cipher`، `KeyGenerator`، `Mac`) لتنفيذ العمليات.

أدناه أمثلة خطوة بخطوة للحالات الشائعة.

---

### **1. التشفير المتساوي مع AES**
التشفير المتساوي يستخدم مفتاح واحد للتشفير والفك التشفير. إليك كيفية تشفير وفك تشفير نص باستخدام AES (الاستاندارد المتقدم للتشفير) مع الفئة `Cipher` في وضع CBC مع ملء PKCS5.

#### **الخطوات**
- توليد مفتاح سر.
- إنشاء وإعداد فئة `Cipher`.
- تشفير وفك تشفير البيانات.

#### **كود المثال**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // الخطوة 1: توليد مفتاح سر لأيس
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // مفتاح 128 بت
        SecretKey secretKey = keyGen.generateKey();

        // الخطوة 2: توليد متغير تهيئة عشوائي (IV)
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // حجم كتلة AES هو 16 بايت
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // الخطوة 3: إنشاء وإعداد Cipher للتشفير
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // الخطوة 4: تشفير البيانات
        String plaintext = "مرحبا، عالم!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // الخطوة 5: إعداد Cipher لفك التشفير مع نفس IV
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // إخراج النتائج
        System.out.println("الأصل: " + plaintext);
        System.out.println("الفك التشفير: " + decryptedText);
    }
}
```

#### **النقاط الرئيسية**
- **الخوارزمية**: `"AES/CBC/PKCS5Padding"` يحدد AES في وضع CBC مع ملء لتعامل مع البيانات التي ليست مضاعفة من حجم الكتلة.
- **IV**: يجب أن يكون متغير التهيئة عشوائي للتشفير ومكرر لفك التشفير. عادةً ما يتم إضافته إلى النص المشفّر أو إرسالها بشكل منفصل.
- **إدارة المفتاح**: في تطبيق حقيقي، قم بتوزيع المفتاح السري بشكل آمن مع المستلم.

---

### **2. التشفير غير المتساوي مع RSA**
التشفير غير المتساوي يستخدم المفتاح العام للتشفير والمفتاح الخاص لفك التشفير. إليك مثال باستخدام RSA.

#### **الخطوات**
- توليد زوج المفتاح العام/الخاص.
- تشفير بالمفتاح العام.
- فك التشفير بالمفتاح الخاص.

#### **كود المثال**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // الخطوة 1: توليد زوج مفتاح RSA
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // مفتاح 2048 بت
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // الخطوة 2: تشفير بالمفتاح العام
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "رسالة سرية";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // الخطوة 3: فك التشفير بالمفتاح الخاص
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // إخراج النتائج
        System.out.println("الأصل: " + plaintext);
        System.out.println("الفك التشفير: " + decryptedText);
    }
}
```

#### **النقاط الرئيسية**
- **حد الحجم**: يمكن أن يشفّر RSA فقط البيانات الأصغر من حجم المفتاح (مثل ~245 بايت لمفتاح 2048 بت). بالنسبة للبيانات الأكبر، استخدم التشفير الهجين (تشفير البيانات بمفتاح متساوي، ثم تشفير ذلك المفتاح باستخدام RSA).
- **توزيع المفتاح**: قم بتوزيع المفتاح العام بشكل علني؛ احتفظ بالمفتاح الخاص سرًا.

---

### **3. التحقق من الرسالة مع HMAC**
رمز التحقق من الرسالة (MAC) يضمن سلامة البيانات والصدق. إليك كيفية استخدام `Mac` مع HMAC-SHA256.

#### **كود المثال**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // الخطوة 1: إنشاء مفتاح سر
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // الخطوة 2: إعداد Mac بالمفتاح
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // الخطوة 3: حساب MAC للبيانات
        String data = "بيانات للتحقق";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // إخراج النتيجة
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **النقاط الرئيسية**
- **التحقق**: يقوم المستلم بحساب MAC مرة أخرى باستخدام نفس المفتاح والبيانات؛ إذا كان مطابقًا، فإن البيانات صحيحة ومغير.
- **المفتاح**: استخدم مفتاح سر مشترك، تم توزيعه بشكل آمن مسبقًا.

---

### **4. تشفير/فك تشفير التدفقات**
لبيانات كبيرة (مثل الملفات)، استخدم `CipherInputStream` أو `CipherOutputStream`.

#### **كود المثال (تشفير ملف)**
```java
import javax.crypto.Cipher;
import javax.crypto.CipherOutputStream;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.security.SecureRandom;

public class StreamEncryptionExample {
    public static void main(String[] args) throws Exception {
        // توليد المفتاح وIV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // إعداد Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // تشفير الملف
        try (FileInputStream fis = new FileInputStream("input.txt");
             FileOutputStream fos = new FileOutputStream("encrypted.txt");
             CipherOutputStream cos = new CipherOutputStream(fos, cipher)) {
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = fis.read(buffer)) != -1) {
                cos.write(buffer, 0, bytesRead);
            }
        }
    }
}
```

#### **النقاط الرئيسية**
- **التدفقات**: استخدم `CipherOutputStream` للتشفير و`CipherInputStream` لفك التشفير لمعالجة البيانات تدريجيًا.
- **إدارة IV**: احفظ IV مع الملف المشفّر (مثل إضافته إليه).

---

### **5. التشفير القائم على كلمة المرور (PBE)**
استخرج المفتاح من كلمة المرور باستخدام `SecretKeyFactory`.

#### **كود المثال**
```java
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class PBEExample {
    public static void main(String[] args) throws Exception {
        // كلمة المرور والملح
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // استخراج المفتاح من كلمة المرور
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // مفتاح 256 بت
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // تشفير بالمفتاح المستخرج
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "مرحبا من PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("المشفّر: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **النقاط الرئيسية**
- **الملح**: عشوائي استخراج المفتاح؛ احفظه مع البيانات المشفرة.
- **التكرار**: زيادة تكلفة الحساب لتجنب الهجمات بالقوة الغاشمة (مثل 10,000).

---

### **الفئات الرئيسية في javax.crypto**
- **`Cipher`**: يقوم بتشفير وفك التشفير.
- **`KeyGenerator`**: يولد مفتاحات متساوية (مثل AES).
- **`KeyPairGenerator`**: يولد أزواج مفتاحات غير متساوية (مثل RSA).
- **`Mac`**: يحسب رموز التحقق من الرسالة.
- **`SecretKeyFactory`**: يستخرج المفتاحات (مثل من كلمات المرور).
- **`SecureRandom`**: يولد أرقام عشوائية آمنة تشفيرية.

---

### **أفضل الممارسات**
- **إدارة الاستثناءات**: قم بغلاف الكود في كتل try-catch للاستثناءات مثل `NoSuchAlgorithmException`، `InvalidKeyException`، إلخ.
- **إدارة المفتاح**: احفظ المفتاحات بشكل آمن (مثل في `KeyStore`) ولا تقم بتشفيرها بشكل صريح.
- **اختيار الخوارزمية**: استخدم خوارزميات آمنة (مثل AES-256، RSA-2048) وأوضاع (مثل CBC مع IV).
- **الموفرين**: يفي الموفر الافتراضي SunJCE، ولكن يمكنك استخدام آخرين (مثل BouncyCastle) عبر `Cipher.getInstance("AES", "BC")`.

---

### **الخاتمة**
لاستخدام `javax.crypto`، اختر الخوارزمية التشفيرية المناسبة لحاجتك، تولد أو احصل على المفتاحات، واستخدم الفئات مثل `Cipher`، `KeyGenerator`، و`Mac` لتنفيذ العمليات. سواء كنت تشفّر البيانات بشكل متساوي مع AES، غير متساوي مع RSA، أو تأكد من سلامتها مع HMAC، فإن `javax.crypto` توفر الأدوات - مع التهيئة المناسبة وإدارة المفتاح الآمنة - لتنفيذ التشفير القوي في جاڤا.