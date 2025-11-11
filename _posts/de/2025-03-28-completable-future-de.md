---
audio: false
generated: true
lang: de
layout: post
title: CompletableFuture in Java
translated: true
type: note
---

In einem Java Spring Boot Projekt gibt es keine direkte Entsprechung zu JavaScripts `Promise.all`, das auf mehrere Promises wartet und deren Ergebnisse bereitstellt. Sie können jedoch eine ähnliche Funktionalität erreichen – das gleichzeitige Ausführen mehrerer Aufgaben in einer for-Schleife und die Verwendung ihrer Ergebnisse nach Abschluss aller Threads – indem Sie `CompletableFuture` aus dem `java.util.concurrent`-Paket verwenden, insbesondere mit der Methode `CompletableFuture.allOf`. Dieser Ansatz eignet sich gut für ein Spring Boot Projekt, insbesondere in Kombination mit den asynchronen Programmierfunktionen von Spring. Im Folgenden werde ich Schritt für Schritt erklären, wie Sie dies tun, einschließlich eines vollständigen Beispiels.

### Warum `CompletableFuture`?
`CompletableFuture` (eingeführt in Java 8) ermöglicht es Ihnen, asynchrone Operationen durchzuführen und deren Abschluss zu verwalten. Die Methode `allOf` nimmt mehrere `CompletableFuture`-Instanzen entgegen und gibt ein neues `CompletableFuture` zurück, das abgeschlossen wird, wenn alle angegebenen Futures fertig sind. Dies macht es ideal für Ihr Szenario, in dem Sie möchten:
- Aufgaben parallel innerhalb einer for-Schleife ausführen.
- Warten, bis alle Aufgaben beendet sind.
- Die Ergebnisse anschließend verwenden.

### Schritte zur Implementierung
So können Sie Ihre Lösung in einem Spring Boot Projekt strukturieren:

1. **Definieren der asynchronen Aufgaben**  
   Jede Iteration Ihrer for-Schleife stellt eine Aufgabe dar, die unabhängig ausgeführt werden kann. Diese Aufgaben geben `CompletableFuture`-Instanzen zurück, die ihre eventuellen Ergebnisse repräsentieren.

2. **Sammeln der Futures**  
   Speichern Sie alle `CompletableFuture`-Objekte in einer Liste, während Sie sie in der Schleife erstellen.

3. **Auf den Abschluss aller Aufgaben warten**  
   Verwenden Sie `CompletableFuture.allOf`, um die Futures zu einem einzigen Future zu kombinieren, der abgeschlossen wird, wenn alle Aufgaben fertig sind.

4. **Ergebnisse abrufen und verwenden**  
   Nachdem alle Aufgaben abgeschlossen sind, extrahieren Sie die Ergebnisse aus jedem `CompletableFuture` und verarbeiten Sie sie nach Bedarf.

5. **Ausnahmen behandeln**  
   Berücksichtigen Sie potenzielle Fehler während der Aufgabenausführung.

### Beispielimplementierung
Nehmen wir an, Sie haben eine Liste von Elementen, die Sie parallel verarbeiten möchten (z.B. Aufruf eines Services oder Durchführung einer Berechnung). Hier sind zwei Ansätze: einer verwendet die `@Async`-Annotation von Spring und ein anderer verwendet `CompletableFuture.supplyAsync`.

#### Ansatz 1: Verwenden von `@Async` mit Spring
Spring Boot bietet die Annotation `@Async`, um Methoden asynchron auszuführen. Sie müssen die Async-Unterstützung in Ihrer Anwendung aktivieren.

**Schritt 1: Async-Unterstützung aktivieren**
Fügen Sie die Annotation `@EnableAsync` zu einer Konfigurationsklasse oder Ihrer Hauptanwendungsklasse hinzu:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableAsync;

@SpringBootApplication
@EnableAsync
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

