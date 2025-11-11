---
audio: false
generated: true
lang: fr
layout: post
title: CompletableFuture en Java
translated: true
type: note
---

Dans un projet Java Spring Boot, il n'existe pas d'équivalent direct au `Promise.all` de JavaScript, qui attend la résolution de plusieurs promesses et fournit leurs résultats. Cependant, vous pouvez obtenir une fonctionnalité similaire - exécuter plusieurs tâches simultanément dans une boucle for et utiliser leurs résultats après la fin de tous les threads - en utilisant `CompletableFuture` du package `java.util.concurrent`, spécifiquement avec la méthode `CompletableFuture.allOf`. Cette approche est bien adaptée à un projet Spring Boot, surtout lorsqu'elle est combinée avec les fonctionnalités de programmation asynchrone de Spring. Ci-dessous, je vais expliquer comment procéder étape par étape, y compris un exemple complet.

### Pourquoi `CompletableFuture` ?
`CompletableFuture` (introduit dans Java 8) vous permet d'effectuer des opérations asynchrones et de gérer leur achèvement. La méthode `allOf` prend plusieurs instances de `CompletableFuture` et renvoie un nouveau `CompletableFuture` qui se termine lorsque tous les futurs donnés sont terminés, ce qui le rend idéal pour votre scénario où vous voulez :
- Exécuter des tâches en parallèle dans une boucle for.
- Attendre que toutes les tâches se terminent.
- Utiliser les résultats par la suite.

### Étapes de mise en œuvre
Voici comment vous pouvez structurer votre solution dans un projet Spring Boot :

1. **Définir les tâches asynchrones**  
   Chaque itération de votre boucle for représente une tâche qui peut s'exécuter indépendamment. Ces tâches renverront des instances `CompletableFuture`, représentant leurs résultats éventuels.

2. **Collecter les Futures**  
   Stockez tous les objets `CompletableFuture` dans une liste au fur et à mesure que vous les créez dans la boucle.

3. **Attendre que toutes les tâches se terminent**  
   Utilisez `CompletableFuture.allOf` pour combiner les futurs en un seul futur qui se termine lorsque toutes les tâches sont terminées.

4. **Récupérer et utiliser les résultats**  
   Après la fin de toutes les tâches, extrayez les résultats de chaque `CompletableFuture` et traitez-les selon les besoins.

5. **Gérer les exceptions**  
   Prenez en compte les erreurs potentielles pendant l'exécution de la tâche.

### Exemple de mise en œuvre
Supposons que vous ayez une liste d'éléments à traiter simultanément (par exemple, appeler un service ou effectuer un calcul). Voici deux approches : une utilisant l'annotation `@Async` de Spring et une autre utilisant `CompletableFuture.supplyAsync`.

#### Approche 1 : Utilisation de `@Async` avec Spring
Spring Boot fournit l'annotation `@Async` pour exécuter des méthodes de manière asynchrone. Vous devrez activer la prise en charge asynchrone dans votre application.

**Étape 1 : Activer la prise en charge asynchrone**
Ajoutez l'annotation `@EnableAsync` à une classe de configuration ou à votre classe d'application principale :

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

**Étape 2 : Définir un Service avec une méthode asynchrone**
Créez un service avec une méthode qui traite chaque élément de manière asynchrone :

```java
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import java.util.concurrent.CompletableFuture;

@Service
public class MyService {

    @Async
    public CompletableFuture<String> processItem(String item) {
        // Simuler un travail (par exemple, E/S ou calcul)
        try {
            Thread.sleep(1000); // Délai d'une seconde
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            return CompletableFuture.completedFuture("Interrupted: " + item);
        }
        return CompletableFuture.completedFuture("Processed: " + item);
    }
}
```

