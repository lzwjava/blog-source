---
audio: false
generated: true
lang: de
layout: post
title: Maven-Abhängigkeitsproblem
translated: true
type: note
---

### Problemüberblick

Der Benutzer erlebt einen Build-Fehler beim Ausführen einer Spring Boot Anwendung mit Maven. Die Fehlermeldung weist auf eine `IllegalArgumentException` hin, verursacht durch `NoClassDefFoundError: org/springframework/beans/factory/aot/BeanRegistrationExcludeFilter`. Dies deutet auf ein Versionsinkompatibilitätsproblem innerhalb der Projektabhängigkeiten hin, das den korrekten Start der Anwendung verhindert. Die bereitgestellte `pom.xml`-Datei und die Maven-Ausgabe geben uns den Kontext, der zur Diagnose und Lösung des Problems benötigt wird.

### Grundursache

Der Fehler tritt auf, weil die Spring Boot Anwendung die Klasse `SharedMetadataReaderFactoryContextInitializer`, die am Auto-Konfigurationsprozess von Spring Boot beteiligt ist, nicht instanziieren kann. Die zugrundeliegende Ursache ist eine fehlende Klasse, `BeanRegistrationExcludeFilter`, die Teil des Spring Frameworks 6.0 und höher ist. Das Projekt verwendet Spring Boot 3.4.2, welches vom Spring Framework 6.1.14 abhängt. Allerdings spezifiziert die `pom.xml` ältere, inkompatible Versionen der Spring Framework Abhängigkeiten, was zu einem Classpath-Konflikt führt.

Hier sind die wichtigsten, in der `pom.xml` identifizierten Probleme:

1. **Inkompatible Version des Spring Boot Maven Plugins:**
   - Das `spring-boot-maven-plugin` ist auf Version `2.7.0` gesetzt, welche für Spring Boot 2.x und nicht für Spring Boot 3.4.2 (eine 3.x Version) entwickelt wurde. Diese Fehlanpassung kann Probleme während der Build- und Laufzeitphasen verursachen.

2. **Explizite, inkompatible Spring Framework Abhängigkeiten:**
   - Die `pom.xml` deklariert explizit `spring-aop` und `spring-aspects` mit Version `5.3.23` (Spring Framework 5.x), während Spring Boot 3.4.2 Spring Framework 6.1.14 benötigt. Maven priorisiert diese explizit deklarierten Versionen gegenüber den von Spring Boot verwalteten Versionen, was zu einer Mischung von Spring Framework 5.x und 6.x im Classpath führt. Diese Mischung verursacht den `NoClassDefFoundError`, weil `BeanRegistrationExcludeFilter` (aus Spring Framework 6.x) nicht verfügbar ist, wenn ältere 5.x JARs geladen werden.

### Lösung

Um das Problem zu beheben, müssen wir sicherstellen, dass alle Projektkomponenten mit Spring Boot 3.4.2 kompatibel sind und dass Spring Boot die Versionen seiner Abhängigkeiten verwaltet, um Konflikte zu vermeiden. Die folgenden Änderungen sollten an der `pom.xml` vorgenommen werden:

1. **Aktualisieren der Spring Boot Maven Plugin Version:**
   - Ändern Sie die `spring-boot-maven-plugin` Version von `2.7.0` auf `3.4.2`, um sie an die im Projekt verwendete Spring Boot Version anzupassen.

2. **Entfernen der expliziten Spring Framework Abhängigkeiten:**
   - Entfernen Sie die expliziten Deklarationen von `spring-aop` und `spring-aspects` mit Version `5.3.23`. Spring Boot 3.4.2 verwaltet diese Abhängigkeiten über seine Starter (z.B. beinhaltet `spring-boot-starter-web` `spring-aop` mit der korrekten Version 6.1.14). Durch deren Entfernung verhindern wir, dass Maven das Dependency Management von Spring Boot überschreibt.

### Aktualisierte `pom.xml`

