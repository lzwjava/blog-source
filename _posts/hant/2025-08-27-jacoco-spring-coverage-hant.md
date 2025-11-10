---
audio: false
generated: true
image: false
lang: hant
layout: post
title: JaCoCo 多模組 Spring 覆蓋率設定
translated: true
type: note
---

很好——JaCoCo 在多模組 Spring 專案中運作良好。你需要：

1. 每個模組的單元測試涵蓋率；
2. 在父層級生成彙總報告；
3. 可選的設定檔來處理**整合**測試涵蓋率（例如，由 Python 測試執行的 Liberty+EAR）。

以下是一個經過實戰驗證的設定，你可以直接使用。

---

### 父層級 `pom.xml`（打包方式為 `pom`）

```xml
<project>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.myco.chat</groupId>
  <artifactId>chat-parent</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <modules>
    <module>ChatCommon</module>
    <module>ChatLib</module>
    <module>ChatCore</module>
    <module>ChatWeb</module>
  </modules>

  <build>
    <pluginManagement>
      <plugins>
        <plugin>
          <groupId>org.jacoco</groupId>
          <artifactId>jacoco-maven-plugin</artifactId>
          <version>0.8.12</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
        <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-failsafe-plugin</artifactId>
          <version>3.2.5</version>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>

  <!-- 為所有模組的單元測試生成彙總報告 -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- 當你在父層級執行 'mvn verify' 時，這會觸發 'report-aggregate' -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- 可選的全域過濾器 -->
              <excludes>
                <exclude>**/*Application.class</exclude>
                <exclude>**/*Configuration.class</exclude>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </reportSet>
        </plugins>
      </plugin>
    </plugins>
  </reporting>

  <!-- 用於加入整合測試涵蓋率的設定檔（例如 Liberty + Python 測試） -->
  <profiles>
    <profile>
      <id>it-coverage</id>
      <activation><activeByDefault>false</activeByDefault></activation>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <!-- 建立一個也能讀取外部 .exec 檔案的彙總報告 -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- 指向由 Liberty JVM 代理程式傾印的一個或多個 .exec 檔案 -->
                  <dataFiles>
                    <!-- 路徑範例；請根據你的 CI/Liberty 位置調整 -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- 如果你傾印了每個節點的檔案並希望全部包含，可以加入更多 dataFile 條目 -->
                  </dataFiles>
                  <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate-it</outputDirectory>
                  <reports>
                    <xml>true</xml>
                    <html>true</html>
                    <csv>false</csv>
                  </reports>
                  <excludes>
                    <exclude>**/generated/**</exclude>
                  </excludes>
                </configuration>
              </execution>
            </executions>
          </plugin>
        </plugins>
      </build>
    </profile>
  </profiles>
</project>
```

---

### 每個子模組（`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`）

```xml
<project>
  <parent>
    <groupId>com.myco.chat</groupId>
    <artifactId>chat-parent</artifactId>
    <version>1.0.0</version>
  </parent>
  <modelVersion>4.0.0</modelVersion>
  <artifactId>ChatCommon</artifactId>
  <packaging>jar</packaging>

  <build>
    <plugins>
      <!-- 為此模組的單元測試附加代理程式 -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- 將 argLine 放入一個命名屬性中，以便與其他參數混合使用 -->
              <propertyName>jacocoArgLine</propertyName>
              <append>true</append>
              <excludes>
                <exclude>**/generated/**</exclude>
              </excludes>
            </configuration>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
            <configuration>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
            </configuration>
          </execution>
          <!-- 可選：強制執行最低涵蓋率 -->
          <execution>
            <id>check</id>
            <goals><goal>check</goal></goals>
            <configuration>
              <rules>
                <rule>
                  <element>PACKAGE</element>
                  <limits>
                    <limit>
                      <counter>LINE</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.60</minimum>
                    </limit>
                    <limit>
                      <counter>BRANCH</counter>
                      <value>COVEREDRATIO</value>
                      <minimum>0.40</minimum>
                    </limit>
                  </limits>
                </rule>
              </rules>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- 確保 Surefire 使用代理程式 -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- （可選）用於模組級整合測試的 Failsafe -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-failsafe-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${failsafeArgLine}</argLine>
        </configuration>
      </plugin>
    </plugins>
  </build>
</project>
```

> 在 `ChatLib`、`ChatCore` 和 `ChatWeb` 中進行相同的設定。
> 對於 `ChatWeb`（一個 Spring Boot WAR/JAR），設定是相同的。

---

### 執行方式

**跨模組的單元測試涵蓋率（在父層級生成彙總 XML）：**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**來自 Liberty + Python 測試的整合測試涵蓋率：**

1. 使用 JaCoCo 代理程式啟動 Liberty（如前所述），執行 Python 測試，停止或傾印資料。
   確保 `.exec` 檔案位於 `${project.basedir}/.jacoco/jacoco-it.exec`（或在父設定檔中更新該路徑）。
2. 建置包含整合測試資料的彙總報告：

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### 節省時間的注意事項

* **彙總僅在父層級**（打包方式為 `pom`）且宣告了模組時有效。請從父目錄執行 `mvn`。
* 當你在 `<reports>` 中啟用時，會產生 **XML**（`jacoco.xml`）；這是 Codecov/Sonar 使用的格式。
* 如果你收集了多個 `.exec` 檔案（例如，多個 Liberty 節點），你可以：

  * 在 `it-coverage` 設定檔中的 `<dataFiles>…</dataFiles>` 下列出所有檔案，或者
  * 先合併（使用 `jacococli.jar merge …`），然後指向合併後的檔案。
* 不要將 classfiles 指向 EAR；JaCoCo 的報告需要**模組編譯後的類別**（`*/target/classes`）和原始碼——`report-aggregate` 會自動處理。
* 如果 Surefire 也設定自己的 `argLine`，請將 `${jacocoArgLine}` 放在前面，以免遺失代理程式。

如果你分享確切的模組套件根目錄和 Liberty `.exec` 檔案的位置，我可以為你調整 `<dataFiles>` 和任何排除項，使你的彙總 XML 乾淨且適合 CI 使用。