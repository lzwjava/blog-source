---
audio: false
generated: true
lang: hant
layout: post
title: Java 日期與時間操作
translated: true
type: note
---

### 重點摘要
- 要使用 `org.joda.time`，您可能需要將其加入 Java 專案並導入其類別來進行日期與時間操作。
- 研究建議透過 Maven 加入版本 2.13.1 的函式庫，或下載 JAR 檔案，然後使用如 `DateTime` 和 `LocalDate` 等類別。
- 證據顯示 Joda-Time 在處理時區、曆法系統和時間區間方面相當有用，例如建立日期物件並進行修改。

### 什麼是 Joda-Time 及其設定方法
Joda-Time 是一個用於處理 Java 日期與時間的函式庫，在 Java 8 之前尤其有用，提供直觀的 API 以取代較舊且線程安全性較差的 `Date` 和 `Calendar` 類別。使用前需先將函式庫加入專案。若使用 Maven，請在 `pom.xml` 中加入以下依賴項：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
或者，從[此網站](https://www.joda.org/joda-time/download.html)下載 JAR 檔案，並將其加入專案的 classpath，例如在 Eclipse 中建立 "libs" 資料夾並透過專案屬性連結 JAR。

### 基本使用範例
設定完成後，導入如 `org.joda.time.DateTime` 或 `org.joda.time.LocalDate` 等類別。以下是一些範例：
- 建立當前日期時間：`DateTime now = new DateTime();`
- 存取欄位：`int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- 修改：`DateTime future = now.plusDays(5);`

### 進階功能
Joda-Time 支援時區（例如 `DateTimeZone.forID("America/New_York")`）和不同曆法系統（例如透過 `CopticChronology.getInstance()` 使用科普特曆）。它還能處理區間和持續時間，例如 `Interval interval = new Interval(startDt, endDt);`。

一個意外的細節是 Joda-Time 被視為「已完成」的專案，Java 8 的 `java.time` 套件被推薦用於新專案，但對於遺留系統或特定需求仍具相關性。

---

### 調查筆記：使用 `org.joda.time` 的完整指南

本節詳細探討如何使用 `org.joda.time` 函式庫，在直接答案的基礎上擴展額外上下文和技術深度，適合尋求全面理解的開發人員。內容包括設定、使用範例、關鍵功能和進一步資源，確保為實作提供完整參考。

#### Joda-Time 簡介
Joda-Time 由 joda.org 開發，是一個廣泛使用的日期與時間處理函式庫，尤其在 Java 8 發布之前。它透過使用不可變類別解決了 Java `Date` 和 `Calendar` 類別的設計問題，例如線程安全疑慮。在 Java 8 之前，`Date` 類別和 `SimpleDateFormatter` 並非線程安全，且操作如日/月/年偏移直觀性差（例如天數從 0 開始、月份從 1 開始，需使用 `Calendar`）。Joda-Time 提供清晰、流暢的 API，並支援八種曆法系統，而 Java 僅支援兩種（公曆和日本皇曆）。Java 8 之後，作者認為 Joda-Time 基本已完成，推薦新專案遷移至 `java.time` (JSR-310)，但對於遺留系統或特定用例仍具相關性。

#### 設定 Joda-Time
要使用 Joda-Time，必須先將其加入 Java 專案。截至 2025 年 3 月 3 日，最新版本為 2.13.1，確保穩定性和與 JDK 1.5 或更高版本的相容性。Maven 使用者請在 `pom.xml` 中加入以下依賴項：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
可在 [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) 找到。非 Maven 專案請從[此網站](https://www.joda.org/joda-time/download.html)下載 `.tar.gz` 檔案，解壓縮後將 `joda-time-2.13.1.jar` 加入專案的 classpath。例如在 Eclipse 中，建立 "libs" 資料夾，複製 JAR 並透過 Properties -> Java Build Path -> Libraries -> Add Jars 連結。使用 `DateTime test = new DateTime();` 測試設定以確保功能正常。

#### 基本使用與範例
加入後，從 `org.joda.time` 導入類別，如 `DateTime`、`LocalDate`、`LocalTime` 和 `LocalDateTime`，所有類別均為不可變以確保線程安全。以下是詳細範例：

- **建立日期時間物件：**
  - 從當前時間：`DateTime now = new DateTime();` 使用預設時區和 ISO 曆法。
  - 從 Java `Date`：`java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` 以實現互通性。
  - 從特定值：建構函式接受 `Long`（毫秒）、`String`（ISO8601）或其他 Joda-Time 物件，例如 `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`。

- **存取欄位：**
  - 使用 getter 方法：`int year = now.getYear(); int month = now.getMonthOfYear();` 其中一月為 1，十二月為 12。
  - 文字表示：`String dayName = now.dayOfWeek().getAsText();` 輸出如 2025 年 3 月 3 日的 "Monday"。
  - 檢查屬性：`boolean isLeap = now.year().isLeap();` 對 2025 年返回 `false`。

- **修改日期時間：**
  - 建立修改後的新實例：`DateTime newDt = now.withYear(2025);` 或 `DateTime future = now.plusDays(5);`。
  - 添加持續時間：`DateTime later = now.plusHours(2);` 用於添加兩小時，返回新實例。

GeeksforGeeks 的實用範例說明用法：
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
對於 2025 年 3 月 3 日，輸出可能包括 "Current Day: Monday"、"Current Month: March"、"Current Year: 2025"、"Current Year is Leap Year: false"，以及時間戳記如 "2025-03-03T08:39:00.000"。

#### 關鍵功能與進階使用
Joda-Time 為複雜的日期時間操作提供強大功能，詳細如下：

- **時區：**
  - 透過 `DateTimeZone` 管理，支援命名時區（例如 "Asia/Tokyo"）和固定偏移。範例：
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - 預設時區與 JDK 相同，但可透過 `DateTimeZone.setDefault(zone);` 覆寫。時區資料每年手動更新數次，基於 [global-tz](https://github.com/JodaOrg/global-tz)。

- **曆法系統：**
  - 支援七種系統：佛曆、科普特曆、埃塞俄比亞曆、公曆、公曆-儒略曆、伊斯蘭曆、儒略曆，並提供自訂系統的機制。範例：
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - 預設為 ISO 曆法，1583 年之前歷史不準確，但適合現代民用。

- **區間、持續時間與期間：**
  - `Interval`：代表時間範圍，半開區間（起始包含，結束不包含），例如 `Interval interval = new Interval(startDt, endDt);`。
  - `Duration`：精確的毫秒時間，例如 `Duration duration = new Duration(interval);`，適用於添加到時間點。
  - `Period`：以欄位定義（年、月、日等），毫秒不精確，例如 `Period period = new Period(startDt, endDt);`。範例差異：在夏令時添加 1 天（例如 2005-03-26 12:00:00）時，`plus(Period.days(1))` 添加 23 小時，而 `plus(new Duration(24L*60L*60L*1000L))` 添加 24 小時，凸顯期間與持續時間的行為差異。

快速入門指南提供表格總結主要類別和用例：
| **方面**                  | **詳細資訊**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **主要日期時間類別**   | Instant、DateTime、LocalDate、LocalTime、LocalDateTime（5 個類別，均為不可變）               |
| **Instant 用例**         | 事件時間戳，無曆法系統或時區                                          |
| **LocalDate 用例**       | 出生日期，無需時間                                               |
| **LocalTime 用例**       | 一天中的時間，例如商店營業時間，無日期                                                |
| **DateTime 用例**        | 通用目的，取代 JDK Calendar，包含時區資訊                          |
| **建構函式類型**        | 物件建構函式接受：Date、Calendar、String (ISO8601)、Long (毫秒)、Joda-Time 類別 |
| **轉換範例**       | `java.util.Date` 轉 `DateTime`：`DateTime dt = new DateTime(new Date());`                      |
| **欄位存取方法**     | `getMonthOfYear()` (1=一月, 12=十二月)、`getYear()`                                        |
| **修改方法**     | `withYear(2000)`、`plusHours(2)`                                                               |
| **屬性方法範例**| `monthOfYear().getAsText()`、`monthOfYear().getAsShortText(Locale.FRENCH)`、`year().isLeap()`、`dayOfMonth().roundFloorCopy()` |
| **預設曆法系統**  | ISO 曆法系統（事實上的民用曆法，1583 年前歷史不準確）              |
| **預設時區**        | 與 JDK 預設相同，可覆寫                                                         |
| **Chronology 類別**         | 支援多種曆法系統，例如 `CopticChronology.getInstance()`                     |
| **時區範例**        | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`、`GJChronology.getInstance(zone)`      |
| **Interval 類別**           | `Interval` - 保存開始和結束日期時間，基於範圍的操作                          |
| **Period 類別**             | `Period` - 保存期間如 6 個月、3 天、7 小時，可從區間推導                |
| **Duration 類別**           | `Duration` - 精確的毫秒持續時間，可從區間推導                          |
| **Period 與 Duration 範例**| 在夏令時添加 1 天（2005-03-26 12:00:00）：`plus(Period.days(1))` 添加 23 小時，`plus(new Duration(24L*60L*60L*1000L))` 添加 24 小時 |

一個有趣的細節是物件建構函式的可擴展性，允許直接傳遞 JDK `Date` 或 `Calendar` 進行轉換，簡化從遺留代碼的遷移。

#### 進一步學習與資源
深入探索請參考官方文件 [Joda-Time User Guide](https://www.joda.org/joda-time/userguide.html)，涵蓋進階主題如格式化和解析。快速入門指南 [Joda-Time Quick Start](https://www.joda.org/joda-time/quickstart.html) 提供簡明介紹。額外教程可在 [Baeldung Joda-Time](https://www.baeldung.com/joda-time) 和 [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) 找到，包含代碼範例和設定說明。API 文件 [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) 適合技術參考。

#### 結論
Joda-Time 為日期與時間操作提供強大、線程安全的替代方案，廣泛支援時區、曆法系統和時間計算。雖然在 Java 8 後被視為已完成，但對遺留系統仍具價值，可透過 Maven 或手動加入 JAR 進行設定，並透過不可變類別如 `DateTime` 和 `LocalDate` 使用。本指南確保開發人員擁有從基本範例到進階功能的所有必要資訊，並由完整資源支援。

### 主要引用文獻
- [Joda-Time 首頁與一般資訊](https://www.joda.org/joda-time/)
- [Joda-Time 快速入門指南](https://www.joda.org/joda-time/quickstart.html)
- [Baeldung Joda-Time 使用教程](https://www.baeldung.com/joda-time)
- [GeeksforGeeks Joda-Time 文章與範例](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Time 用戶指南詳細參考](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time 下載與安裝頁面](https://www.joda.org/joda-time/download.html)
- [Maven Repository Joda-Time 依賴項](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time API 文件技術參考](https://www.joda.org/joda-time/apidocs/index.html)