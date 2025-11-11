---
audio: false
generated: true
lang: fr
layout: post
title: Synchronisation des fils d'exécution en Java
translated: true
type: note
---

Plongeons dans la synchronisation des threads en Java ! Lorsque plusieurs threads accèdent à des ressources partagées (comme des variables, des collections ou des fichiers), vous devez empêcher les conditions de course — où les threads interfèrent les uns avec les autres, conduisant à des résultats imprévisibles. Java fournit plusieurs outils pour cela : `synchronized`, `Lock` et `Semaphore`. Je vais expliquer chacun, montrer des exemples et les comparer afin que vous puissiez choisir celui qui correspond à vos besoins.

---

### 1. Le mot-clé `synchronized`
Le mot-clé `synchronized` garantit qu'un seul thread peut exécuter un bloc de code ou une méthode à la fois. C'est l'outil de synchronisation le plus simple, intégré au cœur de Java.

#### Comment ça marche
- Verrouille le moniteur d'un objet (chaque objet Java en possède un).
- Les autres threads attendent jusqu'à ce que le verrou soit libéré.

#### Exemple : Compteur avec `synchronized`
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

        System.out.println("Final count: " + counter.getCount()); // Toujours 2000
    }
}
```
- Sans `synchronized`, `count++` (lecture-modification-écriture) pourrait se chevaucher, donnant un résultat inférieur à 2000.
- `synchronized` verrouille l'instance de `Counter`, garantissant des mises à jour atomiques.

#### Bloc Synchronized
Vous pouvez aussi verrouiller un code spécifique au lieu d'une méthode entière :
```java
public void increment() {
    synchronized (this) {
        count++;
    }
}
```
- Utilisez un objet différent comme verrou pour un contrôle plus fin :
```java
private final Object lock = new Object();
public void increment() {
    synchronized (lock) {
        count++;
    }
}
```

#### Avantages et Inconvénients
- **Avantages** : Simple, intégré au langage, bon pour les cas d'usage basiques.
- **Inconvénients** : Manque de flexibilité (ex. : impossible d'interrompre un thread en attente), bloque jusqu'à la libération.

---

### 2. L'interface `Lock` (java.util.concurrent.locks)
L'interface `Lock` (par ex., `ReentrantLock`) offre plus de contrôle que `synchronized`. Elle fait partie du package `java.util.concurrent` et a été introduite pour pallier les limitations de `synchronized`.

#### Fonctionnalités Clés
- Appels explicites `lock()` et `unlock()`.
- Prend en charge les essais de verrouillage (try-lock), les timeouts et le verrouillage interruptible.
- Option d'équité (les threads attendent dans l'ordre).

#### Exemple : Compteur avec `ReentrantLock`
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
            lock.unlock(); // Toujours déverrouiller dans finally
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

        System.out.println("Final count: " + counter.getCount()); // Toujours 2000
    }
}
```
- `try-finally` garantit que le verrou est libéré même si une exception se produit.

#### Fonctionnalités Avancées
- **Try Lock** : Tentative non bloquante d'acquisition du verrou :
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
- **Timeout** : Attendre pendant un temps limité :
```java
if (lock.tryLock(1, TimeUnit.SECONDS)) { ... }
```
- **Interruptible** : Permet d'interrompre les threads en attente :
```java
lock.lockInterruptibly();
```

#### Avantages et Inconvénients
- **Avantages** : Flexible, prend en charge les fonctionnalités avancées, contrôle explicite.
- **Inconvénients** : Plus verbeux, déverrouillage manuel requis (risque d'oubli).

---

### 3. `Semaphore`
Un `Semaphore` contrôle l'accès à une ressource en maintenant un ensemble de permis. Il est excellent pour limiter la concurrence (ex. : max 5 threads peuvent accéder à une ressource).

#### Comment ça marche
- Les threads acquièrent des permis avec `acquire()`.
- Libèrent des permis avec `release()`.
- Si aucun permis n'est disponible, les threads attendent.

#### Exemple : Limitation des connexions à une base de données
```java
import java.util.concurrent.Semaphore;

class ConnectionPool {
    private final Semaphore semaphore = new Semaphore(3); // Max 3 connexions

    public void connect() {
        try {
            semaphore.acquire();
            System.out.println(Thread.currentThread().getName() + " connected");
            Thread.sleep(1000); // Simule un travail
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
- Seulement 3 threads peuvent se "connecter" à la fois ; les autres attendent qu'un permis soit libéré.

#### Fonctionnalités Avancées
- **Équité** : `new Semaphore(3, true)` garantit l'ordre FIFO.
- **Try Acquire** : `semaphore.tryAcquire()` vérifie sans bloquer.

#### Avantages et Inconvénients
- **Avantages** : Idéal pour les pools de ressources, système de permis flexible.
- **Inconvénients** : Plus complexe que `synchronized` ou `Lock`, pas pour l'exclusion mutuelle simple.

---

### Combinaison avec `ExecutorService`
Voici comment ces outils fonctionnent avec un pool de threads :
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
        System.out.println("Final value: " + resource.getValue()); // Toujours 1000
    }
}
```

---

### Comparaison

| Fonctionnalité     | `synchronized`       | `Lock` (ReentrantLock) | `Semaphore`         |
|--------------------|----------------------|------------------------|---------------------|
| Facilité d'utilisation | Élevée          | Moyenne                | Faible             |
| Flexibilité        | Faible              | Élevée                 | Moyenne            |
| Granularité        | Méthode/bloc        | Explicite              | Basé sur les permis |
| Interruptible      | Non                 | Oui                    | Oui                |
| Option d'équité    | Non                 | Oui                    | Oui                |
| Cas d'utilisation  | Exclusion mutuelle simple | Contrôle avancé | Limitation de ressources |

---

### Quand utiliser quoi ?
- **`synchronized`** : Exclusion mutuelle rapide et simple (ex. : protéger une variable unique).
- **`Lock`** : Besoin d'essais de verrouillage, de timeouts ou d'interruptibilité (ex. : workflows complexes).
- **`Semaphore`** : Limiter l'accès concurrent à une ressource (ex. : pools de connexions, limitation de débit).