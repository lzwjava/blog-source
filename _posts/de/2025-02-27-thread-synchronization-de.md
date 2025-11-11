---
audio: false
generated: true
lang: de
layout: post
title: Thread-Synchronisation in Java
translated: true
type: note
---

Lassen Sie uns in die Thread-Synchronisation in Java eintauchen! Wenn mehrere Threads auf gemeinsam genutzte Ressourcen (wie Variablen, Collections oder Dateien) zugreifen, müssen Sie Race Conditions verhindern – Situationen, in denen Threads sich gegenseitig stören und zu unvorhersehbaren Ergebnissen führen. Java bietet mehrere Werkzeuge dafür: `synchronized`, `Lock` und `Semaphore`. Ich werde jedes erklären, Beispiele zeigen und sie vergleichen, damit Sie das richtige für Ihre Bedürfnisse auswählen können.

---

### 1. `synchronized` Schlüsselwort
Das `synchronized` Schlüsselwort stellt sicher, dass nur ein Thread einen Codeblock oder eine Methode gleichzeitig ausführen kann. Es ist das einfachste Synchronisationswerkzeug und in Javas Kern integriert.

#### So funktioniert es
- Sperrt den Monitor eines Objekts (jedes Java-Objekt hat einen).
- Andere Threads warten, bis die Sperre freigegeben wird.

#### Beispiel: Zähler mit `synchronized`
```java
class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // Immer 2000
    }
}
```
- Ohne `synchronized` könnte `count++` (Lesen-Modifizieren-Schreiben) sich überlappen, was ein Ergebnis von weniger als 2000 zur Folge hätte.
- `synchronized` sperrt die `Counter`-Instanz und stellt atomare Updates sicher.

#### Synchronisierter Block
Sie können auch spezifischen Code anstelle einer ganzen Methode sperren:
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- Verwenden Sie ein anderes Objekt als Sperre, wenn Sie feinere Kontrolle wünschen:
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### Vor- und Nachteile
- **Vorteile**: Einfach, integriert, gut für grundlegende Anwendungen.
- **Nachteile**: Keine Flexibilität (z.B. kann ein wartender Thread nicht unterbrochen werden), blockiert bis zur Freigabe.

---

### 2. `Lock` Interface (java.util.concurrent.locks)
Das `Lock` Interface (z.B. `ReentrantLock`) bietet mehr Kontrolle als `synchronized`. Es ist Teil des `java.util.concurrent` Pakets und wurde eingeführt, um die Einschränkungen von `synchronized` zu adressieren.

#### Wichtige Merkmale
- Explizite `lock()` und `unlock()` Aufrufe.
- Unterstützt Try-Locks, Timeouts und unterbrechbare Sperren.
- Fairness-Option (Threads warten in der Reihenfolge).

#### Beispiel: Zähler mit `ReentrantLock`
```java
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class Counter {
    private int count = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock(); // Immer im finally-Block freigeben
        }
    }

    public int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        Runnable task = () -> {
            for (int i = 0; i < 1000; i++) {
                counter.increment();
            }
        };

        Thread t1 = new Thread(task);
        Thread t2 = new Thread(task);
        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Final count: " + counter.getCount()); // Immer 2000
    }
}
```
- `try-finally` stellt sicher, dass die Sperre auch bei einer Ausnahme freigegeben wird.

#### Erweiterte Funktionen
- **Try Lock**: Nicht-blockierender Versuch, die Sperre zu erlangen:
```java
if (lock.tryLock()) {
    try {
        count++;
    } finally {
        lock.unlock();
    }
} else {
    System.out.println("Couldn’t acquire lock");
}
```
- **Timeout**: Warte für eine begrenzte Zeit:
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **Unterbrechbar**: Erlaubt es wartenden Threads, unterbrochen zu werden:
```java
lock.lockInterruptibly();
```

#### Vor- und Nachteile
- **Vorteile**: Flexibel, unterstützt erweiterte Funktionen, explizite Kontrolle.
- **Nachteile**: Ausführlicher, manuelle Freigabe erforderlich (Risiko des Vergessens).

---

### 3. `Semaphore`
Ein `Semaphore` kontrolliert den Zugriff auf eine Ressource, indem er eine Reihe von Permits (Berechtigungen) verwaltet. Es ist ideal, um Parallelität zu begrenzen (z.B. max. 5 Threads können auf eine Ressource zugreifen).

#### So funktioniert es
- Threads erwerben Permits mit `acquire()`.
- Geben Permits mit `release()` frei.
- Wenn keine Permits verfügbar sind, warten Threads.

#### Beispiel: Begrenzung von Datenbankverbindungen
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // Max 3 Verbindungen

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " connected");
            Thread.sleep(1000); // Arbeit simulieren
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            semaphore.release();
            System.out.println(Thread.currentThread().getName() + " disconnected");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        ConnectionPool pool = new ConnectionPool();
        Runnable task = () -> pool.connect();

        Thread[] threads = new Thread[10];
        for (int i = 0; i < 10; i++) {
            threads[i] = new Thread(task, "Thread-" + i);
            threads[i].start();
        }
    }
}
```
- Nur 3 Threads können gleichzeitig "verbinden"; andere warten, bis ein Permit freigegeben wird.

#### Erweiterte Funktionen
- **Fairness**: `new Semaphore(3, true)` stellt FIFO-Reihenfolge sicher.
- **Try Acquire**: `semaphore.tryAcquire()` überprüft, ohne zu blockieren.

#### Vor- und Nachteile
- **Vorteile**: Ideal für Ressourcen-Pools, flexibles Permit-System.
- **Nachteile**: Komplexer als `synchronized` oder `Lock`, nicht für einfachen gegenseitigen Ausschluss.

---

### Kombination mit `ExecutorService`
So arbeiten diese Werkzeuge mit einem Thread-Pool:
```java
import java.util.concurrent.*;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

class SharedResource {
    private int value = 0;
    private final Lock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            value++;
        } finally {
            lock.unlock();
        }
    }

    public int getValue() {
        return value;
    }
}

public class Main {
    public static void main(String[] args) throws InterruptedException {
        SharedResource resource = new SharedResource();
        ExecutorService executor = Executors.newFixedThreadPool(4);

        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                for (int j = 0; j < 100; j++) {
                    resource.increment();
                }
            });
        }

        executor.shutdown();
        executor.awaitTermination(5, TimeUnit.SECONDS);
        System.out.println("Final value: " + resource.getValue()); // Immer 1000
    }
}
```

---

### Vergleich

| Merkmal            | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| Einfachheit        | Hoch                | Mittel                 | Niedrig            |
| Flexibilität       | Niedrig             | Hoch                   | Mittel             |
| Granularität       | Methode/Block       | Explizit               | Permit-basiert     |
| Unterbrechbar      | Nein                | Ja                     | Ja                 |
| Fairness-Option    | Nein                | Ja                     | Ja                 |
| Anwendungsfall     | Einfacher gegenseitiger Ausschluss | Erweiterte Kontrolle | Ressourcenbegrenzung |

---

### Wann verwende ich was?
- **`synchronized`**: Schneller, einfacher gegenseitiger Ausschluss (z.B. zum Schutz einer einzelnen Variable).
- **`Lock`**: Bei Bedarf für Try-Locks, Timeouts oder Unterbrechbarkeit (z.B. komplexe Workflows).
- **`Semaphore`**: Zum Begrenzen des gleichzeitigen Zugriffs auf eine Ressource (z.B. Verbindungspools, Ratenbegrenzung).