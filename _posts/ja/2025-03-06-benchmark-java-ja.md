---
audio: false
generated: true
lang: ja
layout: post
title: Javaにおけるベンチマーキング
translated: true
type: note
---

Java Microbenchmark Harness（JMH）は、Javaでマイクロベンチマークを構築、実行、分析するための強力なツールです。開発者がコードのパフォーマンスを制御された再現性のある方法で測定することを可能にします。以下はJMHを効果的に使用するための包括的なガイドです。

---

## 1. プロジェクトのセットアップ

JMHを使用するには、プロジェクトに含める必要があります。MavenまたはGradleでの方法は以下の通りです：

### **Maven**
`pom.xml`に以下の依存関係を追加します：

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
`build.gradle`に以下の行を追加します：

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

これらの依存関係は、JMHコアライブラリとベンチマークコードを生成するために必要なアノテーションプロセッサを提供します。

---

## 2. ベンチマークの作成

ベンチマークを定義するJavaクラスを作成します。測定したいメソッドに`@Benchmark`アノテーションを使用してマークします。簡単な例は以下の通りです：

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
        // ベンチマーク対象のコード
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**: メソッドをベンチマーク対象としてマークします。
- **`@BenchmarkMode`**: パフォーマンスの測定方法を指定します（例：平均実行時間の場合は`Mode.AverageTime`）。
- **`@OutputTimeUnit`**: 結果の時間単位を設定します（例：`TimeUnit.NANOSECONDS`）。

---

## 3. ベンチマークの設定

追加のJMHアノテーションを使用してベンチマークをカスタマイズできます：

- **`@Warmup`**: ウォームアップフェーズを定義します（例：`@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）。
- **`@Measurement`**: 測定フェーズを設定します（例：`@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）。
- **`@Fork`**: 使用するJVMフォークの数を指定します（例：1つのJVMインスタンスで実行する場合は`@Fork(value = 1)`）。
- **`@State`**: 状態オブジェクトのスコープを定義します（例：スレッドローカル状態の場合は`@State(Scope.Thread)`）。

設定を含む例：

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
        // ベンチマーク対象のコード
    }
}
```

---

## 4. ベンチマークの実行

ベンチマークを実行するには、JMHランナーを使用します。Mavenでの実行方法は以下の通りです：

### **Maven Shade Pluginの追加**
実行可能JARを作成するために`pom.xml`に以下を含めます：

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
1. JARをビルド：`mvn clean package`
2. ベンチマークを実行：`java -jar target/benchmarks.jar`

JMHはベンチマークを実行し、結果をターミナルに表示します。

---

## 5. 結果の分析

JMHは設定に基づいてパフォーマンスメトリクスを出力します。例：

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**: ベンチマークモード（例：平均時間の場合は`avgt`）。
- **Cnt**: 測定反復回数。
- **Score**: 測定されたパフォーマンス（例：操作あたりの平均ナノ秒時間）。
- **Error**: 誤差範囲。
- **Units**: 測定単位。

これらの結果を使用してコードのパフォーマンスを評価し最適化します。

---

## 6. 高度な機能

JMHはより複雑なシナリオのための追加ツールを提供します：

### **パラメータ化**
`@Param`を使用して異なる入力でコードをテスト：

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // ベンチマーク対象のコード
        }
    }
}
```

### **Blackholes**
`Blackhole`を使用して未使用の結果をJVMが最適化で除去するのを防止：

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // デッドコード除去を防止
}
```

---

## 7. ベストプラクティス

- **JVMのウォームアップ**: 測定前にJITコンパイラがコードを最適化するように、常にウォームアップフェーズを含めます。
- **適切なモードの選択**: レイテンシには`Mode.AverageTime`、1秒あたりの操作数には`Mode.Throughput`などを使用します。
- **環境の制御**: 他のプロセスからの干渉を避けるために、安定したシステムでベンチマークを実行します。
- **最適化の回避**: JVMがコードを除去するのを防ぐために、ブラックホールや他のJMH機能を使用します。

---

これらの手順に従うことで、`org.openjdk.jmh`を使用してJavaコードのパフォーマンスを正確に測定し改善できます。単純な操作でも複雑なアルゴリズムでも、JMHは信頼性の高いベンチマークに必要なツールを提供します。