---
audio: false
generated: true
lang: de
layout: post
title: Ein Multithread-Fall
translated: true
type: note
---

Um die mehrfädige Validierung in einem Java Spring Boot-Projekt mit 10 Regeln zu handhaben, bei dem einige Regeln möglicherweise auf die Datenbank zugreifen und Sie die anderen abbrechen möchten, sobald eine fehlschlägt, um Zeitverschwendung zu vermeiden, können Sie die Concurrency Utilities von Java in Kombination mit den Features von Spring verwenden. Hier ist eine vollständige und effiziente Lösung:

### Ansatzübersicht
- **Validierungen parallel ausführen**: Verwenden Sie mehrere Threads, um die 10 Validierungsregeln parallel auszuführen und den Prozess zu beschleunigen, wenn alle Regeln erfolgreich sind.
- **Bei Fehlschlag abbrechen**: Brechen Sie die verbleibenden Validierungen sofort ab, sobald eine Regel fehlschlägt, um unnötige Arbeit zu minimieren.
- **Spring nutzen**: Nutzen Sie die Dependency Injection und Transaktionsverwaltung von Spring für datenbankzugreifende Regeln.

Der beste Weg, dies zu erreichen, ist die Verwendung eines `ExecutorService` in Kombination mit einem `CompletionService`. Der `CompletionService` ermöglicht es, die Ergebnisse von Tasks zu verarbeiten, sobald sie abgeschlossen sind, was die sofortige Erkennung eines Fehlschlags und den Abbruch ausstehender Tasks ermöglicht.

---

### Schritt-für-Schritt-Lösung

#### 1. Validierungsregeln definieren
Jede der 10 Regeln sollte eine unabhängige Validierungsaufgabe sein. Einige Regeln können Datenbankzugriffe beinhalten, daher kapseln Sie diese in einem Service mit transaktionalen Methoden.

```java
@Service
public class RuleValidator {
    // Beispiel: Regel, die auf die Datenbank zugreift
    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // Simuliere Regelvalidierung, z.B. Datenbankabfrage
        // Gib true zurück, wenn die Regel erfolgreich ist, false bei Fehlschlag
        return performValidation(ruleId); // Implementierung hängt von Ihrer Logik ab
    }

    private boolean performValidation(int ruleId) {
        // Ersetzen Sie dies durch die tatsächliche Validierungslogik
        return ruleId % 2 == 0; // Beispiel: Gerade Regel-IDs sind erfolgreich
    }
}
```

- Verwenden Sie `@Transactional(readOnly = true)` für Regeln, die nur aus der Datenbank lesen, um sicherzustellen, dass jede in ihrem eigenen Transaktionskontext auf thread-sichere Weise läuft.

#### 2. Einen ExecutorService konfigurieren
Definieren Sie einen Thread-Pool, um die parallele Ausführung der Validierungstasks zu verwalten. In Spring können Sie ihn als Bean erstellen:

```java
@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 10 Threads für 10 Regeln
    }
}
```

- Passen Sie die Größe des Thread-Pools basierend auf den Fähigkeiten Ihres Systems an (z.B. CPU-Kerne, Datenbankverbindungslimits).

