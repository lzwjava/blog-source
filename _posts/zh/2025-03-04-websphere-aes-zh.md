---
audio: false
generated: true
lang: zh
layout: post
title: 使用AES加密密码的WebSphere Liberty
translated: true
---

使用 WebSphere Liberty 的 `server.xml` 中的 AES 加密密码在 Squirrel SQL 客户端中，请按照以下步骤进行操作：

---

### **1. 使用 WebSphere Liberty 的工具解密密码**
首先必须解密密码（例如 `password="{aes}ABC123..."`）。如果您有访问用于加密的密钥库，Liberty 的 `securityUtility` 工具可以完成此操作。

#### **解密命令：**
```bash
# 导航到 Liberty 的 bin 目录
cd /path/to/wlp/bin

# 运行 securityUtility 解码命令
./securityUtility decode \
  --server=<LibertyServerPath> \
  --key=<KeyAlias> \
  --keyPassword=<KeystorePassword> \
  --source="{aes}ABC123..."
```

替换：
- `<LibertyServerPath>`：Liberty 服务器的路径（例如 `usr/servers/defaultServer`）。
- `<KeyAlias>`：密钥库中的密钥别名（默认：`default`）。
- `<KeystorePassword>`：密钥库的密码（默认：`KeystorePass` 如果未更改）。
- `{aes}ABC123...`：`server.xml` 中的加密密码。

---

### **2. 在 Squirrel 中使用解密后的密码**
1. 打开 Squirrel SQL 客户端。
2. 创建一个新的连接别名。
3. 在连接属性中：
   - **驱动程序**：选择您的 Oracle JDBC 驱动程序。
   - **URL**：使用 Liberty 的 `server.xml` 中的 JDBC URL（例如 `jdbc:oracle:thin:@//host:port/service`）。
   - **用户名**：Liberty 的 `<dataSource>` 中的用户名。
   - **密码**：输入从步骤 1 获得的 **解密后的密码**。

---

### **重要说明**
- **密钥库访问**：您需要密钥库文件（`key.jks` 或 `key.p12`）及其密码。默认情况下，它位于 Liberty 的 `resources/security` 目录中。
- **安全性**：永远不要以纯文本形式存储解密后的密码。直接在 Squirrel 中输入，而不将其保存到文件中。
- **管理员帮助**：如果您没有密钥库凭据，请联系您的 Liberty 管理员以安全地解密密码。

---

### **替代方法（不推荐）**
如果解密不可行，请暂时在 `server.xml` 中将加密密码替换为纯文本密码（仅用于测试）。重新启动 Liberty，并在 Squirrel 中使用纯文本密码。之后恢复为加密密码。

```xml
<!-- 示例：纯文本密码（避免在生产环境中使用） -->
<dataSource ...>
  <properties password="plaintextPassword" />
</dataSource>
```

---

通过遵循这些步骤，您可以在遵守安全最佳实践的同时，安全地在 Squirrel 中使用解密后的密码。

---

要将 Squirrel SQL 客户端连接到 Oracle 数据库，使用 WebSphere Liberty Profile 的 `server.xml` 文件中指定的配置，特别是当 Oracle JDBC 驱动程序属性包括 AES 加密密码时，请按照以下步骤进行操作。该过程涉及从 `server.xml` 文件中提取连接详细信息，处理加密密码，并适当配置 Squirrel SQL。以下是完整指南：

### 步骤 1：了解 `server.xml` 配置
在 WebSphere Liberty Profile 中，数据库连接在 `server.xml` 文件中使用 `<dataSource>` 元素定义。该元素指定数据源属性，包括通过嵌套的 `<properties.oracle>` 元素指定的 Oracle 数据库。示例配置可能如下所示：

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
- **`url`**：连接到 Oracle 数据库的 JDBC URL（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
- **`user`**：数据库用户名（例如 `scott`）。
- **`password`**：使用 AES 加密的密码，前缀为 `{aes}`（例如 `{aes}encrypted_password`）。
- **`<jdbcDriver>`**：引用 Oracle JDBC 驱动程序 JAR 文件。

由于 Squirrel SQL 是独立客户端，无法直接访问 WebSphere 管理的数据源（例如通过 JNDI 查找），因此需要手动配置它，使用相同的连接详细信息。

### 步骤 2：从 `server.xml` 提取连接详细信息
在 `server.xml` 文件中，找到与您的 Oracle 数据库对应的 `<dataSource>` 元素。从 `<properties.oracle>` 元素中，注意以下内容：
- **JDBC URL**：在 `url` 属性中找到（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
- **用户名**：在 `user` 属性中找到（例如 `scott`）。
- **加密密码**：在 `password` 属性中找到（例如 `{aes}encrypted_password`）。

JDBC URL 指定如何连接到 Oracle 数据库，通常格式如下：
- `jdbc:oracle:thin:@//hostname:port/service_name`（使用服务名称）
- `jdbc:oracle:thin:@hostname:port:SID`（使用 SID）

检查您的 `server.xml` 以确认确切的 URL。

