---
audio: false
generated: true
lang: de
layout: post
title: Auflösen von Zirkulären Abhängigkeiten mit AspectJ
translated: true
type: note
---

Zyklische Abhängigkeiten in Ihrem Szenario entstehen, weil `BlogConfig`, `BlogCore` und `BlogWeb` sich gegenseitig referenzieren und eine Abhängigkeitsschleife bilden. Zusätzlich kann der AspectJ `LoggingAspect` in `BlogCore` (oder möglicherweise `BlogWeb`) das Problem verschärfen, wenn er auf Methoden über Module hinweg angewendet wird, einschließlich `BlogConfig`, welches von `BlogCore` abhängt. Lassen Sie uns das Problem aufschlüsseln und eine Lösung zur Behebung der zyklischen Abhängigkeit bei gleichzeitigem Erhalt der AspectJ-Funktionalität bereitstellen.

### Problemanalyse
1. **Modulabhängigkeiten**:
   - `BlogCore` hängt von `BlogConfig` ab.
   - `BlogWeb` hängt von `BlogCore` und `BlogConfig` ab.
   - `BlogConfig` hängt von `BlogCore` ab (dies erzeugt die zyklische Abhängigkeit: `BlogCore` ↔ `BlogConfig`).
   - Die Abhängigkeit von `BlogWeb` von beiden Modulen kann die zyklische Abhängigkeit mit sich ziehen.

2. **AspectJ LoggingAspect**:
   - Der `LoggingAspect` in `BlogCore` (oder `BlogWeb`) verwendet einen breiten Pointcut (`execution(* *(..))`), der auf alle Methodenausführungen im Anwendungskontext angewendet wird, einschließlich Methoden in `BlogConfig`, `BlogCore` und `BlogWeb`.
   - Wenn sich `LoggingAspect` in `BlogCore` befindet und in `BlogConfig` einwebt und `BlogConfig` von `BlogCore` abhängt, kann der AspectJ-Weaving-Prozess die zyklische Abhängigkeit während der Initialisierung verkomplizieren.

