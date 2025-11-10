---
audio: false
generated: true
lang: es
layout: post
title: Automatización de la Recopilación de Registros en Spring Boot
translated: true
type: note
---

¡Tienes toda la razón! Copiar y pegar logs manualmente es tedioso y propenso a errores. Permíteme mostrarte cómo configurar la recolección automatizada de logs en proyectos Spring Boot usando Logback.

Ahora permíteme mostrarte cómo configurar esto en las propiedades de tu aplicación Spring Boot:

Aquí también hay un enfoque de configuración Java si prefieres la configuración programática:

Estos son los beneficios clave de esta configuración automatizada:

**Lo que esto te proporciona:**
1. **Creación automática de directorios de logs** - Crea una carpeta `logs/` en tu proyecto
2. **Múltiples archivos de log** - Separa logs generales, logs de error y logs de inicio
3. **Archivos rotativos** - Rota automáticamente los logs por fecha y tamaño
4. **Logging basado en sesiones** - Cada ejecución obtiene archivos de log con marca de tiempo
5. **Sin copia manual** - Todo se guarda automáticamente

**Estructura de archivos que obtendrás:**
```
logs/
├── myapp.log                    # Log general actual
├── myapp-error.log             # Solo logs de error
├── myapp-startup.log           # Logs de inicio
├── myapp-session-20250710_143022.log  # Específico de sesión
└── archived/                   # Logs rotados más antiguos
```

**Para usar esto:**
1. Coloca `logback-spring.xml` en tu carpeta `src/main/resources/`
2. Actualiza tu `application.yml` con la configuración de logging
3. Ejecuta tu aplicación Spring Boot
4. Los logs se recopilarán automáticamente en el directorio `logs/`

¡Esto elimina completamente la necesidad de copiar logs manualmente - cada ejecución de tu aplicación generará automáticamente archivos de log organizados y buscables que puedes consultar fácilmente más tarde!

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