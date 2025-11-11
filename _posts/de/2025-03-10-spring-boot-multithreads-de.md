---
audio: false
generated: true
lang: de
layout: post
title: Spring Boot Multithreading
translated: true
type: note
---

In einem Spring Boot-Projekt beziehen sich die Konzepte von "Executors" und "Threads" typischerweise darauf, wie die Anwendung gleichzeitige Tasks handhabt und ihre Arbeitslast verwaltet, insbesondere in Szenarien, die asynchrone Verarbeitung, Task-Scheduling oder die Bearbeitung mehrerer Anfragen umfassen. Lass uns das Schritt für Schritt aufschlüsseln:

---

### **Was sind Executors und Threads in Spring Boot?**

1.  **Threads**:
    - Ein Thread ist die kleinste Ausführungseinheit in einem Java-Programm. In einer Spring Boot-Anwendung werden Threads verwendet, um Tasks wie die Verarbeitung von HTTP-Anfragen, die Ausführung von Hintergrundjobs oder die Durchführung von I/O-Operationen zu handhaben.
    - Spring Boot läuft standardmäßig in einem eingebetteten Webserver (z.B. Tomcat, Jetty oder Undertow), der einen Thread-Pool verwendet, um eingehende Anfragen zu verwalten. Jede Anfrage wird typischerweise einem Thread aus diesem Pool zugewiesen.

2.  **Executors**:
    - Ein `Executor` in Java (und Spring Boot) ist eine Abstraktion über die Thread-Verwaltung. Es ist Teil des `java.util.concurrent`-Pakets und bietet eine Möglichkeit, Tasks asynchron auszuführen und zu verwalten, ohne Threads manuell zu erstellen und zu verwalten.
    - In Spring Boot werden Executors oft verwendet, um Tasks vom Hauptanwendungsthread (z.B. dem Thread, der eine HTTP-Anfrage bearbeitet) auf einen separaten Thread-Pool auszulagern. Dies ist nützlich für langlaufende Tasks, Parallelverarbeitung oder geplante Jobs.

3.  **Spring-spezifischer Kontext**:
    - Spring Boot bietet Hilfsprogramme wie `ThreadPoolTaskExecutor` (für allgemeine Task-Ausführung) und `ThreadPoolTaskScheduler` (für geplante Tasks), um die Arbeit mit Executors und Threads zu vereinfachen.
    - Diese bauen auf Javas `ExecutorService` auf und werden häufig verwendet für:
        - Asynchrone Methodenausführung (via `@Async`).
        - Task-Scheduling (via `@Scheduled`).
        - Verwaltung von Arbeitslasten in Hochlast-Szenarien.

---

### **Wie funktionieren sie in Spring Boot?**

#### **1. Standard-Thread-Verwaltung in Spring Boot**
- Wenn Sie eine Spring Boot-Webanwendung starten, initialisiert der eingebettete Server (z.B. Tomcat) einen Thread-Pool, um eingehende HTTP-Anfragen zu handhaben.
- Beispielsweise könnte die Standardkonfiguration von Tomcat 200 Threads zuweisen (konfigurierbar über `server.tomcat.threads.max` in `application.properties`).
- Jede eingehende Anfrage erhält einen Thread aus diesem Pool. Wenn alle Threads beschäftigt sind und eine neue Anfrage eintrifft, kann diese in die Warteschlange gestellt werden (abhängig von der Serverkonfiguration) oder abgelehnt werden.

#### **2. Executors in Spring Boot**
- Spring Boot stellt die `TaskExecutor`-Schnittstelle (eine Erweiterung von Javas `Executor`) bereit, um benutzerdefinierte Thread-Pools für spezifische Tasks zu verwalten.
- Eine gängige Implementierung ist `ThreadPoolTaskExecutor`, mit dem Sie konfigurieren können:
    - **Core Pool Size**: Die Anzahl der Threads, die immer aktiv gehalten werden.
    - **Max Pool Size**: Die maximale Anzahl von Threads, die im Pool erlaubt sind.
    - **Queue Capacity**: Die Anzahl der Tasks, die in der Warteschlange warten können, bevor neue Threads erstellt werden (bis zur max Pool Size).
    - **Thread Naming**: Zur einfacheren Fehlersuche (z.B. "my-executor-thread-1").

    Beispielkonfiguration in einer Spring Boot-App:
    ```java
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.Configuration;
    import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

    @Configuration
    public class ExecutorConfig {

        @Bean
        public ThreadPoolTaskExecutor taskExecutor() {
            ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
            executor.setCorePoolSize(5);      // Minimum 5 Threads
            executor.setMaxPoolSize(10);      // Maximum 10 Threads
            executor.setQueueCapacity(100);   // Bis zu 100 Tasks in der Warteschlange
            executor.setThreadNamePrefix("MyExecutor-");
            executor.initialize();
            return executor;
        }
    }
    ```

