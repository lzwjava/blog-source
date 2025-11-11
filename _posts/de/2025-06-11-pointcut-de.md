---
audio: false
generated: true
lang: de
layout: post
title: Verstehen von Pointcut-Ausdrücken
translated: true
type: note
---

Sie bitten um einen umfassenden Leitfaden zu AspectJ Pointcut-Ausdrücken, speziell mit Fokus auf `execution`, der Verwendung von Wildcards, dem Abgleichen von Klassennamen (Präfix/Suffix) und auch über andere Advice-Typen wie `@AfterReturning`. Lassen Sie uns das aufschlüsseln.

### Grundlegendes zu Pointcut-Ausdrücken in Spring AOP (AspectJ-Syntax)

Spring AOP verwendet AspectJ Pointcut-Ausdrücke, um zu bestimmen, *wo* ein Advice (wie `@Before`, `@AfterReturning` usw.) angewendet werden soll. Der Kern Ihrer Frage dreht sich um den `execution` Pointcut Designator, der am häufigsten verwendet wird.

#### Der `execution` Pointcut Designator

Der `execution` Pointcut Designator passt auf Methodenausführungen. Seine allgemeine Syntax lautet:

`execution(modifiers-pattern? ret-type-pattern declaring-type-pattern?name-pattern(param-pattern) throws-pattern?)`

Lassen Sie uns die Komponenten aufschlüsseln:

*   **`modifiers-pattern?`**: Optional. Passt auf Methodenmodifikatoren (z.B. `public`, `private`, `protected`).
*   **`ret-type-pattern`**: Erforderlich. Passt auf den Rückgabetyp der Methode.
*   **`declaring-type-pattern?`**: Optional. Passt auf den vollqualifizierten Klassennamen, in dem die Methode deklariert ist.
*   **`name-pattern`**: Erforderlich. Passt auf den Namen der Methode.
*   **`param-pattern`**: Erforderlich. Passt auf die Parameter der Methode.
*   **`throws-pattern?`**: Optional. Passt auf die von der Methode geworfenen Exceptions.

#### Ihr Beispiel: `@Before("execution(* com.example.service.*.*(..))")`

Lassen Sie uns Ihr gegebenes Beispiel sezieren:

*   `@Before`: Dies ist eine Advice-Annotation, was bedeutet, dass die annotierte Methode *vor* dem gematchten Join Point ausgeführt wird.
*   `execution()`: Der Pointcut Designator.
*   `*`: Passt auf jeden Rückgabetyp.
*   `com.example.service.*.*`:
    *   `com.example.service`: Passt auf das Package `com.example.service`.
    *   `.*`: Das erste `*` nach `service` passt auf jede Klasse innerhalb des `com.example.service` Packages.
    *   `.`: Trenner zwischen Package/Klasse und Methode.
    *   `*`: Das zweite `*` passt auf jeden Methodennamen innerhalb dieser Klassen.
*   `(..)`: Passt auf eine beliebige Anzahl von Parametern (null oder mehr, von jedem Typ).

**Auf Deutsch gesagt:** Dieser Pointcut passt auf die Ausführung *jeder Methode* in *jeder Klasse* innerhalb des `com.example.service` Packages (und seinen direkten Unter-Packages, falls Klassen direkt in `com.example.service` sind).

---

### Wildcards in Pointcut-Ausdrücken

Wildcards sind entscheidend für die Erstellung flexibler Pointcut-Ausdrücke.

*   **`*` (einzelner Asterisk)**:
    *   Passt auf jedes einzelne Element in einem Namensmuster (z.B. jeder Rückgabetyp, jeder Klassenname, jeder Methodenname).
    *   Passt auf jedes einzelne Segment in einem Paketnamen (z.B. `com.example.*.service` würde auf `com.example.foo.service` passen).
*   **`..` (doppelter Punkt)**:
    *   **In Paketmustern**: Passt auf null oder mehr Segmente in einem Paketnamen.
        *   `com.example..service`: Passt auf `com.example.service`, `com.example.foo.service`, `com.example.foo.bar.service`, usw.
    *   **In Parametermustern**: Passt auf null oder mehr Argumente eines beliebigen Typs.
        *   `(..)`: Passt auf eine beliebige Anzahl von Argumenten.
        *   `(java.lang.String, ..)`: Passt auf Methoden mit einem `String` als erstes Argument, gefolgt von einer beliebigen Anzahl weiterer Argumente.
        *   `(.., java.lang.Long)`: Passt auf Methoden mit einer beliebigen Anzahl anfänglicher Argumente, die mit einem `Long` enden.

---

### Abgleichen von Klassennamen

#### 1. Abgleichen von Klassennamen mit Suffix

Um Klassen abzugleichen, die mit einem bestimmten Suffix enden, setzen Sie den Wildcard vor das Suffix.

