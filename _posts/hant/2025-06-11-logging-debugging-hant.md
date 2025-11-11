---
audio: false
generated: true
lang: hant
layout: post
title: Java 除錯與記錄技術
translated: true
type: note
---

Java 沒有內建的旗標能自動記錄每個執行語句的所有變數和狀態，因為這會產生過於龐大的輸出並嚴重影響效能。不過，你可以透過各種工具、技術和配置來實現詳細的除錯與變數及程式狀態記錄。以下將概述在 Java 中最接近實現此目標的方法，包括除錯旗標、工具和自訂解決方案。

---

### 1. **使用 JVM 除錯旗標搭配除錯器**
Java 虛擬機（JVM）透過 Java 除錯連線協定（JDWP）支援除錯功能。你可以透過傳遞特定的 JVM 旗標來啟用除錯，從而連接除錯器（如 IntelliJ IDEA、Eclipse 或 Visual Studio Code）以逐步監控變數、堆疊追蹤和程式狀態。

#### 如何啟用 JVM 除錯
使用以下 JVM 選項啟動你的 Java 應用程式：
```bash
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyApp
```

- **關鍵旗標**：
  - `-agentlib:jdwp`：啟用 JDWP 代理以進行除錯。
  - `transport=dt_socket`：使用通訊端傳輸進行除錯器通訊。
  - `server=y`：JVM 作為伺服器，等待除錯器連接。
  - `suspend=y`：暫停 JVM 直到除錯器連接（使用 `suspend=n` 則無需等待即可執行）。
  - `address=*:5005`：指定除錯器連接的埠號（例如 5005）。

#### 與除錯器搭配使用
1. **連接除錯器**：使用 IDE 如 IntelliJ IDEA、Eclipse 或 Visual Studio Code 連接到指定埠號（例如 5005）的 JVM。
2. **設定中斷點**：在程式碼中你想要檢查變數和狀態的位置設定中斷點。
3. **逐步執行程式碼**：除錯器允許你逐步執行每個語句，即時檢查變數值、評估運算式和檢視呼叫堆疊。

#### 可獲得的資訊
- 在每個中斷點檢查變數。
- 監控程式狀態（例如區域變數、實例欄位、堆疊框架）。
- 逐步進入、跳過或跳出方法呼叫以追蹤執行過程。

#### 限制
- 需要手動設定中斷點和逐步執行。
- 除非你明確配置監看點或記錄點，否則無法自動記錄每個語句的所有變數。

---

### 2. **使用記錄框架（例如 SLF4J、Log4j 或 Java Logging）**
若要記錄變數值和程式狀態，你可以使用記錄框架如 SLF4J 搭配 Logback、Log4j 或 Java 內建的 `java.util.logging`。然而，這需要你在程式碼中手動加入記錄語句來捕捉變數值和狀態。

#### 使用 SLF4J 和 Logback 的範例
1. **加入依賴項**（例如 Maven）：

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.4.11</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>2.0.9</version>
</dependency>
```

2. **配置 Logback**（`logback.xml`）：

```xml
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    <root level="DEBUG">
        <appender-ref ref="CONSOLE" />
    </root>
</configuration>
```

3. **在程式碼中加入記錄**：

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyApp {
    private static final Logger logger = LoggerFactory.getLogger(MyApp.class);

    public static void main(String[] args) {
        int x = 10;
        String message = "Hello";
        logger.debug("Variable x: {}, message: {}", x, message);
        x++;
        logger.debug("After increment, x: {}", x);
    }
}
```

#### 輸出
```
2025-06-06 20:50:00 DEBUG MyApp - Variable x: 10, message: Hello
2025-06-06 20:50:00 DEBUG MyApp - After increment, x: 11
```

#### 注意事項
- **優點**：你可以在所需位置記錄特定變數和狀態，並自訂格式。
- **缺點**：需要為每個你想追蹤的變數或狀態手動加入記錄語句。若無程式碼插樁，自動記錄每個變數是不切實際的。

