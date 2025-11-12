---
audio: false
generated: true
lang: de
layout: post
title: Implementierung Multithread-Validierung mit CompletableFuture
translated: true
type: note
---

Wenn wir `CompletableFuture` in einer Spring Boot-Anwendung für eine mehrfädige Validierung verwenden, bietet es eine moderne, flexible Möglichkeit, asynchrone Aufgaben zu handhaben. Im Folgenden werde ich erklären, wie man es implementiert, seine Vorteile und Herausforderungen hervorheben und eine komplette Lösung vorstellen, die auf die gleichzeitige Validierung mehrerer Regeln zugeschnitten ist.

### Implementierung einer mehrfädigen Validierung mit CompletableFuture

`CompletableFuture` ist Teil der Java Concurrency API und erlaubt es Ihnen, Aufgaben asynchron auszuführen, Operationen zu verketten und Ergebnisse oder Ausnahmen elegant zu behandeln. So können wir es verwenden, um mehrere Regeln parallel zu validieren und abzubrechen, sobald eine fehlschlägt.

#### Schritt 1: Definieren der Validierungslogik

Nehmen wir zunächst an, wir haben einen Service, der individuelle Validierungsregeln definiert. Jede Regel könnte Datenbankzugriffe oder komplexe Logik beinhalten, daher verwenden wir die `@Transactional`-Annotation von Spring für ein korrektes Transaktionsmanagement.

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // Validierungslogik simulieren (z.B. Datenbankabfrage)
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // Beispiel: Gerade Regel-IDs bestehen, ungerade scheitern
        return ruleId % 2 == 0;
    }
}
```

#### Schritt 2: Implementierung des Validierungsservices mit CompletableFuture

Erstellen wir nun einen Service, der mehrere Validierungsregeln gleichzeitig mit `CompletableFuture` ausführt. Wir verwenden einen `ExecutorService`, um Threads zu verwalten und sicherzustellen, dass wir die Verarbeitung der anderen abbrechen können, falls eine Regel fehlschlägt.

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;

@Service
public class ValidationService {
    private static final Logger log = LoggerFactory.getLogger(ValidationService.class);
    private final ExecutorService executorService;
    private final RuleValidator ruleValidator;

    @Autowired
    public ValidationService(ExecutorService executorService, RuleValidator ruleValidator) {
        this.executorService = executorService;
        this.ruleValidator = ruleValidator;
    }

    public boolean validateAllRules() {
        // Liste für alle Futures erstellen
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // 10 Validierungsregeln einreichen (als Beispiel)
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validierung fehlgeschlagen für Regel " + ruleId, e);
                    return false; // Ausnahmen als Fehler behandeln
                }
            }, executorService);
            futures.add(future);
        }

        // Future zur Überwachung des Gesamtergebnisses erstellen
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // Jeden Future auf Fehler überwachen
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // Erster Fehler erkannt
                    resultFuture.complete(false);
                    // Verbleibende Aufgaben abbrechen
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // Wenn alle Futures erfolgreich abgeschlossen sind, als true markieren
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // Blockieren, bis Ergebnis verfügbar ist
        } catch (InterruptedException | ExecutionException e) {
            log.error("Fehler während der Validierung", e);
            return false;
        }
    }
}
```

#### So funktioniert es

1. **Aufgabeneinreichung**:
   - Wir erstellen für jede Regel ein `CompletableFuture` mit `supplyAsync()`, das die Validierungslogik asynchron ausführt.
   - Der `executorService` (via Spring injiziert) verwaltet den Thread-Pool.

2. **Fehlererkennung**:
   - Jeder Future wird mit `thenAccept()` überwacht. Wenn eine Regel `false` zurückgibt, schließen wir den `resultFuture` mit `false` ab und brechen die verbleibenden Futures ab.

3. **Erfolgsfall**:
   - `CompletableFuture.allOf()` wartet, bis alle Futures abgeschlossen sind. Wenn keine Fehler auftreten, schließt es den `resultFuture` mit `true` ab.

4. **Ergebnisabruf**:
   - Wir blockieren mit `resultFuture.get()`, um das Endergebnis zu erhalten, und behandeln alle auftretenden Ausnahmen.

### Vorteile der Verwendung von CompletableFuture

- **Flexibilität**: Sie können Operationen verketten (z.B. `thenApply`, `thenCompose`), um Ergebnisse bei Bedarf weiterzuverarbeiten.
- **Ausnahmebehandlung**: Eingebaute Methoden wie `exceptionally()` oder `handle()` erleichtern die Fehlerbehandlung.
- **Nicht-blockierendes Design**: Es unterstützt einen reaktiven Programmierstil, der für komplexere Workflows erweitert werden kann.

### Herausforderungen

- **Abbruch**: Im Gegensatz zu `ExecutorService` mit `CompletionService` (wo man leicht auf das erste Ergebnis warten und andere abbrechen kann), erfordert `CompletableFuture` einen manuellen Abbruch der anderen Futures, wenn einer fehlschlägt. Dies erhöht die Komplexität.
- **Komplexität**: Der Code kann im Vergleich zu einem einfacheren, schleifenbasierten Ansatz mit `ExecutorService` schwerer lesbar und wartbar werden.

### Beispiel zur Verwendung

Um dies in einer Spring Boot-Anwendung zu verwenden, konfigurieren Sie eine `ExecutorService`-Bean:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // Größe nach Bedarf anpassen
    }
}
```

Rufen Sie dann den Service von einem Controller oder einer anderen Komponente aus auf:

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
        return ResponseEntity.ok(result ? "Alle Regeln bestanden" : "Validierung fehlgeschlagen");
    }
}
```

### Schlussfolgerung

Die Verwendung von `CompletableFuture` für die mehrfädige Validierung in Spring Boot ist ein praktikabler Ansatz, insbesondere wenn Sie seine asynchrone, verkettene Natur schätzen. Es erlaubt Ihnen, Validierungsregeln gleichzeitig auszuführen und Ergebnisse flexibel zu handhaben. Wenn Ihr Hauptziel jedoch Einfachheit ist – insbesondere für die Erkennung des ersten Fehlers und den Abbruch verbleibender Aufgaben – könnte der traditionelle `ExecutorService` mit `CompletionService` einfacher zu implementieren und zu warten sein. Mit `CompletableFuture` gewinnen Sie Leistungsfähigkeit und Flexibilität auf Kosten einer etwas komplexeren Abbruchlogik.