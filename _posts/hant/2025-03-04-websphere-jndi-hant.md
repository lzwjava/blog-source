---
audio: false
generated: true
lang: hant
layout: post
title: JNDI 資料來源配置於 WebSphere Liberty
translated: true
---

要確定一個 EAR Java 程序是否使用在 WebSphere Liberty 中 `server.xml` 文件中定義的數據源，您需要驗證應用程序是否通過一個對應於在伺服器配置中定義的數據源的 JNDI（Java Naming and Directory Interface）名稱來訪問數據源，具體來說是 `server.xml` 文件或它包含的任何文件。以下是一個分步指南來幫助您確認這一點：

### 第 1 步：識別應用程序使用的 JNDI 名稱
首先要找出 EAR 應用程序使用的 JNDI 名稱來查找其數據源。在以 EAR 文件部署的 Java EE 應用程序中，這可以在多個地方指定：

- **部署描述符**：檢查應用程序的部署描述符，例如 `web.xml`（用於 Web 模組）或 `ejb-jar.xml`（用於 EJB 模組），查找 `<resource-ref>` 元素。該元素聲明應用程序用來訪問數據源的資源引用。例如：

  ```xml
  <resource-ref>
      <res-ref-name>jdbc/myDataSource</res-ref-name>
      <res-type>javax.sql.DataSource</res-type>
      <res-auth>Container</res-auth>
  </resource-ref>
  ```

  這裡，應用程序使用 JNDI 名稱 `java:comp/env/jdbc/myDataSource` 查找數據源。

- **綁定文件**：在 WebSphere Liberty 中，部署描述符中的資源引用可能會綁定到伺服器通過綁定文件（如 `ibm-web-bnd.xml`（用於 Web 模組）或 `ibm-ejb-jar-bnd.xml`（用於 EJB））定義的實際 JNDI 名稱。查找 `<resource-ref>` 綁定，例如：

  ```xml
  <resource-ref name="jdbc/myDataSource" binding-name="jdbc/actualDataSource"/>
  ```

  這裡，應用程序的引用 `jdbc/myDataSource` 被映射到伺服器的 JNDI 名稱 `jdbc/actualDataSource`。

- **應用程序代碼**：如果您有訪問源代碼的權限，搜索 JNDI 查找或註解：
  - **JNDI 查找**：查找類似以下的代碼：

    ```java
    Context ctx = new InitialContext();
    DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/myDataSource");
    ```

    這表明 JNDI 名稱 `java:comp/env/jdbc/myDataSource`。

  - **註解**：在現代 Java EE 應用程序中，可能會使用 `@Resource` 註解，例如：

    ```java
    @Resource(name = "jdbc/myDataSource")
    private DataSource ds;
    ```

    這也指向 `java:comp/env/jdbc/myDataSource`。

如果不存在綁定文件，代碼或部署描述符中的 JNDI 名稱（例如 `jdbc/myDataSource`）可能直接對應於伺服器配置中預期的名稱。

### 第 2 步：檢查 `server.xml` 配置
一旦您確定了應用程序使用的 JNDI 名稱（直接或通過綁定），檢查 WebSphere Liberty 的 `server.xml` 文件（以及通過 `<include>` 元素包含的任何配置文件）是否有匹配的數據源定義。`server.xml` 中的數據源通常使用 `<dataSource>` 元素定義，例如：

```xml
<dataSource id="myDataSource" jndiName="jdbc/myDataSource">
    <jdbcDriver libraryRef="myDBLib"/>
    <properties url="jdbc:mysql://localhost:3306/mydb" user="user" password="pass"/>
</dataSource>
```

- 查找 `jndiName` 屬性（例如 `jdbc/myDataSource`）。
- 將其與應用程序使用的 JNDI 名稱（例如 `jdbc/myDataSource` 或綁定名稱如 `jdbc/actualDataSource`）進行比較。

如果 JNDI 名稱匹配，則應用程序正在使用 `server.xml` 中定義的數據源。

### 第 3 步：解釋結果
- **匹配找到**：如果應用程序使用的 JNDI 名稱對應於 `server.xml`（或包含的文件）中的 `<dataSource>` 元素，則 EAR Java 程序正在使用 `server.xml` 數據源。
- **無匹配**：如果在 `server.xml` 中沒有匹配的 JNDI 名稱，應用程序可能沒有使用伺服器定義的數據源。它可能會以編程方式創建自己的數據源（例如，使用 JDBC 驅動程序直接使用 URL、用戶名和密碼），但這在受管理的環境中如 WebSphere Liberty 中不常見且不推薦。

### 額外考量
- **包含的配置文件**：如果 `server.xml` 使用 `<include>` 元素（例如 `<include location="datasources.xml"/>`），檢查這些文件中的數據源定義。
- **預設行為**：如果沒有綁定文件覆蓋 JNDI 名稱，應用程序可能假設資源引用名稱（例如 `jdbc/myDataSource`）與 `server.xml` 中的數據源匹配。
- **伺服器日誌或工具**：雖然這不是配置檢查的一部分，您也可以檢查伺服器日誌或使用 WebSphere Liberty Admin Center 來查看哪些數據源與應用程序相關聯，但這更多的是運行時驗證。

### 結論
要確認 EAR Java 程序是否使用 WebSphere Liberty 中的 `server.xml` 數據源：
1. 識別應用程序使用的 JNDI 名稱（通過部署描述符、綁定文件或代碼）。
2. 驗證該 JNDI 名稱是否與 `server.xml` 或其包含的文件中定義的數據源匹配。

如果有匹配，應用程序依賴於 `server.xml` 數據源；否則，它可能使用其他方法。