---
audio: false
generated: true
lang: hant
layout: post
title: 理解切入點表達式
translated: true
type: note
---

你正在尋求一份關於 AspectJ 切入點表達式的綜合指南，特別是針對 `execution` 的使用方法，包括如何使用萬用字元、匹配類別名稱（前綴/後綴），以及關於其他通知類型如 `@AfterReturning`。讓我們來詳細解析。

### 理解 Spring AOP 中的切入點表達式（AspectJ 語法）

Spring AOP 使用 AspectJ 切入點表達式來決定通知（如 `@Before`、`@AfterReturning` 等）應該在*何處*應用。你問題的核心圍繞著 `execution` 切入點指示符，這是最常用的一個。

#### `execution` 切入點指示符

`execution` 切入點指示符匹配方法執行。其通用語法為：

`execution(修飾符模式? 返回類型模式 宣告類型模式?名稱模式(參數模式) 異常模式?)`

讓我們分解各個部分：

* **`修飾符模式?`**: 可選。匹配方法修飾符（例如 `public`、`private`、`protected`）。
* **`返回類型模式`**: 必需。匹配方法的返回類型。
* **`宣告類型模式?`**: 可選。匹配方法宣告所在類別的完整限定名稱。
* **`名稱模式`**: 必需。匹配方法的名稱。
* **`參數模式`**: 必需。匹配方法的參數。
* **`異常模式?`**: 可選。匹配方法拋出的異常。

#### 你的範例：`@Before("execution(* com.example.service.*.*(..))")`

讓我們剖析你給出的範例：

* `@Before`: 這是一個通知註解，意味著被註解的方法將在匹配的連接點*之前*運行。
* `execution()`: 切入點指示符。
* `*`: 匹配任何返回類型。
* `com.example.service.*.*`:
    * `com.example.service`: 匹配套件 `com.example.service`。
    * `.*`: `service` 之後的第一個 `*` 匹配 `com.example.service` 套件內的任何類別。
    * `.`: 套件/類別和方法之間的分隔符。
    * `*`: 第二個 `*` 匹配這些類別內的任何方法名稱。
* `(..)`: 匹配任意數量的參數（零個或多個，任何類型）。

**簡單來說：** 這個切入點匹配在 `com.example.service` 套件內的*任何類別*中的*任何方法*的執行。

---

### 切入點表達式中的萬用字元

萬用字元對於創建靈活的切入點表達式至關重要。

* **`*` (單個星號)**:
    * 匹配名稱模式中的任何單個元素（例如，任何返回類型、任何類別名稱、任何方法名稱）。
    * 匹配套件名稱中的任何單個區段（例如，`com.example.*.service` 會匹配 `com.example.foo.service`）。
* **`..` (雙點)**:
    * **在套件模式中**: 匹配套件名稱中的零個或多個區段。
        * `com.example..service`: 匹配 `com.example.service`、`com.example.foo.service`、`com.example.foo.bar.service` 等。
    * **在參數模式中**: 匹配零個或多個任何類型的參數。
        * `(..)`: 匹配任意數量的參數。
        * `(java.lang.String, ..)`: 匹配第一個參數是 `String`，後面跟著任意數量其他參數的方法。
        * `(.., java.lang.Long)`: 匹配前面有任意數量參數，最後一個參數是 `Long` 的方法。

---

### 匹配類別名稱

#### 1. 匹配後綴類別名稱

要匹配以特定後綴結尾的類別，你將萬用字元放在後綴之前。

**範例：匹配所有以 `ServiceImpl` 結尾的類別**

```java
@Before("execution(* com.example.service.*ServiceImpl.*(..))")
```

* `*ServiceImpl`: 匹配任何以 `ServiceImpl` 結尾的類別名稱。

**範例：匹配 `com.example.web` 任何子套件中所有以 `Controller` 結尾的類別**

```java
@Before("execution(* com.example.web..*Controller.*(..))")
```

* `com.example.web..`: 匹配 `com.example.web` 及其任何子套件。
* `*Controller`: 匹配任何以 `Controller` 結尾的類別名稱。

#### 2. 匹配前綴類別名稱

要匹配以特定前綴開頭的類別，你將萬用字元放在前綴之後。

**範例：匹配所有以 `User` 開頭的類別**

