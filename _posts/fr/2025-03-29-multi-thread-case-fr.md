---
audio: false
generated: true
lang: fr
layout: post
title: Étude de Cas Multifilaire
translated: true
type: note
---

Pour gérer la validation multi-thread dans un projet Java Spring Boot avec 10 règles, où certaines règles peuvent accéder à la base de données et vous souhaitez annuler les autres dès qu'une échoue pour éviter de perdre du temps, vous pouvez utiliser les utilitaires de concurrence de Java en combinaison avec les fonctionnalités de Spring. Voici une solution complète et efficace :

### Aperçu de l'approche
- **Exécuter les validations concurremment** : Utiliser plusieurs threads pour exécuter les 10 règles de validation en parallèle, accélérant le processus lorsque toutes les règles passent.
- **Annuler en cas d'échec** : Arrêter les validations restantes dès qu'une règle échoue, minimisant le travail inutile.
- **Tirer parti de Spring** : Utiliser l'injection de dépendances et la gestion des transactions de Spring pour les règles accédant à la base de données.

La meilleure façon d'y parvenir est d'utiliser un `ExecutorService` couplé à un `CompletionService`. Le `CompletionService` permet de traiter les résultats des tâches au fur et à mesure de leur achèvement, permettant une détection immédiate d'un échec et l'annulation des tâches en attente.

---

### Solution étape par étape

#### 1. Définir les règles de validation
Chacune des 10 règles doit être une tâche de validation indépendante. Certaines règles peuvent impliquer un accès à la base de données, encapsulez-les donc dans un service avec des méthodes transactionnelles.

```java
@Service
public class RuleValidator {
    // Exemple : Règle accédant à la base de données
    @Transactional(readOnly = true)
    public boolean validateRule(int ruleId) {
        // Simuler la validation de la règle, par exemple, une requête en base de données
        // Retourner true si la règle passe, false si elle échoue
        return performValidation(ruleId); // L'implémentation dépend de votre logique
    }

    private boolean performValidation(int ruleId) {
        // Remplacer par la logique de validation réelle
        return ruleId % 2 == 0; // Exemple : les règles avec un ID pair passent
    }
}
```

- Utilisez `@Transactional(readOnly = true)` pour les règles qui ne font que lire dans la base de données, garantissant que chacune s'exécute dans son propre contexte de transaction de manière thread-safe.

#### 2. Configurer un ExecutorService
Définissez un pool de threads pour gérer l'exécution concurrente des tâches de validation. Dans Spring, vous pouvez le créer en tant que bean :

```java
@Configuration
public class AppConfig {
    @Bean
    public ExecutorService executorService() {
        return Executors.newFixedThreadPool(10); // 10 threads pour 10 règles
    }
}
```

- Ajustez la taille du pool de threads en fonction des capacités de votre système (par exemple, cœurs CPU, limites de connexions à la base de données).

#### 3. Implémenter la validation multi-thread
Créez un service qui orchestre le processus de validation en utilisant `CompletionService` :

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
        // Étape 1 : Créer les tâches de validation
        List<Callable<Boolean>> tasks = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            final int ruleId = i;
            tasks.add(() -> {
                try {
                    return ruleValidator.validateRule(ruleId);
                } catch (Exception e) {
                    // Gérer les exceptions (par exemple, erreurs de base de données) comme des échecs
                    log.error("Validation failed for rule " + ruleId, e);
                    return false;
                }
            });
        }

        // Étape 2 : Configurer le CompletionService et soumettre les tâches
        CompletionService<Boolean> completionService = new ExecutorCompletionService<>(executorService);
        List<Future<Boolean>> futures = new ArrayList<>();
        for (Callable<Boolean> task : tasks) {
            futures.add(completionService.submit(task));
        }

        // Étape 3 : Traiter les résultats au fur et à mesure de leur achèvement
        boolean hasFailed = false;
        for (int i = 0; i < 10; i++) {
            try {
                Future<Boolean> completed = completionService.take(); // Bloque jusqu'à la fin de la tâche suivante
                boolean result = completed.get();
                if (!result) {
                    hasFailed = true;
                    break; // Arrêter de vérifier dès qu'un échec est détecté
                }
            } catch (InterruptedException | ExecutionException e) {
                log.error("Error during validation", e);
                hasFailed = true;
                break;
            }
        }

        // Étape 4 : Annuler les tâches restantes si un échec s'est produit
        if (hasFailed) {
            for (Future<Boolean> future : futures) {
                if (!future.isDone()) {
                    future.cancel(true); // Interrompre les tâches en cours d'exécution
                }
            }
            return false; // La validation a échoué
        }

        return true; // Toutes les règles sont passées
    }
}
```

#### Fonctionnement
- **Création des tâches** : Chaque règle de validation est encapsulée dans un `Callable<Boolean>` qui retourne `true` si la règle passe et `false` si elle échoue. Les exceptions sont capturées et traitées comme des échecs.
- **Exécution concurrente** : Les tâches sont soumises au `CompletionService`, qui les exécute en parallèle en utilisant le pool de threads. Les Futures sont collectées pour suivre le statut des tâches.
- **Traitement des résultats** : `completionService.take()` récupère le résultat de la prochaine tâche achevée. Si un résultat est `false`, la boucle est interrompue et `hasFailed` est défini.
- **Annulation** : En cas d'échec, toutes les tâches non terminées sont annulées en utilisant `future.cancel(true)`, ce qui tente d'interrompre les threads en cours d'exécution.
- **Résultat** : Retourne `false` si une règle échoue, `true` si toutes passent.

---

### Considérations clés
- **Accès à la base de données** : Étant donné que les règles peuvent accéder à la base de données, `@Transactional` garantit des opérations thread-safe. Chaque tâche s'exécute dans sa propre transaction, ce qui est approprié pour des validations indépendantes.
- **Annulation des tâches** : Annuler un `Future` interrompt le thread, mais les requêtes de base de données en cours peuvent ne pas s'arrêter immédiatement. Cependant, cela empêche tout traitement ultérieur et permet au thread principal de continuer.
- **Gestion des exceptions** : Les exceptions (par exemple, erreurs de base de données) sont capturées dans les tâches et traitées comme des échecs, garantissant un comportement robuste.
- **Taille du pool de threads** : Définie à 10 pour plus de simplicité (un thread par règle), mais optimisez en fonction des besoins et des ressources de votre application.

---

### Pourquoi cette approche est la meilleure
- **Efficacité** : Les validations s'exécutent concurremment, réduisant le temps total lorsqu'elles passent toutes.
- **Terminaison anticipée** : `CompletionService` permet une détection immédiate des échecs, et l'annulation arrête le travail inutile.
- **Simplicité** : Tire parti des utilitaires de concurrence standard de Java et s'intègre parfaitement avec Spring Boot.
- **Évolutivité** : Facilement extensible à plus de règles en ajustant le pool de threads et la liste des tâches.

Des approches alternatives comme `CompletableFuture` ou l'interrogation des résultats `Future` avec des timeouts ont été envisagées, mais `CompletionService` est plus simple pour ce cas d'utilisation, car il gère efficacement les résultats dans l'ordre d'achèvement et prend en charge l'annulation.

---

### Exemple d'utilisation
Injectez et appelez le service dans votre contrôleur ou logique métier :

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

Cette solution répond à vos exigences : elle exécute 10 règles de validation en parallèle, annule les tâches restantes lorsqu'une échoue et évite de perdre du temps, le tout en s'intégrant proprement avec Spring Boot.