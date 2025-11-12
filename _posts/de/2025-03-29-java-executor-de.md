---
audio: false
generated: true
lang: de
layout: post
title: Verstehen von ExecutorService und ThreadPoolExecutor
translated: true
type: note
---

Das Festlegen von Parametern für einen `ExecutorService` in Java beinhaltet die Konfiguration seines Thread-Pools, um die Leistung basierend auf den Ressourcen Ihres Systems (wie einer 8-Kern-CPU) und der Art Ihrer Aufgaben (z. B. CPU-gebunden oder I/O-gebunden) zu optimieren. Im Folgenden werde ich erklären, wie Sie einen `ExecutorService` für eine 8-Kern-CPU konfigurieren, mit Schwerpunkt auf gängigen Implementierungen wie `ThreadPoolExecutor`, und praktische Beispiele liefern, die auf Ihren Anwendungsfall zugeschnitten sind.

---

### Grundlagen zu ExecutorService und ThreadPoolExecutor

Die `ExecutorService`-Schnittstelle wird typischerweise von Klassen wie `ThreadPoolExecutor` implementiert, die eine feingranulare Kontrolle über die Thread-Pool-Parameter ermöglichen. Bei der Konfiguration für eine 8-Kern-CPU müssen Sie Folgendes berücksichtigen:
- **Core Pool Size**: Die Anzahl der Threads, die auch im Leerlauf aktiv gehalten werden.
- **Maximum Pool Size**: Die maximale Anzahl der im Pool zulässigen Threads.
- **Queue Capacity**: Die Größe der Task-Warteschlange zum Halten von Aufgaben, bevor sie ausgeführt werden.
- **Thread Creation Strategy**: Wie Threads erstellt und verwaltet werden.
- **Task Type**: Ob Aufgaben CPU-gebunden (z. B. Berechnungen) oder I/O-gebunden (z. B. Datenbankaufrufe) sind.

Für eine 8-Kern-CPU hängt die optimale Konfiguration davon ab, ob Ihre Aufgaben CPU-intensiv oder I/O-intensiv (wie der Datenbankzugriff in Ihrem Validierungsszenario) sind.

---

### Wichtige Parameter für ThreadPoolExecutor

So können Sie einen `ThreadPoolExecutor` einrichten:

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // Anzahl der lebendig zu haltenden Threads
    maximumPoolSize,   // Maximale Anzahl erlaubter Threads
    keepAliveTime,     // Zeit, die inaktive Threads lebendig gehalten werden (z.B. 60L)
    TimeUnit.SECONDS,  // Zeiteinheit für keepAliveTime
    workQueue,         // Warteschlange für Aufgaben (z.B. new LinkedBlockingQueue<>())
    threadFactory,     // Optional: Benutzerdefinierte Thread-Namensgebung oder Priorität
    rejectionHandler   // Aktion, wenn die Warteschlange voll und die max. Threads erreicht sind
);
```

#### Parameter-Übersicht
1. **`corePoolSize`**:
   - Minimale Anzahl der immer lebendig gehaltenen Threads.
   - Für CPU-gebundene Aufgaben: Auf die Anzahl der Kerne setzen (z. B. 8).
   - Für I/O-gebundene Aufgaben: Kann höher sein (z. B. 16 oder mehr), da Threads möglicherweise Wartezeit haben.

2. **`maximumPoolSize`**:
   - Maximale Threads, die erlaubt sind, wenn die Warteschlange voll ist.
   - Für CPU-gebunden: Oft gleich `corePoolSize` (z. B. 8).
   - Für I/O-gebunden: Höher, um Lastspitzen zu bewältigen (z. B. 20 oder 50).

3. **`keepAliveTime`**:
   - Wie lange überschüssige inaktive Threads (über `corePoolSize` hinaus) lebendig gehalten werden, bevor sie beendet werden.
   - Beispiel: `60L` Sekunden ist ein gängiger Standard.

4. **`workQueue`**:
   - Warteschlange für Aufgaben, die auf Ausführung warten:
     - `LinkedBlockingQueue`: Unbegrenzte Warteschlange (Standard in vielen Fällen).
     - `ArrayBlockingQueue`: Begrenzte Warteschlange (z. B. `new ArrayBlockingQueue<>(100)`).
     - `SynchronousQueue`: Keine Warteschlange; Aufgaben werden direkt an Threads übergeben (wird in `Executors.newCachedThreadPool()` verwendet).

5. **`threadFactory`** (Optional):
   - Passt die Thread-Erstellung an (z. B. Benennung von Threads zur Fehlersuche).
   - Standard: `Executors.defaultThreadFactory()`.

6. **`rejectionHandler`** (Optional):
   - Richtlinie, wenn Aufgaben `maximumPoolSize` und die Warteschlangenkapazität überschreiten:
     - `AbortPolicy` (Standard): Wirft `RejectedExecutionException`.
     - `CallerRunsPolicy`: Führt die Aufgabe im aufrufenden Thread aus.
     - `DiscardPolicy`: Verwirft die Aufgabe stillschweigend.

---

### Konfiguration für eine 8-Kern-CPU

#### Szenario 1: CPU-gebundene Aufgaben
Wenn Ihre Aufgaben CPU-intensiv sind (z. B. aufwändige Berechnungen), sollten Sie die Thread-Anzahl an die CPU-Kerne anpassen, um den Durchsatz zu maximieren, ohne das System zu überlasten.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // Entspricht 8 Kernen
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60 Sekunden

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // Unbegrenzte Warteschlange
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **Warum**: 8 Threads nutzen die 8 Kerne voll aus. Das Hinzufügen weiterer Threads würde Overhead durch Kontextwechsel verursachen und die Leistung verringern.

#### Szenario 2: I/O-gebundene Aufgaben (z. B. Datenbankvalidierung)
Für Ihr Validierungsszenario mit Datenbankzugriff sind die Aufgaben I/O-gebunden – Threads verbringen Zeit mit Warten auf Datenbankantworten. Sie können mehr Threads als Kerne verwenden, um die CPU beschäftigt zu halten, während einige Threads warten.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // 2x Kerne für I/O-gebundene Aufgaben
        int maximumPoolSize = 20; // Etwas Kapazität für Lastspitzen zulassen
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // Begrenzte Warteschlange, um Speicher zu begrenzen
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // Benutzerdefinierte Namensgebung
            new ThreadPoolExecutor.CallerRunsPolicy() // Fallback auf Aufrufer bei Überlastung
        );
    }
}
```

