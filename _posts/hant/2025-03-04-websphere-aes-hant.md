---
audio: false
generated: true
lang: hant
layout: post
title: 使用 AES 加密密碼在 WebSphere Liberty
translated: true
---

在 WebSphere Liberty 的 `server.xml` 中使用 AES 加密的密碼在 Squirrel SQL Client 中，請按照以下步驟進行：

---

### **1. 使用 WebSphere Liberty 的工具解密密碼**
加密的密碼（例如 `password="{aes}ABC123..."`）必須先解密。如果您有訪問用於加密的密鑰存儲，Liberty 的 `securityUtility` 工具可以完成這項工作。

#### **解密命令：**
```bash
# 導航到 Liberty 的 bin 目錄
cd /path/to/wlp/bin

# 運行 securityUtility 解碼命令
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

替換：
- `<LibertyServerPath>`：您的 Liberty 伺服器的路徑（例如 `usr/servers/defaultServer`）。
- `<KeyAlias>`：密鑰存儲中的密鑰別名（預設：`default`）。
- `<KeystorePassword>`：密鑰存儲的密碼（預設：`KeystorePass` 如果未更改）。
- `{aes}ABC123...`：來自 `server.xml` 的加密密碼。

---

### **2. 在 Squirrel 中使用解密後的密碼**
1. 打開 Squirrel SQL Client。
2. 創建一個新的連接別名。
3. 在連接屬性中：
   - **Driver**：選擇您的 Oracle JDBC 驅動程序。
   - **URL**：使用來自 Liberty 的 `server.xml` 的 JDBC URL（例如 `jdbc:oracle:thin:@//host:port/service`）。
   - **Username**：來自 Liberty 的 `<dataSource>` 的用戶名。
   - **Password**：輸入從步驟 1 获得的 **解密密碼**。

---

### **重要說明**
- **密鑰存儲訪問**：您需要密鑰存儲文件（`key.jks` 或 `key.p12`）及其密碼。預設情況下，它位於 Liberty 的 `resources/security` 目錄中。
- **安全性**：永遠不要以純文本形式存儲解密後的密碼。直接在 Squirrel 中輸入，而不將其保存到文件中。
- **管理員幫助**：如果您沒有密鑰存儲憑證，請聯繫您的 Liberty 管理員以安全地解密密碼。

---

### **替代方法（不推薦）**
如果解密不可行，請暫時在 `server.xml` 中將加密密碼替換為純文本密碼（僅用於測試）。重新啟動 Liberty 並在 Squirrel 中使用純文本密碼。完成後恢復加密密碼。

```xml
<!-- 示例：純文本密碼（避免在生產環境中使用） -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

按照這些步驟，您可以在 Squirrel 中安全地使用解密後的密碼，同時遵守安全最佳實踐。

---

要將 Squirrel SQL 客戶端連接到 Oracle 資料庫，使用 WebSphere Liberty Profile 的 `server.xml` 文件中指定的配置，特別是當 Oracle JDBC 驅動程序屬性包括 AES 加密密碼時，請按照以下步驟進行。該過程涉及從 `server.xml` 文件中提取連接詳細信息，處理加密密碼，並適當配置 Squirrel SQL。以下是完整指南：

### 步驟 1：了解 `server.xml` 配置
在 WebSphere Liberty Profile 中，資料庫連接在 `server.xml` 文件中使用 `<dataSource>` 元素定義。該元素指定資料源屬性，包括通過嵌套的 `<properties.oracle>` 元素的 Oracle 資料庫。示例配置可能如下所示：

```xml
<dataSource jndiName="jdbc/myOracleDS">
    <jdbcDriver libraryRef="OracleLib"/>
    <properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" user="scott" password="{aes}encrypted_password"/>
</dataSource>
<library id="OracleLib">
    <fileset dir="${server.config.dir}/lib" includes="ojdbc6.jar"/>
</library>
```

其中：
- **`url`**：連接到 Oracle 資料庫的 JDBC URL（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
- **`user`**：資料庫用戶名（例如 `scott`）。
- **`password`**：使用 AES 加密的密碼，前綴為 `{aes}`（例如 `{aes}encrypted_password`）。
- **`<jdbcDriver>`**：參考 Oracle JDBC 驅動程序 JAR 文件。

由於 Squirrel SQL 是獨立客戶端，無法直接訪問 WebSphere 管理的資料源（例如通過 JNDI 查找），您需要手動配置它，使用相同的連接詳細信息。

### 步驟 2：從 `server.xml` 提取連接詳細信息
在您的 `server.xml` 文件中，找到與您的 Oracle 資料庫對應的 `<dataSource>` 元素。從 `<properties.oracle>` 元素中，注意以下內容：
- **JDBC URL**：在 `url` 屬性中找到（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
- **Username**：在 `user` 屬性中找到（例如 `scott`）。
- **加密密碼**：在 `password` 屬性中找到（例如 `{aes}encrypted_password`）。

JDBC URL 指定如何連接到 Oracle 資料庫，通常格式如下：
- `jdbc:oracle:thin:@//hostname:port/service_name`（使用服務名）
- `jdbc:oracle:thin:@hostname:port:SID`（使用 SID）

