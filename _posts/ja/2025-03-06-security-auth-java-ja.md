---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおける認証と認可
translated: true
type: note
---

Javaで`javax.security.auth`パッケージを使用するには、これがJava Authentication and Authorization Service (JAAS)フレームワークの一部であることを理解する必要があります。このパッケージは、ユーザーの認証（本人確認）と認可（実行権限の決定）を行うためのクラスとインターフェースを提供します。以下に、ユーザー名とパスワードによるユーザー認証といった基本的な認証シナリオで`javax.security.auth`を使用するためのステップバイステップガイドを示します。

---

### **主要概念の概要**
ステップに入る前に、`javax.security.auth`のコアコンポーネントについて簡単に説明します：

- **Subject**: 認証されるエンティティ（ユーザーやサービスなど）を表します。複数のアイデンティティ（Principal）と資格情報（パスワードや証明書など）を持つことができます。
- **Principal**: Subjectに関連付けられたアイデンティティやロール（ユーザー名やグループメンバーシップなど）。
- **Credential**: Subjectを認証するために使用される情報（パスワードや暗号鍵など）。
- **LoginModule**: 認証ロジック（データベースに対するユーザー名とパスワードの照合など）を実行するプラグ可能なコンポーネント。
- **LoginContext**: 1つ以上のLoginModuleを使用して認証プロセスを調整する中心的なクラス。
- **CallbackHandler**: ユーザーとの対話（ユーザー名とパスワードの入力プロンプトなど）のためのインターフェース。

これらの概念を念頭に置いて、パッケージの使用方法を探ってみましょう。

---

### **`javax.security.auth`使用手順**

#### **1. JAAS設定のセットアップ**
認証プロセスは、使用する`LoginModule`を指定する設定に依存します。これは設定ファイルまたはプログラムで定義できます。

例えば、`jaas.config`という名前のファイルを作成し、以下の内容を記述します：

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: アプリケーションまたはコンテキストの名前。コード内で参照します。
- **`com.example.MyLoginModule`**: カスタム`LoginModule`の完全修飾名（後で実装します）。
- **`required`**: このモジュールが認証を成功させるために必須であることを示すフラグ。他のフラグには、複数のモジュールによるより複雑なロジックを可能にする`requisite`、`sufficient`、`optional`があります。

このファイルを指すようにシステムプロパティを設定します：

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

あるいは、プログラムで設定することもできますが、多くの場合ファイルの方が簡単です。

#### **2. CallbackHandlerの実装**
`CallbackHandler`は、ユーザー名やパスワードなど、ユーザーからの入力を収集します。コンソールを使用した簡単な実装を以下に示します：

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

- **NameCallback**: ユーザー名のプロンプト表示と取得を行います。
- **PasswordCallback**: パスワードのプロンプト表示と取得を行います（セキュリティのため`char[]`として保存）。

#### **3. LoginModuleの実装**
`LoginModule`は認証ロジックを定義します。以下は、ハードコードされたユーザー名とパスワードをチェックする基本的な例です（実際には、データベースや外部サービスを使用します）：

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

            // ハードコードされたチェック（実際には本物のロジックに置き換える）
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

    // 認証のコミット（SubjectにPrincipalを追加）
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // 認証プロセスの中止
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Subjectのログアウト
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// シンプルなPrincipalの実装
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

- **login()**: `CallbackHandler`を使用して資格情報を取得し、チェックします。
- **commit()**: 認証が成功した場合、`Principal`を`Subject`に追加します。
- **abort()** と **logout()**: クリーンアップまたはキャンセルを処理します。

#### **4. LoginContextを使用した認証**
次に、メインアプリケーションで`LoginContext`を使用して認証を実行します：

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // JAAS設定がセットされていることを確認
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // 設定名とCallbackHandlerでLoginContextを作成
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // 認証を実行
            lc.login();

            // 認証されたSubjectを取得
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // SubjectのPrincipalを表示
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // 完了したらログアウト
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: `"MyApp"`設定にリンクし、`MyCallbackHandler`を使用します。
- **`lc.login()`**: 認証プロセスをトリガーします。
- **`lc.getSubject()`**: 認証された`Subject`を取得します。

#### **5. 認可されたアクションの実行（オプション）**
認証後、`Subject.doAs()`を使用して、その権限でコードを実行できます：

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // ここで特権アクションを実行
        return null;
    }
});
```

これは、アクションが`Subject`の`Principal`に基づいて制限される認可に役立ちます。

---

### **全体のまとめ**
1. **設定**: `LoginModule`を含む`jaas.config`を定義します。
2. **CallbackHandler**: ユーザー入力を収集する`MyCallbackHandler`を実装します。
3. **LoginModule**: 認証ロジックを含む`MyLoginModule`を実装します。
4. **メインコード**: `LoginContext`を使用して認証し、`Subject`を取得します。
5. **認可**: 必要に応じて`Subject.doAs()`を使用して特権アクションを実行します。

`Main`クラスを実行すると、以下のようになります：
- ユーザー名とパスワードの入力を求めます。
- `MyLoginModule`を使用して認証します。
- 成功した場合、`Subject`とその`Principal`を表示します。

---

### **追加の注意点**
- **実世界での使用法**: `MyLoginModule`のハードコードされた資格情報を、データベース、LDAP、または別のサービスに対するチェックに置き換えてください。Javaは`Krb5LoginModule`（Kerberos）や`JndiLoginModule`（LDAP）のような標準モジュールを提供しますが、追加の設定が必要な場合があります。
- **複数のLoginModule**: 設定では、フラグ（`required`、`sufficient`など）を使用して複数のモジュールを指定し、複雑な認証フローを作成できます。
- **セキュリティ**: パスワードに`String`を使用するのを避け（`char[]`を使用）、既存のセキュリティフレームワークと統合するなど、安全な慣行を使用してください。

このガイドでは、Javaでの認証と認可に`javax.security.auth`を使用する基本をカバーしています！