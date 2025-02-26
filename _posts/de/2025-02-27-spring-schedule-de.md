---
audio: true
lang: de
layout: post
title: Aufgabenplanung in Spring
translated: true
---

### Aufgabenplanung in Spring

Die Planung von Aufgaben in Spring ist eine häufige Anforderung zur Automatisierung wiederholter Aufgaben, wie das Senden von E-Mails, das Generieren von Berichten oder das Durchführen von Systemwartung. Spring bietet eine leistungsstarke und einfach zu verwendende Aufgabenplanungsfunktion über die `@Scheduled`-Annotierung und den Spring Task Scheduler. Im Folgenden werde ich Sie durch die Schritte zur Einrichtung führen und die wichtigsten Konzepte erklären.

### 1. **Aktivieren der Planung in Ihrer Spring-Anwendung**

Um die Planung zu verwenden, müssen Sie sie in Ihrer Spring-Anwendung aktivieren. Dies geschieht durch Hinzufügen der `@EnableScheduling`-Annotierung zu einer Konfigurationsklasse.

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // Die Konfigurationsklasse kann leer bleiben, es sei denn, Sie benötigen benutzerdefinierte Scheduler-Einstellungen
}
```

Dies weist Spring an, nach Methoden zu suchen, die mit `@Scheduled` annotiert sind, und sie gemäß ihren definierten Zeitplänen auszuführen.

---

### 2. **Erstellen einer zu planenden Aufgabe**

Sie können eine Methode in jedem Spring-verwalteten Bean (wie einem `@Component` oder `@Service`) definieren und sie mit `@Scheduled` annotieren. Hier ist ein Beispiel:

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // Wird alle 5 Sekunden ausgeführt
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Aufgabe ausgeführt um: " + System.currentTimeMillis());
    }
}
```

In diesem Beispiel:
- `@Component` macht die Klasse zu einem Spring-Bean.
- `@Scheduled(fixedRate = 5000)` führt die Methode alle 5 Sekunden (5000 Millisekunden) aus.

---

### 3. **Arten von Planungsoptionen**

Spring bietet mehrere Möglichkeiten, festzulegen, wann eine Aufgabe ausgeführt werden soll:

#### a) **Feste Rate**

- Führt die Aufgabe in festen Intervallen aus, unabhängig davon, wie lange die Aufgabe dauert.
- Beispiel: `@Scheduled(fixedRate = 5000)` (jeder 5 Sekunden).

#### b) **Feste Verzögerung**

- Führt die Aufgabe mit einer festen Verzögerung zwischen dem Ende einer Ausführung und dem Beginn der nächsten aus.
- Beispiel: `@Scheduled(fixedDelay = 5000)` (5 Sekunden nach Beendigung der vorherigen Aufgabe).

#### c) **Cron-Ausdruck**

- Verwendet eine cron-ähnliche Syntax für komplexere Zeitpläne (z. B. „jeden Werktag um 9 Uhr“).
- Beispiel: `@Scheduled(cron = "0 0 9 * * MON-FRI")`.

#### d) **Anfangsverzögerung**

- Verzögert die erste Ausführung der Aufgabe. Kombinieren Sie es mit `fixedRate` oder `fixedDelay`.
- Beispiel: `@Scheduled(fixedRate = 5000, initialDelay = 10000)` (startet nach 10 Sekunden, dann läuft jede 5 Sekunden).

---

### 4. **Grundlagen der Cron-Syntax**

Wenn Sie cron verwenden, hier eine schnelle Referenz:
- Format: `Sekunde Minute Stunde Tag-des-Monats Monat Wochentag`
- Beispiel: `@Scheduled(cron = "0 15 10 * * ?")` (wird täglich um 10:15 Uhr ausgeführt).

| Feld          | Erlaubte Werte       |
|---------------|----------------------|
| Sekunde        | 0-59                |
| Minute        | 0-59                |
| Stunde         | 0-23                |
| Tag des Monats | 1-31                |
| Monat         | 1-12 oder JAN-DEC    |
| Wochentag     | 0-7 oder SON-SAT (0 oder 7 ist Sonntag) |

Spezielle Zeichen wie `*` (alle), `,` (Liste), `-` (Bereich), `/` (Inkrement) können verwendet werden.

---

### 5. **Abhängigkeiten**

Wenn Sie Spring Boot verwenden, ist die Planungsfunktion standardmäßig in der `spring-boot-starter`-Abhängigkeit enthalten. Für ein nicht-Boot-Spring-Projekt stellen Sie sicher, dass Sie haben:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- Verwenden Sie die neueste Version -->
</dependency>
```

---

### 6. **Vollständiges Beispiel mit Spring Boot**

Hier ist ein vollständiges Spring Boot-Beispiel:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Component
class ScheduledTasks {

    @Scheduled(fixedRate = 5000)
    public void runEveryFiveSeconds() {
        System.out.println("Wird jede 5 Sekunden ausgeführt: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("Wird jede Minute ausgeführt: " + System.currentTimeMillis());
    }
}
```

---

### 7. **Anpassen des Schedulers (optional)**

Standardmäßig verwendet Spring einen einthreadigen Scheduler. Wenn Sie eine gleichzeitige Aufgabenausführung benötigen, können Sie einen benutzerdefinierten `TaskScheduler` konfigurieren:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // Anzahl der Threads
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

Dies ermöglicht es mehreren Aufgaben, parallel zu laufen.

---

### 8. **Testen Ihrer geplanten Aufgaben**

- Starten Sie Ihre Anwendung und überprüfen Sie die Konsolenprotokolle, um sicherzustellen, dass die Aufgaben wie erwartet ausgeführt werden.
- Verwenden Sie kürzere Intervalle (z. B. jede 2 Sekunden) während des Testens, um schnell Ergebnisse zu sehen.