---
audio: false
generated: true
lang: zh
layout: post
title: 日期和时间操作
translated: true
---

### 关键要点
- 使用 `org.joda.time` 似乎需要将其添加到 Java 项目中，并导入其类以进行日期和时间操作。
- 研究表明，可以通过 Maven 使用版本 2.13.1 来包含该库，或者下载 JAR 文件，然后使用类如 `DateTime` 和 `LocalDate`。
- 证据表明，Joda-Time 对于处理时区、日历系统和时间间隔非常有用，例如创建日期对象并修改它们。

### Joda-Time 是什么以及如何设置
Joda-Time 是一个用于在 Java 中处理日期和时间的库，特别是在 Java 8 之前非常有用，提供了一个直观的 API 来替代旧的、不太安全的 `Date` 和 `Calendar` 类。要使用它，首先将库包含在项目中。如果使用 Maven，将以下依赖项添加到 `pom.xml` 中：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
或者，从 [这个网站](https://www.joda.org/joda-time/download.html) 下载 JAR 文件，并将其添加到项目的类路径中，例如在 Eclipse 中创建一个 "libs" 文件夹并通过项目属性链接 JAR。

### 基本使用示例
设置好后，导入类如 `org.joda.time.DateTime` 或 `org.joda.time.LocalDate`。以下是一些示例：
- 创建当前日期时间：`DateTime now = new DateTime();`
- 访问字段：`int year = now.getYear(); String monthName = now.monthOfYear().getAsText();`
- 修改：`DateTime future = now.plusDays(5);`

### 高级功能
Joda-Time 支持时区（例如，`DateTimeZone.forID("America/New_York")`）和不同的日历系统（例如，通过 `CopticChronology.getInstance()` 使用科普特日历）。它还处理间隔和持续时间，例如 `Interval interval = new Interval(startDt, endDt);`。

一个意外的细节是，Joda-Time 被认为是一个“完成”的项目，建议新项目使用 Java 8 的 `java.time` 包，但它对于遗留系统或特定需求仍然相关。

---

### 问卷说明：使用 `org.joda.time` 的全面指南

本节提供了对使用 `org.joda.time` 库的详细探讨，扩展了直接答案，提供了更多的上下文和技术深度，适合寻求全面理解的开发人员。它包括设置、使用示例、关键功能和进一步的资源，确保实现的完整参考。

#### Joda-Time 简介
Joda-Time，由 joda.org 开发，是一个广泛使用的日期和时间处理库，特别是在 Java 8 发布之前。它解决了 Java `Date` 和 `Calendar` 类的设计问题，例如线程安全问题，通过使用不可变类。在 Java 8 之前，`Date` 类和 `SimpleDateFormatter` 不是线程安全的，操作如天/月/年偏移量不直观（例如，天从 0 开始，月从 1 开始，需要 `Calendar`）。Joda-Time 提供了一个干净、流畅的 API，并支持八种日历系统，而 Java 只支持两种（格里高利和日本皇家）。在 Java 8 之后，作者认为 Joda-Time 基本完成，建议将新项目迁移到 `java.time`（JSR-310），但它对于遗留系统或特定用例仍然相关。

#### 设置 Joda-Time
要使用 Joda-Time，必须首先将其包含在 Java 项目中。截至 2025 年 3 月 3 日，最新版本是 2.13.1，确保稳定性和与 JDK 1.5 或更高版本的兼容性。对于 Maven 用户，将以下依赖项添加到 `pom.xml` 中：
```xml
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.13.1</version>
</dependency>
```
这可以在 [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time) 上找到。对于非 Maven 项目，从 [这个网站](https://www.joda.org/joda-time/download.html) 下载 `.tar.gz` 文件，解压缩它，并将 `joda-time-2.13.1.jar` 添加到项目的类路径。例如，在 Eclipse 中，创建一个 "libs" 文件夹，复制 JAR，并通过 Properties -> Java Build Path -> Libraries -> Add Jars 链接它。使用 `DateTime test = new DateTime();` 测试设置，以确保功能。

#### 基本使用和示例
包含后，导入 `org.joda.time` 的类，例如 `DateTime`、`LocalDate`、`LocalTime` 和 `LocalDateTime`，所有这些类都是不可变的，以确保线程安全。以下是详细示例：

- **创建日期时间对象：**
  - 从当前时间：`DateTime now = new DateTime();` 使用默认时区和 ISO 日历。
  - 从 Java `Date`：`java.util.Date juDate = new Date(); DateTime dt = new DateTime(juDate);` 以实现互操作性。
  - 从特定值：构造函数接受 `Long`（毫秒）、`String`（ISO8601）或其他 Joda-Time 对象，例如 `DateTime dt = new DateTime(2025, 3, 3, 8, 39);`。

- **访问字段：**
  - 使用 getter 方法：`int year = now.getYear(); int month = now.getMonthOfYear();` 其中一月是 1，十二月是 12。
  - 文本表示：`String dayName = now.dayOfWeek().getAsText();` 输出例如 2025 年 3 月 3 日的 "星期一"。
  - 检查属性：`boolean isLeap = now.year().isLeap();` 返回 2025 年的 `false`。

- **修改日期时间：**
  - 创建带有修改的新实例：`DateTime newDt = now.withYear(2025);` 或 `DateTime future = now.plusDays(5);`。
  - 添加持续时间：`DateTime later = now.plusHours(2);` 为添加两小时，返回新实例。

一个来自 GeeksforGeeks 的实际示例说明了使用：
```java
import org.joda.time.DateTime;
import org.joda.time.LocalDateTime;
public class JodaTime {
    public static void main(String[] args) {
        DateTime now = new DateTime();
        System.out.println("当前日： " + now.dayOfWeek().getAsText());
        System.out.println("当前月： " + now.monthOfYear().getAsText());
        System.out.println("当前年： " + now.year().getAsText());
        System.out.println("当前年是闰年： " + now.year().isLeap());
        LocalDateTime dt = LocalDateTime.now();
        System.out.println(dt);
    }
}
```
对于 2025 年 3 月 3 日，输出可能包括 "当前日： 星期一"、"当前月： 三月"、"当前年： 2025"、"当前年是闰年： false" 和一个时间戳，例如 "2025-03-03T08:39:00.000"。

#### 关键功能和高级使用
Joda-Time 提供了用于复杂日期时间操作的强大功能，详细说明如下：

- **时区：**
  - 通过 `DateTimeZone` 管理，支持命名区（例如 "Asia/Tokyo"）和固定偏移量。示例：
    ```java
    DateTimeZone zone = DateTimeZone.forID("America/New_York");
    DateTime nyTime = new DateTime(zone);
    ```
  - 默认区与 JDK 的相同，但可以通过 `DateTimeZone.setDefault(zone);` 覆盖。时区数据每年手动更新几次，基于 [global-tz](https://github.com/JodaOrg/global-tz)。

- **日历系统：**
  - 支持七种系统：佛教、科普特、埃塞俄比亚、格里高利、格里高利-儒略、伊斯兰、儒略，并提供自定义系统的条款。示例：
    ```java
    Chronology coptic = CopticChronology.getInstance();
    LocalDate copticDate = new LocalDate(coptic);
    ```
  - 默认为 ISO 日历，在 1583 年之前历史上不准确，但适用于现代民用。

- **间隔、持续时间和周期：**
  - `Interval`：表示时间范围，半开（开始包含，结束不包含），例如 `Interval interval = new Interval(startDt, endDt);`。
  - `Duration`：精确时间（毫秒），例如 `Duration duration = new Duration(interval);`，用于添加到瞬时。
  - `Period`：以字段定义（年、月、日等），毫秒不精确，例如 `Period period = new Period(startDt, endDt);`。示例差异：在夏令时（例如 2005 年 3 月 26 日 12:00:00）添加 1 天，`plus(Period.days(1))` 添加 23 小时，而 `plus(new Duration(24L*60L*60L*1000L))` 添加 24 小时，突出了周期与持续时间的行为。

快速入门指南提供了一个总结表，列出了主要类和用例：
| **方面**                  | **详细信息**                                                                                     |
|-----------------------------|-------------------------------------------------------------------------------------------------|
| **主要日期时间类**         | Instant, DateTime, LocalDate, LocalTime, LocalDateTime (5 个类，所有不可变)               |
| **Instant 用例**           | 事件的时间戳，没有日历系统或时区                                                         |
| **LocalDate 用例**         | 出生日期，不需要时间                                                                      |
| **LocalTime 用例**         | 一天中的时间，例如商店开/关，没有日期                                                     |
| **DateTime 用例**          | 通用用途，替代 JDK Calendar，包括时区信息                                               |
| **构造函数类型**           | 对象构造函数接受：Date, Calendar, String (ISO8601), Long (毫秒), Joda-Time 类               |
| **示例转换**               | `java.util.Date` 到 `DateTime`：`DateTime dt = new DateTime(new Date());`                      |
| **字段访问方法**           | `getMonthOfYear()` (1=一月，12=十二月)，`getYear()`                                        |
| **修改方法**               | `withYear(2000)`, `plusHours(2)`                                                               |
| **属性方法示例**           | `monthOfYear().getAsText()`, `monthOfYear().getAsShortText(Locale.FRENCH)`, `year().isLeap()`, `dayOfMonth().roundFloorCopy()` |
| **默认日历系统**           | ISO 日历系统（现代民用日历，在 1583 年之前历史上不准确）                                      |
| **默认时区**               | 与 JDK 默认相同，可以覆盖                                                         |
| **Chronology 类**           | 支持多种日历系统，例如 `CopticChronology.getInstance()`                                     |
| **时区示例**               | `DateTimeZone zone = DateTimeZone.forID("Asia/Tokyo");`, `GJChronology.getInstance(zone)`      |
| **Interval 类**            | `Interval` - 保存开始和结束日期时间，基于范围的操作                          |
| **Period 类**              | `Period` - 保存周期，例如 6 个月，3 天，7 小时，可以从间隔派生               |
| **Duration 类**            | `Duration` - 精确持续时间（毫秒），可以从间隔派生                          |
| **Period vs Duration 示例** | 在夏令时（2005 年 3 月 26 日 12:00:00）添加 1 天：`plus(Period.days(1))` 添加 23 小时，`plus(new Duration(24L*60L*60L*1000L))` 添加 24 小时 |

一个有趣的细节是对象构造函数的可扩展性，允许通过直接传递它们来从 JDK `Date` 或 `Calendar` 转换，简化了从遗留代码的迁移。

#### 进一步学习和资源
要进行更深入的探索，请参考 [Joda-Time 用户指南](https://www.joda.org/joda-time/userguide.html)，涵盖了格式化和解析等高级主题。快速入门指南 [Joda-Time 快速入门](https://www.joda.org/joda-time/quickstart.html) 提供了简洁的介绍。其他教程可在 [Baeldung Joda-Time](https://www.baeldung.com/joda-time) 和 [GeeksforGeeks Joda-Time](https://www.geeksforgeeks.org/joda-time/) 上找到，提供代码示例和设置说明。API 文档 [Joda-Time API Docs](https://www.joda.org/joda-time/apidocs/index.html) 对于参考非常有用，尽管更技术性。

#### 结论
Joda-Time 提供了一个强大、线程安全的日期和时间操作替代方案，具有对时区、日历系统和时间计算的广泛支持。虽然在 Java 8 之后被认为是完成的，但它对于遗留系统仍然有价值，可以通过 Maven 或手动 JAR 包含，并通过不可变类如 `DateTime` 和 `LocalDate` 使用。本指南确保开发人员在实现中拥有所有必要的信息，从基本示例到高级功能，并由全面的资源支持。

### 关键引用
- [Joda-Time 主页与一般信息](https://www.joda.org/joda-time/)
- [Joda-Time 快速入门指南](https://www.joda.org/joda-time/quickstart.html)
- [Baeldung 关于 Joda-Time 使用的教程](https://www.baeldung.com/joda-time)
- [GeeksforGeeks 关于 Joda-Time 的文章](https://www.geeksforgeeks.org/joda-time/)
- [Joda-Time 用户指南](https://www.joda.org/joda-time/userguide.html)
- [Joda-Time 下载和安装页面](https://www.joda.org/joda-time/download.html)
- [Maven Repository](https://mvnrepository.com/artifact/joda-time/joda-time)
- [Joda-Time API 文档](https://www.joda.org/joda-time/apidocs/index.html)