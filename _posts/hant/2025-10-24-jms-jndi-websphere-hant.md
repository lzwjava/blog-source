---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: WebSphere 的 JMS 與 JNDI API
translated: true
type: note
---

### Java 中使用 JMS 所需的套件與 API

要使用您參考的 JMS 程式碼片段（用於在 IBM WebSphere Application Server 中查詢並連線至 JMS 連線工廠），您需要匯入相關的 Java 套件。這些是來自 Java EE/Jakarta EE 生態系統的標準 API：

- **JNDI（Java 命名與目錄介面）**：用於 `InitialContext` 查詢。
  - 套件：`javax.naming`（或在較新的 Jakarta EE 版本中使用 `jakarta.naming`）。
  - 關鍵類別：`InitialContext` – 這是 JNDI 操作的起點。它提供了一個上下文，用於透過 JNDI 名稱（例如 `"jms/MyConnectionFactory"`）查詢資源（如 JMS 工廠或佇列）。在像 WAS 這樣的容器中，它會自動連線到伺服器的命名服務。

- **JMS（Java 訊息服務）API**：用於建立連線、工作階段、發送者/接收者和訊息。
  - 套件：`javax.jms`（JMS 1.1/2.0）或 `jakarta.jms`（現代 EE 中的 Jakarta JMS 3.0+）。
  - 關鍵介面：`QueueConnectionFactory`、`QueueConnection`、`QueueSession`、`QueueSender`、`Queue`、`TextMessage` 等。

在您的 Java 類別頂部匯入範例：
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**什麼是 `InitialContext`？**  
它是 JNDI API 中的一個類別，作為命名服務的入口點。在您的程式碼中：  
```java
InitialContext ctx = new InitialContext();  // 建立一個預設上下文，綁定到應用伺服器的 JNDI 環境
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // 透過 JNDI 名稱查詢預先設定的工廠
```  
對於在 WAS *內部* 運行的應用程式，建構函式不需要任何屬性，因為容器會注入環境（例如透過 `java.naming.factory.initial`）。如果是在 WAS *外部* 運行的獨立客戶端，您需要傳遞一個包含提供者 URL 等屬性的 `Hashtable`。

### Maven 依賴項 (pom.xml)

如果您的 Java 應用程式 **部署並運行在 WAS 內部**（例如作為 Web 應用程式、EJB 或企業 Bean）：  
- **不需要額外的依賴項**。WAS 作為其 Java EE 運行時的一部分，提供了 JMS 和 JNDI API。只需在編譯時對應它們（它們在構建/部署期間位於類別路徑上）。  
- 在 `pom.xml` 中，您可以使用 `<scope>provided</scope>` 明確聲明它們，以避免將它們打包到您的 WAR/EAR 中（保持輕量）：  
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- 或對於較新版本使用 jakarta.jms -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0，與 WAS 8.5+ 相容 -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0，標準 -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

如果您的應用程式是 **獨立客戶端**（在 WAS 外部運行，例如連線到伺服器的精簡客戶端）：  
- 您將需要 **WebSphere Application Client** 函式庫以透過 IIOP 獲得完整的 JMS 支援。從 IBM 下載 "IBM WebSphere Application Server traditional" 客戶端套件，然後將其添加到您的類別路徑中。  
- 在 `pom.xml` 中，包含：  
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- 近似值；如果可用，請使用 IBM 的 Maven 儲存庫 -->
      <version>9.0.5</version>  <!-- 與您的 WAS 版本匹配 -->
  </dependency>
  ```  
  或者使用完整的精簡客戶端 JAR（例如 `com.ibm.ws.orb_8.5.5.jar`、`com.ibm.ws.jndi_*.jar`）。請查閱 IBM 文件以獲取確切的設定。

對於 Jakarta EE 遷移（2020 年後），請切換到 `jakarta.*` 套件，但 WAS 9.x 預設仍使用 `javax.*` – 如果需要，請透過功能包啟用 Jakarta。

[IBM WebSphere JMS API 文件](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[Java EE JNDI 教程](https://docs.oracle.com/javase/tutorial/jndi/)