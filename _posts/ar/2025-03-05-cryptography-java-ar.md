---
audio: false
generated: true
lang: ar
layout: post
title: التشفير في جافا
translated: true
type: note
---

توفّر حزمة `javax.crypto` في Java مجموعة من الفئات والطرق لتنفيذ عمليات التشفير مثل التشفير، وفك التشفير، وتوليد المفاتيح، والمصادقة على الرسائل. فيما يلي دليل شامل حول كيفية استخدام `javax.crypto`، يتضمن شروحات وأمثلة عملية لحالات الاستخدام الشائعة مثل التشفير المتناظر، والتشفير غير المتناظر، والمصادقة على الرسائل.

---

### **ما هي حزمة javax.crypto؟**
حزمة `javax.crypto` هي جزء من Java Cryptography Architecture (JCA) وتوفر أدوات لتنفيذ اتصال آمن عبر التشفير. وهي تدعم:
- **التشفير المتناظر**: يستخدم نفس المفتاح للتشفير وفك التشفير (مثل AES, DES).
- **التشفير غير المتناظر**: يستخدم زوجًا من المفاتيح (عام/خاص) (مثل RSA).
- **مصادقة الرسائل**: تضمن سلامة البيانات وأصالتها (مثل HMAC).
- **توليد المفاتيح وإدارتها**: أدوات لإنشاء والتعامل مع المفاتيح المشفرة.

لاستخدام `javax.crypto`، تحتاج إلى:
1. اختيار خوارزمية تشفير مناسبة.
2. توليد أو الحصول على المفاتيح اللازمة.
3. استخدام الفئات الموفرة (مثل `Cipher`، `KeyGenerator`، `Mac`) لتنفيذ العمليات.

فيما يلي أمثلة خطوة بخطوة لحالات شائعة.

---

### **1. التشفير المتناظر باستخدام AES**
يستخدم التشفير المتناظر مفتاحًا واحدًا لكل من التشفير وفك التشفير. إليك كيفية تشفير وفك تشفير سلسلة نصية باستخدام AES (معيار التشفير المتقدم) مع فئة `Cipher` في وضع CBC مع حشو PKCS5.

#### **الخطوات**
- توليد مفتاح سري.
- إنشاء وتهيئة مثيل من `Cipher`.
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
        // الخطوة 1: توليد مفتاح سري لـ AES
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // مفتاح 128-بت
        SecretKey secretKey = keyGen.generateKey();

        // الخطوة 2: توليد متجه تهيئة عشوائي (IV)
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // حجم كتلة AES هو 16 بايت
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // الخطوة 3: إنشاء وتهيئة Cipher للتشفير
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // الخطوة 4: تشفير البيانات
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // الخطوة 5: تهيئة Cipher لفك التشفير بنفس IV
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // عرض النتائج
        System.out.println("Original: " + plaintext);
        System.out.println("Decrypted: " + decryptedText);
    }
}
```

#### **النقاط الرئيسية**
- **الخوارزمية**: `"AES/CBC/PKCS5Padding"` تحدد AES مع وضع CBC والحشو للتعامل مع البيانات التي ليست مضاعفًا لحجم الكتلة.
- **IV**: يجب أن يكون متجه التهيئة عشوائيًا للتشفير ويعاد استخدامه لفك التشفير. عادةً ما يضاف في بداية النص المشفر أو ينقل بشكل منفصل.
- **إدارة المفاتيح**: في التطبيق الحقيقي، شارك `secretKey` مع المستلم بطريقة آمنة.

---

### **2. التشفير غير المتناظر باستخدام RSA**
يستخدم التشفير غير المتناظر مفتاحًا عامًا للتشفير ومفتاحًا خاصًا لفك التشفير. إليك مثال باستخدام RSA.

#### **الخطوات**
- توليد زوج مفاتيح (عام/خاص).
- التشفير باستخدام المفتاح العام.
- فك التشفير باستخدام المفتاح الخاص.

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
        // الخطوة 1: توليد زوج مفاتيح RSA
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // مفتاح 2048-بت
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // الخطوة 2: التشفير باستخدام المفتاح العام
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // الخطوة 3: فك التشفير باستخدام المفتاح الخاص
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // عرض النتائج
        System.out.println("Original: " + plaintext);
        System.out.println("Decrypted: " + decryptedText);
    }
}
```

