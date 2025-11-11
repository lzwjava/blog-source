---
audio: false
generated: true
lang: de
layout: post
title: Leitfaden zu Spring AOP
translated: true
type: note
---

## 1. Einführung in Spring AOP

Spring AOP (Aspektorientierte Programmierung) ist eine Schlüsselkomponente des Spring Frameworks, die eine Möglichkeit bietet, übergreifende Belange (wie Logging, Sicherheit, Transaktionsverwaltung) separat von der Geschäftslogik zu implementieren.

### Wichtige Konzepte:
- **Übergreifende Belange (Cross-cutting concerns)**: Funktionalität, die mehrere Ebenen umfasst (Logging, Sicherheit, etc.)
- **Aspekt (Aspect)**: Eine Modularisierung eines Belangs, der mehrere Klassen betrifft
- **Verbindungspunkt (Join point)**: Ein Punkt während der Programmausführung (Methodenausführung, Ausnahmebehandlung, etc.)
- **Rat (Advice)**: Aktion, die von einem Aspekt an einem bestimmten Verbindungspunkt durchgeführt wird
- **Schnittpunkt (Pointcut)**: Prädikat, das Verbindungspunkte abgleicht
- **Weber (Weaving)**: Verknüpfen von Aspekten mit anderen Anwendungstypen, um ein beratenes Objekt zu erstellen

## 2. Spring AOP vs AspectJ

| Merkmal               | Spring AOP | AspectJ |
|-----------------------|-----------|---------|
| Implementierung       | Laufzeit-Proxying | Compile-Time/Load-Time-Weaving |
| Leistung              | Langsamer | Schneller |
| Unterstützte Verbindungspunkte | Nur Methodenausführung | Alle (Methode, Konstruktor, Feldzugriff, etc.) |
| Komplexität           | Einfacher | Komplexer |
| Abhängigkeit          | Keine zusätzlichen Abhängigkeiten | Benötigt AspectJ-Compiler/Weaver |

## 3. Kern-AOP-Komponenten

### 3.1 Aspekte
Eine Klasse, die mit `@Aspect` annotiert ist und Ratschläge sowie Schnittpunkte enthält.

```java
@Aspect
@Component
public class LoggingAspect {
    // Ratschläge und Schnittpunkte kommen hier hin
}
```

### 3.2 Rat-Typen

1. **Before**: Wird vor einem Verbindungspunkt ausgeführt
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("Vor Methodenausführung");
   }
   ```

2. **AfterReturning**: Wird ausgeführt, nachdem ein Verbindungspunkt normal abgeschlossen wurde
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("Methode gab zurück: " + result);
   }
   ```

3. **AfterThrowing**: Wird ausgeführt, wenn eine Methode durch Auslösen einer Ausnahme beendet wird
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("Ausnahme ausgelöst: " + ex.getMessage());
   }
   ```

4. **After (Finally)**: Wird nach einem Verbindungspunkt unabhängig vom Ergebnis ausgeführt
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("Nach Methodenausführung (finally)");
   }
   ```

5. **Around**: Umhüllt einen Verbindungspunkt, der leistungsstärkste Rat
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("Vor proceeding");
       Object result = joinPoint.proceed();
       System.out.println("Nach proceeding");
       return result;
   }
   ```

### 3.3 Schnittpunkt-Ausdrücke

Schnittpunkte definieren, wo Ratschläge angewendet werden sollen, mithilfe von Ausdrücken:

- **Execution**: Gleicht Methodenausführung ab
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **Within**: Gleicht alle Verbindungspunkte innerhalb bestimmter Typen ab
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **this**: Gleicht Beans ab, die Instanzen eines gegebenen Typs sind
- **target**: Gleicht Beans ab, die einem gegebenen Typ zuweisbar sind
- **args**: Gleicht Methoden mit spezifischen Argumenttypen ab
- **@annotation**: Gleicht Methoden mit spezifischen Annotationen ab

### 3.4 Kombinieren von Schnittpunkten

Schnittpunkte können mit logischen Operatoren kombiniert werden:
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. Implementierungsschritte

### 4.1 Setup

1. Spring AOP-Abhängigkeit hinzufügen (wenn nicht Spring Boot verwendet wird):
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

2. Für Spring Boot, einfach `spring-boot-starter-aop` einbinden:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. AOP in der Konfiguration aktivieren:
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 Erstellen von Aspekten

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("Betrete: {}.{}() mit Argumenten = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("Verlasse: {}.{}() mit Ergebnis = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} ausgeführt in {} ms", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 Benutzerdefinierte Annotationen

Erstellen Sie benutzerdefinierte Annotationen, um Methoden für spezifisches AOP-Verhalten zu markieren:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

Dann verwenden Sie es auf Methoden:
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // Implementierung
    }
}
```

