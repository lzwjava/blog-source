---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおける日付と時刻の操作
translated: true
type: note
---

### 主なポイント
- `org.joda.time` を使用するには、Javaプロジェクトに追加し、日付と時刻の操作のためにそのクラスをインポートする必要があるようです。
- 調査によると、バージョン2.13.1でMaven経由でライブラリを含めるか、JARファイルをダウンロードし、`DateTime` や `LocalDate` などのクラスを使用することが推奨されています。
- 証拠から、Joda-Timeはタイムゾーン、暦システム、時間間隔の処理に有用であり、日付オブジェクトの作成や変更などの例が示されています。

### Joda-Timeとはとセットアップ方法
Joda-Timeは、Javaで日付と時刻を扱うためのライブラリで、特にJava 8以前において、古くてスレッドセーフでない `Date` と `Calendar` クラスを置き換える直感的なAPIを提供します。これを使用するには、まずプロジェクトにライブラリを含めます。Mavenを使用する場合は、`pom.xml` に以下の依存関係を追加します：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
あるいは、[このウェブサイト](https://www.joda.org/joda-time/download.html) からJARファイルをダウンロードし、Eclipseなどで「libs」フォルダを作成してプロジェクトプロパティ経由でJARをリンクするなど、プロジェクトのクラスパスに追加します。

### 基本的な使用例
セットアップ後、`org.joda.time.DateTime` や `org.joda.time.LocalDate` などのクラスをインポートします。以下にいくつかの例を示します：
- 現在の日時を作成: `DateTime now = new DateTime();`
- フィールドにアクセス: `int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- 変更: `DateTime future = now.plusDays(5);`

### 高度な機能
Joda-Timeはタイムゾーン（例: `DateTimeZone.forID("America/New_York")`）や異なる暦システム（例: `CopticChronology.getInstance()` によるコプト暦）をサポートします。また、`Interval interval = new Interval(startDt, endDt);` のような間隔と期間の処理も行います。

予期しない詳細として、Joda-Timeは「完成した」プロジェクトと見なされており、新しいプロジェクトにはJava 8の `java.time` パッケージが推奨されていますが、レガシーシステムや特定のニーズには依然として関連しています。

---

### 調査ノート: `org.joda.time` 使用包括的ガイド

このセクションでは、`org.joda.time` ライブラリの使用について詳細に探求し、直接的な回答を追加の文脈と技術的深さで拡張し、徹底的な理解を求める開発者に適しています。セットアップ、使用例、主な機能、さらなるリソースを含み、実装のための完全なリファレンスを保証します。

#### Joda-Timeの紹介
Joda-Timeは、joda.orgによって開発された、広く使用されている日付と時刻の処理ライブラリで、特にJava 8のリリース以前に顕著でした。不変クラスを使用することで、スレッドセーフ性の懸念などのJava `Date` および `Calendar` クラスの設計上の問題に対処します。Java 8以前では、`Date` クラスと `SimpleDateFormatter` はスレッドセーフではなく、日/月/年のオフセットなどの操作（例えば、日が0から始まり、月が1から始まり、`Calendar` を必要とする）は直感的ではありませんでした。Joda-Timeは、クリーンで流暢なAPIを提供し、Javaの2つ（グレゴリオ暦と和暦）に対して8つの暦システムをサポートします。Java 8以降、作者はJoda-Timeをほぼ完成したものと見なし、新しいプロジェクトには `java.time` (JSR-310) への移行を推奨していますが、レガシーシステムや特定のユースケースでは依然として関連しています。

#### Joda-Timeのセットアップ
Joda-Timeを使用するには、まずJavaプロジェクトに含める必要があります。2025年3月3日時点での最新バージョンは2.13.1で、JDK 1.5以降との安定性と互換性を確保しています。Mavenユーザーは、`pom.xml` に以下の依存関係を追加します：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
これは [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) で見つけることができます。Mavenを使用しないプロジェクトでは、[このウェブサイト](https://www.joda.org/joda-time/download.html) から `.tar.gz` ファイルをダウンロードし、展開し、`joda-time-2.13.1.jar` をプロジェクトのクラスパスに追加します。例えば、Eclipseでは、「libs」フォルダを作成し、JARをコピーし、Properties -> Java Build Path -> Libraries -> Add Jars 経由でリンクします。セットアップを `DateTime test = new DateTime();` でテストして機能を確認します。

#### 基本的な使用法と例
含めた後、`org.joda.time` から `DateTime`、`LocalDate`、`LocalTime`、`LocalDateTime` などのクラスをインポートします。これらはすべて不変であり、スレッドセーフです。以下に詳細な例を示します：

- **日時オブジェクトの作成:**
  - 現在時刻から: `DateTime now = new DateTime();` はデフォルトのタイムゾーンとISO暦を使用します。
  - Java `Date` から: `java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` で相互運用性を持たせます。
  - 特定の値から: コンストラクタは `Long` (ミリ秒)、`String` (ISO8601)、または他のJoda-Timeオブジェクトを受け入れます。例: `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`.

- **フィールドへのアクセス:**
  - ゲッターメソッドを使用: `int year = now.getYear(); int month = now.getMonthOfYear();` ここで1月は1、12月は12です。
  - テキスト表現の場合: `String dayName = now.dayOfWeek().getAsText();` は、例えば2025年3月3日の場合 "Monday" を出力します。
  - プロパティをチェック: `boolean isLeap = now.year().isLeap();` は2025年に対して `false` を返します。

- **日時の変更:**
  - 変更を加えて新しいインスタンスを作成: `DateTime newDt = now.withYear(2025);` または `DateTime future = now.plusDays(5);`.
  - 期間を追加: `DateTime later = now.plusHours(2);` で2時間を追加し、新しいインスタンスを返します。

GeeksforGeeksからの実用的な例を示します：
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
2025年3月3日の場合、出力には "Current Day: Monday"、"Current Month: March"、"Current Year: 2025"、"Current Year is Leap Year: false"、および "2025-03-03T08:39:00.000" のようなタイムスタンプが含まれる可能性があります。

#### 主な機能と高度な使用法
Joda-Timeは、複雑な日時操作に対する堅牢な機能を提供します。以下に詳細を示します：

- **タイムゾーン:**
  - `DateTimeZone` 経由で管理され、名前付きゾーン（例: "Asia/Tokyo"）と固定オフセットをサポートします。例：
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - デフォルトゾーンはJDKのものと一致しますが、`DateTimeZone.setDefault(zone);` でオーバーライドできます。タイムゾーンデータは年に数回手動で更新され、[global-tz](https://github.com/JodaOrg/global-tz) に基づいています。

- **暦システム:**
  - 7つのシステムをサポート: Buddhist, Coptic, Ethiopic, Gregorian, GregorianJulian, Islamic, Julian。カスタムシステムの提供も可能。例：
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - デフォルトはISO暦で、1583年以前は歴史的に不正確ですが、現代の市民用途には適しています。

- **間隔、期間、ピリオド:**
  - `Interval`: 時間範囲を表し、半開区間（開始を含み、終了を含まない）。例: `Interval interval = new Interval(startDt, endDt);`.
  - `Duration`: ミリ秒単位の正確な時間。例: `Duration duration = new Duration(interval);`。インスタントへの追加に有用。
  - `Period`: フィールド（年、月、日など）で定義され、ミリ秒単位では不正確。例: `Period period = new Period(startDt, endDt);`。例の違い：夏時間（例: 2005-03-26 12:00:00）で1日を `plus(Period.days(1))` で追加すると23時間追加され、`plus(new Duration(24L*60L*60L*1000L))` で24時間追加され、ピリオドと期間の動作の違いを強調します。

クイックスタートガイドは、主なクラスとユースケースをまとめた表を提供します：
| **側面**                  | **詳細**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **主な日時クラス**   | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5クラス、すべて不変)               |
| **Instantのユースケース**         | イベントのタイムスタンプ、暦システムやタイムゾーンなし                                          |
| **LocalDateのユースケース**       | 生年月日、時刻は不要                                                           |
| **LocalTimeのユースケース**       | 時刻、例えば店の開閉時間、日付なし                                               |
| **DateTimeのユースケース**        | 汎用、JDK Calendarを置き換え、タイムゾーン情報を含む                          |
| **コンストラクタの種類**        | オブジェクトコンストラクタが受け入れるもの: Date, Calendar, String (ISO8601), Long (ミリ秒), Joda-Timeクラス |
| **変換の例**       | `java.util.Date` から `DateTime`: `DateTime dt = new DateTime(new Date());`                      |
| **フィールドアクセスメソッド**     | `getMonthOfYear()` (1=1月, 12=12月), `getYear()`                                        |
| **変更メソッド**     | `withYear(2000)`, `plusHours(2)`                                                               |
| **プロパティメソッドの例**| `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **デフォルトの暦システム**  | ISO暦システム (事実上の市民暦、1583年以前は歴史的に不正確)              |
| **デフォルトのタイムゾーン**        | JDKデフォルトと同じ、オーバーライド可能                                                         |
| **Chronologyクラス**         | 複数の暦システムをサポート、例: `CopticChronology.getInstance()`                     |
| **タイムゾーンの例**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Intervalクラス**           | `Interval` - 開始と終了の日時を保持、範囲に基づく操作                          |
| **Periodクラス**             | `Period` - 6ヶ月、3日、7時間のような期間を保持、間隔から導出可能               |
| **Durationクラス**           | `Duration` - ミリ秒単位の正確な期間、間隔から導出可能                          |
| **PeriodとDurationの例**| 夏時間で1日を追加 (2005-03-26 12:00:00): `plus(Period.days(1))` は23時間追加、`plus(new Duration(24L*60L*60L*1000L))` は24時間追加 |

興味深い詳細は、オブジェクトコンストラクタの拡張性にあり、JDK `Date` や `Calendar` からの変換を直接渡すことで可能にし、レガシーコードからの移行を簡素化します。

#### さらなる学習とリソース
より深く探求するには、[Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html) の公式ドキュメントを参照してください。これは、フォーマットとパースのような高度なトピックをカバーしています。[Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) のクイックスタートガイドは、簡潔な紹介を提供します。追加のチュートリアルは [Baeldung Joda-Time](https://www.baeldung.com/joda-time) と [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) で利用可能で、コード例とセットアップ手順を含みます。[Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) のAPIドキュメントは、より技術的ですがリファレンスとして有用です。

#### 結論
Joda-Timeは、日付と時刻の操作に対する堅牢でスレッドセーフな代替手段を提供し、タイムゾーン、暦システム、時間計算に対する広範なサポートを備えています。Java 8以降では完成したものと見なされていますが、Mavenまたは手動のJAR包含によるセットアップ、および `DateTime` や `LocalDate` などの不変クラスを通じた使用により、レガシーシステムに対して価値を保っています。このガイドは、開発者が基本的な例から高度な機能まで、実装に必要なすべての情報を、包括的なリソースによって保証します。

### 主な引用文献
- [Joda-Time Home Page with General Information](https://www.joda.org/joda-time/)
- [Joda-Time Quick Start Guide for Beginners](https://www.joda.org/joda-time/quickstart.html)
- [Baeldung Tutorial on Joda-Time Usage](https://www.baeldung.com/joda-time)
- [GeeksforGeeks Article on Joda-Time with Examples](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Time User Guide for Detailed Reference](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time Download and Installation Page](https://www.joda.org/joda-time/download.html)
- [Maven Repository for Joda-Time Dependency](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time API Documentation for Technical Reference](https://www.joda.org/joda-time/apidocs/index.html)