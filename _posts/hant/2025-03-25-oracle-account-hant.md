---
audio: false
generated: true
lang: hant
layout: post
title: Oracle 數據庫 - 用戶帳戶
translated: true
type: note
---

當嘗試連線至 Oracle 資料庫（例如透過 thin JDBC driver）時，若使用的使用者帳戶已被鎖定，便會出現 `ORA-28000: The account is locked` 錯誤。這通常是由於登入失敗次數過多、管理員手動鎖定，或帳戶到期政策所致。要解決此問題，您需要解鎖該帳戶，並在必要時重設密碼或檢查帳戶狀態。以下是在連線至 Oracle 資料庫時解決此問題的步驟。

---

### 解決 ORA-28000 的步驟

#### 1. **確認錯誤**
   在 JDBC 連線中遇到此錯誤時，可能會顯示如下：
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   這確認了問題在於資料庫帳戶，而非 JDBC 配置本身（例如 URL、驅動程式或 WebSphere 資料來源設定）。

#### 2. **以具權限使用者登入**
   要解鎖帳戶，您需要存取具有管理權限的資料庫使用者（例如 `SYS`、`SYSTEM` 或具有 `DBA` 角色的使用者）。使用如 SQL*Plus、SQL Developer 或 JDBC 用戶端等工具連線至資料庫：
   ```bash
   sqlplus / as sysdba
   ```
   或
   ```bash
   sqlplus system/<password>@<service_name>
   ```
   請將 `<password>` 和 `<service_name>` 替換為您的實際憑證和資料庫服務名稱（例如 `ORCL`）。

#### 3. **檢查帳戶狀態**
   執行以下 SQL 查詢以檢查被鎖定帳戶的狀態：
   ```sql
   SELECT username, account_status, lock_date 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   - 將 `YOUR_USERNAME` 替換為您嘗試連線的使用者名稱（例如 `myuser`）。
   - 查看 `ACCOUNT_STATUS` 欄位。若顯示為 `LOCKED` 或 `LOCKED(TIMED)`，表示帳戶已被鎖定。

   範例輸出：
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MYUSER     LOCKED           24-MAR-25 10:00:00
   ```

#### 4. **解鎖帳戶**
   以具權限使用者身份執行以下 SQL 指令來解鎖帳戶：
   ```sql
   ALTER USER your_username ACCOUNT UNLOCK;
   ```
   範例：
   ```sql
   ALTER USER myuser ACCOUNT UNLOCK;
   ```

#### 5. **（可選）重設密碼**
   若密碼可能已過期或您懷疑其不正確，可同時重設密碼：
   ```sql
   ALTER USER your_username IDENTIFIED BY new_password;
   ```
   範例：
   ```sql
   ALTER USER myuser IDENTIFIED BY mynewpass123;
   ```
   - 重設後，請在您的 WebSphere `server.xml`（或 JDBC 資料來源配置所在位置）中更新密碼，並在必要時重新加密（請參閱您先前的問題以了解 AES 編碼步驟）。

#### 6. **提交變更（如需要）**
   在多數情況下，`ALTER USER` 指令會立即生效，無需 `COMMIT`。然而，若您處於交易頻繁的環境中，請確保不會發生回滾，必要時可重新啟動工作階段或資料庫。

#### 7. **測試連線**
   再次嘗試使用您的 JDBC 應用程式或簡單測試進行連線：
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
   - 更新 `url`、`user` 和 `password` 以符合您的環境。
   - 若測試成功，請相應地更新您的 WebSphere 資料來源配置。

#### 8. **檢查設定檔政策（預防未來鎖定）**
   帳戶可能因使用者設定檔中的安全政策而被鎖定（例如 `FAILED_LOGIN_ATTEMPTS` 或 `PASSWORD_LOCK_TIME`）。檢查指派給使用者的設定檔：
   ```sql
   SELECT profile 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   然後，檢查該設定檔的限制：
   ```sql
   SELECT resource_name, limit 
   FROM dba_profiles 
   WHERE profile = 'YOUR_PROFILE_NAME';
   ```
   尋找：
   - `FAILED_LOGIN_ATTEMPTS`：鎖定前的失敗嘗試次數（例如 `10`）。
   - `PASSWORD_LOCK_TIME`：鎖定持續時間（例如 `1` 天）。

   若要放寬這些設定（如適用），修改設定檔：
   ```sql
   ALTER PROFILE your_profile_name LIMIT 
       FAILED_LOGIN_ATTEMPTS UNLIMITED 
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   範例：
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **重新啟動 WebSphere（如需要）**
   若您使用 WebSphere 並更新了資料來源密碼，請重新啟動應用程式伺服器以確保變更生效：
   - 對於 Liberty：`./bin/server stop` 和 `./bin/server start`。
   - 對於傳統 WebSphere：使用 Admin Console 或 `stopServer.sh`/`startServer.sh`。

---

### ORA-28000 的常見原因
- **登入失敗次數過多**：檢查應用程式日誌或 WebSphere 日誌（例如 `SystemOut.log`）中先前的連線錯誤。
- **手動鎖定**：管理員可能有意鎖定了帳戶（`ALTER USER myuser ACCOUNT LOCK`）。
- **帳戶到期**：某些環境在密碼到期時會鎖定帳戶。檢查 `dba_users` 中的 `EXPIRY_DATE`。

---

### 疑難排解提示
- 若您沒有 `SYS` 或 `SYSTEM` 存取權限，請聯絡您的資料庫管理員以解鎖帳戶。
- 在重試前，請確保 `server.xml` 中的 JDBC URL、使用者名稱和密碼正確無誤。
- 若問題持續存在，請確認 Oracle listener 正在執行：
  ```bash
  lsnrctl status
  ```

如果您遇到其他錯誤或需要特定步驟的協助，請告知！