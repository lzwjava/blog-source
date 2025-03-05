---
audio: false
generated: true
lang: ja
layout: post
title: 暗号学のJava
translated: true
---

`javax.crypto` パッケージは、Javaで暗号化操作を行うためのクラスとメソッドのセットを提供します。暗号化、復号化、キー生成、メッセージ認証などの操作が含まれます。以下は、`javax.crypto` の使用方法の包括的なガイドです。説明と実用的な例を含み、対称暗号化、非対称暗号化、メッセージ認証などの一般的な使用例について説明します。

---

### **javax.cryptoとは？**
`javax.crypto` パッケージは、Java Cryptography Architecture (JCA) の一部であり、暗号化を通じて安全な通信を実装するためのツールを提供します。以下をサポートします：
- **対称暗号化**：暗号化と復号化に同じキーを使用します（例：AES、DES）。
- **非対称暗号化**：公開/秘密キーペアを使用します（例：RSA）。
- **メッセージ認証**：データの整合性と真正性を確保します（例：HMAC）。
- **キー生成と管理**：暗号化キーを作成および管理するためのツール。

`javax.crypto` を使用するには、以下の手順を実行します：
1. 暗号化アルゴリズムを選択します。
2. 必要なキーを生成または取得します。
3. 提供されるクラス（例：`Cipher`、`KeyGenerator`、`Mac`）を使用して操作を行います。

以下に、一般的なシナリオの手順別の例を示します。

---

### **1. AESを使用した対称暗号化**
対称暗号化は、暗号化と復号化に同じキーを使用します。以下に、AES（Advanced Encryption Standard）を使用して文字列を暗号化および復号化する方法を示します。`Cipher` クラスをCBCモードでPKCS5パディングを使用して実装します。

#### **手順**
- 秘密キーを生成します。
- `Cipher` インスタンスを作成および初期化します。
- データを暗号化および復号化します。

#### **例コード**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 手順 1: AES用の秘密キーを生成
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128ビットキー
        SecretKey secretKey = keyGen.generateKey();

        // 手順 2: 乱数の初期化ベクトル（IV）を生成
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AESブロックサイズは16バイト
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // 手順 3: 暗号化用にCipherを作成および初期化
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // 手順 4: データを暗号化
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // 手順 5: 同じIVを使用してCipherを復号化モードで初期化
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 結果を出力
        System.out.println("オリジナル: " + plaintext);
        System.out.println("復号化された: " + decryptedText);
    }
}
```

#### **重要なポイント**
- **アルゴリズム**：`"AES/CBC/PKCS5Padding"` は、ブロックサイズの倍数でないデータを処理するためにパディングを使用するCBCモードのAESを指定します。
- **IV**：暗号化に対してはランダムで、復号化に対しては再利用する必要があります。通常、暗号文にプレフィックスとして追加されるか、別途伝送されます。
- **キー管理**：実際のアプリケーションでは、受信者と安全に`secretKey`を共有します。

---

### **2. RSAを使用した非対称暗号化**
非対称暗号化は、公開キーを使用して暗号化し、秘密キーを使用して復号化します。以下に、RSAを使用する例を示します。

#### **手順**
- 公開/秘密キーペアを生成します。
- 公開キーで暗号化します。
- 秘密キーで復号化します。

#### **例コード**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // 手順 1: RSAキーペアを生成
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048ビットキー
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // 手順 2: 公開キーで暗号化
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // 手順 3: 秘密キーで復号化
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 結果を出力
        System.out.println("オリジナル: " + plaintext);
        System.out.println("復号化された: " + decryptedText);
    }
}
```

#### **重要なポイント**
- **サイズ制限**：RSAは、キーサイズ（例：2048ビットキーの場合、約245バイト）より小さいデータのみ暗号化できます。より大きなデータについては、ハイブリッド暗号化（データを対称キーで暗号化し、そのキーをRSAで暗号化）を使用します。
- **キー配布**：公開キーは公開して構いませんが、秘密キーは秘密に保持します。

---

### **3. HMACを使用したメッセージ認証**
メッセージ認証コード（MAC）は、データの整合性と真正性を確保します。以下に、`Mac` を使用してHMAC-SHA256を実装する方法を示します。

#### **例コード**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // 手順 1: 秘密キーを作成
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // 手順 2: キーでMacを初期化
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // 手順 3: データのMACを計算
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // 結果を出力
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **重要なポイント**
- **検証**：受信者は同じキーとデータでMACを再計算し、一致するかどうかを確認します。一致する場合、データは真正で変更されていません。
- **キー**：事前に安全に共有された共有秘密キーを使用します。

---

### **4. ストリームの暗号化/復号化**
大量のデータ（例：ファイル）については、`CipherInputStream` または `CipherOutputStream` を使用します。

#### **例コード（ファイルの暗号化）**
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
        // キーとIVを生成
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);
        SecretKey secretKey = keyGen.generateKey();
        byte[] iv = new byte[16];
        new SecureRandom().nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // Cipherを初期化
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // ファイルを暗号化
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

#### **重要なポイント**
- **ストリーム**：暗号化には `CipherOutputStream` を、復号化には `CipherInputStream` を使用してデータを増分的に処理します。
- **IVの処理**：IVを暗号化されたファイルと一緒に保存します（例：プレフィックスとして追加）。

---

### **5. パスワードベースの暗号化（PBE）**
`SecretKeyFactory` を使用してパスワードからキーを導出します。

#### **例コード**
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
        // パスワードとソルト
        char[] password = "mysecretpassword".toCharArray();
        byte[] salt = new byte[16];
        new SecureRandom().nextBytes(salt);

        // パスワードからキーを導出
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256ビットキー
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // 導出されたキーで暗号化
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("暗号化された: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **重要なポイント**
- **ソルト**：キー導出をランダム化し、暗号化されたデータと一緒に保存します。
- **反復回数**：暴力攻撃を防ぐために計算コストを増加させます（例：10,000）。

---

### **javax.cryptoの主要クラス**
- **`Cipher`**：暗号化と復号化を実行します。
- **`KeyGenerator`**：対称キー（例：AES）を生成します。
- **`KeyPairGenerator`**：非対称キーペア（例：RSA）を生成します。
- **`Mac`**：メッセージ認証コードを計算します。
- **`SecretKeyFactory`**：キーを導出します（例：パスワードから）。
- **`SecureRandom`**：暗号化的に安全な乱数を生成します。

---

### **ベストプラクティス**
- **例外処理**：`NoSuchAlgorithmException`、`InvalidKeyException` などの例外を処理するために、コードをtry-catchブロックでラップします。
- **キー管理**：キーを安全に保存します（例：`KeyStore` に）し、決してハードコードしないでください。
- **アルゴリズムの選択**：安全なアルゴリズム（例：AES-256、RSA-2048）とモード（例：IV付きのCBC）を使用します。
- **プロバイダー**：デフォルトのSunJCEプロバイダーが十分ですが、他のプロバイダー（例：BouncyCastle）を使用することもできます（例：`Cipher.getInstance("AES", "BC")`）。

---

### **まとめ**
`javax.crypto` を使用するには、必要な暗号化アルゴリズムを選択し、キーを生成または取得し、`Cipher`、`KeyGenerator`、`Mac` などのクラスを使用して操作を行います。AESで対称的に暗号化するか、RSAで非対称的に暗号化するか、HMACで整合性を確保するか、`javax.crypto` は適切な初期化と安全なキー管理を組み合わせることで、Javaで強力な暗号化を実装するためのツールを提供します。