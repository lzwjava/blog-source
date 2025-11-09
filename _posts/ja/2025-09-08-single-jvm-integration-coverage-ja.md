---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ja
layout: post
title: シングルJVM統合カバレッジ戦略
translated: true
type: note
---

Jettyを2回実行したり、モジュールごとに個別のJaCoCoの`.exec`ファイルを作成する必要はありません。あなたのWARを提供する単一のJVM上で動作する1つのエージェントが、**そのJVMがロードするすべてのクラス**（`PlaygroundUtils`を含む）のカバレッジを**1つの共有execファイル**に記録できます。その後、各モジュールはその同じexecファイルを参照して独自のレポートを生成できます。大きなリアクター（10以上のモジュール）の場合、これはきれいにスケールします。

以下は、あなたのリポジトリに対する具体的で最小限の計画とそのまま適用できる編集内容です。

---

## 戦略

1.  **親レベルで単一の共有IT execファイルを使用する。**
    JaCoCoで計装されたJettyを**1回だけ**起動し、`../target/it-coverage/jacoco-it.exec`（親スコープのパス）に書き込むようにする。
2.  **外部のPythonテストを1回実行する。**
    これらはデプロイされたアプリにアクセスし、エージェントはロードされたすべてのクラス（Web + ライブラリ）のヒットを記録する。
3.  **モジュールごとのレポートを生成する**。各モジュールは共有の`jacoco-it.exec`を参照する。
    `PlaygroundUtils`はテストがなくてもレポートを取得する — 共有のexecを自身の`target/classes`にマッピングする。
4.  （オプション）親で`report-aggregate`を使用して**集約HTMLも生成する**、または単にモジュールごとのレポートを保持する。

**複数のJVM**（例えば、いくつかのマイクロサービス）が本当にある場合にのみ、複数のexecファイルと`jacoco:merge`ステップが必要になります。現在の単一JVM（Jetty）ビルドでは、1つのexecに抑えてください。

---

## 正確な編集内容

### 1) 親 `pom.xml` (PlaygroundLib)

すべてのモジュールが同じexecファイルを参照できるように、共有プロパティを追加します：

```xml
<properties>
  <!-- ... 既存のバージョン ... -->
  <it.coverage.dir>${project.basedir}/target/it-coverage</it.coverage.dir>
  <jacoco.it.exec>${it.coverage.dir}/jacoco-it.exec</jacoco.it.exec>
  <!-- モジュールごとのITレポート生成をトグル -->
  <it.report.skip>false</it.report.skip>
</properties>
```

（オプション）親で単一の**集約**HTMLが必要な場合は、この実行を追加します：

```xml
<build>
  <pluginManagement>
    <!-- 既存のブロックを保持 -->
  </pluginManagement>

  <plugins>
    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>it-aggregate-report</id>
          <phase>verify</phase>
          <goals>
            <goal>report-aggregate</goal>
          </goals>
          <configuration>
            <!-- Jetty実行で生成された共有IT execを使用 -->
            <dataFile>${jacoco.it.exec}</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

> あなたのJaCoCoバージョンが`report-aggregate`での`<dataFile>`を拒否する場合は、このオプションブロックをスキップして、以下のモジュールごとのレポートに依存してください。後で`merge` + `report`を実行するための小さな「カバレッジ」集約モジュールを追加することは常に可能です。

---

### 2) `PlaygroundWeb/pom.xml`

Jettyエージェントを**親レベル**のexecパスに向け、appendを有効にします：

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals><goal>start</goal></goals>
      <configuration>
        <daemon>true</daemon>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${project.parent.basedir}/target/it-coverage/jacoco-it.exec,append=true,includes=org.lzw.*
        </jvmArgs>
        <httpConnector>
          <port>8080</port>
          <host>127.0.0.1</host>
        </httpConnector>
        <webApp><contextPath>/</contextPath></webApp>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals><goal>stop</goal></goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>
      </configuration>
    </execution>
  </executions>
</plugin>
```

`PlaygroundWeb`内の`jacoco:report`を更新して、**同じ**共有execを読み取るようにします：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
      <configuration>
        <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
        <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

