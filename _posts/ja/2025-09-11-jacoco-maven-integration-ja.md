---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: JaCoCoとMavenの連携の理解
translated: true
type: note
---

了解しました。以下に、**あなたのPOMファイル**におけるJaCoCoの各構成がどのように連携するかをステップバイステップで説明します。

---

# このPOMが生成する2種類のカバレッジデータ

1. **単体テストカバレッジ (Surefire経由)**

* JaCoCoの **`prepare-agent`** を特別な設定なしでバインドしています:

  ```xml
  <execution>
    <id>prepare-agent</id>
    <goals><goal>prepare-agent</goal></goals>
  </execution>
  ```

  これは、`argLine`プロパティを通じて **Surefire** のテストJVMに `-javaagent:...org.jacoco.agent-<ver>-runtime.jar` を注入します。
  • デフォルトの **destfile** は `${project.build.directory}/jacoco.exec` です。
  • デフォルトの **append** は `true` です (JaCoCoエージェントはファイルが既に存在する場合に追記します)。
  • 効果: `test` フェーズで単体テストを実行すると (もしあれば)、カバレッジは `target/jacoco.exec` に書き込まれます。

2. **結合テストカバレッジ (Jetty経由)**

* ITカバレッジ用に **別ファイル** を定義しています:

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
  </properties>
  ```
* Jettyを **独自のJaCoCoエージェント** で起動し、そのファイルを指すように設定しています:

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
        </jvmArgs>
        ...
      </configuration>
    </execution>
  </plugin>
  ```

  • Jettyは **別のJVM** として実行されます。そのエージェントは `target/jacoco-it.exec` に書き込みます。
  • `append` が指定されていないため、JaCoCoのデフォルト `append=true` が適用されます。よって、クリーンしないか `append=false` を設定しない限り、複数回のJetty起動で同じファイルに追記されます。

---

# ライフサイクルの流れ (`mvn verify` 実行時)

1. **compile**

   * Spotlessによるフォーマット (`spotless-maven-plugin`) と Checkstyleの実行 (`maven-checkstyle-plugin`)。
   * WARファイルの準備 (`maven-war-plugin`)。

2. **test (Surefire)**

   * 単体テストがある場合、それらは **`prepare-agent`** によって注入されたargLineの下で実行されます → カバレッジは `target/jacoco.exec` に記録されます。

3. **pre-integration-test**

   * Jettyが **デーモンモード** で起動されます:

     ```xml
     <daemon>true</daemon>
     ```

     Mavenは直ちに制御を回復します。JettyはJaCoCoエージェントがアタッチされた状態で動作を継続し、`jacoco-it.exec` に書き込み続けます。

4. **integration-test**

   * Pythonテストが動作中のアプリケーションにリクエストを送信します:

     ```xml
     <plugin>
       <artifactId>exec-maven-plugin</artifactId>
       <execution>
         <id>python-integration-tests</id>
         <phase>integration-test</phase>
         <goals><goal>exec</goal></goals>
         <configuration>
           <executable>python3</executable>
           <workingDirectory>${project.parent.basedir}</workingDirectory>
           <arguments>
             <argument>-m</argument><argument>unittest</argument>
             <argument>discover</argument><argument>tests/</argument>
             <argument>-v</argument>
           </arguments>
         </configuration>
       </execution>
     </plugin>
     ```

     これらのテストはJettyを実行するため、カバレッジはJetty JVMのエージェントを通じて **`target/jacoco-it.exec`** に蓄積されます。

5. **post-integration-test**

   * Jettyが適切に停止されます:

     ```xml
     <execution>
       <id>stop-jetty</id>
       <phase>post-integration-test</phase>
       <goals><goal>stop</goal></goals>
       ...
     </execution>
     ```

6. **verify**

   * ITデータファイルとカスタム出力ディレクトリを使用して、**独立したITレポート** を生成します:

     ```xml
     <execution>
       <id>report-it</id>
       <phase>verify</phase>
       <goals><goal>report</goal></goals>
       <configuration>
         <dataFile>${jacoco.it.exec}</dataFile>
         <outputDirectory>${project.reporting.outputDirectory}/jacoco-it
         </outputDirectory>
       </configuration>
     </execution>
     ```
   * 結果: HTMLレポートが `target/site/jacoco-it/index.html` に生成され、**結合** テストカバレッジ (Jettyからのもの) のみをまとめて表示します。

