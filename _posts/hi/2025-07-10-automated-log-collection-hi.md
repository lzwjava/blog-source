---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग बूट में लॉग संग्रह को स्वचालित करें
translated: true
type: note
---

आप बिल्कुल सही हैं! मैन्युअल रूप से लॉग्स को कॉपी और पेस्ट करना थकाऊ और त्रुटिपूर्ण है। मुझे आपको दिखाने दें कि Spring Boot प्रोजेक्ट्स में Logback का उपयोग करके स्वचालित लॉग संग्रह कैसे सेट अप करें।

अब मुझे आपको दिखाने दें कि इसे अपने Spring Boot एप्लिकेशन प्रॉपर्टीज में कैसे कॉन्फ़िगर करें:

यहाँ एक Java कॉन्फ़िगरेशन दृष्टिकोण भी है यदि आप प्रोग्रामेटिक सेटअप पसंद करते हैं:

इस स्वचालित सेटअप के प्रमुख लाभ यहाँ दिए गए हैं:

**यह आपको क्या देता है:**
1. **स्वचालित लॉग डायरेक्टरी निर्माण** - आपके प्रोजेक्ट में एक `logs/` फ़ोल्डर बनाता है
2. **एकाधिक लॉग फ़ाइलें** - सामान्य लॉग्स, एरर लॉग्स और स्टार्टअप लॉग्स को अलग करता है
3. **रोलिंग फ़ाइलें** - तारीख और आकार के आधार पर लॉग्स को स्वचालित रूप से रोटेट करता है
4. **सत्र-आधारित लॉगिंग** - प्रत्येक रन को टाइमस्टैम्प वाली लॉग फ़ाइलें मिलती हैं
5. **कोई मैन्युअल कॉपीिंग नहीं** - सब कुछ स्वचालित रूप से सेव हो जाता है

**आपको मिलने वाली फ़ाइल संरचना:**
```
logs/
├── myapp.log                    # वर्तमान सामान्य लॉग
├── myapp-error.log             # केवल एरर लॉग्स
├── myapp-startup.log           # स्टार्टअप लॉग्स
├── myapp-session-20250710_143022.log  # सत्र-विशिष्ट लॉग
└── archived/                   # पुराने रोटेटेड लॉग्स
```

**इसका उपयोग करने के लिए:**
1. `logback-spring.xml` को अपने `src/main/resources/` फ़ोल्डर में रखें
2. अपने `application.yml` को लॉगिंग कॉन्फ़िगरेशन के साथ अपडेट करें
3. अपने Spring Boot एप्लिकेशन को रन करें
4. लॉग्स स्वचालित रूप से `logs/` डायरेक्टरी में एकत्रित हो जाएंगे

यह मैन्युअल लॉग कॉपी करने की आवश्यकता को पूरी तरह से समाप्त कर देता है - आपके एप्लिकेशन का हर रन स्वचालित रूप से संगठित, खोजने योग्य लॉग फ़ाइलें उत्पन्न करेगा जिन्हें आप बाद में आसानी से संदर्भित कर सकते हैं!

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- लॉग डायरेक्टरी और फ़ाइल पैटर्न परिभाषित करें -->
    <property name="LOG_DIR" value="logs"/>
    <property name="APP_NAME" value="myapp"/>
    
    <!-- विकास के लिए कंसोल ऐपेंडर -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- सभी लॉग्स के लिए फ़ाइल ऐपेंडर -->
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
    
    <!-- केवल ERROR लॉग्स के लिए अलग ऐपेंडर -->
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
    
    <!-- स्टार्टअप लॉग्स के लिए अलग ऐपेंडर -->
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
    
    <!-- स्टार्टअप इवेंट्स के लिए एप्लिकेशन-स्पेसिफिक लॉगर -->
    <logger name="org.springframework.boot" level="INFO" additivity="false">
        <appender-ref ref="STARTUP_FILE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="CONSOLE"/>
    </logger>
    
    <!-- SQL लॉग्स कैप्चर करें यदि JPA उपयोग कर रहे हैं -->
    <logger name="org.hibernate.SQL" level="DEBUG" additivity="false">
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- रूट लॉगर कॉन्फ़िगरेशन -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
    
    <!-- प्रोफ़ाइल-स्पेसिफिक कॉन्फ़िगरेशन -->
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
    
# वैकल्पिक: application.yml में सीधी कॉन्फ़िगरेशन (सरल दृष्टिकोण)
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

# लॉग्स की निगरानी के लिए मैनेजमेंट एंडपॉइंट्स
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
        
        // सत्र-विशिष्ट लॉग फ़ाइल बनाएं
        String sessionId = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String sessionLogFile = logPath + "/" + appName + "-session-" + sessionId + ".log";
        
        // सत्र ऐपेंडर सेटअप करें
        RollingFileAppender sessionAppender = new RollingFileAppender();
        sessionAppender.setContext(context);
        sessionAppender.setFile(sessionLogFile);
        
        // पैटर्न एनकोडर
        PatternLayoutEncoder encoder = new PatternLayoutEncoder();
        encoder.setContext(context);
        encoder.setPattern("%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        encoder.start();
        sessionAppender.setEncoder(encoder);
        
        // रोलिंग पॉलिसी
        TimeBasedRollingPolicy rollingPolicy = new TimeBasedRollingPolicy();
        rollingPolicy.setContext(context);
        rollingPolicy.setParent(sessionAppender);
        rollingPolicy.setFileNamePattern(logPath + "/" + appName + "-session-%d{yyyy-MM-dd}.%i.log");
        rollingPolicy.setMaxHistory(7);
        rollingPolicy.setTotalSizeCap(FileSize.valueOf("100MB"));
        rollingPolicy.start();
        
        sessionAppender.setRollingPolicy(rollingPolicy);
        sessionAppender.start();
        
        // रूट लॉगर में जोड़ें
        Logger rootLogger = context.getLogger(Logger.ROOT_LOGGER_NAME);
        rootLogger.addAppender(sessionAppender);
    }
}

// कस्टम लॉग संग्रह के लिए यूटिलिटी क्लास
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
        // वैकल्पिक: शटडाउन पर लॉग्स को कंप्रेस या आर्काइव करें
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