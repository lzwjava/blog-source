---
audio: false
generated: true
image: false
lang: ja
layout: post
title: マルチモジュールSpringカバレッジ設定におけるJaCoCo
translated: true
type: note
---

素晴らしい—JaCoCoはマルチモジュールのSpringプロジェクトでうまく機能します。以下が必要になるでしょう：

1. モジュールごとの単体テストカバレッジ
2. 親プロジェクトでの集計レポート
3. **統合**カバレッジを取り込むためのオプションプロファイル（例：Liberty+EARの実行をPythonテストでカバー）

以下は、そのまま使用できる実戦で検証された設定です。

---

### 親 `pom.xml` (packaging `pom`)

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

  <!-- 全モジュールの単体テストの集計レポート -->
  <reporting>
    <plugins>
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <reportSets>
          <reportSet>
            <reports>
              <!-- 親で'mvn verify'を実行すると'report-aggregate'がトリガーされる -->
              <report>report-aggregate</report>
            </reports>
            <configuration>
              <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
              <reports>
                <xml>true</xml>
                <html>true</html>
                <csv>false</csv>
              </reports>
              <!-- オプションのグローバルフィルター -->
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

  <!-- 統合カバレッジを追加するプロファイル（例：Liberty + Pythonテスト） -->
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
              <!-- 外部の.execファイルも読み取る集計レポートを作成 -->
              <execution>
                <id>report-aggregate-it</id>
                <phase>verify</phase>
                <goals><goal>report-aggregate</goal></goals>
                <configuration>
                  <!-- Liberty JVMエージェントによってダンプされた1つ以上の.execファイルを指定 -->
                  <dataFiles>
                    <!-- 例のパス；CI/Libertyの場所に合わせて調整 -->
                    <dataFile>${project.basedir}/.jacoco/jacoco-it.exec</dataFile>
                    <!-- ノードごとにダンプしてすべてを含めたい場合は、さらにdataFileエントリを追加可能 -->
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

### 各子モジュール (`ChatCommon/pom.xml`, `ChatLib/pom.xml`, `ChatCore/pom.xml`, `ChatWeb/pom.xml`)

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
      <!-- このモジュールのUNITテスト用にエージェントをアタッチ -->
      <plugin>
        <groupId>org.jacoco</groupId>
        <artifactId>jacoco-maven-plugin</artifactId>
        <version>0.8.12</version>
        <executions>
          <execution>
            <id>prepare-agent</id>
            <goals><goal>prepare-agent</goal></goals>
            <configuration>
              <!-- argLineを名前付きプロパティに入れ、他の引数と混在可能にする -->
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
          <!-- オプション：最小値の強制 -->
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

      <!-- Surefireがエージェントを確実に取得するようにする -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <configuration>
          <argLine>${jacocoArgLine} ${surefireArgLine}</argLine>
        </configuration>
      </plugin>

      <!-- （オプション）モジュールレベルのIT用のFailsafe -->
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

> `ChatLib`、`ChatCore`、`ChatWeb`でも同様に行います。
> `ChatWeb`（Spring Boot WAR/JAR）の場合、設定は同じです。

---

### 実行方法

**モジュール全体の単体テストカバレッジ（親での集計XML）：**

```bash
mvn -q clean verify
# XML:  target/site/jacoco-aggregate/jacoco.xml
# HTML: target/site/jacoco-aggregate/index.html
```

**Liberty + Pythonテストからの統合カバレッジ：**

1. JaCoCoエージェントを使用してLibertyを起動（前述のように）、Pythonテストを実行、停止またはダンプ。
   `.exec`が`${project.basedir}/.jacoco/jacoco-it.exec`に配置されるようにする（または親プロファイルのパスを更新）。
2. ITデータを含む集計をビルド：

```bash
mvn -q -Pit-coverage verify
# XML:  target/site/jacoco-aggregate-it/jacoco.xml
# HTML: target/site/jacoco-aggregate-it/index.html
```

---

### 時間を節約する注意点

* **集計は親（packaging `pom`）でモジュールが宣言されている場合にのみ機能**します。親ディレクトリから`mvn`を実行してください。
* **XML**（`jacoco.xml`）は`<reports>`で有効にすると生成されます。これはCodecov/Sonarが使用するものです。
* 複数の`.exec`ファイル（例：複数のLibertyノード）を収集する場合は、以下のいずれかを行います：

  * `it-coverage`プロファイルの`<dataFiles>…</dataFiles>`の下にすべてリストアップする、または
  * 最初にマージ（`jacococli.jar merge …`を使用）してから、マージされたファイルを指定します。
* クラスファイルをEARに向けないでください。JaCoCoのレポートには**モジュールのコンパイル済みクラス**（`*/target/classes`）とソースが必要です—`report-aggregate`によって自動的に処理されます。
* Surefireも独自の`argLine`を設定する場合、エージェントが失われないように`${jacocoArgLine}`を最初に保ってください。

正確なモジュールパッケージルートとLibertyの`.exec`の配置場所を共有していただければ、`<dataFiles>`と除外設定を調整して、集計XMLがクリーンでCI対応になるようにできます。