> 注意: **単体テスト** 用のレポートも必要な場合は、デフォルトの `target/jacoco.exec` を指し、`target/site/jacoco` に出力する別の `jacoco:report` 実行を追加できます。これにより、単体テストとITのレポートを分離して管理できます。

---

# `.exec` ファイルに関する「新規作成か上書きか？」

* **JaCoCoエージェントのデフォルトは `append=true`** です。

  * **単体テスト** の場合、ファイルは `target/jacoco.exec` です。`clean` せずに `mvn verify` を繰り返し実行すると、データは実行間で追記される可能性があります。
  * **Jetty IT** の場合、あなたの `jvmArgs` は `append` を上書きしないため、`target/jacoco-it.exec` もデフォルトで **追記** されます。

**ベストプラクティス** (古いデータが混入するのを防ぐため):

* `mvn clean verify` を実行する、**または** Jettyエージェントの行に `append=false` を追加します:

  ```xml
  -javaagent:...org.jacoco.agent-...-runtime.jar=destfile=${jacoco.it.exec},append=false
  ```
* 意図的に複数の `.exec` ファイルをマージしたい場合は、`jacoco:report` の前に `jacoco:merge` を使用します。

---

# 元のXML内の関連ブロックの役割 (参照用)

* **ITファイルの場所**

  ```xml
  <properties>
    <jacoco.it.exec>${project.build.directory}/jacoco-it.exec</jacoco.it.exec>
    <it.report.skip>false</it.report.skip>
  </properties>
  ```

  結合テストカバレッジの保存場所を定義します。`it.report.skip` は宣言されていますが、まだレポート実行に紐づけられていません (下記のヒントを参照)。

* **単体テストエージェント (Surefire経由)**

  ```xml
  <plugin>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>prepare-agent</id>
        <goals><goal>prepare-agent</goal></goals>
      </execution>
      ...
    </executions>
  </plugin>
  ```

* **IT用のJaCoCo付きJetty**

  ```xml
  <plugin>
    <artifactId>jetty-maven-plugin</artifactId>
    ...
    <jvmArgs>
      -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec}
    </jvmArgs>
    ...
  </plugin>
  ```

* **Jetty動作中のPython結合テスト**

  ```xml
  <plugin>
    <artifactId>exec-maven-plugin</artifactId>
    <execution>
      <id>python-integration-tests</id>
      <phase>integration-test</phase>
      <goals><goal>exec</goal></goals>
      ...
    </execution>
  </plugin>
  ```

* **verifyフェーズでのITカバレッジレポート生成**

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

---

# 実用的なヒント / 小さな改善点

* **古いITデータを避ける**
  Jettyエージェントに `append=false` を追加する (上記参照)、または常に `mvn clean verify` を実行する。

* **`it.report.skip` スイッチを有効化する**
  プロパティ経由でITレポートの生成をスキップしたい場合:

  ```xml
  <execution>
    <id>report-it</id>
    <phase>verify</phase>
    <goals><goal>report</goal></goals>
    <configuration>
      <skip>${it.report.skip}</skip>
      <dataFile>${jacoco.it.exec}</dataFile>
      <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
    </configuration>
  </execution>
  ```

* **単体テストとITレポートは分離したままにする**
  ITレポートを `site/jacoco-it` に分離することは既に行われています。単体テストレポートも必要な場合は、`dataFile` の上書きなしで `site/jacoco` に書き込む別の `jacoco:report` を追加してください。

* **マルチモジュールに関する注意**
  このモジュールローカルな設定は、**PlaygroundWeb** のみのカバレッジをレポートします。後で **結合** ビューが必要になった場合は、親の `pom` (で `packaging=pom`) から `jacoco:merge` (`.exec` ファイルを結合するため) および/または `report-aggregate` (JaCoCo 0.8.8以降) を使用してください。

---

# 要約

* **単体テスト** → `prepare-agent` がSurefire JVMにJaCoCoを注入 → `target/jacoco.exec`。
* **結合テスト** → Jettyが独自のJaCoCoエージェントで起動 → `target/jacoco-it.exec`。
* **レポート** → `verify` フェーズで、`jacoco:report` が **ITカバレッジのみ** を `target/site/jacoco-it` にレンダリング。
* **ファイルの動作** → JaCoCoは **デフォルトで追記**。実行間の混合を避けるため、`mvn clean verify` または `append=false` を推奨。