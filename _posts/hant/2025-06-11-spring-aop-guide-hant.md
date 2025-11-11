---
audio: false
generated: true
lang: hant
layout: post
title: Spring AOP 入門指南
translated: true
type: note
---

## 1. Spring AOP 簡介

Spring AOP（面向切面程式設計）是 Spring Framework 的關鍵組件，提供了一種將橫切關注點（如日誌記錄、安全性、事務管理）與業務邏輯分開實作的方法。

### 核心概念：
- **橫切關注點**：跨越多個層級的功能（日誌記錄、安全性等）
- **切面**：跨越多個類別的關注點模組化
- **連接點**：程式執行過程中的點（方法執行、異常處理等）
- **通知**：切面在特定連接點執行的動作
- **切入點**：匹配連接點的謂詞
- **織入**：將切面與其他應用程式類型連結以建立建議物件

## 2. Spring AOP 與 AspectJ 比較

| 功能特性           | Spring AOP | AspectJ |
|-------------------|-----------|---------|
| 實作方式          | 運行時代理 | 編譯時/載入時織入 |
| 性能              | 較慢 | 較快 |
| 支援的連接點      | 僅方法執行 | 全部（方法、構造函數、字段訪問等） |
| 複雜度            | 較簡單 | 較複雜 |
| 依賴關係          | 無額外依賴 | 需要 AspectJ 編譯器/織入器 |

## 3. 核心 AOP 組件

### 3.1 切面
使用 `@Aspect` 註解的類，包含通知和切入點。

```java
@Aspect
@Component
public class LoggingAspect {
    // 通知和切入點將放在這裡
}
```

### 3.2 通知類型

1. **Before**：在連接點之前執行
   ```java
   @Before("execution(* com.example.service.*.*(..))")
   public void beforeAdvice() {
       System.out.println("Before method execution");
   }
   ```

2. **AfterReturning**：在連接點正常完成後執行
   ```java
   @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", returning = "result")
   public void afterReturningAdvice(Object result) {
       System.out.println("Method returned: " + result);
   }
   ```

3. **AfterThrowing**：如果方法通過拋出異常退出時執行
   ```java
   @AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", throwing = "ex")
   public void afterThrowingAdvice(Exception ex) {
       System.out.println("Exception thrown: " + ex.getMessage());
   }
   ```

4. **After (Finally)**：在連接點之後執行，無論結果如何
   ```java
   @After("execution(* com.example.service.*.*(..))")
   public void afterAdvice() {
       System.out.println("After method execution (finally)");
   }
   ```

5. **Around**：包裝連接點，最強大的通知
   ```java
   @Around("execution(* com.example.service.*.*(..))")
   public Object aroundAdvice(ProceedingJoinPoint joinPoint) throws Throwable {
       System.out.println("Before proceeding");
       Object result = joinPoint.proceed();
       System.out.println("After proceeding");
       return result;
   }
   ```

### 3.3 切入點表達式

切入點使用表達式定義通知應用的位置：

- **Execution**：匹配方法執行
  ```java
  @Pointcut("execution(public * com.example.service.*.*(..))")
  public void serviceMethods() {}
  ```

- **Within**：匹配特定類型內的所有連接點
  ```java
  @Pointcut("within(com.example.service..*)")
  public void inServiceLayer() {}
  ```

- **this**：匹配給定類型實例的 bean
- **target**：匹配可分配給給定類型的 bean
- **args**：匹配具有特定參數類型的方法
- **@annotation**：匹配具有特定註解的方法

### 3.4 組合切入點

可以使用邏輯運算符組合切入點：
```java
@Pointcut("execution(* com.example.service.*.*(..)) && !execution(* com.example.service.UserService.*(..))")
public void serviceMethodsExceptUserService() {}
```

## 4. 實作步驟

### 4.1 設置