Nachfolgend finden Sie die korrigierte `pom.xml`-Datei mit den notwendigen Änderungen:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.lzwjava</groupId>
    <artifactId>blog-server</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>3.4.2</version>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-api</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter-engine</artifactId>
            <version>5.9.3</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>5.3.1</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>3.4.2</version>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.22</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.22</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>3.4.2</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M8</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.1</version>
                <configuration>
                    <configLocation>google_checks.xml</configLocation>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### Erklärung der Änderungen

- **Aktualisierung des Spring Boot Maven Plugins:**
  - Geändert `<version>2.7.0</version>` zu `<version>3.4.2</version>` in der `spring-boot-maven-plugin` Konfiguration. Dies stellt sicher, dass das Plugin mit Spring Boot 3.4.2 kompatibel ist und Funktionen sowie Konfigurationen unterstützt, die spezifisch für die 3.x Serie sind.

- **Entfernung von `spring-aop` und `spring-aspects`:**
  - Folgende Abhängigkeiten wurden entfernt:
    ```xml
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aop</artifactId>
        <version>5.3.23</version>
    </dependency>
    <dependency>
        <groupId>org.springframework</groupId>
        <artifactId>spring-aspects</artifactId>
        <version>5.3.23</version>
    </dependency>
    ```
  - `spring-aop` ist bereits in `spring-boot-starter-web` (über `spring-web`) enthalten, und Spring Boot verwaltet dessen Version auf 6.1.14, was mit 3.4.2 kompatibel ist.
  - `spring-aspects` ist keine Standardabhängigkeit in Spring Boot Startern. Wenn das Projekt sie explizit benötigt (z.B. für benutzerdefinierte Aspekte), kann sie ohne Version (wodurch das Dependency Management von Spring Boot sie verwaltet) oder auf `6.1.14` gesetzt wieder hinzugefügt werden. Da der Fehler jedoch während des Starts auftritt und sich auf die Auto-Konfiguration und nicht auf fehlende Aspekte bezieht, ist sie hier wahrscheinlich unnötig und kann sicher entfernt werden.

### Zusätzliche Hinweise

- **AspectJ Abhängigkeiten:**
  - Die `aspectjrt` und `aspectjweaver` Abhängigkeiten (Version 1.9.22) verbleiben in der `pom.xml`, da sie mit Spring Framework 6.1.14 kompatibel sind und möglicherweise benötigt werden, wenn das Projekt AspectJ-Features verwendet. Diese stehen nicht im Konflikt mit Spring Boot 3.4.2.

- **Best Practices:**
  - Für Spring Boot Projekte wird empfohlen, `spring-boot-starter-parent` als Parent POM zu verwenden oder das `spring-boot-dependencies` BOM zu importieren, um Abhängigkeitsversionen automatisch zu verwalten. Die aktuelle `pom.xml` tut keines von beiden, aber die Lösung funktioniert ohne diese Änderung, da `spring-boot-starter-web` und andere Starter weiterhin Versionskonsistenz erzwingen, wenn explizite Overrides entfernt werden.

- **Verifikation:**
  - Führen Sie nach Anwendung dieser Änderungen `mvn clean spring-boot:run` aus, um zu überprüfen, ob die Anwendung ohne Fehler startet. Wenn das Projekt auf `spring-aspects` angewiesen ist (z.B. für spezifische AOP-Funktionalität) und deren Entfernung Probleme verursacht, fügen Sie sie mit `<version>6.1.14</version>` wieder hinzu oder lassen Sie die Version weg und stellen Sie ein korrektes Dependency Management sicher.

### Fazit

Durch die Aktualisierung des `spring-boot-maven-plugin` auf Version 3.4.2 und das Entfernen der expliziten `spring-aop` und `spring-aspects` Abhängigkeiten verwendet das Projekt konsistente Versionen von Spring Boot (3.4.2) und Spring Framework (6.1.14). Dies behebt den Classpath-Konflikt, der den `NoClassDefFoundError` verursacht hat, und ermöglicht einen erfolgreichen Start der Anwendung.