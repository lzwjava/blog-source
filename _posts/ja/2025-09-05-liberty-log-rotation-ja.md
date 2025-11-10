---
audio: false
generated: true
image: false
lang: ja
layout: post
title: リバティログローテーション設定ガイド
translated: true
type: note
---

以下に概要と、`server.xml`に貼り付けて使用できる例を示します。

### Libertyのログローテーションの仕組み

* **ローテーション対象:** `messages.log` と `trace.log`。
  ローテーションは **サイズベース** および/または **時間ベース** で行えます。([openliberty.io][1])
* **ローテーション非対象:** `console.log` (これは単なるstdout/stderrです)。代わりにこれを削減または無効化できます。([openliberty.io][2], [IBM][3])
* **設定箇所:** `server.xml`内の`<logging …/>`要素。(`server.xml`が読み込まれる*前*に適用する必要がある場合は、`bootstrap.properties`/環境変数で同じ値を設定することもできます。) ([openliberty.io][2])
* **アクセスログ:** HTTPアクセスログは、`httpAccessLogging` / `accessLogging`の下に、それ自身の**独立した**時間ベースのロールオーバー設定を持っています。([openliberty.io][4])
* **サイズ＋時間の両方:** モダンなLibertyは、従来のサイズベースオプションに加えて時間ベースのロールオーバーをサポートしているため、いずれか、または両方を使用できます (`console.log`を除く)。([IBM][5])

---

### よく使われる `server.xml` のレシピ

#### 1) サイズベースのローテーション (クラシック)

最大10ファイル、各ファイル最大256 MBを保持します。

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="10"/>
```

効果: `messages.log` または `trace.log` が 256 MB を超えると、Libertyはそれをタイムスタンプ付きのファイルにロールオーバーし、そのようなファイルを最大10個保持します。(`console.log`には影響しません。) ([openliberty.io][1])

#### 2) 時間ベースのローテーション (例: 毎日深夜0時)

```xml
<logging
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

効果: `messages.log` と `trace.log` は毎日00:00にロールオーバーします。分(`m`)や時間(`h`)も使用できます (例: `30m` や `6h`)。([openliberty.io][2])

#### 3) サイズ＋時間の組み合わせ (典型的な本番環境)

```xml
<logging
  logDirectory="${server.output.dir}/logs"
  maxFileSize="256"
  maxFiles="14"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>
```

効果: **サイズまたはスケジュールのいずれか早い方**でロールオーバーし、14ファイル分の履歴を保持します。([IBM][5])

#### 4) `console.log` の肥大化を抑制または無効化

`console.log`はローテーションできません。これを削減またはオフにして、`messages.log`に依存します。

```xml
<logging
  consoleLogLevel="OFF"
  copySystemStreams="false"/>
```

注意: コンソールをオフにすると、Liberty自身による`console.log`へのログコピーは停止しますが、JVMは依然として`-verbose:gc`のようなものをstdout/stderrに書き込む可能性があります。([openliberty.io][2])

#### 5) 名前/フォーマットの調整 (オプション)

```xml
<logging
  messageFileName="messages.log"
  traceFileName="trace.log"
  messageFormat="JSON"/>
```

JSONはログスタックに送信する場合に便利です。必要なければデフォルトのままにしておきます。([openliberty.io][1])

---

### HTTPアクセスログ (上記とは別設定)

アクセスログを有効にし、毎日深夜0時にロールオーバーさせます:

```xml
<httpAccessLogging id="accessLogging"
  rolloverStartTime="00:00"
  rolloverInterval="1d"/>

<httpEndpoint id="defaultHttpEndpoint"
  httpPort="9080" httpsPort="9443"
  accessLoggingRef="accessLogging"/>
```

(または、`rolloverStartTime`/`rolloverInterval`を`httpEndpoint`の子要素である`<accessLogging …/>`に直接記述することもできます。) ([openliberty.io][4])

---

### クイックチェックリスト

* サイズベースのロールオーバーには **`maxFileSize` + `maxFiles`** を使用します。([openliberty.io][1])
* 時間ベースのロールオーバーには **`rolloverStartTime` + `rolloverInterval`** を使用します。([openliberty.io][2])
* **`console.log`がローテーションすることを期待しないでください**。大きなコンソールファイルを避けたい場合は、`consoleLogLevel="OFF"` と `copySystemStreams="false"` を設定します。([openliberty.io][2], [IBM][3])

現在の`server.xml`のスニペットや保持目標 (例: 「約7日間保持」や「2 GBで制限」) を共有していただければ、正確な値を調整します。

[1]: https://openliberty.io/docs/latest/reference/config/logging.html "Logging (logging) :: Open Liberty Docs"
[2]: https://openliberty.io/docs/latest/log-trace-configuration.html "Log and trace configuration :: Open Liberty Docs"
[3]: https://www.ibm.com/support/pages/how-turn-console-logging-prevent-excess-file-growth-and-use-only-message-log-rotation-liberty-profile-or-open-liberty?utm_source=chatgpt.com "How to turn off Console logging, prevent excess file growth ..."
[4]: https://openliberty.io/docs/latest/access-logging.html "HTTP access logging :: Open Liberty Docs"
[5]: https://www.ibm.com/support/pages/how-setup-liberty-log-rollover-both-time-based-and-size-based-options-similar-traditional-websphere-0?utm_source=chatgpt.com "How to setup Liberty Log Rollover with both Time-Based ..."