`python -m unittest discover tests -v`を実行する既存のExec Maven Pluginは完璧です — そのままにしておいてください。

---

### 3) `PlaygroundUtils/pom.xml`

共有execを自身のクラスにマッピングできるように、**レポートのみ**の実行を追加します：

```xml
<build>
  <plugins>
    <!-- 既存のプラグインを保持 -->

    <plugin>
      <groupId>org.jacoco</groupId>
      <artifactId>jacoco-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>report-it</id>
          <phase>verify</phase>
          <goals><goal>report</goal></goals>
          <configuration>
            <dataFile>${project.parent.basedir}/target/it-coverage/jacoco-it.exec</dataFile>
            <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
            <skip>${it.report.skip}</skip>
          </configuration>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

このモジュールはJettyを起動したりPythonを実行したりすることはありません。共有execと自身の`target/classes`のみを消費します。テスト中にWebアプリによって`PlaygroundUtils`クラスが使用されていれば、それらはカバレッジとして表示されます。実行されていない場合は0%になります — これは正しいシグナルです。

---

## 実行方法

リポジトリのルートから：

```bash
mvn -pl PlaygroundWeb -am clean verify
```

このビルド順序は、両方のモジュールをコンパイルし、エージェントとともにJettyを1回起動し、Pythonテストを実行し、Jettyを停止し、その後以下を生成します：

*   `PlaygroundWeb/target/site/jacoco-it/index.html`
*   `PlaygroundUtils/target/site/jacoco-it/index.html`
*   `report-aggregate`を有効にした場合、オプションで親配下に集約レポート。

---

## 10モジュールある場合

*   10個すべてが**同じWAR/JVM**内にある場合は、**単一共有exec**パターンを維持します。すべてのモジュールが共有execを指す`report`実行を追加します。Jettyは1回だけ起動し、Pythonは1回だけ実行します。

*   **複数のJVM**（例えば、別々のサービス）がある場合は、各JVMに独自の`destfile`（例: `it-coverage/serviceA.exec`, `serviceB.exec`）を与え、その後親で以下を実行します：

  ```xml
  <plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
      <execution>
        <id>merge-it</id>
        <phase>post-integration-test</phase>
        <goals><goal>merge</goal></goals>
        <configuration>
          <destFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</destFile>
          <files>
            <file>${project.basedir}/target/it-coverage/serviceA.exec</file>
            <file>${project.basedir}/target/it-coverage/serviceB.exec</file>
            <!-- 必要に応じて追加 -->
          </files>
        </configuration>
      </execution>

      <execution>
        <id>aggregate-report</id>
        <phase>verify</phase>
        <goals><goal>report-aggregate</goal></goals>
        <configuration>
          <dataFile>${project.basedir}/target/it-coverage/jacoco-merged.exec</dataFile>
          <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
        </configuration>
      </execution>
    </executions>
  </plugin>
  ```

*   ノイズを制限したい場合は、エージェント行に`includes=org.lzw.*`（既に表示済み）を追加するか、`excludes`を追加してサードパーティライブラリをフィルタリングします。

---

## 現在の問題が発生する理由

*   あなたは**モジュールごとのexecファイル**を作成していたため、それぞれを埋めるために異なるエージェントでJettyを再実行することを強いられていると感じていました。それは不要です。エージェントはクラスがどのモジュールに「属しているか」を気にしません — ロードされたすべてのクラスを記録します。execを集中化し、各モジュールの`report`がそれを指すようにします。

---

## クイックチェックリスト

*   親の下に1つの**共有**`${jacoco.it.exec}`。
*   Jettyは`append=true`と`includes=org.lzw.*`で**1回だけ**起動。
*   Pythonテストは**1回だけ**実行。
*   各モジュールは共有execを読み取る`jacoco:report`を持つ。
*   単一のトップレベルHTMLのためのオプションの親`report-aggregate`。

これにより、あなたのセットアップはよりシンプルかつスケーラブルになるはずです。必要であれば、これらの変更を適用した現在のPOMに対する正確な差分を提供できます。