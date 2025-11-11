---
audio: false
generated: true
lang: hant
layout: post
title: Java 密碼學
translated: true
type: note
---

Java 中的 `javax.crypto` 套件提供了一系列用於執行加密操作的類別和方法，例如加密、解密、金鑰生成和訊息驗證。以下是如何使用 `javax.crypto` 的完整指南，包括對稱加密、非對稱加密和訊息驗證等常見用例的說明與實例。

---

### **什麼是 javax.crypto？**
`javax.crypto` 套件是 Java 加密架構（JCA）的一部分，提供了透過密碼學實現安全通訊的工具。它支援：
- **對稱密碼學**：使用相同金鑰進行加密和解密（例如 AES、DES）。
- **非對稱密碼學**：使用公鑰/私鑰對（例如 RSA）。
- **訊息驗證**：確保資料完整性和真實性（例如 HMAC）。
- **金鑰生成與管理**：用於建立和處理加密金鑰的工具。

使用 `javax.crypto` 時，你需要：
1. 選擇一種加密演算法。
2. 生成或取得必要的金鑰。
3. 使用提供的類別（例如 `Cipher`、`KeyGenerator`、`Mac`）來執行操作。

以下是常見情境的逐步範例。

---

### **1. 使用 AES 進行對稱加密**
對稱加密使用單一金鑰進行加密和解密。以下展示如何使用 `Cipher` 類別，以 CBC 模式和 PKCS5 填充方式，對字串進行 AES（進階加密標準）加密和解密。

#### **步驟**
- 生成一個秘密金鑰。
- 建立並初始化 `Cipher` 實例。
- 加密和解密資料。

#### **範例程式碼**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 步驟 1：生成 AES 秘密金鑰
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128 位元金鑰
        SecretKey secretKey = keyGen.generateKey();

        // 步驟 2：生成隨機初始化向量（IV）
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AES 區塊大小為 16 位元組
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // 步驟 3：建立並初始化用於加密的 Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // 步驟 4：加密資料
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // 步驟 5：使用相同 IV 初始化用於解密的 Cipher
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 輸出結果
        System.out.println("原始內容：" + plaintext);
        System.out.println("解密內容：" + decryptedText);
    }
}
```

#### **關鍵點**
- **演算法**：`"AES/CBC/PKCS5Padding"` 指定了使用 CBC 模式和填充方式處理非區塊大小倍數的資料。
- **IV**：初始化向量必須隨機生成用於加密，並在解密時重複使用。通常會預先附加到密文或單獨傳輸。
- **金鑰管理**：在實際應用中，需安全地與接收方共享 `secretKey`。

---

### **2. 使用 RSA 進行非對稱加密**
非對稱加密使用公鑰加密，私鑰解密。以下是使用 RSA 的範例。

#### **步驟**
- 生成公鑰/私鑰對。
- 使用公鑰加密。
- 使用私鑰解密。

#### **範例程式碼**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 步驟 1：生成 RSA 金鑰對
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048 位元金鑰
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // 步驟 2：使用公鑰加密
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // 步驟 3：使用私鑰解密
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 輸出結果
        System.out.println("原始內容：" + plaintext);
        System.out.println("解密內容：" + decryptedText);
    }
}
```

#### **關鍵點**
- **大小限制**：RSA 只能加密小於金鑰大小的資料（例如 2048 位元金鑰約為 245 位元組）。對於較大資料，請使用混合加密（先用對稱金鑰加密資料，再用 RSA 加密該金鑰）。
- **金鑰分發**：公開分享公鑰；私鑰必須保密。

---

### **3. 使用 HMAC 進行訊息驗證**
訊息驗證碼（MAC）確保資料的完整性和真實性。以下展示如何使用 `Mac` 與 HMAC-SHA256。

#### **範例程式碼**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // 步驟 1：建立秘密金鑰
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // 步驟 2：使用金鑰初始化 Mac
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // 步驟 3：計算資料的 MAC
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // 輸出結果
        System.out.println("MAC：" + macBase64);
    }
}
```

#### **關鍵點**
- **驗證**：接收方使用相同金鑰和資料重新計算 MAC；若匹配，則資料真實且未被篡改。
- **金鑰**：使用事先安全分發的共享秘密金鑰。

---

### **4. 加密/解密串流**
對於大型資料（例如檔案），請使用 `CipherInputStream` 或 `CipherOutputStream`。

#### **範例程式碼（加密檔案）**
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
        // 生成金鑰和 IV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // 初始化 Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // 加密檔案
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

#### **關鍵點**
- **串流**：使用 `CipherOutputStream` 進行加密，`CipherInputStream` 進行解密，以增量方式處理資料。
- **IV 處理**：將 IV 與加密檔案一起儲存（例如預先附加）。

---

### **5. 基於密碼的加密（PBE）**
使用 `SecretKeyFactory` 從密碼衍生金鑰。

#### **範例程式碼**
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
        // 密碼和鹽
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // 從密碼衍生金鑰
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256 位元金鑰
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // 使用衍生金鑰加密
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("加密內容：" + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **關鍵點**
- **鹽**：隨機化金鑰衍生過程；將其與加密資料一起儲存。
- **迭代次數**：增加計算成本以防範暴力攻擊（例如 10,000 次）。

---

### **javax.crypto 中的關鍵類別**
- **`Cipher`**：執行加密和解密。
- **`KeyGenerator`**：生成對稱金鑰（例如 AES）。
- **`KeyPairGenerator`**：生成非對稱金鑰對（例如 RSA）。
- **`Mac`**：計算訊息驗證碼。
- **`SecretKeyFactory`**：衍生金鑰（例如從密碼）。
- **`SecureRandom`**：生成密碼學安全的隨機數。

---

### **最佳實踐**
- **例外處理**：使用 try-catch 區塊處理例外，例如 `NoSuchAlgorithmException`、`InvalidKeyException` 等。
- **金鑰管理**：安全儲存金鑰（例如在 `KeyStore` 中），切勿硬編碼。
- **演算法選擇**：使用安全的演算法（例如 AES-256、RSA-2048）和模式（例如帶有 IV 的 CBC）。
- **提供者**：預設的 SunJCE 提供者已足夠，但也可以透過 `Cipher.getInstance("AES", "BC")` 使用其他提供者（例如 BouncyCastle）。

---

### **結論**
使用 `javax.crypto` 時，根據需求選擇適當的加密演算法，生成或取得金鑰，並利用 `Cipher`、`KeyGenerator` 和 `Mac` 等類別執行操作。無論是使用 AES 進行對稱加密、RSA 進行非對稱加密，還是使用 HMAC 確保完整性，`javax.crypto` 都提供了相應的工具——配合適當的初始化和安全的金鑰管理——以在 Java 中實現穩健的密碼學功能。