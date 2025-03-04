---
audio: false
generated: true
lang: ja
layout: post
title: AES暗号化されたパスワードをWebSphere Libertyで使用する
translated: true
---

WebSphere Libertyの`server.xml`からAES暗号化されたパスワードをSquirrel SQLクライアントで使用するには、以下の手順に従ってください。

---

### **1. WebSphere Libertyのツールを使用してパスワードを復号化する**

暗号化されたパスワード（例：`password="{aes}ABC123..."）はまず復号化する必要があります。Libertyの`securityUtility`ツールがこれを行うことができますが、暗号化に使用されたキーストアへのアクセスが必要です。

#### **復号化コマンド:**
```bash
# Libertyのbinディレクトリに移動
cd /path/to/wlp/bin

# securityUtility decodeコマンドを実行
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

置換する項目：
- `<LibertyServerPath>`: Libertyサーバーへのパス（例：`usr/servers/defaultServer`）。
- `<KeyAlias>`: キーストア内のキーのエイリアス（デフォルト：`default`）。
- `<KeystorePassword>`: キーストアのパスワード（デフォルト：`KeystorePass`が変更されていない場合）。
- `{aes}ABC123...`: `server.xml`からの暗号化されたパスワード。

---

### **2. 復号化されたパスワードをSquirrelで使用する**

1. Squirrel SQLクライアントを開く。
2. 新しい接続エイリアスを作成する。
3. 接続プロパティで以下を設定する：
   - **ドライバー**: Oracle JDBCドライバーを選択する。
   - **URL**: Libertyの`server.xml`からのJDBC URLを使用する（例：`jdbc:oracle:thin:@//host:port/service`）。
   - **ユーザー名**: Libertyの`<dataSource>`からのユーザー名。
   - **パスワード**: 手順1で得られた**復号化されたパスワード**を入力する。

---

### **重要な注意点**

- **キーストアへのアクセス**: キーストアファイル（`key.jks`または`key.p12`）とそのパスワードが必要です。デフォルトでは、Libertyの`resources/security`ディレクトリにあります。
- **セキュリティ**: 復号化されたパスワードを平文で保存しないでください。ファイルに保存せずにSquirrelに直接入力してください。
- **管理者の助け**: キーストアの資格情報がなければ、Liberty管理者に連絡して安全にパスワードを復号化してもらう。

---

### **代替手段（推奨されません）**

復号化が不可能な場合、一時的に`server.xml`内の暗号化されたパスワードを平文のパスワードに置き換える（テスト専用）。Libertyを再起動し、Squirrelで平文のパスワードを使用する。その後、暗号化されたパスワードに戻す。

```xml
<!-- 例：平文パスワード（運用では避ける） -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

これらの手順に従うことで、復号化されたパスワードをSquirrelで安全に使用しながら、セキュリティベストプラクティスに準拠することができます。

---

Squirrel SQLクライアントをOracleデータベースに接続するためのWebSphere Liberty Profileの`server.xml`ファイルの設定を使用するには、特にOracle JDBCドライバーのプロパティにAES暗号化されたパスワードが含まれる場合、以下の手順に従ってください。このプロセスには、`server.xml`ファイルから接続詳細を抽出し、暗号化されたパスワードを処理し、Squirrel SQLを適切に設定することが含まれます。以下は完全なガイドです。

### 手順1: `server.xml`の設定を理解する

WebSphere Liberty Profileでは、データベース接続は`server.xml`ファイル内の`<dataSource>`要素で定義されます。この要素は、Oracleデータベースへのデータソースのプロパティを含む`<properties.oracle>`要素を指定します。例の設定は以下のようになります。

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}encrypted_password"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

ここで：
- **`url`**: Oracleデータベースに接続するためのJDBC URL（例：`jdbc:oracle:thin:@//localhost:1521/orcl`）。
- **`user`**: データベースのユーザー名（例：`scott`）。
- **`password`**: AESで暗号化されたパスワードで、`{aes}`でプレフィックスが付いています（例：`{aes}encrypted_password`）。
- **`<jdbcDriver>`**: Oracle JDBCドライバーJARファイルへの参照。

