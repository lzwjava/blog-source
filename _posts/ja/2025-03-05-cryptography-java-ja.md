---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおける暗号化
translated: true
type: note
---

Javaの`javax.crypto`パッケージは、暗号化、復号、鍵生成、メッセージ認証などの暗号操作を実行するための一連のクラスとメソッドを提供します。以下は、対称暗号、非対称暗号、メッセージ認証などの一般的なユースケースの説明と実践的な例を含む、`javax.crypto`の使用方法に関する包括的なガイドです。

---

### **javax.cryptoとは？**
`javax.crypto`パッケージは、Java Cryptography Architecture (JCA) の一部であり、暗号化を通じて安全な通信を実装するためのツールを提供します。以下の機能をサポートします：
- **対称暗号**：暗号化と復号に同じ鍵を使用します（例：AES、DES）。
- **非対称暗号**：公開鍵/秘密鍵のペアを使用します（例：RSA）。
- **メッセージ認証**：データの完全性と真正性を保証します（例：HMAC）。
- **鍵生成と管理**：暗号鍵を作成し扱うためのツール。

`javax.crypto`を使用するには、以下の手順が必要です：
1. 暗号アルゴリズムを選択します。
2. 必要な鍵を生成または取得します。
3. 提供されているクラス（例：`Cipher`、`KeyGenerator`、`Mac`）を使用して操作を実行します。

以下に、一般的なシナリオに対するステップバイステップの例を示します。

---

### **1. AESによる対称暗号化**
対称暗号化は、暗号化と復号の両方に単一の鍵を使用します。以下は、CBCモードとPKCS5パディングを使用したAES（Advanced Encryption Standard）と`Cipher`クラスを使って文字列を暗号化および復号する方法です。

#### **手順**
- 秘密鍵を生成します。
- `Cipher`インスタンスを作成し初期化します。
- データを暗号化および復号します。

#### **コード例**
```java
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.security.SecureRandom;
import java.nio.charset.StandardCharsets;

public class SymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // ステップ1: AES用の秘密鍵を生成
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128); // 128ビット鍵
        SecretKey secretKey = keyGen.generateKey();

        // ステップ2: ランダムな初期化ベクトル(IV)を生成
        SecureRandom random = new SecureRandom();
        byte[] iv = new byte[16]; // AESブロックサイズは16バイト
        random.nextBytes(iv);
        IvParameterSpec ivSpec = new IvParameterSpec(iv);

        // ステップ3: 暗号化用のCipherを作成し初期化
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, ivSpec);

        // ステップ4: データを暗号化
        String plaintext = "Hello, World!";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // ステップ5: 同じIVを使用して復号用のCipherを初期化
        cipher.init(Cipher.DECRYPT_MODE, secretKey, ivSpec);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 結果を出力
        System.out.println("Original: " + plaintext);
        System.out.println("Decrypted: " + decryptedText);
    }
}
```

#### **重要なポイント**
- **アルゴリズム**: `"AES/CBC/PKCS5Padding"`は、CBCモードとブロックサイズの倍数でないデータを扱うためのパディングを使用するAESを指定します。
- **IV**: 初期化ベクトルは暗号化時にランダムである必要があり、復号時に再利用する必要があります。通常、暗号文の先頭に付加するか、別途送信します。
- **鍵管理**: 実際のアプリケーションでは、`secretKey`を受信者と安全に共有してください。

---

### **2. RSAによる非対称暗号化**
非対称暗号化は、公開鍵で暗号化し、秘密鍵で復号します。以下はRSAを使用した例です。

#### **手順**
- 公開鍵/秘密鍵のペアを生成します。
- 公開鍵で暗号化します。
- 秘密鍵で復号します。

#### **コード例**
```java
import javax.crypto.Cipher;
import java.security.KeyPair;
import java.security.KeyPairGenerator;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.nio.charset.StandardCharsets;

public class AsymmetricEncryptionExample {
    public static void main(String[] args) throws Exception {
        // ステップ1: RSA鍵ペアを生成
        KeyPairGenerator keyPairGen = KeyPairGenerator.getInstance("RSA");
        keyPairGen.initialize(2048); // 2048ビット鍵
        KeyPair keyPair = keyPairGen.generateKeyPair();
        PublicKey publicKey = keyPair.getPublic();
        PrivateKey privateKey = keyPair.getPrivate();

        // ステップ2: 公開鍵で暗号化
        Cipher cipher = Cipher.getInstance("RSA");
        cipher.init(Cipher.ENCRYPT_MODE, publicKey);
        String plaintext = "Secret Message";
        byte[] plaintextBytes = plaintext.getBytes(StandardCharsets.UTF_8);
        byte[] ciphertext = cipher.doFinal(plaintextBytes);

        // ステップ3: 秘密鍵で復号
        cipher.init(Cipher.DECRYPT_MODE, privateKey);
        byte[] decryptedBytes = cipher.doFinal(ciphertext);
        String decryptedText = new String(decryptedBytes, StandardCharsets.UTF_8);

        // 結果を出力
        System.out.println("Original: " + plaintext);
        System.out.println("Decrypted: " + decryptedText);
    }
}
```