3. **Auswirkung der zyklischen Abhängigkeit**:
   - In einem Build-System wie Maven oder Gradle können zyklische Abhängigkeiten zwischen Modulen zu Kompilierungs- oder Laufzeitproblemen führen (z.B. Spring's `BeanCurrentlyInCreationException` bei Verwendung von Spring oder Classloading-Probleme).
   - AspectJs Compile-Time oder Load-Time Weaving kann fehlschlagen oder unerwartetes Verhalten verursachen, wenn Klassen aus `BlogConfig` und `BlogCore` voneinander abhängig und nicht vollständig initialisiert sind.

### Lösung
Um die zyklische Abhängigkeit aufzulösen und sicherzustellen, dass der AspectJ `LoggingAspect` korrekt funktioniert, befolgen Sie diese Schritte:

#### 1. Zyklische Abhängigkeit aufbrechen
Das Hauptproblem ist die `BlogCore` ↔ `BlogConfig` Abhängigkeit. Um dies zu beheben, extrahieren Sie die gemeinsame Funktionalität oder Konfiguration, die `BlogConfig` von `BlogCore` abhängig macht, in ein neues Modul oder refaktorisieren Sie die Abhängigkeiten.

**Option A: Einführung eines neuen Moduls (`BlogCommon`)**
- Erstellen Sie ein neues Modul `BlogCommon`, um gemeinsame Schnittstellen, Konfigurationen oder Utilities zu halten, die sowohl `BlogCore` als auch `BlogConfig` benötigen.
- Verschieben Sie die Teile von `BlogCore`, von denen `BlogConfig` abhängt (z.B. Schnittstellen, Konstanten oder gemeinsame Services), nach `BlogCommon`.
- Aktualisieren Sie die Abhängigkeiten:
  - `BlogConfig` hängt von `BlogCommon` ab.
  - `BlogCore` hängt von `BlogCommon` und `BlogConfig` ab.
  - `BlogWeb` hängt von `BlogCore` und `BlogConfig` ab.

**Beispiel für eine Abhängigkeitsstruktur**:
```
BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
```

**Implementierung**:
- Definieren Sie in `BlogCommon` Schnittstellen oder gemeinsame Komponenten. Zum Beispiel:
  ```java
  // BlogCommon Modul
  public interface BlogService {
      void performAction();
  }
  ```
- Implementieren Sie die Schnittstelle in `BlogCore`:
  ```java
  // BlogCore Modul
  public class BlogCoreService implements BlogService {
      public void performAction() { /* Logik */ }
  }
  ```
- Verwenden Sie in `BlogConfig` die Schnittstelle aus `BlogCommon`:
  ```java
  // BlogConfig Modul
  import com.example.blogcommon.BlogService;
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- Verwenden Sie in `BlogWeb` beide Module nach Bedarf.

Dies beseitigt die zyklische Abhängigkeit, indem sichergestellt wird, dass `BlogConfig` nicht mehr direkt von `BlogCore` abhängt.

**Option B: Inversion of Control (IoC) mit Dependency Injection**
- Wenn Sie ein Framework wie Spring verwenden, refaktorisieren Sie `BlogConfig` so, dass es von Abstraktionen (Schnittstellen) aus `BlogCore` abhängt, anstatt von konkreten Klassen.
- Verwenden Sie Dependency Injection, um die Implementierung von `BlogCore` zur Laufzeit an `BlogConfig` zu übergeben, und vermeiden Sie so eine zyklische Abhängigkeit zur Kompilierzeit.
- Beispiel:
  ```java
  // BlogCore Modul
  public interface BlogService {
      void performAction();
  }
  @Component
  public class BlogCoreService implements BlogService {
      public void performAction() { /* Logik */ }
  }

  // BlogConfig Modul
  @Configuration
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- Der IoC-Container von Spring löst die Abhängigkeit zur Laufzeit auf und bricht die Zyklizität zur Kompilierzeit.

#### 2. AspectJ-Konfiguration anpassen
Der breite Pointcut des `LoggingAspect` (`execution(* *(..))`) kann auf alle Module angewendet werden, einschließlich `BlogConfig`, was die Initialisierung verkomplizieren könnte. Um den Aspekt besser handhabbar zu machen und Weaving-Probleme zu vermeiden:

- **Pointcut einschränken**: Begrenzen Sie den Aspekt auf bestimmte Packages oder Module, um eine Anwendung auf `BlogConfig` oder anderen Infrastrukturcode zu vermeiden.
  ```java
  import org.aspectj.lang.JoinPoint;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import java.util.Arrays;

  @Aspect
  public class LoggingAspect {
      @After("execution(* com.example.blogcore..*(..)) || execution(* com.example.blogweb..*(..))")
      public void logAfter(JoinPoint joinPoint) {
          System.out.println("Methode ausgeführt: " + joinPoint.getSignature());
          System.out.println("Argumente: " + Arrays.toString(joinPoint.getArgs()));
      }
  }
  ```
  Dieser Pointcut wendet sich nur auf Methoden in `BlogCore` (`com.example.blogcore`) und `BlogWeb` (`com.example.blogweb`) an und schließt `BlogConfig` aus.

- **Aspekt in ein separates Modul verschieben**: Um Weaving-Probleme während der Modulinitialisierung zu vermeiden, platzieren Sie `LoggingAspect` in einem neuen Modul (z.B. `BlogAspects`), das von `BlogCore` und `BlogWeb` abhängt, aber nicht von `BlogConfig`.
  - Abhängigkeitsstruktur:
    ```
    BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
                       ↑          ↑
                       └─ BlogAspects ─┘
    ```
  - Aktualisieren Sie die Build-Konfiguration (z.B. Maven/Gradle), um sicherzustellen, dass `BlogAspects` nach `BlogCore` und `BlogWeb` gewebt wird.

- **Load-Time Weaving (LTW) verwenden**: Wenn Compile-Time Weaving aufgrund zyklischer Abhängigkeiten Probleme verursacht, wechseln Sie zu Load-Time Weaving mit AspectJ. Konfigurieren Sie LTW in Ihrer Anwendung (z.B. über Springs `@EnableLoadTimeWeaving` oder eine `aop.xml` Datei), um die Aspektanwendung auf die Laufzeit zu verschieben, nachdem die Klassen geladen wurden.

#### 3. Build-Konfiguration aktualisieren
Stellen Sie sicher, dass Ihr Build-Tool (Maven, Gradle, etc.) die neue Modulstruktur widerspiegelt und Abhängigkeiten korrekt auflöst.

**Maven-Beispiel**:
```xml
<!-- BlogCommon/pom.xml -->
<dependencies>
    <!-- Keine Abhängigkeiten -->
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

**Gradle-Beispiel**:
```groovy
// BlogCommon/build.gradle
dependencies {
    // Keine Abhängigkeiten
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
    id 'io.freefair.aspectj.post-compile-weaving' version '6.5.1'
}
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogWeb')
    aspect 'org.aspectj:aspectjrt:1.9.7'
}
```

#### 4. Anwendung testen
- Verifizieren Sie, dass die zyklische Abhängigkeit aufgelöst ist, indem Sie die Anwendung bauen und ausführen.
- Stellen Sie sicher, dass der `LoggingAspect` Methodenausführungen in `BlogCore` und `BlogWeb` protokolliert, aber nicht in `BlogConfig` (sofern nicht explizit gewünscht).
- Prüfen Sie bei Verwendung von Spring auf `BeanCurrentlyInCreationException` oder ähnliche Fehler während der Kontextinitialisierung.
- Testen Sie das AspectJ-Weaving, um zu bestätigen, dass Protokolle für die korrekten Methoden erscheinen.

#### 5. Zusätzliche Tipps
- **Verwenden Sie ein Abhängigkeitsanalyse-Tool**: Verwenden Sie Tools wie Mavens `mvn dependency:tree` oder Gradles `dependencies` Task, um verbleibende zyklische Abhängigkeiten zu erkennen.
- **Aspektgranularität beachten**: Wenn Protokollierung nur für bestimmte Services benötigt wird, verfeinern Sie den Pointcut weiter, um bestimmte Klassen oder Methoden anzuvisieren (z.B. `execution(* com.example.blogcore.service.*.*(..))`).
- **Vermeiden Sie AspectJ für Konfigurationsmodule**: Vermeiden Sie im Allgemeinen die Anwendung von Aspekten auf Konfigurations- oder Infrastrukturcode (wie `BlogConfig`), um die Komplexität zu reduzieren.

### Finale Abhängigkeitsstruktur
Nach dem Refactoring:
```
BlogCommon → BlogConfig → BlogCore → BlogWeb
   ↑                        ↑
   └────── BlogAspects ─────┘
```

### Warum dies funktioniert
- **Kreislauf durchbrechen**: Das Verschieben gemeinsamer Abhängigkeiten nach `BlogCommon` oder die Verwendung von IoC stellt sicher, dass `BlogConfig` nicht von `BlogCore` abhängt und beseitigt die zyklische Abhängigkeit.
- **Aspekte isolieren**: Das Platzieren von `LoggingAspect` in einem separaten Modul (`BlogAspects`) oder das Einschränken seines Pointcuts verhindert Weaving-Probleme und hält die Aspektlogik unabhängig von der Abhängigkeitskette.
- **Build-Konfiguration**: Die richtige Einrichtung des Build-Tools stellt sicher, dass Module in der richtigen Reihenfolge kompiliert und gewebt werden.

Dieser Ansatz erhält Ihre AspectJ-Protokollierungsfunktionalität bei gleichzeitiger Sicherstellung einer sauberen, wartbaren Modulstruktur. Wenn Sie weitere Details zu Ihrem Setup haben (z.B. Spring-Nutzung, spezifische Klassen, die den Zyklus verursachen), kann ich die Lösung weiter verfeinern!