---

### 3. **使用工具進行位元組碼插樁（例如 Java Agents、Byte Buddy 或 AspectJ）**
若要自動記錄每個變數和狀態而無需修改原始碼，你可以使用位元組碼插樁技術，在執行時或編譯時注入記錄邏輯。這種方法最接近你對自動記錄每個語句的需求。

#### 選項 1：使用 Byte Buddy 的 Java Agent
Byte Buddy 是一個函式庫，允許你建立 Java 代理以動態攔截方法呼叫並記錄變數狀態。

1. **加入 Byte Buddy 依賴項**（Maven）：

```xml
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy</artifactId>
    <version>1.14.9</version>
</dependency>
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy-agent</artifactId>
    <version>1.14.9</version>
</dependency>
```

2. **建立 Java Agent**：

```java
import net.bytebuddy.agent.builder.AgentBuilder;
import net.bytebuddy.description.type.TypeDescription;
import net.bytebuddy.dynamic.DynamicType;
import net.bytebuddy.implementation.MethodDelegation;
import net.bytebuddy.matcher.ElementMatchers;
import java.lang.instrument.Instrumentation;

public class LoggingAgent {
    public static void premain(String args, Instrumentation inst) {
        new AgentBuilder.Default()
            .type(ElementMatchers.any())
            .transform((builder, type, classLoader, module) -> 
                builder.method(ElementMatchers.any())
                       .intercept(MethodDelegation.to(LoggingInterceptor.class)))
            .installOn(inst);
    }
}
```

3. **建立攔截器**：

```java
import net.bytebuddy.implementation.bind.annotation.AllArguments;
import net.bytebuddy.implementation.bind.annotation.Origin;
import net.bytebuddy.implementation.bind.annotation.RuntimeType;

import java.lang.reflect.Method;
import java.util.Arrays;

public class LoggingInterceptor {
    @RuntimeType
    public static Object intercept(@Origin Method method, @AllArguments Object[] args) throws Exception {
        System.out.println("Executing: " + method.getName() + " with args: " + Arrays.toString(args));
        // 繼續執行原始方法呼叫
        return method.invoke(null, args);
    }
}
```

4. **使用代理執行**：
```bash
java -javaagent:logging-agent.jar -cp . MyApp
```

#### 注意事項
- **優點**：能自動記錄方法呼叫、參數，並透過檢查堆疊或位元組碼來捕捉變數狀態。
- **缺點**：記錄每個語句的所有變數需要複雜的位元組碼分析，這可能速度緩慢且難以全面實現。你可能需要進一步自訂代理以捕捉區域變數。

#### 選項 2：使用 AspectJ 進行面向切面程式設計
AspectJ 允許你定義切面以攔截程式碼執行並記錄變數狀態。

1. **加入 AspectJ 依賴項**（Maven）：

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.22</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.22</version>
</dependency>
```

2. **定義切面**：

```java
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;

