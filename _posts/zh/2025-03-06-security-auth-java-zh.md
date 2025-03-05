---
audio: false
generated: true
lang: zh
layout: post
title: Java 中的身份验证和授权
translated: true
---

要在 Java 中使用 `javax.security.auth` 包，你需要理解它是 Java Authentication and Authorization Service (JAAS) 框架的一部分。这个包提供了用于验证用户（验证他们的身份）和授权他们（确定他们可以做什么）的类和接口。以下是使用 `javax.security.auth` 进行基本身份验证场景的分步指南，例如使用用户名和密码验证用户。

---

### **关键概念概述**
在深入步骤之前，这里是 `javax.security.auth` 中核心组件的简要说明：

- **Subject**：表示被验证的实体（例如用户或服务）。它可以有多个身份（Principals）和凭证（例如密码或证书）。
- **Principal**：与 Subject 相关联的身份或角色，例如用户名或组成员。
- **Credential**：用于验证 Subject 的信息，例如密码或加密密钥。
- **LoginModule**：执行身份验证逻辑的可插入组件（例如，将用户名和密码与数据库进行比较）。
- **LoginContext**：协调使用一个或多个 LoginModules 进行身份验证的中心类。
- **CallbackHandler**：与用户交互的接口，例如提示用户名和密码。

了解这些概念后，让我们探索如何使用这个包。

---

### **使用 `javax.security.auth` 的步骤**

#### **1. 设置 JAAS 配置**
身份验证过程依赖于指定要使用的 `LoginModule`(s) 的配置。这可以在配置文件或程序中定义。

例如，创建一个名为 `jaas.config` 的文件，内容如下：

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**：应用程序或上下文的名称，你将在代码中引用它。
- **`com.example.MyLoginModule`**：你的自定义 `LoginModule` 的完全限定名称（你将在后面实现它）。
- **`required`**：表示此模块必须成功才能通过身份验证。其他标志包括 `requisite`、`sufficient` 和 `optional`，允许使用多个模块进行更复杂的逻辑。

设置系统属性以指向此文件：

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

或者，你可以以编程方式设置配置，但对于大多数情况，文件更简单。

#### **2. 实现 CallbackHandler**
`CallbackHandler` 收集用户的输入，例如用户名和密码。以下是使用控制台的简单实现：

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

- **NameCallback**：提示并检索用户名。
- **PasswordCallback**：提示并检索密码（以 `char[]` 形式存储以确保安全）。

#### **3. 实现 LoginModule**
`LoginModule` 定义身份验证逻辑。以下是一个基本示例，它检查硬编码的用户名和密码（在实践中，你会使用数据库或外部服务）：

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

    // 初始化模块
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // 执行身份验证
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

            // 硬编码检查（在实践中用真实逻辑替换）
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

    // 提交身份验证（将 Principals 添加到 Subject）
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // 中止身份验证过程
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // 注销 Subject
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// 简单的 Principal 实现
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

- **login()**：使用 `CallbackHandler` 获取凭证并检查它们。
- **commit()**：如果身份验证成功，将 `Principal` 添加到 `Subject`。
- **abort()** 和 **logout()**：处理清理或取消。

#### **4. 使用 LoginContext 进行身份验证**
现在，使用 `LoginContext` 在主应用程序中执行身份验证：

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // 确保 JAAS 配置已设置
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // 创建 LoginContext 并使用配置名称和 CallbackHandler
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // 执行身份验证
            lc.login();

            // 获取验证的 Subject
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // 打印 Subject 的 Principals
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // 完成时注销
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**：链接到 `"MyApp"` 配置并使用 `MyCallbackHandler`。
- **`lc.login()`**：触发身份验证过程。
- **`lc.getSubject()`**：检索验证的 `Subject`。

#### **5. 执行授权操作（可选）**
身份验证后，你可以使用 `Subject` 使用其权限执行代码，使用 `Subject.doAs()`：

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // 在这里执行特权操作
        return null;
    }
});
```

这对于授权很有用，其中操作基于 `Subject` 的 `Principals` 受到限制。

---

### **将所有内容结合起来**
1. **配置**：使用你的 `LoginModule` 定义 `jaas.config`。
2. **CallbackHandler**：实现 `MyCallbackHandler` 以收集用户输入。
3. **LoginModule**：使用你的身份验证逻辑实现 `MyLoginModule`。
4. **主代码**：使用 `LoginContext` 进行身份验证并检索 `Subject`。
5. **授权**：如果需要，使用 `Subject.doAs()` 进行特权操作。

当你运行 `Main` 类时，它将：
- 提示用户名和密码。
- 使用 `MyLoginModule` 进行身份验证。
- 如果成功，打印 `Subject` 和其 `Principals`。

---

### **额外说明**
- **实际使用**：在 `MyLoginModule` 中替换硬编码凭证，使用数据库、LDAP 或其他服务进行检查。Java 提供了标准模块，如 `Krb5LoginModule`（Kerberos）或 `JndiLoginModule`（LDAP），但它们可能需要额外的设置。
- **多个 LoginModules**：配置可以指定多个模块，使用标志（`required`、`sufficient` 等）创建复杂的身份验证流程。
- **安全**：使用安全实践，例如避免使用 `String` 存储密码（使用 `char[]`），并与现有的安全框架集成。

这个指南涵盖了在 Java 中使用 `javax.security.auth` 进行身份验证和授权的基础知识！