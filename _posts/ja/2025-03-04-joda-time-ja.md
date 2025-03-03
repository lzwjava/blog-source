---
audio: false
generated: true
lang: ja
layout: post
title: 日付と時刻の操作
translated: true
---

### 主要ポイント
- `org.joda.time` を使用するためには、Javaプロジェクトに追加し、日付と時間の操作に使用するクラスをインポートする必要があります。
- 研究によると、Mavenを使用してバージョン2.13.1でライブラリを含めるか、JARファイルをダウンロードし、`DateTime`や`LocalDate`のようなクラスを使用することが推奨されています。
- 証拠は、Joda-Timeがタイムゾーン、カレンダーシステム、時間間隔の処理に役立つことを示しており、日付オブジェクトの作成やその変更の例があります。

### Joda-Timeとは、そしてその設定方法
Joda-Timeは、Javaで日付と時間を扱うためのライブラリで、特にJava 8以前に有用です。古い`Date`と`Calendar`クラスを置き換える直感的なAPIを提供します。使用するには、まずプロジェクトにライブラリを含めます。Mavenを使用している場合は、`pom.xml`に次の依存関係を追加します：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
または、[このウェブサイト](https://www.joda.org/joda-time/download.html)からJARファイルをダウンロードし、プロジェクトのクラスパスに追加します。例えば、Eclipseでは、「libs」フォルダを作成し、プロジェクトのプロパティからJARをリンクします。

### 基本的な使用例
設定が完了したら、`org.joda.time.DateTime`や`org.joda.time.LocalDate`のようなクラスをインポートします。以下にいくつかの例を示します：
- 現在の日付と時間を作成する: `DateTime now = new DateTime();`
- フィールドにアクセスする: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- 修正する: `DateTime future = now.plusDays(5);`

### 高度な機能
Joda-Timeはタイムゾーン（例：`DateTimeZone.forID("America/New_York")`）、異なるカレンダーシステム（例：コプティックの`CopticChronology.getInstance()`）、間隔と期間（例：`Interval interval = new Interval(startDt, endDt);`）をサポートしています。

Joda-Timeは「完了した」プロジェクトとされており、新しいプロジェクトにはJava 8の`java.time`パッケージが推奨されますが、引き続きレガシーシステムや特定のニーズに対して関連性があります。

---

### アンケートノート: `org.joda.time`の使用に関する包括的なガイド

このセクションでは、`org.joda.time`ライブラリの使用に関する詳細な探求を行い、直接の回答に追加のコンテキストと技術的な深みを提供します。開発者が包括的な理解を得るために、設定、使用例、主要な機能、さらにリソースを含みます。

#### Joda-Timeの紹介
Joda-Timeは、joda.orgによって開発された広く使用されている日付と時間の処理ライブラリで、特にJava 8のリリース以前に有用です。Javaの`Date`と`Calendar`クラスの設計上の問題、例えばスレッドセーフ性の問題を解決するために、不変のクラスを使用します。Java 8以前では、`Date`クラスと`SimpleDateFormatter`はスレッドセーフではありませんでした。Joda-Timeは、直感的なフルエントAPIを提供し、8つのカレンダーシステムをサポートします。Javaの2つ（グレゴリオ暦と日本の皇紀）に対してです。Java 8以降、Joda-Timeは「完了した」とされており、新しいプロジェクトには`java.time`（JSR-310）への移行が推奨されますが、引き続きレガシーシステムや特定の使用例に対して関連性があります。

#### Joda-Timeの設定
Joda-Timeを使用するには、まずJavaプロジェクトに含める必要があります。2025年3月3日現在の最新バージョンは2.13.1で、JDK 1.5以降との互換性と安定性が確保されています。Mavenユーザーは、`pom.xml`に次の依存関係を追加します：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
これは[Mavenリポジトリ](https://mvnrepository.com/artifact/joda-time/joda-time)で見つけることができます。Mavenを使用していないプロジェクトでは、[このウェブサイト](https://www.joda.org/joda-time/download.html)から`.tar.gz`ファイルをダウンロードし、展開し、`joda-time-2.13.1.jar`をプロジェクトのクラスパスに追加します。例えば、Eclipseでは、「libs」フォルダを作成し、JARをコピーし、プロパティ -> Javaビルドパス -> ライブラリ -> JARを追加してリンクします。設定をテストするには、`DateTime test = new DateTime();`を使用して機能を確認します。

#### 基本的な使用と例
含まれると、`org.joda.time`からクラスをインポートします。例えば、`DateTime`、`LocalDate`、`LocalTime`、`LocalDateTime`など、すべてがスレッドセーフのために不変です。以下に詳細な例を示します：

- **日付と時間のオブジェクトを作成する:**
  - 現在の時間から: `DateTime now = new DateTime();`はデフォルトのタイムゾーンとISOカレンダーを使用します。
  - Javaの`Date`から: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);`は相互運用性を提供します。
  - 特定の値から: コンストラクタは`Long`（ミリ秒）、`String`（ISO8601）、または他のJoda-Timeオブジェクトを受け入れます。例えば、`DateTime dt = new DateTime(2025, 3, 3, 8, 39);`。

- **フィールドにアクセスする:**
  - ゲッターメソッドを使用: `int year = now.getYear(); int month = now.getMonthOfYear();`で1月は1、12月は12です。
  - 文字列表現: `String dayName = now.dayOfWeek().getAsText();`は、例えば、2025年3月3日の場合「月曜」を出力します。
  - プロパティを確認: `boolean isLeap = now.year().isLeap();`は2025年の場合`false`を返します。

- **日付と時間を修正する:**
  - 修正された新しいインスタンスを作成: `DateTime newDt = now.withYear(2025);`または`DateTime future = now.plusDays(5);`。
  - 期間を追加: `DateTime later = now.plusHours(2);`は2時間を追加し、新しいインスタンスを返します。

GeeksforGeeksの実践的な例を示します：
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("Current Day: " + now.dayOfWeek().getAsText());
        System.out.println("Current Month: " + now.monthOfYear().getAsText());
        System.out.println("Current Year: " + now.year().getAsText());
        System.out.println("Current Year is Leap Year: " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
2025年3月3日の場合、出力には「Current Day: Monday」、「Current Month: March」、「Current Year: 2025」、「Current Year is Leap Year: false」、タイムスタンプ「2025-03-03T08:39:00.000」が含まれるかもしれません。

#### 主要な機能と高度な使用
Joda-Timeは複雑な日付と時間の操作に対する強力な機能を提供します。以下に詳細を示します：

- **タイムゾーン:**
  - `DateTimeZone`を通じて管理され、名前付きゾーン（例：「Asia/Tokyo」）と固定オフセットをサポートします。例:
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - デフォルトゾーンはJDKのものと一致しますが、`DateTimeZone.setDefault(zone);`でオーバーライドできます。タイムゾーンデータは、[global-tz](https://github.com/JodaOrg/global-tz)に基づいて、年に数回手動で更新されます。

- **カレンダーシステム:**
  - 7つのシステムをサポート: ブッディズム、コプティック、エチオピア、グレゴリオ暦、グレゴリオ暦ユリウス暦、イスラム、ユリウス暦、カスタムシステムの提供もあります。例:
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - デフォルトはISOカレンダーで、1583年以前は歴史的に正確ではありませんが、現代の民事用途には適しています。

- **間隔、期間、期間:**
  - `Interval`: 時間範囲を表し、半開（開始は含まれ、終了は含まれない）です。例: `Interval interval = new Interval(startDt, endDt);`。
  - `Duration`: ミリ秒単位の正確な時間です。例: `Duration duration = new Duration(interval);`はインスタントに追加するのに役立ちます。
  - `Period`: フィールド（年、月、日など）で定義され、ミリ秒では不正確です。例: `Period period = new Period(startDt, endDt);`。期間と期間の違い: 夏時間（例: 2005-03-26 12:00:00）に1日を追加する場合、`plus(Period.days(1))`は23時間を追加し、`plus(new Duration(24L*60L*60L*1000L))`は24時間を追加し、期間と期間の動作を示します。

クイックスタートガイドには、主要なクラスと使用例をまとめた表があります：
| **アスペクト**                  | **詳細**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **メインの日付と時間のクラス**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5クラス、すべて不変)               |
| **Instantの使用例**         | イベントのタイムスタンプ、カレンダーシステムやタイムゾーンなし                                          |
| **LocalDateの使用例**       | 誕生日、時刻は必要ありません                                                           |
| **LocalTimeの使用例**       | 時刻、例: ショップの営業時間、日付なし                                               |
| **DateTimeの使用例**        | 一般的な用途、JDK Calendarを置き換え、タイムゾーン情報を含む                          |
| **コンストラクタの種類**        | オブジェクトコンストラクタは、Date、Calendar、String（ISO8601）、Long（ミリ秒）、Joda-Timeクラスを受け入れます |
| **例の変換**       | `java.util.Date`を`DateTime`に: `DateTime dt = new DateTime(new Date());`                      |
| **フィールドアクセスメソッド**     | `getMonthOfYear()`（1=1月、12=12月）、`getYear()`                                        |
| **修正メソッド**     | `withYear(2000)`、`plusHours(2)`                                                               |
| **プロパティメソッドの例**| `monthOfYear().getAsText()`、`monthOfYear().getAsShortText(Locale.FRENCH)`、`year().isLeap()`、`dayOfMonth().roundFloorCopy()` |
| **デフォルトのカレンダーシステム**  | ISOカレンダーシステム（事実上の民事カレンダー、1583年以前は歴史的に正確ではありません）              |
| **デフォルトのタイムゾーン**        | JDKのデフォルトと同じ、オーバーライド可能                                                         |
| **Chronologyクラス**         | 複数のカレンダーシステムをサポート、例: `CopticChronology.getInstance()`                     |
| **タイムゾーンの例**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`、`GJChronology.getInstance(zone)`      |
| **Intervalクラス**           | `Interval` - 開始と終了の日付と時間を保持、範囲に基づく操作                          |
| **Periodクラス**             | `Period` - 期間（例: 6ヶ月、3日、7時間）を保持、間隔から導出可能               |
| **Durationクラス**           | `Duration` - 間隔から導出可能なミリ秒単位の正確な期間                          |
| **期間と期間の例**| 夏時間（2005-03-26 12:00:00）に1日を追加する: `plus(Period.days(1))`は23時間を追加し、`plus(new Duration(24L*60L*60L*1000L))`は24時間を追加します |

オブジェクトコンストラクタの拡張性は、JDKの`Date`や`Calendar`を直接渡すことで、レガシーコードからの移行を簡素化します。

#### さらに学ぶためのリソース
より深い探求には、[Joda-Timeユーザーガイド](https://www.joda.org/joda-time/userguide.html)の公式ドキュメントを参照してください。これは、フォーマットと解析のような高度なトピックをカバーしています。[Joda-Timeクイックスタート](https://www.joda.org/joda-time/quickstart.html)のクイックスタートガイドは、簡潔な導入を提供します。追加のチュートリアルは、[Baeldung Joda-Time](https://www.baeldung.com/joda-time)と[GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/)でコード例と設定手順が含まれています。[Joda-Time APIドキュメント](https://www.joda.org/joda-time/apidocs/index.html)はリファレンスとして有用ですが、より技術的です。

#### 結論
Joda-Timeは、スレッドセーフな代替手段として、日付と時間の操作を提供し、タイムゾーン、カレンダーシステム、時間計算のサポートが豊富です。Java 8以降は「完了した」とされていますが、引き続きレガシーシステムに対して価値があります。Mavenまたは手動のJARの含有、不変のクラス`DateTime`や`LocalDate`を通じた使用を通じて設定されます。このガイドは、開発者が実装に必要なすべての情報を提供し、基本的な例から高度な機能まで、包括的なリソースをサポートします。

### 主要な引用
- [Joda-Timeホームページの一般情報](https://www.joda.org/joda-time/)
- [Joda-Timeクイックスタートガイド](https://www.joda.org/joda-time/quickstart.html)
- [BaeldungのJoda-Time使用チュートリアル](https://www.baeldung.com/joda-time)
- [GeeksforGeeksのJoda-Timeの記事](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Timeユーザーガイドの詳細リファレンス](https://www.joda.org/joda-time/userguide.html)
- [Joda-Timeのダウンロードとインストールページ](https://www.joda.org/joda-time/download.html)
- [MavenリポジトリのJoda-Time依存関係](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time APIドキュメントの技術リファレンス](https://www.joda.org/joda-time/apidocs/index.html)