---
audio: false
generated: true
lang: de
layout: post
title: 'Benchmarking in Java


  Benchmarking in Java'
translated: true
---

Der Java Microbenchmark Harness (JMH) ist ein leistungsfähiges Werkzeug zum Erstellen, Ausführen und Analysieren von Mikrobenchmarks in Java. Es ermöglicht Entwicklern, die Leistung ihres Codes auf kontrollierte und wiederholbare Weise zu messen. Hier ist eine umfassende Anleitung zur effektiven Verwendung von JMH.

---

## 1. Projekt einrichten

Um JMH zu verwenden, müssen Sie es in Ihr Projekt einbinden. Hier ist, wie Sie dies mit Maven oder Gradle tun können:

### **Maven**
Fügen Sie die folgenden Abhängigkeiten zu Ihrer `pom.xml` hinzu:

```xml
<dependency>
    <groupId>org.openjdk.jmh</groupId>
    <artifactId>jmh-core</artifactId>
    <version>1.36</version>
</dependency>
<dependency>
    <groupId>org.openjdk.jmh</groupId>
    <artifactId>jmh-generator-annprocess</artifactId>
    <version>1.36</version>
    <scope>provided</scope>
</dependency>
```

### **Gradle**
Fügen Sie diese Zeilen zu Ihrer `build.gradle` hinzu:

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

Diese Abhängigkeiten stellen die JMH-Kernbibliothek und den Annotationsprozessor bereit, der benötigt wird, um Benchmark-Code zu generieren.

---

## 2. Benchmark schreiben

Erstellen Sie eine Java-Klasse, um Ihren Benchmark zu definieren. Verwenden Sie die `@Benchmark`-Annotation, um die Methoden zu markieren, die Sie messen möchten. Hier ist ein einfaches Beispiel:

```java
import org.openjdk.jmh.annotations.Benchmark;
import org.openjdk.jmh.annotations.BenchmarkMode;
import org.openjdk.jmh.annotations.Mode;
import org.openjdk.jmh.annotations.OutputTimeUnit;
import java.util.concurrent.TimeUnit;

public class MyBenchmark {

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    @OutputTimeUnit(TimeUnit.NANOSECONDS)
    public void testMethod() {
        // Code zum Benchmarken
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: Markiert die Methode als Benchmark-Ziel.
- **`@BenchmarkMode`**: Gibt an, wie die Leistung gemessen werden soll (z. B. `Mode.AverageTime` für die durchschnittliche Ausführungszeit).
- **`@OutputTimeUnit`**: Legt die Zeiteinheit für die Ergebnisse fest (z. B. `TimeUnit.NANOSECONDS`).

---

## 3. Benchmark konfigurieren

Sie können Ihren Benchmark mit zusätzlichen JMH-Anmerkungen anpassen:

- **`@Warmup`**: Definiert die Aufwärmphase (z. B. `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`**: Konfiguriert die Messphase (z. B. `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`**: Gibt an, wie viele JVM-Forks verwendet werden sollen (z. B. `@Fork(value = 1)`, um in einer JVM-Instanz auszuführen).
- **`@State`**: Definiert den Geltungsbereich von Zustandsobjekten (z. B. `@State(Scope.Thread)` für thread-lokale Zustände).

Beispiel mit Konfiguration:

```java
@State(Scope.Thread)
@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)
@Fork(1)
public class MyBenchmark {
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    @OutputTimeUnit(TimeUnit.SECONDS)
    public void testMethod() {
        // Code zum Benchmarken
    }
}
```

---

## 4. Benchmark ausführen

Um Ihren Benchmark auszuführen, können Sie den JMH-Runner verwenden. Hier ist, wie Sie dies mit Maven tun können:

### **Maven Shade Plugin hinzufügen**
Fügen Sie dies in Ihre `pom.xml` ein, um ein ausführbares JAR zu erstellen:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-shade-plugin</artifactId>
            <version>3.2.4</version>
            <executions>
                <execution>
                    <phase>package</phase>
                    <goals>
                        <goal>shade</goal>
                    </goals>
                    <configuration>
                        <finalName>benchmarks</finalName>
                        <transformers>
                            <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                <mainClass>org.openjdk.jmh.Main</mainClass>
                            </transformer>
                        </transformers>
                    </configuration>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

### **Erstellen und Ausführen**
1. Erstellen Sie das JAR: `mvn clean package`
2. Führen Sie den Benchmark aus: `java -jar target/benchmarks.jar`

JMH führt die Benchmarks aus und zeigt die Ergebnisse in Ihrem Terminal an.

---

## 5. Ergebnisse analysieren

JMH gibt Leistungsmetriken basierend auf Ihrer Konfiguration aus. Zum Beispiel:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: Der Benchmark-Modus (z. B. `avgt` für Durchschnittszeit).
- **Cnt**: Anzahl der Messiterationen.
- **Score**: Die gemessene Leistung (z. B. Durchschnittszeit in Nanosekunden pro Operation).
- **Error**: Der Fehlerbereich.
- **Units**: Die Einheit der Messung.

Verwenden Sie diese Ergebnisse, um die Leistung Ihres Codes zu bewerten und zu optimieren.

---

## 6. Fortgeschrittene Funktionen

JMH bietet zusätzliche Tools für komplexere Szenarien:

### **Parameterisierung**
Testen Sie Ihren Code mit unterschiedlichen Eingaben mit `@Param`:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // Code zum Benchmarken
        }
    }
}
```

### **Blackholes**
Verhindern Sie, dass die JVM ungenutzte Ergebnisse optimiert, mit `Blackhole`:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // Verhindert die Eliminierung von totem Code
}
```

---

## 7. Best Practices

- **JVM aufwärmen**: Schließen Sie immer eine Aufwärmphase ein, um sicherzustellen, dass der JIT-Compiler Ihren Code vor der Messung optimiert.
- **Richtigen Modus wählen**: Verwenden Sie `Mode.AverageTime` für Latenz, `Mode.Throughput` für Operationen pro Sekunde usw.
- **Umgebung kontrollieren**: Führen Sie Benchmarks auf einem stabilen System aus, um Interferenzen durch andere Prozesse zu vermeiden.
- **Optimierungen vermeiden**: Verwenden Sie Blackholes oder andere JMH-Funktionen, um zu verhindern, dass die JVM Code eliminiert.

---

Durch die Befolgung dieser Schritte können Sie `org.openjdk.jmh` verwenden, um die Leistung Ihres Java-Codes genau zu messen und zu verbessern. Ob Sie einfache Operationen oder komplexe Algorithmen testen, JMH bietet die Tools, die Sie für zuverlässiges Benchmarking benötigen.