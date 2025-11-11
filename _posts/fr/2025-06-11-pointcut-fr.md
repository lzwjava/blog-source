---
audio: false
generated: true
lang: fr
layout: post
title: Comprendre les expressions Pointcut
translated: true
type: note
---

Vous demandez un guide complet sur les expressions de pointcut AspectJ, en vous concentrant spécifiquement sur `execution`, sur la façon d'utiliser les caractères génériques, de faire correspondre les noms de classes (préfixe/suffixe), et également sur d'autres types d'advice comme `@AfterReturning`. Décomposons cela.

### Comprendre les expressions de pointcut dans Spring AOP (Syntaxe AspectJ)

Spring AOP utilise les expressions de pointcut d'AspectJ pour déterminer *où* un advice (comme `@Before`, `@AfterReturning`, etc.) doit être appliqué. Le cœur de votre question tourne autour du designator de pointcut `execution`, qui est le plus couramment utilisé.

#### Le designator de pointcut `execution`

Le designator de pointcut `execution` correspond aux exécutions de méthodes. Sa syntaxe générale est :

`execution(modifiers-pattern? ret-type-pattern declaring-type-pattern?name-pattern(param-pattern) throws-pattern?)`

Décomposons les composants :

* **`modifiers-pattern?`** : Optionnel. Correspond aux modificateurs de méthode (par exemple, `public`, `private`, `protected`).
* **`ret-type-pattern`** : Requis. Correspond au type de retour de la méthode.
* **`declaring-type-pattern?`** : Optionnel. Correspond au nom de classe complet où la méthode est déclarée.
* **`name-pattern`** : Requis. Correspond au nom de la méthode.
* **`param-pattern`** : Requis. Correspond aux paramètres de la méthode.
* **`throws-pattern?`** : Optionnel. Correspond aux exceptions levées par la méthode.

#### Votre exemple : `@Before("execution(* com.example.service.*.*(..))")`

Disséquons votre exemple donné :

* `@Before` : Il s'agit d'une annotation d'advice, ce qui signifie que la méthode annotée s'exécutera *avant* le point de jointure correspondant.
* `execution()` : Le designator de pointcut.
* `*` : Correspond à n'importe quel type de retour.
* `com.example.service.*.*` :
    * `com.example.service` : Correspond au package `com.example.service`.
    * `.*` : Le premier `*` après `service` correspond à n'importe quelle classe dans le package `com.example.service`.
    * `.` : Séparateur entre le package/la classe et la méthode.
    * `*` : Le deuxième `*` correspond à n'importe quel nom de méthode dans ces classes.
* `(..)` : Correspond à n'importe quel nombre de paramètres (zéro ou plus, de n'importe quel type).

**En français simple :** Ce pointcut correspond à l'exécution de *n'importe quelle méthode* dans *n'importe quelle classe* du package `com.example.service` (et ses sous-packages directs, si des classes se trouvent directement dans `com.example.service`).

---

### Caractères génériques dans les expressions de pointcut

Les caractères génériques sont cruciaux pour créer des expressions de pointcut flexibles.

* **`*` (astérisque simple)** :
    * Correspond à n'importe quel élément unique dans un modèle de nom (par exemple, n'importe quel type de retour, n'importe quel nom de classe, n'importe quel nom de méthode).
    * Correspond à n'importe quel segment unique dans un nom de package (par exemple, `com.example.*.service` correspondrait à `com.example.foo.service`).
* **`..` (double point)** :
    * **Dans les modèles de package** : Correspond à zéro ou plusieurs segments dans un nom de package.
        * `com.example..service` : Correspond à `com.example.service`, `com.example.foo.service`, `com.example.foo.bar.service`, etc.
    * **Dans les modèles de paramètres** : Correspond à zéro ou plusieurs arguments de n'importe quel type.
        * `(..)` : Correspond à n'importe quel nombre d'arguments.
        * `(java.lang.String, ..)` : Correspond aux méthodes avec un `String` comme premier argument, suivi de n'importe quel nombre d'autres arguments.
        * `(.., java.lang.Long)` : Correspond aux méthodes avec n'importe quel nombre d'arguments initiaux, se terminant par un `Long`.

---

### Faire correspondre les noms de classes

#### 1. Faire correspondre un nom de classe par suffixe

