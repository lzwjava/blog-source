---
audio: false
generated: true
lang: hant
layout: post
title: 日期和時間操作
translated: true
---

### 關鍵要點
- 使用 `org.joda.time` 似乎需要將其添加到 Java 專案中並導入其類別以進行日期和時間操作。
- 研究建議通過 Maven 使用版本 2.13.1 或下載 JAR 文件，然後使用類別如 `DateTime` 和 `LocalDate`。
- 證據表明 Joda-Time 適用於處理時區、日曆系統和時間間隔，例如創建日期對象並修改它們。

### 什麼是 Joda-Time 以及如何設置
Joda-Time 是一個用於在 Java 中處理日期和時間的庫，特別是在 Java 8 之前非常有用，提供了一個直觀的 API 來替換較舊的、不太安全的 `Date` 和 `Calendar` 類。要使用它，首先在專案中包含庫。如果使用 Maven，將以下依賴項添加到 `pom.xml`：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
或者，從 [這個網站](https://www.joda.org/joda-time/download.html) 下載 JAR 文件，並將其添加到專案的類路徑中，例如在 Eclipse 中創建一個 "libs" 資料夾並通過專案屬性鏈接 JAR。

### 基本使用示例
設置完成後，導入類別如 `org.joda.time.DateTime` 或 `org.joda.time.LocalDate`。以下是一些示例：
- 創建當前日期時間：`DateTime now = new DateTime();`
- 訪問字段：`int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- 修改：`DateTime future = now.plusDays(5);`

### 高級功能
Joda-Time 支持時區（例如，`DateTimeZone.forID("America/New_York")`）和不同的日曆系統（例如，Coptic 通過 `CopticChronology.getInstance()`）。它還處理間隔和持續時間，例如 `Interval interval = new Interval(startDt, endDt);`。

一個意外的細節是，Joda-Time 被認為是一個 "完成" 的項目，建議新專案使用 Java 8 的 `java.time` 包，但它對於舊系統或特定需求仍然相關。

---

### 調查筆記：使用 `org.joda.time` 的全面指南

本節提供了對使用 `org.joda.time` 庫的詳細探討，擴展了直接答案，並提供了更多的上下文和技術深度，適合尋求全面理解的開發人員。它包括設置、使用示例、關鍵功能和進一步的資源，確保實施的完整參考。

#### Joda-Time 簡介
Joda-Time，由 joda.org 开發，是一個廣泛使用的日期和時間處理庫，特別是在 Java 8 發布之前。它解決了 Java `Date` 和 `Calendar` 類的設計問題，例如線程安全問題，通過使用不可變類。在 Java 8 之前，`Date` 類和 `SimpleDateFormatter` 不是線程安全的，操作如日/月/年偏移量不直觀（例如，日從 0 開始，月從 1 開始，需要 `Calendar`）。Joda-Time 提供了一個乾淨、流暢的 API，並支持八種日曆系統，而 Java 只支持兩種（格里曆和日本皇家）。在 Java 8 之後，作者認為 Joda-Time 幾乎完成，建議將新專案遷移到 `java.time`（JSR-310），但它對於舊系統或特定用例仍然相關。

#### 設置 Joda-Time
要使用 Joda-Time，必須首先將其包含在 Java 專案中。截至 2025 年 3 月 3 日，最新版本是 2.13.1，確保穩定性和與 JDK 1.5 或更高版本的兼容性。對於 Maven 用戶，將以下依賴項添加到 `pom.xml`：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
這可以在 [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) 找到。對於非 Maven 專案，從 [這個網站](https://www.joda.org/joda-time/download.html) 下載 `.tar.gz` 文件，解壓縮它，並將 `joda-time-2.13.1.jar` 添加到專案的類路徑。例如，在 Eclipse 中，創建一個 "libs" 資料夾，複製 JAR，並通過屬性 -> Java 構建路徑 -> 圖書館 -> 添加 JAR 鏈接它。使用 `DateTime test = new DateTime();` 測試設置以確保功能。

#### 基本使用和示例
包含後，從 `org.joda.time` 導入類別，例如 `DateTime`、`LocalDate`、`LocalTime` 和 `LocalDateTime`，所有這些類別都是不可變的以確保線程安全。以下是詳細示例：

- **創建日期時間對象：**
  - 從當前時間：`DateTime now = new DateTime();` 使用默認時區和 ISO 日曆。
  - 從 Java `Date`：`java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` 以實現互操作性。
  - 從特定值：構造函數接受 `Long`（毫秒）、`String`（ISO8601）或其他 Joda-Time 對象，例如 `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`。

- **訪問字段：**
  - 使用 getter 方法：`int year = now.getYear(); int month = now.getMonthOfYear();` 其中一月是 1，十二月是 12。
  - 文本表示：`String dayName = now.dayOfWeek().getAsText();` 例如，輸出 "星期一" 2025 年 3 月 3 日。
  - 檢查屬性：`boolean isLeap = now.year().isLeap();` 返回 `false` 2025 年。

- **修改日期時間：**
  - 創建具有修改的新實例：`DateTime newDt = now.withYear(2025);` 或 `DateTime future = now.plusDays(5);`。
  - 添加持續時間：`DateTime later = now.plusHours(2);` 以添加兩小時，返回新實例。

GeeksforGeeks 的實際示例說明了使用：
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("當前日：" + now.dayOfWeek().getAsText());
        System.out.println("當前月：" + now.monthOfYear().getAsText());
        System.out.println("當前年：" + now.year().getAsText());
        System.out.println("當前年是閏年：" + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
對於 2025 年 3 月 3 日，輸出可能包括 "當前日：星期一"、"當前月：三月"、"當前年：2025"、"當前年是閏年：false" 和時間戳如 "2025-03-03T08:39:00.000"。

#### 關鍵功能和高級使用
Joda-Time 提供了強大的功能來處理複雜的日期時間操作，詳細如下：

- **時區：**
  - 通過 `DateTimeZone` 管理，支持命名區（例如，"Asia/Tokyo"）和固定偏移量。示例：
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - 默認區與 JDK 的相同，但可以通過 `DateTimeZone.setDefault(zone);` 覆蓋。時區數據每年手動更新幾次，基於 [global-tz](https://github.com/JodaOrg/global-tz)。

- **日曆系統：**
  - 支持七種系統：佛教、科普特、埃塞俄比亞、格里曆、格里曆儒略、伊斯蘭、儒略，並且有條件支持自定義系統。示例：
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - 默認 ISO 日曆，歷史上在 1583 年之前不準確，但適用於現代民用。

- **間隔、持續時間和期間：**
  - `Interval`：表示時間範圍，半開放（開始包含，結束不包含），例如 `Interval interval = new Interval(startDt, endDt);`。
  - `Duration`：毫秒的精確時間，例如 `Duration duration = new Duration(interval);`，用於添加到瞬間。
  - `Period`：以字段（年、月、日等）定義，毫秒不精確，例如 `Period period = new Period(startDt, endDt);`。示例差異：在夏令時間（例如 2005 年 3 月 26 日 12:00:00）添加 1 天，`plus(Period.days(1))` 添加 23 小時，而 `plus(new Duration(24L*60L*60L*1000L))` 添加 24 小時，突出了期間與持續時間的行為。

快速啟動指南提供了一個總結主類別和用例的表：
| **方面**                  | **詳細信息**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **主要日期時間類**         | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 類，所有不可變)               |
| **Instant 用例**           | 事件的時間戳，無日曆系統或時區                                                             |
| **LocalDate 用例**         | 出生日期，無時間需要                                                                      |
| **LocalTime 用例**         | 當天的時間，例如商店開/關，無日期                                                           |
| **DateTime 用例**          | 通用用途，替換 JDK 日曆，包括時區信息                                                           |
| **構造函數類型**           | 對象構造函數接受：Date, Calendar, String (ISO8601), Long (毫秒), Joda-Time 類別 |
| **示例轉換**               | `java.util.Date` 到 `DateTime`：`DateTime dt = new DateTime(new Date());`                      |
| **字段訪問方法**           | `getMonthOfYear()` (1=一月，12=十二月)，`getYear()`                                        |
| **修改方法**               | `withYear(2000)`，`plusHours(2)`                                                               |
| **屬性方法示例**           | `monthOfYear().getAsText()`，`monthOfYear().getAsShortText(Locale.FRENCH)`，`year().isLeap()`，`dayOfMonth().roundFloorCopy()` |
| **默認日曆系統**           | ISO 日曆系統（事實上的民用日曆，歷史上在 1583 年之前不準確）                              |
| **默認時區**               | 同 JDK 默認，可以覆蓋                                                                      |
| **Chronology 類**           | 支持多種日曆系統，例如 `CopticChronology.getInstance()`                                     |
| **時區示例**               | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`，`GJChronology.getInstance(zone)`      |
| **Interval 類**            | `Interval` - 保持開始和結束日期時間，基於範圍的操作                          |
| **Period 類**              | `Period` - 保持期間如 6 個月，3 天，7 小時，可以從間隔派生               |
| **Duration 類**            | `Duration` - 精確的毫秒持續時間，可以從間隔派生                          |
| **期間與持續時間示例**     | 在夏令時間（2005 年 3 月 26 日 12:00:00）添加 1 天：`plus(Period.days(1))` 添加 23 小時，`plus(new Duration(24L*60L*60L*1000L))` 添加 24 小時 |

一個有趣的細節是對象構造函數的可擴展性，允許通過直接傳遞它們來轉換 JDK `Date` 或 `Calendar`，簡化了從舊代碼的遷移。

#### 進一步學習和資源
要進行更深入的探索，請參考 [Joda-Time 用戶指南](https://www.joda.org/joda-time/userguide.html)，涵蓋了高級主題如格式化和解析。快速啟動指南 [Joda-Time 快速啟動](https://www.joda.org/joda-time/quickstart.html) 提供了一個簡潔的介紹。其他教程可在 [Baeldung Joda-Time](https://www.baeldung.com/joda-time) 和 [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) 找到，並附有代碼示例和設置說明。API 文檔 [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) 適用於參考，但更技術。

#### 結論
Joda-Time 提供了一個強大、線程安全的日期和時間操作替代方案，並對時區、日曆系統和時間計算提供了廣泛支持。雖然在 Java 8 之後被認為是完成的，但它對於舊系統仍然有價值，設置通過 Maven 或手動 JAR 包含，並通過不可變類如 `DateTime` 和 `LocalDate` 使用。本指南確保開發人員具備實施所需的所有信息，從基本示例到高級功能，並由全面的資源支持。