#### **النقاط الرئيسية**
- **حد الحجم**: يمكن لـ RSA تشفير بيانات أصغر من حجم المفتاح فقط (مثل ~245 بايت لمفتاح 2048-بت). للبيانات الأكبر، استخدم التشفير الهجين (شفر البيانات بمفتاح متناظر، ثم شفر ذلك المفتاح باستخدام RSA).
- **توزيع المفاتيح**: شارك المفتاح العام بشكل علني؛ احتفظ بالمفتاح الخاص سريًا.

---

### **3. مصادقة الرسائل باستخدام HMAC**
يضمن رمز مصادقة الرسالة (MAC) سلامة البيانات وأصالتها. إليك كيفية استخدام `Mac` مع HMAC-SHA256.

#### **كود المثال**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // الخطوة 1: إنشاء مفتاح سري
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // الخطوة 2: تهيئة Mac بالمفتاح
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // الخطوة 3: حساب MAC للبيانات
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // عرض النتيجة
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **النقاط الرئيسية**
- **التحقق**: يعيد المستلم حساب MAC باستخدام نفس المفتاح والبيانات؛ إذا تطابق، تكون البيانات أصلية وغير معدلة.
- **المفتاح**: استخدم مفتاحًا سريًا مشتركًا، يتم توزيعه مسبقًا بطريقة آمنة.

---

### **4. تشفير/فك تشفير التدفقات (Streams)**
للبيانات الكبيرة (مثل الملفات)، استخدم `CipherInputStream` أو `CipherOutputStream`.

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
        // توليد المفتاح و IV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // تهيئة Cipher
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
- **التدفقات**: استخدم `CipherOutputStream` للتشفير و `CipherInputStream` لفك التشفير لمعالجة البيانات بشكل تدريجي.
- **التعامل مع IV**: خزن IV مع الملف المشفر (مثل إضافته في البداية).

---

### **5. التشفير القائم على كلمة المرور (PBE)**
اشتق مفتاحًا من كلمة مرور باستخدام `SecretKeyFactory`.

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
        // كلمة المرور والملح (Salt)
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // اشتقاق المفتاح من كلمة المرور
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // مفتاح 256-بت
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // التشفير بالمفتاح المشتق
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **النقاط الرئيسية**
- **الملح (Salt)**: عشوائية اشتقاق المفتاح؛ خزنه مع البيانات المشفرة.
- **التكرارات**: زد التكلفة الحسابية لصد هجمات القوة الغاشمة (مثل 10,000).

---

### **الفئات الرئيسية في javax.crypto**
- **`Cipher`**: ينفذ التشفير وفك التشفير.
- **`KeyGenerator`**: يولد مفاتيح متناظرة (مثل AES).
- **`KeyPairGenerator`**: يولد أزواج مفاتيح غير متناظرة (مثل RSA).
- **`Mac`**: يحسب رموز مصادقة الرسائل.
- **`SecretKeyFactory`**: يشتق مفاتيح (مثل من كلمات المرور).
- **`SecureRandom`**: يولد أرقام عشوائية آمنة مشفريًا.

---

### **أفضل الممارسات**
- **معالجة الاستثناءات**: ضع الكود داخل كتل try-catch للاستثناءات مثل `NoSuchAlgorithmException`، `InvalidKeyException`، إلخ.
- **إدارة المفاتيح**: خزن المفاتيح بشكل آمن (مثل في `KeyStore`) ولا تضعها مباشرة في الكود.
- **اختيار الخوارزمية**: استخدم خوارزميات آمنة (مثل AES-256, RSA-2048) وأوضاع آمنة (مثل CBC مع IV).
- **مزودو الخدمة (Providers)**: مزود SunJCE الافتراضي كافٍ، ولكن يمكنك استخدام آخرين (مثل BouncyCastle) عبر `Cipher.getInstance("AES", "BC")`.

---

### **الخلاصة**
لاستخدام `javax.crypto`، اختر خوارزمية التشفير المناسبة لاحتياجاتك، وقم بتوليد أو الحصول على المفاتيح، واستفد من فئات مثل `Cipher`، `KeyGenerator`، و `Mac` لتنفيذ العمليات. سواء كنت تشفر البيانات بشكل متناظر باستخدام AES، أو بشكل غير متناظر باستخدام RSA، أو تضمن السلامة باستخدام HMAC، فإن `javax.crypto` يوفر الأدوات—إلى جانب التهيئة الصحيحة والإدارة الآمنة للمفاتيح—لتنفيذ تشفير قوي في Java.