### 步骤 3：解码 AES 加密密码
`server.xml` 中的密码使用 AES 加密，如 `{aes}` 前缀所示。WebSphere Liberty Profile 为安全起见加密密码，但 Squirrel SQL 需要纯文本密码来建立连接。要解码加密密码：

1. **使用 WebSphere 的 `securityUtility` 工具**：
   - 该工具包含在您的 WebSphere Liberty 安装中，通常位于 `bin` 目录（例如 `<liberty_install_dir>/bin/`）。
   - 在终端或命令提示符中从 `bin` 目录运行以下命令：
     ```
     securityUtility decode --encoding=aes <encrypted_password>
     ```
     将 `<encrypted_password>` 替换为 `password` 属性中的实际加密字符串（`{aes}` 后的所有内容）。例如：
     ```
     securityUtility decode --encoding=aes encrypted_password
     ```
   - 工具将输出纯文本密码。

2. **替代方法**：
   - 如果您无法访问 WebSphere Liberty 安装或 `securityUtility` 工具，请联系您的系统管理员或配置数据源的人员获取纯文本密码。

安全保存解码后的密码，因为您将在 Squirrel SQL 中需要它。

### 步骤 4：在 Squirrel SQL 中配置 Oracle JDBC 驱动程序
Squirrel SQL 需要 Oracle JDBC 驱动程序才能连接到数据库。您需要与 `server.xml` 中 `<library>` 元素中引用的相同驱动程序 JAR 文件（例如 `ojdbc6.jar`）。

1. **获取驱动程序 JAR**：
   - 在 `server.xml` 的 `<fileset>` 元素中找到 Oracle JDBC 驱动程序 JAR 文件（例如 `ojdbc6.jar` 在 `${server.config.dir}/lib`）。
   - 如果没有，请从 Oracle 网站下载相应版本（例如 `ojdbc6.jar` 或 `ojdbc8.jar`，与数据库版本匹配）。

2. **将驱动程序添加到 Squirrel SQL**：
   - 打开 Squirrel SQL。
   - 转到左侧的 **驱动程序** 选项卡。
   - 点击 **+** 按钮添加新驱动程序。
   - 配置驱动程序：
     - **名称**：输入名称（例如 “Oracle JDBC 驱动程序”）。
     - **示例 URL**：输入示例 URL（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
     - **类名称**：输入 `oracle.jdbc.OracleDriver`。
     - **额外类路径**：点击 **添加**，然后浏览并选择 Oracle JDBC 驱动程序 JAR 文件。
   - 点击 **确定** 保存驱动程序。

### 步骤 5：在 Squirrel SQL 中创建连接（别名）
现在，使用提取的详细信息创建连接别名：

1. **添加新别名**：
   - 转到 Squirrel SQL 的 **别名** 选项卡。
   - 点击 **+** 按钮添加新别名。
   - 配置别名：
     - **名称**：为连接输入名称（例如 “通过 WebSphere 的 Oracle DB”）。
     - **驱动程序**：选择您刚刚配置的 Oracle JDBC 驱动程序。
     - **URL**：输入 `server.xml` 中 `<properties.oracle>` 元素的 JDBC URL（例如 `jdbc:oracle:thin:@//localhost:1521/orcl`）。
     - **用户名**：输入 `server.xml` 中的用户名（例如 `scott`）。
     - **密码**：输入步骤 3 中获取的解码后的纯文本密码。

2. **可选：额外属性**：
   - 如果 `server.xml` 中的 `<properties.oracle>` 元素包含额外属性（例如 `ssl="true"` 或 `connectionTimeout="30000"`），点击别名配置中的 **属性** 选项卡，并将它们添加为键值对。

3. **测试连接**：
   - 点击 **测试连接** 以验证 Squirrel SQL 是否可以连接到数据库。
   - 如果成功，点击 **确定** 保存别名。

### JDBC URL
在 Squirrel SQL 中使用的 URL 是 `server.xml` 文件中 `<properties.oracle>` 元素的 `url` 属性的值。例如：
- 如果 `server.xml` 有 `<properties.oracle url="jdbc:oracle:thin:@//localhost:1521/orcl" .../>`，则使用：
  ```
  jdbc:oracle:thin:@//localhost:1521/orcl
  ```

该 URL 与用户名和解码后的密码一起，使 Squirrel SQL 能够连接到 Oracle 数据库。

### 说明
- **加密密码**：您不能直接在 Squirrel SQL 中使用加密密码；它必须解码为纯文本。
- **DataSource 范围**：`server.xml` 中的 `<dataSource>` 旨在为在 WebSphere Liberty 中运行的应用程序。Squirrel SQL 作为外部客户端，需要手动配置以镜像这些设置。
- **JAR 兼容性**：确保 Oracle JDBC 驱动程序 JAR 版本与数据库版本兼容。

通过遵循这些步骤，您可以成功配置 Squirrel SQL 以使用 WebSphere Liberty Profile 的 `server.xml` 中定义的属性连接到 Oracle 数据库。

---

