---
audio: false
generated: true
lang: ja
layout: post
title: Spring Bootでのログ収集の自動化
translated: true
type: note
---

おっしゃる通りです！ログを手動でコピー＆ペーストするのは面倒でエラーも発生しやすいです。Spring BootプロジェクトでLogbackを使用して自動ログ収集を設定する方法をご紹介します。

Spring Bootアプリケーションプロパティでの設定方法：

プログラムによる設定を好む場合のJava設定アプローチ：

この自動設定の主な利点：

**これにより得られるもの：**
1. **自動ログディレクトリ作成** - プロジェクト内に`logs/`フォルダを作成
2. **複数ログファイル** - 一般ログ、エラーログ、起動ログを分離
3. **ローテーション機能** - 日付とサイズに基づいてログを自動ローテーション
4. **セッションベースのロギング** - 各実行にタイムスタンプ付きログファイル
5. **手動コピー不要** - すべてが自動的に保存

**得られるファイル構造：**
```
logs/
├── myapp.log                    # 現在の一般ログ
├── myapp-error.log             # エラーログのみ
├── myapp-startup.log           # 起動ログ
├── myapp-session-20250710_143022.log  # セッション固有ログ
└── archived/                   # 古いローテーション済みログ
```

**使用方法：**
1. `logback-spring.xml`を`src/main/resources/`フォルダに配置
2. `application.yml`をロギング設定で更新
3. Spring Bootアプリケーションを実行
4. ログは自動的に`logs/`ディレクトリに収集されます

これで手動でのログコピーは完全に不要になります - アプリケーションの実行ごとに整理された検索可能なログファイルが自動生成され、後で簡単に参照できます！

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- ログディレクトリとファイルパターンの定義 -->
    <property name="LOG_DIR" value="logs"/>
    <property name="APP_NAME" value="myapp"/>
    
    <!-- 開発用コンソールアペンダー -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- 全ログ用ファイルアペンダー -->
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
    
    <!-- エラーログ専用アペンダー -->
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
    
    <!-- 起動ログ専用アペンダー -->
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
    
    <!-- 起動イベント用アプリケーション固有ロガー -->
    <logger name="org.springframework.boot" level="INFO" additivity="false">
        <appender-ref ref="STARTUP_FILE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="CONSOLE"/>
    </logger>
    
    <!-- JPA使用時のSQLログ取得 -->
    <logger name="org.hibernate.SQL" level="DEBUG" additivity="false">
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- ルートロガー設定 -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
    
    <!-- プロファイル固有設定 -->
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
    
# 代替案：application.ymlでの直接設定（シンプルなアプローチ）
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

# ログ監視用管理エンドポイント
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
        
        // セッション固有ログファイルの作成
        String sessionId = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String sessionLogFile = logPath + "/" + appName + "-session-" + sessionId + ".log";
        
        // セッションアペンダーの設定
        RollingFileAppender sessionAppender = new RollingFileAppender();
        sessionAppender.setContext(context);
        sessionAppender.setFile(sessionLogFile);
        
        // パターンエンコーダー
        PatternLayoutEncoder encoder = new PatternLayoutEncoder();
        encoder.setContext(context);
        encoder.setPattern("%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        encoder.start();
        sessionAppender.setEncoder(encoder);
        
        // ローテーションポリシー
        TimeBasedRollingPolicy rollingPolicy = new TimeBasedRollingPolicy();
        rollingPolicy.setContext(context);
        rollingPolicy.setParent(sessionAppender);
        rollingPolicy.setFileNamePattern(logPath + "/" + appName + "-session-%d{yyyy-MM-dd}.%i.log");
        rollingPolicy.setMaxHistory(7);
        rollingPolicy.setTotalSizeCap(FileSize.valueOf("100MB"));
        rollingPolicy.start();
        
        sessionAppender.setRollingPolicy(rollingPolicy);
        sessionAppender.start();
        
        // ルートロガーに追加
        Logger rootLogger = context.getLogger(Logger.ROOT_LOGGER_NAME);
        rootLogger.addAppender(sessionAppender);
    }
}

// カスタムログ収集用ユーティリティクラス
@Component
public class LogCollector {
    
    private static final Logger logger = LoggerFactory.getLogger(LogCollector.class);
    
    @Value("${logging.path:logs}")
    private String logPath;
    
    @EventListener(ApplicationReadyEvent.class)
    public void onApplicationReady() {
        logger.info("Application started successfully at {}", LocalDateTime.now());
        logger.info("Log files are being collected in: {}", new File(logPath).getAbsolutePath());
    }
    
    @EventListener(ContextClosedEvent.class)
    public void onApplicationShutdown() {
        logger.info("Application shutting down at {}", LocalDateTime.now());
        collectFinalLogs();
    }
    
    private void collectFinalLogs() {
        // オプション：シャットダウン時にログを圧縮またはアーカイブ
        try {
            File logDir = new File(logPath);
            if (logDir.exists()) {
                logger.info("Log collection completed. Total files: {}", logDir.listFiles().length);
            }
        } catch (Exception e) {
            logger.error("Error during log collection", e);
        }
    }
}
```