檢查您的 `server.xml` 以確認確切的 URL。

### 步驟 3：解碼 AES 加密密碼
`server.xml` 中的密碼使用 AES 加密，如 `{aes}` 前綴所示。WebSphere Liberty Profile 為安全起見加密密碼，但 Squirrel SQL 需要純文本密碼來建立連接。要解碼加密密碼：

1. **使用 WebSphere 的 `securityUtility` 工具**：
   - 該工具隨 WebSphere Liberty 安裝一起提供，通常位於 `bin` 目錄（例如 `<liberty_install_dir>/bin/`）。
   - 在終端或命令提示符中從 `bin` 目錄運行以下命令：
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     將 `<encrypted_password>` 替換為 `password` 屬性中的實際加密字符串（`{aes}` 後面的所有內容）。例如：
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - 工具將輸出純文本密碼。

2. **替代方法**：
   - 如果您無法訪問 WebSphere Liberty 安裝或 `securityUtility` 工具，您需要從系統管理員或配置資料源的人那裡獲取純文本密碼。

安全保存解碼密碼，因為您將在 Squirrel SQL 中需要它。

### 步驟 4：在 Squirrel SQL 中配置 Oracle JDBC 驅動程序
Squirrel SQL 需要 Oracle JDBC 驅動程序來連接到資料庫。您需要與 `server.xml` 中 `<library>` 元素中指定的相同驅動程序 JAR 文件（例如 `ojdbc6.jar`）。

1. **獲取驅動程序 JAR**：
   - 找到 `server.xml` 中 `<fileset>` 元素中指定的 Oracle JDBC 驅動程序 JAR 文件（例如 `ojdbc6.jar` 在 `${server.config.dir}/lib`）。
   - 如果您沒有它，請從 Oracle 網站下載適當的版本（例如 `ojdbc6.jar` 或 `ojdbc8.jar`，與您的資料庫版本匹配）。

2. **將驅動程序添加到 Squirrel SQL**：
   - 打開 Squirrel SQL。
   - 轉到左側的 **Drivers** 選項卡。
   - 點擊 **+** 按鈕以添加新驅動程序。
   - 配置驅動程序：
     - **Name**：輸入一個名稱（例如 “Oracle JDBC Driver”）。
     - **Example URL**：輸入示例 URL（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
     - **Class Name**：輸入 `oracle.jdbc.OracleDriver`。
     - **Extra Class Path**：點擊 **Add**，然後瀏覽並選擇 Oracle JDBC 驅動程序 JAR 文件。
   - 點擊 **OK** 以保存驅動程序。

### 步驟 5：在 Squirrel SQL 中創建連接（別名）
現在，使用提取的詳細信息創建連接別名：

1. **添加新別名**：
   - 轉到 Squirrel SQL 的 **Aliases** 選項卡。
   - 點擊 **+** 按鈕以添加新別名。
   - 配置別名：
     - **Name**：為連接輸入一個名稱（例如 “Oracle DB via WebSphere”）。
     - **Driver**：選擇您剛剛配置的 Oracle JDBC 驅動程序。
     - **URL**：輸入來自 `server.xml` `<properties.oracle>` 元素的 JDBC URL（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
     - **Username**：輸入來自 `server.xml` 的用戶名（例如 `scott`）。
     - **Password**：輸入從步驟 3 获得的解碼純文本密碼。

2. **可選：額外屬性**：
   - 如果 `server.xml` 中的 `<properties.oracle>` 元素包含額外屬性（例如 `ssl="true"` 或 `connectionTimeout="30000"`），點擊別名配置中的 **Properties** 選項卡，並將它們添加為鍵值對。

3. **測試連接**：
   - 點擊 **Test Connection** 以驗證 Squirrel SQL 是否可以連接到資料庫。
   - 如果成功，點擊 **OK** 以保存別名。

### JDBC URL
在 Squirrel SQL 中使用的 URL 是 `server.xml` 文件中 `<properties.oracle>` 元素的 `url` 屬性的值。例如：
- 如果 `server.xml` 有 `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>`，則使用：
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

該 URL 結合用戶名和解碼密碼，使 Squirrel SQL 能夠連接到 Oracle 資料庫。

