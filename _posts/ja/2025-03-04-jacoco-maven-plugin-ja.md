---
audio: false
generated: true
lang: ja
layout: post
title: JaCoCo Maven プラグイン
translated: true
---

ここでは、MavenベースのJavaプロジェクトでコードカバレッジを測定するために**JaCoCo Mavenプラグインを使用する方法**についてのステップバイステップガイドを提供します。JaCoCo（Java Code Coverage）は、Mavenと統合して、テスト（通常はユニットテスト）によってどれだけのコードが実行されているかを追跡するツールです。プロジェクトにJaCoCo Mavenプラグインを追加し設定することで、ビルドプロセス中に詳細なカバレッジレポートを生成できます。

---

### **JaCoCo Mavenプラグインの使用方法**

#### **1. `pom.xml`にJaCoCo Mavenプラグインを追加**
JaCoCo Mavenプラグインを使用するには、プロジェクトの`pom.xml`ファイルの`<build><plugins>`セクションに含める必要があります。以下は、プラグインを設定する基本的な構成です：

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.jacoco</groupId>
            <artifactId>jacoco-maven-plugin</artifactId>
            <version>0.8.12</version> <!-- 利用可能な最新バージョンを使用 -->
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

- **`groupId`、`artifactId`、`version`**: これらはJaCoCo Mavenプラグインを識別します。`0.8.12`を[Maven Central Repository](https://mvnrepository.com/artifact/org.jacoco/jacoco-maven-plugin)で利用可能な最新バージョンに置き換えてください。
- **`<executions>`**: このセクションは、プラグインがMavenビルドライフサイクル中にどのように実行されるかを設定します：
  - **`<goal>prepare-agent</goal>`**: テスト実行中にカバレッジデータを収集するためにJaCoCoエージェントを準備します。デフォルトでは、早いフェーズ（例：`initialize`）にバインドされ、明示的なフェーズが指定されない限りカスタマイズされません。
  - **`<goal>report</goal>`**: テストが実行された後にカバレッジレポートを生成します。ここでは、`test`フェーズの後に実行される`verify`フェーズにバインドされています。

#### **2. テストの設定を確認**
JaCoCoプラグインは、Maven Surefireプラグインによって実行されるテスト（通常はユニットテスト）の実行を分析します。ほとんどのMavenプロジェクトでは、Surefireはデフォルトで含まれており、`src/test/java`にあるテストを実行します。追加の設定は必要ありませんが、テストが非標準の場合は確認してください。以下を確認してください：
- ユニットテストが書かれている（例：JUnitまたはTestNGを使用）。
- Surefireプラグインが存在する（デフォルトのMaven親POMから継承されることが多い）。

Surefireを明示的に設定する必要がある場合、以下のようになります：

```xml
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <version>3.5.0</version> <!-- 利用可能な最新バージョンを使用 -->
</plugin>
```

`prepare-agent`ゴールは、`argLine`プロパティを変更してカバレッジ追跡を有効にすることで、JaCoCoエージェントを設定します。

#### **3. Mavenビルドを実行**
カバレッジレポートを生成するには、プロジェクトディレクトリで以下のコマンドを実行します：

```bash
mvn verify
```

- **`mvn verify`**: これは、`compile`、`test`、`verify`を含むすべてのフェーズを実行します。JaCoCoプラグインは以下を行います：
  1. テストが実行される前にエージェントを準備します。
  2. `test`フェーズ（Surefireがテストを実行するとき）中にカバレッジデータを収集します。
  3. `verify`フェーズ中にレポートを生成します。

また、テストのみを実行して`verify`に進まない場合は、以下を使用します：

```bash
mvn test
```

ただし、この設定では、`report`ゴールが`verify`にバインドされているため、`mvn verify`を実行してレポートを表示する必要があります。レポートを`mvn test`中に生成したい場合、`report`実行の`<phase>`を`test`に変更することもできますが、`verify`は一般的な慣習です。

#### **4. カバレッジレポートを確認**
`mvn verify`を実行すると、JaCoCoはデフォルトでHTMLレポートを生成します。以下の場所にあります：

```
target/site/jacoco/index.html
```

- このファイルを開いて、パッケージ、クラス、メソッド、行ごとの詳細なカバレッジの概要を確認します。
- このレポートには、CIシステムと統合するために便利なXMLおよびCSV形式も同じディレクトリにあります（`jacoco.xml`および`jacoco.csv`）。

---

### **オプションのカスタマイズ**
より高度な使用例では、プラグインの設定を調整できます：

- **クラスまたはパッケージの除外**:
  カバレッジ分析から特定のコードを除外するには（例：生成されたコード）、`<configuration>`セクションを追加します：

  ```xml
  <configuration>
      <excludes>
          <exclude>**/generated/**/*</exclude>
      </excludes>
  </configuration>
  ```

  これを`<plugin>`タグ内、`<executions>`の上に配置します。

- **カバレッジの閾値を強制**:
  カバレッジが閾値を下回った場合にビルドを失敗させるには、`check`ゴールを追加します：

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
                          <minimum>0.80</minimum> <!-- 80%の行カバレッジ -->
                      </limit>
                  </limits>
              </rule>
          </rules>
      </configuration>
  </execution>
  ```

- **レポートの出力ディレクトリを変更**:
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
1. `pom.xml`にプラグインを追加し、`prepare-agent`および`report`ゴールを設定します。
2. プロジェクトにテストが設定されていることを確認します（通常はSurefireを使用）。
3. `mvn verify`を実行してカバレッジレポートを生成します。
4. `target/site/jacoco/index.html`でレポートを確認します。

この設定は、Mavenビルドプロセスにコードカバレッジを簡単に統合する方法を提供し、テストの効果を評価するのに役立ちます。最新のプラグインバージョンや高度な設定については、[公式JaCoCoドキュメント](https://www.jacoco.org/jacoco/trunk/doc/maven.html)を参照してください。