Pour faire correspondre les classes se terminant par un suffixe spécifique, vous placez le caractère générique avant le suffixe.

**Exemple : Faire correspondre toutes les classes se terminant par `ServiceImpl`**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

* `*ServiceImpl` : Correspond à n'importe quel nom de classe qui se termine par `ServiceImpl`.

**Exemple : Faire correspondre toutes les classes se terminant par `Controller` dans n'importe quel sous-package de `com.example.web`**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

* `com.example.web..` : Correspond à `com.example.web` et n'importe lequel de ses sous-packages.
* `*Controller` : Correspond à n'importe quel nom de classe se terminant par `Controller`.

#### 2. Faire correspondre un nom de classe par préfixe

Pour faire correspondre les classes commençant par un préfixe spécifique, vous placez le caractère générique après le préfixe.

**Exemple : Faire correspondre toutes les classes commençant par `User`**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

* `User*` : Correspond à n'importe quel nom de classe qui commence par `User`.

**Exemple : Faire correspondre toutes les classes commençant par `Admin` dans le package `com.example.admin`**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. Faire correspondre des noms de classes spécifiques (correspondance exacte)

Aucun caractère générique n'est nécessaire pour les correspondances exactes.

**Exemple : Faire correspondre les méthodes uniquement dans `com.example.service.UserServiceImpl`**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### Différents types de designators de pointcut

Bien que `execution` soit le plus courant, AspectJ fournit plusieurs autres designators de pointcut pour spécifier les points de jointure. Vous pouvez les combiner en utilisant des opérateurs logiques (`and`, `or`, `not` ou `&&`, `||`, `!`).

Voici les plus importants :

1.  **`execution()`** : Comme discuté, correspond aux exécutions de méthodes.
    * Exemple : `@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`** : Correspond aux points de jointure où le code se trouve dans un certain type (classe). Ceci est souvent utilisé pour restreindre la portée d'autres pointcuts.
    * Exemple : `@Before("within(com.example.service.*) && execution(* *(..))")`
        * Ceci combine `within` et `execution`. Cela signifie "toute exécution de méthode dans n'importe quelle classe du package `com.example.service`." La partie `execution` est alors juste un caractère générique pour n'importe quelle méthode, car `within` gère la correspondance des classes.

3.  **`this()`** : Correspond aux points de jointure où le proxy *lui-même* est une instance du type donné. Ceci est moins couramment utilisé pour les advice simples et davantage pour les introductions ou les problèmes d'auto-invocation.
    * Exemple : `@Around("this(com.example.service.UserService)")`
        * Correspond si le proxy AOP implémente `UserService`.

4.  **`target()`** : Correspond aux points de jointure où l'*objet cible* (l'objet réel étant conseillé, pas le proxy) est une instance du type donné. Ceci est souvent plus intuitif que `this()` lorsque vous vous souciez de l'implémentation sous-jacente.
    * Exemple : `@Around("target(com.example.service.UserServiceImpl)")`
        * Correspond si l'objet cible est une instance de `UserServiceImpl`.

5.  **`args()`** : Correspond aux points de jointure où les arguments sont d'un certain type ou correspondent à un certain modèle.
    * Exemple : `@Before("execution(* com.example.service.*.*(String, ..))")`
        * Correspond aux méthodes où le premier argument est un `String`.
    * Exemple : `@Before("args(java.lang.String, int)")`
        * Correspond aux méthodes qui prennent exactement un `String` suivi d'un `int`.
    * Exemple : `@Before("args(name, age)")` où `name` et `age` peuvent ensuite être liés aux paramètres de la méthode d'advice.

6.  **`bean()`** : (Spécifique à Spring) Correspond aux méthodes exécutées sur des beans Spring avec des noms spécifiques ou des modèles de noms.
    * Exemple : `@Before("bean(userService) && execution(* *(..))")`
        * Correspond à toute exécution de méthode sur le bean Spring nommé "userService".
    * Exemple : `@Before("bean(*Service) && execution(* *(..))")`
        * Correspond à toute exécution de méthode sur les beans Spring dont les noms se terminent par "Service".

