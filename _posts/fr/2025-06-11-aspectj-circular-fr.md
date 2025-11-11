---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre les Dépendances Circulaires avec AspectJ
translated: true
type: note
---

Les dépendances circulaires dans votre scénario surviennent parce que `BlogConfig`, `BlogCore` et `BlogWeb` se référencent mutuellement, créant une boucle de dépendance. De plus, l'`LoggingAspect` AspectJ dans `BlogCore` (ou potentiellement `BlogWeb`) peut exacerber le problème s'il est appliqué à des méthodes à travers les modules, y compris `BlogConfig`, qui dépend de `BlogCore`. Analysons le problème et proposons une solution pour résoudre la dépendance circulaire tout en conservant la fonctionnalité AspectJ.

### Analyse du problème
1. **Dépendances des modules** :
   - `BlogCore` dépend de `BlogConfig`.
   - `BlogWeb` dépend à la fois de `BlogCore` et de `BlogConfig`.
   - `BlogConfig` dépend de `BlogCore` (ceci crée la dépendance circulaire : `BlogCore` ↔ `BlogConfig`).
   - La dépendance de `BlogWeb` sur les deux modules peut entraîner la dépendance circulaire.

2. **AspectJ LoggingAspect** :
   - Le `LoggingAspect` dans `BlogCore` (ou `BlogWeb`) utilise un pointcut large (`execution(* *(..))`), qui s'applique à toutes les exécutions de méthodes dans le contexte de l'application, y compris les méthodes dans `BlogConfig`, `BlogCore` et `BlogWeb`.
   - Si `LoggingAspect` est dans `BlogCore` et tisse du code dans `BlogConfig`, et que `BlogConfig` dépend de `BlogCore`, le processus de tissage AspectJ peut compliquer la dépendance circulaire lors de l'initialisation.

3. **Impact de la dépendance circulaire** :
   - Dans un système de build comme Maven ou Gradle, les dépendances circulaires entre modules peuvent causer des problèmes de compilation ou d'exécution (par exemple, `BeanCurrentlyInCreationException` de Spring si vous utilisez Spring, ou des problèmes de chargement de classes).
   - Le tissage à la compilation ou au chargement d'AspectJ peut échouer ou produire un comportement inattendu si les classes de `BlogConfig` et `BlogCore` sont interdépendantes et non entièrement initialisées.

### Solution
Pour résoudre la dépendance circulaire et garantir le bon fonctionnement de l'`LoggingAspect` AspectJ, suivez ces étapes :

#### 1. Rompre la dépendance circulaire
Le problème principal est la dépendance `BlogCore` ↔ `BlogConfig`. Pour le corriger, extrayez la fonctionnalité ou la configuration partagée qui amène `BlogConfig` à dépendre de `BlogCore` dans un nouveau module ou restructurez les dépendances.

**Option A : Introduire un nouveau module (`BlogCommon`)**
- Créez un nouveau module, `BlogCommon`, pour contenir les interfaces, configurations ou utilitaires partagés dont `BlogCore` et `BlogConfig` ont besoin.
- Déplacez les parties de `BlogCore` dont dépend `BlogConfig` (par exemple, les interfaces, constantes ou services partagés) vers `BlogCommon`.
- Mettez à jour les dépendances :
  - `BlogConfig` dépend de `BlogCommon`.
  - `BlogCore` dépend de `BlogCommon` et de `BlogConfig`.
  - `BlogWeb` dépend de `BlogCore` et de `BlogConfig`.

**Exemple de structure de dépendance** :
```
BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
```

**Implémentation** :
- Dans `BlogCommon`, définissez les interfaces ou composants partagés. Par exemple :
  ```java
  // Module BlogCommon
  public interface BlogService {
      void performAction();
  }
  ```
- Dans `BlogCore`, implémentez l'interface :
  ```java
  // Module BlogCore
  public class BlogCoreService implements BlogService {
      public void performAction() { /* logique */ }
  }
  ```
- Dans `BlogConfig`, utilisez l'interface de `BlogCommon` :
  ```java
  // Module BlogConfig
  import com.example.blogcommon.BlogService;
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- Dans `BlogWeb`, utilisez les deux modules selon les besoins.

Cela élimine la dépendance circulaire en garantissant que `BlogConfig` ne dépend plus directement de `BlogCore`.

**Option B : Inversion de contrôle (IoC) avec l'injection de dépendances**
- Si vous utilisez un framework comme Spring, restructurez `BlogConfig` pour qu'il dépende d'abstractions (interfaces) définies dans `BlogCore` plutôt que de classes concrètes.
- Utilisez l'injection de dépendances pour fournir l'implémentation de `BlogCore` à `BlogConfig` à l'exécution, évitant ainsi une dépendance circulaire à la compilation.
- Exemple :
  ```java
  // Module BlogCore
  public interface BlogService {
      void performAction();
  }
  @Component
  public class BlogCoreService implements BlogService {
      public void performAction() { /* logique */ }
  }

  // Module BlogConfig
  @Configuration
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- Le conteneur IoC de Spring résout la dépendance à l'exécution, rompant la circularité à la compilation.

#### 2. Ajuster la configuration AspectJ
Le pointcut large de `LoggingAspect` (`execution(* *(..))`) peut s'appliquer à tous les modules, y compris `BlogConfig`, ce qui pourrait compliquer l'initialisation. Pour rendre l'aspect plus gérable et éviter les problèmes de tissage :

