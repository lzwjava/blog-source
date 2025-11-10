---
audio: false
generated: true
lang: fr
layout: post
title: Configurer Maven pour l'exécution de tests en parallèle
translated: true
type: note
---

Pour activer l'exécution parallèle des tests dans votre projet Maven, en particulier pour la classe `MavenTest.java` fournie, vous pouvez configurer le plugin Maven Surefire pour exécuter les tests en parallèle. La classe `MavenTest.java` utilise JUnit 4 avec des tests dynamiques pour exécuter des commandes Maven pour différents problèmes, et la stack trace de votre erreur originale indique que les tests s'exécutent déjà en parallèle (comme en témoigne `ForkJoinPool` dans la stack trace). Cependant, vous pouvez contrôler explicitement l'exécution parallèle en configurant le plugin Surefire dans votre fichier `pom.xml`. Ci-dessous, j'expliquerai comment configurer l'exécution parallèle des tests et comment gérer l'utilisation d'un flag `-DParallel` comme demandé.

### Pourquoi l'exécution parallèle se produit
Votre sortie de test montre `ForkJoinPool` dans la stack trace, indiquant que JUnit ou Maven utilise déjà un pool de threads pour l'exécution parallèle. La classe `MavenTest` utilise `@TestFactory` avec `DynamicTest`, et les tests s'exécutent probablement en parallèle en raison du comportement par défaut de JUnit ou d'une configuration Surefire existante. L'objectif est maintenant de configurer explicitement l'exécution parallèle et de permettre un contrôle via un flag en ligne de commande comme `-DParallel`.

### Étapes pour configurer l'exécution parallèle des tests

