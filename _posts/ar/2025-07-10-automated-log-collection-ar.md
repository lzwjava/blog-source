---
audio: false
generated: true
lang: ar
layout: post
title: أتمتة جمع السجلات في سبرينغ بوت
translated: true
type: note
---

أنت محق تمامًا! النسخ اليدوي للسجلات ولصقها ممل وعرضة للأخطاء. دعني أوضح لك كيفية إعداد جمع السجلات الآلي في مشاريع Spring Boot باستخدام Logback.

الآن دعني أوضح لك كيفية تكوين هذا في خصائص تطبيق Spring Boot:

إليك أيضًا نهج التكوين باستخدام Java إذا كنت تفضل الإعداد البرمجي:

إليك الفوائد الرئيسية لهذا الإعداد الآلي:

**ما يوفره لك هذا:**
1. **إنشاء دليل السجلات تلقائيًا** - ينشئ مجلد `logs/` في مشروعك
2. **ملفات سجلات متعددة** - يفصل بين السجلات العامة، وسجلات الأخطاء، وسجلات بدء التشغيل
3. **ملفات متداولة** - يقوم بتدوير السجلات تلقائيًا حسب التاريخ والحجم
4. **التسجيل حسب الجلسة** - كل تشغيل يحصل على ملفات سجلات ذات طابع زمني
5. **لا حاجة للنسخ اليدوي** - كل شيء يتم حفظه تلقائيًا

**هيكل الملفات الذي ستحصل عليه:**
```
logs/
├── myapp.log                    # السجل العام الحالي
├── myapp-error.log             # سجلات الأخطاء فقط
├── myapp-startup.log           # سجلات بدء التشغيل
├── myapp-session-20250710_143022.log  # مخصص للجلسة
└── archived/                   # السجلات الأقدم المُدوَّرة
```

**لاستخدام هذا:**
1. ضع `logback-spring.xml` في مجلد `src/main/resources/` الخاص بك
2. قم بتحديث `application.yml` الخاص بك بتكوين التسجيل
3. شغل تطبيق Spring Boot الخاص بك
4. سيتم جمع السجلات تلقائيًا في دليل `logs/`

هذا يلغي تمامًا الحاجة إلى نسخ السجلات يدويًا - كل تشغيل لتطبيقك سيولد تلقائيًا ملفات سجلات منظمة وقابلة للبحث يمكنك الرجوع إليها لاحقًا بسهولة!

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- Define log directory and file patterns -->
    <property name="LOG_DIR" value="logs"/>
    <property name="APP_NAME" value="myapp"/>
    
    <!-- Console appender for development -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- File appender for all logs -->
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
    
    <!-- Separate appender for ERROR logs only -->
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
    
    <!-- Separate appender for startup logs -->
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
    
    <!-- Application-specific logger for startup events -->
    <logger name="org.springframework.boot" level="INFO" additivity="false">
        <appender-ref ref="STARTUP_FILE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="CONSOLE"/>
    </logger>
    
    <!-- Capture SQL logs if using JPA -->
    <logger name="org.hibernate.SQL" level="DEBUG" additivity="false">
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Root logger configuration -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
    
    <!-- Profile-specific configurations -->
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
    
# Alternative: Direct configuration in application.yml (simpler approach)
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

# Management endpoints for monitoring logs
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
        
        // Create session-specific log file
        String sessionId = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String sessionLogFile = logPath + "/" + appName + "-session-" + sessionId + ".log";
        
        // Setup session appender
        RollingFileAppender sessionAppender = new RollingFileAppender();
        sessionAppender.setContext(context);
        sessionAppender.setFile(sessionLogFile);
        
        // Pattern encoder
        PatternLayoutEncoder encoder = new PatternLayoutEncoder();
        encoder.setContext(context);
        encoder.setPattern("%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        encoder.start();
        sessionAppender.setEncoder(encoder);
        
        // Rolling policy
        TimeBasedRollingPolicy rollingPolicy = new TimeBasedRollingPolicy();
        rollingPolicy.setContext(context);
        rollingPolicy.setParent(sessionAppender);
        rollingPolicy.setFileNamePattern(logPath + "/" + appName + "-session-%d{yyyy-MM-dd}.%i.log");
        rollingPolicy.setMaxHistory(7);
        rollingPolicy.setTotalSizeCap(FileSize.valueOf("100MB"));
        rollingPolicy.start();
        
        sessionAppender.setRollingPolicy(rollingPolicy);
        sessionAppender.start();
        
        // Add to root logger
        Logger rootLogger = context.getLogger(Logger.ROOT_LOGGER_NAME);
        rootLogger.addAppender(sessionAppender);
    }
}

// Utility class for custom log collection
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
        // Optional: Compress or archive logs on shutdown
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