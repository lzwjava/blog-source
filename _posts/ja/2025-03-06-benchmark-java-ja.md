---
audio: false
generated: true
lang: ja
layout: post
title: Javaのベンチマーク
translated: true
---

Java Microbenchmark Harness (JMH) は、Java でマイクロベンチマークを構築、実行、分析するための強力なツールです。開発者は、制御された環境でコードのパフォーマンスを測定し、繰り返し可能な方法で測定することができます。以下は、JMH を効果的に使用するための包括的なガイドです。

---

## 1. プロジェクトのセットアップ

JMH を使用するには、プロジェクトに含める必要があります。以下に、Maven または Gradle で行う方法を示します。

### **Maven**
`pom.xml` に以下の依存関係を追加します：

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
`build.gradle` に以下の行を追加します：

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

これらの依存関係は、JMH のコアライブラリと、ベンチマークコードを生成するために必要なアノテーションプロセッサを提供します。

---

## 2. ベンチマークの作成

ベンチマークを定義するための Java クラスを作成します。測定したいメソッドに `@Benchmark` アノテーションを付けます。以下は、簡単な例です：

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
        // ベンチマークするコード
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: メソッドをベンチマーク対象としてマークします。
- **`@BenchmarkMode`**: パフォーマンスの測定方法を指定します（例：`Mode.AverageTime` は平均実行時間）。
- **`@OutputTimeUnit`**: 結果の時間単位を設定します（例：`TimeUnit.NANOSECONDS`）。

---

## 3. ベンチマークの設定

追加の JMH アノテーションを使用して、ベンチマークをカスタマイズできます：

- **`@Warmup`**: ウォームアップフェーズを定義します（例：`@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）。
- **`@Measurement`**: 測定フェーズを設定します（例：`@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）。
- **`@Fork`**: 使用する JVM フォークの数を指定します（例：`@Fork(value = 1)` は 1 つの JVM インスタンスで実行）。
- **`@State`**: ステートオブジェクトのスコープを定義します（例：`@State(Scope.Thread)` はスレッドローカルのステート）。

設定例：

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
        // ベンチマークするコード
    }
}
```

---

## 4. ベンチマークの実行

ベンチマークを実行するには、JMH ランナーを使用します。以下に、Maven で行う方法を示します。

### **Maven Shade プラグインの追加**
実行可能な JAR を作成するために、`pom.xml` に以下を追加します：

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

### **ビルドと実行**
1. JAR をビルドします：`mvn clean package`
2. ベンチマークを実行します：`java -jar target/benchmarks.jar`

JMH はベンチマークを実行し、ターミナルに結果を表示します。

---

## 5. 結果の分析

JMH は設定に基づいてパフォーマンスメトリクスを出力します。例えば：

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: ベンチマークモード（例：`avgt` は平均時間）。
- **Cnt**: 測定反復回数。
- **Score**: 測定されたパフォーマンス（例：ナノ秒/操作の平均時間）。
- **Error**: 誤差の範囲。
- **Units**: 測定単位。

これらの結果を使用して、コードのパフォーマンスを評価および最適化します。

---

## 6. 高度な機能

JMH は、より複雑なシナリオのための追加ツールを提供します。

### **パラメータ化**
`@Param` を使用して、異なる入力でコードをテストします：

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // ベンチマークするコード
        }
    }
}
```

### **ブラックホール**
JVM が未使用の結果を最適化して削除するのを防ぐために `Blackhole` を使用します：

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // デッドコードの削除を防ぐ
}
```

---

## 7. ベストプラクティス

- **JVM のウォームアップ**: 計測前に JIT コンパイラがコードを最適化するように、ウォームアップフェーズを必ず含めます。
- **適切なモードの選択**: `Mode.AverageTime` は遅延、`Mode.Throughput` は秒あたりの操作数など、適切なモードを使用します。
- **環境の制御**: 他のプロセスからの干渉を避けるために、安定したシステムでベンチマークを実行します。
- **最適化の回避**: ブラックホールや他の JMH 機能を使用して、JVM がコードを削除するのを防ぎます。

---

これらの手順に従うことで、`org.openjdk.jmh` を使用して、Java コードのパフォーマンスを正確に測定し、改善することができます。単純な操作から複雑なアルゴリズムまで、JMH は信頼性のあるベンチマークのためのツールを提供します。