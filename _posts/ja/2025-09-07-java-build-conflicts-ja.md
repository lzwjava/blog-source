---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: Javaビルドバージョン競合の解決
translated: true
type: note
---

あなたは**Java 8**（クラスファイル52.0）でビルドしていますが、POM内のいくつかのビルドプラグインやライブラリは新しいJava向けにコンパイルされています。最初に問題を引き起こすのは**Spotless**（クラスファイル55.0 = Java 11）です。Spotlessを削除しても、他にもJava 11以降が必要なアイテムがあり、問題が発生します（Checkstyle 10.x、Logback 1.5、Spring 5のjavax名前空間とJakarta Servlet 5の不一致）。

以下に、問題を解決する2つのクリーンな方法を示します。いずれかを選択すれば問題は解決します。

---

## オプションA — Java 8に留まる（Spring 5.2.xおよびJetty 9.4で動作）

* Java 11以降が必要なプラグインとライブラリを削除/ロールバックします。
* **javax.servlet-api 4.0.1**を使用します（Spring 5は`javax.*`を使用し、`jakarta.*`は使用しません）。
* Jetty 9.4（Servlet 3.1/4時代）を維持します。

以下のPOMを貼り付けてください（以下の部分のみがあなたのものと異なります）：

```xml
<project>
  ...
  <properties>
    <maven.compiler.source>8</maven.compiler.source>
    <maven.compiler.target>8</maven.compiler.target>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>

  <dependencies>
    <!-- Spring 5.xは問題ありません -->
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

    <!-- テスト依存関係は変更なし -->
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

    <!-- AOPはOK -->
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

    <!-- SLF4J 2.0はJava 8以降でOK -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-api</artifactId>
      <version>2.0.17</version>
    </dependency>

    <!-- ↓ LogbackをJava 8互換のラインにダウングレード -->
    <dependency>
      <groupId>ch.qos.logback</groupId>
      <artifactId>logback-classic</artifactId>
      <version>1.2.13</version>
    </dependency>

    <!-- ↓ Spring 5.x + Jetty 9.4用にjavax servletを使用 -->
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
      <!-- JavadocRemoverが必要な場合はexec-maven-pluginを維持 -->
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

      <!-- ↓ Spotlessを削除するか、Java 11+プロファイルの背後に制限します。
           Java 8で本当に必要なら、古いSpotless + JDK8を使用しますが、
           今は削除するのが最も簡単です。 -->
      <!-- (Spotlessプラグインブロックは削除されました) -->

      <!-- ↓ Checkstyle: Java 8互換エンジンを選択 -->
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

      <!-- Jetty 9.4はJava 8 + javax.servletで問題ありません -->
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

  <!-- 'python-integration-tests'プロファイルは維持しますが、
       spring-boot-maven-plugin 3.5.0はJava 17以降が必要です。
       Java 8でビルドするときはこのプロファイルをOFFにしてください。 -->
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

          <!-- このBootプラグインはここに残しますが、Java 8ではこのプロファイルを有効にしないでください -->
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

その後、実行します：

```bash
mvn -v                # JDK 1.8.xを使用していることを確認
mvn clean package
# または開発用
mvn jetty:run
```

---

## オプションB — ビルドJDKをアップグレード（Java 17がおすすめ）

* **ビルド**をJDK 17+に切り替えます（`mvn -v`がJava 17を表示するはずです）。
* SpotlessとCheckstyle 10.xを現状のまま維持します。
* `jakarta.servlet-api`を維持できるのは、ランタイムをJetty 11+またはTomcat 10+に移行し、コードを`jakarta.*`名前空間に移行した場合のみです（Spring 6 / Spring Boot 3の世界）。Spring 5.2.xに留まる場合は、`javax.servlet-api:4.0.1`とServlet 4コンテナを使用してください。

典型的なコマンド：

```bash
# Ubuntuの場合、JDK 17をインストールして選択します：
sudo apt install openjdk-17-jdk
sudo update-alternatives --config java
sudo update-alternatives --config javac

mvn -v             # Javaバージョン17を表示するはず
mvn clean package
```

Java 17でビルドしながらJava 8バイトコードを生成する必要がある場合は、以下を設定します：

```xml
<properties>
  <maven.compiler.release>8</maven.compiler.release>
</properties>
```

（ただし、Logback 1.5などの依存関係はJava 11+であるため、それらを含める場合、**ランタイム**は11+である必要があります。）

---

## 失敗した理由（短い説明）

* `UnsupportedClassVersionError ... class file version 55.0` = プラグイン/ライブラリが**Java 11**でコンパイルされているが、Mavenが**Java 8**で実行された。
* Java 8での具体的な問題点：

  * Spotless plugin 2.44.5 (Java 11+)
  * Checkstyle 10.25.0 (Java 11+)
  * Logback 1.5.x (Java 11+)
  * `jakarta.servlet-api:5.0.0`がSpring 5の`javax.*`およびJetty 9.4と不一致。

---

どちらの方法を希望するか（Java 8に留まる vs Java 17+に移行）を教えていただければ、そのセットアップに合わせてPOMを正確に調整し、必要に応じて`web.xml`/Spring設定およびJetty/Tomcat選択に対する最小限の差分をお伝えします。