1. 添加 Spring AOP 依賴（如果未使用 Spring Boot）：
   ```xml
   <dependency>
       <groupId>org.springframework</groupId>
       <artifactId>spring-aop</artifactId>
       <version>${spring.version}</version>
   </dependency>
   <dependency>
       <groupId>org.aspectj</groupId>
       <artifactId>aspectjweaver</artifactId>
       <version>${aspectj.version}</version>
   </dependency>
   ```

2. 對於 Spring Boot，只需包含 `spring-boot-starter-aop`：
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-aop</artifactId>
   </dependency>
   ```

3. 在配置中啟用 AOP：
   ```java
   @Configuration
   @EnableAspectJAutoProxy
   public class AppConfig {
   }
   ```

### 4.2 建立切面

```java
@Aspect
@Component
public class LoggingAspect {
    
    private final Logger logger = LoggerFactory.getLogger(this.getClass());
    
    @Before("execution(* com.example.service.*.*(..))")
    public void logBefore(JoinPoint joinPoint) {
        logger.info("Entering: {}.{}() with arguments = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            Arrays.toString(joinPoint.getArgs()));
    }
    
    @AfterReturning(pointcut = "execution(* com.example.service.*.*(..))", 
                   returning = "result")
    public void logAfterReturning(JoinPoint joinPoint, Object result) {
        logger.info("Exiting: {}.{}() with result = {}", 
            joinPoint.getSignature().getDeclaringTypeName(),
            joinPoint.getSignature().getName(),
            result);
    }
    
    @Around("@annotation(com.example.annotations.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        Object proceed = joinPoint.proceed();
        long executionTime = System.currentTimeMillis() - start;
        logger.info("{} executed in {} ms", 
            joinPoint.getSignature(), executionTime);
        return proceed;
    }
}
```

### 4.3 自定義註解

建立自定義註解以標記需要特定 AOP 行為的方法：

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

然後在方法上使用它：
```java
@Service
public class UserService {
    
