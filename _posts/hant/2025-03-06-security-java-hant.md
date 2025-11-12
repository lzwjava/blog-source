---
audio: false
generated: true
lang: hant
layout: post
title: Java 安全功能
translated: true
type: note
---

Java 中的 `java.security` 套件提供了實現應用程式安全功能的類別與介面。它屬於 Java 標準函式庫的一部分，包含密碼學運算、金鑰管理、安全隨機數生成、數位簽章及存取控制等工具。由於此套件涵蓋範圍廣泛，本文將概述其用途並透過實例示範如何使用。

### `java.security` 的用途為何？
`java.security` 套件是 Java 密碼學架構（JCA）的基礎組件，提供多種安全相關功能，例如：
- **密碼學運算**：資料雜湊處理（如使用 `MessageDigest`）、資料簽章（如使用 `Signature`）。
- **金鑰管理**：生成金鑰（如 `KeyPairGenerator`、`KeyGenerator`）及管理憑證（如 `KeyStore`）。
- **安全隨機數**：生成密碼學強度的隨機數（如 `SecureRandom`）。
- **存取控制**：定義與執行安全策略（如 `Permission`、`AccessController`）。

使用 `java.security` 時，通常需導入所需類別，並透過其 API 執行這些安全任務。

### 如何使用 `java.security`：逐步範例
讓我們透過常見用例來演示：使用 `java.security` 中的 `MessageDigest` 類別計算字串的 SHA-256 雜湊值。此範例將展示如何在實務中應用此套件。

#### 範例：計算 SHA-256 雜湊值
以下是完整程式碼片段，使用 SHA-256 對字串 "Hello, World!" 進行雜湊計算，並將結果以十六進位字串顯示：

```java
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.nio.charset.StandardCharsets;

public class HashExample {
    public static void main(String[] args) {
        try {
            // 步驟 1：取得 SHA-256 的 MessageDigest 實例
            MessageDigest digest = MessageDigest.getInstance("SHA-256");

            // 步驟 2：計算輸入字串的雜湊值
            byte[] hashBytes = digest.digest("Hello, World!".getBytes(StandardCharsets.UTF_8));

            // 步驟 3：將位元組陣列轉換為十六進位字串
            String hash = bytesToHex(hashBytes);

            // 步驟 4：輸出結果
            System.out.println("SHA-256 雜湊值: " + hash);
        } catch (NoSuchAlgorithmException e) {
            System.err.println("SHA-256 演算法不可用。");
        }
    }

    // 將位元組陣列轉換為十六進位字串的輔助方法
    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }
}
```

#### 程式碼解析
1. **導入陳述**：
   - `java.security.MessageDigest`：提供雜湊功能。
   - `java.security.NoSuchAlgorithmException`：當請求的演算法（如 "SHA-256"）不可用時拋出異常。
   - `java.nio.charset.StandardCharsets`：確保字串轉換為位元組時使用一致的字元編碼（UTF-8）。

2. **建立 MessageDigest 實例**：
   - `MessageDigest.getInstance("SHA-256")` 建立配置為使用 SHA-256 演算法的 `MessageDigest` 物件。

3. **計算資料雜湊值**：
   - `digest` 方法接收位元組陣列（透過 `getBytes(StandardCharsets.UTF_8)` 從字串轉換）並計算雜湊值，以位元組陣列形式傳回。

4. **轉換為十六進位格式**：
   - `bytesToHex` 輔助方法將原始位元組陣列轉換為可讀的十六進位字串。

5. **異常處理**：
   - 程式碼以 `try-catch` 區塊包裹，以處理 `NoSuchAlgorithmException`（雖然標準演算法中較少發生）。

執行此程式碼後，將輸出類似以下結果：
```
SHA-256 雜湊值: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```
此雜湊值是 SHA-256 為 "Hello, World!" 生成的唯一指紋。

### 使用 `java.security` 的通用步驟
雖然上述範例聚焦於 `MessageDigest`，但使用 `java.security` 中其他類別的方法也遵循類似模式：
1. **導入類別**：導入所需特定類別（如 `java.security.KeyPairGenerator`、`java.security.SecureRandom`）。
2. **實例化服務**：使用工廠方法（如 `getInstance`）建立實例（如 `KeyPairGenerator.getInstance("RSA")`）。
3. **配置與使用**：按需設定物件（如初始化金鑰長度）並呼叫其方法（如 `generateKeyPair()`）。
4. **處理異常**：以 `try-catch` 區塊包裹安全操作，管理如 `NoSuchAlgorithmException` 或 `InvalidKeyException` 等異常。
5. **保護敏感資料**：確保敏感資料（如金鑰、密碼）被謹慎處理，例如使用後從記憶體中清除。

### `java.security` 中其他常用類別
以下列出其他實用類別及其典型用途：
- **`SecureRandom`**：生成密碼學安全的隨機數。
  - 範例：`SecureRandom random = new SecureRandom(); byte[] bytes = new byte[16]; random.nextBytes(bytes);`
- **`KeyPairGenerator`**：為非對稱加密生成公開/私密金鑰對（如 RSA）。
  - 範例：`KeyPairGenerator gen = KeyPairGenerator.getInstance("RSA"); gen.initialize(2048); KeyPair pair = gen.generateKeyPair();`
- **`KeyStore`**：管理密碼學金鑰與憑證的儲存設施。
  - 範例：`KeyStore ks = KeyStore.getInstance("JKS"); ks.load(new FileInputStream("keystore.jks"), "password".toCharArray());`
- **`Signature`**：建立與驗證數位簽章。
  - 範例：`Signature sig = Signature.getInstance("SHA256withRSA"); sig.initSign(privateKey); sig.update(data); byte[] signature = sig.sign();`

### 關鍵注意事項
- **可用性**：`java.security` 套件包含於 Java 標準函式庫中（自 Java 9 起屬於 `java.base` 模組），無需外部依賴。
- **安全最佳實踐**：始終使用安全演算法（如以 SHA-256 取代 MD5）、處理異常時避免洩漏敏感資訊，並在使用後清除記憶體中的敏感資料。
- **擴充性**：如需進階功能，可將 `java.security` 與 `javax.crypto`（如用於加密/解密）或第三方函式庫（如 Bouncy Castle）結合使用。

本概述與範例應能為您在 Java 專案中使用 `java.security` 提供穩固的起點！