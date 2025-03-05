---
audio: false
generated: true
lang: hi
layout: post
title: क्रिप्टोग्राफी इन जावा
translated: true
---

`javax.crypto` पैकेज जावा में क्रिप्टोग्राफिक ऑपरेशन्स जैसे एन्क्रिप्शन, डिक्रिप्शन, की जनरेशन, और मेसेज ऑथेंटिकेशन करने के लिए एक सेट ऑफ क्लासेस और मेथड्स प्रदान करता है। नीचे `javax.crypto` का उपयोग करने के लिए एक विस्तृत गाइड है, जिसमें सामान्य उपयोग केस जैसे सिमेट्रिक एन्क्रिप्शन, असिमेट्रिक एन्क्रिप्शन, और मेसेज ऑथेंटिकेशन के लिए स्पष्टीकरण और प्रैक्टिकल उदाहरण शामिल हैं।

---

### **javax.crypto क्या है?**
`javax.crypto` पैकेज जावा क्रिप्टोग्राफी आर्किटेक्चर (JCA) का हिस्सा है और क्रिप्टोग्राफी के माध्यम से सुरक्षित संचार को लागू करने के लिए औजार प्रदान करता है। यह समर्थन करता है:
- **सिमेट्रिक क्रिप्टोग्राफी**: एन्क्रिप्शन और डिक्रिप्शन के लिए एक ही की का उपयोग करता है (उदाहरण के लिए, AES, DES).
- **असिमेट्रिक क्रिप्टोग्राफी**: एक पब्लिक/प्राइवेट की पेर का उपयोग करता है (उदाहरण के लिए, RSA).
- **मेसेज ऑथेंटिकेशन**: डेटा की एकीकृतता और सत्यापन को सुनिश्चित करता है (उदाहरण के लिए, HMAC).
- **की जनरेशन और मैनेजमेंट**: क्रिप्टोग्राफिक कीज बनाना और संभालने के औजार.

`javax.crypto` का उपयोग करने के लिए, आपको:
1. एक क्रिप्टोग्राफिक एल्गोरिथम चुनना होगा।
2. आवश्यक कीज जनरेट करना या प्राप्त करना होगा।
3. प्रदान की गई क्लासेस (उदाहरण के लिए, `Cipher`, `KeyGenerator`, `Mac`) का उपयोग करके ऑपरेशन्स करने होंगे।

नीचे सामान्य सीनारियो के लिए चरण-दर-चरण उदाहरण दिए गए हैं।

---

### **1. AES के साथ सिमेट्रिक एन्क्रिप्शन**
सिमेट्रिक एन्क्रिप्शन एन्क्रिप्शन और डिक्रिप्शन दोनों के लिए एक ही की का उपयोग करता है। यहां `Cipher` क्लास के साथ CBC मोड के साथ PKCS5 पेडिंग के साथ AES (एडवांस्ड एन्क्रिप्शन स्टैंडर्ड) का उपयोग करके एक स्ट्रिंग को एन्क्रिप्ट और डिक्रिप्ट करने का तरीका है।

