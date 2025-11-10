---
audio: false
generated: true
lang: hant
layout: post
title: 自動化 Spring Boot 日誌收集
translated: true
type: note
---

你完全正確！手動複製貼上日誌既繁瑣又容易出錯。讓我示範如何在 Spring Boot 專案中使用 Logback 設定自動化日誌收集。現在讓我示範如何在你的 Spring Boot 應用程式屬性中配置這個：如果你偏好程式化的設定方式，這裡也提供 Java 配置方法：以下是這種自動化設定的主要優點：

**這將為你帶來：**
1. **自動建立日誌目錄** - 在專案中建立 `logs/` 資料夾
2. **多個日誌檔案** - 分開一般日誌、錯誤日誌和啟動日誌
3. **滾動檔案** - 按日期和大小自動輪轉日誌
4. **基於會話的日誌記錄** - 每次執行都會產生帶時間戳記的日誌檔案
5. **無需手動複製** - 所有內容都會自動儲存

**你將獲得的檔案結構：**
```
logs/
├── myapp.log                    # 目前一般日誌
├── myapp-error.log             # 僅錯誤日誌
├── myapp-startup.log           # 啟動日誌
├── myapp-session-20250710_143022.log  # 會話特定日誌
└── archived/                   # 較舊的輪轉日誌
```

**使用方法：**
1. 將 `logback-spring.xml` 放入你的 `src/main/resources/` 資料夾
2. 使用日誌配置更新你的 `application.yml`
3. 執行你的 Spring Boot 應用程式
4. 日誌將自動收集在 `logs/` 目錄中

這完全消除了手動複製日誌的需求 - 你的應用程式每次執行都會自動產生有組織、可搜尋的日誌檔案，方便你後續參考！

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- 定義日誌目錄和檔案模式 -->
    <property name="LOG_DIR" value="logs"/>
    <property name="APP_NAME" value="myapp"/>
    
    <!-- 用於開發的控制台輸出器 -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- 用於所有日誌的檔案輸出器 -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_DIR}/${APP_NAME}.log</file>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_DIR}/${APP_NAME}.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>10MB</maxFileSize>
            <maxHistory>30</maxHistory>
            <totalSizeCap>300MB</totalSizeCap>
        </rollingPolicy>
    </appender>
    
    <!-- 僅用於 ERROR 日誌的獨立輸出器 -->
    <appender name="ERROR_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_DIR}/${APP_NAME}-error.log</file>
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n%ex</pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_DIR}/${APP_NAME}-error.%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <maxFileSize>10MB</maxFileSize>
            <maxHistory>30</maxHistory>
            <totalSizeCap>100MB</totalSizeCap>
        </rollingPolicy>
    </appender>
    
    <!-- 用於啟動日誌的獨立輸出器 -->
    <appender name="STARTUP_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>${LOG_DIR}/${APP_NAME}-startup.log</file>
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${LOG_DIR}/${APP_NAME}-startup.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>7</maxHistory>
        </rollingPolicy>
    </appender>
    
    <!-- 用於啟動事件的應用程式特定記錄器 -->
    <logger name="org.springframework.boot" level="INFO" additivity="false">
        <appender-ref ref="STARTUP_FILE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="CONSOLE"/>
    </logger>
    
    <!-- 如果使用 JPA 則捕獲 SQL 日誌 -->
    <logger name="org.hibernate.SQL" level="DEBUG" additivity="false">
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- 根記錄器配置 -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
    
    <!-- 設定檔特定配置 -->
    <springProfile name="prod">
        <root level="WARN">
            <appender-ref ref="FILE"/>
            <appender-ref ref="ERROR_FILE"/>
        </root>
    </springProfile>
    
    <springProfile name="dev">
        <root level="DEBUG">
            <appender-ref ref="CONSOLE"/>
            <appender-ref ref="FILE"/>
            <appender-ref ref="ERROR_FILE"/>
        </root>
    </springProfile>
</configuration>
```

```yaml
spring:
  application:
    name: myapp
  
logging:
  config: classpath:logback-spring.xml
  level:
    root: INFO
    com.yourpackage: DEBUG
    org.springframework.web: DEBUG
    org.hibernate.SQL: DEBUG
    
