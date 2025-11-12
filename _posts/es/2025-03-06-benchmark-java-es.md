---
audio: false
generated: true
lang: es
layout: post
title: Evaluación Comparativa en Java
translated: true
type: note
---

El Java Microbenchmark Harness (JMH) es una herramienta potente para construir, ejecutar y analizar microbenchmarks en Java. Permite a los desarrolladores medir el rendimiento de su código de forma controlada y repetible. A continuación se presenta una guía completa sobre cómo usar JMH de manera efectiva.

---

## 1. Configura tu proyecto

Para usar JMH, necesitas incluirlo en tu proyecto. Así es cómo hacerlo con Maven o Gradle:

### **Maven**
Añade las siguientes dependencias a tu `pom.xml`:

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
Añade estas líneas a tu `build.gradle`:

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

Estas dependencias proporcionan la librería core de JMH y el procesador de anotaciones necesario para generar el código del benchmark.

---

## 2. Escribe tu Benchmark

Crea una clase Java para definir tu benchmark. Usa la anotación `@Benchmark` para marcar los métodos que quieres medir. Aquí tienes un ejemplo simple:

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
        // Código a medir
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: Marca el método como objetivo del benchmark.
- **`@BenchmarkMode`**: Especifica cómo medir el rendimiento (ej., `Mode.AverageTime` para el tiempo de ejecución promedio).
- **`@OutputTimeUnit`**: Establece la unidad de tiempo para los resultados (ej., `TimeUnit.NANOSECONDS`).

---

## 3. Configura el Benchmark

Puedes personalizar tu benchmark usando anotaciones adicionales de JMH:

- **`@Warmup`**: Define la fase de calentamiento (ej., `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`**: Configura la fase de medición (ej., `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`**: Especifica cuántos forks de JVM usar (ej., `@Fork(value = 1)` para ejecutar en una instancia JVM).
- **`@State`**: Define el alcance de los objetos de estado (ej., `@State(Scope.Thread)` para estado local del hilo).

Ejemplo con configuración:

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
        // Código a medir
    }
}
```

---

## 4. Ejecuta el Benchmark

Para ejecutar tu benchmark, puedes usar el runner de JMH. Así es cómo hacerlo con Maven:

### **Añade el Maven Shade Plugin**
Incluye esto en tu `pom.xml` para crear un JAR ejecutable:

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

### **Construye y Ejecuta**
1. Construye el JAR: `mvn clean package`
2. Ejecuta el benchmark: `java -jar target/benchmarks.jar`

JMH ejecutará los benchmarks y mostrará los resultados en tu terminal.

---

## 5. Analiza los Resultados

JMH genera métricas de rendimiento basadas en tu configuración. Por ejemplo:

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: El modo del benchmark (ej., `avgt` para tiempo promedio).
- **Cnt**: Número de iteraciones de medición.
- **Score**: El rendimiento medido (ej., tiempo promedio en nanosegundos por operación).
- **Error**: El margen de error.
- **Units**: La unidad de medida.

Usa estos resultados para evaluar y optimizar el rendimiento de tu código.

---

## 6. Características Avanzadas

JMH ofrece herramientas adicionales para escenarios más complejos:

### **Parametrización**
Prueba tu código con diferentes entradas usando `@Param`:

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // Código a medir
        }
    }
}
```

### **Blackholes**
Evita que la JVM optimice los resultados no utilizados con `Blackhole`:

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // Previene la eliminación de código muerto
}
```

---

## 7. Mejores Prácticas

- **Calienta la JVM**: Incluye siempre una fase de calentamiento para asegurar que el compilador JIT optimice tu código antes de la medición.
- **Elige el Modo Correcto**: Usa `Mode.AverageTime` para latencia, `Mode.Throughput` para operaciones por segundo, etc.
- **Controla el Entorno**: Ejecuta los benchmarks en un sistema estable para evitar interferencias de otros procesos.
- **Evita Optimizaciones**: Usa blackholes u otras características de JMH para evitar que la JVM elimine código.

---

Siguiendo estos pasos, puedes usar `org.openjdk.jmh` para medir con precisión y mejorar el rendimiento de tu código Java. Ya sea que estés probando operaciones simples o algoritmos complejos, JMH proporciona las herramientas que necesitas para un benchmarking confiable.