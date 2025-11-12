---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的 SASL 認證
translated: true
type: note
---

要在 Java 中使用 `javax.security.sasl` 套件，您需要利用其類別和介面來實作簡單認證與安全層（SASL）機制，以實現用戶端-伺服器應用程式中的認證及可選的資料安全功能。主要涉及的類別包括 `Sasl`、`SaslClient` 和 `SaslServer`。以下是如何使用此套件的完整指南，包含用戶端與伺服器實作的步驟及範例程式碼。

---

### **javax.security.sasl 概覽**
`javax.security.sasl` 套件提供了一個 SASL 認證框架，常用於 LDAP、IMAP 等通訊協定或自訂應用程式中。其包含：
- **`Sasl`**：一個工具類別，提供建立 `SaslClient` 和 `SaslServer` 實例的靜態方法。
- **`SaslClient`**：代表 SASL 認證過程中的用戶端。
- **`SaslClient`**：代表 SASL 認證過程中的伺服器端。
- **`CallbackHandler`**：您需要實作的介面，用於處理認證回呼（例如提供使用者名稱或密碼）。

該過程包括建立 `SaslClient` 或 `SaslServer`、提供用於管理認證資料的回呼處理器，以及進行挑戰-回應交換直至認證完成。

---

### **使用 javax.security.sasl 的步驟**

#### **1. 確定您的角色（用戶端或伺服器）**
決定您的應用程式是作為用戶端（向伺服器進行認證）還是伺服器（對用戶端進行認證）。這將決定您使用 `SaslClient` 還是 `SaslServer`。

#### **2. 選擇 SASL 機制**
SASL 支援多種機制，例如：
- `PLAIN`：簡單的使用者名稱/密碼認證（無加密）。
- `DIGEST-MD5`：基於密碼的挑戰-回應機制。
- `GSSAPI`：基於 Kerberos 的認證。

選擇用戶端和伺服器均支援的機制。為簡化說明，本指南以 `PLAIN` 機制為例。

#### **3. 實作 CallbackHandler**
需要一個 `CallbackHandler` 來提供或驗證認證憑證。您需要實作 `javax.security.auth.callback.CallbackHandler` 介面。

- **對於用戶端**：提供如使用者名稱和密碼等憑證。
- **對於伺服器**：驗證用戶端憑證或提供伺服器端認證資料。

以下是用戶端 `CallbackHandler` 的範例，適用於 `PLAIN` 機制：

```java
import javax.security.auth.callback.*;
import java.io.IOException;

public class ClientCallbackHandler implements CallbackHandler {
    private final String username;
    private final String password;

    public ClientCallbackHandler(String username, String password) {
        this.username = username;
        this.password = password;
    }

    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                ((NameCallback) callback).setName(username);
            } else if (callback instanceof PasswordCallback) {
                ((PasswordCallback) callback).setPassword(password.toCharArray());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

對於伺服器，您可能需要根據資料庫驗證憑證：

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // 從資料庫中取得該使用者名稱的預期密碼
            } else if (callback instanceof PasswordCallback) {
                // 設定預期密碼以供驗證
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. 用戶端實作**
作為用戶端進行認證：

1. **建立 SaslClient**：
   使用 `Sasl.createSaslClient` 並指定機制、通訊協定、伺服器名稱、屬性和回呼處理器。

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // 可選；若與認證 ID 相同則為 null
   String protocol = "ldap"; // 例如 "ldap"、"imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // 可選屬性，例如 QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **處理挑戰-回應交換**：
   - 檢查是否有初始回應（在如 `PLAIN` 這類用戶端優先的機制中常見）。
   - 向伺服器傳送回應並處理挑戰，直至認證完成。

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // 將回應傳送給伺服器（依通訊協定而定，例如透過 socket 或 LDAP BindRequest）
   }

   // 接收伺服器挑戰（依通訊協定而定）
   byte[] challenge = /* 從伺服器讀取 */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // 將回應傳送給伺服器
       if (sc.isComplete()) break;
       challenge = /* 從伺服器讀取下一個挑戰 */;
   }

   // 認證完成；透過通訊協定特定方式檢查是否成功
   ```

   對於 `PLAIN` 機制，用戶端會在初始回應中傳送憑證，伺服器通常會回應成功或失敗，無需進一步挑戰。

#### **5. 伺服器端實作**
作為伺服器對用戶端進行認證：

1. **建立 SaslServer**：
   使用 `Sasl.createSaslServer` 並指定機制、通訊協定、伺服器名稱、屬性和回呼處理器。

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslServer;
   import java.util.HashMap;

   String mechanism = "PLAIN";
   String protocol = "ldap";
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null;
   CallbackHandler cbh = new ServerCallbackHandler();

   SaslServer ss = Sasl.createSaslServer(mechanism, protocol, serverName, props, cbh);
   ```

2. **處理挑戰-回應交換**：
   - 處理用戶端的初始回應並產生挑戰，直至認證完成。

   ```java
   byte[] response = /* 從用戶端讀取初始回應 */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // 將挑戰傳送給用戶端（依通訊協定而定）

   while (!ss.isComplete()) {
       response = /* 從用戶端讀取下一個回應 */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // 認證完成
           break;
       }
       // 將挑戰傳送給用戶端
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // 以授權使用者身份繼續進行
   }
   ```

   對於 `PLAIN` 機制，伺服器會在初始回應中驗證憑證，並在無需額外挑戰的情況下完成認證。

#### **6. 可選：使用安全層**
如果機制（例如 `DIGEST-MD5`）支援安全層：
- 在用戶端使用 `sc.wrap()` 和 `sc.unwrap()`，或在伺服器使用 `ss.wrap()` 和 `ss.unwrap()`，以在認證後加密/解密訊息。
- `PLAIN` 不支援安全層。

---

### **關鍵要點**
- **整合**：將 SASL 交換嵌入到您的應用程式通訊協定中（例如 LDAP Bind 請求、IMAP AUTHENTICATE 指令）。
- **錯誤處理**：使用 try-catch 區塊包裝程式碼，以處理 `SaslException` 和其他潛在錯誤。
- **屬性**：使用 `props` 映射來配置選項，例如保護品質（`"javax.security.sasl.qop"`），如果機制支援的話。

---

### **範例使用情境**
對於使用 `PLAIN` 機制進行認證的 LDAP 用戶端：
1. 使用 `PLAIN` 機制建立 `SaslClient`。
2. 傳送帶有機制和初始回應（`sc.evaluateChallenge(new byte[0])`）的 LDAP `BindRequest`。
3. 處理伺服器的 `BindResponse` 以確認成功。

對於自訂通訊協定，請將 LDAP 特定步驟替換為您的通訊協定認證指令。

---

透過遵循這些步驟，您可以有效地使用 `javax.security.sasl` 在 Java 應用程式中實作 SASL 認證，並根據所選機制和通訊協定自訂過程。