- **Réduire le pointcut** : Limitez l'aspect à des packages ou modules spécifiques pour éviter de l'appliquer à `BlogConfig` ou à d'autres codes d'infrastructure.
  ```java
  import org.aspectj.lang.JoinPoint;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import java.util.Arrays;

  @Aspect
  public class LoggingAspect {
      @After("execution(* com.example.blogcore..*(..)) || execution(* com.example.blogweb..*(..))")
      public void logAfter(JoinPoint joinPoint) {
          System.out.println("Méthode exécutée : " + joinPoint.getSignature());
          System.out.println("Arguments : " + Arrays.toString(joinPoint.getArgs()));
      }
  }
  ```
  Ce pointcut s'applique uniquement aux méthodes dans `BlogCore` (`com.example.blogcore`) et `BlogWeb` (`com.example.blogweb`), excluant `BlogConfig`.

- **Déplacer l'aspect vers un module séparé** : Pour éviter les problèmes de tissage lors de l'initialisation des modules, placez `LoggingAspect` dans un nouveau module (par exemple, `BlogAspects`) qui dépend de `BlogCore` et `BlogWeb` mais pas de `BlogConfig`.
  - Structure de dépendance :
    ```
    BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
                       ↑          ↑
                       └─ BlogAspects ─┘
    ```
  - Mettez à jour la configuration de build (par exemple, Maven/Gradle) pour garantir que `BlogAspects` est tissé après `BlogCore` et `BlogWeb`.

- **Utiliser le tissage au chargement (LTW)** : Si le tissage à la compilation cause des problèmes dus aux dépendances circulaires, passez au tissage au chargement avec AspectJ. Configurez LTW dans votre application (par exemple, via `@EnableLoadTimeWeaving` de Spring ou un fichier `aop.xml`) pour différer l'application de l'aspect jusqu'à l'exécution, après le chargement des classes.

#### 3. Mettre à jour la configuration du build
Assurez-vous que votre outil de build (Maven, Gradle, etc.) reflète la nouvelle structure de module et résout correctement les dépendances.

**Exemple Maven** :
```xml
<!-- BlogCommon/pom.xml -->
<dependencies>
    <!-- Aucune dépendance -->
</dependencies>

<!-- BlogConfig/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogCore/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogWeb/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogAspects/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogWeb</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>org.aspectj</groupId>
        <artifactId>aspectjrt</artifactId>
        <version>1.9.7</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>aspectj-maven-plugin</artifactId>
            <version>1.14.0</version>
            <configuration>
                <complianceLevel>11</complianceLevel>
                <source>11</source>
                <target>11</target>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>compile</goal>
                        <goal>test-compile</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

**Exemple Gradle** :
```groovy
// BlogCommon/build.gradle
dependencies {
    // Aucune dépendance
}

// BlogConfig/build.gradle
dependencies {
    implementation project(':BlogCommon')
}

// BlogCore/build.gradle
dependencies {
    implementation project(':BlogCommon')
    implementation project(':BlogConfig')
}

// BlogWeb/build.gradle
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogConfig')
}

// BlogAspects/build.gradle
plugins {
    id 'java'
    id 'io.freefair.aspectj.post-compile-weaving' version '6.3.0'
}
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogWeb')
    implementation 'org.aspectj:aspectjrt:1.9.7'
}
```

#### 4. Tester l'application
- Vérifiez que la dépendance circulaire est résolue en construisant et en exécutant l'application.
- Assurez-vous que `LoggingAspect` enregistre les exécutions de méthodes dans `BlogCore` et `BlogWeb` mais pas dans `BlogConfig` (sauf si explicitement souhaité).
- Si vous utilisez Spring, vérifiez l'absence d'erreurs `BeanCurrentlyInCreationException` ou similaires lors de l'initialisation du contexte.
- Testez le tissage AspectJ pour confirmer que les logs apparaissent pour les méthodes correctes.

#### 5. Conseils supplémentaires
- **Utiliser un outil d'analyse des dépendances** : Utilisez des outils comme `mvn dependency:tree` de Maven ou la tâche `dependencies` de Gradle pour détecter toute dépendance circulaire restante.
- **Envisager la granularité des aspects** : Si la journalisation n'est nécessaire que pour des services spécifiques, affinez davantage le pointcut pour cibler des classes ou méthodes spécifiques (par exemple, `execution(* com.example.blogcore.service.*.*(..))`).
- **Éviter AspectJ pour les modules de configuration** : En général, évitez d'appliquer des aspects au code de configuration ou d'infrastructure (comme `BlogConfig`) pour réduire la complexité.

### Structure de dépendance finale
Après restructuration :
```
BlogCommon → BlogConfig → BlogCore → BlogWeb
   ↑                        ↑
   └────── BlogAspects ─────┘
```

### Pourquoi cela fonctionne
- **Rompre le cercle** : Déplacer les dépendances partagées vers `BlogCommon` ou utiliser l'IoC garantit que `BlogConfig` ne dépend pas de `BlogCore`, éliminant la dépendance circulaire.
- **Isoler les aspects** : Placer `LoggingAspect` dans un module séparé (`BlogAspects`) ou réduire son pointcut empêche les problèmes de tissage et maintient la logique de l'aspect indépendante de la chaîne de dépendances.
- **Configuration du build** : Une configuration correcte de l'outil de build garantit que les modules sont compilés et tissés dans le bon ordre.

Cette approche maintient votre fonctionnalité de journalisation AspectJ tout en garantissant une structure de module propre et maintenable. Si vous avez des détails supplémentaires sur votre configuration (par exemple, l'utilisation de Spring, les classes spécifiques causant le cycle), je peux affiner la solution davantage !