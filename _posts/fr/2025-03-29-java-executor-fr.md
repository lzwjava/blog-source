---
audio: false
generated: true
lang: fr
layout: post
title: Comprendre ExecutorService et ThreadPoolExecutor
translated: true
type: note
---

Configurer les paramètres d'un `ExecutorService` en Java implique de configurer son pool de threads pour optimiser les performances en fonction des ressources de votre système (comme un CPU 8 cœurs) et de la nature de vos tâches (par exemple, liées au CPU ou liées aux E/S). Ci-dessous, j'expliquerai comment configurer un `ExecutorService` pour un CPU 8 cœurs, en me concentrant sur les implémentations courantes comme `ThreadPoolExecutor`, et je fournirai des exemples pratiques adaptés à votre cas d'utilisation.

---

### Comprendre ExecutorService et ThreadPoolExecutor

L'interface `ExecutorService` est généralement implémentée par des classes comme `ThreadPoolExecutor`, qui permet un contrôle précis des paramètres du pool de threads. Lors de sa configuration pour un CPU 8 cœurs, vous devez considérer :
- **Taille du pool de base (Core Pool Size)** : Le nombre de threads à maintenir en vie même s'ils sont inactifs.
- **Taille maximale du pool (Maximum Pool Size)** : Le nombre maximum de threads autorisés dans le pool.
- **Capacité de la file d'attente (Queue Capacity)** : La taille de la file d'attente des tâches pour contenir les tâches avant leur exécution.
- **Stratégie de création de threads** : Comment les threads sont créés et gérés.
- **Type de tâche** : Si les tâches sont liées au CPU (ex: calculs) ou liées aux E/S (ex: appels base de données).

Pour un CPU 8 cœurs, la configuration optimale dépend du fait que vos tâches soient intensives en CPU ou intensives en E/S (comme l'accès à la base de données dans votre scénario de validation).

---

### Paramètres clés pour ThreadPoolExecutor

Voici comment vous pouvez configurer un `ThreadPoolExecutor` :

```java
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,      // Nombre de threads à maintenir en vie
    maximumPoolSize,   // Nombre maximum de threads autorisés
    keepAliveTime,     // Durée de vie des threads inactifs (ex: 60L)
    TimeUnit.SECONDS,  // Unité pour keepAliveTime
    workQueue,         // File d'attente pour les tâches (ex: new LinkedBlockingQueue<>())
    threadFactory,     // Optionnel : Personnalisation du nom ou de la priorité des threads
    rejectionHandler   // Comportement lorsque la file est pleine et le max de threads est atteint
);
```

#### Détail des paramètres
1. **`corePoolSize`** :
   - Nombre minimum de threads toujours maintenus en vie.
   - Pour les tâches liées au CPU : Définir égal au nombre de cœurs (ex: 8).
   - Pour les tâches liées aux E/S : Peut être plus élevé (ex: 16 ou plus), car les threads peuvent passer du temps à attendre.

2. **`maximumPoolSize`** :
   - Nombre maximum de threads autorisés si la file d'attente se remplit.
   - Pour les tâches liées au CPU : Souvent égal à `corePoolSize` (ex: 8).
   - Pour les tâches liées aux E/S : Plus élevé pour gérer les pics (ex: 20 ou 50).

3. **`keepAliveTime`** :
   - Durée pendant laquelle les threads inactifs excédentaires (au-delà de `corePoolSize`) sont maintenus en vie avant d'être terminés.
   - Exemple : `60L` secondes est une valeur par défaut courante.

4. **`workQueue`** :
   - File d'attente pour les tâches en attente d'exécution :
     - `LinkedBlockingQueue` : File d'attente non bornée (par défaut dans nombreux cas).
     - `ArrayBlockingQueue` : File d'attente bornée (ex: `new ArrayBlockingQueue<>(100)`).
     - `SynchronousQueue` : Aucune file d'attente ; les tâches sont directement transmises aux threads (utilisée dans `Executors.newCachedThreadPool()`).

5. **`threadFactory`** (Optionnel) :
   - Personnalise la création des threads (ex: nommer les threads pour le débogage).
   - Par défaut : `Executors.defaultThreadFactory()`.

6. **`rejectionHandler`** (Optionnel) :
   - Politique lorsque les tâches dépassent `maximumPoolSize` et la capacité de la file d'attente :
     - `AbortPolicy` (par défaut) : Lance une `RejectedExecutionException`.
     - `CallerRunsPolicy` : Exécute la tâche dans le thread appelant.
     - `DiscardPolicy` : Ignore silencieusement la tâche.

---

### Configuration pour un CPU 8 cœurs

#### Scénario 1 : Tâches liées au CPU
Si vos tâches sont intensives en CPU (ex: calculs lourds), vous devez faire correspondre le nombre de threads au nombre de cœurs du CPU pour maximiser le débit sans surcharger le système.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createCpuBoundExecutor() {
        int corePoolSize = 8; // Correspond aux 8 cœurs
        int maximumPoolSize = 8;
        long keepAliveTime = 60L; // 60 secondes

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new LinkedBlockingQueue<>(), // File d'attente non bornée
            Executors.defaultThreadFactory(),
            new ThreadPoolExecutor.AbortPolicy()
        );
    }
}
```

- **Pourquoi** : 8 threads utilisent pleinement les 8 cœurs. Ajouter plus de threads entraînerait une surcharge de changement de contexte, réduisant les performances.

#### Scénario 2 : Tâches liées aux E/S (ex: Validation de base de données)
Pour votre scénario de validation avec accès à la base de données, les tâches sont liées aux E/S—les threads passent du temps à attendre les réponses de la base de données. Vous pouvez utiliser plus de threads que de cœurs pour occuper le CPU pendant que certains threads attendent.

```java
import java.util.concurrent.*;

