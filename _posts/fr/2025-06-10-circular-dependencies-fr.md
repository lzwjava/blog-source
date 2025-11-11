---
audio: false
generated: true
lang: fr
layout: post
title: Dépendances circulaires dans Spring
translated: true
type: note
---

Les dépendances circulaires dans Spring ou Spring Boot se produisent lorsque deux beans ou plus dépendent les uns des autres, directement ou indirectement, lors de l'initialisation. Cela crée un cycle où le mécanisme d'injection de dépendances de Spring ne peut pas résoudre les dépendances car chaque bean nécessite que l'autre soit entièrement initialisé en premier. Ce problème survient généralement lors de la création des beans dans le Spring Application Context, conduisant à une `BeanCurrentlyInCreationException`.

### Pourquoi les Dépendances Circulaires se Produisent
Spring gère les beans dans un conteneur d'injection de dépendances, et les beans sont généralement créés dans un ordre spécifique basé sur leurs dépendances. Lorsque les beans se référencent mutuellement de manière cyclique (par exemple, le Bean A dépend du Bean B, et le Bean B dépend du Bean A), Spring ne peut pas les instancier car il reste bloqué dans une boucle infinie lors de l'initialisation. Ceci est particulièrement courant dans les applications complexes avec des composants fortement couplés.

Le problème est plus susceptible de se produire dans les scénarios suivants :
1. **Injection par Constructeur** : Lorsque les beans sont connectés via des constructeurs, Spring doit résoudre les dépendances au moment de l'instanciation, ce qui peut entraîner des problèmes de circularité si les beans se référencent mutuellement.
2. **Injection par Champ ou Setter avec Initialisation Eager** : Si les beans sont initialisés de manière eager (comportement par défaut pour les beans singleton), Spring tente de résoudre les dépendances immédiatement, exposant les dépendances circulaires.
3. **Relations entre Beans Mal Configurées ou Excessivement Complexes** : Une conception médiocre ou un manque de séparation des préoccupations peut conduire à des cycles non intentionnels.
4. **Annotations comme `@Autowired` ou `@Component`** : L'injection automatique de dépendances dans des composants fortement couplés peut créer involontairement des cycles.

### Exemples Courants de Dépendances Circulaires

#### Exemple 1 : Cycle d'Injection par Constructeur
```java
@Component
public class BeanA {
    private final BeanB beanB;

    @Autowired
    public BeanA(BeanB beanB) {
        this.beanB = beanB;
    }
}

@Component
public class BeanB {
    private final BeanA beanA;

    @Autowired
    public BeanB(BeanA beanA) {
        this.beanA = beanA;
    }
}
```
**Problème** : `BeanA` nécessite `BeanB` dans son constructeur, et `BeanB` nécessite `BeanA` dans son constructeur. Spring ne peut créer aucun des deux beans car chacun dépend de l'autre étant entièrement initialisé en premier.

**Erreur** : `BeanCurrentlyInCreationException: Error creating bean with name 'beanA': Requested bean is currently in creation: Is there an unresolvable circular reference?`

#### Exemple 2 : Cycle d'Injection par Champ
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanA beanA;
}
```
**Problème** : `BeanA` et `BeanB` utilisent tous deux `@Autowired` pour s'injecter mutuellement via des champs. Même si l'injection par champ est plus flexible que l'injection par constructeur, Spring détecte toujours le cycle lors de l'initialisation du bean si les deux sont des beans singleton (portée par défaut).

#### Exemple 3 : Dépendance Circulaire Indirecte
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanC beanC;
}

@Component
public class BeanC {
    @Autowired
    private BeanA beanA;
}
```
**Problème** : `BeanA` dépend de `BeanB`, `BeanB` dépend de `BeanC`, et `BeanC` dépend de `BeanA`, formant un cycle. Cette dépendance indirecte est plus difficile à repérer mais cause le même problème.

#### Exemple 4 : Classes `@Configuration` avec Références Circulaires
```java
@Configuration
public class ConfigA {
    @Autowired
    private ConfigB configB;

    @Bean
    public ServiceA serviceA() {
        return new ServiceA(configB);
    }
}

@Configuration
public class ConfigB {
    @Autowired
    private ConfigA configA;

    @Bean
    public ServiceB serviceB() {
        return new ServiceB(configA);
    }
}
```
**Problème** : Les classes `@Configuration` `ConfigA` et `ConfigB` dépendent l'une de l'autre, créant un cycle lorsque Spring tente d'initialiser les beans définis dans ces classes.

### Causes Courantes dans Spring Boot
- **Auto-Configuration** : L'auto-configuration de Spring Boot peut parfois introduire des dépendances qui mènent à des cycles, surtout lorsque des beans personnalisés interagissent avec ceux auto-configurés.
- **Component Scanning** : Une utilisation excessive de `@ComponentScan` ou des packages mal configurés peuvent récupérer des beans non intentionnels, conduisant à des dépendances cycliques.
- **Conception Fortement Couplée** : Une logique métier qui couple étroitement les services, repositories ou contrôleurs peut créer involontairement des cycles.
- **Mauvaise Utilisation de la Portée Prototype** : Bien que les beans à portée prototype puissent parfois éviter les dépendances circulaires, les combiner avec des beans singleton de manière cyclique peut toujours causer des problèmes.

