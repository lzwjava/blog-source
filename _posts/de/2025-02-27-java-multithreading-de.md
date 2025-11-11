---
audio: false
generated: true
lang: de
layout: post
title: Java-Multithreading
translated: true
type: note
---

Lassen Sie uns in Java-Multithreading eintauchen und sehen, wie man das `Executor`-Framework effektiv nutzt. Multithreading ermöglicht es Ihrem Programm, mehrere Aufgaben gleichzeitig auszuführen und verbessert die Leistung bei E/A-lastigen oder CPU-intensiven Operationen. Das `Executor`-Framework vereinfacht die Thread-Verwaltung, indem es die Low-Level-Thread-Erstellung und -Handlung abstrahiert. Ich führe Sie durch die Grundlagen und zeige Ihnen dann, wie Sie `Executor` und verwandte Tools verwenden.

---

### 1. Grundlagen von Multithreading in Java
Java bietet zwei primäre Möglichkeiten, Threads zu erstellen:
- **Erweitern der `Thread`-Klasse**:

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread läuft: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // Startet den Thread
    }
}
```

- **Implementieren des `Runnable`-Interfaces**:

```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable läuft: " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

- Rufen Sie `start()` auf (nicht `run()`), um den Thread zu starten – `run()` führt den Code nur im aktuellen Thread aus.

---

### 2. Warum `Executor` verwenden?
Das manuelle Erstellen von Threads funktioniert für einfache Fälle, ist aber ineffizient für die Verwaltung vieler Aufgaben (z.B. Thread-Overhead, Ressourcenerschöpfung). Das `Executor`-Framework (eingeführt in Java 5 unter `java.util.concurrent`) bietet einen Thread-Pool und ein Task-Management-System, was Multithreading sauberer und skalierbarer macht.

---

### 3. Verwendung von `ExecutorService`
Die `ExecutorService`-Schnittstelle (eine Unter-Schnittstelle von `Executor`) ist das wichtigste Werkzeug. So verwenden Sie es:

#### Schritt 1: Einen ExecutorService erstellen
Verwenden Sie die `Executors`-Hilfsklasse, um einen Thread-Pool zu erstellen:
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // Fester Thread-Pool mit 4 Threads
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // Aufgaben einreichen
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Aufgabe ausgeführt von: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // Arbeit simulieren
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // Den Executor herunterfahren
        executor.shutdown(); // Verhindert neue Aufgaben, wartet auf Beendigung bestehender
    }
}
```
- `newFixedThreadPool(4)` erstellt einen Pool mit 4 Threads. Überschüssige Aufgaben warten in einer Warteschlange.
- `submit()` akzeptiert `Runnable`- oder `Callable`-Aufgaben (`Callable` gibt ein Ergebnis zurück).

#### Häufige Executor-Typen
- `Executors.newSingleThreadExecutor()`: Ein Thread, verarbeitet Aufgaben sequenziell.
- `Executors.newCachedThreadPool()`: Erstellt Threads bei Bedarf, wiederverwendet im Leerlauf befindliche (gut für kurzlebige Aufgaben).
- `Executors.newScheduledThreadPool(n)`: Zum Planen von Aufgaben mit Verzögerungen oder Periodizität.

---

### 4. Umgang mit Ergebnissen mittels `Callable` und `Future`
Wenn Sie Aufgabenergebnisse benötigen, verwenden Sie `Callable` anstelle von `Runnable`:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Eine Callable-Aufgabe einreichen
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // Andere Arbeit erledigen, während die Aufgabe läuft
        System.out.println("Aufgabe eingereicht...");

        // Ergebnis abrufen (blockiert bis zur Fertigstellung)
        Integer result = future.get();
        System.out.println("Ergebnis: " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` ruft das Ergebnis ab und blockiert, falls die Aufgabe noch nicht fertig ist.
- Verwenden Sie `future.isDone()`, um den Abschluss ohne Blockierung zu prüfen.

---

### 5. Fortgeschritten: Thread-Pool-Anpassung
Für reale Anwendungen möchten Sie möglicherweise einen benutzerdefinierten `ThreadPoolExecutor`:
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // Benutzerdefinierter Thread-Pool: 2-4 Threads, Warteschlangenkapazität von 10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // Kerngröße des Pools
            4, // Maximale Poolgröße
            60L, // Timeout für inaktive Threads
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // Aufgabenschlange
        );

        for (int i = 0; i < 15; i++) {
            executor.execute(() -> {
                System.out.println("Aufgabe von: " + Thread.currentThread().getName());
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        executor.shutdown();
    }
}
```
- Kerngröße (2): Minimale Anzahl an Threads, die aktiv gehalten werden.
- Max. Größe (4): Maximale Threads, wenn die Warteschlange voll ist.
- Warteschlange: Hält Aufgaben, wenn alle Threads beschäftigt sind.

---

### 6. Best Practices
- **Korrekt herunterfahren**: Rufen Sie immer `shutdown()` oder `shutdownNow()` auf, um Ressourcenlecks zu vermeiden.
- **Unterbrechungen behandeln**: Prüfen Sie `Thread.currentThread().isInterrupted()` in Schleifen.
- **Überlastung vermeiden**: Zu viele Threads können die Leistung beeinträchtigen – passen Sie die Poolgröße basierend auf CPU-Kernen an (z.B. `Runtime.getRuntime().availableProcessors()`).
- **Verwenden Sie `try-finally` mit `ExecutorService`**:
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // Aufgaben einreichen
} finally {
    executor.shutdown();
}
```

---

### Beispiel mit Log4j (Zusammenfügen)
Kombination von Multithreading mit Ihrer früheren Log4j-Frage:
```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import java.util.concurrent.*;

public class Main {
    private static final Logger logger = LogManager.getLogger(Main.class);

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(3);

        for (int i = 0; i < 5; i++) {
            final int taskId = i;
            executor.submit(() -> {
                logger.info("Aufgabe {} gestartet von {}", taskId, Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    logger.error("Aufgabe {} unterbrochen", taskId, e);
                    Thread.currentThread().interrupt();
                }
                logger.info("Aufgabe {} abgeschlossen", taskId);
            });
        }

        executor.shutdown();
    }
}
```
Mit der `log4j2.xml` von früher protokolliert dies den Aufgabenfortschritt in der Konsole und in einer Datei.