#### **重要なポイント**
- **サイズ制限**: RSAは鍵サイズよりも小さいデータしか暗号化できません（例：2048ビット鍵で約245バイト）。より大きなデータには、ハイブリッド暗号（データを対称鍵で暗号化し、その鍵をRSAで暗号化する）を使用してください。
- **鍵配布**: 公開鍵は公開して共有し、秘密鍵は秘密に保持してください。

---

### **3. HMACによるメッセージ認証**
メッセージ認証コード（MAC）は、データの完全性と真正性を保証します。以下は、`Mac`をHMAC-SHA256で使用する方法です。

#### **コード例**
```java
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class MacExample {
    public static void main(String[] args) throws Exception {
        // ステップ1: 秘密鍵を作成
        String secret = "mysecretkey";
        SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");

        // ステップ2: 鍵でMacを初期化
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKey);

        // ステップ3: データのMACを計算
        String data = "Data to authenticate";
        byte[] macValue = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
        String macBase64 = Base64.getEncoder().encodeToString(macValue);

        // 結果を出力
        System.out.println("MAC: " + macBase64);
    }
}
```

#### **重要なポイント**
- **検証**: 受信者は同じ鍵とデータでMACを再計算します。一致すれば、データは真正で改ざんされていません。
- **鍵**: 事前に安全に配布された共有秘密鍵を使用してください。

---

### **4. ストリームの暗号化/復号**
大きなデータ（例：ファイル）には、`CipherInputStream`または`CipherOutputStream`を使用します。

#### **コード例（ファイルの暗号化）**
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
        // 鍵とIVを生成
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
- **ストリーム**: データをインクリメンタルに処理するには、暗号化に`CipherOutputStream`を、復号に`CipherInputStream`を使用します。
- **IVの取り扱い**: IVは暗号化されたファイルと共に保存してください（例：先頭に付加する）。

---

### **5. パスワードベースの暗号化（PBE）**
`SecretKeyFactory`を使用してパスワードから鍵を導出します。

#### **コード例**
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

        // パスワードから鍵を導出
        PBEKeySpec pbeKeySpec = new PBEKeySpec(password, salt, 10000, 256); // 256ビット鍵
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        SecretKey tempKey = factory.generateSecret(pbeKeySpec);
        SecretKey secretKey = new SecretKeySpec(tempKey.getEncoded(), "AES");

        // 導出された鍵で暗号化
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        String plaintext = "Hello from PBE";
        byte[] ciphertext = cipher.doFinal(plaintext.getBytes(StandardCharsets.UTF_8));

        System.out.println("Encrypted: " + Base64.getEncoder().encodeToString(ciphertext));
    }
}
```

#### **重要なポイント**
- **ソルト**: 鍵導出をランダム化します。暗号化されたデータと共に保存してください。
- **反復回数**: ブルートフォース攻撃を防ぐために計算コストを増加させます（例：10,000回）。

---

### **javax.cryptoの主要なクラス**
- **`Cipher`**: 暗号化と復号を実行します。
- **`KeyGenerator`**: 対称鍵（例：AES）を生成します。
- **`KeyPairGenerator`**: 非対称鍵ペア（例：RSA）を生成します。
- **`Mac`**: メッセージ認証コードを計算します。
- **`SecretKeyFactory`**: （パスワードなどから）鍵を導出します。
- **`SecureRandom`**: 暗号的に安全な乱数を生成します。

---

### **ベストプラクティス**
- **例外処理**: `NoSuchAlgorithmException`、`InvalidKeyException`などの例外に対して、コードをtry-catchブロックで囲んでください。
- **鍵管理**: 鍵は安全に（例：`KeyStore`内に）保存し、決してハードコードしないでください。
- **アルゴリズムの選択**: 安全なアルゴリズム（例：AES-256、RSA-2048）とモード（例：IV付きCBC）を使用してください。
- **プロバイダ**: デフォルトのSunJCEプロバイダで十分ですが、`Cipher.getInstance("AES", "BC")`のように他のプロバイダ（例：BouncyCastle）も使用できます。

---

### **結論**
`javax.crypto`を使用するには、ニーズに合った適切な暗号アルゴリズムを選択し、鍵を生成または取得し、`Cipher`、`KeyGenerator`、`Mac`などのクラスを活用して操作を実行します。AESで対称的にデータを暗号化する場合でも、RSAで非対称的に暗号化する場合でも、HMACで完全性を保証する場合でも、`javax.crypto`はツールを提供します。適切な初期化と安全な鍵管理と組み合わせることで、Javaで堅牢な暗号化を実装できます。