---
audio: false
generated: true
lang: ja
layout: post
title: SASL 認証の Java
translated: true
---

`javax.security.sasl` パッケージをJavaで使用するには、そのクラスとインターフェースを利用して、クライアントサーバーアプリケーションの認証と、オプションでデータのセキュリティを実現するためのSimple Authentication and Security Layer (SASL) メカニズムを実装する必要があります。主要なクラスは `Sasl`、`SaslClient`、`SaslServer` です。以下は、このパッケージを使用するための包括的なガイドです。クライアントとサーバーの実装の手順と例コードを含みます。

---

### **javax.security.sasl の概要**
`javax.security.sasl` パッケージは、LDAP、IMAP、またはカスタムアプリケーションなどのプロトコルで一般的に使用されるSASL認証のフレームワークを提供します。以下を含みます：
- **`Sasl`**：`SaslClient` と `SaslServer` のインスタンスを作成するための静的メソッドを含むユーティリティクラス。
- **`SaslClient`**：SASL認証プロセスのクライアント側を表します。
- **`SaslServer`**：SASL認証プロセスのサーバー側を表します。
- **`CallbackHandler`**：認証コールバックを処理するために実装するインターフェース（例：ユーザー名やパスワードの提供）。

このプロセスには、`SaslClient` または `SaslServer` を作成し、認証データを管理するためのコールバックハンドラーを提供し、認証が完了するまでチャレンジ-レスポンスの交換を行うことが含まれます。

---

### **javax.security.sasl の使用手順**

#### **1. あなたの役割を決定する（クライアントまたはサーバー）**
アプリケーションがサーバーに認証するクライアントとして機能するか、クライアントを認証するサーバーとして機能するかを決定します。これにより、`SaslClient` または `SaslServer` を使用するかが決定されます。

#### **2. SASL メカニズムを選択する**
SASLは、以下のようなさまざまなメカニズムをサポートしています：
- `PLAIN`：簡単なユーザー名/パスワード認証（暗号化なし）。
- `DIGEST-MD5`：パスワードベースのチャレンジ-レスポンス。
- `GSSAPI`：Kerberosベースの認証。

クライアントとサーバーの両方でサポートされるメカニズムを選択します。このガイドでは、簡単さのために `PLAIN` メカニズムを例として使用します。

#### **3. CallbackHandler を実装する**
`CallbackHandler` は、認証資格情報を提供または検証するために必要です。`javax.security.auth.callback.CallbackHandler` インターフェースを実装する必要があります。

- **クライアントの場合**：ユーザー名やパスワードなどの資格情報を提供します。
- **サーバーの場合**：クライアントの資格情報を検証するか、サーバー側の認証データを提供します。

以下は、`PLAIN` メカニズム用のクライアント側 `CallbackHandler` の例です：

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

サーバーの場合、データベースから資格情報を検証するかもしれません：

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // データベースからユーザー名の期待されるパスワードを取得
            } else if (callback instanceof PasswordCallback) {
                // 検証のために期待されるパスワードを設定
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. クライアント側の実装**
クライアントとして認証するには：

1. **SaslClient を作成する**：
   メカニズム、プロトコル、サーバー名、プロパティ、コールバックハンドラーを使用して `Sasl.createSaslClient` を使用します。

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // オプション；認証IDと同じ場合はnull
   String protocol = "ldap"; // 例："ldap"、"imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // オプションのプロパティ、例：QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **チャレンジ-レスポンスの交換を処理する**：
   - 初期レスポンスを確認します（`PLAIN` などのクライアントファーストメカニズムで一般的）。
   - サーバーにレスポンスを送信し、認証が完了するまでチャレンジを処理します。

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // サーバーにレスポンスを送信（プロトコル固有、例：ソケットまたはLDAP BindRequestを介して）
   }

   // サーバーからチャレンジを受信（プロトコル固有）
   byte[] challenge = /* サーバーから読み取り */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // サーバーにレスポンスを送信
       if (sc.isComplete()) break;
       challenge = /* サーバーから次のチャレンジを読み取り */;
   }

   // 認証が完了しました；プロトコル固有の手段で成功を確認
   ```

   `PLAIN` の場合、クライアントは初期レスポンスに資格情報を送信し、サーバーは通常、追加のチャレンジなしで成功または失敗を返します。

#### **5. サーバー側の実装**
クライアントをサーバーとして認証するには：

1. **SaslServer を作成する**：
   メカニズム、プロトコル、サーバー名、プロパティ、コールバックハンドラーを使用して `Sasl.createSaslServer` を使用します。

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

2. **チャレンジ-レスポンスの交換を処理する**：
   - クライアントの初期レスポンスを処理し、認証が完了するまでチャレンジを生成します。

   ```java
   byte[] response = /* クライアントから初期レスポンスを読み取り */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // クライアントにチャレンジを送信（プロトコル固有）

   while (!ss.isComplete()) {
       response = /* クライアントから次のレスポンスを読み取り */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // 認証完了
           break;
       }
       // クライアントにチャレンジを送信
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // 認証されたユーザーで進行
   }
   ```

   `PLAIN` の場合、サーバーは初期レスポンスの資格情報を検証し、追加のチャレンジなしで認証を完了します。

#### **6. オプション：セキュリティレイヤーの使用**
メカニズム（例：`DIGEST-MD5`）がセキュリティレイヤーをサポートする場合：
- 認証後、クライアントでは `sc.wrap()` と `sc.unwrap()` を、サーバーでは `ss.wrap()` と `ss.unwrap()` を使用してメッセージを暗号化/復号化します。
- `PLAIN` はセキュリティレイヤーをサポートしていません。

---

### **重要なポイント**
- **統合**：SASL交換をアプリケーションの通信プロトコルに組み込みます（例：LDAP Bindリクエスト、IMAP AUTHENTICATEコマンド）。
- **エラーハンドリング**：`SaslException` およびその他の可能なエラーを処理するためにコードをtry-catchブロックでラップします。
- **プロパティ**：メカニズムがサポートする場合は、`props` マップを使用して、品質の保護（`"javax.security.sasl.qop"`）などのオプションを構成します。

---

### **使用例**
`PLAIN` でLDAPクライアントを認証する場合：
1. `PLAIN` メカニズムで `SaslClient` を作成します。
2. メカニズムと初期レスポンス（`sc.evaluateChallenge(new byte[0])`）を含むLDAP `BindRequest` を送信します。
3. サーバーの `BindResponse` を処理して成功を確認します。

カスタムプロトコルの場合、LDAP固有の手順をプロトコルの認証コマンドに置き換えます。

---

これらの手順に従うことで、`javax.security.sasl` を使用してJavaアプリケーションにSASL認証を実装し、選択したメカニズムとプロトコルに合わせてプロセスをカスタマイズすることができます。