7.  **`@annotation()`** : Correspond aux points de jointure où la méthode cible (ou la classe pour `within`) est annotée avec une annotation spécifique.
    * Exemple : `@Before("@annotation(com.example.annotation.Loggable)")`
        * Correspond à toute méthode qui est annotée avec `@Loggable`.
    * Exemple : `@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        * Correspond à toute exécution de méthode qui est annotée avec `@Transactional`.

8.  **`@within()`** : Correspond aux points de jointure où le type déclarant (classe) est annoté avec une annotation spécifique.
    * Exemple : `@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        * Correspond à toute exécution de méthode dans une classe qui est annotée avec `@Service`.

9.  **`@target()`** : Correspond aux points de jointure où la classe de l'objet cible a l'annotation donnée.
    * Exemple : `@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`** : Correspond aux points de jointure où le type d'exécution des arguments réels passés à la méthode a des annotations du type donné.
    * Exemple : `@Before("@args(com.example.annotation.ValidInput)")`

---

### Types d'advice (Annotations)

Vous avez mentionné `@AfterReturning` et "tout autre que nous pouvons utiliser dans les annotations". Spring AOP fournit plusieurs types d'advice, chacun s'exécutant à un point différent du cycle de vie du point de jointure :

1.  **`@Before`** :
    * S'exécute *avant* l'exécution de la méthode correspondante.
    * Exemple : Journaliser les détails de la requête avant l'exécution d'une méthode de service.
    * Ne peut pas empêcher la méthode de s'exécuter ou modifier sa valeur de retour.

2.  **`@AfterReturning`** :
    * S'exécute *après* que la méthode correspondante a retourné *avec succès* (sans lever d'exception).
    * Peut accéder à la valeur de retour de la méthode.
    * Syntaxe : `@AfterReturning(pointcut="yourPointcut()", returning="result")`
    * Exemple :
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("User retrieved: " + user);
        }
        ```
        *Note : Le nom de l'attribut `returning` (`user` dans ce cas) doit correspondre au nom du paramètre dans la méthode d'advice.*

3.  **`@AfterThrowing`** :
    * S'exécute *après* que la méthode correspondante a levé une exception.
    * Peut accéder à l'exception levée.
    * Syntaxe : `@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    * Exemple :
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Exception occurred: " + ex.getMessage());
        }
        ```
        *Note : Le nom de l'attribut `throwing` (`ex` dans ce cas) doit correspondre au nom du paramètre dans la méthode d'advice.*

4.  **`@After` (advice finally)** :
    * S'exécute *après* que la méthode correspondante s'est terminée, qu'elle ait retourné une valeur avec succès ou levé une exception.
    * Similaire à un bloc `finally`.
    * Exemple : Libérer des ressources, indépendamment du résultat de la méthode.
    * ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Order process completed (cleanup)");
        }
        ```

5.  **`@Around`** :
    * Le type d'advice le plus puissant et le plus flexible.
    * S'exécute *autour* de l'exécution de la méthode correspondante.
    * Vous êtes responsable de l'invocation de la méthode réelle en utilisant `ProceedingJoinPoint.proceed()`.
    * Peut inspecter, modifier ou même supprimer les arguments et la valeur de retour de la méthode.
    * Peut attraper et gérer les exceptions levées par la méthode conseillée.
    * Exemple : Surveillance des performances, gestion des transactions, mise en cache.
    * ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // Exécute la méthode originale
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " executed in " + (end - start) + "ms");
                return result;
            }
        }
        ```

### Définir des pointcuts réutilisables

Pour une meilleure lisibilité et réutilisabilité, vous pouvez définir des pointcuts nommés en utilisant `@Pointcut`.

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // Définir un pointcut pour toutes les méthodes dans le package com.example.service
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // Définir un pointcut pour les méthodes qui retournent un objet User
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // Utiliser le pointcut défini
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Before service method execution.");
    }

    // Combiner des pointcuts avec un ET logique
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("Service method returned user: " + user);
    }

    // Vous pouvez également définir des pointcuts avec des arguments
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Saving entity: " + entity);
    }
}
```

Ce guide complet couvre les bases des expressions de pointcut, l'utilisation des caractères génériques, la correspondance des noms de classes et les différents types d'advice dans Spring AOP. Maîtriser ces concepts vous permettra de contrôler avec précision où et quand vos préoccupations transversales sont appliquées.