由于 WebSphere Liberty 的 `securityUtility` 命令不提供用于解码 AES 加密密码（例如在 `server.xml` 文件中以 `{aes}` 为前缀的密码）的解码选项，因此需要使用编程方法来解密它们。推荐的方法是利用 `com.ibm.websphere.crypto.PasswordUtil` 类，它是 Liberty 运行时的一部分，可以解码这些密码。以下是两种实用的解决方案：

### 选项 1：使用临时 Web 应用程序（推荐）
在 Liberty 服务器上部署一个简单的 Web 应用程序，可以在服务器环境中运行解码逻辑，从而确保访问正确的加密密钥（默认或自定义，如 `server.xml` 中定义）。

#### 步骤：
1. **创建一个 JSP 文件**
   创建一个名为 `decode.jsp` 的文件，内容如下：
   ```jsp
   <%@ page import="com.ibm.websphere.crypto.PasswordUtil" %>
   <%
       String encoded = request.getParameter("encoded");
       if (encoded != null) {
           try {
               String decoded = PasswordUtil.decode(encoded);
               out.println("解码后的密码: " + decoded);
           } catch (Exception e) {
               out.println("解码密码时出错: " + e.getMessage());
           }
       }
   %>
   ```

2. **部署 JSP**
   - 将 `decode.jsp` 放置在 Web 应用程序目录中，例如 `wlp/usr/servers/yourServer/apps/myApp.war/WEB-INF/`。
   - 如果需要，创建一个基本的 WAR 文件，其中包含此 JSP，并使用 Liberty 管理控制台或将其放置在 `dropins` 目录中进行部署。

3. **访问 JSP**
   - 启动您的 Liberty 服务器（`server start yourServer`）。
   - 打开浏览器并导航到：
     `http://localhost:9080/myApp/decode.jsp?encoded={aes}your_encrypted_password`
     将 `{aes}your_encrypted_password` 替换为 `server.xml` 中的实际加密密码。

4. **检索解码后的密码**
   页面将显示解密后的密码，您可以将其用于（例如在 Squirrel SQL 中连接到数据库）。

5. **保护应用程序**
   获取密码后，删除或限制对 JSP 的访问，以防止未经授权的使用。

#### 为什么有效：
在 Liberty 服务器中运行确保 `PasswordUtil.decode()` 使用与编码密码相同的加密密钥（默认或自定义，通过 `wlp.password.encryption.key` 在 `server.xml` 中指定）。

---

### 选项 2：使用独立的 Java 程序
如果部署 Web 应用程序不可行，可以编写独立的 Java 程序并在运行时库在类路径中运行它。这种方法更复杂，因为它需要手动处理加密密钥，特别是如果使用了自定义密钥。

#### 示例代码：
```java
import com.ibm.websphere.crypto.PasswordUtil;

public class PasswordDecoder {
    public static void main(String[] args) {
        if (args.length < 1 || args.length > 2) {
            System.out.println("用法: java PasswordDecoder <encoded_password> [crypto_key]");
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
            System.out.println("解码后的密码: " + decoded);
        } catch (Exception e) {
            System.err.println("解码密码时出错: " + e.getMessage());
        }
    }
}
```

#### 步骤：
1. **编译程序**
   - 将代码保存为 `PasswordDecoder.java`。
   - 使用 Liberty 的 jar 进行编译：
     ```bash
     javac -cp /path/to/wlp/lib/* PasswordDecoder.java
     ```
     将 `/path/to/wlp` 替换为您的 Liberty 安装目录（例如 `/opt/ibm/wlp`）。

2. **运行程序**
   - 如果密码是使用默认密钥加密的：
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password"
     ```
   - 如果使用了自定义密钥（例如在 `server.xml` 中定义为 `<variable name="wlp.password.encryption.key" value="yourKey"/>`）：
     ```bash
     java -cp /path/to/wlp/lib/*:. PasswordDecoder "{aes}your_encrypted_password" "yourKey"
     ```

3. **处理输出**
   程序将打印解码后的密码或错误（如果密钥不正确）。

#### 说明：
- Liberty jar（例如在 `wlp/lib` 中）包含 `com.ibm.websphere.crypto.PasswordUtil` 及其依赖项。
- 如果使用了自定义密钥且您未提供它，则解码将失败。检查 `server.xml` 或包含的配置文件以获取密钥。

---

### 关键考虑
- **默认与自定义密钥**：
  - 如果 `server.xml` 中未指定 `wlp.password.encryption.key`，则使用默认密钥，并且 `PasswordUtil.decode(encoded)` 应该在不附加参数的情况下工作。
  - 如果定义了自定义密钥，则在外部解码时（选项 2）必须显式提供它，或者依赖服务器上下文（选项 1）。

- **安全性**：
  请小心处理解码后的密码，因为它将以纯文本形式出现。避免记录它或不必要地暴露它。

- **偏好**：
  选项 1（Web 应用程序）通常更可靠，因为它在 Liberty 环境中运行，自动处理密钥和依赖项。

通过遵循任何一种方法，您可以成功解码 `server.xml` 中的 AES 加密密码，尽管 `securityUtility` 中没有解码选项。