**Étape 3 : Traiter les éléments dans un contrôleur ou un service**
Dans votre contrôleur ou un autre service, utilisez une boucle for pour soumettre des tâches et attendre tous les résultats :

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
        // Liste pour contenir tous les futurs
        List<CompletableFuture<String>> futures = new ArrayList<>();

        // Soumettre chaque tâche dans la boucle for
        for (String item : items) {
            CompletableFuture<String> future = myService.processItem(item);
            futures.add(future);
        }

        // Attendre que toutes les tâches se terminent
        CompletableFuture<Void> allFutures = CompletableFuture.allOf(
            futures.toArray(new CompletableFuture[0])
        );

        // Bloquer jusqu'à ce que toutes les tâches soient terminées
        allFutures.join();

        // Collecter les résultats
        List<String> results = futures.stream()
            .map(CompletableFuture::join) // Obtenir chaque résultat
            .collect(Collectors.toList());

        return results;
    }
}
```

**Exemple d'utilisation :**
```java
List<String> items = Arrays.asList("Item1", "Item2", "Item3");
List<String> results = itemProcessor.processItems(items);
System.out.println(results); // Affiche : [Processed: Item1, Processed: Item2, Processed: Item3]
```

#### Approche 2 : Utilisation de `CompletableFuture.supplyAsync`
Si vous préférez ne pas utiliser `@Async`, vous pouvez gérer manuellement les threads avec un `Executor` et `CompletableFuture.supplyAsync`.

**Étape 1 : Configurer un pool de threads**
Définissez un bean `TaskExecutor` pour contrôler le pool de threads :

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
        executor.setCorePoolSize(5);    // Nombre de threads à garder dans le pool
        executor.setMaxPoolSize(10);    // Nombre maximum de threads
        executor.setQueueCapacity(25);  // Capacité de la file d'attente pour les tâches en attente
        executor.initialize();
        return executor;
    }
}
```

**Étape 2 : Traiter les éléments avec `supplyAsync`**
Utilisez l'executor pour exécuter les tâches de manière asynchrone :

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
        // Créer les futurs en utilisant supplyAsync
        List<CompletableFuture<String>> futures = items.stream()
            .map(item -> CompletableFuture.supplyAsync(() -> processItem(item), taskExecutor))
            .collect(Collectors.toList());

        // Attendre que toutes les tâches se terminent
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

        // Collecter les résultats
        List<String> results = futures.stream()
            .map(CompletableFuture::join)
            .collect(Collectors.toList());

        return results;
    }

    private String processItem(String item) {
        // Simuler un travail
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

### Points clés
- **Attente de l'achèvement** : `CompletableFuture.allOf(...).join()` ou `.get()` garantit que le thread principal attend que toutes les tâches se terminent. Utilisez `join()` pour éviter de gérer les exceptions vérifiées ; elle lance `CompletionException` si une tâche échoue.
- **Gestion des exceptions** : Enveloppez l'appel `.join()` ou `.get()` dans un bloc try-catch si vous devez gérer les exceptions :

```java
try {
    allFutures.get();
} catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    // Gérer l'interruption
} catch (ExecutionException e) {
    // Gérer les échecs de tâche
    e.printStackTrace();
}
```

- **Configuration du pool de threads** : Ajustez la taille du pool de threads en fonction de votre charge de travail. Pour les tâches liées aux E/S (par exemple, appels de base de données, requêtes API), un pool plus grand (par exemple, 5 à 10 threads) convient. Pour les tâches liées au CPU, correspondez au nombre de cœurs de processeur (par exemple, `Runtime.getRuntime().availableProcessors()`).
- **Ordre des résultats** : Les résultats conservent l'ordre de la liste d'entrée puisque les futurs sont collectés dans le même ordre que la boucle.

### Quelle approche choisir ?
- **Utilisez `@Async`** si vos tâches font naturellement partie d'un service Spring et que vous voulez que Spring gère le threading. C'est plus propre et s'intègre bien avec Spring Boot.
- **Utilisez `supplyAsync`** si vous avez besoin de plus de contrôle sur l'exécution des tâches ou si vous ne voulez pas dépendre du framework asynchrone de Spring.

### Réponse finale
Pour reproduire `Promise.all` dans un projet Java Spring Boot pour un travail en boucle for où vous voulez utiliser les résultats des threads après une exécution multithread, utilisez `CompletableFuture.allOf` avec une liste d'instances `CompletableFuture`. L'approche `@Async` avec Spring est recommandée pour sa simplicité, mais `supplyAsync` avec un exécuteur personnalisé fonctionne aussi. L'exemple ci-dessus avec `@Async` le démontre :

- Créez des instances `CompletableFuture` dans une boucle for en utilisant une méthode `@Async`.
- Utilisez `CompletableFuture.allOf` pour attendre toutes les tâches.
- Collectez et utilisez les résultats après l'achèvement.

Cela garantit que toutes les tâches s'exécutent simultanément, et vous pouvez traiter leurs résultats une fois qu'elles sont toutes terminées, répondant ainsi efficacement à vos exigences.