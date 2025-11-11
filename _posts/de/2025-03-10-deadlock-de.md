---
audio: false
generated: true
lang: de
layout: post
title: Deadlock in Spring Boot
translated: true
type: note
---

Lassen Sie uns die Lösung eines Deadlock-Problems in einem Spring Boot-Projekt angehen, wenn mehrere Anfragen gleichzeitig auf eine Methode eines Beans treffen. Deadlocks treten auf, wenn sich zwei oder mehr Threads gegenseitig blockieren, oft aufgrund des Wettbewerbs um gemeinsam genutzte Ressourcen wie Datenbanksperren, synchronisierte Blöcke oder thread-sichere Datenstrukturen. Da Sie eine Methode eines Beans erwähnt haben, die viele Anfragen verarbeitet, gehe ich davon aus, dass es sich um einen Singleton-scoped Bean (der Standard-Scope von Spring) handelt, und untersuche häufige Ursachen und Lösungen.

Zuerst identifizieren wir mögliche Deadlock-Szenarien in diesem Kontext:
1.  **Datenbanksperren**: Wenn die Methode des Beans mit einer Datenbank interagiert (z.B. über JPA/Hibernate), könnten gleichzeitige Transaktionen Zeilen oder Tabellen in widersprüchlicher Reihenfolge sperren.
2.  **Synchronisierte Blöcke**: Wenn die Methode das `synchronized`-Schlüsselwort oder Locks (z.B. `ReentrantLock`) verwendet, könnte eine falsche Sperrreihenfolge dazu führen, dass Threads aufeinander warten.
3.  **Gemeinsam genutzte Ressourcen**: Wenn der Bean eine gemeinsam genutzte In-Memory-Ressource (z.B. eine statische Variable oder Sammlung) ändert, könnte Contention zu Deadlocks führen.
4.  **Externe Aufrufe**: Wenn die Methode externe Dienste oder APIs aufruft, könnten Verzögerungen oder blockierendes Verhalten Nebenläufigkeitsprobleme verschlimmern.

Da Sie keinen spezifischen Code geteilt haben, liefere ich einen allgemeinen Ansatz zur Diagnose und Behebung des Problems, gefolgt von einem konkreten Beispiel.

### Schritt 1: Den Deadlock diagnostizieren
-   **Logging aktivieren**: Fügen Sie Logging (z.B. SLF4J mit Logback) hinzu, um den Methodeneintritt, -austritt und Ressourcenzugriff zu verfolgen. Dies hilft zu identifizieren, wo Threads hängen bleiben.
-   **Thread-Dump**: Wenn der Deadlock auftritt, erfassen Sie einen Thread-Dump (z.B. mit `jstack` oder VisualVM). Suchen Sie nach Threads in `BLOCKED`- oder `WAITING`-Zuständen und prüfen Sie ihre Stack-Traces auf Lock-Contention.
-   **Monitoring**: Verwenden Sie Tools wie Spring Actuator oder einen Profiler (z.B. YourKit), um das Thread-Verhalten unter Last zu beobachten.

### Schritt 2: Häufige Lösungen
So beheben Sie den Deadlock basierend auf wahrscheinlichen Ursachen:

#### Fall 1: Datenbankbezogener Deadlock
Wenn die Methode des Beans Datenbankoperationen durchführt, entstehen Deadlocks oft durch Transaktionskonflikte.
-   **Lösung**: Optimieren Sie Transaktionsgrenzen und die Sperrreihenfolge.
    -   Verwenden Sie `@Transactional` mit einem geeigneten Isolationslevel (z.B. `READ_COMMITTED` anstelle von `SERIALIZABLE`, es sei denn, es ist unbedingt erforderlich).
    -   Stellen Sie eine konsistente Reihenfolge des Ressourcenzugriffs sicher (z.B. immer Tabelle A vor Tabelle B aktualisieren).
    -   Reduzieren Sie den Transaktionsumfang, indem Sie nicht-transaktionale Logik außerhalb von `@Transactional` verschieben.
-   **Beispiel**:
    ```java
    @Service
    public class MyService {
        @Autowired
        private MyRepository repo;

        @Transactional
        public void processRequest(Long id1, Long id2) {
            // Konsistente Reihenfolge sicherstellen, um Deadlock zu vermeiden
            if (id1 < id2) {
                repo.updateEntity(id1);
                repo.updateEntity(id2);
            } else {
                repo.updateEntity(id2);
                repo.updateEntity(id1);
            }
        }
    }
    ```
-   **Bonus**: Setzen Sie ein Transaktion-Timeout (z.B. `@Transactional(timeout = 5)`), um langlaufende Transaktionen abzubrechen und indefinite Wartezeiten zu verhindern.

