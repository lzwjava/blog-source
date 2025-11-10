---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Log4j 配置指南
translated: true
type: note
---

### Log4j 配置概述
Log4j 是一個流行的 Java 日誌記錄框架，可讓您控制日誌輸出級別和目的地。對於 2.x 版本（推薦），配置通常定義在 XML、JSON、YAML 或 Properties 檔案中（例如 `log4j2.xml`）。此設定涉及：

- **Loggers**：定義特定類別或套件的日誌訊息級別（例如 DEBUG、INFO、WARN、ERROR）。
- **Appenders**：指定日誌發送的位置，例如控制台（標準輸出）或檔案（具有輪轉等選項）。
- **Root Logger**：一個預設的 logger，適用於所有未被特定 logger 覆蓋的類別。

要配置控制台和檔案日誌記錄，通常需要添加 `ConsoleAppender` 和 `RollingFileAppender`（用於具有自動輪轉的檔案日誌）。將配置檔案放在您的 classpath 中（例如 Maven 專案中的 `src/main/resources`）。

如果您正在使用 Log4j 1.x，請升級到 2.x — 它速度更快且功能更佳。以下是一個帶有範例 XML 配置的逐步指南。

### 配置檔案和控制台記錄器的步驟
1. **添加依賴項**：確保 Log4j 2.x 在您的 pom.xml（Maven）或 build.gradle（Gradle）中。Maven 範例：
   ```
   <dependency>
       <groupId>org.apache.logging.log4j</groupId>
       <artifactId>log4j-core</artifactId>
       <version>2.23.1</version>  <!-- 使用最新版本 -->
   </dependency>
   <dependency>
       <groupId>org.apache.logging.log4j</groupId>
       <artifactId>log4j-api</artifactId>
       <version>2.23.1</version>
   </dependency>
   ```

2. **創建配置檔案**：在您的資源資料夾中創建 `log4j2.xml`。

3. **定義 Appenders**：
   - ConsoleAppender：輸出到終端/控制台。
   - RollingFileAppender：寫入檔案並根據大小進行輪轉（例如，當達到 10MB 時，創建新檔案）。

4. **配置 Loggers**：設定日誌記錄級別（例如 INFO）並分配 appenders。Root logger 處理全域日誌記錄。

5. **在代碼中使用**：在您的 Java 類別中，像這樣獲取一個 logger：
   ```java
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   
   public class MyClass {
       private static final Logger logger = LogManager.getLogger(MyClass.class);
       // 記錄訊息：logger.debug("Debug message"); logger.info("Info message");
   }
   ```

### 範例配置 (log4j2.xml)
以下是一個用於控制台和輪轉檔案日誌記錄的完整 XML 配置。它將 INFO 及以上級別的日誌記錄到控制台，並將所有級別的日誌記錄到每日輪轉或達到 10MB 時輪轉的檔案中。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">  <!-- Log4j 內部日誌記錄級別 -->

    <!-- Appenders 部分 -->
    <Appenders>

        <!-- Console Appender -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>

        <!-- Rolling File Appender -->
        <RollingFile name="File" fileName="logs/app.log" filePattern="logs/app-%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>
            <Policies>
                <TimeBasedTriggeringPolicy />  <!-- 每日輪轉 -->
                <SizeBasedTriggeringPolicy size="10MB"/>  <!-- 或基於大小輪轉 -->
            </Policies>
            <DefaultRolloverStrategy max="7"/>  <!-- 最多保留 7 個舊檔案 -->
        </RollingFile>

    </Appenders>

    <!-- Loggers 部分 -->
    <Loggers>

        <!-- 針對您的套件的特定 logger（可選） -->
        <Logger name="com.yourapp" level="DEBUG" additivity="false">
            <AppenderRef ref="File"/>  <!-- 僅針對此套件記錄到檔案 -->
        </Logger>

        <!-- Root logger -->
        <Root level="INFO">
            <AppenderRef ref="Console"/>  <!-- Debug/info 輸出到控制台 -->
            <AppenderRef ref="File"/>     <!-- 所有級別輸出到檔案 -->
        </Root>

    </Loggers>

</Configuration>
```

- **Pattern Layout**：定義日誌格式（例如時間戳、執行緒、日誌級別、logger 名稱、訊息）。
- **Rolling Policies**：檔案基於時間（例如 `-d{yyyy-MM-dd}`）或大小進行輪轉；使用 `.gz` 壓縮。
- **Levels**：開發時設定為 `DEBUG` 以獲取詳細日誌，生產環境設定為 `INFO`（根據需要調整）。
- **Testing**：運行您的應用程式並檢查控制台輸出以及 `logs/` 資料夾中的檔案。

對於基於 Properties 的配置，請參閱 Log4j 文檔 — 它更簡單但靈活性較差。如果您需要 JSON/YAML 或版本特定的調整，請參考 [官方 Log4j 2 配置文檔](https://logging.apache.org/log4j/2.x/manual/configuration.html)。如果這與您的設定不匹配（例如 Log4j 1.x），請提供更多詳細資訊！