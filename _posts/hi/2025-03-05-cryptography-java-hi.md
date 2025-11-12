---
audio: false
generated: true
lang: hi
layout: post
title: जावा में क्रिप्टोग्राफी
translated: true
type: note
---

जावा में `javax.crypto` पैकेज क्रिप्टोग्राफिक ऑपरेशन जैसे एन्क्रिप्शन, डिक्रिप्शन, कुंजी जनरेशन और मैसेज ऑथेंटिकेशन करने के लिए क्लासेज और मेथड्स का एक सेट प्रदान करता है। नीचे `javax.crypto` के उपयोग पर एक व्यापक गाइड दी गई है, जिसमें सामान्य उपयोग के मामलों जैसे सिमेट्रिक एन्क्रिप्शन, एसिमेट्रिक एन्क्रिप्शन और मैसेज ऑथेंटिकेशन के लिए स्पष्टीकरण और प्रैक्टिकल उदाहरण शामिल हैं।

---

### **javax.crypto क्या है?**
`javax.crypto` पैकेज जावा क्रिप्टोग्राफी आर्किटेक्चर (JCA) का हिस्सा है और क्रिप्टोग्राफी के माध्यम से सुरक्षित कम्युनिकेशन लागू करने के लिए टूल्स प्रदान करता है। यह सपोर्ट करता है:
- **सिमेट्रिक क्रिप्टोग्राफी**: एन्क्रिप्शन और डिक्रिप्शन के लिए एक ही कुंजी का उपयोग करता है (जैसे, AES, DES)।
- **एसिमेट्रिक क्रिप्टोग्राफी**: एक पब्लिक/प्राइवेट कुंजी जोड़ी का उपयोग करता है (जैसे, RSA)।
- **मैसेज ऑथेंटिकेशन**: डेटा इंटीग्रिटी और प्रामाणिकता सुनिश्चित करता है (जैसे, HMAC)।
- **कुंजी जनरेशन और प्रबंधन**: क्रिप्टोग्राफिक कुंजियाँ बनाने और संभालने के लिए टूल।

`javax.crypto` का उपयोग करने के लिए, आपको यह करना होगा:
1. एक क्रिप्टोग्राफिक एल्गोरिदम चुनें।
2. आवश्यक कुंजियाँ जनरेट या प्राप्त करें।
3. ऑपरेशन करने के लिए प्रदान की गई क्लासेज (जैसे, `Cipher`, `KeyGenerator`, `Mac`) का उपयोग करें।

नीचे सामान्य परिदृश्यों के लिए चरण-दर-चरण उदाहरण दिए गए हैं।

---

### **1. AES के साथ सिमेट्रिक एन्क्रिप्शन**
सिमेट्रिक एन्क्रिप्शन एन्क्रिप्शन और डिक्रिप्शन दोनों के लिए एक ही कुंजी का उपयोग करता है। यहाँ बताया गया है कि कैसे `Cipher` क्लास का उपयोग करके CBC मोड में PKCS5 पैडिंग के साथ AES (एडवांस्ड एन्क्रिप्शन स्टैंडर्ड) का उपयोग करके एक स्ट्रिंग को एन्क्रिप्ट और डिक्रिप्ट किया जाए।

#### **चरण**
- एक सीक्रेट कुंजी जनरेट करें।
- एक `Cipher` इंस्टेंस बनाएँ और इनिशियलाइज़ करें।
- डेटा को एन्क्रिप्ट और डिक्रिप्ट करें।

