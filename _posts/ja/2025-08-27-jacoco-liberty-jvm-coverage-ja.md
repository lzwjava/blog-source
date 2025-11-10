---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Liberty JVMカバレッジのためのJaCoCo
translated: true
type: note
---

できますよ―JaCoCoをあなたのEARを実行する**Liberty JVM**にアタッチしましょう。鍵は、JaCoCoがあなたのPythonランナーではなく、Libertyと同じJVM内に存在しなければならないことです。

以下は信頼性の高いセットアップです（いずれか一つを選んでください）。

---

## 1) シンプルで堅牢: JVM終了時にファイルに書き出す

**使用する場面:** テスト後にLibertyサーバーを停止できる場合。

1. **エージェントjarを利用可能にする** (ビルド時に一度だけ)

```xml
<!-- jacoco agent を target/jacoco/jacocoagent.jar にコピー -->
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-dependency-plugin</artifactId>
  <version>3.6.1</version>
  <executions>
    <execution>
      <id>copy-jacoco-agent</id>
      <phase>prepare-package</phase>
      <goals><goal>copy</goal></goals>
      <configuration>
        <artifactItems>
          <artifactItem>
            <groupId>org.jacoco</groupId>
            <artifactId>org.jacoco.agent</artifactId>
            <version>0.8.12</version>
            <classifier>runtime</classifier>
            <destFileName>jacocoagent.jar</destFileName>
          </artifactItem>
        </artifactItems>
        <outputDirectory>${project.build.directory}/jacoco</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

2. **Liberty JVMオプションを追加する** (ファイル: `wlp/usr/servers/<serverName>/jvm.options`)

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=file,append=false,includes=com.myco.*,excludes=org.slf4j.*,destfile=${server.output.dir}/jacoco/jacoco-it.exec
```

* `jacocoagent.jar` を `wlp/usr/servers/<serverName>/jacoco/` (または任意の読み取り可能なパス) に配置します。
* あなたのパッケージに合わせて `includes`/`excludes` を調整してください。

3. **実行フロー**

* Libertyを起動 (`server start <serverName>`)、EARをデプロイ。
* Pythonの `unittest` を実行 (エンドポイントにリクエストを送信)。
* Libertyを停止 (`server stop <serverName>`)。
  → エージェントが `${server.output.dir}/jacoco/jacoco-it.exec` を書き出します。

4. **レポートを生成**

* もしプロジェクトがマルチモジュール (EAR + EJB + WAR) の場合、アグリゲータpomと `report-aggregate` を使用します:

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-aggregate</goal></goals>
      <configuration>
        <dataFile>${env.SERVER_OUTPUT_DIR}/jacoco/jacoco-it.exec</dataFile>
        <includes>
          <include>com/myco/**</include>
        </includes>
      </configuration>
    </execution>
  </executions>
</plugin>
```

(または `jacococli` を使用:)

```bash
java -jar jacococli.jar report /path/to/jacoco-it.exec \
  --classfiles module1/target/classes --classfiles module2/target/classes \
  --sourcefiles module1/src/main/java --sourcefiles module2/src/main/java \
  --html target/jacoco-it-report
```

---

## 2) Libertyを停止せずにライブダンプ (TCPサーバーモード)

**使用する場面:** Libertyを実行したままにして、オンデマンドでカバレッジを取得したい場合。

1. `jvm.options`:

```text
-javaagent:${server.config.dir}/jacoco/jacocoagent.jar=output=tcpserver,address=*,port=6300,append=false,includes=com.myco.*
```

2. Libertyを実行し、Pythonテストを実行した後、**ダンプ**を取得:

```bash
# TCP経由でカバレッジを取得し、ローカルに .exec ファイルを書き出します
java -jar jacococli.jar dump --address 127.0.0.1 --port 6300 --destfile jacoco-it.exec --reset
```

あとは上記と同様にレポートを生成します。
ヒント: `--reset` はカウンターをリセットするので、長時間の実行中に複数のスナップショットを取得できます。

---

## 3) コンテナ / CI (環境変数スタイル)

* Docker/K8sでLibertyを実行する場合、エージェントをマウントし、以下を設定します:

  * 上記のように `jvm.options` を設定する、**または**
  * 同じ `-javaagent=...` を含む `WLP_JAVA_OPTIONS` / `JAVA_TOOL_OPTIONS` 環境変数を設定する。
* 複数のLiberty JVMからなるクラスターの場合、それぞれに異なるTCPポートまたはファイルパスを割り当て、その後**マージ**します:

```bash
java -jar jacococli.jar merge node1.exec node2.exec --destfile merged.exec
```

---

## 注意点と落とし穴

* **EARのレイアウトは**JaCoCoには関係ありません。それはメモリ内のバイトコードをインストルメントします。レポート生成には、きれいなHTMLレポートのための、あなたのモジュール (`target/classes`) からの**元のクラスファイル**とそのソースファイルが必要です。
* Java 17/21互換性のために**最近のJaCoCo (0.8.12以上)**を使用してください (Libertyは多くの場合OpenJ9/HotSpot上で動作します―どちらも問題ありません)。
* サードパーティのライブラリをカウントしないように `includes/excludes` に注意してください。
* もし `.exec` ファイルが空の場合、以下の可能性があります:

  * エージェントのアタッチを忘れた、
  * あなたのパッケージがフィルタリングされた、
  * または、コードにトラフィックが到達する前にダンプを取得した。

---

もしあなたのEARのモジュールレイアウト (EJB/WARモジュールとパッケージルート) を共有していただければ、正確な `report-aggregate` 設定と、Liberty起動→Pythonテスト実行→ダンプ取得→HTMLレポート構築を一気通貫で行う小さなスクリプトをお伝えできます。