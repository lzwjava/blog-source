---
audio: false
generated: true
lang: zh
layout: post
title: SASL 认证在 Java 中
translated: true
---

要在 Java 中使用 `javax.security.sasl` 包，你需要利用其类和接口来实现简单身份验证和安全层（SASL）机制，用于客户端-服务器应用程序的身份验证和可选的数据安全。主要涉及的类是 `Sasl`、`SaslClient` 和 `SaslServer`。下面是如何使用这个包的全面指南，包括客户端和服务器实现的步骤和示例代码。

---

### **javax.security.sasl 概述**
`javax.security.sasl` 包提供了一个用于 SASL 身份验证的框架，常用于 LDAP、IMAP 等协议或自定义应用程序。它包括：
- **`Sasl`**：一个包含静态方法的实用类，用于创建 `SaslClient` 和 `SaslServer` 实例。
- **`SaslClient`**：表示 SASL 身份验证过程的客户端端。
- **`SaslServer`**：表示 SASL 身份验证过程的服务器端。
- **`CallbackHandler`**：一个你需要实现的接口，用于处理身份验证回调（例如提供用户名或密码）。

该过程涉及创建 `SaslClient` 或 `SaslServer`，提供一个回调处理程序来管理身份验证数据，并进行挑战-响应交换，直到身份验证完成。

---

### **使用 javax.security.sasl 的步骤**

#### **1. 确定你的角色（客户端或服务器）**
决定你的应用程序是作为客户端（向服务器进行身份验证）还是服务器（向客户端进行身份验证）。这决定了你是否使用 `SaslClient` 或 `SaslServer`。

#### **2. 选择一个 SASL 机制**
SASL 支持各种机制，例如：
- `PLAIN`：简单的用户名/密码身份验证（无加密）。
- `DIGEST-MD5`：基于密码的挑战-响应。
- `GSSAPI`：基于 Kerberos 的身份验证。

选择一个客户端和服务器都支持的机制。为了简单起见，本指南以 `PLAIN` 机制为例。

#### **3. 实现一个 CallbackHandler**
`CallbackHandler` 是必需的，用于提供或验证身份验证凭据。你需要实现 `javax.security.auth.callback.CallbackHandler` 接口。

- **对于客户端**：提供凭据，如用户名和密码。
- **对于服务器**：验证客户端凭据或提供服务器端身份验证数据。

以下是 `PLAIN` 机制的客户端 `CallbackHandler` 示例：

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

对于服务器，你可能会验证凭据与数据库中的数据：

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // 从数据库中检索用户名的预期密码
            } else if (callback instanceof PasswordCallback) {
                // 设置预期密码以进行验证
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. 客户端实现**
作为客户端进行身份验证：

1. **创建一个 SaslClient**：
   使用 `Sasl.createSaslClient`，带有机制、协议、服务器名称、属性和回调处理程序。

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // 可选；如果与身份验证 ID 相同，则为 null
   String protocol = "ldap"; // 例如，"ldap"、"imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // 可选属性，例如 QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **处理挑战-响应交换**：
   - 检查初始响应（在客户端优先机制如 `PLAIN` 中常见）。
   - 向服务器发送响应并处理挑战，直到身份验证完成。

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // 向服务器发送响应（协议特定，例如通过套接字或 LDAP BindRequest）
   }

   // 从服务器接收挑战（协议特定）
   byte[] challenge = /* 从服务器读取 */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // 向服务器发送响应
       if (sc.isComplete()) break;
       challenge = /* 从服务器读取下一个挑战 */;
   }

   // 身份验证完成；通过协议特定的方式检查成功
   ```

   对于 `PLAIN`，客户端在初始响应中发送凭据，服务器通常在没有进一步挑战的情况下响应成功或失败。

#### **5. 服务器实现**
作为服务器进行客户端身份验证：

1. **创建一个 SaslServer**：
   使用 `Sasl.createSaslServer`，带有机制、协议、服务器名称、属性和回调处理程序。

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

2. **处理挑战-响应交换**：
   - 处理客户端的初始响应并生成挑战，直到身份验证完成。

   ```java
   byte[] response = /* 从客户端读取初始响应 */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // 向客户端发送挑战（协议特定）

   while (!ss.isComplete()) {
       response = /* 从客户端读取下一个响应 */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // 身份验证完成
           break;
       }
       // 向客户端发送挑战
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // 继续处理授权用户
   }
   ```

   对于 `PLAIN`，服务器在初始响应中验证凭据并在没有进一步挑战的情况下完成身份验证。

#### **6. 可选：使用安全层**
如果机制（例如 `DIGEST-MD5`）支持安全层：
- 在客户端使用 `sc.wrap()` 和 `sc.unwrap()`，在服务器使用 `ss.wrap()` 和 `ss.unwrap()`，在身份验证后加密/解密消息。
- `PLAIN` 不支持安全层。

---

### **关键点**
- **集成**：将 SASL 交换嵌入到应用程序的通信协议中（例如，LDAP Bind 请求、IMAP AUTHENTICATE 命令）。
- **错误处理**：使用 try-catch 块包装代码以处理 `SaslException` 和其他潜在错误。
- **属性**：使用 `props` 映射配置选项，例如质量保护（`"javax.security.sasl.qop"`），如果机制支持。

---

### **示例用例**
对于使用 `PLAIN` 进行身份验证的 LDAP 客户端：
1. 使用 `PLAIN` 机制创建一个 `SaslClient`。
2. 发送一个 LDAP `BindRequest`，带有机制和初始响应（`sc.evaluateChallenge(new byte[0])`）。
3. 处理服务器的 `BindResponse` 以确认成功。

对于自定义协议，用你的协议的身份验证命令替换 LDAP 特定的步骤。

---

通过遵循这些步骤，你可以有效地在 Java 应用程序中实现 SASL 身份验证，根据你选择的机制和协议进行定制。