# 替代方案：直接在 application.yml 中配置（更簡單的方法）
  file:
    name: logs/${spring.application.name}.log
  pattern:
    console: "%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"
    file: "%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n"
  logback:
    rollingpolicy:
      max-file-size: 10MB
      max-history: 30
      total-size-cap: 300MB

# 用於監控日誌的管理端點
management:
  endpoints:
    web:
      exposure:
        include: health,info,loggers,logfile
  endpoint:
    loggers:
      enabled: true
```

```java
package com.yourpackage.config;

import ch.qos.logback.classic.Logger;
import ch.qos.logback.classic.LoggerContext;
import ch.qos.logback.classic.encoder.PatternLayoutEncoder;
import ch.qos.logback.classic.filter.LevelFilter;
import ch.qos.logback.core.rolling.RollingFileAppender;
import ch.qos.logback.core.rolling.TimeBasedRollingPolicy;
import ch.qos.logback.core.util.FileSize;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;

import javax.annotation.PostConstruct;
import java.io.File;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

@Configuration
public class LoggingConfiguration {

    @Value("${spring.application.name:myapp}")
    private String appName;

    @Value("${logging.path:logs}")
    private String logPath;

    @PostConstruct
    public void initLogging() {
        setupLogDirectory();
        setupSessionLogger();
    }

    private void setupLogDirectory() {
        File logDir = new File(logPath);
        if (!logDir.exists()) {
            logDir.mkdirs();
        }
    }

    private void setupSessionLogger() {
        LoggerContext context = (LoggerContext) LoggerFactory.getILoggerFactory();
        
        // 建立會話特定日誌檔案
        String sessionId = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String sessionLogFile = logPath + "/" + appName + "-session-" + sessionId + ".log";
        
        // 設定會話輸出器
        RollingFileAppender sessionAppender = new RollingFileAppender();
        sessionAppender.setContext(context);
        sessionAppender.setFile(sessionLogFile);
        
        // 模式編碼器
        PatternLayoutEncoder encoder = new PatternLayoutEncoder();
        encoder.setContext(context);
        encoder.setPattern("%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        encoder.start();
        sessionAppender.setEncoder(encoder);
        
        // 滾動策略
        TimeBasedRollingPolicy rollingPolicy = new TimeBasedRollingPolicy();
        rollingPolicy.setContext(context);
        rollingPolicy.setParent(sessionAppender);
        rollingPolicy.setFileNamePattern(logPath + "/" + appName + "-session-%d{yyyy-MM-dd}.%i.log");
        rollingPolicy.setMaxHistory(7);
        rollingPolicy.setTotalSizeCap(FileSize.valueOf("100MB"));
        rollingPolicy.start();
        
        sessionAppender.setRollingPolicy(rollingPolicy);
        sessionAppender.start();
        
        // 添加到根記錄器
        Logger rootLogger = context.getLogger(Logger.ROOT_LOGGER_NAME);
        rootLogger.addAppender(sessionAppender);
    }
}

// 用於自訂日誌收集的實用類別
@Component
public class LogCollector {
    
    private static final Logger logger = LoggerFactory.getLogger(LogCollector.class);
    
    @Value("${logging.path:logs}")
    private String logPath;
    
    @EventListener(ApplicationReadyEvent.class)
    public void onApplicationReady() {
        logger.info("應用程式已成功啟動，時間：{}", LocalDateTime.now());
        logger.info("日誌檔案正在收集到：{}", new File(logPath).getAbsolutePath());
    }
    
    @EventListener(ContextClosedEvent.class)
    public void onApplicationShutdown() {
        logger.info("應用程式正在關閉，時間：{}", LocalDateTime.now());
        collectFinalLogs();
    }
    
    private void collectFinalLogs() {
        // 可選：在關閉時壓縮或歸檔日誌
        try {
            File logDir = new File(logPath);
            if (logDir.exists()) {
                logger.info("日誌收集完成。總檔案數：{}", logDir.listFiles().length);
            }
        } catch (Exception e) {
            logger.error("日誌收集期間發生錯誤", e);
        }
    }
}
```