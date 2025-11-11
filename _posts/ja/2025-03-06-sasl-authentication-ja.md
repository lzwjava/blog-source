---
audio: false
generated: true
lang: ja
layout: post
title: JavaにおけるSASL認証
translated: true
type: note
---

Javaで`javax.security.sasl`パッケージを使用するには、そのクラスとインターフェースを活用して、クライアント-サーバーアプリケーションにおけるSimple Authentication and Security Layer（SASL）メカニズムを実装し、認証と（オプションで）データセキュリティを提供します。主に関わるクラスは`Sasl`、`SaslClient`、`SaslServer`です。以下に、クライアントとサーバーの両方の実装に関する手順とサンプルコードを含む、このパッケージの使用方法に関する包括的なガイドを示します。

---

### **javax.security.saslの概要**
`javax.security.sasl`パッケージは、LDAP、IMAP、またはカスタムアプリケーションなどのプロトコルで一般的に使用されるSASL認証のフレームワークを提供します。これには以下が含まれます：
- **`Sasl`**: `SaslClient`および`SaslServer`インスタンスを作成するための静的メソッドを持つユーティリティクラス。
- **`SaslClient`**: SASL認証プロセスのクライアント側を表します。
- **`SaslServer`**: SASL認証プロセスのサーバー側を表します。
- **`CallbackHandler`**: 認証コールバック（ユーザー名やパスワードの提供など）を処理するために実装するインターフェース。

このプロセスには、`SaslClient`または`SaslServer`の作成、認証データを管理するコールバックハンドラの提供、および認証が完了するまでのチャレンジ-レスポンス交換の実行が含まれます。

---

### **javax.security.saslを使用する手順**

#### **1. 役割（クライアントまたはサーバー）を決定する**
アプリケーションがクライアント（サーバーに対して認証する）として機能するか、サーバー（クライアントを認証する）として機能するかを決定します。これにより、`SaslClient`と`SaslServer`のどちらを使用するかが決まります。

#### **2. SASLメカニズムを選択する**
SASLは様々なメカニズムをサポートしています。例えば：
- `PLAIN`: シンプルなユーザー名/パスワード認証（暗号化なし）。
- `DIGEST-MD5`: チャレンジ-レスポンスを用いたパスワードベースの認証。
- `GSSAPI`: Kerberosベースの認証。

クライアントとサーバーの両方でサポートされているメカニズムを選択します。簡単のため、このガイドでは例として`PLAIN`メカニズムを使用します。

#### **3. CallbackHandlerを実装する**
認証資格情報を提供または検証するには、`CallbackHandler`が必要です。`javax.security.auth.callback.CallbackHandler`インターフェースを実装する必要があります。

- **クライアントの場合**: ユーザー名やパスワードなどの資格情報を提供します。
- **サーバーの場合**: クライアントの資格情報を検証するか、サーバー側の認証データを提供します。

以下は、`PLAIN`メカニズム用のクライアント側`CallbackHandler`の例です：

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

サーバーの場合、データベースに対して資格情報を検証するかもしれません：

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // データベースからユーザー名に対応する期待されるパスワードを取得
            } else if (callback instanceof PasswordCallback) {
                // 検証のための期待されるパスワードを設定
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

1. **SaslClientを作成する**:
   メカニズム、プロトコル、サーバー名、プロパティ、およびコールバックハンドラを指定して`Sasl.createSaslClient`を使用します。

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // オプション。認証IDと同じ場合はnull
   String protocol = "ldap"; // 例: "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // オプションのプロパティ（例: QoP）
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **チャレンジ-レスポンス交換を処理する**:
   - 初期レスポンスがあるか確認します（`PLAIN`のようなクライアントファーストのメカニズムで一般的）。
   - サーバーにレスポンスを送信し、認証が完了するまでチャレンジを処理します。

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // レスポンスをサーバーに送信（プロトコル固有、例: ソケット経由またはLDAP BindRequest）
   }

   // サーバーチャレンジを受信（プロトコル固有）
   byte[] challenge = /* サーバーから読み取り */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // レスポンスをサーバーに送信
       if (sc.isComplete()) break;
       challenge = /* サーバーから次のチャレンジを読み取り */;
   }

   // 認証完了。プロトコル固有の方法で成功を確認
   ```

   `PLAIN`の場合、クライアントは初期レスポンスで資格情報を送信し、サーバーは通常、追加のチャレンジなしで成功または失敗で応答します。

#### **5. サーバー側の実装**
サーバーとしてクライアントを認証するには：

1. **SaslServerを作成する**:
   メカニズム、プロトコル、サーバー名、プロパティ、およびコールバックハンドラを指定して`Sasl.createSaslServer`を使用します。

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

2. **チャレンジ-レスポンス交換を処理する**:
   - クライアントの初期レスポンスを処理し、認証が完了するまでチャレンジを生成します。

   ```java
   byte[] response = /* クライアントから初期レスポンスを読み取り */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // チャレンジをクライアントに送信（プロトコル固有）

   while (!ss.isComplete()) {
       response = /* クライアントから次のレスポンスを読み取り */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // 認証完了
           break;
       }
       // チャレンジをクライアントに送信
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // 認証されたユーザーで処理を続行
   }
   ```

   `PLAIN`の場合、サーバーは初期レスポンスで資格情報を検証し、追加のチャレンジなしで認証を完了します。

#### **6. オプション：セキュリティレイヤーを使用する**
メカニズム（例: `DIGEST-MD5`）がセキュリティレイヤーをサポートしている場合：
- 認証後にメッセージを暗号化/復号化するために、クライアントで`sc.wrap()`と`sc.unwrap()`を、またはサーバーで`ss.wrap()`と`ss.unwrap()`を使用します。
- `PLAIN`はセキュリティレイヤーをサポートしていません。

---

### **重要なポイント**
- **統合**: SASL交換をアプリケーションの通信プロトコル（例: LDAP Bindリクエスト、IMAP AUTHENTICATEコマンド）に組み込みます。
- **エラーハンドリング**: `SaslException`やその他の潜在的なエラーを処理するために、コードをtry-catchブロックでラップします。
- **プロパティ**: メカニズムでサポートされている場合、保護の品質（`"javax.security.sasl.qop"`）などのオプションを構成するために`props`マップを使用します。

---

### **使用例**
`PLAIN`で認証するLDAPクライアントの場合：
1. `PLAIN`メカニズムで`SaslClient`を作成します。
2. メカニズムと初期レスポンス（`sc.evaluateChallenge(new byte[0])`）を含むLDAP `BindRequest`を送信します。
3. サーバーの`BindResponse`を処理して成功を確認します。

カスタムプロトコルの場合、LDAP固有の手順をプロトコルの認証コマンドに置き換えます。

---

これらの手順に従うことで、`javax.security.sasl`を効果的に使用してJavaアプリケーションにSASL認証を実装し、選択したメカニズムとプロトコルに合わせてプロセスを調整できます。