**Beispiel: Alle Klassen abgleichen, die auf `ServiceImpl` enden**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

*   `*ServiceImpl`: Passt auf jeden Klassennamen, der auf `ServiceImpl` endet.

**Beispiel: Alle Klassen abgleichen, die auf `Controller` enden, in jedem Unter-Package von `com.example.web`**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

*   `com.example.web..`: Passt auf `com.example.web` und alle seine Unter-Packages.
*   `*Controller`: Passt auf jeden Klassennamen, der auf `Controller` endet.

#### 2. Abgleichen von Klassennamen mit Präfix

Um Klassen abzugleichen, die mit einem bestimmten Präfix beginnen, setzen Sie den Wildcard nach dem Präfix.

**Beispiel: Alle Klassen abgleichen, die mit `User` beginnen**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

*   `User*`: Passt auf jeden Klassennamen, der mit `User` beginnt.

**Beispiel: Alle Klassen abgleichen, die mit `Admin` im `com.example.admin` Package beginnen**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. Abgleichen spezifischer Klassennamen (Exakte Übereinstimmung)

Für exakte Übereinstimmungen werden keine Wildcards benötigt.

**Beispiel: Nur Methoden in `com.example.service.UserServiceImpl` abgleichen**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### Verschiedene Arten von Pointcut Designators

Während `execution` der gebräuchlichste ist, bietet AspectJ mehrere andere Pointcut Designators an, um Join Points zu spezifizieren. Sie können diese mit logischen Operatoren (`and`, `or`, `not` oder `&&`, `||`, `!`) kombinieren.

Hier sind die wichtigsten:

1.  **`execution()`**: Wie besprochen, passt auf Methodenausführungen.
    *   Beispiel: `@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`**: Passt auf Join Points, bei denen sich der Code innerhalb eines bestimmten Typs (Klasse) befindet. Dies wird oft verwendet, um den Geltungsbereich anderer Pointcuts einzuschränken.
    *   Beispiel: `@Before("within(com.example.service.*) && execution(* *(..))")`
        *   Dies kombiniert `within` und `execution`. Es bedeutet "jede Methodenausführung innerhalb jeder Klasse im `com.example.service` Package." Der `execution`-Teil ist dann nur ein Wildcard für jede Methode, da `within` das Abgleichen der Klassen übernimmt.

3.  **`this()`**: Passt auf Join Points, bei denen der Proxy *selbst* eine Instanz des gegebenen Typs ist. Dies wird weniger häufig für einfachen Advice verwendet und mehr für Introductions oder Self-Invocation-Probleme.
    *   Beispiel: `@Around("this(com.example.service.UserService)")`
        *   Passt, wenn der AOP-Proxy `UserService` implementiert.

4.  **`target()`**: Passt auf Join Points, bei denen das *Zielobjekt* (das tatsächliche, beratene Objekt, nicht der Proxy) eine Instanz des gegebenen Typs ist. Dies ist oft intuitiver als `this()`, wenn Ihnen die zugrundeliegende Implementierung wichtig ist.
    *   Beispiel: `@Around("target(com.example.service.UserServiceImpl)")`
        *   Passt, wenn das Zielobjekt eine Instanz von `UserServiceImpl` ist.

5.  **`args()`**: Passt auf Join Points, bei denen die Argumente von einem bestimmten Typ sind oder einem bestimmten Muster entsprechen.
    *   Beispiel: `@Before("execution(* com.example.service.*.*(String, ..))")`
        *   Passt auf Methoden, bei denen das erste Argument ein `String` ist.
    *   Beispiel: `@Before("args(java.lang.String, int)")`
        *   Passt auf Methoden, die genau einen `String` gefolgt von einem `int` entgegennehmen.
    *   Beispiel: `@Before("args(name, age)")` wobei `name` und `age` dann an die Advice-Methodenparameter gebunden werden können.

6.  **`bean()`**: (Spring-spezifisch) Passt auf Methoden, die auf Spring Beans mit bestimmten Namen oder Namensmustern ausgeführt werden.
    *   Beispiel: `@Before("bean(userService) && execution(* *(..))")`
        *   Passt auf jede Methodenausführung auf der Spring Bean mit dem Namen "userService".
    *   Beispiel: `@Before("bean(*Service) && execution(* *(..))")`
        *   Passt auf jede Methodenausführung auf Spring Beans, deren Namen auf "Service" enden.

7.  **`@annotation()`**: Passt auf Join Points, bei denen die Zielmethode (oder Klasse für `within`) mit einer bestimmten Annotation annotiert ist.
    *   Beispiel: `@Before("@annotation(com.example.annotation.Loggable)")`
        *   Passt auf jede Methode, die mit `@Loggable` annotiert ist.
    *   Beispiel: `@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        *   Passt auf jede Methodenausführung, die mit `@Transactional` annotiert ist.

8.  **`@within()`**: Passt auf Join Points, bei denen der deklarierende Typ (Klasse) mit einer bestimmten Annotation annotiert ist.
    *   Beispiel: `@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        *   Passt auf jede Methodenausführung innerhalb einer Klasse, die mit `@Service` annotiert ist.

