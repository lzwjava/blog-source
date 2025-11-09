---
audio: false
date: 2025-09-07
generated: true
image: false
lang: hant
layout: post
title: 解決Java構建版本衝突
translated: true
type: note
---

您正在使用 **Java 8**（類別檔案版本 52.0）進行建置，但 POM 中的某些建置外掛/函式庫是為較新的 Java 版本編譯的。首先出問題的是 **Spotless**（類別檔案版本 55.0 = Java 11）。即使移除了 Spotless，您還有一些其他 Java 11+ 的項目會造成問題（Checkstyle 10.x、Logback 1.5，以及 Jakarta Servlet 5 與 Spring 5 的 javax 命名空間衝突）。

以下是兩個乾淨的解決方法。選擇其中一種即可。

---

## 選項 A — 維持使用 Java 8（適用於 Spring 5.2.x 和 Jetty 9.4）

* 移除/降級 Java 11+ 的外掛和函式庫。
* 使用 **javax.servlet-api 4.0.1**（Spring 5 使用 `javax.*`，而非 `jakarta.*`）。
* 保持使用 Jetty 9.4（Servlet 3.1/4 時代）。

貼上此 POM（僅以下部分與您的不同）：

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.x 沒問題 -->
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-web</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-webmvc</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-core</artifactId>
      <version>5.2.2.RELEASE</version>
    </dependency>

    <!-- 測試依賴不變 -->
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-api</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter-engine</artifactId>
      <version>5.13.1</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>5.18.0</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-test</artifactId>
      <version>5.2.2.RELEASE</version>
      <scope>test</scope>
    </dependency>

    <!-- AOP 沒問題 -->
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjrt</artifactId>
      <version>1.9.24</version>
    </dependency>
    <dependency>
      <groupId>org.aspectj</groupId>
      <artifactId>aspectjweaver</artifactId>
      <version>1.9.24</version>
    </dependency>

    <!-- SLF4J 2.0 是 Java 8+，沒問題 -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ 將 Logback 降級至與 Java 8 相容的版本 -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ 為 Spring 5.x + Jetty 9.4 使用 javax servlet -->
    <dependency>
      <groupId>javax.servlet</groupId>
      <artifactId>javax.servlet-api</artifactId>
      <version>4.0.1</version>
      <scope>provided</scope>
    </dependency>

    <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-lang3</artifactId>
      <version>3.17.0</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- 如果需要 JavadocRemover，請保留您的 exec-maven-plugin -->
      <plugin>
        <groupId>org.codehaus.mojo</groupId>
        <artifactId>exec-maven-plugin</artifactId>
        <version>3.5.1</version>
        <executions>
          <execution>
            <id>remove-javadoc</id>
            <phase>compile</phase>
            <goals><goal>java</goal></goals>
            <configuration>
              <mainClass>org.lzw.JavadocRemover</mainClass>
              <arguments><argument>src/main</argument></arguments>
            </configuration>
          </execution>
        </executions>
      </plugin>

      <!-- ↓ 移除 Spotless 或將其限制在 Java 11+ 的 profile 中。
           如果您真的想在 Java 8 上使用它，請使用舊版 Spotless + JDK8，
           但最簡單的方法是現在就移除它。 -->
      <!-- (Spotless 外掛區塊已移除) -->

      <!-- ↓ Checkstyle：選擇與 Java 8 相容的引擎 -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-checkstyle-plugin</artifactId>
        <version>3.1.2</version>
        <dependencies>
          <dependency>
            <groupId>com.puppycrawl.tools</groupId>
            <artifactId>checkstyle</artifactId>
            <version>9.3</version>
          </dependency>
        </dependencies>
        <configuration>
          <configLocation>${project.basedir}/checks.xml</configLocation>
          <failOnViolation>true</failOnViolation>
        </configuration>
        <executions>
          <execution>
            <id>checkstyle-check</id>
            <phase>compile</phase>
            <goals><goal>check</goal></goals>
          </execution>
        </executions>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-war-plugin</artifactId>
        <version>3.4.0</version>
        <configuration>
          <failOnMissingWebXml>true</failOnMissingWebXml>
        </configuration>
      </plugin>

      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.5.3</version>
      </plugin>

      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
          </execution>
          <execution>
            <id>report</id>
            <phase>verify</phase>
            <goals><goal>report</goal></goals>
          </execution>
        </executions>
      </plugin>

      <!-- Jetty 9.4 在 Java 8 + javax.servlet 上沒問題 -->
      <plugin>
        <groupId>org.eclipse.jetty</groupId>
        <artifactId>jetty-maven-plugin</artifactId>
        <version>9.4.54.v20240208</version>
        <configuration>
          <httpConnector><port>8080</port></httpConnector>
          <webApp><contextPath>/</contextPath></webApp>
        </configuration>
      </plugin>
    </plugins>
  </build>

  <!-- 保留您的 'python-integration-tests' profile，
       但請注意 spring-boot-maven-plugin 3.5.0 需要 Java 17+。
       在 Java 8 上建置時，請關閉此 profile。 -->
  <profiles>
    <profile>
      <id>python-integration-tests</id>
      <build>
        <plugins>
          <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version>
            <executions>
              <execution>
                <id>prepare-agent-integration</id>
                <goals><goal>prepare-agent-integration</goal></goals>
                <configuration>
                  <destFile>${project.build.directory}/jacoco-it.exec</destFile>
                  <propertyName>jacoco.agent.it</propertyName>
                </configuration>
              </execution>
            </executions>
          </plugin>

          <!-- 將此 Boot 外掛保留在此處，但請勿在 Java 8 上啟用此 profile -->
          <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <version>3.5.0</version>
          </plugin>

          <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>3.5.1</version>
            <executions>
              <execution>
                <id>python-integration-tests</id>
                <phase>integration-test</phase>
                <goals><goal>exec</goal></goals>
                <configuration>
                  <executable>python</executable>
                  <workingDirectory>${project.basedir}</workingDirectory>
                  <arguments>
                    <argument>-m</argument><argument>unittest</argument>
                    <argument>discover</argument><argument>tests/</argument>
                    <argument>-v</argument>
                  </arguments>
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

