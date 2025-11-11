---
audio: false
generated: true
lang: fr
layout: post
title: Mise en œuvre de la validation multithread avec CompletableFuture
translated: true
type: note
---

Si nous utilisons `CompletableFuture` dans une application Spring Boot pour une validation multi-thread, cela offre une manière moderne et flexible de gérer les tâches asynchrones. Ci-dessous, j'expliquerai comment l'implémenter, mettrai en lumière ses avantages et ses défis, et fournirai une solution complète conçue pour valider plusieurs règles simultanément.

### Implémentation d'une validation multi-thread avec CompletableFuture

`CompletableFuture` fait partie de l'API de concurrence de Java et vous permet d'exécuter des tâches de manière asynchrone, d'enchaîner les opérations et de gérer les résultats ou les exceptions de manière élégante. Voici comment nous pouvons l'utiliser pour valider plusieurs règles en parallèle, en s'arrêtant dès qu'une échoue.

#### Étape 1 : Définir la logique de validation

Supposons d'abord que nous ayons un service qui définit des règles de validation individuelles. Chaque règle peut impliquer un accès à la base de données ou une logique complexe, nous utiliserons donc l'annotation `@Transactional` de Spring pour une gestion appropriée des transactions.

```java
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class RuleValidator {

    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // Simuler la logique de validation (par exemple, une requête en base de données)
        return performValidation(ruleId);
    }

    private boolean performValidation(int ruleId) {
        // Exemple : les règles avec un ID pair passent, celles avec un ID impair échouent
        return ruleId % 2 == 0;
    }
}
```

#### Étape 2 : Implémenter le service de validation avec CompletableFuture

Créons maintenant un service qui exécute plusieurs règles de validation simultanément en utilisant `CompletableFuture`. Nous utiliserons un `ExecutorService` pour gérer les threads et nous assurer que si une règle échoue, nous pouvons arrêter le traitement des autres.

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
        // Créer une liste pour contenir tous les futures
        List<CompletableFuture<Boolean>> futures = new ArrayList<>();

        // Soumettre 10 règles de validation (par exemple)
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            CompletableFuture<Boolean> future = CompletableFuture.supplyAsync(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    log.error("Validation failed for rule " + ruleId, e);
                    return false; // Traiter les exceptions comme des échecs
                }
            }, executorService);
            futures.add(future);
        }

        // Créer un future pour suivre le résultat global
        CompletableFuture<Boolean> resultFuture = new CompletableFuture<>();

        // Surveiller chaque future pour détecter un échec
        for (CompletableFuture<Boolean> future : futures) {
            future.thenAccept(result -> {
                if (!result && !resultFuture.isDone()) {
                    // Premier échec détecté
                    resultFuture.complete(false);
                    // Annuler les tâches restantes
                    futures.forEach(f -> {
                        if (!f.isDone()) {
                            f.cancel(true);
                        }
                    });
                }
            });
        }

        // Si tous les futures se terminent avec succès, marquer comme vrai
        CompletableFuture.allOf(futures.toArray(new CompletableFuture[0]))
                .thenRun(() -> {
                    if (!resultFuture.isDone()) {
                        resultFuture.complete(true);
                    }
                });

        try {
            return resultFuture.get(); // Bloquer jusqu'à ce que le résultat soit disponible
        } catch (InterruptedException | ExecutionException e) {
            log.error("Error during validation", e);
            return false;
        }
    }
}
```

#### Comment cela fonctionne

1. **Soumission des tâches** :
   - Nous créons un `CompletableFuture` pour chaque règle en utilisant `supplyAsync()`, qui exécute la logique de validation de manière asynchrone.
   - Le `executorService` (injecté via Spring) gère le pool de threads.

2. **Détection des échecs** :
   - Chaque future est surveillé en utilisant `thenAccept()`. Si une règle retourne `false`, nous complétons le `resultFuture` avec `false` et annulons les autres futures.

3. **Cas de succès** :
   - `CompletableFuture.allOf()` attend que tous les futures se terminent. Si aucun échec ne survient, il complète `resultFuture` avec `true`.

4. **Récupération du résultat** :
   - Nous bloquons sur `resultFuture.get()` pour obtenir le résultat final, en gérant les exceptions qui pourraient survenir.

### Avantages de l'utilisation de CompletableFuture

- **Flexibilité** : Vous pouvez enchaîner les opérations (par exemple, `thenApply`, `thenCompose`) pour traiter davantage les résultats si nécessaire.
- **Gestion des exceptions** : Des méthodes intégrées comme `exceptionally()` ou `handle()` facilitent la gestion des erreurs.
- **Conception non-bloquante** : Elle prend en charge un style de programmation réactive, qui peut être étendu pour des workflows plus complexes.

### Défis

- **Annulation** : Contrairement à `ExecutorService` avec `CompletionService` (où vous pouvez facilement interroger le premier résultat et annuler les autres), `CompletableFuture` nécessite une annulation manuelle des autres futures lorsqu'un échoue. Cela ajoute de la complexité.
- **Complexité** : Le code peut devenir plus difficile à lire et à maintenir par rapport à une approche plus simple basée sur une boucle avec `ExecutorService`.

### Exemple d'utilisation

Pour utiliser cela dans une application Spring Boot, vous configureriez un bean `ExecutorService` :

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // Ajuster la taille selon les besoins
    }
}
```

Ensuite, appelez le service depuis un contrôleur ou un autre composant :

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

### Conclusion

Utiliser `CompletableFuture` pour la validation multi-thread dans Spring Boot est une approche viable, surtout si vous valorisez sa nature asynchrone et chaînable. Cela vous permet d'exécuter des règles de validation simultanément et de gérer les résultats avec flexibilité. Cependant, si votre objectif principal est la simplicité - en particulier pour détecter le premier échec et annuler les tâches restantes - le `ExecutorService` traditionnel avec `CompletionService` pourrait être plus facile à implémenter et à maintenir. Avec `CompletableFuture`, vous gagnez en puissance et en flexibilité au prix d'une logique d'annulation légèrement plus complexe.