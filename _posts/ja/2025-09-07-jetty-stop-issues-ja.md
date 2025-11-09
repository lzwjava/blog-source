---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: フォークされたJettyの停止問題の修正
translated: true
type: note
---

実際にはほとんどのことを正しく行っていましたが、ハングするのはほぼ常に、**stop goalがフォークされたJettyに到達できない**（stopHost/port/keyスコープが間違っている）か、**`run-forked`が予期せずMavenにアタッチされたまま**になるためです。以下に2つの確実な修正方法を示します。どちらかをお選びください。

### オプションA — 信頼性の高いパターン: `jetty:start` (デーモン) + `jetty:stop`

これは`run-forked`を完全に回避し、ITライフサイクルにおいて最も安定しています。

**変更点**

1. プラグインバージョンを固定し、`pre-integration-test`フェーズで`daemon=true`を設定した`start`を使用します。
2. PythonのITを`integration-test`フェーズに保持します。
3. `post-integration-test`フェーズで`stop`を使用します。
4. **両方の**実行で*同じ*`stopHost/stopPort/stopKey`を指定します。

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <configuration>
    <httpConnector>
      <port>8080</port>
      <host>127.0.0.1</host>
    </httpConnector>
  </configuration>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>start</goal>
      </goals>
      <configuration>
        <daemon>true</daemon>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
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

**これが「スタック」を修正する理由**

* `daemon=true`により、`start`は直ちに制御をMavenに戻すため、ITを実行できます。
* 一致する`stopHost/stopPort/stopKey`により、`stop` mojoが同じJettyに確実に到達します。
* `run-forked`のモニタースレッドの動作に依存しません。

---

### オプションB — `run-forked`を維持し、stopを実際に機能させる

`run-forked`を希望する場合、一般的な落とし穴は以下の通りです:

* `stopHost`のデフォルトが、子プロセスのバインド方法（IPv6 vs IPv4）と異なる場合があります。
* `stopPort/stopKey`が開始実行でのみ設定され、停止実行に**反映されていない**。
* 設定が誤っている場合、子プロセスがstopハンドラーを公開しない。

**以下のように設定を厳密にします:**

```xml
<plugin>
  <groupId>org.eclipse.jetty</groupId>
  <artifactId>jetty-maven-plugin</artifactId>
  <version>9.4.54.v20240208</version>

  <executions>
    <execution>
      <id>start-jetty</id>
      <phase>pre-integration-test</phase>
      <goals>
        <goal>run-forked</goal>
      </goals>
      <configuration>
        <stopHost>127.0.0.1</stopHost>
        <stopPort>8081</stopPort>
        <stopKey>stop</stopKey>
        <stopWait>15</stopWait>

        <httpConnector>
          <host>127.0.0.1</host>
          <port>8080</port>
        </httpConnector>

        <jvmArgs>
          -javaagent:${settings.localRepository}/org/jacoco/org.jacoco.agent/${jacoco.version}/org.jacoco.agent-${jacoco.version}-runtime.jar=destfile=${jacoco.it.exec},append=true
        </jvmArgs>
        <webApp>
          <contextPath>/</contextPath>
        </webApp>
      </configuration>
    </execution>

    <execution>
      <id>stop-jetty</id>
      <phase>post-integration-test</phase>
      <goals>
        <goal>stop</goal>
      </goals>
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

**追加のガードレール**

* あなたのmacOS/JavaがIPv6を選択し、stop goalがIPv4を使用する場合、子プロセスの`jvmArgs`に`-Djava.net.preferIPv4Stack=true`を追加します:

  ```
  <jvmArgs>
    -Djava.net.preferIPv4Stack=true
    -javaagent:...
  </jvmArgs>
  ```
* `8081`に他の何もないことを確認してください。もし使用中なら、開始と停止の両方を別の空きポートに変更します。
* ITがクラッシュまたはハングした場合、`post-integration-test`は実行されない可能性があります。その場合、`verify`フェーズでのkillフォールバックを追加してください（下記参照）。

---

### オプションの安全策 — `stop`が失敗した場合に子プロセスを強制終了する

ファイルに書き出されたPIDを使用して、フォークされたJettyを強制的に終了する小さなヘルパーを追加します:

1. `run-forked`/`start`設定内で:

```
<pidFile>${project.build.directory}/jetty.pid</pidFile>
```

2. `post-integration-test`の後、`verify`フェーズで`exec-maven-plugin`を追加し、pidファイルをチェックして、プロセスがまだ生きている場合に強制終了します。

---

### ログからのいくつかの細かい注意点

* `No Spring WebApplicationInitializer types detected`は、`web.xml` + DispatcherServletを使用している場合は正常であり、停止のハングとは関係ありません。
* ITを**maven-failsafe-plugin**（`integration-test`/`verify`にバインド）に移動し、ユニットテストをsurefireに維持することを検討してください。現在の`exec-maven-plugin`アプローチは機能しますが、failsafeはITライフサイクルにより良く統合されます。

---

必要であれば、**完全な**Jettyプラグインブロックと（ローカルリポジトリパス用の）`settings.xml`ミラーを貼り付けてください。あなたのリポジトリに合わせて正確な最小限の差分を調整します。