#### **चरण**
- एक सिक्रेट की जनरेट करें।
- एक `Cipher` इंस्टेंस बनाएं और इनिशियलाइज करें।
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
        // चरण 1: AES के लिए एक सिक्रेट की जनरेट करें
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128-बिट की
        SecretKey secretKey = keyGen.generateKey();

        // चरण 2: एक रैंडम इनिशियलाइजेशन वेक्टर (IV) जनरेट करें
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AES ब्लॉक साइज 16 बाइट्स है
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // चरण 3: एन्क्रिप्शन के लिए Cipher बनाएं और इनिशियलाइज करें
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // चरण 4: डेटा को एन्क्रिप्ट करें
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // चरण 5: डिक्रिप्शन के लिए Cipher को उसी IV के साथ इनिशियलाइज करें
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // परिणाम निकालें
        System.out.println("मूल: " + plaintext);
        System.out.println("डिक्रिप्ट: " + decryptedText);
    }
}
```

#### **मुख्य बिंदु**
- **एल्गोरिथम**: `"AES/CBC/PKCS5Padding"` AES के साथ CBC मोड और पेडिंग को स्पेसिफाइ करता है ताकि ब्लॉक साइज का गुणा न हो सके।
- **IV**: एन्क्रिप्शन के लिए IV रैंडम होना चाहिए और डिक्रिप्शन के लिए पुनः उपयोग किया जाना चाहिए। यह आमतौर पर सिफरटेक्स्ट के साथ जोड़ा जाता है या अलग से ट्रांसमिट किया जाता है।
- **की मैनेजमेंट**: एक वास्तविक एप्लिकेशन में, `secretKey` को सुरक्षित रूप से प्राप्तकर्ता के साथ साझा करें।

---

### **2. RSA के साथ असिमेट्रिक एन्क्रिप्शन**
असिमेट्रिक एन्क्रिप्शन एक पब्लिक की को एन्क्रिप्ट करने और एक प्राइवेट की को डिक्रिप्ट करने के लिए उपयोग करता है। यहां RSA का उपयोग करने का उदाहरण है।

#### **चरण**
- एक पब्लिक/प्राइवेट की पेर जनरेट करें।
- पब्लिक की के साथ एन्क्रिप्ट करें।
- प्राइवेट की के साथ डिक्रिप्ट करें।

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
        // चरण 1: एक RSA की पेर जनरेट करें
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048-बिट की
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // चरण 2: पब्लिक की के साथ एन्क्रिप्ट करें
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // चरण 3: प्राइवेट की के साथ डिक्रिप्ट करें
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // परिणाम निकालें
        System.out.println("मूल: " + plaintext);
        System.out.println("डिक्रिप्ट: " + decryptedText);
    }
}
```

#### **मुख्य बिंदु**
- **साइज सीमा**: RSA केवल की साइज से छोटे डेटा को एन्क्रिप्ट कर सकता है (उदाहरण के लिए, ~245 बाइट्स के लिए एक 2048-बिट की)। बड़े डेटा के लिए, हाइब्रिड एन्क्रिप्शन का उपयोग करें (डेटा को एक सिमेट्रिक की के साथ एन्क्रिप्ट करें, फिर उस की को RSA के साथ एन्क्रिप्ट करें).
- **की वितरण**: पब्लिक की को खुले तौर पर साझा करें; प्राइवेट की को गुप्त रखें।

---

### **3. HMAC के साथ मेसेज ऑथेंटिकेशन**
एक मेसेज ऑथेंटिकेशन कोड (MAC) डेटा की एकीकृतता और सत्यापन सुनिश्चित करता है। यहां `Mac` के साथ HMAC-SHA256 का उपयोग करने का तरीका है।

#### **उदाहरण कोड**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // चरण 1: एक सिक्रेट की बनाएं
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // चरण 2: की के साथ Mac इनिशियलाइज करें
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // चरण 3: डेटा के लिए MAC कंप्यूट करें
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // परिणाम निकालें
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **मुख्य बिंदु**
- **सत्यापन**: प्राप्तकर्ता उसी की और डेटा के साथ MAC को पुनः कंप्यूट करता है; अगर यह मिलता है, तो डेटा सत्यापित और अक्षत है।
- **की**: एक साझा सिक्रेट की का उपयोग करें, जो पहले से सुरक्षित रूप से वितरित किया गया है।

---

### **4. स्ट्रीम एन्क्रिप्ट/डिक्रिप्ट**
बड़े डेटा (उदाहरण के लिए, फाइलें) के लिए, `CipherInputStream` या `CipherOutputStream` का उपयोग करें।

