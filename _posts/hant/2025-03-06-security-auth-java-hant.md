---
audio: false
generated: true
lang: hant
layout: post
title: Java 中的認證與授權
translated: true
type: note
---

要在 Java 中使用 `javax.security.auth` 套件，您需要了解它是 Java 認證與授權服務（JAAS）框架的一部分。此套件提供了用於驗證使用者（確認其身分）和授權（決定其可執行操作）的類別與介面。以下將逐步說明如何在基本驗證情境（例如使用使用者名稱和密碼驗證使用者）中使用 `javax.security.auth`。

---

### **核心概念概述**
在深入步驟之前，先簡要說明 `javax.security.auth` 中的核心元件：

- **Subject**：代表正在被驗證的實體（例如使用者或服務）。它可以擁有多個身分（Principals）和憑證（例如密碼或憑證）。
- **Principal**：與 Subject 關聯的身分或角色，例如使用者名稱或群組成員資格。
- **Credential**：用於驗證 Subject 的資訊，例如密碼或加密金鑰。
- **LoginModule**：可外掛的元件，負責執行驗證邏輯（例如檢查使用者名稱和密碼是否與資料庫中的相符）。
- **LoginContext**：核心類別，用於協調使用一個或多個 LoginModules 的驗證過程。
- **CallbackHandler**：用於與使用者互動的介面，例如提示輸入使用者名稱和密碼。

了解這些概念後，我們來探討如何使用此套件。

---

### **使用 `javax.security.auth` 的步驟**

#### **1. 設定 JAAS 配置**
驗證過程依賴於指定要使用哪些 `LoginModule` 的配置。這可以透過配置檔案或程式方式定義。

例如，建立一個名為 `jaas.config` 的檔案，內容如下：

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**：應用程式或上下文的名稱，您將在程式碼中引用此名稱。
- **`com.example.MyLoginModule`**：您自訂 `LoginModule` 的完整限定名稱（稍後將實作此模組）。
- **`required`**：標誌，表示此模組必須成功才能通過驗證。其他標誌包括 `requisite`、`sufficient` 和 `optional`，這些標誌允許使用多個模組建立更複雜的邏輯。

設定系統屬性以指向此檔案：

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

或者，您也可以透過程式方式設定配置，但對於大多數情況，使用檔案更為簡單。

#### **2. 實作 CallbackHandler**
`CallbackHandler` 用於收集使用者的輸入，例如使用者名稱和密碼。以下是一個使用控制台的簡單實作：

```java
import javax.security.auth.callback.*;
import java.io.*;

public class MyCallbackHandler implements CallbackHandler {
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                NameCallback nc = (NameCallback) callback;
                System.out.print(nc.getPrompt());
                nc.setName(System.console().readLine());
            } else if (callback instanceof PasswordCallback) {
                PasswordCallback pc = (PasswordCallback) callback;
                System.out.print(pc.getPrompt());
                pc.setPassword(System.console().readPassword());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

- **NameCallback**：提示並取得使用者名稱。
- **PasswordCallback**：提示並取得密碼（以 `char[]` 形式儲存以確保安全）。

#### **3. 實作 LoginModule**
`LoginModule` 定義了驗證邏輯。以下是一個基本範例，檢查硬編碼的使用者名稱和密碼（在實際應用中，您應使用資料庫或外部服務）：

```java
import javax.security.auth.*;
import javax.security.auth.callback.*;
import javax.security.auth.login.*;
import javax.security.auth.spi.*;
import java.security.Principal;
import java.util.*;

public class MyLoginModule implements LoginModule {
    private Subject subject;
    private CallbackHandler callbackHandler;
    private boolean succeeded = false;

    // 初始化模組
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // 執行驗證
    public boolean login() throws LoginException {
        if (callbackHandler == null) {
            throw new LoginException("No callback handler provided");
        }

        try {
            NameCallback nameCallback = new NameCallback("Username: ");
            PasswordCallback passwordCallback = new PasswordCallback("Password: ", false);
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});

            String username = nameCallback.getName();
            char[] password = passwordCallback.getPassword();

            // 硬編碼檢查（在實際應用中請替換為真實邏輯）
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Authentication failed");
            }
        } catch (Exception e) {
            throw new LoginException("Login error: " + e.getMessage());
        }
    }

    // 提交驗證（將 Principals 加入 Subject）
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // 中止驗證過程
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // 登出 Subject
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// 簡單的 Principal 實作
class MyPrincipal implements Principal {
    private String name;

    public MyPrincipal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

- **login()**：使用 `CallbackHandler` 取得憑證並進行檢查。
- **commit()**：如果驗證成功，將 `Principal` 加入 `Subject`。
- **abort()** 和 **logout()**：處理清理或取消操作。

#### **4. 使用 LoginContext 進行驗證**
現在，在您的主應用程式中使用 `LoginContext` 來執行驗證：

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // 確保 JAAS 配置已設定
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // 使用配置名稱和 CallbackHandler 建立 LoginContext
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // 執行驗證
            lc.login();

            // 取得已驗證的 Subject
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // 列印 Subject 的 Principals
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // 完成後登出
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**：連結到 `"MyApp"` 配置並使用 `MyCallbackHandler`。
- **`lc.login()`**：觸發驗證過程。
- **`lc.getSubject()`**：擷取已驗證的 `Subject`。

#### **5. 執行授權操作（可選）**
驗證後，您可以使用 `Subject` 透過 `Subject.doAs()` 以其權限執行程式碼：

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // 在此處執行特權操作
        return null;
    }
});
```

這對於授權非常有用，其中操作會根據 `Subject` 的 `Principals` 進行限制。

---

### **整合所有步驟**
1. **配置**：使用您的 `LoginModule` 定義 `jaas.config`。
2. **CallbackHandler**：實作 `MyCallbackHandler` 以收集使用者輸入。
3. **LoginModule**：使用您的驗證邏輯實作 `MyLoginModule`。
4. **主程式碼**：使用 `LoginContext` 進行驗證並擷取 `Subject`。
5. **授權**：如有需要，使用 `Subject.doAs()` 執行特權操作。

當您執行 `Main` 類別時，它將：
- 提示輸入使用者名稱和密碼。
- 使用 `MyLoginModule` 進行驗證。
- 如果成功，列印 `Subject` 及其 `Principals`。

---

### **補充說明**
- **實際應用**：請將 `MyLoginModule` 中的硬編碼憑證替換為對資料庫、LDAP 或其他服務的檢查。Java 提供了標準模組，例如 `Krb5LoginModule`（Kerberos）或 `JndiLoginModule`（LDAP），但它們可能需要額外設定。
- **多個 LoginModules**：配置可以指定多個模組，並使用標誌（`required`、`sufficient` 等）來建立複雜的驗證流程。
- **安全性**：請使用安全實踐，例如避免對密碼使用 `String`（改用 `char[]`）並與現有安全框架整合。

本指南涵蓋了在 Java 中使用 `javax.security.auth` 進行驗證和授權的基礎知識！