## 5. Fortgeschrittene Themen

### 5.1 Aspekt-Reihenfolge

Steuern Sie die Ausführungsreihenfolge von Aspekten mit `@Order`:
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

### 5.2 Zugriff auf Methodeninformationen

In Rat-Methoden können Sie zugreifen auf:
- `JoinPoint` (für Before, After, AfterReturning, AfterThrowing)
- `ProceedingJoinPoint` (für Around)

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 Ausnahmebehandlung

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // Ausnahme protokollieren, Alarm senden, etc.
}
```

### 5.4 Proxying-Mechanismen

Spring AOP verwendet zwei Arten von Proxys:
- **JDK Dynamic Proxy**: Standard für Interfaces
- **CGLIB Proxy**: Wird verwendet, wenn kein Interface verfügbar ist (kann mit `proxyTargetClass=true` erzwungen werden)

## 6. Best Practices

1. **Aspekte fokussiert halten**: Jeder Aspekt sollte einen spezifischen übergreifenden Belang behandeln
2. **Aussagekräftige Schnittpunkt-Namen verwenden**: Macht Code besser lesbar
3. **Vermeiden Sie aufwändige Operationen in Aspekten**: Sie werden für jeden abgeglichenen Verbindungspunkt ausgeführt
4. **Seien Sie vorsichtig mit Around-Rat**: Rufen Sie immer `proceed()` auf, es sei denn, Sie verhindern die Ausführung absichtlich
5. **Testen Sie Aspekte gründlich**: Sie betreffen mehrere Teile Ihrer Anwendung
6. **Dokumentieren Sie Aspekte**: Insbesondere wenn sie das Verhalten signifikant verändern
7. **Berücksichtigen Sie die Leistung**: Komplexe Schnittpunkte oder viele Aspekte können die Leistung beeinträchtigen

## 7. Häufige Anwendungsfälle

1. **Logging**: Methodeneintritt/-austritt, Parameter, Rückgabewerte
2. **Leistungsüberwachung**: Ausführungszeit messen
3. **Transaktionsverwaltung**: (Obwohl typischerweise durch Springs `@Transactional` behandelt)
4. **Sicherheit**: Autorisierungsprüfungen
5. **Validierung**: Parameter-Validierung
6. **Fehlerbehandlung**: Konsistente Ausnahmebehandlung
7. **Caching**: Zwischenspeichern von Methodenergebnissen
8. **Auditing**: Verfolgen, wer was und wann aufgerufen hat

## 8. Einschränkungen

1. Funktioniert nur mit Spring-verwalteten Beans
2. Nur Methodenausführungs-Verbindungspunkte werden unterstützt
3. Kann keine finalen Klassen oder Methoden beraten
4. Selbstaufruf (Methode innerhalb einer Klasse ruft eine andere Methode derselben Klasse auf) umgeht den Proxy
5. Eingeschränkte Schnittpunkt-Ausdrücke im Vergleich zu AspectJ

## 9. Problembehandlung

**Problem**: Rat wird nicht ausgeführt
- Prüfen, ob die Bean Spring-verwaltet ist
- Überprüfen, ob der Schnittpunkt-Ausdruck die beabsichtigten Methoden abgleicht
- Sicherstellen, dass `@EnableAspectJAutoProxy` vorhanden ist

**Problem**: Around-Rat schreitet nicht fort
- Stellen Sie sicher, dass `proceed()` auf `ProceedingJoinPoint` aufgerufen wird

**Problem**: Falscher Proxy-Typ
- Verwenden Sie `@EnableAspectJAutoProxy(proxyTargetClass=true)`, um CGLIB zu erzwingen

## 10. Fazit

Spring AOP bietet eine leistungsstarke und dennoch einfache Möglichkeit, übergreifende Belange in Ihrer Anwendung zu implementieren. Obwohl es einige Einschränkungen im Vergleich zum vollständigen AspectJ hat, integriert es sich nahtlos mit Spring und deckt die meisten gängigen Anwendungsfälle ab. Durch Befolgen der in diesem Leitfaden beschriebenen Muster und Best Practices können Sie übergreifende Belange effektiv modularisieren und Ihre Geschäftslogik sauber und fokussiert halten.

---

Obwohl Spring AOP nicht AspectJs Weber-Fähigkeiten verwendet (es verwendet stattdessen proxy-basiertes AOP), benötigen Sie die `aspectjweaver`-Abhängigkeit aus mehreren wichtigen Gründen:

### 1. **AspectJ-Annotation-Unterstützung**
Spring AOP verwendet AspectJs **Annotationen** (wie `@Aspect`, `@Pointcut`, `@Before`, `@After`, etc.), um Aspekte und Ratschläge zu definieren. Diese Annotationen stammen aus der `aspectjweaver`-Bibliothek.

- Ohne sie würden Sie Kompilierungsfehler erhalten, wenn Sie `@Aspect` oder andere AOP-Annotationen verwenden.

### 2. **Schnittpunkt-Ausdruckssprache**
Spring AOP leiht sich AspectJs **Schnittpunkt-Ausdruckssprache** für die Definition aus, wo Ratschläge angewendet werden sollen (z.B. `execution(* com.example.service.*.*(..))`).

- Der `aspectjweaver` stellt den Parser und die Abgleichslogik für diese Ausdrücke bereit.

### 3. **Unterstützung für zusätzliche Verbindungspunkte (Eingeschränkt)**
Während Spring AOP nur **Methodenausführungs**-Verbindungspunkte unterstützt (im Gegensatz zu AspectJ, das Konstruktoren, Feldzugriff, etc. unterstützt), verlässt es sich dennoch auf AspectJs zugrunde liegenden Schnittpunkt-Abgleichsmechanismus.

### 4. **Load-Time Weaving (Optional)**
Wenn Sie sich entscheiden, **Load-Time Weaving (LTW)** mit Spring AOP zu verwenden (was selten, aber möglich ist), wird `aspectjweaver` benötigt. LTW ermöglicht das Weben von Aspekten zur Ladezeit der Klasse anstelle der Verwendung von Proxys.

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **Kompatibilität mit @EnableAspectJAutoProxy**
Wenn Sie `@EnableAspectJAutoProxy` verwenden, nutzt Spring intern AspectJs Infrastruktur, um die AOP-Annotationen zu verarbeiten, auch wenn es kein vollständiges AspectJ-Weaving durchführt.

---

### **Wird es immer benötigt?**
- **Bei Verwendung von Spring Boot (`spring-boot-starter-aop`)**: Nein, da es `aspectjweaver` transitiv einschließt.
- **Bei Verwendung von reinem Spring AOP**: Ja, Sie müssen es explizit einbinden.

### **Alternativen?**
- Wenn Sie **vollständiges AspectJ** (Compile-Time oder Load-Time Weaving) verwenden würden, bräuchten Sie auch `aspectjrt` und `aspectjtools`.
- Aber für **Spring AOP** ist `aspectjweaver` allein ausreichend.

### **Schlussfolgerung**
Spring AOP ist **proxy-basiert**, aber es **verwendet AspectJs Annotationen und Schnittpunkt-Syntax wieder**, weshalb `aspectjweaver` erforderlich ist. Es überbrückt die Lücke zwischen Springs Proxy-Ansatz und AspectJs leistungsstärkerem AOP-Modell.