### Comment Résoudre les Dépendances Circulaires
1. **Utiliser l'Annotation `@Lazy`** :
   - Annotez l'une des dépendances avec `@Lazy` pour retarder son initialisation jusqu'à ce qu'elle soit réellement nécessaire.
   ```java
   @Component
   public class BeanA {
       @Autowired
       @Lazy
       private BeanB beanB;
   }
   ```
   Cela brise le cycle en permettant à `BeanA` d'être partiellement initialisé avant que `BeanB` ne soit résolu.

2. **Passer à l'Injection par Setter ou par Champ** :
   - Au lieu de l'injection par constructeur, utilisez l'injection par setter ou par champ pour l'un des beans afin de permettre à Spring d'initialiser le bean d'abord et d'injecter les dépendances plus tard.
   ```java
   @Component
   public class BeanA {
       private BeanB beanB;

       @Autowired
       public void setBeanB(BeanB beanB) {
           this.beanB = beanB;
       }
   }
   ```

3. **Refactoriser le Code pour Briser le Cycle** :
   - Introduisez une interface ou un composant intermédiaire pour découpler les beans.
   - Exemple : Extrayez une dépendance commune dans un troisième bean ou utilisez une couche de service pour médiatiser les interactions.
   ```java
   public interface Service {
       void performAction();
   }

   @Component
   public class BeanA implements Service {
       @Autowired
       private BeanB beanB;

       public void performAction() {
           // Logique
       }
   }

   @Component
   public class BeanB {
       @Autowired
       private Service service; // Dépend de l'interface, pas directement de BeanA
   }
   ```

4. **Utiliser l'Annotation `@DependsOn`** :
   - Contrôlez explicitement l'ordre d'initialisation des beans pour éviter les cycles dans des cas spécifiques.
   ```java
   @Component
   @DependsOn("beanB")
   public class BeanA {
       @Autowired
       private BeanB beanB;
   }
   ```

5. **Activer le Proxying avec `@EnableAspectJAutoProxy`** :
   - Assurez-vous que Spring utilise des proxies (CGLIB ou JDK dynamic proxies) pour gérer les dépendances, ce qui peut résoudre certains problèmes de circularité en injectant un proxy au lieu du bean actuel.

6. **Réévaluer la Conception** :
   - Les dépendances circulaires indiquent souvent un défaut de conception. Envisagez de refactoriser pour respecter le Principe de Responsabilité Unique ou le Principe d'Inversion des Dépendances.

### Comment Débuguer les Dépendances Circulaires
- **Vérifier la Stack Trace** : La stack trace de `BeanCurrentlyInCreationException` indiquera les beans impliqués dans le cycle.
- **Activer les Logs de Débugage** : Définissez `spring.main.lazy-initialization=true` ou activez les logs de débugage pour `org.springframework` pour voir les détails de création des beans.
- **Utiliser des Outils** : Des outils comme Spring Boot Actuator ou des plugins IDE (par exemple, Spring Tools Suite) peuvent visualiser les dépendances entre beans.

### Prévenir les Dépendances Circulaires
- **Suivre les Bonnes Pratiques** : Utilisez des modèles d'injection de dépendances comme les interfaces ou les abstractions pour réduire le couplage fort.
- **Modulariser le Code** : Décomposez les grandes applications en modules plus petits et faiblement couplés.
- **Tester Tôt** : Exécutez des tests d'intégration pour détecter les dépendances circulaires pendant le développement.
- **Limiter le Component Scanning** : Soyez spécifique avec `@ComponentScan` pour éviter de récupérer des beans inutiles.

### Quand les Dépendances Circulaires sont Moins Probables
- **Portée Prototype** : Les beans avec une portée prototype sont créés à la demande, réduisant la probabilité de circularité (mais ne l'éliminant pas entièrement).
- **Initialisation Lazy** : Activer l'initialisation lazy globale (`spring.main.lazy-initialization=true`) peut différer la création des beans, bien que cela ne puisse que masquer le problème.

### Conclusion
Les dépendances circulaires dans Spring/Spring Boot proviennent d'un couplage fort entre les beans, souvent exacerbé par l'injection par constructeur ou des configurations complexes. Les solutions courantes incluent l'utilisation de `@Lazy`, le passage à l'injection par setter/champ, ou la refactorisation pour briser le cycle. En comprenant la cause racine et en appliquant les bonnes pratiques, vous pouvez prévenir ou résoudre ces problèmes efficacement. Si vous rencontrez une dépendance circulaire spécifique, partagez le code pertinent ou les détails de l'erreur, et je peux vous aider à l'analyser plus en détail !