**Schritt 2: Definieren eines Services mit einer Async-Methode**
Erstellen Sie einen Service mit einer Methode, die jedes Element asynchron verarbeitet:

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // Simuliere einige Arbeit (z.B. I/O oder Berechnung)
        try {
            Thread.sleep(1000); // 1 Sekunde Verzögerung
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**Schritt 3: Elemente in einem Controller oder Service verarbeiten**
Verwenden Sie in Ihrem Controller oder einem anderen Service eine for-Schleife, um Aufgaben zu übermitteln und auf alle Ergebnisse zu warten:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.concurrent.CompletableFuture;

@Component
public class ItemProcessor {

    @Autowired
    private MyService myService;

    public List<String> processItems(List<String> items) {
        // Liste zum Halten aller Futures
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // Übermittle jede Aufgabe in der for-Schleife
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // Warte auf den Abschluss aller Aufgaben
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // Blockiere, bis alle Aufgaben erledigt sind
        allFutures.join();

        // Sammle Ergebnisse
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // Hole jedes Ergebnis
            .collect(Collectors.toList());

        return results;
    }
}
```

**Verwendungsbeispiel:**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // Druckt: [Processed: Item1, Processed: Item2, Processed: Item3]
```

#### Ansatz 2: Verwenden von `CompletableFuture.supplyAsync`
Wenn Sie `@Async` nicht verwenden möchten, können Sie Threads manuell mit einem `Executor` und `CompletableFuture.supplyAsync` verwalten.

**Schritt 1: Einen Thread-Pool konfigurieren**
Definieren Sie eine `TaskExecutor`-Bean, um den Thread-Pool zu steuern:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;
import org.springframework.core.task.TaskExecutor;

@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);    // Anzahl der Threads, die im Pool gehalten werden
        executor.setMaxPoolSize(10);    // Maximale Anzahl von Threads
        executor.setQueueCapacity(25);  // Warteschlangenkapazität für anstehende Aufgaben
        executor.initialize();
        return executor;
    }
}
```

**Schritt 2: Elemente mit `supplyAsync` verarbeiten**
Verwenden Sie den Executor, um Aufgaben asynchron auszuführen:

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.stream.Collectors;
import org.springframework.core.task.TaskExecutor;

@Component
public class ItemProcessor {

    @Autowired
    private TaskExecutor taskExecutor;

    public List<String> processItems(List<String> items) {
        // Erstelle Futures mit supplyAsync
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // Warte auf den Abschluss aller Aufgaben
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // Sammle Ergebnisse
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // Simuliere einige Arbeit
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return "Interrupted: " + item;
        }
        return "Processed: " + item;
    }
}
```

### Wichtige Punkte
- **Warten auf Abschluss**: `CompletableFuture.allOf(...).join()` oder `.get()` stellt sicher, dass der Hauptthread wartet, bis alle Aufgaben beendet sind. Verwenden Sie `join()`, um die Behandlung geprüfter Ausnahmen zu vermeiden; es wirft `CompletionException`, wenn eine Aufgabe fehlschlägt.
- **Ausnahmebehandlung**: Wickeln Sie den `.join()` oder `.get()`-Aufruf in einen try-catch-Block, wenn Sie Ausnahmen behandeln müssen:

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // Unterbrechung behandeln
} catch (ExecutionException e) {
    // Aufgabenfehler behandeln
    e.printStackTrace();
}
```

- **Thread-Pool-Konfiguration**: Passen Sie die Thread-Pool-Größe basierend auf Ihrer Arbeitslast an. Für I/O-gebundene Aufgaben (z.B. Datenbankaufrufe, API-Anfragen) ist ein größerer Pool (z.B. 5–10 Threads) in Ordnung. Für CPU-gebundene Aufgaben passen Sie die Anzahl der CPU-Kerne an (z.B. `Runtime.getRuntime().availableProcessors()`).
- **Reihenfolge der Ergebnisse**: Die Ergebnisse behalten die Reihenfolge der Eingabeliste, da Futures in derselben Reihenfolge wie die Schleife gesammelt werden.

### Welchen Ansatz sollten Sie wählen?
- **Verwenden Sie `@Async`**, wenn Ihre Aufgaben natürlicherweise Teil eines Spring-Services sind und Sie möchten, dass Spring das Threading verwaltet. Es ist sauberer und integriert sich gut mit Spring Boot.
- **Verwenden Sie `supplyAsync`**, wenn Sie mehr Kontrolle über die Aufgabenausführung benötigen oder sich nicht auf Springs Async-Framework verlassen möchten.

### Endgültige Antwort
Um `Promise.all` in einem Java Spring Boot Projekt für einen For-Schleifen-Job zu replizieren, bei dem Sie Thread-Ergebnisse nach einer Multithread-Ausführung verwenden möchten, verwenden Sie `CompletableFuture.allOf` mit einer Liste von `CompletableFuture`-Instanzen. Der `@Async`-Ansatz mit Spring wird für Einfachheit empfohlen, aber `supplyAsync` mit einem benutzerdefinierten Executor funktioniert ebenfalls. Das obige Beispiel mit `@Async` demonstriert dies:

- Erstellen Sie `CompletableFuture`-Instanzen in einer for-Schleife unter Verwendung einer `@Async`-Methode.
- Verwenden Sie `CompletableFuture.allOf`, um auf alle Aufgaben zu warten.
- Sammeln und verwenden Sie die Ergebnisse nach Abschluss.

Dies stellt sicher, dass alle Aufgaben gleichzeitig ausgeführt werden, und Sie können ihre Ergebnisse verarbeiten, sobald sie alle fertig sind, was Ihre Anforderungen effektiv erfüllt.