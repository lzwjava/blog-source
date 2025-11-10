---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 戰爭與耳朵封裝指南
translated: true
type: note
---

這是一個實用、無表格的 Maven **WAR** 與 **EAR** 打包方式對比，以及如何在實際專案中使用它們。

# 每種打包方式的用途

* **WAR (`packaging: war`)** – 單一 Web 應用程式：servlets/Jakarta REST、JSP/JSF、Spring MVC/Boot（作為 WAR）等。部署至 servlet 容器（Tomcat/Jetty）或完整應用伺服器的 Web 層。
* **EAR (`packaging: ear`)** – 多個模組的套件，共同部署到完整的 Java EE/Jakarta EE 應用伺服器（WildFly/JBoss EAP、WebLogic、WebSphere）。通常包含一個或多個 WAR、EJB JAR 以及共享函式庫，形成一個部署單元。

# 典型的選擇時機

* 選擇 **WAR** 如果你有單一 Web 應用程式或 Spring Boot 應用程式，且不需要 EJB 或多模組伺服器功能。
* 選擇 **EAR** 如果你必須將多個模組一起部署（例如 EJB + 多個 WAR + 共享函式庫）、需要跨模組使用應用伺服器服務（XA、集中式安全領域、JMS、分散式事務），或是你的組織規定使用 EAR。

# 成品內包含的內容

* **WAR** 內容：`/WEB-INF/classes`、`/WEB-INF/lib`、可選的 `web.xml`（或註解）、靜態資源。在大多數伺服器中，每個 WAR 有獨立的類別載入器。
* **EAR** 內容：`*.war`、`*.jar`（EJB/工具）、`META-INF/application.xml`（或註解/精簡配置），以及可選的 `lib/` 用於跨模組共享的函式庫。提供一個 EAR 層級的類別載入器，對所有模組可見。

# 依賴關係與類別載入注意事項

* **WAR**：將 servlet/Jakarta EE API 宣告為 `provided`；其他所有內容都放在 `/WEB-INF/lib` 下。隔離更簡單；版本衝突較少。
* **EAR**：將共享函式庫放在 EAR 的 `lib/` 中（透過 `maven-ear-plugin`），這樣所有模組共享同一版本。注意模組函式庫與伺服器提供 API 之間的衝突；對齊版本並在適當處使用 `provided`。

# 你會用到的 Maven 插件

* **WAR 專案**：`maven-war-plugin`
* **EAR 聚合器**：`maven-ear-plugin`
* **EJB 模組（如有）**：`maven-ejb-plugin`
* 父專案/聚合器通常使用 `packaging: pom` 來連結模組。

# 最小範例

單一 Web 應用程式 (WAR)：

```xml
<!-- pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-web</artifactId><version>1.0.0</version>
  <packaging>war</packaging>

  <dependencies>
    <!-- 對伺服器 API 使用 provided -->
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <!-- 你的應用程式依賴 -->
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <!-- 可選：配置 webResources、warName、filtering -->
      </plugin>
    </plugins>
  </build>
</project>
```

包含 WAR 和 EJB 的多模組 EAR：

```xml
<!-- parent/pom.xml -->
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.example</groupId><artifactId>my-app</artifactId><version>1.0.0</version>
  <packaging>pom</packaging>
  <modules>
    <module>ejb-module</module>
    <module>web-module</module>
    <module>ear-assembly</module>
  </modules>
</project>
```

```xml
<!-- ejb-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ejb-module</artifactId>
  <packaging>ejb</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- web-module/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>web-module</artifactId>
  <packaging>war</packaging>
  <dependencies>
    <dependency>
      <groupId>jakarta.platform</groupId><artifactId>jakarta.jakartaee-web-api</artifactId>
      <version>10.0.0</version><scope>provided</scope>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type> <!-- 允許 @EJB 注入 -->
    </dependency>
  </dependencies>
</project>
```

```xml
<!-- ear-assembly/pom.xml -->
<project>
  <parent>…</parent>
  <artifactId>ear-assembly</artifactId>
  <packaging>ear</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId><artifactId>web-module</artifactId><version>1.0.0</version>
      <type>war</type>
    </dependency>
    <dependency>
      <groupId>com.example</groupId><artifactId>ejb-module</artifactId><version>1.0.0</version>
      <type>ejb</type>
    </dependency>
    <!-- 要放入 EAR/lib 供所有模組共享的函式庫 -->
    <dependency>
      <groupId>com.fasterxml.jackson.core</groupId><artifactId>jackson-databind</artifactId>
      <version>2.17.2</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-ear-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <defaultLibBundleDir>lib</defaultLibBundleDir>
          <modules>
            <webModule>
              <groupId>com.example</groupId>
              <artifactId>web-module</artifactId>
              <contextRoot>/myapp</contextRoot>
            </webModule>
            <ejbModule>
              <groupId>com.example</groupId>
              <artifactId>ejb-module</artifactId>
            </ejbModule>
          </modules>
          <!-- 可選：生成 application.xml，或提供自定義的 -->
          <generateApplicationXml>true</generateApplicationXml>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

建置結果：

* `mvn -pl web-module -am clean package` → `web-module-1.0.0.war`
* `mvn -pl ear-assembly -am clean package` → `ear-assembly-1.0.0.ear` 包含 WAR、EJB 和 `lib/`。

# 重要的運作差異

* **部署目標**

  * WAR：servlet 容器或應用伺服器 Web 層。
  * EAR：完整應用伺服器；以原子操作部署所有模組。
* **事務與訊息傳遞**

  * 單獨的 WAR 使用容器公開的功能；複雜的 XA/JMS 設定通常存在於 EAR 內的 EJB 中。
* **版本控制與推出**

  * WAR：重建和重新部署單一應用程式很簡單。
  * EAR：協調多個模組的版本；一個部署單元以確保一致性。
* **啟動時間與本地開發**

  * WAR：快速回饋，執行環境更輕量。
  * EAR：較重；IDE/伺服器整合有幫助，但開發週期較慢。
* **現代 Spring Boot 注意事項**

  * Boot 偏好可執行的 **JAR**；如果部署到外部容器，則支援 WAR。
  * Boot **不** 以 EAR 為目標；如果必須使用應用伺服器，請將 Boot 作為 WAR 部署，並避免使用 EAR，除非你的平台要求。

# 常見陷阱與提示

* 對伺服器 API 使用 `provided` 以避免打包它們。
* 對於 EAR，將共享函式庫放在 `defaultLibBundleDir` 中，以防止在每個 WAR/EJB 內出現重複副本。
* 跨模組對齊 Jakarta EE 版本；版本不匹配會導致類別載入錯誤。
* 在 WebLogic/WebSphere 上，注意類別載入器策略（parent-first 與 parent-last）；有時你需要供應商特定的描述符。
* 如果不需要 EJB/XA，普通的 WAR（或 Boot JAR）更簡單且通常更具可移植性。

如果你告訴我你的應用伺服器（Tomcat vs WildFly/WebLogic/etc.）以及你是否有 EJB 或多個 Web 應用程式，我可以勾勒出你需要的確切 POM 和部署描述符。