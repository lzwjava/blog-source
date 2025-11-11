---
audio: false
generated: true
lang: ja
layout: post
title: Oracleデータベース - ユーザーアカウント
translated: true
type: note
---

`ORA-28000: The account is locked` エラーは、Oracleデータベース（例：thin JDBCドライバ経由）への接続を試みた際に、使用しようとしているユーザーアカウントがロックされている場合に発生します。これは通常、ログイン失敗回数が多すぎる、管理者による手動ロック、またはアカウントの有効期限ポリシーが原因で発生します。この問題を解決するには、アカウントのロックを解除し、必要に応じてパスワードをリセットするか、アカウントステータスを確認する必要があります。以下は、Oracleデータベース接続時にこの問題を修正する手順です。

---

### ORA-28000 を修正する手順

#### 1. **エラーの確認**
   JDBC接続でこのエラーが発生すると、以下のように表示されることがあります:
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   これは、問題がJDBC設定自体（URL、ドライバ、WebSphereデータソース設定など）ではなく、データベースアカウントにあることを確認します。

#### 2. **権限を持つユーザーとしてログイン**
   アカウントのロックを解除するには、管理権限を持つデータベースユーザー（例: `SYS`、`SYSTEM`、または `DBA` ロールを持つユーザー）へのアクセス権が必要です。SQL*Plus、SQL Developer、またはJDBCクライアントなどのツールを使用してデータベースに接続します:
   ```bash
   sqlplus / as sysdba
   ```
   または
   ```bash
   sqlplus system/<password>@<service_name>
   ```
   `<password>` と `<service_name>` を実際の資格情報とデータベースサービス名（例: `ORCL`）に置き換えてください。

#### 3. **アカウントステータスの確認**
   次のSQLクエリを実行して、ロックされたアカウントのステータスを確認します:
   ```sql
   SELECT username, account_status, lock_date 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   - `YOUR_USERNAME` を接続に使用しているユーザー名（例: `myuser`）に置き換えてください。
   - `ACCOUNT_STATUS` 列を確認します。`LOCKED` または `LOCKED(TIMED)` と表示されている場合、アカウントはロックされています。

   出力例:
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MYUSER     LOCKED           24-MAR-25 10:00:00
   ```

#### 4. **アカウントのロック解除**
   権限を持つユーザーとして次のSQLコマンドを実行して、アカウントのロックを解除します:
   ```sql
   ALTER USER your_username ACCOUNT UNLOCK;
   ```
   例:
   ```sql
   ALTER USER myuser ACCOUNT UNLOCK;
   ```

#### 5. **（オプション）パスワードのリセット**
   パスワードの有効期限が切れている可能性がある場合、または正しくないと思われる場合は、合わせてリセットします:
   ```sql
   ALTER USER your_username IDENTIFIED BY new_password;
   ```
   例:
   ```sql
   ALTER USER myuser IDENTIFIED BY mynewpass123;
   ```
   - リセット後、WebSphereの `server.xml`（またはJDBCデータソースが設定されている場所）のパスワードを更新し、必要に応じて再暗号化します（AESエンコードの手順については前回の質問を参照してください）。

#### 6. **変更の確定（必要な場合）**
   ほとんどの場合、`ALTER USER` コマンドは即座に有効になり、`COMMIT` は必要ありません。ただし、トランザクションが頻繁な環境では、セッションまたはデータベースを再起動してロールバックが発生しないようにします。

#### 7. **接続のテスト**
   JDBCアプリケーションまたは簡単なテストを使用して、再度接続を試みます:
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "myuser";
           String password = "mynewpass123";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("Connection successful!");
           conn.close();
       }
   }
   ```
   - `url`、`user`、`password` を環境に合わせて更新してください。
   - これが機能する場合は、WebSphereデータソース設定を適宜更新してください。

#### 8. **プロファイルポリシーの確認（将来のロックを防止）**
   アカウントは、ユーザーに割り当てられたプロファイル内のセキュリティポリシー（例: `FAILED_LOGIN_ATTEMPTS` または `PASSWORD_LOCK_TIME`）が原因でロックされた可能性があります。ユーザーに割り当てられたプロファイルを確認します:
   ```sql
   SELECT profile 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   次に、プロファイルの制限を調査します:
   ```sql
   SELECT resource_name, limit 
   FROM dba_profiles 
   WHERE profile = 'YOUR_PROFILE_NAME';
   ```
   以下を探します:
   - `FAILED_LOGIN_ATTEMPTS`: ロック前の失敗した試行回数（例: `10`）。
   - `PASSWORD_LOCK_TIME`: ロック期間（例: `1` 日）。

   これらの設定を緩和する必要がある場合（適切であれば）、プロファイルを変更します:
   ```sql
   ALTER PROFILE your_profile_name LIMIT 
       FAILED_LOGIN_ATTEMPTS UNLIMITED 
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   例:
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **WebSphereの再起動（必要な場合）**
   WebSphereを使用していてデータソースのパスワードを更新した場合、変更が確実に適用されるようにアプリケーションサーバーを再起動します:
   - Libertyの場合: `./bin/server stop` および `./bin/server start`。
   - 従来型WebSphereの場合: 管理コンソールまたは `stopServer.sh`/`startServer.sh` を使用します。

---

### ORA-28000 の一般的な原因
- **ログイン失敗回数が多すぎる**: アプリケーションログまたはWebSphereログ（例: `SystemOut.log`）で以前の接続エラーを確認してください。
- **手動ロック**: 管理者が意図的にアカウントをロックした可能性があります（`ALTER USER myuser ACCOUNT LOCK`）。
- **アカウントの有効期限切れ**: 一部の環境では、パスワードの有効期限が切れるとアカウントがロックされます。`dba_users` の `EXPIRY_DATE` を確認してください。

---

### トラブルシューティングのヒント
- `SYS` または `SYSTEM` へのアクセス権がない場合は、データベース管理者に連絡してアカウントのロックを解除してください。
- 再試行する前に、`server.xml` 内のJDBC URL、ユーザー名、パスワードが正しいことを確認してください。
- 問題が解決しない場合は、Oracleリスナーが実行されていることを確認します:
  ```bash
  lsnrctl status
  ```

追加のエラーが発生した場合、または特定の手順についてサポートが必要な場合はお知らせください！