然後執行：

```bash
mvn -v                # 確認使用 JDK 1.8.x
mvn clean package
# 或用於開發
mvn jetty:run
```

---

## 選項 B — 升級您的建置 JDK（Java 17 是個理想選擇）

* 將您的**建置**環境切換到 JDK 17+（並且 `mvn -v` 應顯示 Java 17）。
* 保持 Spotless 和 Checkstyle 10.x 不變。
* 您**僅在**同時將執行環境遷移到 Jetty 11+ 或 Tomcat 10+ 並將您的程式碼遷移到 `jakarta.*` 命名空間（Spring 6 / Spring Boot 3 的世界）時，才能保留 `jakarta.servlet-api`。如果您停留在 Spring 5.2.x，請改用 `javax.servlet-api:4.0.1` 和一個 Servlet 4 容器。

典型指令：

```bash
# 在 Ubuntu 上，安裝 JDK 17 並選擇它：
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # 應顯示 Java 版本 17
mvn clean package
```

如果您必須在 Java 17 上建置的同時仍生成 Java 8 位元組碼，請設定：

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

（但請注意：像 Logback 1.5 這樣的依賴項無論如何都是 Java 11+，所以如果您包含它們，您的**執行環境**必須是 11+。）

---

## 失敗原因（簡短說明）

* `UnsupportedClassVersionError ... class file version 55.0` = 外掛/函式庫是使用 **Java 11** 編譯的，但 Maven 是在 **Java 8** 下執行的。
* 您在 Java 8 上具體的問題項目：

  * Spotless 外掛 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0` 與 Spring 5 的 `javax.*` 和 Jetty 9.4 不匹配。

---

如果您告訴我您傾向於哪種路徑（堅持使用 Java 8 還是遷移到 Java 17+），我將為該設定精確調整 POM，並在需要時為您的 `web.xml`/Spring 配置以及 Jetty/Tomcat 選擇提供最小的差異說明。