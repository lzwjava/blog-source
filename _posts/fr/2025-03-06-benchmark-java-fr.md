---
audio: false
generated: true
lang: fr
layout: post
title: Benchmarking en Java
translated: true
type: note
---

Le Java Microbenchmark Harness (JMH) est un outil puissant pour construire, exécuter et analyser des microbenchmarks en Java. Il permet aux développeurs de mesurer les performances de leur code de manière contrôlée et reproductible. Voici un guide complet sur l'utilisation efficace de JMH.

---

## 1. Configurez votre projet

Pour utiliser JMH, vous devez l'inclure dans votre projet. Voici comment procéder avec Maven ou Gradle :

### **Maven**
Ajoutez les dépendances suivantes à votre `pom.xml` :

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
Ajoutez ces lignes à votre `build.gradle` :

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

Ces dépendances fournissent la bibliothèque principale de JMH et le processeur d'annotations nécessaire pour générer le code de benchmark.

---

## 2. Écrivez votre benchmark

Créez une classe Java pour définir votre benchmark. Utilisez l'annotation `@Benchmark` pour marquer les méthodes que vous souhaitez mesurer. Voici un exemple simple :

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
        // Code à benchmarker
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`** : Marque la méthode comme cible de benchmark.
- **`@BenchmarkMode`** : Spécifie comment mesurer les performances (par exemple, `Mode.AverageTime` pour le temps d'exécution moyen).
- **`@OutputTimeUnit`** : Définit l'unité de temps pour les résultats (par exemple, `TimeUnit.NANOSECONDS`).

---

## 3. Configurez le benchmark

Vous pouvez personnaliser votre benchmark en utilisant des annotations JMH supplémentaires :

- **`@Warmup`** : Définit la phase d'échauffement (par exemple, `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Measurement`** : Configure la phase de mesure (par exemple, `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`).
- **`@Fork`** : Spécifie le nombre de forks JVM à utiliser (par exemple, `@Fork(value = 1)` pour exécuter dans une instance JVM).
- **`@State`** : Définit la portée des objets d'état (par exemple, `@State(Scope.Thread)` pour un état local au thread).

Exemple avec configuration :

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
        // Code à benchmarker
    }
}
```

---

## 4. Exécutez le benchmark

Pour exécuter votre benchmark, vous pouvez utiliser le runner JMH. Voici comment procéder avec Maven :

### **Ajoutez le Maven Shade Plugin**
Incluez ceci dans votre `pom.xml` pour créer un JAR exécutable :

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

### **Construisez et exécutez**
1. Construisez le JAR : `mvn clean package`
2. Exécutez le benchmark : `java -jar target/benchmarks.jar`

JMH exécutera les benchmarks et affichera les résultats dans votre terminal.

---

## 5. Analysez les résultats

JMH produit des métriques de performance basées sur votre configuration. Par exemple :

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode** : Le mode de benchmark (par exemple, `avgt` pour le temps moyen).
- **Cnt** : Nombre d'itérations de mesure.
- **Score** : La performance mesurée (par exemple, le temps moyen en nanosecondes par opération).
- **Error** : La marge d'erreur.
- **Units** : L'unité de mesure.

Utilisez ces résultats pour évaluer et optimiser les performances de votre code.

---

## 6. Fonctionnalités avancées

JMH offre des outils supplémentaires pour des scénarios plus complexes :

### **Paramétrisation**
Testez votre code avec différentes entrées en utilisant `@Param` :

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // Code à benchmarker
        }
    }
}
```

### **Blackholes**
Empêchez la JVM d'optimiser les résultats inutilisés avec `Blackhole` :

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // Empêche l'élimination du code mort
}
```

---

## 7. Bonnes pratiques

- **Échauffez la JVM** : Incluez toujours une phase d'échauffement pour vous assurer que le compilateur JIT optimise votre code avant la mesure.
- **Choisissez le bon mode** : Utilisez `Mode.AverageTime` pour la latence, `Mode.Throughput` pour les opérations par seconde, etc.
- **Contrôlez l'environnement** : Exécutez les benchmarks sur un système stable pour éviter les interférences d'autres processus.
- **Évitez les optimisations** : Utilisez les blackholes ou d'autres fonctionnalités JMH pour empêcher la JVM d'éliminer du code.

---

En suivant ces étapes, vous pouvez utiliser `org.openjdk.jmh` pour mesurer et améliorer précisément les performances de votre code Java. Que vous testiez des opérations simples ou des algorithmes complexes, JMH fournit les outils nécessaires pour un benchmarking fiable.