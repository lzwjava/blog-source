---
audio: false
generated: true
lang: hant
layout: post
title: Java JWT 程式庫
translated: true
---

使用 `com.nimbusds.jwt` 圖書館在 Java 中提取 JSON Web Token (JWT) 的過期日期、簽發日期及其他聲明，請按照以下步驟進行。這個解決方案假設您正在處理簽名 JWT，這是最常見的類型，並專注於提供一個清晰、實際的方法來實現您的目標。

---

## 先決條件

首先，確保您已將 Nimbus JOSE + JWT 圖書館添加到您的項目中。如果您使用 Maven，請在 `pom.xml` 中包含以下依賴項：

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- 替換為最新版本 -->
</dependency>
```

您可以在 [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) 查看最新版本。

---

## 提取過期日期、簽發日期及其他聲明的步驟

以下是如何使用 `com.nimbusds.jwt` 圖書館解析 JWT 並檢索過期日期、簽發日期及其他聲明的方法：

1. **解析 JWT 字串**：使用 `SignedJWT.parse()` 方法將 JWT 字串轉換為 `SignedJWT` 物件。
2. **獲取聲明集**：使用 `getJWTClaimsSet()` 從 JWT 中訪問聲明（鍵值對）。
3. **提取特定聲明**：
   - 使用 `getExpirationTime()` 獲取過期日期（`exp` 聲明）。
   - 使用 `getIssueTime()` 獲取簽發日期（`iat` 聲明）。
   - 使用 `getSubject()`、`getClaim()` 或其他方法獲取其他聲明。
4. **處理錯誤**：將解析邏輯包裹在 try-catch 塊中以管理潛在的解析問題。

---

## 範例程式碼

以下是完整的 Java 範例，展示如何從 JWT 提取過期日期、簽發日期及其他聲明（例如主題）：

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // 替換為您的實際 JWT 字串
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // 步驟 1：解析 JWT 字串
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // 步驟 2：獲取聲明集
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // 步驟 3：提取過期和簽發日期
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // 另一個聲明的範例

            // 步驟 4：顯示結果
            if (expirationDate != null) {
                System.out.println("過期日期: " + expirationDate);
            } else {
                System.out.println("未設定過期日期。");
            }

            if (issuedDate != null) {
                System.out.println("簽發日期: " + issuedDate);
            } else {
                System.out.println("未設定簽發日期。");
            }

            if (subject != null) {
                System.out.println("主題: " + subject);
            } else {
                System.out.println("未設定主題。");
            }

        } catch (ParseException e) {
            System.out.println("無效的 JWT: " + e.getMessage());
        }
    }
}
```

---

## 程式碼說明

### 1. **匯入**
- `SignedJWT`：表示簽名 JWT 並提供解析和處理它的方法。
- `JWTClaimsSet`：包含 JWT 裝載中的聲明。
- `ParseException`：如果 JWT 字串格式不正確或無法解析，則拋出。
- `Date`：用於表示過期和簽發時間。

### 2. **解析 JWT**
- `SignedJWT.parse(jwtString)` 方法接受 JWT 字串（例如 `header.payload.signature`）並返回 `SignedJWT` 物件。如果 JWT 無效，則拋出 `ParseException`。

### 3. **訪問聲明**
- `signedJWT.getJWTClaimsSet()` 檢索聲明集，其中包含 JWT 裝載中的所有聲明。

### 4. **提取特定聲明**
- **`getExpirationTime()`**：以 `Date` 物件返回 `exp` 聲明（或 `null` 如果不存在）。這表示令牌過期的時間。
- **`getIssueTime()`**：以 `Date` 物件返回 `iat` 聲明（或 `null` 如果不存在）。這表示令牌簽發的時間。
- **`getSubject()`**：以 `String` 返回 `sub` 聲明（或 `null` 如果不存在），這是另一個標準聲明的範例。您也可以使用 `getClaim("key")` 以 `Object` 形式檢索自訂聲明。

### 5. **錯誤處理**
- try-catch 塊確保如果 JWT 格式不正確或無效，程式會優雅地處理錯誤並打印錯誤訊息。

---

## 註解

- **簽名 vs. 未簽名 JWT**：這個範例使用 `SignedJWT` 來處理簽名令牌。如果您有未簽名的 JWT，請使用 `PlainJWT.parse(jwtString)`。對於更通用的方法，您可以使用 `JWTParser.parse(jwtString)`，然後使用 `instanceof` 檢查類型（`SignedJWT`、`PlainJWT` 等）。
- **簽名驗證**：這段程式碼不會驗證 JWT 的簽名。在生產環境中，您應該使用 `signedJWT.verify(verifier)` 和適當的鍵來驗證令牌的真實性。
- **空檢查**：在檢索聲明時，始終檢查 `null`，因為它們是可選的，可能不存在於每個 JWT 中。
- **自訂聲明**：要訪問非標準聲明，請使用 `claimsSet.getClaim("claimName")`，它以 `Object` 形式返回，您可以將其轉換為適當的類型（例如 `String`、`Integer`）。

---

## 範例輸出

對於上述範例 JWT 字串：
```
過期日期: 2018 年 1 月 17 日 19:52:02 UTC
簽發日期: 2018 年 1 月 17 日 19:50:22 UTC
主題: 1234567890
```

---

這種方法提供了一種簡單且有效的方法來使用 `com.nimbusds.jwt` 圖書館從 JWT 提取過期日期、簽發日期及其他聲明。請用您自己的令牌替換 `jwtString`，並根據您的具體需求調整程式碼！