Squirrel SQLは独立したクライアントであり、WebSphere管理されたデータソース（例：JNDIルックアップ）に直接アクセスできないため、同じ接続詳細を手動で設定する必要があります。

### 手順2: `server.xml`から接続詳細を抽出する

Oracleデータベースに対応する`<dataSource>`要素を`server.xml`ファイル内で特定し、以下を確認します。
- **JDBC URL**: `<properties.oracle>`要素の`url`属性にあります（例：`jdbc:oracle:thin:@//localhost:1521/orcl`）。
- **ユーザー名**: `<properties.oracle>`要素の`user`属性にあります（例：`scott`）。
- **暗号化されたパスワード**: `<properties.oracle>`要素の`password`属性にあります（例：`{aes}encrypted_password`）。

JDBC URLは、Oracleデータベースに接続するための通常の形式のいずれかです。
- `jdbc:oracle:thin:@//hostname:port/service_name`（サービス名を使用）
- `jdbc:oracle:thin:@hostname:port:SID`（SIDを使用）

`server.xml`を確認して、正確なURLを確認してください。

### 手順3: AES暗号化されたパスワードをデコードする

`server.xml`のパスワードはAESで暗号化されており、`{aes}`プレフィックスが付いています。WebSphere Liberty Profileはセキュリティのためにパスワードを暗号化しますが、Squirrel SQLは接続を確立するために平文のパスワードが必要です。パスワードをデコードするには以下の手順に従います。

1. **WebSphereの`securityUtility`ツールを使用する**:
   - このツールはWebSphere Libertyインストールに含まれており、通常は`bin`ディレクトリ（例：`<liberty_install_dir>/bin/`）にあります。
   - ターミナルまたはコマンドプロンプトから`bin`ディレクトリに移動し、以下のコマンドを実行します。
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     `<encrypted_password>`を`password`属性からの実際の暗号化された文字列（`{aes}`の後に続くもの）に置き換えます。例：
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - ツールは平文のパスワードを出力します。

2. **代替手段**:
   - WebSphere Libertyインストールまたは`securityUtility`ツールにアクセスできない場合、システム管理者またはデータソースを設定した人に平文のパスワードを取得してもらう必要があります。

平文のパスワードを安全に保存しておきます。Squirrel SQLで使用するために必要です。

### 手順4: Squirrel SQLでOracle JDBCドライバーを設定する

Squirrel SQLはOracleデータベースに接続するためにOracle JDBCドライバーが必要です。`server.xml`の`<library>`要素で指定された同じドライバーJARファイルが必要です。

1. **ドライバーJARを取得する**:
   - `server.xml`の`<fileset>`要素で指定されたOracle JDBCドライバーJARファイル（例：`ojdbc6.jar`）を特定します。
   - ない場合は、Oracleのウェブサイトから適切なバージョンをダウンロードします（例：`ojdbc6.jar`または`ojdbc8.jar`、データベースバージョンに一致）。

2. **Squirrel SQLにドライバーを追加する**:
   - Squirrel SQLを開きます。
   - 左側の**Drivers**タブに移動します。
   - **+**ボタンをクリックして新しいドライバーを追加します。
   - ドライバーを設定します：
     - **名前**: 名前を入力します（例：「Oracle JDBCドライバー」）。
     - **例URL**: 例URLを入力します（例：`jdbc:oracle:thin:@//localhost:1521/orcl`）。
     - **クラス名**: `oracle.jdbc.OracleDriver`を入力します。
     - **追加クラスパス**: **Add**をクリックし、Oracle JDBCドライバーJARファイルを選択します。
   - **OK**をクリックしてドライバーを保存します。

### 手順5: Squirrel SQLで接続（エイリアス）を作成する

抽出した詳細を使用して接続エイリアスを作成します。