#### **उदाहरण कोड**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // चरण 1: AES के लिए एक सीक्रेट कुंजी जनरेट करें
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128-बिट कुंजी
        SecretKey secretKey = keyGen.generateKey();

        // चरण 2: एक रैंडम इनिशियलाइजेशन वेक्टर (IV) जनरेट करें
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AES ब्लॉक साइज 16 बाइट्स है
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // चरण 3: एन्क्रिप्शन के लिए Cipher बनाएँ और इनिशियलाइज़ करें
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // चरण 4: डेटा को एन्क्रिप्ट करें
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // चरण 5: उसी IV के साथ डिक्रिप्शन के लिए Cipher को इनिशियलाइज़ करें
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // परिणाम आउटपुट करें
        System.out.println("Original: " + plaintext);
        System.out.println("Decrypted: " + decryptedText);
    }
}
```

#### **मुख्य बिंदु**
- **एल्गोरिदम**: `"AES/CBC/PKCS5Padding"` ब्लॉक साइज के गुणक में न होने वाले डेटा को हैंडल करने के लिए CBC मोड और पैडिंग के साथ AES निर्दिष्ट करता है।
- **IV**: इनिशियलाइजेशन वेक्टर एन्क्रिप्शन के लिए रैंडम होना चाहिए और डिक्रिप्शन के लिए पुन: उपयोग किया जाना चाहिए। यह आमतौर पर सिफरटेक्स्ट के साथ जोड़ा जाता है या अलग से ट्रांसमिट किया जाता है।
- **कुंजी प्रबंधन**: एक वास्तविक एप्लिकेशन में, `secretKey` को प्राप्तकर्ता के साथ सुरक्षित रूप से साझा करें।

---

### **2. RSA के साथ एसिमेट्रिक एन्क्रिप्शन**
एसिमेट्रिक एन्क्रिप्शन एन्क्रिप्ट करने के लिए एक पब्लिक कुंजी और डिक्रिप्ट करने के लिए एक प्राइवेट कुंजी का उपयोग करता है। यहाँ RSA का उपयोग करने का एक उदाहरण दिया गया है।

#### **चरण**
- एक पब्लिक/प्राइवेट कुंजी जोड़ी जनरेट करें।
- पब्लिक कुंजी के साथ एन्क्रिप्ट करें।
- प्राइवेट कुंजी के साथ डिक्रिप्ट करें।

#### **उदाहरण कोड**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // चरण 1: एक RSA कुंजी जोड़ी जनरेट करें
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048-बिट कुंजी
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // चरण 2: पब्लिक कुंजी के साथ एन्क्रिप्ट करें
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // चरण 3: प्राइवेट कुंजी के साथ डिक्रिप्ट करें
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // परिणाम आउटपुट करें
        System.out.println("Original: " + plaintext);
        System.out.println("Decrypted: " + decryptedText);
    }
}
```

#### **मुख्य बिंदु**
- **साइज लिमिट**: RSA केवल कुंजी के आकार से छोटे डेटा को एन्क्रिप्ट कर सकता है (जैसे, 2048-बिट कुंजी के लिए ~245 बाइट्स)। बड़े डेटा के लिए, हाइब्रिड एन्क्रिप्शन का उपयोग करें (डेटा को सिमेट्रिक कुंजी से एन्क्रिप्ट करें, फिर उस कुंजी को RSA से एन्क्रिप्ट करें)।
- **कुंजी वितरण**: पब्लिक कुंजी को खुले तौर पर साझा करें; प्राइवेट कुंजी को गुप्त रखें।

---

### **3. HMAC के साथ मैसेज ऑथेंटिकेशन**
एक मैसेज ऑथेंटिकेशन कोड (MAC) डेटा इंटीग्रिटी और प्रामाणिकता सुनिश्चित करता है। यहाँ बताया गया है कि कैसे HMAC-SHA256 के साथ `Mac` का उपयोग किया जाए।

#### **उदाहरण कोड**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // चरण 1: एक सीक्रेट कुंजी बनाएँ
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // चरण 2: कुंजी के साथ Mac को इनिशियलाइज़ करें
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // चरण 3: डेटा के लिए MAC की गणना करें
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // परिणाम आउटपुट करें
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **मुख्य बिंदु**
- **वेरिफिकेशन**: प्राप्तकर्ता उसी कुंजी और डेटा के साथ MAC की पुनर्गणना करता है; यदि यह मेल खाता है, तो डेटा प्रामाणिक और अपरिवर्तित है।
- **कुंजी**: एक साझा सीक्रेट कुंजी का उपयोग करें, जो पहले से सुरक्षित रूप से वितरित की गई हो।

---

### **4. स्ट्रीम्स को एन्क्रिप्ट/डिक्रिप्ट करना**
बड़े डेटा (जैसे, फाइल्स) के लिए, `CipherInputStream` या `CipherOutputStream` का उपयोग करें।