#### **3. Verwendung von `@Async` mit Executors**
- Spring Boot unterstützt asynchrone Methodenausführung mit der `@Async`-Annotation. Wenn Sie eine Methode mit `@Async` annotieren, läuft sie in einem separaten Thread, der von einem Executor verwaltet wird.
- Standardmäßig verwendet Spring einen `SimpleAsyncTaskExecutor`, der für jede Task einen neuen Thread erstellt (nicht ideal für hohe Last). Um dies zu optimieren, können Sie Ihren eigenen `ThreadPoolTaskExecutor` bereitstellen (wie oben gezeigt) und darauf verweisen:
    ```java
    @Service
    public class MyService {

        @Async("taskExecutor") // Bezieht sich auf den Bean-Namen aus der Konfiguration
        public void doAsyncTask() {
            System.out.println("Running on thread: " + Thread.currentThread().getName());
        }
    }
    ```

#### **4. Task-Scheduling**
- Für geplante Tasks (z.B. das Ausführen eines Jobs alle 5 Minuten) verwendet Spring Boot `ThreadPoolTaskScheduler`. Es ist ähnlich wie `ThreadPoolTaskExecutor`, aber für Scheduling zugeschnitten.
- Beispiel:
    ```java
    @Scheduled(fixedRate = 5000) // Läuft alle 5 Sekunden
    public void scheduledTask() {
        System.out.println("Scheduled task on: " + Thread.currentThread().getName());
    }
    ```

#### **5. Wie Threads und Executors interagieren**
- Wenn ein Task einem Executor übergeben wird (z.B. via `@Async` oder manueller Übergabe), entscheidet der Executor, ob er:
    - Einen bestehenden idle Thread aus dem Pool verwendet.
    - Einen neuen Thread erstellt (wenn die Core Pool Size überschritten, aber die Max Pool Size noch nicht erreicht ist).
    - Den Task in die Warteschlange stellt (wenn die Max Pool Size erreicht ist und die Warteschlange nicht voll ist).
    - Den Task ablehnt (wenn die Warteschlange voll ist und keine weiteren Threads erstellt werden können).
- Threads führen die Tasks aus und kehren nach Abschluss in den Pool zurück, bereit für den nächsten Task.

---

### **Praktisches Beispiel**
Stellen Sie sich eine Spring Boot-App vor, die Benutzerregistrierungen handhabt:
- **HTTP-Request-Thread**: Ein Benutzer sendet ein Registrierungsformular, bearbeitet von einem Thread aus dem Tomcat-Thread-Pool.
- **Async-Task**: Das Senden einer Bestätigungs-E-Mail wird via einer `@Async`-Methode an einen `ThreadPoolTaskExecutor` ausgelagert, sodass der HTTP-Thread sofort antworten kann, ohne auf den Versand der E-Mail zu warten.
- **Geplanter Task**: Ein Bereinigungsjob läuft stündlich, um nicht verifizierte Konten zu entfernen, verwaltet von einem `ThreadPoolTaskScheduler`.

---

### **Wichtige Punkte**
- **Executors** abstrahieren die Thread-Verwaltung, was es einfacher macht, Nebenläufigkeit zu skalieren und zu optimieren.
- **Threads** verrichten die eigentliche Arbeit und ihr Lebenszyklus wird von Executors oder dem Webserver verwaltet.
- Die Standardeinstellungen von Spring Boot sind für kleine Apps ausreichend, aber für Hochlast- oder komplexe Apps konfigurieren Sie benutzerdefinierte Executors, um die Leistung zu optimieren.

Wenn Sie ein bestimmtes Spring Boot-Projekt im Sinn haben und Hilfe bei der Analyse seines Executor/Thread-Setups benötigen, teilen Sie gerne weitere Details mit!