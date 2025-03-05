---
audio: false
generated: true
lang: hant
layout: post
title: 身份驗證與授權於Java
translated: true
---

要在 Java 中使用 `javax.security.auth` 套件，你需要了解它是 Java Authentication and Authorization Service (JAAS) 框架的一部分。這個套件提供了用於驗證用戶（驗證他們的身份）和授權他們（確定他們可以做什麼）的類和介面。以下是使用 `javax.security.auth` 進行基本驗證情境的分步指南，例如使用用戶名和密碼驗證用戶。

---

### **關鍵概念概述**
在深入步驟之前，這裡是 `javax.security.auth` 中核心組件的簡要說明：

- **Subject**：代表一個正在進行驗證的實體（例如用戶或服務）。它可以擁有多個身份（Principals）和憑證（例如密碼或證書）。
- **Principal**：與 Subject 相關聯的身份或角色，例如用戶名或群組成員資格。
- **Credential**：用於驗證 Subject 的信息，例如密碼或加密密鑰。
- **LoginModule**：可插入的組件，執行驗證邏輯（例如將用戶名和密碼與數據庫進行比較）。
- **LoginContext**：協調使用一個或多個 LoginModules 進行驗證過程的中央類。
- **CallbackHandler**：與用戶互動的介面，例如提示用戶名和密碼。

了解這些概念後，讓我們探索如何使用這個套件。

---

### **使用 `javax.security.auth` 的步驟**

#### **1. 設置 JAAS 配置**
驗證過程依賴於指定要使用的 `LoginModule` 的配置。這可以在配置文件中定義，也可以以編程方式定義。

例如，創建一個名為 `jaas.config` 的文件，內容如下：

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**：應用程序或上下文的名稱，你將在代碼中引用它。
- **`com.example.MyLoginModule`**：自定義 `LoginModule` 的完全限定名稱（你將在後面實現它）。
- **`required`**：表示這個模塊必須成功驗證才能通過。其他標誌包括 `requisite`、`sufficient` 和 `optional`，允許使用多個模塊進行更複雜的邏輯。

設置系統屬性以指向此文件：

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

或者，你可以以編程方式設置配置，但對於大多數情況來說，文件更簡單。

#### **2. 實現 CallbackHandler**
`CallbackHandler` 收集用戶的輸入，例如用戶名和密碼。這裡是一個使用控制台的簡單實現：

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

- **NameCallback**：提示並檢索用戶名。
- **PasswordCallback**：提示並檢索密碼（存儲為 `char[]` 以確保安全）。

#### **3. 實現 LoginModule**
`LoginModule` 定義驗證邏輯。以下是一個基本示例，它對硬編碼的用戶名和密碼進行檢查（在實際應用中，你會使用數據庫或外部服務）：

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

    // 初始化模塊
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

            // 硬編碼檢查（在實際應用中替換為真實邏輯）
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

    // 提交驗證（將 Principals 添加到 Subject）
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

// 簡單的 Principal 實現
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

- **login()**：使用 `CallbackHandler` 获取憑證並檢查它們。
- **commit()**：如果驗證成功，將 `Principal` 添加到 `Subject`。
- **abort()** 和 **logout()**：處理清理或取消。

#### **4. 使用 LoginContext 進行驗證**
現在，使用 `LoginContext` 在主應用程序中執行驗證：

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // 確保 JAAS 配置已設置
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // 創建 LoginContext 並使用配置名稱和 CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // 執行驗證
            lc.login();

            // 获取驗證的 Subject
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // 打印 Subject 的 Principals
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

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**：鏈接到 `"MyApp"` 配置並使用 `MyCallbackHandler`。
- **`lc.login()`**：觸發驗證過程。
- **`lc.getSubject()`**：檢索驗證的 `Subject`。

#### **5. 執行授權操作（可選）**
驗證後，你可以使用 `Subject` 以其特權執行代碼，使用 `Subject.doAs()`：

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // 在這裡執行特權操作
        return null;
    }
});
```

這對於授權非常有用，其中操作根據 `Subject` 的 `Principals` 受到限制。

---

### **將所有內容整合在一起**
1. **配置**：使用 `LoginModule` 定義 `jaas.config`。
2. **CallbackHandler**：實現 `MyCallbackHandler` 以收集用戶輸入。
3. **LoginModule**：實現 `MyLoginModule` 並使用驗證邏輯。
4. **主代碼**：使用 `LoginContext` 進行驗證並檢索 `Subject`。
5. **授權**：如果需要，使用 `Subject.doAs()` 進行特權操作。

當你運行 `Main` 類時，它將：
- 提示用戶名和密碼。
- 使用 `MyLoginModule` 進行驗證。
- 如果成功，打印 `Subject` 和其 `Principals`。

---

### **其他說明**
- **實際應用**：在 `MyLoginModule` 中替換硬編碼憑證，使用數據庫、LDAP 或其他服務進行檢查。Java 提供了標準模塊，例如 `Krb5LoginModule`（Kerberos）或 `JndiLoginModule`（LDAP），但它們可能需要額外設置。
- **多個 LoginModules**：配置可以指定多個模塊，使用標誌（`required`、`sufficient` 等）創建複雜的驗證流程。
- **安全性**：使用安全實踐，例如避免使用 `String` 存儲密碼（使用 `char[]`）並與現有的安全框架集成。

這個指南涵蓋了在 Java 中使用 `javax.security.auth` 進行驗證和授權的基本知識！