#### **उदाहरण कोड (एक फाइल को एन्क्रिप्ट करने के लिए)**
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
        // की और IV जनरेट करें
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Cipher इनिशियलाइज करें
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // फाइल को एन्क्रिप्ट करें
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
- **स्ट्रीम**: एन्क्रिप्शन के लिए `CipherOutputStream` और डिक्रिप्शन के लिए `CipherInputStream` का उपयोग करें ताकि डेटा को क्रमशः प्रोसेस किया जा सके।
- **IV हैंडलिंग**: IV को एन्क्रिप्टेड फाइल के साथ स्टोर करें (उदाहरण के लिए, इसे प्रीपेंड करें).

---

### **5. पासवर्ड-बेस्ड एन्क्रिप्शन (PBE)**
`SecretKeyFactory` का उपयोग करके एक पासवर्ड से एक की डेरिव करें।

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

        // पासवर्ड से की डेरिव करें
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256-बिट की
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // डेरिव की के साथ एन्क्रिप्ट करें
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **मुख्य बिंदु**
- **सॉल्ट**: की डेरिवेशन को रैंडमाइज करें; इसे एन्क्रिप्टेड डेटा के साथ स्टोर करें।
- **इटरेशन्स**: ब्रूट-फोर्स अटैक्स को रोकने के लिए कंप्यूटेशनल लागत बढ़ाएं (उदाहरण के लिए, 10,000).

---

### **javax.crypto में मुख्य क्लासेस**
- **`Cipher`**: एन्क्रिप्शन और डिक्रिप्शन करता है।
- **`KeyGenerator`**: सिमेट्रिक कीज जनरेट करता है (उदाहरण के लिए, AES).
- **`KeyPairGenerator`**: असिमेट्रिक की पेर जनरेट करता है (उदाहरण के लिए, RSA).
- **`Mac`**: मेसेज ऑथेंटिकेशन कोड कंप्यूट करता है।
- **`SecretKeyFactory`**: कीज डेरिव करता है (उदाहरण के लिए, पासवर्ड से).
- **`SecureRandom`**: क्रिप्टोग्राफिकली सुरक्षित रैंडम नंबर जनरेट करता है।

---

### **बेस्ट प्रैक्टिस**
- **एक्सेप्शन हैंडलिंग**: `NoSuchAlgorithmException`, `InvalidKeyException` जैसे एक्सेप्शन के लिए कोड को try-catch ब्लॉक में लपेटें।
- **की मैनेजमेंट**: कीज को सुरक्षित रूप से स्टोर करें (उदाहरण के लिए, एक `KeyStore` में) और कभी भी हार्डकोड न करें।
- **एल्गोरिथम चयन**: सुरक्षित एल्गोरिथम (उदाहरण के लिए, AES-256, RSA-2048) और मोड (उदाहरण के लिए, CBC के साथ IV) का उपयोग करें।
- **प्रोवाइडर्स**: डिफ़ॉल्ट SunJCE प्रोवाइडर काफी है, लेकिन आप अन्य (उदाहरण के लिए, BouncyCastle) का उपयोग कर सकते हैं `Cipher.getInstance("AES", "BC")` के माध्यम से।

---

### **निष्कर्ष**
`javax.crypto` का उपयोग करने के लिए, अपने आवश्यकताओं के लिए उपयुक्त क्रिप्टोग्राफिक एल्गोरिथम चुनें, कीज जनरेट करें या प्राप्त करें, और `Cipher`, `KeyGenerator`, और `Mac` जैसे क्लासेस का उपयोग करके ऑपरेशन्स करें। चाहे आप AES के साथ सिमेट्रिक रूप से डेटा को एन्क्रिप्ट करें, RSA के साथ असिमेट्रिक रूप से एन्क्रिप्ट करें, या HMAC के साथ एकीकृतता सुनिश्चित करें, `javax.crypto` आपको औजार प्रदान करता है—साथ ही सही इनिशियलाइजेशन और सुरक्षित की मैनेजमेंट के साथ—जावा में मजबूत क्रिप्टोग्राफी को लागू करने के लिए।