    @LogExecutionTime
    public User getUser(Long id) {
        // implementation
    }
}
```

## 5. 進階主題

### 5.1 切面排序

使用 `@Order` 控制切面執行順序：
```java
@Aspect
@Component
@Order(1)
public class LoggingAspect {
    // ...
}

@Aspect
@Component
@Order(2)
public class ValidationAspect {
    // ...
}
```

### 5.2 訪問方法信息

在通知方法中，可以訪問：
- `JoinPoint`（適用於 Before、After、AfterReturning、AfterThrowing）
- `ProceedingJoinPoint`（適用於 Around）

```java
@Before("execution(* com.example.service.*.*(..))")
public void beforeAdvice(JoinPoint joinPoint) {
    String methodName = joinPoint.getSignature().getName();
    String className = joinPoint.getTarget().getClass().getName();
    Object[] args = joinPoint.getArgs();
    // ...
}
```

### 5.3 異常處理

```java
@AfterThrowing(pointcut = "execution(* com.example.service.*.*(..))", 
               throwing = "ex")
public void handleException(JoinPoint joinPoint, Exception ex) {
    // 記錄異常、發送警報等
}
```

### 5.4 代理機制

Spring AOP 使用兩種類型的代理：
- **JDK 動態代理**：接口的默認選項
- **CGLIB 代理**：當沒有接口可用時使用（可通過 `proxyTargetClass=true` 強制使用）

## 6. 最佳實踐

1. **保持切面專注**：每個切面應處理一個特定的橫切關注點
2. **使用有意義的切入點名稱**：使程式碼更易讀
3. **避免在切面中進行昂貴操作**：它們會為每個匹配的連接點運行
4. **謹慎使用 Around 通知**：除非有意阻止執行，否則始終調用 `proceed()`
5. **徹底測試切面**：它們會影響應用程式的多個部分
6. **記錄切面**：特別是當它們顯著修改行為時
7. **考慮性能**：複雜的切入點或多個切面可能影響性能

## 7. 常見使用場景

1. **日誌記錄**：方法進入/退出、參數、返回值
2. **性能監控**：測量執行時間
3. **事務管理**：（雖然通常由 Spring 的 `@Transactional` 處理）
4. **安全性**：授權檢查
5. **驗證**：參數驗證
6. **錯誤處理**：一致的異常處理
7. **緩存**：方法結果緩存
8. **審計**：跟踪誰在何時調用了什麼

## 8. 限制

1. 僅適用於 Spring 管理的 bean
2. 僅支援方法執行連接點
3. 無法建議 final 類或方法
4. 自調用（類內方法調用同一類的另一方法）會繞過代理
5. 與 AspectJ 相比，切入點表達式有限

## 9. 疑難排解

**問題**：通知未執行
- 檢查 bean 是否由 Spring 管理
- 驗證切入點表達式是否匹配預期方法
- 確保存在 `@EnableAspectJAutoProxy`

**問題**：Around 通知未繼續執行
- 確保在 `ProceedingJoinPoint` 上調用 `proceed()`

**問題**：代理類型不正確
- 使用 `@EnableAspectJAutoProxy(proxyTargetClass=true)` 強制使用 CGLIB

## 10. 結論

Spring AOP 提供了一種強大而簡單的方法來實作應用程式中的橫切關注點。雖然與完整的 AspectJ 相比有一些限制，但它與 Spring 無縫集成並涵蓋了大多數常見使用場景。通過遵循本指南中概述的模式和最佳實踐，您可以有效地模組化橫切關注點，並保持業務邏輯的清晰和專注。

---

儘管 Spring AOP 不使用 AspectJ 的織入功能（它使用基於代理的 AOP），但您仍然需要 `aspectjweaver` 依賴，原因如下：

### 1. **AspectJ 註解支援**
Spring AOP 使用 AspectJ 的**註解**（如 `@Aspect`、`@Pointcut`、`@Before`、`@After` 等）來定義切面和通知。

- 沒有它，使用 `@Aspect` 或其他 AOP 註解時會出現編譯錯誤。

### 2. **切入點表達式語言**
Spring AOP 借用 AspectJ 的**切入點表達式語言**來定義通知應用的位置（例如 `execution(* com.example.service.*.*(..))`）。

- `aspectjweaver` 提供這些表達式的解析器和匹配邏輯。

### 3. **對其他連接點的支援（有限）**
雖然 Spring AOP 僅支援**方法執行**連接點（與支援構造函數、字段訪問等的 AspectJ 不同），但它仍然依賴 AspectJ 的底層切入點匹配機制。

### 4. **載入時織入（可選）**
如果您決定在 Spring AOP 中使用**載入時織入（LTW）**（這種情況很少見但可能），則需要 `aspectjweaver`。LTW 允許在類加載時織入切面，而不是使用代理。

```java
@EnableLoadTimeWeaving
public class AppConfig { ... }
```

### 5. **與 @EnableAspectJAutoProxy 的兼容性**
當您使用 `@EnableAspectJAutoProxy` 時，Spring 在內部使用 AspectJ 的基礎設施來處理 AOP 註解，即使它不進行完整的 AspectJ 織入。

---

### **是否始終需要它？**
- **如果使用 Spring Boot（`spring-boot-starter-aop`）**：不需要，因為它傳遞性地包含了 `aspectjweaver`。
- **如果使用純 Spring AOP**：是的，您必須明確包含它。

### **替代方案？**
- 如果您使用**完整 AspectJ**（編譯時或載入時織入），則還需要 `aspectjrt` 和 `aspectjtools`。
- 但對於 **Spring AOP**，僅 `aspectjweaver` 就足夠了。

### **結論**
Spring AOP 是**基於代理的**，但它**重用了 AspectJ 的註解和切入點語法**，這就是為什麼需要 `aspectjweaver` 的原因。它彌合了 Spring 的代理方法與 AspectJ 更強大的 AOP 模型之間的差距。