---
audio: false
generated: true
lang: ja
layout: post
title: 認証と認可のJava
translated: true
---

`javax.security.auth` パッケージをJavaで使用するには、Java Authentication and Authorization Service (JAAS) フレームワークの一部であることを理解する必要があります。このパッケージは、ユーザーを認証（誰であるかを確認する）し、認証（何をできるかを決定する）するためのクラスとインターフェースを提供します。以下は、`javax.security.auth` を基本的な認証シナリオ（ユーザー名とパスワードでユーザーを認証する）に使用するためのステップバイステップのガイドです。

---

### **主要概念の概要**
手順に入る前に、`javax.security.auth` の主要なコンポーネントについて簡単に説明します。

- **Subject**: 認証されるエンティティ（ユーザーやサービスなど）を表します。複数のアイデンティティ（Principal）と資格情報（パスワードや証明書など）を持つことができます。
- **Principal**: Subject に関連付けられたアイデンティティや役割（ユーザー名やグループメンバーシップなど）です。
- **Credential**: Subject を認証するために使用される情報（パスワードや暗号化キーなど）です。
- **LoginModule**: 認証ロジックを実行するプラグイン可能なコンポーネント（データベースに対してユーザー名とパスワードを確認するなど）です。
- **LoginContext**: 1つ以上の LoginModule を使用して認証プロセスを調整する中央クラスです。
- **CallbackHandler**: ユーザーとの対話を行うインターフェース（ユーザー名とパスワードを求めるなど）です。

これらの概念を頭に入れて、パッケージの使用方法を探ってみましょう。

---

### **`javax.security.auth` の使用方法**

#### **1. JAAS 設定のセットアップ**
認証プロセスは、使用する `LoginModule` を指定する設定に依存しています。これは設定ファイルまたはプログラムで定義できます。

例えば、以下の内容を持つ `jaas.config` という名前のファイルを作成します：

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: コードで参照するアプリケーション名またはコンテキストです。
- **`com.example.MyLoginModule`**: カスタム `LoginModule` の完全修飾名（後で実装します）。
- **`required`**: このモジュールが成功する必要があることを示すフラグです。他のフラグには `requisite`、`sufficient`、`optional` があり、複数のモジュールで複雑なロジックを許可します。

このファイルを指すシステムプロパティを設定します：

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

または、プログラムで設定を設定することもできますが、ほとんどの場合ファイルの方が簡単です。

#### **2. CallbackHandler の実装**
`CallbackHandler` は、ユーザーからの入力を収集します。以下は、コンソールを使用した簡単な実装例です：

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

- **NameCallback**: ユーザー名を求めて取得します。
- **PasswordCallback**: パスワードを求めて取得します（セキュリティのため `char[]` として保存）。

#### **3. LoginModule の実装**
`LoginModule` は認証ロジックを定義します。以下は、ハードコードされたユーザー名とパスワードを使用してチェックする基本的な例です（実際にはデータベースや外部サービスを使用します）：

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

    // モジュールの初期化
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // 認証の実行
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

            // ハードコードされたチェック（実際にはリアルなロジックに置き換えます）
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

    // 認証のコミット（Principal を Subject に追加）
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // 認証プロセスの中断
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Subject のログアウト
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// 簡単な Principal の実装
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

- **login()**: `CallbackHandler` を使用して資格情報を取得し、それをチェックします。
- **commit()**: 認証が成功した場合、`Principal` を `Subject` に追加します。
- **abort()** と **logout()**: クリーンアップやキャンセルを処理します。

#### **4. LoginContext を使用して認証**
次に、`LoginContext` を使用してメインアプリケーションで認証を実行します：

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // JAAS 設定が設定されていることを確認
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // 設定名と CallbackHandler を使用して LoginContext を作成
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // 認証を実行
            lc.login();

            // 認証された Subject を取得
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // Subject の Principals を表示
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // 完了時にログアウト
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: `"MyApp"` 設定にリンクし、`MyCallbackHandler` を使用します。
- **`lc.login()`**: 認証プロセスをトリガーします。
- **`lc.getSubject()`**: 認証された `Subject` を取得します。

#### **5. 認可されたアクションの実行（オプション）**
認証後、`Subject` を使用して `Subject.doAs()` を使用して特権を持ってコードを実行できます：

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // 特権アクションをここに実行
        return null;
    }
});
```

これは、`Subject` の `Principals` に基づいてアクションを制限するための認可に役立ちます。

---

### **すべてをまとめる**
1. **設定**: `jaas.config` で `LoginModule` を定義します。
2. **CallbackHandler**: ユーザー入力を収集するために `MyCallbackHandler` を実装します。
3. **LoginModule**: 認証ロジックを実装するために `MyLoginModule` を実装します。
4. **メインコード**: `LoginContext` を使用して認証し、`Subject` を取得します。
5. **認可**: 必要に応じて `Subject.doAs()` を使用して特権アクションを実行します。

`Main` クラスを実行すると、以下の操作が行われます：
- ユーザー名とパスワードを求めます。
- `MyLoginModule` を使用して認証します。
- 成功した場合、`Subject` とその `Principals` を表示します。

---

### **追加の注意事項**
- **実際の使用**: `MyLoginModule` のハードコードされた資格情報を、データベース、LDAP、または他のサービスとのチェックに置き換えます。Java は `Krb5LoginModule`（Kerberos）や `JndiLoginModule`（LDAP）などの標準モジュールを提供していますが、これらには追加の設定が必要です。
- **複数の LoginModules**: 設定には、複雑な認証フローを作成するためのフラグ（`required`、`sufficient` など）を使用して複数のモジュールを指定できます。
- **セキュリティ**: セキュリティの良い実践を使用し、パスワードに `String` を使用しない（`char[]` を使用）、既存のセキュリティフレームワークと統合するなどの方法を使用します。

このガイドは、Java で `javax.security.auth` を使用して認証と認可を行う基本的な方法をカバーしています！