1. **新しいエイリアスを追加する**:
   - Squirrel SQLの**Aliases**タブに移動します。
   - **+**ボタンをクリックして新しいエイリアスを追加します。
   - エイリアスを設定します：
     - **名前**: 接続の名前を入力します（例：「Oracle DB via WebSphere」）。
     - **ドライバー**: 設定したOracle JDBCドライバーを選択します。
     - **URL**: `server.xml`の`<properties.oracle>`要素からのJDBC URLを入力します（例：`jdbc:oracle:thin:@//localhost:1521/orcl`）。
     - **ユーザー名**: `server.xml`からのユーザー名を入力します（例：`scott`）。
     - **パスワード**: 手順3で得られたデコードされた平文パスワードを入力します。

2. **オプション：追加のプロパティ**:
   - `<properties.oracle>`要素に追加の属性（例：`ssl="true"`または`connectionTimeout="30000"`）が含まれている場合は、エイリアス設定の**Properties**タブに移動し、キーと値のペアとして追加します。

3. **接続をテストする**:
   - **Test Connection**をクリックして、Squirrel SQLがデータベースに接続できることを確認します。
   - 成功した場合は、**OK**をクリックしてエイリアスを保存します。

### JDBC URL

Squirrel SQLで使用するURLは、`server.xml`ファイルの`<properties.oracle>`要素の`url`属性の値です。例：
- `server.xml`に`<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>`が含まれている場合、以下を使用します：
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

このURLとユーザー名、デコードされたパスワードを組み合わせることで、Squirrel SQLがOracleデータベースに接続できます。

### 注意点

- **暗号化されたパスワード**: Squirrel SQLでは暗号化されたパスワードを直接使用できず、平文にデコードする必要があります。
- **DataSourceの範囲**: `server.xml`の`<dataSource>`はWebSphere Libertyで実行されるアプリケーションのために設計されています。Squirrel SQLは外部クライアントであり、これらの設定を手動で反映する必要があります。
- **JARの互換性**: Oracle JDBCドライバーJARのバージョンがデータベースバージョンと一致していることを確認してください。

これらの手順に従うことで、WebSphere Liberty Profileの`server.xml`で定義された設定を使用して、Squirrel SQLをOracleデータベースに成功させることができます。

---

WebSphere Libertyの`securityUtility`コマンドには、`server.xml`ファイル内のAES暗号化されたパスワード（例：`{aes}`プレフィックスが付いたもの）をデコードするオプションが含まれていないため、プログラム的なアプローチを使用してデコードする必要があります。推奨される方法は、Libertyランタイムに含まれる`com.ibm.websphere.crypto.PasswordUtil`クラスを利用してパスワードをデコードすることです。以下に2つの実用的なソリューションがあります。

### オプション1: 一時的なWebアプリケーションを使用する（推奨）

Libertyサーバーに簡単なWebアプリケーションをデプロイすることで、デコードロジックをサーバー環境内で実行し、正しい暗号化キー（デフォルトまたは`server.xml`で定義されたカスタムキー）へのアクセスを確保できます。

#### 手順:
1. **JSPファイルを作成する**
   `decode.jsp`という名前のファイルを以下の内容で作成します。
   ```jsp
   <%@ page import="com.ibm.websphere.crypto.PasswordUtil" %>
   <%
       String encoded = request.getParameter("encoded");
       if (encoded != null) {
           try {
               String decoded = PasswordUtil.decode(encoded);
               out.println("Decoded password: " + decoded);
           } catch (Exception e) {
               out.println("Error decoding password: " + e.getMessage());
           }
       }
   %>
   ```

2. **JSPをデプロイする**
   - `decode.jsp`をWebアプリケーションディレクトリ（例：`wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`）に配置します。
   - 必要に応じて、このJSPを含む基本的なWARファイルを作成し、Liberty管理コンソールまたは`dropins`ディレクトリにドロップしてデプロイします。

