---
audio: false
generated: true
lang: zh
layout: post
title: 加密学与Java
translated: true
---

`javax.crypto` 包在 Java 中提供了一组用于执行加密操作的类和方法，如加密、解密、密钥生成和消息认证。下面是如何使用 `javax.crypto` 的全面指南，包括解释和常见用例的实际示例，如对称加密、非对称加密和消息认证。

---

### **什么是 javax.crypto？**
`javax.crypto` 包是 Java 加密架构（JCA）的一部分，并提供了通过加密实现安全通信的工具。它支持：
- **对称加密**：使用相同的密钥进行加密和解密（例如，AES、DES）。
- **非对称加密**：使用公钥/私钥对（例如，RSA）。
- **消息认证**：确保数据完整性和真实性（例如，HMAC）。
- **密钥生成和管理**：创建和处理加密密钥的工具。

要使用 `javax.crypto`，你需要：
1. 选择一个加密算法。
2. 生成或获取必要的密钥。
3. 使用提供的类（例如，`Cipher`、`KeyGenerator`、`Mac`）执行操作。

下面是常见场景的逐步示例。

---

### **1. 使用 AES 的对称加密**
对称加密使用单个密钥进行加密和解密。以下是如何使用 `Cipher` 类在 CBC 模式下使用 PKCS5 填充加密和解密字符串。

#### **步骤**
- 生成一个密钥。
- 创建并初始化一个 `Cipher` 实例。
- 加密和解密数据。

#### **示例代码**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 步骤 1：生成 AES 的密钥
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128 位密钥
        SecretKey secretKey = keyGen.generateKey();

        // 步骤 2：生成随机初始化向量（IV）
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AES 块大小为 16 字节
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // 步骤 3：创建并初始化 Cipher 进行加密
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // 步骤 4：加密数据
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // 步骤 5：使用相同的 IV 初始化 Cipher 进行解密
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 输出结果
        System.out.println("原始: " + plaintext);
        System.out.println("解密后: " + decryptedText);
    }
}
```

#### **关键点**
- **算法**：`"AES/CBC/PKCS5Padding"` 指定了使用 CBC 模式和填充的 AES。
- **IV**：初始化向量必须在加密时是随机的，并在解密时重用。通常在密文前面或单独传输。
- **密钥管理**：在实际应用中，安全地与接收方共享 `secretKey`。

---

### **2. 使用 RSA 的非对称加密**
非对称加密使用公钥进行加密，使用私钥进行解密。以下是使用 RSA 的示例。

#### **步骤**
- 生成公钥/私钥对。
- 使用公钥加密。
- 使用私钥解密。

#### **示例代码**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 步骤 1：生成 RSA 密钥对
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048 位密钥
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // 步骤 2：使用公钥加密
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // 步骤 3：使用私钥解密
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 输出结果
        System.out.println("原始: " + plaintext);
        System.out.println("解密后: " + decryptedText);
    }
}
```

#### **关键点**
- **大小限制**：RSA 只能加密小于密钥大小的数据（例如，对于 2048 位密钥，大约 245 字节）。对于更大的数据，使用混合加密（使用对称密钥加密数据，然后使用 RSA 加密该密钥）。
- **密钥分发**：公开共享公钥；保密私钥。

---

### **3. 使用 HMAC 的消息认证**
消息认证码（MAC）确保数据完整性和真实性。以下是如何使用 `Mac` 与 HMAC-SHA256。

#### **示例代码**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // 步骤 1：创建一个密钥
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // 步骤 2：使用密钥初始化 Mac
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // 步骤 3：计算数据的 MAC
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // 输出结果
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **关键点**
- **验证**：接收方使用相同的密钥和数据重新计算 MAC；如果匹配，则数据是真实且未被篡改的。
- **密钥**：使用预先安全分发的共享密钥。

---

### **4. 加密/解密流**
对于大数据（例如，文件），使用 `CipherInputStream` 或 `CipherOutputStream`。

#### **示例代码（加密文件）**
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
        // 生成密钥和 IV
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // 初始化 Cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // 加密文件
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

#### **关键点**
- **流**：使用 `CipherOutputStream` 进行加密和 `CipherInputStream` 进行解密以逐步处理数据。
- **IV 处理**：将 IV 存储在加密文件中（例如，预先添加）。

---

### **5. 基于密码的加密（PBE）**
使用 `SecretKeyFactory` 从密码派生密钥。

#### **示例代码**
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
        // 密码和盐
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // 从密码派生密钥
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256 位密钥
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // 使用派生密钥加密
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("加密后: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **关键点**
- **盐**：随机化密钥派生；将其存储在加密数据中。
- **迭代**：增加计算成本以抵御暴力攻击（例如，10,000）。

---

### **javax.crypto 中的关键类**
- **`Cipher`**：执行加密和解密。
- **`KeyGenerator`**：生成对称密钥（例如，AES）。
- **`KeyPairGenerator`**：生成非对称密钥对（例如，RSA）。
- **`Mac`**：计算消息认证码。
- **`SecretKeyFactory`**：派生密钥（例如，从密码）。
- **`SecureRandom`**：生成加密安全的随机数。

---

### **最佳实践**
- **异常处理**：使用 try-catch 块处理异常，如 `NoSuchAlgorithmException`、`InvalidKeyException` 等。
- **密钥管理**：安全存储密钥（例如，在 `KeyStore` 中）并且永远不要硬编码它们。
- **算法选择**：使用安全算法（例如，AES-256、RSA-2048）和模式（例如，带 IV 的 CBC）。
- **提供者**：默认的 SunJCE 提供者足够，但你可以使用其他提供者（例如，BouncyCastle）通过 `Cipher.getInstance("AES", "BC")`。

---

### **结论**
要使用 `javax.crypto`，选择适合你需求的加密算法，生成或获取密钥，并利用类如 `Cipher`、`KeyGenerator` 和 `Mac` 执行操作。无论是使用 AES 对称加密数据、使用 RSA 非对称加密数据，还是使用 HMAC 确保完整性，`javax.crypto` 提供了工具——配合适当的初始化和安全密钥管理——在 Java 中实现强大的加密。