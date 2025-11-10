---
audio: false
generated: true
lang: hant
layout: post
title: Maven Shade Plugin：建立 Uber-JAR 封裝
translated: true
type: note
---

`maven-shade-plugin` 是一個 Maven 插件，用於透過將項目的編譯程式碼與其依賴項組合來建立「uber-JAR」（單一、自包含的 JAR 檔案）。它常用於 Java 項目中，將應用程式及其所有必需的函式庫打包成一個可執行的 JAR 檔案，從而簡化分發和部署過程。

### 關鍵細節：
- **Group ID**：`org.apache.maven.plugins`（表明其為官方 Apache Maven 插件）。
- **Artifact ID**：`maven-shade-plugin`（插件具體名稱）。
- **用途**：
  - **Shading**：重新定位（重命名）依賴項的套件，以避免類別衝突（例如，當多個函式庫使用相同類別的不同版本時）。
  - **打包**：將依賴項捆綁到最終的 JAR 中，使其成為獨立檔案。
  - **資源轉換**：可以修改資源（例如，合併配置檔案如 `MANIFEST.MF`）。
- **常見使用場景**：
  - 為命令列應用程式建立可執行的 JAR。
  - 解決具有多個依賴項的項目中的類別路徑衝突。
  - 簡化如 Spark 或 Hadoop 作業等應用程式的部署。
- **運作原理**：
  - 在 `pom.xml` 檔案中的 `<plugins>` 部分進行配置。
  - 在建置過程中（通常在 `package` 階段），它會合併類別和資源，可選地重新定位套件，並產生最終的 JAR。
- **在 `pom.xml` 中的配置範例**：
  ```xml
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      <version>3.5.0</version> <!-- 使用最新版本 -->
      <executions>
          <execution>
              <phase>package</phase>
              <goals>
                  <goal>shade</goal>
              </goals>
              <configuration>
                  <transformers>
                      <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                          <mainClass>com.example.Main</mainClass>
                      </transformer>
                  </transformers>
              </configuration>
          </execution>
      </executions>
  </plugin>
  ```
  此範例指定了可執行 JAR 的主要類別，並在 `package` 階段執行插件。

- **主要功能**：
  - **依賴項包含**：將依賴項嵌入到 JAR 中。
  - **套件重新定位**：重命名套件以避免衝突（例如，將 `com.google.common` 重新定位為 `shaded.com.google.common`）。
  - **資源過濾**：合併或轉換資源檔案。
  - **可執行 JAR**：添加清單條目，使 JAR 可透過 `java -jar` 執行。

### 使用時機：
- 當您需要單一 JAR 以方便分發時。
- 當處理依賴項衝突時（例如，同一函式庫的不同版本）。
- 當部署應用程式到外部依賴項難以管理的環境時。

如果您對其配置或使用場景有具體問題，請告訴我！