3. **JSPにアクセスする**
   - Libertyサーバーを起動します（`server start yourServer`）。
   - ブラウザを開き、以下のURLにアクセスします：
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}your_encrypted_password`
     `{aes}your_encrypted_password`を`server.xml`からの実際の暗号化されたパスワードに置き換えます。

4. **デコードされたパスワードを取得する**
   ページにはデコードされたパスワードが表示され、これを（例：Squirrel SQLでデータベースに接続するために）使用できます。

5. **アプリケーションをセキュリティ対策する**
   パスワードを取得したら、JSPを削除またはアクセスを制限して、未承認の使用を防ぎます。

#### なぜこれが機能するか:
サーバー内で実行することで、`PasswordUtil.decode()`が同じ暗号化キー（デフォルトまたはカスタムキー、`server.xml`の`wlp.password.encryption.key`で指定）を使用してパスワードをデコードすることが保証されます。

---

### オプション2: 独立したJavaプログラムを使用する

Webアプリケーションをデプロイすることができない場合、Libertyランタイムライブラリをクラスパスに含めて独立したJavaプログラムを作成し、実行することもできます。このアプローチは、特にカスタムキーが使用されている場合、暗号化キーの手動処理が必要なため、少し難しいです。

#### サンプルコード:
```java
import com.ibm.websphere.crypto.PasswordUtil;

public class PasswordDecoder {
    public static void main(String[] args) {
        if (args.length < 1 || args.length > 2) {
            System.out.println("Usage: java PasswordDecoder <encoded_password> [crypto_key]");
            return;
        }
        String encoded = args[0];
        String cryptoKey = args.length == 2 ? args[1] : null;
        try {
            String decoded;
            if (cryptoKey != null) {
                decoded = PasswordUtil.decode(encoded, cryptoKey);
            } else {
                decoded = PasswordUtil.decode(encoded);
            }
            System.out.println("Decoded password: " + decoded);
        } catch (Exception e) {
            System.err.println("Error decoding password: " + e.getMessage());
        }
    }
}
```

#### 手順:
1. **プログラムをコンパイルする**
   - コードを`PasswordDecoder.java`として保存します。
   - Libertyのjarを使用してコンパイルします：
     ```bash
     javac -cp /path/to/wlp/lib/* PasswordDecoder.java
     ```
     `/path/to/wlp`をLibertyインストールディレクトリ（例：`/opt/ibm/wlp`）に置き換えます。

2. **プログラムを実行する**
   - デフォルトキーでパスワードが暗号化されている場合：
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password"
     ```
   - カスタムキーが使用されている場合（例：`server.xml`に`<variable name="wlp.password.encryption.key" value="yourKey"/>`として定義）：
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password" "yourKey"
     ```

3. **出力を処理する**
   プログラムはデコードされたパスワードまたはキーが正しくない場合のエラーを出力します。

#### 注意点:
- Libertyのjar（例：`wlp/lib`）には`com.ibm.websphere.crypto.PasswordUtil`とその依存関係が含まれています。
- カスタムキーが使用され、それを提供しない場合、デコードは失敗します。`server.xml`または含まれる設定ファイルを確認してキーを確認してください。

---

### 重要な考慮事項

- **デフォルトキーとカスタムキー**:
  - `server.xml`に`wlp.password.encryption.key`が指定されていない場合、デフォルトキーが使用され、`PasswordUtil.decode(encoded)`は追加のパラメータなしで動作します。
  - カスタムキーが定義されている場合、外部（オプション2）でデコードする際には明示的に提供する必要があります。

- **セキュリティ**:
  デコードされたパスワードは平文で取り扱うため、ログに記録したり、不要に露出させたりしないように注意してください。

- **優先度**:
  オプション1（Webアプリケーション）は、通常よりも信頼性が高いです。サーバー環境内で実行されるため、キーと依存関係が自動的に処理されます。

これらの方法のいずれかを使用することで、`server.xml`からAES暗号化されたパスワードをデコードし、`securityUtility`コマンドにデコードオプションがない場合でも成功させることができます。