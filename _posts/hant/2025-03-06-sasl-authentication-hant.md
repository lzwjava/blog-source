---
audio: false
generated: true
lang: hant
layout: post
title: SASL 驗證在 Java 中
translated: true
---

要在 Java 中使用 `javax.security.sasl` 包，您需要利用其類別和介面來實現簡單身份驗證和安全層（SASL）機制，以進行客戶端和伺服器應用程序的身份驗證，並選擇性地進行數據安全。主要涉及的類別是 `Sasl`、`SaslClient` 和 `SaslServer`。以下是如何使用此包的全面指南，包括客戶端和伺服器實現的步驟和示例代碼。

---

### **javax.security.sasl 概述**
`javax.security.sasl` 包提供了一個用於 SASL 身份驗證的框架，通常用於 LDAP、IMAP 或自定義應用程序的協議。它包括：
- **`Sasl`**：一個包含靜態方法以創建 `SaslClient` 和 `SaslServer` 實例的實用類。
- **`SaslClient`**：表示 SASL 身份驗證過程的客戶端部分。
- **`SaslServer`**：表示 SASL 身份驗證過程的伺服器部分。
- **`CallbackHandler`**：您需要實現的介面，以處理身份驗證回調（例如，提供用戶名或密碼）。

該過程涉及創建 `SaslClient` 或 `SaslServer`，提供回調處理程序以管理身份驗證數據，並進行挑戰-應答交換，直到身份驗證完成。

---

### **使用 javax.security.sasl 的步驟**

#### **1. 確定您的角色（客戶端或伺服器）**
決定您的應用程序是作為客戶端（向伺服器進行身份驗證）還是作為伺服器（向客戶端進行身份驗證）。這決定了您是否使用 `SaslClient` 或 `SaslServer`。

#### **2. 選擇 SASL 機制**
SASL 支持各種機制，例如：
- `PLAIN`：簡單的用戶名/密碼身份驗證（無加密）。
- `DIGEST-MD5`：基於密碼的挑戰-應答。
- `GSSAPI`：基於 Kerberos 的身份驗證。

選擇客戶端和伺服器都支持的機制。為了簡化，本指南以 `PLAIN` 機制為例。

#### **3. 實現 CallbackHandler**
需要 `CallbackHandler` 來提供或驗證身份驗證憑證。您需要實現 `javax.security.auth.callback.CallbackHandler` 介面。

- **對於客戶端**：提供憑證，例如用戶名和密碼。
- **對於伺服器**：驗證客戶端憑證或提供伺服器端身份驗證數據。

以下是 `PLAIN` 機制的客戶端 `CallbackHandler` 示例：

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

對於伺服器，您可能會從數據庫中驗證憑證：

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // 從數據庫中檢索用戶名的預期密碼
            } else if (callback instanceof PasswordCallback) {
                // 設置用於驗證的預期密碼
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. 客戶端實現**
要作為客戶端進行身份驗證：

1. **創建 SaslClient**：
   使用 `Sasl.createSaslClient`，機制、協議、伺服器名稱、屬性和回調處理程序。

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // 可選；如果與身份驗證 ID 相同，則為 null
   String protocol = "ldap"; // 例如，"ldap"、"imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // 可選屬性，例如 QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **處理挑戰-應答交換**：
   - 檢查初始響應（在客戶端優先機制中常見，例如 `PLAIN`）。
   - 將響應發送到伺服器並處理挑戰，直到身份驗證完成。

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // 將響應發送到伺服器（協議特定，例如通過套接字或 LDAP BindRequest）
   }

   // 從伺服器接收挑戰（協議特定）
   byte[] challenge = /* 從伺服器讀取 */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // 將響應發送到伺服器
       if (sc.isComplete()) break;
       challenge = /* 從伺服器讀取下一個挑戰 */;
   }

   // 身份驗證完成；通過協議特定的方式檢查成功
   ```

   對於 `PLAIN`，客戶端在初始響應中發送憑證，伺服器通常在沒有進一步挑戰的情況下響應成功或失敗。

#### **5. 伺服器端實現**
要作為伺服器進行客戶端身份驗證：

1. **創建 SaslServer**：
   使用 `Sasl.createSaslServer`，機制、協議、伺服器名稱、屬性和回調處理程序。

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

2. **處理挑戰-應答交換**：
   - 處理客戶端的初始響應並生成挑戰，直到身份驗證完成。

   ```java
   byte[] response = /* 從客戶端讀取初始響應 */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // 將挑戰發送到客戶端（協議特定）

   while (!ss.isComplete()) {
       response = /* 從客戶端讀取下一個響應 */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // 身份驗證完成
           break;
       }
       // 將挑戰發送到客戶端
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // 繼續使用授權用戶
   }
   ```

   對於 `PLAIN`，伺服器在初始響應中驗證憑證並完成身份驗證，而不需要進一步的挑戰。

#### **6. 可選：使用安全層**
如果機制（例如 `DIGEST-MD5`）支持安全層：
- 在客戶端使用 `sc.wrap()` 和 `sc.unwrap()`，或在伺服器使用 `ss.wrap()` 和 `ss.unwrap()`，以在身份驗證後加密/解密消息。
- `PLAIN` 不支持安全層。

---

### **關鍵點**
- **整合**：將 SASL 交換嵌入到應用程序的通信協議中（例如，LDAP Bind 請求、IMAP AUTHENTICATE 命令）。
- **錯誤處理**：使用 try-catch 塊來處理 `SaslException` 和其他潛在錯誤。
- **屬性**：使用 `props` 映射來配置選項，例如保護質量（`"javax.security.sasl.qop"`），如果機制支持。

---

### **示例用例**
對於使用 `PLAIN` 的 LDAP 客戶端進行身份驗證：
1. 使用 `PLAIN` 機制創建 `SaslClient`。
2. 發送 LDAP `BindRequest`，機制和初始響應（`sc.evaluateChallenge(new byte[0])`）。
3. 處理伺服器的 `BindResponse` 以確認成功。

對於自定義協議，將 LDAP 特定步驟替換為您的協議的身份驗證命令。

---

通過遵循這些步驟，您可以有效地在 Java 應用程序中實現 SASL 身份驗證，並根據所選機制和協議進行定制。