#### **उदाहरण कोड (एक फाइल को एन्क्रिप्ट करना)**
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
        // कुंजी और IV जनरेट करें
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Cipher को इनिशियलाइज़ करें
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // फाइल एन्क्रिप्ट करें
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

#### **मुख्य बिंदु**
- **स्ट्रीम्स**: डेटा को इंक्रीमेंटली प्रोसेस करने के लिए एन्क्रिप्शन के लिए `CipherOutputStream` और डिक्रिप्शन के लिए `CipherInputStream` का उपयोग करें।
- **IV हैंडलिंग**: IV को एन्क्रिप्टेड फाइल के साथ स्टोर करें (जैसे, इसे प्रीपेंड करें)।

---

### **5. पासवर्ड-आधारित एन्क्रिप्शन (PBE)**
`SecretKeyFactory` का उपयोग करके एक पासवर्ड से कुंजी प्राप्त करें।

#### **उदाहरण कोड**
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
        // पासवर्ड और सॉल्ट
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // पासवर्ड से कुंजी प्राप्त करें
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256-बिट कुंजी
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // प्राप्त कुंजी के साथ एन्क्रिप्ट करें
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **मुख्य बिंदु**
- **सॉल्ट**: कुंजी व्युत्पत्ति को रैंडमाइज़ करें; इसे एन्क्रिप्टेड डेटा के साथ स्टोर करें।
- **पुनरावृत्तियाँ**: ब्रूट-फोर्स अटैक्स को विफल करने के लिए कम्प्यूटेशनल लागत बढ़ाएँ (जैसे, 10,000)।

---

### **javax.crypto में मुख्य क्लासेज**
- **`Cipher`**: एन्क्रिप्शन और डिक्रिप्शन करता है।
- **`KeyGenerator`**: सिमेट्रिक कुंजियाँ जनरेट करता है (जैसे, AES)।
- **`KeyPairGenerator`**: एसिमेट्रिक कुंजी जोड़े जनरेट करता है (जैसे, RSA)।
- **`Mac`**: मैसेज ऑथेंटिकेशन कोड की गणना करता है।
- **`SecretKeyFactory`**: कुंजियाँ प्राप्त करता है (जैसे, पासवर्ड से)।
- **`SecureRandom`**: क्रिप्टोग्राफिक रूप से सुरक्षित रैंडम नंबर जनरेट करता है।

---

### **सर्वोत्तम अभ्यास**
- **एक्सेप्शन हैंडलिंग**: `NoSuchAlgorithmException`, `InvalidKeyException` आदि जैसे एक्सेप्शन के लिए कोड को ट्राई-कैच ब्लॉक में रैप करें।
- **कुंजी प्रबंधन**: कुंजियों को सुरक्षित रूप से स्टोर करें (जैसे, `KeyStore` में) और उन्हें कभी भी हार्डकोड न करें।
- **एल्गोरिदम चयन**: सुरक्षित एल्गोरिदम (जैसे, AES-256, RSA-2048) और मोड (जैसे, IV के साथ CBC) का उपयोग करें।
- **प्रोवाइडर्स**: डिफॉल्ट SunJCE प्रोवाइडर पर्याप्त है, लेकिन आप अन्य (जैसे, BouncyCastle) का उपयोग `Cipher.getInstance("AES", "BC")` के माध्यम से कर सकते हैं।

---

### **निष्कर्ष**
`javax.crypto` का उपयोग करने के लिए, अपनी आवश्यकताओं के लिए उपयुक्त क्रिप्टोग्राफिक एल्गोरिदम चुनें, कुंजियाँ जनरेट या प्राप्त करें, और ऑपरेशन करने के लिए `Cipher`, `KeyGenerator`, और `Mac` जैसी क्लासेज का लाभ उठाएँ। चाहे आप AES के साथ सिमेट्रिक रूप से डेटा एन्क्रिप्ट कर रहे हों, RSA के साथ एसिमेट्रिक रूप से, या HMAC के साथ इंटीग्रिटी सुनिश्चित कर रहे हों, `javax.crypto` उपयुक्त इनिशियलाइजेशन और सुरक्षित कुंजी प्रबंधन के साथ जावा में मजबूत क्रिप्टोग्राफी लागू करने के लिए टूल्स प्रदान करता है।