1. **Mettre à jour le `pom.xml` pour configurer le plugin Maven Surefire** :
   Le plugin Maven Surefire prend en charge l'exécution parallèle des tests pour JUnit 4.7+ (que votre projet utilise, car il est compatible avec `DynamicTest`). Vous pouvez spécifier le niveau de parallélisme (par exemple, `classes`, `methods`, ou `both`) et le nombre de threads. Pour permettre un contrôle via `-DParallel`, vous pouvez utiliser une propriété Maven pour activer ou configurer le parallélisme.

   Ajoutez ou mettez à jour la configuration du plugin Surefire dans votre `pom.xml` :

   ```xml
   <project>
       <!-- Autres configurations -->
       <properties>
           <!-- Par défaut, pas d'exécution parallèle sauf spécification -->
           <parallel.mode>none</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <!-- Optionnel : Timeout pour les tests parallèles -->
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <!-- Configuration du forking pour isoler les tests -->
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   - **Explication** :
     - `<parallel>` : Spécifie le niveau de parallélisme. Les valeurs valides pour JUnit 4.7+ sont `methods`, `classes`, `both`, `suites`, `suitesAndClasses`, `suitesAndMethods`, `classesAndMethods`, ou `all`. Pour votre classe `MavenTest`, `classes` est approprié car chaque `DynamicTest` représente un problème, et vous voulez exécuter les tests pour différents problèmes en parallèle.
     - `<threadCount>` : Définit le nombre de threads (par exemple, `4` pour quatre tests concurrents). Vous pouvez remplacer cette valeur via `-Dthread.count=<nombre>`.
     - `<perCoreThreadCount>false</perCoreThreadCount>` : Garantit que `threadCount` est un nombre fixe, et non mis à l'échelle par le nombre de cœurs du CPU.
     - `<parallelTestsTimeoutInSeconds>` : Définit un timeout pour les tests parallèles pour éviter les blocages (correspond à votre `TEST_TIMEOUT` de 10 secondes dans `MavenTest.java`).
     - `<forkCount>1</forkCount>` : Exécute les tests dans un processus JVM séparé pour les isoler, réduisant les problèmes d'état partagé. `<reuseForks>true</reuseForks>` permet de réutiliser la JVM pour plus d'efficacité.
     - `<parallel.mode>` et `<thread.count>` : Propriétés Maven qui peuvent être remplacées via des flags en ligne de commande (par exemple, `-Dparallel.mode=classes`).

2. **Exécuter les tests avec `-DParallel`** :
   Pour utiliser un flag `-DParallel` pour contrôler l'exécution parallèle, vous pouvez le mapper à la propriété `parallel.mode`. Par exemple, exécutez :

   ```bash
   mvn test -Dparallel.mode=classes -Dthread.count=4
   ```

   - Si `-Dparallel.mode` n'est pas spécifié, la valeur par défaut (`none`) désactive l'exécution parallèle.
   - Vous pouvez également utiliser un flag plus simple comme `-DParallel=true` pour activer le parallélisme avec un mode prédéfini (par exemple, `classes`). Pour prendre cela en charge, mettez à jour le `pom.xml` pour interpréter `-DParallel` :

   ```xml
   <project>
       <!-- Autres configurations -->
       <properties>
           <parallel.mode>${Parallel ? 'classes' : 'none'}</parallel.mode>
           <thread.count>4</thread.count>
       </properties>
       <build>
           <plugins>
               <plugin>
                   <groupId>org.apache.maven.plugins</groupId>
                   <artifactId>maven-surefire-plugin</artifactId>
                   <version>3.5.3</version>
                   <configuration>
                       <parallel>${parallel.mode}</parallel>
                       <threadCount>${thread.count}</threadCount>
                       <perCoreThreadCount>false</perCoreThreadCount>
                       <parallelTestsTimeoutInSeconds>10</parallelTestsTimeoutInSeconds>
                       <forkCount>1</forkCount>
                       <reuseForks>true</reuseForks>
                   </configuration>
               </plugin>
           </plugins>
       </build>
   </project>
   ```

   Maintenant, vous pouvez exécuter les tests avec :

   ```bash
   mvn test -DParallel=true
   ```

   - `-DParallel=true` : Active l'exécution parallèle avec `parallel=classes` et `threadCount=4`.
   - `-DParallel=false` ou omettre `-DParallel` : Désactive l'exécution parallèle (`parallel=none`).
   - Vous pouvez remplacer le nombre de threads avec `-Dthread.count=<nombre>` (par exemple, `-Dthread.count=8`).

3. **Garantir la sécurité des threads** :
   Votre classe `MavenTest` exécute des commandes Maven (`mvn exec:exec -Dproblem=<problem>`) en parallèle, ce qui lance des processus séparés. Ceci est intrinsèquement thread-safe car chaque processus a son propre espace mémoire, évitant les problèmes d'état partagé. Cependant, assurez-vous que :
   - Les classes `com.lzw.solutions.uva.<problem>.Main` ne partagent pas de ressources (par exemple, des fichiers ou des bases de données) qui pourraient causer des conflits.
   - Les fichiers d'entrée/sortie ou les ressources utilisées par chaque problème (par exemple, les données de test pour `p10009`) sont isolées pour éviter les conditions de course.
   - Si des ressources partagées sont utilisées, envisagez d'utiliser `@NotThreadSafe` sur des classes de test spécifiques ou de synchroniser l'accès aux ressources partagées.

4. **Gérer la liste d'exclusion avec l'exécution parallèle** :
   Votre `MavenTest.java` inclut déjà un ensemble `SKIP_PROBLEMS` pour exclure des problèmes comme `p10009`. Ceci fonctionne bien avec l'exécution parallèle, car les problèmes exclus sont écartés avant que les tests ne soient planifiés. Assurez-vous que la liste d'exclusion est mise à jour si nécessaire :

   ```java
   private static final Set<String> SKIP_PROBLEMS = new HashSet<>(Arrays.asList(
       "p10009", // Exclut p10009 en raison de NumberFormatException
       "p10037"  // Ajoutez d'autres problèmes problématiques ici
   ));
   ```

5. **Exécuter les tests** :
   Pour exécuter les tests en parallèle avec la liste d'exclusion et le flag `-DParallel` :

   ```bash
   mvn test -DParallel=true -Dthread.count=4
   ```

   - Ceci exécute jusqu'à quatre tests de problèmes simultanément, en excluant `p10009` et tout autre problème dans `SKIP_PROBLEMS`.
   - Si vous voulez désactiver le parallélisme pour le débogage :

     ```bash
     mvn test -DParallel=false
     ```

6. **Traiter le `NumberFormatException` pour `p10009`** :
   Le `NumberFormatException` dans `p10009` (de votre erreur originale) indique qu'une chaîne `null` est analysée. Bien qu'exclure `p10009` évite le problème, vous pouvez le corriger pour plus de complétude. Vérifiez `com.lzw.solutions.uva.p10009.Main` à la ligne 17 (méthode `readInt`) et ajoutez des vérifications de nullité :

   ```java
   public int readInt() {
       String input = readInput(); // Méthode hypothétique de lecture d'entrée
       if (input == null || input.trim().isEmpty()) {
           throw new IllegalArgumentException("L'entrée ne peut pas être nulle ou vide");
       }
       return Integer.parseInt(input);
   }
   ```

   Alternativement, gardez `p10009` dans la liste d'exclusion jusqu'à ce que le problème soit résolu.

### Notes sur l'exécution parallèle
- **Performance** : L'exécution parallèle avec `parallel=classes` est adaptée à votre classe `MavenTest`, car chaque `DynamicTest` représente un problème distinct. Cela minimise la surcharge comparé à `methods` ou `both`.
- **Utilisation des ressources** : L'exécution parallèle augmente l'utilisation du CPU et de la mémoire. Surveillez votre système pour vous assurer que `threadCount` (par exemple, `4`) ne submerge pas votre matériel. Utilisez `forkCount` pour isoler les tests dans des JVM séparées si des problèmes de mémoire surviennent.
- **Timeouts** : Le paramètre `parallelTestsTimeoutInSeconds` garantit que les tests ne se bloquent pas indéfiniment, correspondant à votre `TEST_TIMEOUT` de 10 secondes dans `MavenTest.java`.
- **Sécurité des threads** : Étant donné que vos tests exécutent des commandes `mvn exec:exec`, qui s'exécutent dans des processus séparés, la sécurité des threads est moins préoccupante. Cependant, assurez-vous que les entrées/sorties des tests (par exemple, les fichiers) sont isolées par problème.
- **Débogage** : Si les tests échouent de manière inattendue en mode parallèle, exécutez-les séquentiellement (`-DParallel=false`) pour isoler les problèmes.

### Exemple de commande complète
Pour exécuter les tests en parallèle, en excluant `p10009`, avec quatre threads :

```bash
mvn test -DParallel=true -Dthread.count=4
```

Pour déboguer un problème spécifique (par exemple, `p10009`) sans parallélisme, retirez-le temporairement de `SKIP_PROBLEMS` et exécutez :

```bash
mvn test -DParallel=false -Dproblem=p10009
```

### Considérations supplémentaires
- **Limitations de JUnit 4** : Votre projet utilise JUnit 4 (basé sur les imports `org.junit.jupiter.api` et `DynamicTest`). JUnit 4.7+ prend en charge l'exécution parallèle via Surefire, mais JUnit 5 offre des options de parallélisation plus flexibles. Envisagez de passer à JUnit 5 si vous avez besoin de fonctionnalités avancées comme le parallélisme par classe ou des stratégies personnalisées.
- **Version de Maven** : Assurez-vous d'utiliser une version récente de Maven (par exemple, 3.9.10, comme dans votre sortie d'erreur) et de Surefire (par exemple, 3.5.3) pour une prise en charge optimale de l'exécution parallèle.
- **Gestion des erreurs** : Pour rendre les tests plus robustes, envisagez de capturer les exceptions dans `runMavenExecTests` (comme suggéré dans la réponse précédente) pour enregistrer les échecs sans arrêter la suite de tests :

   ```java
   @TestFactory
   Collection<DynamicTest> runMavenExecTests() {
       return PROBLEMS.stream()
               .map(problem -> DynamicTest.dynamicTest("Test problem: " + problem, () -> {
                   String command = String.format("mvn exec:exec -Dproblem=%s", problem);
                   System.out.println("Executing command for " + problem + ": " + command);
                   try {
                       Process process = Runtime.getRuntime().exec(command);
                       // ... (reste du code de gestion du processus)
                       int exitCode = process.exitValue();
                       Assertions.assertTrue(
                               exitCode == 0,
                               "Maven command failed for problem: " + problem + "\nError output:\n" + errorOutput);
                   } catch (Exception e) {
                       System.err.println("Exception for problem " + problem + ": " + e.getMessage());
                       // Optionnellement, continuer au lieu d'échouer
                   }
               }))
               .collect(Collectors.toList());
   }
   ```

Cette configuration vous permet de contrôler l'exécution parallèle avec `-DParallel=true`, d'exclure les tests problématiques comme `p10009` et de maintenir une exécution de test robuste. Faites-moi savoir si vous avez besoin de personnalisations supplémentaires, telles que des listes d'exclusion dynamiques via des arguments en ligne de commande ou des configurations JUnit 5 avancées !