- **Warum**:
  - `corePoolSize = 16`: Eine gängige Heuristik für I/O-gebundene Aufgaben ist `N * 2` (wobei `N` die CPU-Kerne ist), aber dies kann basierend auf Datenbankverbindungslimits und Aufgaben-Wartezeiten angepasst werden.
  - `maximumPoolSize = 20`: Erlaubt zusätzliche Threads für Spitzenlasten.
  - `ArrayBlockingQueue(100)`: Verhindert unbegrenztes Wachstum der Aufgaben in der Warteschlange und vermeidet Speicherprobleme.
  - `CallerRunsPolicy`: Stellt sicher, dass das System bei Überlastung elegant degradiert, indem Aufgaben im Thread des Aufrufers ausgeführt werden.

#### Spring Boot Integration
In einer Spring Boot-Anwendung definieren Sie den `ExecutorService` als Bean:

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // I/O-gebundene Annahme für Validierung
        int maximumPoolSize = 20;
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100),
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(),
            new ThreadPoolExecutor.CallerRunsPolicy()
        );
    }
}
```

- **Hinweis**: Fügen Sie Guava (`com.google.guava:guava`) zu Ihren Abhängigkeiten hinzu für `ThreadFactoryBuilder`, oder verwenden Sie `Executors.defaultThreadFactory()`, wenn Sie keine benutzerdefinierte Namensgebung benötigen.

#### Verwendung in Ihrem Validation Service
Injecten und verwenden Sie ihn wie in Ihren früheren Beispielen gezeigt:

```java
@Service
public class ValidationService {
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    // Verwenden Sie ihn in CompletableFuture oder ExecutorService-Logik wie zuvor gezeigt
}
```

---

### Tuning-Tipps für 8-Kern-CPU

1. **Leistung messen**:
   - Verwenden Sie Profiling-Tools (z. B. VisualVM), um die Thread-Nutzung zu überwachen und `corePoolSize` und `maximumPoolSize` anzupassen.

2. **Datenbank-Limits**:
   - Wenn Regeln auf eine Datenbank zugreifen, stellen Sie sicher, dass die Thread-Pool-Größe die Größe Ihres Verbindungspools (z. B. HikariCPs `maximumPoolSize`) nicht überschreitet. Koordinieren Sie diese Einstellungen.

3. **Dynamische Berechnung**:
   - Verwenden Sie `Runtime.getRuntime().availableProcessors()`, um die Core Pool Size dynamisch zu setzen:
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // Gibt 8 auf einer 8-Kern-CPU zurück
     int corePoolSize = cores * 2; // Für I/O-gebundene Aufgaben
     ```

4. **Threads vorstarten**:
   - Rufen Sie `executor.prestartAllCoreThreads()` auf, um alle Core-Threads vorab zu initialisieren und verzögerte Erstellung zu vermeiden.

---

### Fazit

Für eine 8-Kern-CPU, die I/O-gebundene Aufgaben wie Ihre Validierungsregeln mit Datenbankzugriff ausführt:
- Verwenden Sie einen `ThreadPoolExecutor` mit `corePoolSize = 16`, `maximumPoolSize = 20` und einer begrenzten Warteschlange (z. B. `ArrayBlockingQueue(100)`).
- Integrieren Sie ihn als Spring Bean für Dependency Injection.
- Passen Sie die Einstellungen basierend auf Profiling und Datenbankbeschränkungen an.

Dieser Setup balanciert Parallelität, Ressourcennutzung und Systemstabilität und eignet sich daher gut für Ihren Anwendungsfall. Lassen Sie mich wissen, wenn Sie Hilfe bei der Integration in Ihr spezifisches Projekt benötigen!