```java
@Before("execution(* com.example.service.User*.*(..))")
```

* `User*`: 匹配任何以 `User` 開頭的類別名稱。

**範例：匹配 `com.example.admin` 套件中所有以 `Admin` 開頭的類別**

```java
@Before("execution(* com.example.admin.Admin*.*(..))")
```

#### 3. 匹配特定類別名稱（精確匹配）

精確匹配不需要萬用字元。

**範例：僅匹配 `com.example.service.UserServiceImpl` 中的方法**

```java
@Before("execution(* com.example.service.UserServiceImpl.*(..))")
```

---

### 不同類型的切入點指示符

雖然 `execution` 是最常用的，但 AspectJ 提供了其他幾個切入點指示符來指定連接點。你可以使用邏輯運算符（`and`、`or`、`not` 或 `&&`、`||`、`!`）來組合它們。

以下是最重要的幾個：

1.  **`execution()`**: 如前所述，匹配方法執行。
    * 範例：`@Before("execution(* com.example.service.UserService.*(..))")`

2.  **`within()`**: 匹配程式碼位於特定類型（類別）內的連接點。這通常用於限制其他切入點的範圍。
    * 範例：`@Before("within(com.example.service.*) && execution(* *(..))")`
        * 這結合了 `within` 和 `execution`。意思是「在 `com.example.service` 套件內任何類別中的任何方法執行」。`execution` 部分則只是任何方法的萬用字元，因為 `within` 處理了類別匹配。

3.  **`this()`**: 匹配代理*本身*是給定類型實例的連接點。這在簡單通知中較少使用，更多用於引入或自調用問題。
    * 範例：`@Around("this(com.example.service.UserService)")`
        * 如果 AOP 代理實現了 `UserService` 則匹配。

4.  **`target()`**: 匹配*目標物件*（被通知的實際物件，不是代理）是給定類型實例的連接點。當你關心底層實現時，這通常比 `this()` 更直觀。
    * 範例：`@Around("target(com.example.service.UserServiceImpl)")`
        * 如果目標物件是 `UserServiceImpl` 的實例則匹配。

5.  **`args()`**: 匹配參數是特定類型或符合特定模式的連接點。
    * 範例：`@Before("execution(* com.example.service.*.*(String, ..))")`
        * 匹配第一個參數是 `String` 的方法。
    * 範例：`@Before("args(java.lang.String, int)")`
        * 匹配恰好接受一個 `String` 和一個 `int` 的方法。
    * 範例：`@Before("args(name, age)")`，其中 `name` 和 `age` 可以綁定到通知方法的參數。

6.  **`bean()`**: (Spring 特有) 匹配在具有特定名稱或名稱模式的 Spring Bean 上執行的方法。
    * 範例：`@Before("bean(userService) && execution(* *(..))")`
        * 匹配在名為 "userService" 的 Spring Bean 上的任何方法執行。
    * 範例：`@Before("bean(*Service) && execution(* *(..))")`
        * 匹配在名稱以 "Service" 結尾的 Spring Bean 上的任何方法執行。

7.  **`@annotation()`**: 匹配目標方法（或對於 `within` 是類別）帶有特定註解的連接點。
    * 範例：`@Before("@annotation(com.example.annotation.Loggable)")`
        * 匹配任何帶有 `@Loggable` 註解的方法。
    * 範例：`@Before("execution(* *(..)) && @annotation(org.springframework.transaction.annotation.Transactional)")`
        * 匹配任何帶有 `@Transactional` 註解的方法執行。

8.  **`@within()`**: 匹配宣告類型（類別）帶有特定註解的連接點。
    * 範例：`@Before("@within(org.springframework.stereotype.Service) && execution(* *(..))")`
        * 匹配在帶有 `@Service` 註解的類別內的任何方法執行。

9.  **`@target()`**: 匹配目標物件的類別帶有給定註解的連接點。
    * 範例：`@Around("@target(com.example.annotation.Auditable)")`

10. **`@args()`**: 匹配傳遞給方法的實際參數的運行時類型帶有給定類型註解的連接點。
    * 範例：`@Before("@args(com.example.annotation.ValidInput)")`

---

### 通知類型（註解）

你提到了 `@AfterReturning` 和「我們可以在註解中使用的任何其他類型」。Spring AOP 提供了幾種通知類型，每種在連接點生命週期的不同點執行：

