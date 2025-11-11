---
audio: false
generated: true
lang: de
layout: post
title: Benchmarking in Java
translated: true
type: note
---

Das Java Microbenchmark Harness (JMH) ist ein leistungsstarkes Tool zum Erstellen, Ausführen und Analysieren von Microbenchmarks in Java. Es ermöglicht Entwicklern, die Leistung ihres Codes auf kontrollierte und wiederholbare Weise zu messen. Nachfolgend finden Sie eine umfassende Anleitung zur effektiven Nutzung von JMH.

---

## 1. Richten Sie Ihr Projekt ein

Um JMH zu verwenden, müssen Sie es in Ihr Projekt einbinden. So geht es mit Maven oder Gradle:

### **Maven**
Fügen Sie Ihrem `pom.xml` die folgenden Abhängigkeiten hinzu:

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

Diese Abhängigkeiten stellen die JMH-Core-Bibliothek und den zur Generierung des Benchmark-Codes benötigten Annotation Processor bereit.

---

## 2. Schreiben Sie Ihren Benchmark

Erstellen Sie eine Java-Klasse, um Ihren Benchmark zu definieren. Verwenden Sie die Annotation `@Benchmark`, um die Methoden zu markieren, die Sie messen möchten. Hier ein einfaches Beispiel:

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
        // Zu benchmarkender Code
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: Markiert die Methode als Benchmark-Ziel.
- **`@BenchmarkMode`**: Gibt an, wie die Leistung gemessen werden soll (z.B. `Mode.AverageTime` für die durchschnittliche Ausführungszeit).
- **`@OutputTimeUnit`**: Legt die Zeiteinheit für die Ergebnisse fest (z.B. `TimeUnit.NANOSECONDS`).

---

## 3. Konfigurieren Sie den Benchmark

Sie können Ihren Benchmark mit zusätzlichen JMH-Annotationen anpassen:

- **`@Warmup`**: Definiert die Warm-up-Phase (z.B. `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`**: Konfiguriert die Messphase (z.B. `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`**: Gibt an, wie viele JVM-Forks verwendet werden sollen (z.B. `@Fork(value = 1)` für die Ausführung in einer JVM-Instanz).
- **`@State`**: Definiert den Gültigkeitsbereich von Zustandsobjekten (z.B. `@State(Scope.Thread)` für thread-lokalen Zustand).

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
        // Zu benchmarkender Code
    }
}
```

---

## 4. Führen Sie den Benchmark aus

Um Ihren Benchmark auszuführen, können Sie den JMH-Runner verwenden. So geht es mit Maven:

### **Fügen Sie das Maven Shade Plugin hinzu**
Binden Sie dies in Ihr `pom.xml` ein, um ein ausführbares JAR zu erstellen:

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
1. Bauen Sie das JAR: `mvn clean package`
2. Führen Sie den Benchmark aus: `java -jar target/benchmarks.jar`

JMH führt die Benchmarks aus und zeigt die Ergebnisse in Ihrem Terminal an.

---

## 5. Analysieren Sie die Ergebnisse

JMH gibt Leistungsmetriken basierend auf Ihrer Konfiguration aus. Zum Beispiel:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: Der Benchmark-Modus (z.B. `avgt` für Durchschnittszeit).
- **Cnt**: Anzahl der Messiterationen.
- **Score**: Die gemessene Leistung (z.B. Durchschnittszeit in Nanosekunden pro Operation).
- **Error**: Die Fehlerspanne.
- **Units**: Die Maßeinheit.

Verwenden Sie diese Ergebnisse, um die Leistung Ihres Codes zu bewerten und zu optimieren.

---

## 6. Erweiterte Funktionen

JMH bietet zusätzliche Tools für komplexere Szenarien:

### **Parametrisierung**
Testen Sie Ihren Code mit verschiedenen Eingaben mit `@Param`:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // Zu benchmarkender Code
        }
    }
}
```

### **Blackholes**
Verhindern Sie, dass die JVM nicht verwendete Ergebnisse wegoptimiert, mit `Blackhole`:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // Verhindert Dead-Code-Eliminierung
}
```

---

## 7. Best Practices

- **Wärmen Sie die JVM auf**: Schließen Sie immer eine Warm-up-Phase ein, um sicherzustellen, dass der JIT-Compiler Ihren Code vor der Messung optimiert.
- **Wählen Sie den richtigen Modus**: Verwenden Sie `Mode.AverageTime` für Latenz, `Mode.Throughput` für Operationen pro Sekunde usw.
- **Kontrollieren Sie die Umgebung**: Führen Sie Benchmarks auf einem stabilen System aus, um Störungen durch andere Prozesse zu vermeiden.
- **Vermeiden Sie Optimierungen**: Verwenden Sie Blackholes oder andere JMH-Funktionen, um zu verhindern, dass die JVM Code eliminiert.

---

Indem Sie diese Schritte befolgen, können Sie `org.openjdk.jmh` verwenden, um die Leistung Ihres Java-Codes genau zu messen und zu verbessern. Egal, ob Sie einfache Operationen oder komplexe Algorithmen testen, JMH stellt die Tools bereit, die Sie für zuverlässiges Benchmarking benötigen.