---
audio: false
generated: true
lang: de
layout: post
title: AspectJ mit Java und Spring Boot
translated: true
type: note
---

## Inhaltsverzeichnis
1. [Einführung in die aspektorientierte Programmierung (AOP)](#einführung-in-die-aspektorientierte-programmierung-aop)
2. [AspectJ Überblick](#aspectj-überblick)
3. [AspectJ mit Java](#aspectj-mit-java)
4. [AspectJ mit Spring Boot](#aspectj-mit-spring-boot)
5. [Häufige Anwendungsfälle](#häufige-anwendungsfälle)
6. [Best Practices](#best-practices)
7. [Performance-Überlegungen](#performance-überlegungen)

## Einführung in die aspektorientierte Programmierung (AOP)

AOP ist ein Programmierparadigma, das darauf abzielt, die Modularität zu erhöhen, indem es die Trennung von übergreifenden Belangen (Cross-Cutting Concerns) ermöglicht. Übergreifende Belange sind Funktionalitäten, die mehrere Teile eines Systems betreffen (wie Protokollierung, Sicherheit, Transaktionsverwaltung).

Wichtige AOP-Konzepte:
- **Aspekt**: Eine Modularisierung eines Belangs, der mehrere Klassen betrifft
- **Verbindungspunkt**: Ein Punkt während der Programmausführung (Methodenaufruf, Feldzugriff, etc.)
- **Rat**: Aktion, die an einem bestimmten Verbindungspunkt ausgeführt wird
- **Schnittpunkt**: Prädikat, das Verbindungspunkte abgleicht
- **Weaving**: Verknüpfung von Aspekten mit anderen Anwendungstypen

## AspectJ Überblick

AspectJ ist die beliebteste und funktionsreichste AOP-Implementierung für Java. Es bietet:
- Eine leistungsstarke Schnittpunkt-Sprache
- Verschiedene Weaving-Mechanismen (Compile-Time, Post-Compile, Load-Time)
- Vollständige AOP-Unterstützung, die über Spring AOP hinausgeht

### AspectJ vs Spring AOP

| Merkmal            | AspectJ | Spring AOP |
|--------------------|---------|------------|
| Verbindungspunkte  | Methodenausführung, Konstruktoraufrufe, Feldzugriff, etc. | Nur Methodenausführung |
| Weaving            | Compile-Time, Post-Compile, Load-Time | Laufzeit-Proxying |
| Performance        | Besser (kein Laufzeit-Overhead) | Etwas langsamer (verwendet Proxys) |
| Komplexität        | Komplexer | Einfacher |
| Abhängigkeiten     | Benötigt AspectJ-Compiler/Weaver | In Spring integriert |

## AspectJ mit Java

### Einrichtung

1. Fügen Sie AspectJ-Abhängigkeiten zu Ihrer `pom.xml` hinzu (Maven):

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.7</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. Konfigurieren Sie das AspectJ Maven-Plugin für Compile-Time Weaving:

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>aspectj-maven-plugin</artifactId>
    <version>1.14.0</version>
    <configuration>
        <complianceLevel>11</complianceLevel>
        <source>11</source>
        <target>11</target>
        <showWeaveInfo>true</showWeaveInfo>
        <verbose>true</verbose>
        <Xlint>ignore</Xlint>
        <encoding>UTF-8</encoding>
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
```

### Erstellen von Aspekten

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class LoggingAspect {

    // Schnittpunkt-Definition
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // Rat
    @Before("serviceMethods()")
    public void logBeforeServiceMethods() {
        System.out.println("Eine Servicemethode wird gleich ausgeführt");
    }
}
```

### Rat-Typen

1. **Before**: Wird vor einem Verbindungspunkt ausgeführt
2. **After**: Wird nach Abschluss eines Verbindungspunkts ausgeführt (normal oder mit Ausnahme)
3. **AfterReturning**: Wird ausgeführt, nachdem ein Verbindungspunkt normal abgeschlossen wurde
4. **AfterThrowing**: Wird ausgeführt, wenn eine Methode durch Auslösen einer Exception beendet wird
5. **Around**: Umgibt einen Verbindungspunkt (leistungsstärkster Rat)

### Schnittpunkt-Ausdrücke

AspectJ bietet eine umfangreiche Schnittpunkt-Ausdruckssprache:

```java
// Methodenausführung in Package
@Pointcut("execution(* com.example.service.*.*(..))")

// Methodenausführung in Klasse
@Pointcut("execution(* com.example.service.UserService.*(..))")

// Methode mit spezifischem Namen
@Pointcut("execution(* *..find*(..))")

// Mit spezifischem Rückgabetyp
@Pointcut("execution(public String com.example..*(..))")

// Mit spezifischen Parametertypen
@Pointcut("execution(* *.*(String, int))")

// Kombinieren von Schnittpunkten
@Pointcut("serviceMethods() && findMethods()")
```

## AspectJ mit Spring Boot

### Einrichtung

1. Fügen Sie Spring AOP und AspectJ-Abhängigkeiten hinzu:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. Aktivieren Sie AspectJ-Unterstützung in Ihrer Spring Boot-Anwendung:

```java
@SpringBootApplication
@EnableAspectJAutoProxy
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### Beispiel: Protokollierung der Ausführungszeit

```java
@Aspect
@Component
public class ExecutionTimeAspect {

    private static final Logger logger = LoggerFactory.getLogger(ExecutionTimeAspect.class);

    @Around("@annotation(com.example.annotation.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        
        Object proceed = joinPoint.proceed();
        
        long executionTime = System.currentTimeMillis() - startTime;
        
        logger.info("{} executed in {} ms", 
            joinPoint.getSignature(), executionTime);
        
        return proceed;
    }
}
```

Erstellen Sie eine benutzerdefinierte Annotation:

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

Verwenden Sie sie auf Methoden:

```java
@Service
public class UserService {
    
    @LogExecutionTime
    public List<User> getAllUsers() {
        // Implementierung
    }
}
```

### Beispiel: Transaktionsverwaltung

```java
@Aspect
@Component
public class TransactionAspect {

    @Autowired
    private PlatformTransactionManager transactionManager;

    @Around("@annotation(com.example.annotation.Transactional)")
    public Object manageTransaction(ProceedingJoinPoint joinPoint) throws Throwable {
        TransactionDefinition def = new DefaultTransactionDefinition();
        TransactionStatus status = transactionManager.getTransaction(def);
        
        try {
            Object result = joinPoint.proceed();
            transactionManager.commit(status);
            return result;
        } catch (Exception e) {
            transactionManager.rollback(status);
            throw e;
        }
    }
}
```

## Häufige Anwendungsfälle

1. **Protokollierung**: Zentrale Protokollierung von Methodeneintritten/Ausnahmen
2. **Performance-Monitoring**: Verfolgung von Ausführungszeiten
3. **Transaktionsverwaltung**: Deklarative Transaktionsgrenzen
4. **Sicherheit**: Autorisierungsprüfungen
5. **Fehlerbehandlung**: Konsistente Ausnahmebehandlung
6. **Caching**: Automatisches Zwischenspeichern von Methodenergebnissen
7. **Validierung**: Parametervalidierung
8. **Auditing**: Verfolgung, wer was und wann getan hat

## Best Practices

1. **Aspekte fokussiert halten**: Jeder Aspekt sollte einen Belang behandeln
2. **Aussagekräftige Namen verwenden**: Klare Aspekt- und Schnittpunktnamen
3. **Geschäftslogik in Aspekten vermeiden**: Aspekte sollten übergreifende Belange behandeln, nicht Kernlogik
4. **Aspekte dokumentieren**: Insbesondere komplexe Schnittpunkte
5. **Performance berücksichtigen**: Around-Rat kann die Performance beeinträchtigen
6. **Aspekte testen**: Aspekte müssen wie jeder andere Code getestet werden
7. **Annotationen verwenden**: Benutzerdefinierte Annotationen machen Aspekte deklarativer
8. **Vorsicht mit execution() vs @annotation()**: Wissen, wann welches verwendet werden soll

## Performance-Überlegungen

1. **Compile-Time Weaving** ist generell die schnellste Option
2. **Load-Time Weaving** fügt etwas Overhead während des Klassenladens hinzu
3. **Runtime Weaving** (Spring AOP) hat den meisten Overhead
4. **Komplexe Schnittpunkte** können die Performance beeinträchtigen
5. **Around-Rat** ist teurer als andere Rat-Typen

Für maximale Performance in der Produktion:
- Verwenden Sie Compile-Time Weaving wo möglich
- Halten Sie Schnittpunkte einfach
- Vermeiden Sie zu breite Schnittpunkt-Ausdrücke

## Fazit

AspectJ bietet eine leistungsstarke Möglichkeit, übergreifende Belange in Java- und Spring Boot-Anwendungen zu implementieren. Während Spring AOP einfacher ist und für viele Fälle ausreicht, bietet AspectJ mehr Fähigkeiten, wenn Sie über Methodenabfang hinausgehen müssen. Durch Befolgen der in diesem Leitfaden beschriebenen Muster und Best Practices können Sie AspectJ effektiv einsetzen, um modularere, wartbarere Anwendungen zu erstellen.