1.  **`@Before`**:
    * 在匹配的方法執行*之前*執行。
    * 範例：在服務方法運行前記錄請求詳情。
    * 無法阻止方法執行或改變其返回值。

2.  **`@AfterReturning`**:
    * 在匹配的方法*成功*返回後（未拋出異常）執行。
    * 可以訪問方法的返回值。
    * 語法：`@AfterReturning(pointcut="yourPointcut()", returning="result")`
    * 範例：
        ```java
        @AfterReturning(pointcut="execution(* com.example.service.UserService.getUserById(..))", returning="user")
        public void logUserRetrieval(Object user) {
            System.out.println("User retrieved: " + user);
        }
        ```
        *注意：`returning` 屬性名稱（此處為 `user`）必須與通知方法中的參數名稱匹配。*

3.  **`@AfterThrowing`**:
    * 在匹配的方法拋出異常後執行。
    * 可以訪問拋出的異常。
    * 語法：`@AfterThrowing(pointcut="yourPointcut()", throwing="ex")`
    * 範例：
        ```java
        @AfterThrowing(pointcut="execution(* com.example.service.*.*(..))", throwing="ex")
        public void logException(Exception ex) {
            System.err.println("Exception occurred: " + ex.getMessage());
        }
        ```
        *注意：`throwing` 屬性名稱（此處為 `ex`）必須與通知方法中的參數名稱匹配。*

4.  **`@After` (finally advice)**:
    * 在匹配的方法完成後執行，無論它是成功返回還是拋出異常。
    * 類似於 `finally` 區塊。
    * 範例：無論方法結果如何，都釋放資源。
    * ```java
        @After("execution(* com.example.service.OrderService.placeOrder(..))")
        public void cleanupOrderProcess() {
            System.out.println("Order process completed (cleanup)");
        }
        ```

5.  **`@Around`**:
    * 最強大和最靈活的通知類型。
    * 在匹配的方法執行*周圍*執行。
    * 你需要負責使用 `ProceedingJoinPoint.proceed()` 來調用實際方法。
    * 可以檢查、修改甚至抑制方法的參數和返回值。
    * 可以捕獲並處理被通知方法拋出的異常。
    * 範例：性能監控、事務管理、快取。
    * ```java
        import org.aspectj.lang.ProceedingJoinPoint;
        import org.aspectj.lang.annotation.Around;
        import org.aspectj.lang.annotation.Aspect;

        @Aspect
        public class PerformanceMonitorAspect {

            @Around("execution(* com.example.service.*.*(..))")
            public Object profile(ProceedingJoinPoint joinPoint) throws Throwable {
                long start = System.currentTimeMillis();
                Object result = joinPoint.proceed(); // 執行原始方法
                long end = System.currentTimeMillis();
                System.out.println(joinPoint.getSignature().getName() + " executed in " + (end - start) + "ms");
                return result;
            }
        }
        ```

### 定義可重用的切入點

為了更好的可讀性和可重用性，你可以使用 `@Pointcut` 來定義命名切入點。

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.AfterReturning;

@Aspect
public class MyServiceAspect {

    // 為 com.example.service 套件中的所有方法定義一個切入點
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // 為返回 User 物件的方法定義一個切入點
    @Pointcut("execution(com.example.model.User com.example.service.*.*(..))")
    public void returnsUser() {}

    // 使用定義的切入點
    @Before("serviceMethods()")
    public void logBeforeServiceCall() {
        System.out.println("Before service method execution.");
    }

    // 使用邏輯 AND 組合切入點
    @AfterReturning(pointcut="serviceMethods() && returnsUser()", returning="user")
    public void logUserReturned(Object user) {
        System.out.println("Service method returned user: " + user);
    }

    // 你也可以定義帶參數的切入點
    @Pointcut("execution(* com.example.repository.*.save(..)) && args(entity)")
    public void repositorySave(Object entity) {}

    @Before("repositorySave(entity)")
    public void logEntityBeforeSave(Object entity) {
        System.out.println("Saving entity: " + entity);
    }
}
```

這份綜合指南涵蓋了 Spring AOP 中切入點表達式、萬用字元使用、類別名稱匹配以及不同通知類型的基本要點。掌握這些概念將使你能夠精確控制橫切關注點的應用位置和時機。