---
audio: false
generated: true
lang: de
layout: post
title: Zirkuläre Abhängigkeiten in Spring
translated: true
type: note
---

Zyklische Abhängigkeiten in Spring oder Spring Boot treten auf, wenn zwei oder mehr Beans direkt oder indirekt voneinander abhängen, während sie initialisiert werden. Dadurch entsteht ein Zyklus, in dem der Dependency-Injection-Mechanismus von Spring die Abhängigkeiten nicht auflösen kann, da jede Bean die andere benötigt, um selbst vollständig initialisiert zu werden. Dieses Problem tritt typischerweise während der Erstellung von Beans im Spring Application Context auf und führt zu einer `BeanCurrentlyInCreationException`.

### Warum zyklische Abhängigkeiten auftreten
Spring verwaltet Beans in einem Dependency-Injection-Container, und Beans werden normalerweise in einer bestimmten Reihenfolge basierend auf ihren Abhängigkeiten erstellt. Wenn Beans sich zyklisch referenzieren (z. B. Bean A hängt von Bean B ab und Bean B hängt von Bean A ab), kann Spring sie nicht instanziieren, da es während der Initialisierung in einer Endlosschleife stecken bleibt. Dies ist besonders häufig in komplexen Anwendungen mit stark gekoppelten Komponenten der Fall.

Das Problem tritt mit größerer Wahrscheinlichkeit in den folgenden Szenarien auf:
1.  **Constructor Injection**: Wenn Beans über Konstruktoren verbunden werden, muss Spring die Abhängigkeiten zum Zeitpunkt der Instanziierung auflösen, was zu Zyklenproblemen führen kann, wenn Beans sich gegenseitig referenzieren.
2.  **Field oder Setter Injection mit Eager Initialization**: Wenn Beans eifrig initialisiert werden (Standardverhalten für Singleton-Beans), versucht Spring, Abhängigkeiten sofort aufzulösen, was zyklische Abhängigkeiten aufdeckt.
3.  **Falsch konfigurierte oder übermäßig komplexe Bean-Beziehungen**: Schlechtes Design oder mangelnde Trennung der Zuständigkeiten kann zu unbeabsichtigten Zyklen führen.
4.  **Annotationen wie `@Autowired` oder `@Component`**: Automatische Dependency Injection in stark gekoppelten Komponenten kann unbeabsichtigt Zyklen erzeugen.

### Häufige Beispiele für zyklische Abhängigkeiten

#### Beispiel 1: Zyklus durch Constructor Injection
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
**Problem**: `BeanA` benötigt `BeanB` in seinem Konstruktor und `BeanB` benötigt `BeanA` in seinem Konstruktor. Spring kann keine der beiden Beans erstellen, da jede davon abhängt, dass die andere zuerst vollständig initialisiert ist.

**Fehler**: `BeanCurrentlyInCreationException: Error creating bean with name 'beanA': Requested bean is currently in creation: Is there an unresolvable circular reference?`

#### Beispiel 2: Zyklus durch Field Injection
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
**Problem**: Sowohl `BeanA` als auch `BeanB` verwenden `@Autowired`, um sich gegenseitig über Felder zu injizieren. Obwohl Field Injection flexibler ist als Constructor Injection, erkennt Spring den Zyklus dennoch während der Bean-Initialisierung, wenn es sich um Singleton-Beans (Standard-Scope) handelt.

#### Beispiel 3: Indirekte zyklische Abhängigkeit
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
**Problem**: `BeanA` hängt von `BeanB` ab, `BeanB` hängt von `BeanC` ab und `BeanC` hängt von `BeanA` ab, was einen Zyklus bildet. Diese indirekte Abhängigkeit ist schwerer zu erkennen, verursacht aber das gleiche Problem.

#### Beispiel 4: `@Configuration`-Klassen mit zyklischen Referenzen
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
**Problem**: Die `@Configuration`-Klassen `ConfigA` und `ConfigB` hängen voneinander ab, was einen Zyklus erzeugt, wenn Spring versucht, die in diesen Klassen definierten Beans zu initialisieren.

### Häufige Ursachen in Spring Boot
-   **Auto-Configuration**: Die Auto-Konfiguration von Spring Boot kann manchmal Abhängigkeiten einführen, die zu Zyklen führen, insbesondere wenn benutzerdefinierte Beans mit auto-konfigurierten interagieren.
-   **Component Scanning**: Übermäßige Verwendung von `@ComponentScan` oder falsch konfigurierte Pakete können unbeabsichtigte Beans erfassen, was zu zyklischen Abhängigkeiten führt.
-   **Stark gekoppeltes Design**: Geschäftslogik, die Services, Repositories oder Controller stark koppelt, kann unbeabsichtigt Zyklen erzeugen.
-   **Falsche Verwendung des Prototype-Scope**: Während Prototype-Scoped-Beans manchmal zyklische Abhängigkeiten vermeiden können, kann deren Kombination mit Singleton-Beans in einem zyklischen Muster dennoch Probleme verursachen.