### 說明
- **加密密碼**：您無法直接在 Squirrel SQL 中使用加密密碼；它必須解碼為純文本。
- **DataSource 範圍**：`server.xml` 中的 `<dataSource>` 設計用於在 WebSphere Liberty 中運行的應用程序。Squirrel SQL 作為外部客戶端，需要手動配置，鏡像這些設置。
- **JAR 兼容性**：確保 Oracle JDBC 驅動程序 JAR 版本與您的資料庫版本兼容。

按照這些步驟，您可以成功配置 Squirrel SQL 連接到使用 WebSphere Liberty Profile 的 `server.xml` 中定義的屬性的 Oracle 資料庫。

---

由於 WebSphere Liberty 的 `securityUtility` 命令不提供用於解碼 AES 加密密碼（例如在 `server.xml` 文件中以 `{aes}` 為前綴的密碼）的解碼選項，您需要使用程序化方法來解碼它們。推薦的方法是利用 `com.ibm.websphere.crypto.PasswordUtil` 類，該類是 Liberty 運行時的一部分，並且可以解碼這些密碼。以下是兩種實際解決方案：

### 選項 1：使用臨時 Web 應用程序（推薦）
在 Liberty 伺服器上部署簡單的 Web 應用程序，允許您在伺服器環境中運行解碼邏輯，從而確保訪問正確的加密密鑰（默認或自定義，如 `server.xml` 中定義）。

#### 步驟：
1. **創建一個 JSP 文件**
   創建一個名為 `decode.jsp` 的文件，內容如下：
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

2. **部署 JSP**
   - 將 `decode.jsp` 放置在 Web 應用程序目錄中，例如 `wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`。
   - 如果需要，創建一個基本的 WAR 文件，其中包含這個 JSP，並使用 Liberty 管理控制台或將其放置在 `dropins` 目錄中部署它。

3. **訪問 JSP**
   - 啟動您的 Liberty 伺服器（`server start yourServer`）。
   - 打開瀏覽器並導航到：
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}your_encrypted_password`
     將 `{aes}your_encrypted_password` 替換為 `server.xml` 中的實際加密密碼。

4. **檢索解碼密碼**
   該頁面將顯示解密後的密碼，您可以將其用於（例如在 Squirrel SQL 中連接到資料庫）。

5. **保護應用程序**
   獲取密碼後，移除或限制對 JSP 的訪問，以防止未經授權的使用。

#### 為什麼這樣有效：
在 Liberty 伺服器內運行確保 `PasswordUtil.decode()` 使用相同的加密密鑰（默認或自定義，通過 `wlp.password.encryption.key` 在 `server.xml` 中指定）來編碼密碼。

---

### 選項 2：使用獨立的 Java 程序
如果部署 Web 應用程序不可行，您可以編寫獨立的 Java 程序並使用 Liberty 運行時庫在類路徑中運行它。這種方法更加棘手，因為它需要手動處理加密密鑰，特別是如果使用了自定義密鑰。

#### 示例代碼：
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

#### 步驟：
1. **編譯程序**
   - 將代碼保存為 `PasswordDecoder.java`。
   - 使用 Liberty 的 jar 文件編譯它：
     ```bash
     javac -cp /path/to/wlp/lib/* PasswordDecoder.java
     ```
     將 `/path/to/wlp` 替換為您的 Liberty 安裝目錄（例如 `/opt/ibm/wlp`）。

2. **運行程序**
   - 如果密碼是使用默認密鑰加密的：
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password"
     ```
   - 如果使用了自定義密鑰（例如在 `server.xml` 中定義為 `<variable name="wlp.password.encryption.key" value="yourKey"/>`）：
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password" "yourKey"
     ```

3. **處理輸出**
   程序將打印解碼後的密碼或錯誤（如果密鑰不正確）。

#### 說明：
- Liberty jar 文件（例如在 `wlp/lib` 中）包含 `com.ibm.websphere.crypto.PasswordUtil` 及其依賴項。
- 如果使用了自定義密鑰且您未提供它，解碼將失敗。檢查 `server.xml` 或包含的配置文件以獲取密鑰。

---

### 關鍵考量
- **默認與自定義密鑰**：
  - 如果 `server.xml` 中未指定 `wlp.password.encryption.key`，則使用默認密鑰，並且 `PasswordUtil.decode(encoded)` 應該在不附加參數的情況下工作。
  - 如果定義了自定義密鑰，您必須在解碼時明確提供它（選項 2）或依賴伺服器上下文（選項 1）。

- **安全性**：
  小心處理解碼後的密碼，因為它將以純文本形式存在。避免記錄它或不必要地暴露它。

- **偏好**：
  選項 1（Web 應用程序）通常更可靠，因為它在 Liberty 環境中運行，自動處理密鑰和依賴項。

按照任何一種方法，您可以成功解碼 `server.xml` 中的 AES 加密密碼，儘管 `securityUtility` 沒有解碼選項。