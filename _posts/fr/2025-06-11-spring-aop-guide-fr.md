---
audio: false
generated: true
lang: fr
layout: post
title: Guide de Spring AOP
translated: true
type: note
---

## 1. Introduction à Spring AOP

Spring AOP (Programmation Orientée Aspect) est un composant clé du Spring Framework qui fournit un moyen de mettre en œuvre des préoccupations transversales (comme la journalisation, la sécurité, la gestion des transactions) séparément de la logique métier.

### Concepts Clés :
- **Préoccupations transversales** : Fonctionnalité qui s'étend sur plusieurs couches (journalisation, sécurité, etc.)
- **Aspect** : Une modularisation d'une préoccupation qui traverse plusieurs classes
- **Point de jonction** : Un point pendant l'exécution du programme (exécution de méthode, gestion d'exception, etc.)
- **Advice** : Action entreprise par un aspect à un point de jonction particulier
- **Pointcut** : Prédicat qui correspond aux points de jonction
- **Tissage** : Liaison des aspects avec d'autres types d'application pour créer un objet conseillé

## 2. Spring AOP vs AspectJ

| Fonctionnalité               | Spring AOP | AspectJ |
|-----------------------|-----------|---------|
| Implémentation        | Proxy à l'exécution | Tissage à la compilation/au chargement |
| Performance           | Plus lent | Plus rapide |
| Points de jonction supportés | Exécution de méthode uniquement | Tous (méthode, constructeur, accès aux champs, etc.) |
| Complexité            | Plus simple | Plus complexe |
| Dépendance            | Aucune dépendance supplémentaire | Requiert le compilateur/tisseur AspectJ |

## 3. Composants AOP de Base

### 3.1 Aspects
Une classe annotée avec `@Aspect` contenant des advices et des pointcuts.

```java
@Aspect
@Component
public class LoggingAspect {
    // les advices et pointcuts iront ici
}
```

### 3.2 Types d'Advice

1. **Before** : S'exécute avant un point de jonction
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("Avant l'exécution de la méthode");
   }
   ```

2. **AfterReturning** : S'exécute après qu'un point de jonction se termine normalement
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("Méthode retournée : " + result);
   }
   ```

3. **AfterThrowing** : S'exécute si une méthode se termine en lançant une exception
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("Exception lancée : " + ex.getMessage());
   }
   ```

4. **After (Finally)** : S'exécute après un point de jonction quel que soit le résultat
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("Après l'exécution de la méthode (finally)");
   }
   ```

5. **Around** : Encapsule un point de jonction, advice le plus puissant
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("Avant proceeding");
       Object result = joinPoint.proceed();
       System.out.println("Après proceeding");
       return result;
   }
   ```

### 3.3 Expressions Pointcut

Les pointcuts définissent où l'advice doit être appliqué en utilisant des expressions :

- **Execution** : Correspond à l'exécution de méthode
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **Within** : Correspond à tous les points de jonction dans certains types
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **this** : Correspond aux beans qui sont des instances d'un type donné
- **target** : Correspond aux beans qui sont assignables à un type donné
- **args** : Correspond aux méthodes avec des types d'arguments spécifiques
- **@annotation** : Correspond aux méthodes avec des annotations spécifiques

### 3.4 Combinaison de Pointcuts

Les pointcuts peuvent être combinés en utilisant des opérateurs logiques :
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. Étapes d'Implémentation

### 4.1 Configuration

1. Ajouter la dépendance Spring AOP (si n'utilise pas Spring Boot) :
   ```xml
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-aop</artifactId>
       <version>${spring.version}</version>
   </dependency>
   <dependency>
       <groupId>org.aspectj</groupId>
       <artifactId>aspectjweaver</artifactId>
       <version>${aspectj.version}</version>
   </dependency>
   ```

2. Pour Spring Boot, inclure simplement `spring-boot-starter-aop` :
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. Activer AOP dans votre configuration :
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 Création d'Aspects

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("Entrée : {}.{}() avec arguments = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("Sortie : {}.{}() avec résultat = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} exécuté en {} ms", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 Annotations Personnalisées

Créer des annotations personnalisées pour marquer les méthodes pour un comportement AOP spécifique :

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

Puis l'utiliser sur les méthodes :
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // implémentation
    }
}
```

## 5. Sujets Avancés

### 5.1 Ordre des Aspects

Contrôler l'ordre d'exécution des aspects avec `@Order` :
```java
@Aspect
@Component
@Order(1)
public class LoggingAspect {
    // ...
}

@Aspect
@Component
@Order(2)
public class ValidationAspect {
    // ...
}
```

### 5.2 Accès aux Informations de Méthode