### Wie man zyklische Abhängigkeiten auflöst
1.  **Verwende die `@Lazy` Annotation**:
    - Kennzeichne eine der Abhängigkeiten mit `@Lazy`, um deren Initialisierung zu verzögern, bis sie tatsächlich benötigt wird.
    ```java
    @Component
    public class BeanA {
        @Autowired
        @Lazy
        private BeanB beanB;
    }
    ```
    Dies unterbricht den Zyklus, indem `BeanA` teilweise initialisiert werden kann, bevor `BeanB` aufgelöst wird.

2.  **Wechsle zu Setter oder Field Injection**:
    - Verwende anstelle von Constructor Injection Setter oder Field Injection für eine der Beans, um Spring zu ermöglichen, die Bean zuerst zu initialisieren und die Abhängigkeiten später zu injizieren.
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

3.  **Refaktorisiere den Code, um den Zyklus zu unterbrechen**:
    - Führe ein Interface oder eine Zwischenkomponente ein, um die Beans zu entkoppeln.
    - Beispiel: Extrahiere eine gemeinsame Abhängigkeit in eine dritte Bean oder verwende eine Service-Schicht, um Interaktionen zu vermitteln.
    ```java
    public interface Service {
        void performAction();
    }

    @Component
    public class BeanA implements Service {
        @Autowired
        private BeanB beanB;

        public void performAction() {
            // Logik
        }
    }

    @Component
    public class BeanB {
        @Autowired
        private Service service; // Hängt vom Interface ab, nicht direkt von BeanA
    }
    ```

4.  **Verwende die `@DependsOn` Annotation**:
    - Kontrolliere explizit die Reihenfolge der Bean-Initialisierung, um Zyklen in bestimmten Fällen zu vermeiden.
    ```java
    @Component
    @DependsOn("beanB")
    public class BeanA {
        @Autowired
        private BeanB beanB;
    }
    ```

5.  **Aktiviere Proxying mit `@EnableAspectJAutoProxy`**:
    - Stelle sicher, dass Spring Proxys (CGLIB oder JDK dynamic proxies) verwendet, um Abhängigkeiten zu behandeln, was einige Zyklenprobleme lösen kann, indem ein Proxy anstelle der eigentlichen Bean injiziert wird.

6.  **Überprüfe das Design**:
    - Zyklische Abhängigkeiten deuten oft auf einen Designfehler hin. Ziehe eine Refaktorisierung in Betracht, um das Single Responsibility Principle oder das Dependency Inversion Principle einzuhalten.

### Wie man zyklische Abhängigkeiten debuggt
-   **Prüfe die Stack Trace**: Die `BeanCurrentlyInCreationException`-Stack Trace zeigt die am Zyklus beteiligten Beans an.
-   **Aktiviere Debug-Logging**: Setze `spring.main.lazy-initialization=true` oder aktiviere Debug-Logging für `org.springframework`, um Details zur Bean-Erstellung zu sehen.
-   **Verwende Tools**: Tools wie Spring Boot Actuator oder IDE-Plugins (z. B. Spring Tools Suite) können Bean-Abhängigkeiten visualisieren.

### Zyklischen Abhängigkeiten vorbeugen
-   **Befolge Best Practices**: Verwende Dependency-Injection-Muster wie Interfaces oder Abstraktionen, um starke Kopplung zu reduzieren.
-   **Modularisiere Code**: Unterteile große Anwendungen in kleinere, lose gekoppelte Module.
-   **Teste frühzeitig**: Führe Integrationstests durch, um zyklische Abhängigkeiten während der Entwicklung zu erkennen.
-   **Beschränke Component Scanning**: Sei spezifisch mit `@ComponentScan`, um das Erfassen unnötiger Beans zu vermeiden.

### Wann zyklische Abhängigkeiten weniger wahrscheinlich sind
-   **Prototype-Scope**: Beans mit Prototype-Scope werden bei Bedarf erstellt, was die Wahrscheinlichkeit von Zyklen verringert (aber nicht vollständig beseitigt).
-   **Lazy Initialization**: Das Aktivieren der globalen Lazy Initialization (`spring.main.lazy-initialization=true`) kann die Bean-Erstellung verzögern, maskiert aber möglicherweise nur das Problem.

### Fazit
Zyklische Abhängigkeiten in Spring/Spring Boot entstehen durch starke Kopplung zwischen Beans, die oft durch Constructor Injection oder komplexe Konfigurationen verschärft wird. Häufige Lösungen umfassen die Verwendung von `@Lazy`, den Wechsel zu Setter/Field Injection oder die Refaktorisierung, um den Zyklus zu unterbrechen. Indem man die Ursache versteht und Best Practices anwendet, kann man diese Probleme effektiv verhindern oder lösen. Wenn du auf eine spezifische zyklische Abhängigkeit stößt, teile den relevanten Code oder die Fehlerdetails, und ich kann helfen, sie weiter zu analysieren!