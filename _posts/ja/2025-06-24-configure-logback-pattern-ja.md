---
audio: false
generated: true
lang: ja
layout: post
title: カスタムログフォーマットのためのLogback設定
translated: true
type: note
---

指定されたログ形式を実現するには、`logback.xml`ファイルを設定する必要があります。鍵は、アペンダー内で`PatternLayout`を使用し、`pattern`プロパティを正しく設定することです。

以下に、目的のログ形式の構成要素と、それらをLogbackのパターンコンバーターにマッピングする方法を示します：

* **`2025-06-15T01:37:52.452+08:00`**: タイムスタンプです。これには`%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`を使用します。
    * `yyyy-MM-dd'T'HH:mm:ss.SSS`: 日付と時刻（ミリ秒を含む）。
    * `XXX`: UTCからのISO 8601オフセット（例: `+08:00`）。
* **`DEBUG`**: ロギングレベルです。`%-5p`（左揃え、5文字幅）を使用します。
* **`302244`**: プロセスIDです。Logbackは標準のコンバーターでプロセスIDを直接公開しません。ただし、**スレッドID**（`%t`または`%thread`）は公開しています。例の「302244」が実際にはスレッドID（アプリケーションログで非常に一般的）である場合、`%thread`が必要です。これがOSのプロセスIDで*なければならない*場合、カスタムLogbackコンバーターまたは環境が許せばシステムプロパティが必要になる可能性があります。典型的なSpring Bootアプリケーションでは、これは通常スレッドIDです。この例ではスレッドIDであると仮定します。
* **`---`**: リテラル文字列です。
* **`[nio-8090-exec-1]`**: スレッド名です。`[%thread]`または固定幅にしたい場合は`%-40.40thread`を使用します。
* **`o.s.w.s.m.m.a.HttpEntityMethodProcessor`**: ロガー名（通常は完全修飾クラス名）です。右揃えで最大39文字に切り詰められたロガー名を取得するには、`%-40.40logger{39}`を使用します。
* **`:`**: リテラルのコロンです。
* **`Writing ["{"vnstatversion":"2.9","jsonversion":"2","interfaces":[{"name":"enp4s0","alias":"","created":{"date" (truncated)..."]`**: ログメッセージです。`%msg%n`を使用します。

非常に類似した出力を生成するはずの`logback.xml`設定のサンプルを以下に示します：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %highlight(%-5p) %thread --- [%thread] %-40.40logger{39} : %msg%n</pattern>
        </encoder>
    </appender>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>

    <logger name="org.springframework.web.servlet.mvc.method.annotation.HttpEntityMethodProcessor" level="DEBUG"/>
    <logger name="org.springframework.web.servlet.DispatcherServlet" level="DEBUG"/>

</configuration>
```

**`pattern`の説明：**

* `%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX}`: ミリ秒とタイムゾーンオフセットを含むISO 8601形式の日付と時刻。
* `%highlight(%-5p)`: ロギングレベル（例: DEBUG, INFO）を左揃えで5文字で出力し、コンソールに出力する場合、Logbackは色付けを試みます。
* `%thread`: ログイベントを記録したスレッドの名前。（プロセスIDが必要な場合はより複雑になりますが、Springアプリでは通常、スレッドIDがここでは関連します）。
* `---`: リテラル文字列の区切り文字。
* `[%thread]`: 角括弧で囲まれたスレッド名。
* `%-40.40logger{39}`: ロガーの名前（通常はクラス名）。
    * `%-40`: 左揃えで40文字にパディング。
    * `.40logger`: ロガー名が40文字より長い場合に切り詰めます。
    * `{39}`: パッケージ名の末尾から最大39文字のロガー名を表示するようLogbackに指示します（例：`o.s.w.s.m.m.a.HttpEntityMethodProcessor`は、収まる場合はそのまま、または先頭から切り詰められる場合は`...HttpEntityMethodProcessor`になる可能性があります）。この数値は調整できます。
* ` :  `: リテラルのコロンとスペース。
* `%msg%n`: 実際のログメッセージとそれに続く改行。

**重要な注意点：**

1.  **配置:** このXMLをSpring Bootプロジェクトの`src/main/resources`ディレクトリに`logback.xml`として保存します。
2.  **プロセスIDとスレッドID:** 前述のとおり、Logbackの標準パターンコンバーターはOSのプロセスIDを直接公開しません。`302244`が*必ず*プロセスIDでなければならない場合、通常、カスタムの`PatternLayoutConverter`を実装するか、起動時にシステムプロパティを設定し、そのログバックパターンで参照する必要があります。ただし、ほとんどのアプリケーションロギングでは、スレッドID（`%thread`）で十分であり、この位置で一般的に使用されています。
3.  **Spring Bootのデフォルト:** Spring Bootは、独自のデフォルトのLogback設定を提供しない場合、独自のデフォルトを提供することがよくあります。`src/main/resources`に`logback.xml`を配置することで、デフォルトを上書きします。
4.  **ロガーレベル:** 特定のロガー（`HttpEntityMethodProcessor`や`DispatcherServlet`など）のDEBUGメッセージを表示したい場合は、それらが`DEBUG`レベルに設定されていることを確認してください。ルートレベルが`INFO`の場合、デフォルトでは、特定のロガーのレベルを明示的に設定しない限り、DEBUGメッセージは表示されません。

この設定により、目的のログ形式に非常に近いものが得られるはずです。