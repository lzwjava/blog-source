---
audio: false
generated: true
lang: fr
layout: post
title: Automatisation de la Collecte de Journaux dans Spring Boot
translated: true
type: note
---

Vous avez absolument raison ! Copier et coller manuellement les logs est fastidieux et sujet aux erreurs. Laissez-moi vous montrer comment configurer la collecte automatisée des logs dans les projets Spring Boot en utilisant Logback.

Laissez-moi maintenant vous montrer comment configurer cela dans vos propriétés d'application Spring Boot :

Voici également une approche de configuration Java si vous préférez une configuration programmatique :

Voici les principaux avantages de cette configuration automatisée :

**Ce que cela vous apporte :**
1. **Création automatique du répertoire de logs** - Crée un dossier `logs/` dans votre projet
2. **Fichiers de logs multiples** - Sépare les logs généraux, les logs d'erreur et les logs de démarrage
3. **Fichiers rotatifs** - Fait tourner automatiquement les logs par date et taille
4. **Journalisation par session** - Chaque exécution obtient des fichiers de logs horodatés
5. **Aucune copie manuelle** - Tout est automatiquement sauvegardé

**Structure de fichiers que vous obtiendrez :**
```
logs/
├── myapp.log                    # Log général actuel
├── myapp-error.log             # Logs d'erreur uniquement
├── myapp-startup.log           # Logs de démarrage
├── myapp-session-20250710_143022.log  # Spécifique à la session
└── archived/                   # Anciens logs rotatifs
```

**Pour utiliser cela :**
1. Placez `logback-spring.xml` dans votre dossier `src/main/resources/`
2. Mettez à jour votre `application.yml` avec la configuration de logging
3. Exécutez votre application Spring Boot
4. Les logs seront automatiquement collectés dans le répertoire `logs/`

Cela élimine complètement le besoin de copier manuellement les logs - chaque exécution de votre application générera automatiquement des fichiers de logs organisés et consultables que vous pourrez facilement référencer plus tard !

```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <!-- Définir le répertoire de logs et les modèles de fichiers -->
    <property name="LOG_DIR" value="logs"/>
    <property name="APP_NAME" value="myapp"/>
    
    <!-- Appender console pour le développement -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <!-- Appender fichier pour tous les logs -->
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
    
    <!-- Appender séparé pour les logs ERROR uniquement -->
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
    
    <!-- Appender séparé pour les logs de démarrage -->
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
    
    <!-- Logger spécifique à l'application pour les événements de démarrage -->
    <logger name="org.springframework.boot" level="INFO" additivity="false">
        <appender-ref ref="STARTUP_FILE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="CONSOLE"/>
    </logger>
    
    <!-- Capturer les logs SQL si utilisation de JPA -->
    <logger name="org.hibernate.SQL" level="DEBUG" additivity="false">
        <appender-ref ref="FILE"/>
    </logger>
    
    <!-- Configuration du logger racine -->
    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
        <appender-ref ref="FILE"/>
        <appender-ref ref="ERROR_FILE"/>
    </root>
    
    <!-- Configurations spécifiques aux profils -->
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
    
# Alternative : Configuration directe dans application.yml (approche plus simple)
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

# Endpoints de management pour surveiller les logs
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
        
        // Créer un fichier de log spécifique à la session
        String sessionId = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMdd_HHmmss"));
        String sessionLogFile = logPath + "/" + appName + "-session-" + sessionId + ".log";
        
        // Configurer l'appender de session
        RollingFileAppender sessionAppender = new RollingFileAppender();
        sessionAppender.setContext(context);
        sessionAppender.setFile(sessionLogFile);
        
        // Encodeur de pattern
        PatternLayoutEncoder encoder = new PatternLayoutEncoder();
        encoder.setContext(context);
        encoder.setPattern("%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n");
        encoder.start();
        sessionAppender.setEncoder(encoder);
        
        // Politique de rotation
        TimeBasedRollingPolicy rollingPolicy = new TimeBasedRollingPolicy();
        rollingPolicy.setContext(context);
        rollingPolicy.setParent(sessionAppender);
        rollingPolicy.setFileNamePattern(logPath + "/" + appName + "-session-%d{yyyy-MM-dd}.%i.log");
        rollingPolicy.setMaxHistory(7);
        rollingPolicy.setTotalSizeCap(FileSize.valueOf("100MB"));
        rollingPolicy.start();
        
        sessionAppender.setRollingPolicy(rollingPolicy);
        sessionAppender.start();
        
        // Ajouter au logger racine
        Logger rootLogger = context.getLogger(Logger.ROOT_LOGGER_NAME);
        rootLogger.addAppender(sessionAppender);
    }
}

// Classe utilitaire pour la collecte de logs personnalisée
@Component
public class LogCollector {
    
    private static final Logger logger = LoggerFactory.getLogger(LogCollector.class);
    
    @Value("${logging.path:logs}")
    private String logPath;
    
    @EventListener(ApplicationReadyEvent.class)
    public void onApplicationReady() {
        logger.info("Application démarrée avec succès à {}", LocalDateTime.now());
        logger.info("Les fichiers de logs sont collectés dans : {}", new File(logPath).getAbsolutePath());
    }
    
    @EventListener(ContextClosedEvent.class)
    public void onApplicationShutdown() {
        logger.info("Application arrêtée à {}", LocalDateTime.now());
        collectFinalLogs();
    }
    
    private void collectFinalLogs() {
        // Optionnel : Compresser ou archiver les logs à l'arrêt
        try {
            File logDir = new File(logPath);
            if (logDir.exists()) {
                logger.info("Collecte des logs terminée. Fichiers totaux : {}", logDir.listFiles().length);
            }
        } catch (Exception e) {
            logger.error("Erreur lors de la collecte des logs", e);
        }
    }
}
```