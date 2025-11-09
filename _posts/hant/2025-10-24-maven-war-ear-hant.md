---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Maven WAR 與 EAR 模組設定
translated: true
type: note
---

### 適用於 WAR 至 EAR 的 Maven 多模組專案設定

在 Maven 中，若要讓一個模組生成 WAR（例如網頁應用程式），而另一個模組將其組裝成 EAR（企業歸檔檔），需使用多模組專案結構。EAR 模組透過 `maven-ear-plugin` 依賴 WAR 模組，這確保了在建置過程中 WAR 會被包含在 EAR 內。

#### 步驟 1：建立父 POM
父 POM 定義模組並管理共享配置。將其打包類型設定為 `pom`。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>parent</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <modules>
        <module>web-module</module>  <!-- 先建置此模組 -->
        <module>ear-module</module>
    </modules>

    <!-- 可選：共享依賴項和插件版本 -->
    <dependencyManagement>
        <dependencies>
            <!-- 在此定義子模組的版本 -->
        </dependencies>
    </dependencyManagement>

    <build>
        <pluginManagement>
            <plugins>
                <!-- 管理插件版本 -->
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-ear-plugin</artifactId>
                    <version>3.3.0</version>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

#### 步驟 2：設定 WAR 模組
此模組將網頁應用程式建置為 WAR。將其打包類型設定為 `war`。此處無需特別的 EAR 配置——只需確保其先被建置。

目錄結構：`web-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>web-module</artifactId>
    <packaging>war</packaging>

    <dependencies>
        <!-- 加入您的網頁依賴項，例如 servlet-api -->
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>4.0.1</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-war-plugin</artifactId>
                <version>3.3.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 步驟 3：設定 EAR 模組
此模組負責組裝 EAR。將其打包類型設定為 `ear`，並使用 `maven-ear-plugin` 來引用 WAR 模組。該插件將拉取 WAR 成品並將其打包進 EAR。

目錄結構：`ear-module/pom.xml`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.example</groupId>
        <artifactId>parent</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>ear-module</artifactId>
    <packaging>ear</packaging>

    <dependencies>
        <!-- 依賴 WAR 模組以將其包含在建置中 -->
        <dependency>
            <groupId>com.example</groupId>
            <artifactId>web-module</artifactId>
            <version>${project.version}</version>
            <type>war</type>
        </dependency>
        <!-- 可選：如有需要，加入 EJB 或其他模組 -->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-ear-plugin</artifactId>
                <version>3.3.0</version>
                <configuration>
                    <!-- EAR 版本（例如用於 Java EE） -->
                    <version>8</version>
                    
                    <!-- EAR 中的函式庫目錄 -->
                    <defaultLibBundleDir>lib</defaultLibBundleDir>
                    
                    <!-- 精簡 WAR（排除已存在於 EAR libs 中的依賴項） -->
                    <skinnyWars>true</skinnyWars>
                    
                    <!-- 定義要包含的模組 -->
                    <modules>
                        <webModule>
                            <groupId>com.example</groupId>
                            <artifactId>web-module</artifactId>
                            <bundleDir>/</bundleDir>  <!-- EAR 的根目錄 -->
                            <contextRoot>/mywebapp</contextRoot>  <!-- 部署上下文 -->
                        </webModule>
                        <!-- 如有需要，加入更多 <ejbModule> 或 <jarModule> -->
                    </modules>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 步驟 4：建置專案
- 從**父目錄**執行：`mvn clean install`
  - 這會按順序建置模組（先 WAR，後 EAR）。
- EAR 將位於 `ear-module/target/ear-module-1.0-SNAPSHOT.ear`。
- 若僅建置 EAR（假設 WAR 已建置）：`cd ear-module && mvn clean package`。

#### 關鍵注意事項
- **建置順序**：在父 POM 的 `<modules>` 中，將 WAR 模組列在 EAR 之前，以確保 Maven 先建置 WAR。
- **依賴關係**：EAR 模組對 WAR 的 `<dependency>` 確保其在打包過程中被解析。
- **自訂設定**：調整 `<contextRoot>` 以設定網頁應用程式的 URL 路徑。在 `<modules>` 中加入更多模組（例如 EJB JARs）。
- **疑難排解**：若 WAR 未被包含，請檢查成品座標是否完全匹配。在 EAR 模組中使用 `mvn dependency:tree` 來驗證。

更多詳細資訊，請參閱官方 Maven EAR 插件文件。

[Apache Maven EAR Plugin](https://maven.apache.org/plugins/maven-ear-plugin/)  
[Maven Multi-Module Projects](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#Multi-module_Projects)