---
audio: false
generated: true
lang: fr
layout: post
title: Programmation Java Multithread
translated: true
type: note
---

Plongeons dans le multithreading Java et découvrons comment utiliser efficacement le framework `Executor`. Le multithreading permet à votre programme d'exécuter plusieurs tâches simultanément, améliorant les performances pour les opérations liées aux E/S ou intensives en calcul processeur. Le framework `Executor` simplifie la gestion des threads en abstraisant la création et la gestion de bas niveau. Je vais vous guider à travers les bases, puis vous montrer comment utiliser `Executor` et les outils associés.

---

### 1. Bases du Multithreading en Java
Java fournit deux méthodes principales pour créer des threads :
- **Étendre la classe `Thread`** :

```java
class MyThread extends Thread {
    public void run() {
        System.out.println("Thread en cours d'exécution : " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start(); // Démarre le thread
    }
}
```

- **Implémenter l'interface `Runnable`** :

```java
class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Runnable en cours d'exécution : " + Thread.currentThread().getName());
    }
}

public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

- Appelez `start()` (et non `run()`) pour lancer le thread—`run()` exécute simplement le code dans le thread actuel.

---

### 2. Pourquoi Utiliser `Executor` ?
Créer des threads manuellement fonctionne pour des cas simples, mais c'est inefficace pour gérer de nombreuses tâches (par exemple, surcharge des threads, épuisement des ressources). Le framework `Executor` (introduit dans Java 5 sous `java.util.concurrent`) fournit un pool de threads et un système de gestion des tâches, rendant le multithreading plus propre et plus évolutif.

---

### 3. Utilisation de `ExecutorService`
L'interface `ExecutorService` (une sous-interface de `Executor`) est l'outil principal. Voici comment l'utiliser :

#### Étape 1 : Créer un ExecutorService
Utilisez la classe utilitaire `Executors` pour créer un pool de threads :
```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        // Pool de threads fixe avec 4 threads
        ExecutorService executor = Executors.newFixedThreadPool(4);

        // Soumettre des tâches
        for (int i = 0; i < 10; i++) {
            executor.submit(() -> {
                System.out.println("Tâche exécutée par : " + Thread.currentThread().getName());
                try {
                    Thread.sleep(1000); // Simule un travail
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            });
        }

        // Arrêter l'executor
        executor.shutdown(); // Empêche les nouvelles tâches, attend la fin des existantes
    }
}
```
- `newFixedThreadPool(4)` crée un pool avec 4 threads. Les tâches excédentaires attendent dans une file d'attente.
- `submit()` accepte des tâches `Runnable` ou `Callable` (`Callable` renvoie un résultat).

#### Types d'Executor Courants
- `Executors.newSingleThreadExecutor()` : Un seul thread, traite les tâches séquentiellement.
- `Executors.newCachedThreadPool()` : Crée des threads selon les besoins, réutilise ceux inactifs (bon pour les tâches de courte durée).
- `Executors.newScheduledThreadPool(n)` : Pour planifier des tâches avec des délais ou une périodicité.

---

### 4. Gérer les Résultats avec `Callable` et `Future`
Si vous avez besoin des résultats des tâches, utilisez `Callable` au lieu de `Runnable` :
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ExecutorService executor = Executors.newFixedThreadPool(2);

        // Soumettre une tâche Callable
        Future<Integer> future = executor.submit(() -> {
            Thread.sleep(1000);
            return 42;
        });

        // Faire d'autres travaux pendant l'exécution de la tâche
        System.out.println("Tâche soumise...");

        // Obtenir le résultat (bloque jusqu'à la fin)
        Integer result = future.get();
        System.out.println("Résultat : " + result);

        executor.shutdown();
    }
}
```
- `Future.get()` récupère le résultat, en bloquant si la tâche n'est pas terminée.
- Utilisez `future.isDone()` pour vérifier l'achèvement sans bloquer.

---

### 5. Avancé : Ajustement du Pool de Threads
Pour les applications réelles, vous pourriez vouloir un `ThreadPoolExecutor` personnalisé :
```java
import java.util.concurrent.*;

public class Main {
    public static void main(String[] args) {
        // Pool de threads personnalisé : 2-4 threads, capacité de file d'attente de 10
        ThreadPoolExecutor executor = new ThreadPoolExecutor(
            2, // Taille du pool de base
            4, // Taille maximale du pool
            60L, // Délai d'inactivité des threads
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(10) // File d'attente des tâches
        );

        for (int i = 0; i < 15; i++) {
            executor.execute(() -> {
                System.out.println("Tâche par : " + Thread.currentThread().getName());
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
- Taille de base (2) : Nombre minimum de threads maintenus actifs.
- Taille max (4) : Nombre maximum de threads si la file d'attente est pleine.
- File d'attente : Contient les tâches lorsque tous les threads sont occupés.

---

### 6. Bonnes Pratiques
- **Arrêt Correct** : Appelez toujours `shutdown()` ou `shutdownNow()` pour éviter les fuites de ressources.
- **Gérer les Interruptions** : Vérifiez `Thread.currentThread().isInterrupted()` dans les boucles.
- **Éviter la Surcharge** : Trop de threads peuvent dégrader les performances—ajustez la taille du pool en fonction des cœurs du processeur (par exemple, `Runtime.getRuntime().availableProcessors()`).
- **Utiliser `try-finally` avec `ExecutorService`** :
```java
ExecutorService executor = Executors.newFixedThreadPool(4);
try {
    // Soumettre des tâches
} finally {
    executor.shutdown();
}
```

---

### Exemple avec Log4j (Pour Faire le Lien)
Combiner le multithreading avec votre question précédente sur Log4j :
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
                logger.info("Tâche {} démarrée par {}", taskId, Thread.currentThread().getName());
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    logger.error("Tâche {} interrompue", taskId, e);
                    Thread.currentThread().interrupt();
                }
                logger.info("Tâche {} terminée", taskId);
            });
        }

        executor.shutdown();
    }
}
```
Avec le `log4j2.xml` de la question précédente, cela enregistre la progression des tâches dans la console et dans un fichier.