---
audio: false
generated: true
lang: hant
layout: post
title: Java JWT 程式庫
translated: true
type: note
---

要在 Java 中使用 `com.nimbusds.jwt` 函式庫從 JSON Web Token (JWT) 中提取過期時間、簽發時間及其他聲明（claims）等資訊，請遵循以下步驟。本解決方案假設您正在處理已簽名的 JWT（這是最常見的類型），並著重於提供清晰實用的方法來達成目標。

---

## 前置準備

首先，請確保您的專案中已加入 Nimbus JOSE + JWT 函式庫。若您使用 Maven，請在 `pom.xml` 中加入以下依賴項：

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- 請替換為最新版本 -->
</dependency>
```

您可以在 [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) 上查看最新版本。

---

## 提取過期時間、簽發時間及其他聲明的步驟

以下是使用 `com.nimbusds.jwt` 函式庫解析 JWT 並獲取過期時間、簽發時間及其他聲明的方法：

1. **解析 JWT 字串**：使用 `SignedJWT.parse()` 方法將 JWT 字串轉換為 `SignedJWT` 物件。
2. **取得聲明集**：透過 `getJWTClaimsSet()` 從 JWT 中存取聲明（鍵值對）。
3. **提取特定聲明**：
   - 使用 `getExpirationTime()` 獲取過期時間（`exp` 聲明）。
   - 使用 `getIssueTime()` 獲取簽發時間（`iat` 聲明）。
   - 使用 `getSubject()`、`getClaim()` 或其他方法獲取其他聲明。
4. **錯誤處理**：將解析邏輯包裝在 try-catch 區塊中，以處理可能的解析問題。

---

## 範例程式碼

以下是一個完整的 Java 範例，展示如何從 JWT 中提取過期時間、簽發時間及一個額外的聲明（例如主題）：

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // 請將此處替換為您的實際 JWT 字串
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // 步驟 1：解析 JWT 字串
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // 步驟 2：取得聲明集
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // 步驟 3：提取過期時間和簽發時間
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // 其他聲明的範例

            // 步驟 4：顯示結果
            if (expirationDate != null) {
                System.out.println("過期時間: " + expirationDate);
            } else {
                System.out.println("未設定過期時間。");
            }

            if (issuedDate != null) {
                System.out.println("簽發時間: " + issuedDate);
            } else {
                System.out.println("未設定簽發時間。");
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
- `SignedJWT`：代表已簽名的 JWT，並提供解析和處理的方法。
- `JWTClaimsSet`：包含 JWT 承載中的聲明。
- `ParseException`：若 JWT 字串格式錯誤或無法解析時拋出。
- `Date`：用於表示過期時間和簽發時間。

### 2. **解析 JWT**
- `SignedJWT.parse(jwtString)` 方法接收 JWT 字串（例如 `header.payload.signature`）並返回一個 `SignedJWT` 物件。若 JWT 無效，則拋出 `ParseException`。

### 3. **存取聲明**
- `signedJWT.getJWTClaimsSet()` 獲取聲明集，其中包含 JWT 承載中的所有聲明。

### 4. **提取特定聲明**
- **`getExpirationTime()`**：將 `exp` 聲明作為 `Date` 物件返回（若不存在則返回 `null`）。這代表令牌的過期時間。
- **`getIssueTime()`**：將 `iat` 聲明作為 `Date` 物件返回（若不存在則返回 `null`）。這表示令牌的簽發時間。
- **`getSubject()`**：將 `sub` 聲明作為 `String` 返回（若不存在則返回 `null`），這是另一個標準聲明的範例。您也可以使用 `getClaim("key")` 來獲取自訂聲明作為 `Object`。

### 5. **錯誤處理**
- try-catch 區塊確保若 JWT 格式錯誤或無效，程式能透過輸出錯誤訊息優雅地處理錯誤。

---

## 注意事項

- **已簽名與未簽名的 JWT**：本範例使用 `SignedJWT` 處理已簽名的令牌。若您有未簽名的 JWT，請改用 `PlainJWT.parse(jwtString)`。若需更通用的方法，您可以使用 `JWTParser.parse(jwtString)`，然後使用 instanceof 檢查類型（`SignedJWT`、`PlainJWT` 等）。
- **簽名驗證**：此程式碼未驗證 JWT 的簽名。在生產環境中，您應使用 `signedJWT.verify(verifier)` 並搭配適當的金鑰來驗證簽名，以確保令牌的真實性。
- **空值檢查**：提取聲明時請務必檢查 `null`，因為它們是選填的，且可能不存在於每個 JWT 中。
- **自訂聲明**：要存取非標準聲明，請使用 `claimsSet.getClaim("claimName")`，它會返回一個 `Object`，您可以將其轉換為適當的類型（例如 `String`、`Integer`）。

---

## 範例輸出

對於上述範例 JWT 字串：
```
過期時間: Wed Jan 17 19:52:02 UTC 2018
簽發時間: Wed Jan 17 19:50:22 UTC 2018
主題: 1234567890
```

---

此方法提供了一種簡單有效的方式，使用 `com.nimbusds.jwt` 函式庫從 JWT 中提取過期時間、簽發時間及其他聲明。請將 `jwtString` 替換為您自己的令牌，並根據您的具體需求調整程式碼！