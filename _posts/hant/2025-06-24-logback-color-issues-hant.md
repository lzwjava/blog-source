---
audio: false
generated: true
lang: hant
layout: post
title: 為何 Logback 輸出在 Gnome 終端機中可能缺少色彩
translated: true
type: note
---

你提出了一個很好的問題，這涉及到終端機、日誌庫和作業系統如何與彩色輸出互動！

你的 Logback 輸出在 Gnome Terminal 中可能沒有顏色（即使使用了 `%highlight`），而 Spring Boot 的預設輸出卻有顏色，這背後有幾個原因：

1.  **ANSI 跳脫序列：** 終端機的彩色輸出是通過列印特殊的字元序列（稱為 **ANSI 跳脫序列**）來實現的。這些序列告訴終端機模擬器（如 Gnome Terminal）改變前景色、背景色、重置顏色等等。
      * 例如，`\u001B[31m` 可能會將文字顏色設為紅色，而 `\u001B[0m` 則重置顏色。
2.  **Logback 的 `%highlight` 轉換器：** Logback 的 `%highlight` 轉換器（以及其他如 `%red`、`%green` 等轉換器）內部會產生這些 ANSI 跳脫序列。所以，你的 `logback.xml` 確實配置了產生彩色輸出。
3.  **終端機模擬器與 ANSI 支援：** 大多數現代 Linux 終端機（包括 Gnome Terminal）預設都支援 ANSI 跳脫序列。在 Linux 上，這通常不是問題。
4.  **Spring Boot 的預設配置：** Spring Boot 提供了一個非常固執己見且通常增強過的 Logback 預設配置。這個預設配置做了幾件事：
      * 它使用帶有 `%highlight` 和其他顏色轉換器的 `PatternLayout`。
      * **關鍵在於，對於 Windows 使用者，它通常包含了 `jansi` 函式庫。** Logback 本身有一個 `withJansi` 屬性，你可以在 `ConsoleAppender` 上設定。在 Windows 上，命令提示字元（CMD.exe）本身不解析 ANSI 跳脫序列。`jansi` 函式庫（Java ANSI 支援）充當一個適配器，攔截 ANSI 代碼並將其轉換為 Windows 可以理解的特定控制台命令。雖然 Linux 終端機通常*不需要* Jansi 來提供基本的 ANSI 支援，但有時它的存在與否會影響 Logback 檢測「終端機能力」的方式或它刷新輸出的方式，儘管在 Linux 上這種情況較少見。
      * Spring Boot 的預設設定可能還包含額外的邏輯或屬性，以確保顏色能一致地呈現。

**為什麼你的自訂 `logback.xml` 在 Gnome Terminal 中可能沒有顯示顏色：**

既然你使用了 `%highlight`，那麼 ANSI 代碼*應該*存在。如果它們沒有出現，請考慮以下可能性：

1.  **你的 `logback.xml` 真的被載入了嗎？**
      * 再次檢查它的位置：它應該位於 `src/main/resources/logback.xml`（或者使用 `logback-spring.xml`，如果你希望 Spring Boot 先應用其預設值*然後再*套用你的自訂設定）。
      * 查看你應用程式的啟動日誌。Logback 通常會列印訊息，指示它正在載入哪個配置檔案。如果你看到關於 `BasicConfigurator` 或不同檔案的消息，那麼你的 `logback.xml` 沒有被使用。
2.  **重新導向輸出：** 你是否重新導向了應用程式的輸出？
      * 如果你將應用程式的輸出管道傳輸到檔案（`java -jar your-app.jar > log.txt`）或其他命令，終端機模擬器將不會解析 ANSI 代碼，你只會在檔案中看到原始的跳脫序列。
      * 某些工具或環境可能會剝離 ANSI 代碼，假設輸出不是發送到「真正的」終端機。
3.  **終端機類型檢測：** Logback 的 `ConsoleAppender` 及其高亮邏輯通常會嘗試檢測輸出目標是否為「真正的」終端機（TTY）。如果沒有被檢測為 TTY（例如，在某些沒有完全模擬 TTY 的 IDE 控制台中執行，或者輸出被管道傳輸），Logback 可能會自動抑制 ANSI 代碼，以避免混亂非顏色感知的輸出。
      * Gnome Terminal 通常被檢測為 TTY，所以這不太可能是主要原因，但值得注意。
4.  **使用 `withJansi` 實現跨平台一致性（與 Linux 較不相關，但了解有益）：** 雖然 Jansi 主要用於 Windows，但有時在你的 `logback.xml` 中的 `ConsoleAppender` 內明確設定 `<withJansi>true</withJansi>` 可以幫助確保跨平台行為的一致性，即使在嚴格來說不需要它的 Linux 上。這通常沒有壞處。
5.  **環境變數：** 極少數情況下，某些環境變數（例如 `TERM` 或 `CLICOLOR_FORCE`）會影響終端機或應用程式處理彩色輸出的方式。然而，對於標準的 Gnome Terminal，這不太可能是導致*完全沒有*顏色的原因。

**要進行故障排除並確保顏色顯示：**

1.  **驗證 `logback.xml` 已載入：** 啟動你的應用程式，並尋找 Logback 的自我配置訊息。它們會告訴你正在使用哪個配置檔案。
      * 你也可以在 `logback.xml` 中的 `<configuration>` 標籤添加 `debug="true"`，以在啟動時獲得更多詳細的 Logback 內部狀態訊息：
        ```xml
        <configuration debug="true">
            </configuration>
        ```
2.  **使用原始的 ANSI 代碼測試一個簡單的 Java 應用程式：**
    ```java
    public class AnsiTest {
        public static void main(String[] args) {
            System.out.println("\u001B[31m這行文字是紅色的。\u001B[0m");
            System.out.println("\u001B[32m這行文字是綠色的。\u001B[0m");
            System.out.println("這行文字是預設顏色。");
        }
    }
    ```
    在你的 Gnome Terminal 中編譯並執行這個程式（`javac AnsiTest.java && java AnsiTest`）。如果這顯示了顏色，那麼你的終端機本身是具備能力的，問題很可能出在你的 Logback 配置或它的執行方式上。如果這*沒有*顯示顏色，那麼你的 Gnome Terminal 設定存在更根本的問題（儘管可能性極低）。
3.  **將你的 `logback.xml` 與 Spring Boot 的預設配置進行比較：**
      * 如果你使用 Spring Boot，通常可以在 Spring Boot JAR 檔案或文件中找到其預設的 `logback-spring.xml`（或類似檔案）。比較 `ConsoleAppender` 部分可能會發現細微的差異。
      * Spring Boot 通常使用類似這樣的模式：
        `%d{${LOG_DATEFORMAT_PATTERN:-yyyy-MM-dd HH:mm:ss.SSS}} %highlight(${LOG_LEVEL_PATTERN:-%-5p}) ${PID:- } --- [%thread] %logger{40}.%M{1.}: %msg%n%throwable`
        注意使用了系統屬性（`LOG_DATEFORMAT_PATTERN`、`LOG_LEVEL_PATTERN`、`PID`），這些是 Spring Boot 為你設定的。

通過這些步驟，你應該能夠找出為什麼你的自訂 Logback 配置沒有在 Gnome Terminal 中產生彩色輸出。最常見的原因是 `logback.xml` 沒有被載入，或者存在輸出重新導向的問題。