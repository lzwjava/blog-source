---
audio: false
generated: true
lang: de
layout: post
title: Planen Von Aufgaben In Spring
translated: true
type: note
---

Das Planen von Aufgaben in Spring ist eine häufige Anforderung für die Automatisierung sich wiederholender Jobs, wie das Senden von E-Mails, das Generieren von Berichten oder die Durchführung von Systemwartungen. Spring bietet eine leistungsstarke und einfach zu verwendende Task-Scheduling-Funktion durch seine `@Scheduled`-Annotation und den Spring Task Scheduler. Im Folgenden werde ich Sie durch die Einrichtungsschritte führen und die Schlüsselkonzepte erklären.

### 1. **Aktivieren Sie Scheduling in Ihrer Spring-Anwendung**
Um Scheduling zu verwenden, müssen Sie es in Ihrer Spring-Anwendung aktivieren. Dies geschieht durch Hinzufügen der `@EnableScheduling`-Annotation zu einer Konfigurationsklasse.

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // Die Konfigurationsklasse kann leer sein, es sei denn, Sie benötigen benutzerdefinierte Scheduler-Einstellungen
}
```

Dies weist Spring an, nach Methoden zu suchen, die mit `@Scheduled` annotiert sind, und sie gemäß ihrem definierten Zeitplan auszuführen.

---

### 2. **Erstellen Sie eine zu planende Aufgabe**
Sie können eine Methode in jeder Spring-verwalteten Bean (wie einer `@Component` oder `@Service`) definieren und sie mit `@Scheduled` annotieren. Hier ist ein Beispiel:

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // Läuft alle 5 Sekunden
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Task executed at: " + System.currentTimeMillis());
    }
}
```

In diesem Beispiel:
- `@Component` macht die Klasse zu einer Spring-Bean.
- `@Scheduled(fixedRate = 5000)` führt die Methode alle 5 Sekunden (5000 Millisekunden) aus.

---

### 3. **Arten von Scheduling-Optionen**
Spring bietet mehrere Möglichkeiten zu definieren, wann eine Aufgabe ausgeführt werden soll:

#### a) **Feste Rate (Fixed Rate)**
- Führt die Aufgabe in einem festen Intervall aus, unabhängig davon, wie lange die Aufgabe dauert.
- Beispiel: `@Scheduled(fixedRate = 5000)` (alle 5 Sekunden).

#### b) **Feste Verzögerung (Fixed Delay)**
- Führt die Aufgabe mit einer festen Verzögerung zwischen dem Ende einer Ausführung und dem Start der nächsten aus.
- Beispiel: `@Scheduled(fixedDelay = 5000)` (5 Sekunden, nachdem die vorherige Aufgabe beendet ist).

#### c) **Cron-Ausdruck**
- Verwendet eine cron-ähnliche Syntax für komplexere Zeitpläne (z. B. "jeden Werktag um 9 Uhr").
- Beispiel: `@Scheduled(cron = "0 0 9 * * MON-FRI")`.

#### d) **Anfangsverzögerung (Initial Delay)**
- Verzögert die erste Ausführung der Aufgabe. Kann mit `fixedRate` oder `fixedDelay` kombiniert werden.
- Beispiel: `@Scheduled(fixedRate = 5000, initialDelay = 10000)` (startet nach 10 Sekunden, läuft dann alle 5 Sekunden).

---

### 4. **Cron-Syntax Grundlagen**
Wenn Sie Cron verwenden, hier eine kurze Referenz:
- Format: `Sekunde Minute Stunde Tag-des-Monats Monat Tag-der-Woche`
- Beispiel: `@Scheduled(cron = "0 15 10 * * ?")` (läuft jeden Tag um 10:15 Uhr).

| Feld          | Zulässige Werte      |
|---------------|----------------------|
| Sekunde       | 0-59                |
| Minute        | 0-59                |
| Stunde        | 0-23                |
| Tag des Monats| 1-31                |
| Monat         | 1-12 oder JAN-DEC   |
| Tag der Woche | 0-7 oder SUN-SAT (0 oder 7 ist Sonntag) |

Sonderzeichen wie `*` (alle), `,` (Liste), `-` (Bereich), `/` (Inkrement) können verwendet werden.

---

### 5. **Abhängigkeiten**
Wenn Sie Spring Boot verwenden, ist die Scheduling-Funktion standardmäßig in der `spring-boot-starter`-Abhängigkeit enthalten. Für ein Nicht-Boot-Spring-Projekt stellen Sie sicher, dass Sie Folgendes haben:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- Verwenden Sie die neueste Version -->
</dependency>
```

---

### 6. **Vollständiges Beispiel mit Spring Boot**
Hier ein vollständiges Spring Boot-Beispiel:

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
        System.out.println("Running every 5 seconds: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("Running every minute: " + System.currentTimeMillis());
    }
}
```

---

### 7. **Anpassen des Schedulers (Optional)**
Standardmäßig verwendet Spring einen Single-Threaded-Scheduler. Wenn Sie eine gleichzeitige Aufgabenausführung benötigen, können Sie einen benutzerdefinierten `TaskScheduler` konfigurieren:

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

Dies ermöglicht es mehreren Aufgaben, parallel ausgeführt zu werden.

---

### 8. **Testen Ihrer geplanten Aufgaben**
- Führen Sie Ihre Anwendung aus und überprüfen Sie die Konsolenprotokolle, um zu verifizieren, dass die Aufgaben wie erwartet ausgeführt werden.
- Verwenden Sie während des Testens kürzere Intervalle (z. B. alle 2 Sekunden), um die Ergebnisse schnell zu sehen.