#### Fall 2: Synchronisierte Blöcke oder Locks
Wenn die Methode explizite Sperren verwendet, können Deadlocks auftreten, wenn Sperren in unterschiedlicher Reihenfolge über Threads hinweg erworben werden.
-   **Lösung**: Verwenden Sie eine einzelne Sperre oder erzwingen Sie eine Sperrreihenfolge.
    -   Ersetzen Sie mehrere `synchronized`-Blöcke durch eine einzige grobgranulare Sperre, falls möglich.
    -   Verwenden Sie `ReentrantLock` mit einem Timeout, um indefinite Blockierung zu vermeiden.
-   **Beispiel**:
    ```java
    @Service
    public class MyService {
        private final ReentrantLock lock = new ReentrantLock();

        public void processRequest(String resourceA, String resourceB) {
            try {
                if (lock.tryLock(2, TimeUnit.SECONDS)) {
                    // Kritischer Abschnitt
                    System.out.println("Processing " + resourceA + " and " + resourceB);
                } else {
                    throw new RuntimeException("Could not acquire lock in time");
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            } finally {
                if (lock.isHeldByCurrentThread()) {
                    lock.unlock();
                }
            }
        }
    }
    ```

#### Fall 3: Gemeinsam genutzte In-Memory-Ressourcen
Wenn der Bean eine gemeinsame Sammlung oder Variable ändert, könnte gleichzeitiger Zugriff Probleme verursachen.
-   **Lösung**: Verwenden Sie thread-sichere Alternativen oder vermeiden Sie gemeinsamen Zustand.
    -   Ersetzen Sie `ArrayList` durch `CopyOnWriteArrayList` oder `Collections.synchronizedList`.
    -   Verwenden Sie `ConcurrentHashMap` für Maps.
    -   Noch besser: Machen Sie den Bean zustandslos oder verwenden Sie Request-scoped Beans (`@Scope("request")`).
-   **Beispiel**:
    ```java
    @Service
    @Scope("prototype") // Singleton vermeiden, wenn zustandsbehaftet
    public class MyService {
        private final ConcurrentHashMap<String, Integer> cache = new ConcurrentHashMap<>();

        public void processRequest(String key, int value) {
            cache.put(key, value); // Thread-sicher
        }
    }
    ```

#### Fall 4: Hohe Nebenläufigkeitslast
Wenn der Deadlock von der Überlastung des Beans mit Anfragen herrührt, könnte Thread-Contention die Ursache sein.
-   **Lösung**: Führen Sie asynchrone Verarbeitung oder Ratenbegrenzung ein.
    -   Verwenden Sie `@Async`, um Arbeit an einen Thread-Pool auszulagern.
    -   Konfigurieren Sie einen Thread-Pool mit `TaskExecutor`, um die Nebenläufigkeit zu verwalten.
-   **Beispiel**:
    ```java
    @Service
    public class MyService {
        @Async
        public CompletableFuture<String> processRequest(String input) {
            // Arbeit simulieren
            Thread.sleep(1000);
            return CompletableFuture.completedFuture("Done: " + input);
        }
    }

    @Configuration
    @EnableAsync
    public class AsyncConfig {
        @Bean
        public TaskExecutor taskExecutor() {
            ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
            executor.setCorePoolSize(10);
            executor.setMaxPoolSize(50);
            executor.setQueueCapacity(100);
            return executor;
        }
    }
    ```
-   **Verwendung**: Rufen Sie `processRequest` auf und behandeln Sie die `CompletableFuture` im Controller.

### Schritt 3: Zukünftige Probleme verhindern
-   **Lasttests**: Simulieren Sie hohe Nebenläufigkeit mit Tools wie JMeter oder Gatling, um Deadlocks frühzeitig zu erkennen.
-   **Code-Review**: Überprüfen Sie den Code auf verschachtelte Sperren, langlaufende Transaktionen oder gemeinsamen veränderlichen Zustand.
-   **Timeouts**: Setzen Sie immer Timeouts für Sperren, Transaktionen oder externe Aufrufe.

### Abschließende Gedanken
Ohne den Code Ihres Beans gesehen zu haben, bin ich von einem Singleton-Bean unter hoher Last mit potenzieller Datenbank- oder Lock-Contention ausgegangen. Wenn Sie mehr Details teilen (z.B. den Code der Methode, Stack Traces oder auf welche Ressourcen sie zugreift), kann ich die Lösung weiter anpassen. Beginnen Sie vorerst mit der Diagnose mittels eines Thread-Dumps und wenden Sie die relevante Lösung an – Datenbankoptimierung, Lock-Management oder asynchrone Verarbeitung. Lassen Sie mich wissen, wie es läuft!