@Aspect
public class LoggingAspect {
    @After("execution(* *(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());
        System.out.println("Arguments: " + Arrays.toString(joinPoint.getArgs()));
    }
}
```

3. **使用 AspectJ 執行**：
透過加入代理使用 AspectJ 織入器：
```bash
java -javaagent:aspectjweaver.jar -cp . MyApp
```

#### 注意事項
- **優點**：能自動記錄方法執行和參數。
- **缺點**：捕捉每個區域變數和狀態需要進階的切入點配置，且可能需要原始碼修改或執行時織入。

---

### 4. **使用 IDE 特定的除錯功能**
現代 IDE 如 IntelliJ IDEA、Eclipse 或 Visual Studio Code 提供進階除錯功能，可模擬你想要的行為：

- **記錄點**：IntelliJ IDEA 和 Eclipse 允許你設定「記錄點」（或「追蹤點」），在不暫停執行的情況下輸出變數值。
- **變數監看**：你可以監看特定變數並在每個步驟記錄其值。
- **條件中斷點**：設定在符合特定條件時記錄變數的中斷點。

#### 在 IntelliJ IDEA 中的範例
1. 設定中斷點。
2. 右鍵點擊中斷點，選擇「More」或「Edit Breakpoint」。
3. 啟用「Evaluate and Log」以輸出變數值或運算式（例如 `System.out.println("x = " + x)`）。
4. 逐步執行程式碼以在每個語句記錄狀態。

#### 注意事項
- **優點**：非侵入性且易於為特定變數或方法設定。
- **缺點**：非全自動；你需要指定要記錄的內容。

---

### 5. **自訂程式碼插樁**
為了完全控制，你可以編寫工具來解析和修改 Java 原始碼或位元組碼，為每個變數和語句插入記錄語句。像 **ASM** 或 **Javassist** 這樣的工具可以協助進行位元組碼操作，但這很複雜，通常用於進階使用情境。

#### 範例工作流程
1. 使用像 ASM 這樣的函式庫解析 Java 原始碼或位元組碼。
2. 識別所有區域變數和語句。
3. 在每個語句前後插入記錄呼叫（例如 `System.out.println("Variable x = " + x)`）。
4. 編譯並執行修改後的程式碼。

由於複雜性和效能開銷，這種方法在大型專案中很少實用。

---

### 6. **用於追蹤和分析的現有工具**
有幾種工具可以幫助追蹤和記錄程式執行而無需修改程式碼：

- **Java Flight Recorder（JFR）**：
  - 使用 JVM 旗標啟用 JFR：
    ```bash
    java -XX:StartFlightRecording=settings=profile,dumponexit=true,filename=recording.jfr MyApp
    ```
  - 使用 JDK Mission Control 分析記錄，以檢視方法呼叫、堆疊追蹤和事件。
  - **限制**：不記錄每個變數，但提供詳細的執行追蹤。

- **VisualVM**：
  - 一個分析工具，可以監控方法呼叫、記憶體使用和 CPU 活動。
  - 搭配 VisualVM-MBeans 插件使用以記錄特定變數或狀態。
  - **限制**：需要手動配置以記錄變數。

- **BTrace**：
  - 一個 Java 動態追蹤工具，允許你將追蹤邏輯注入到執行中的 JVM。
  - 範例腳本：

    ```java
    import com.sun.btrace.annotations.*;
    import static com.sun.btrace.BTraceUtils.*;

    @BTrace
    public class TraceVariables {
        @OnMethod(clazz = "MyApp", method = "main")
        public static void trace(@ProbeMethodName String methodName, @AllLocals Object[] locals) {
            println("Method: " + methodName + ", Locals: " + Arrays.toString(locals));
        }
    }
    ```
  - **限制**：需要謹慎編寫腳本，且可能不易捕捉所有區域變數。

---

### 建議
由於效能和輸出量的考量，沒有單一的 JVM 旗標能自動記錄每個語句的所有變數和狀態。相反地，請根據你的需求考慮以下方法：

- **用於開發**：使用除錯器（例如 IntelliJ IDEA）搭配中斷點和記錄點以進行細粒度控制。
- **用於自動記錄**：使用記錄框架（SLF4J/Logback）搭配手動記錄語句，或使用 AspectJ 進行方法層級的記錄。
- **用於進階使用情境**：實作使用 Byte Buddy 的 Java 代理，或使用 BTrace 進行動態追蹤。
- **用於生產環境監控**：使用 Java Flight Recorder 或 VisualVM 進行分析而無需修改程式碼。

如果你想自動記錄特定變數或方法，我可以協助你設定 Java 代理或 AspectJ 配置。或者，如果你有特定的程式碼片段，我可以示範如何加入記錄或有效除錯。請告訴我你的偏好或限制！