9.  **`@target()`**: Passt auf Join Points, bei denen die Klasse des Zielobjekts die gegebene Annotation hat.
    *   Beispiel: `@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`**: Passt auf Join Points, bei denen der Laufzeittyp der tatsächlichen, an die Methode übergebenen Argumente Annotationen des gegebenen Typs/der gegebenen Typen hat.
    *   Beispiel: `@Before("@args(com.example.annotation.ValidInput)")`

---

### Advice-Typen (Annotationen)

Sie haben `@AfterReturning` und "alle anderen, die wir in Annotationen verwenden können" erwähnt. Spring AOP bietet mehrere Advice-Typen, die jeweils zu einem unterschiedlichen Zeitpunkt im Lebenszyklus des Join Points ausgeführt werden:

1.  **`@Before`**:
    *   Wird *vor* der Ausführung der gematchten Methode ausgeführt.
    *   Beispiel: Protokollieren von Anfragedetails, bevor eine Service-Methode läuft.
    *   Kann die Ausführung der Methode nicht verhindern oder deren Rückgabewert verändern.

2.  **`@AfterReturning`**:
    *   Wird *nach* der gematchten Methode ausgeführt, wenn sie *erfolgreich* zurückkehrt (ohne eine Exception zu werfen).
    *   Kann auf den Rückgabewert der Methode zugreifen.
    *   Syntax: `@AfterReturning(pointcut="yourPointcut()", returning="result")`
    *   Beispiel:
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("User retrieved: " + user);
        }
        ```
        *Hinweis: Der Name des `returning`-Attributs (`user` in diesem Fall) muss mit dem Parameternamen in der Advice-Methode übereinstimmen.*

3.  **`@AfterThrowing`**:
    *   Wird *nach* der gematchten Methode ausgeführt, wenn sie eine Exception wirft.
    *   Kann auf die geworfene Exception zugreifen.
    *   Syntax: `@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    *   Beispiel:
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Exception occurred: " + ex.getMessage());
        }
        ```
        *Hinweis: Der Name des `throwing`-Attributs (`ex` in diesem Fall) muss mit dem Parameternamen in der Advice-Methode übereinstimmen.*

4.  **`@After` (finally Advice)**:
    *   Wird *nach* Abschluss der gematchten Methode ausgeführt, unabhängig davon, ob sie erfolgreich zurückgekehrt ist oder eine Exception geworfen hat.
    *   Ähnlich einem `finally`-Block.
    *   Beispiel: Freigeben von Ressourcen, unabhängig vom Methodenergebnis.
    *   ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Order process completed (cleanup)");
        }
        ```

5.  **`@Around`**:
    *   Der mächtigste und flexibelste Advice-Typ.
    *   Wird *um* die Ausführung der gematchten Methode herum ausgeführt.
    *   Sie sind dafür verantwortlich, die eigentliche Methode mit `ProceedingJoinPoint.proceed()` aufzurufen.
    *   Kann die Argumente und Rückgabewerte der Methode prüfen, modifizieren oder sogar unterdrücken.
    *   Kann von der beratenen Methode geworfene Exceptions abfangen und behandeln.
    *   Beispiel: Performance-Monitoring, Transaktionsverwaltung, Caching.
    *   ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // Führe die ursprüngliche Methode aus
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " executed in " + (end - start) + "ms");
                return result;
            }
        }
        ```

### Definieren wiederverwendbarer Pointcuts

Für bessere Lesbarkeit und Wiederverwendbarkeit können Sie benannte Pointcuts mit `@Pointcut` definieren.

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // Definiere einen Pointcut für alle Methoden im com.example.service Package
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // Definiere einen Pointcut für Methoden, die ein User-Objekt zurückgeben
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // Verwendung des definierten Pointcuts
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Before service method execution.");
    }

    // Kombinieren von Pointcuts mit logischem UND
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("Service method returned user: " + user);
    }

    // Sie können auch Pointcuts mit Argumenten definieren
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Saving entity: " + entity);
    }
}
```

Dieser umfassende Leitfaden deckt die Grundlagen von Pointcut-Ausdrücken, der Verwendung von Wildcards, dem Abgleichen von Klassennamen und den verschiedenen Advice-Typen in Spring AOP ab. Die Beherrschung dieser Konzepte ermöglicht es Ihnen, präzise zu steuern, wo und wann Ihre übergreifenden Belange (Cross-Cutting Concerns) angewendet werden.