public class ExecutorConfig {
    public static ExecutorService createIoBoundExecutor() {
        int corePoolSize = 16; // 2x cœurs pour les tâches liées aux E/S
        int maximumPoolSize = 20; // Permettre une capacité pour les pics
        long keepAliveTime = 60L;

        return new ThreadPoolExecutor(
            corePoolSize,
            maximumPoolSize,
            keepAliveTime,
            TimeUnit.SECONDS,
            new ArrayBlockingQueue<>(100), // File d'attente bornée pour limiter la mémoire
            new ThreadFactoryBuilder().setNameFormat("validation-thread-%d").build(), // Nommage personnalisé
            new ThreadPoolExecutor.CallerRunsPolicy() // Retour au thread appelant en cas de surcharge
        );
    }
}
```

- **Pourquoi** :
  - `corePoolSize = 16` : Une heuristique courante pour les tâches liées aux E/S est `N * 2` (où `N` est le nombre de cœurs CPU), mais vous pouvez l'ajuster en fonction des limites de connexion à la base de données et des temps d'attente des tâches.
  - `maximumPoolSize = 20` : Permet des threads supplémentaires pour les charges de pointe.
  - `ArrayBlockingQueue(100)` : Empêche la croissance illimitée des tâches en file d'attente, évitant les problèmes de mémoire.
  - `CallerRunsPolicy` : Garantit que le système se dégrade gracieusement en cas de surcharge en exécutant les tâches dans le thread de l'appelant.

#### Intégration avec Spring Boot
Dans une application Spring Boot, définissez l'`ExecutorService` comme un bean :

```java
import com.google.common.util.concurrent.ThreadFactoryBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.*;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        int corePoolSize = 16; // Hypothèse de tâches liées aux E/S pour la validation
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

- **Remarque** : Ajoutez Guava (`com.google.guava:guava`) à vos dépendances pour `ThreadFactoryBuilder`, ou utilisez `Executors.defaultThreadFactory()` si vous n'avez pas besoin de nommage personnalisé.

#### Utilisation dans votre Service de Validation
Injectez et utilisez-le comme montré dans vos exemples précédents :

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

    // Utiliser dans la logique CompletableFuture ou ExecutorService comme montré précédemment
}
```

---

### Conseils d'ajustement pour un CPU 8 cœurs

1. **Mesurer les Performances** :
   - Utilisez des outils de profilage (ex: VisualVM) pour surveiller l'utilisation des threads et ajuster `corePoolSize` et `maximumPoolSize`.

2. **Limites de la Base de Données** :
   - Si les règles accèdent à une base de données, assurez-vous que la taille du pool de threads ne dépasse pas la taille de votre pool de connexions (ex: `maximumPoolSize` de HikariCP). Coordonnez ces paramètres.

3. **Calcul Dynamique** :
   - Utilisez `Runtime.getRuntime().availableProcessors()` pour définir dynamiquement la taille du pool de base :
     ```java
     int cores = Runtime.getRuntime().availableProcessors(); // Retourne 8 sur un CPU 8 cœurs
     int corePoolSize = cores * 2; // Pour les tâches liées aux E/S
     ```

4. **Pré-démarrer les Threads** :
   - Appelez `executor.prestartAllCoreThreads()` pour initialiser tous les threads de base au préalable, évitant une création différée.

---

### Conclusion

Pour un CPU 8 cœurs exécutant des tâches liées aux E/S comme vos règles de validation avec accès à la base de données :
- Utilisez un `ThreadPoolExecutor` avec `corePoolSize = 16`, `maximumPoolSize = 20`, et une file d'attente bornée (ex: `ArrayBlockingQueue(100)`).
- Intégrez-le en tant que bean Spring pour l'injection de dépendances.
- Ajustez en fonction du profilage et des contraintes de la base de données.

Cette configuration équilibre le parallélisme, l'utilisation des ressources et la stabilité du système, la rendant bien adaptée à votre cas d'utilisation. Faites-moi savoir si vous avez besoin d'aide pour l'intégrer dans votre projet spécifique !