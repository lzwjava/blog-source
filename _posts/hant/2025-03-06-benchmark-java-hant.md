---
audio: false
generated: true
lang: hant
layout: post
title: Java 基準測試
translated: true
type: note
---

Java Microbenchmark Harness (JMH) 是建構、執行及分析 Java 微基準測試的強大工具，可讓開發者在受控且可重複的環境中量測程式碼效能。以下是如何有效使用 JMH 的完整指南。

---

## 1. 專案設定

使用 JMH 前需先將其加入專案，以下分別說明 Maven 與 Gradle 的設定方式：

### **Maven**
在 `pom.xml` 中加入以下依賴項：

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
在 `build.gradle` 中加入以下設定：

```groovy
dependencies {
    implementation 'org.openjdk.jmh:jmh-core:1.36'
    annotationProcessor 'org.openjdk.jmh:jmh-generator-annprocess:1.36'
}
```

這些依賴項提供 JMH 核心函式庫及生成基準測試程式碼所需的註解處理器。

---

## 2. 撰寫基準測試

建立 Java 類別來定義基準測試，使用 `@Benchmark` 註解標記需量測的方法。以下為簡單範例：

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
        // 待測試程式碼
        int a = 1;
        int b = 2;
        int sum = a + b;
    }
}
```

- **`@Benchmark`**：將方法標記為基準測試目標
- **`@BenchmarkMode`**：指定效能量測模式（例如 `Mode.AverageTime` 表示平均執行時間）
- **`@OutputTimeUnit`**：設定結果的時間單位（例如 `TimeUnit.NANOSECONDS`）

---

## 3. 設定基準測試

可透過 JMH 註解自訂基準測試設定：

- **`@Warmup`**：定義預熱階段（例如 `@Warmup(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）
- **`@Measurement`**：設定量測階段（例如 `@Measurement(iterations = 5, time = 1, timeUnit = TimeUnit.SECONDS)`）
- **`@Fork`**：指定 JVM 進程數量（例如 `@Fork(value = 1)` 表示在單一 JVM 實例中執行）
- **`@State`**：定義狀態物件範圍（例如 `@State(Scope.Thread)` 表示執行緒本地狀態）

含設定的完整範例：

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
        // 待測試程式碼
    }
}
```

---

## 4. 執行基準測試

可透過 JMH runner 執行基準測試，以下示範 Maven 操作方式：

### **加入 Maven Shade Plugin**
在 `pom.xml` 中加入以下設定以建立可執行 JAR：

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

### **建置與執行**
1. 建置 JAR 檔：`mvn clean package`
2. 執行基準測試：`java -jar target/benchmarks.jar`

JMH 將執行基準測試並在終端機顯示結果。

---

## 5. 分析結果

JMH 會根據設定輸出效能指標，例如：

```
Benchmark              Mode  Cnt  Score   Error  Units
MyBenchmark.testMethod avgt    5  1.234 ± 0.012  ns/op
```

- **Mode**：基準測試模式（例如 `avgt` 表示平均時間）
- **Cnt**：量測迭代次數
- **Score**：量測到的效能數據（例如每次操作的平均納秒時間）
- **Error**：誤差範圍
- **Units**：量測單位

可根據這些結果評估並優化程式碼效能。

---

## 6. 進階功能

JMH 提供進階工具處理複雜情境：

### **參數化測試**
使用 `@Param` 測試不同輸入值：

```java
@State(Scope.Benchmark)
public class MyBenchmark {
    @Param({"1", "10", "100"})
    private int iterations;

    @Benchmark
    public void testMethod() {
        for (int i = 0; i < iterations; i++) {
            // 待測試程式碼
        }
    }
}
```

### **Blackholes**
透過 `Blackhole` 避免 JVM 優化掉未使用的結果：

```java
@Benchmark
public void testMethod(Blackhole bh) {
    int sum = 1 + 2;
    bh.consume(sum); // 防止死碼消除
}
```

---

## 7. 最佳實踐

- **JVM 預熱**：始終包含預熱階段，確保 JIT 編譯器在量測前完成程式碼優化
- **選擇合適模式**：延遲測試用 `Mode.AverageTime`，吞吐量測試用 `Mode.Throughput`
- **控制執行環境**：在穩定系統上執行基準測試，避免其他程序干擾
- **防止過度優化**：使用 blackholes 或其他 JMH 功能避免 JVM 消除程式碼

---

透過遵循以上步驟，即可運用 `org.openjdk.jmh` 精準量測並提升 Java 程式碼效能。無論是測試簡單操作或複雜演算法，JMH 皆能提供可靠的基準測試工具。