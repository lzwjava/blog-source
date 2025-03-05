---
audio: false
generated: true
lang: hant
layout: post
title: Java 之基準測試
translated: true
---

Java Microbenchmark Harness (JMH) 是一個強大的工具，用於在 Java 中構建、運行和分析微基準測試。它允許開發者以受控和可重複的方式測量他們的代碼性能。以下是如何有效使用 JMH 的全面指南。

---

## 1. 設置您的項目

要使用 JMH，您需要將其包含在您的項目中。以下是使用 Maven 或 Gradle 的方法：

### **Maven**
在 `pom.xml` 中添加以下依賴：

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
在 `build.gradle` 中添加以下行：

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

這些依賴項提供了 JMH 核心庫和生成基準代碼所需的註釋處理器。

---

## 2. 編寫您的基準測試

創建一個 Java 類來定義您的基準測試。使用 `@Benchmark` 注釋來標記您要測量的方法。以下是一個簡單的例子：

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
        // 要基準測試的代碼
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**：將方法標記為基準測試目標。
- **`@BenchmarkMode`**：指定如何測量性能（例如，`Mode.AverageTime` 表示平均執行時間）。
- **`@OutputTimeUnit`**：設置結果的時間單位（例如，`TimeUnit.NANOSECONDS`）。

---

## 3. 配置基準測試

您可以使用額外的 JMH 注釋來自定義您的基準測試：

- **`@Warmup`**：定義預熱階段（例如，`@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）。
- **`@Measurement`**：配置測量階段（例如，`@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）。
- **`@Fork`**：指定使用多少 JVM 分叉（例如，`@Fork(value = 1)` 以在一個 JVM 實例中運行）。
- **`@State`**：定義狀態對象的範圍（例如，`@State(Scope.Thread)` 表示線程本地狀態）。

配置示例：

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
        // 要基準測試的代碼
    }
}
```

---

## 4. 運行基準測試

要執行您的基準測試，可以使用 JMH 運行器。以下是使用 Maven 的方法：

### **添加 Maven Shade 插件**
在 `pom.xml` 中包含以下內容以創建可執行的 JAR：

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

### **構建和運行**
1. 构建 JAR：`mvn clean package`
2. 運行基準測試：`java -jar target/benchmarks.jar`

JMH 將執行基準測試並在您的終端顯示結果。

---

## 5. 分析結果

JMH 根據您的配置輸出性能指標。例如：

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**：基準測試模式（例如，`avgt` 表示平均時間）。
- **Cnt**：測量迭代次數。
- **Score**：測量的性能（例如，平均時間以納秒為單位）。
- **Error**：誤差範圍。
- **Units**：測量單位。

使用這些結果來評估和優化您的代碼性能。

---

## 6. 高級功能

JMH 提供了更多工具來處理更複雜的情況：

### **參數化**
使用 `@Param` 來測試不同的輸入：

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // 要基準測試的代碼
        }
    }
}
```

### **Blackholes**
使用 `Blackhole` 來防止 JVM 優化掉未使用的結果：

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // 防止死代碼消除
}
```

---

## 7. 最佳實踐

- **預熱 JVM**：始終包括預熱階段，以確保 JIT 編譯器在測量之前優化您的代碼。
- **選擇合適的模式**：使用 `Mode.AverageTime` 來測量延遲，使用 `Mode.Throughput` 來測量每秒操作數等。
- **控制環境**：在穩定的系統上運行基準測試，以避免其他進程的干擾。
- **避免優化**：使用黑洞或其他 JMH 功能來防止 JVM 刪除代碼。

---

通過遵循這些步驟，您可以使用 `org.openjdk.jmh` 來準確測量和改進您的 Java 代碼性能。無論您是測試簡單操作還是複雜算法，JMH 都提供了您需要的可靠基準測試工具。