Dans les méthodes d'advice, vous pouvez accéder à :
- `JoinPoint` (pour Before, After, AfterReturning, AfterThrowing)
- `ProceedingJoinPoint` (pour Around)

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 Gestion des Exceptions

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // Logger l'exception, envoyer une alerte, etc.
}
```

### 5.4 Mécanismes de Proxification

Spring AOP utilise deux types de proxies :
- **JDK Dynamic Proxy** : Par défaut pour les interfaces
- **CGLIB Proxy** : Utilisé quand aucune interface n'est disponible (peut être forcé avec `proxyTargetClass=true`)

## 6. Bonnes Pratiques

1. **Garder les aspects focalisés** : Chaque aspect devrait gérer une préoccupation transversale spécifique
2. **Utiliser des noms de pointcut significatifs** : Rend le code plus lisible
3. **Éviter les opérations coûteuses dans les aspects** : Ils s'exécutent pour chaque point de jonction correspondant
4. **Être prudent avec l'advice Around** : Toujours appeler `proceed()` sauf si vous empêchez intentionnellement l'exécution
5. **Tester les aspects minutieusement** : Ils affectent plusieurs parties de votre application
6. **Documenter les aspects** : Surtout s'ils modifient significativement le comportement
7. **Considérer la performance** : Les pointcuts complexes ou de nombreux aspects peuvent impacter les performances

## 7. Cas d'Utilisation Courants

1. **Journalisation** : Entrée/sortie de méthode, paramètres, valeurs de retour
2. **Monitoring des Performances** : Mesurer le temps d'exécution
3. **Gestion des Transactions** (Bien que généralement gérée par `@Transactional` de Spring)
4. **Sécurité** : Vérifications d'autorisation
5. **Validation** : Validation des paramètres
6. **Gestion des Erreurs** : Gestion cohérente des exceptions
7. **Cache** : Mise en cache des résultats de méthode
8. **Audit** : Suivi de qui a appelé quoi et quand

## 8. Limitations

1. Fonctionne uniquement avec les beans gérés par Spring
2. Seuls les points de jonction d'exécution de méthode sont supportés
3. Ne peut pas conseiller les classes ou méthodes final
4. L'auto-invocation (méthode dans une classe appelant une autre méthode de la même classe) contourne le proxy
5. Expressions pointcut limitées comparé à AspectJ

## 9. Dépannage

**Problème** : Advice ne s'exécute pas
- Vérifier si le bean est géré par Spring
- Vérifier que l'expression pointcut correspond aux méthodes visées
- S'assurer que `@EnableAspectJAutoProxy` est présent

**Problème** : Advice Around ne procède pas
- S'assurer d'appeler `proceed()` sur `ProceedingJoinPoint`

**Problème** : Type de proxy incorrect
- Utiliser `@EnableAspectJAutoProxy(proxyTargetClass=true)` pour forcer CGLIB

## 10. Conclusion

Spring AOP fournit un moyen puissant mais simple de mettre en œuvre des préoccupations transversales dans votre application. Bien qu'il ait certaines limitations comparé à AspectJ complet, il s'intègre parfaitement avec Spring et couvre la plupart des cas d'utilisation courants. En suivant les modèles et bonnes pratiques décrits dans ce guide, vous pouvez modulariser efficacement les préoccupations transversales et garder votre logique métier propre et focalisée.

---

Même si Spring AOP n'utilise pas les capacités de tissage d'AspectJ (il utilise plutôt AOP basé sur les proxies), vous avez toujours besoin de la dépendance `aspectjweaver` pour plusieurs raisons importantes :

### 1. **Support des Annotations AspectJ**
Spring AOP utilise les **annotations** d'AspectJ (comme `@Aspect`, `@Pointcut`, `@Before`, `@After`, etc.) pour définir les aspects et les advices. Ces annotations proviennent de la bibliothèque `aspectjweaver`.

- Sans elle, vous auriez des erreurs de compilation lors de l'utilisation de `@Aspect` ou d'autres annotations AOP.

### 2. **Langage d'Expression Pointcut**
Spring AOP emprunte le **langage d'expression pointcut** d'AspectJ pour définir où l'advice doit être appliqué (par exemple, `execution(* com.example.service.*.*(..))`).

- Le `aspectjweaver` fournit l'analyseur syntaxique et la logique de correspondance pour ces expressions.

### 3. **Support pour les Points de Jonction Supplémentaires (Limité)**
Bien que Spring AOP ne supporte que les points de jonction d'**exécution de méthode** (contrairement à AspectJ, qui supporte les constructeurs, l'accès aux champs, etc.), il s'appuie toujours sur le mécanisme de correspondance pointcut sous-jacent d'AspectJ.

### 4. **Tissage au Chargement (Optionnel)**
Si vous décidez d'utiliser le **Tissage au Chargement (LTW)** avec Spring AOP (ce qui est rare mais possible), `aspectjweaver` est requis. LTW permet de tisser les aspects au moment du chargement des classes au lieu d'utiliser des proxies.

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **Compatibilité avec @EnableAspectJAutoProxy**
Lorsque vous utilisez `@EnableAspectJAutoProxy`, Spring utilise en interne l'infrastructure d'AspectJ pour traiter les annotations AOP, même s'il n'effectue pas le tissage complet d'AspectJ.

---

### **En Avez-Vous Toujours Besoin ?**
- **Si vous utilisez Spring Boot (`spring-boot-starter-aop`)** : Non, car il inclut transitivement `aspectjweaver`.
- **Si vous utilisez Spring AOP standard** : Oui, vous devez l'inclure explicitement.

### **Alternatives ?**
- Si vous utilisiez **AspectJ complet** (tissage à la compilation ou au chargement), vous auriez besoin de `aspectjrt` et `aspectjtools` également.
- Mais pour **Spring AOP**, `aspectjweaver` seul est suffisant.

### **Conclusion**
Spring AOP est **basé sur les proxies**, mais il **réutilise les annotations et la syntaxe pointcut d'AspectJ**, c'est pourquoi `aspectjweaver` est requis. Il comble le fossé entre l'approche par proxy de Spring et le modèle AOP plus puissant d'AspectJ.