#### 3. Mehrfädige Validierung implementieren
Erstellen Sie einen Service, der den Validierungsprozess unter Verwendung von `CompletionService` orchestriert:

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

    public boolean validateAllRules() {
        // Schritt 1: Validierungstasks erstellen
        List<Callable<Boolean>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            tasks.add(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    // Behandle Exceptions (z.B. Datenbankfehler) als Fehlschläge
                    log.error("Validation failed for rule " + ruleId, e);
                    return false;
                }
            });
        }

        // Schritt 2: CompletionService einrichten und Tasks übergeben
        CompletionService<Boolean> completionService = new ExecutorCompletionService<>(executorService);
        List<Future<Boolean>> futures = new ArrayList<>();
        for (Callable<Boolean> task : tasks) {
            futures.add(completionService.submit(task));
        }

        // Schritt 3: Ergebnisse verarbeiten, sobald sie abgeschlossen sind
        boolean hasFailed = false;
        for (int i = 0; i < 10; i++) {
            try {
                Future<Boolean> completed = completionService.take(); // Blockiert, bis nächster Task abgeschlossen ist
                boolean result = completed.get();
                if (!result) {
                    hasFailed = true;
                    break; // Stoppe die Überprüfung, sobald ein Fehlschlag gefunden wurde
                }
            } catch (InterruptedException | ExecutionException e) {
                log.error("Error during validation", e);
                hasFailed = true;
                break;
            }
        }

        // Schritt 4: Verbleibende Tasks abbrechen, wenn ein Fehlschlag aufgetreten ist
        if (hasFailed) {
            for (Future<Boolean> future : futures) {
                if (!future.isDone()) {
                    future.cancel(true); // Unterbricht laufende Tasks
                }
            }
            return false; // Validierung fehlgeschlagen
        }

        return true; // Alle Regeln erfolgreich
    }
}
```

#### So funktioniert es
- **Task-Erstellung**: Jede Validierungsregel wird in ein `Callable<Boolean>` eingepackt, das `true` zurückgibt, wenn die Regel erfolgreich ist, und `false` bei Fehlschlag. Exceptions werden abgefangen und als Fehlschläge behandelt.
- **Parallele Ausführung**: Tasks werden an den `CompletionService` übergeben, der sie parallel unter Verwendung des Thread-Pools ausführt. Futures werden gesammelt, um den Task-Status zu verfolgen.
- **Ergebnisverarbeitung**: `completionService.take()` ruft das Ergebnis des nächsten abgeschlossenen Tasks ab. Wenn ein Ergebnis `false` ist, bricht die Schleife ab und `hasFailed` wird gesetzt.
- **Abbruch**: Bei einem Fehlschlag werden alle unfertigen Tasks mit `future.cancel(true)` abgebrochen, was versucht, die laufenden Threads zu unterbrechen.
- **Ergebnis**: Gibt `false` zurück, wenn eine Regel fehlschlägt, `true` wenn alle erfolgreich sind.

---

### Wichtige Überlegungen
- **Datenbankzugriff**: Da Regeln auf die Datenbank zugreifen können, stellt `@Transactional` thread-sichere Operationen sicher. Jede Task läuft in ihrer eigenen Transaktion, was für unabhängige Validierungen angemessen ist.
- **Task-Abbruch**: Das Abbrechen eines `Future` unterbricht den Thread, aber laufende Datenbankabfragen stoppen möglicherweise nicht sofort. Dies verhindert jedoch die weitere Verarbeitung und ermöglicht es dem Hauptthread, fortzufahren.
- **Exception Handling**: Exceptions (z.B. Datenbankfehler) werden innerhalb der Tasks abgefangen und als Fehlschläge behandelt, was ein robustes Verhalten gewährleistet.
- **Thread-Pool-Größe**: Der Einfachheit halber auf 10 gesetzt (ein Thread pro Regel), aber optimieren Sie basierend auf den Anforderungen und Ressourcen Ihrer Anwendung.

---

### Warum dies der beste Ansatz ist
- **Effizienz**: Validierungen laufen parallel und reduzieren die Gesamtzeit, wenn alle erfolgreich sind.
- **Frühes Beenden**: `CompletionService` ermöglicht die sofortige Erkennung von Fehlschlägen, und der Abbruch stoppt unnötige Arbeit.
- **Einfachheit**: Nutzt standardmäßige Java Concurrency Utilities und integriert sich nahtlos mit Spring Boot.
- **Skalierbarkeit**: Leicht erweiterbar auf mehr Regeln durch Anpassen des Thread-Pools und der Task-Liste.

Alternative Ansätze wie `CompletableFuture` oder das Abfragen von `Future`-Ergebnissen mit Timeouts wurden in Betracht gezogen, aber `CompletionService` ist für diesen Anwendungsfall unkomplizierter, da es Ergebnisse in Abschlussreihenfolge effizient handhabt und Abbruch unterstützt.

---

### Anwendungsbeispiel
Injecten Sie den Service und rufen Sie ihn in Ihrem Controller oder Ihrer Geschäftslogik auf:

```java
@RestController
public class ValidationController {
    private final ValidationService validationService;

    @Autowired
    public ValidationController(ValidationService validationService) {
        this.validationService = validationService;
    }

    @GetMapping("/validate")
    public ResponseEntity<String> validate() {
        boolean result = validationService.validateAllRules();
        return ResponseEntity.ok(result ? "All rules passed" : "Validation failed");
    }
}
```

Diese Lösung erfüllt Ihre Anforderungen: Sie führt 10 Validierungsregeln parallel aus, bricht verbleibende Tasks bei einem Fehlschlag ab und vermeidet Zeitverschwendung, während sie sich sauber in Spring Boot integriert.