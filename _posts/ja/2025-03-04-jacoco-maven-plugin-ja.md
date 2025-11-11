---
audio: false
generated: true
lang: ja
layout: post
title: JaCoCo Mavenプラグイン
translated: true
type: note
---

以下は、MavenベースのJavaプロジェクトでコードカバレッジを測定するための**JaCoCo Mavenプラグインの使用方法**に関するステップバイステップガイドです。JaCoCo（Java Code Coverage）は、Mavenと統合して、テスト（通常は単体テスト）によってコードのどの程度が実行されたかを追跡するツールです。プロジェクトにJaCoCo Mavenプラグインを追加して設定することで、ビルドプロセス中に詳細なカバレッジレポートを生成できます。

---

### **JaCoCo Mavenプラグインを使用する手順**

#### **1. JaCoCo Mavenプラグインを`pom.xml`に追加する**
JaCoCo Mavenプラグインを使用するには、プロジェクトの`pom.xml`ファイルの`<build><plugins>`セクションに含める必要があります。以下は、プラグインを設定する基本的な構成です：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- 利用可能な最新バージョンを使用してください -->
            <executions>
                <execution>
                    <goals>
                        <goal>prepare-agent</goal>
                    </goals>
                </execution>
                <execution>
                    <id>report</id>
                    <phase>verify</phase>
                    <goals>
                        <goal>report</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

- **`groupId`、`artifactId`、`version`**：これらはJaCoCo Mavenプラグインを識別します。`0.8.12`は[Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin)で利用可能な最新バージョンに置き換えてください。
- **`<executions>`**：このセクションは、Mavenビルドライフサイクル中にプラグインがいつ、どのように実行されるかを設定します：
  - **`<goal>prepare-agent</goal>`**：テスト実行中にカバレッジデータを収集するためにJaCoCoエージェントを準備します。デフォルトでは、早期のフェーズ（`initialize`など）にバインドされ、カスタマイズしない限り明示的なフェーズは必要ありません。
  - **`<goal>report</goal>`**：テスト実行後にカバレッジレポートを生成します。ここでは`verify`フェーズにバインドされており、`test`フェーズの後で発生するため、すべてのテストデータが利用可能になります。

#### **2. テストが設定されていることを確認する**
JaCoCoプラグインは、テスト実行（通常はMaven Surefire Pluginによって実行される単体テスト）を分析することで動作します。ほとんどのMavenプロジェクトでは、Surefireはデフォルトで含まれており、`src/test/java`にあるテストを実行します。テストが標準的でない場合を除き、追加の設定は必要ありません。以下を確認してください：
- 単体テストが記述されていること（例：JUnitまたはTestNGを使用）。
- Surefireプラグインが存在すること（ほとんどの場合、デフォルトのMaven親POMから継承されます）。

Surefireを明示的に設定する必要がある場合は、以下のようになります：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- 最新バージョンを使用してください -->
</plugin>
```

`prepare-agent`ゴールは、`argLine`プロパティを変更してJaCoCoエージェントを設定します。このプロパティは、Surefireがカバレッジ追跡を有効にしてテストを実行するために使用します。

#### **3. Mavenビルドを実行する**
カバレッジレポートを生成するには、プロジェクトディレクトリで次のコマンドを実行します：

```bash
mvn verify
```

- **`mvn verify`**：これは`verify`までのすべてのフェーズ（`compile`、`test`、`verify`を含む）を実行します。JaCoCoプラグインは以下を行います：
  1. テスト実行前にエージェントを準備します。
  2. `test`フェーズ中（Surefireがテストを実行するとき）にカバレッジデータを収集します。
  3. `verify`フェーズ中にレポートを生成します。

あるいは、`verify`に進まずにテストのみを実行したい場合は、以下を使用します：

```bash
mvn test
```

ただし、この構成では`report`ゴールが`verify`にバインドされているため、レポートを表示するには`mvn verify`を実行する必要があります。`mvn test`中にレポートを生成したい場合は、`report`実行の`<phase>`を`test`に変更できますが、`verify`が一般的な慣例です。

#### **4. カバレッジレポートを表示する**
`mvn verify`を実行した後、JaCoCoはデフォルトでHTMLレポートを生成します。以下で確認できます：

```
target/site/jacoco/index.html
```

- このファイルをウェブブラウザで開くと、パッケージ、クラス、メソッド、行の割合を含むコードカバレッジの詳細な内訳を表示できます。
- レポートには、同じディレクトリにXMLおよびCSV形式（`jacoco.xml`および`jacoco.csv`）も含まれており、CIシステムのようなツールとの統合に役立ちます。

---

### **オプションのカスタマイズ**
より高度なユースケースでは、プラグイン構成を調整できます：

- **クラスまたはパッケージを除外する**：
  カバレッジ分析から特定のコード（例：生成されたコード）を除外するには、`<configuration>`セクションを追加します：

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  これを`<executions>`の上の`<plugin>`タグ内に配置します。

- **カバレッジしきい値を強制する**：
  カバレッジがしきい値を下回った場合にビルドを失敗させるには、`check`ゴールを追加します：

  ```xml
  <execution>
      <id>check</id>
      <phase>verify</phase>
      <goals>
          <goal>check</goal>
      </goals>
      <configuration>
          <rules>
              <rule>
                  <element>BUNDLE</element>
                  <limits>
                      <limit>
                          <counter>LINE</counter>
                          <value>COVEREDRATIO</value>
                          <minimum>0.80</minimum> <!-- 80% line coverage -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **レポート出力ディレクトリを変更する**：
  レポートの場所をカスタマイズするには、以下を追加します：

  ```xml
  <configuration>
      <destFile>${project.build.directory}/custom-jacoco.exec</destFile>
      <dataFile>${project.build.directory}/custom-jacoco.exec</dataFile>
      <outputDirectory>${project.build.directory}/custom-reports</outputDirectory>
  </configuration>
  ```

---

### **まとめ**
JaCoCo Mavenプラグインを使用するには：
1. `prepare-agent`および`report`ゴールを含むプラグインを`pom.xml`に追加します。
2. プロジェクトにテストが設定されていることを確認します（通常はSurefire経由）。
3. `mvn verify`を実行してカバレッジレポートを生成します。
4. `target/site/jacoco/index.html`でレポートを確認します。

この設定は、コードカバレッジをMavenビルドプロセスに統合する簡単な方法を提供し、テストの効果を評価するのに役立ちます。最新のプラグインバージョンや高度な構成については、[公式JaCoCoドキュメント](https://www.jacoco.org/jacoco/trunk/doc/maven.html)を参照してください。