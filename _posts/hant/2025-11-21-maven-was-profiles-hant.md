---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4.1-fast
title: WAS 環境配置的 Maven 設定檔
translated: true
type: note
---

針對 IBM WebSphere Application Server（傳統 WAS，非 Liberty），標準封裝格式為 **EAR** 檔案（即使是簡單的 Web 應用程式，WAS 也偏好 EAR 而非獨立的 WAR）。處理不同環境（例如本地開發環境使用固定/硬編碼的測試登入用戶，而伺服器/生產環境使用 SSO 或適當的安全域）的最佳實踐是在單一 `pom.xml` 中使用 **Maven 建置設定檔**。這樣可以避免維護多個獨立的 POM 檔案（例如 `pom.xml` 和 `build_pom.xml`），這不僅容易出錯，也不符合 Maven 的慣例。

### 為何使用設定檔而非多個 POM？
- 單一來源（單一 POM）。
- 輕鬆啟用：`mvn package -Plocal` 或 `mvn package -Pserver`。
- 設定檔可以過濾資源、覆寫檔案、更改外掛配置或調整綁定（例如，用於 WAS 特定身份驗證的 `ibm-web-bnd.xml`、`ibm-application-ext.xml`）。
- 常用於開發/測試/生產環境的差異，包括身份驗證設定。

### 推薦結構
使用 Maven Resources Plugin 配合過濾功能 + 設定檔特定的資源目錄來交換配置檔案（例如 `web.xml`、`properties` 檔案、Spring security 配置或 WAS 綁定）。

目錄結構範例：
```
src/
├── main/
│   ├── resources/          (通用配置)
│   ├── webapp/
│   │   ├── WEB-INF/
│   │   │   ├── web.xml      (通用或基礎版本)
│   │   │   └── ibm-web-bnd.xml (選用，用於 JNDI/身份驗證綁定)
│   └── ...
├── local/                   (設定檔特定資源，僅在 local 設定檔下複製/過濾)
│   └── webapp/
│       └── WEB-INF/
│           ├── web.xml      (本地版本，使用表單登入 + 硬編碼用戶/角色或無安全性)
│           └── ...
└── server/                  (設定檔特定，用於生產/SSO)
    └── webapp/
        └── WEB-INF/
            ├── web.xml      (伺服器版本，使用 <login-config><auth-method>CLIENT-CERT</auth-method> 或用於 SSO 的 SPNEGO)
            └── ...
```

### pom.xml 範例片段
```xml
<project ...>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-was-app</artifactId>
    <version>1.0.0</version>
    <packaging>ear</packaging>   <!-- 或者如果您部署為 WAR，但 WAS 偏好 EAR -->

    <properties>
        <maven.compiler.source>11</maven.compiler.source> <!-- 或您的 Java 版本 -->
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <!-- 您的應用程式依賴 -->
        <!-- 用於 WAS 編譯時期 API（provided 範圍） -->
        <dependency>
            <groupId>com.ibm.tools.target</groupId>
            <artifactId>was</artifactId>
            <version>9.0</version> <!-- 符合您的 WAS 版本，例如 8.5.5 或 9.0 -->
            <type>pom</type>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- 建置 EAR（如果需要，調整為 WAR） -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- 您的 EAR 配置、模組等 -->
                </configuration>
            </plugin>

            <!-- 資源過濾與設定檔特定覆寫 -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-resources-plugin</artifactId>
                <version>3.3.1</version>
                <configuration>
                    <useDefaultDelimiters>true</useDefaultDelimiters>
                </configuration>
            </plugin>
        </plugins>
    </build>

    <!-- 設定檔 -->
    <profiles>
        <!-- 本地/開發設定檔：固定用戶、表單登入或無安全性 -->
        <profile>
            <id>local</id>
            <activation>
                <activeByDefault>true</activeByDefault> <!-- 本地建置的預設值 -->
            </activation>
            <build>
                <resources>
                    <!-- 通用資源 -->
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <!-- 使用本地特定檔案覆寫 -->
                    <resource>
                        <directory>src/local/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- 用於本地硬編碼用戶的範例過濾屬性 -->
                <app.login.user>devuser</app.login.user>
                <app.login.password>devpass</app.login.password>
            </properties>
        </profile>

        <!-- 伺服器/生產設定檔：真實 SSO（例如 SPNEGO、LTPA 或 OpenIDConnect） -->
        <profile>
            <id>server</id>
            <build>
                <resources>
                    <resource>
                        <directory>src/main/resources</directory>
                        <filtering>true</filtering>
                    </resource>
                    <resource>
                        <directory>src/server/webapp</directory>
                        <targetPath>${project.build.directory}/${project.artifactId}/WEB-INF</targetPath>
                    </resource>
                </resources>
            </build>
            <properties>
                <!-- 生產屬性，例如啟用 SSO 標誌 -->
                <app.auth.method>SSO</app.auth.method>
            </properties>
        </profile>
    </profiles>
</project>
```

### 身份驗證差異的關鍵點
- **本地**：在 `web.xml` 或 properties 檔案中使用 FORM 登入搭配簡單的用戶/角色，或完全停用安全性（移除 `<security-constraint>`）。
- **伺服器**：在 `web.xml` 中配置 WAS 特定的 SSO（例如，搭配 SPNEGO 使用 `<auth-method>FORM</auth-method>`，或在 Liberty 風格中使用 OpenID Connect 功能，但傳統 WAS 通常使用 LTPA + 全域安全域）。WAS 綁定（`ibm-web-bnd.xml`）也可以按設定檔覆寫以進行用戶/角色映射。
- 如果使用 Spring Security 或類似框架，以相同方式交換 `applicationContext-security.xml` 或 properties。
- 對於硬編碼的本地用戶：避免真實的硬編碼憑證；使用在本地 `users.properties` 中映射的測試用戶，或透過標誌停用身份驗證檢查。

### 建置指令
- 本地（預設）：`mvn clean package`
- 伺服器/生產：`mvn clean package -Pserver`

這會從**相同的程式碼庫**產生針對每個環境量身定制的不同 EAR。如果您確實需要單獨的成品名稱（例如 `myapp-local.ear` 與 `myapp.ear`），請在設定檔特定的 `<build>` 區段中添加 `<finalName>${project.artifactId}-${profile}</finalName>`。

[Maven Profiles Guide](https://maven.apache.org/guides/introduction/introduction-to-profiles.html)  
[Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[IBM WAS Maven Integration](https://www.ibm.com/docs/en/wasdtfe/9.7.0?topic=suye-configuring-dependency-pom-files-that-emulate-classpath-specific-websphere-runtime-environments)