---
audio: false
generated: true
lang: hant
layout: post
title: AspectJ 與 Java 及 Spring Boot
translated: true
type: note
---

## 目錄
1. [面向切面程式設計 (AOP) 簡介](#面向切面程式設計-aop-簡介)
2. [AspectJ 概述](#aspectj-概述)
3. [AspectJ 與 Java](#aspectj-與-java)
4. [AspectJ 與 Spring Boot](#aspectj-與-spring-boot)
5. [常見使用場景](#常見使用場景)
6. [最佳實踐](#最佳實踐)
7. [效能考量](#效能考量)

## 面向切面程式設計 (AOP) 簡介

AOP 是一種程式設計範式，旨在通過分離橫切關注點來提高模組化程度。橫切關注點是指跨越系統多個部分的功能（例如日誌記錄、安全性、事務管理）。

AOP 核心概念：
- **切面**：對橫跨多個類別的關注點進行模組化
- **連接點**：程式執行過程中的某個點（方法呼叫、欄位存取等）
- **通知**：在特定連接點執行的動作
- **切入點**：匹配連接點的謂詞
- **織入**：將切面與其他應用程式類型連結起來

## AspectJ 概述

AspectJ 是 Java 中最流行且功能最完整的 AOP 實作。它提供：
- 強大的切入點語言
- 不同的織入機制（編譯時、編譯後、載入時）
- 超越 Spring AOP 的完整 AOP 支援

### AspectJ 與 Spring AOP 對比

| 功能特性         | AspectJ | Spring AOP |
|------------------|---------|------------|
| 連接點           | 方法執行、建構函式呼叫、欄位存取等 | 僅限方法執行 |
| 織入方式         | 編譯時、編譯後、載入時 | 執行時代理 |
| 效能表現         | 更佳（無執行時開銷） | 稍慢（使用代理） |
| 複雜度           | 較複雜 | 較簡單 |
| 依賴項           | 需要 AspectJ 編譯器/織入器 | 內建於 Spring 中 |

## AspectJ 與 Java

### 環境設定

1. 在 `pom.xml` 中添加 AspectJ 依賴項（Maven）：

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.7</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. 配置 AspectJ Maven 插件以實現編譯時織入：

```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>aspectj-maven-plugin</artifactId>
    <version>1.14.0</version>
    <configuration>
        <complianceLevel>11</complianceLevel>
        <source>11</source>
        <target>11</target>
        <showWeaveInfo>true</showWeaveInfo>
        <verbose>true</verbose>
        <Xlint>ignore</Xlint>
        <encoding>UTF-8</encoding>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>compile</goal>
                <goal>test-compile</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

### 建立切面

```java
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.aspectj.lang.annotation.Pointcut;

@Aspect
public class LoggingAspect {

    // 切入點定義
    @Pointcut("execution(* com.example.service.*.*(..))")
    public void serviceMethods() {}

    // 通知
    @Before("serviceMethods()")
    public void logBeforeServiceMethods() {
        System.out.println("服務方法即將執行");
    }
}
```

### 通知類型

1. **Before**：在連接點之前執行
2. **After**：在連接點完成後執行（正常或異常）
3. **AfterReturning**：在連接點正常完成後執行
4. **AfterThrowing**：在方法因拋出異常而退出時執行
5. **Around**：環繞連接點（功能最強大的通知）

### 切入點表達式

AspectJ 提供豐富的切入點表達式語言：

```java
// 套件中的方法執行
@Pointcut("execution(* com.example.service.*.*(..))")

// 類別中的方法執行
@Pointcut("execution(* com.example.service.UserService.*(..))")

// 特定名稱的方法
@Pointcut("execution(* *..find*(..))")

// 特定返回類型
@Pointcut("execution(public String com.example..*(..))")

// 特定參數類型
@Pointcut("execution(* *.*(String, int))")

// 組合切入點
@Pointcut("serviceMethods() && findMethods()")
```

## AspectJ 與 Spring Boot

### 環境設定

1. 添加 Spring AOP 和 AspectJ 依賴項：

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.7</version>
</dependency>
```

2. 在 Spring Boot 應用程式中啟用 AspectJ 支援：

```java
@SpringBootApplication
@EnableAspectJAutoProxy
public class MyApplication {
    public static void main(String[] args) {
        SpringApplication.run(MyApplication.class, args);
    }
}
```

### 範例：記錄執行時間

```java
@Aspect
@Component
public class ExecutionTimeAspect {

    private static final Logger logger = LoggerFactory.getLogger(ExecutionTimeAspect.class);

    @Around("@annotation(com.example.annotation.LogExecutionTime)")
    public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
        long startTime = System.currentTimeMillis();
        
        Object proceed = joinPoint.proceed();
        
        long executionTime = System.currentTimeMillis() - startTime;
        
        logger.info("{} 在 {} ms 內執行完成", 
            joinPoint.getSignature(), executionTime);
        
        return proceed;
    }
}
```

建立自定義註解：

```java
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface LogExecutionTime {
}
```

在方法上使用：

```java
@Service
public class UserService {
    
    @LogExecutionTime
    public List<User> getAllUsers() {
        // 實作
    }
}
```

### 範例：事務管理

```java
@Aspect
@Component
public class TransactionAspect {

    @Autowired
    private PlatformTransactionManager transactionManager;

    @Around("@annotation(com.example.annotation.Transactional)")
    public Object manageTransaction(ProceedingJoinPoint joinPoint) throws Throwable {
        TransactionDefinition def = new DefaultTransactionDefinition();
        TransactionStatus status = transactionManager.getTransaction(def);
        
        try {
            Object result = joinPoint.proceed();
            transactionManager.commit(status);
            return result;
        } catch (Exception e) {
            transactionManager.rollback(status);
            throw e;
        }
    }
}
```

## 常見使用場景

1. **日誌記錄**：集中記錄方法進入/異常
2. **效能監控**：追蹤執行時間
3. **事務管理**：宣告式事務邊界
4. **安全性**：授權檢查
5. **錯誤處理**：一致的異常處理
6. **快取**：自動方法結果快取
7. **驗證**：參數驗證
8. **審計**：追蹤操作人員和時間

## 最佳實踐

1. **保持切面專注**：每個切面應處理一個關注點
2. **使用有意義的名稱**：清晰的切面和切入點名稱
3. **避免在切面中包含業務邏輯**：切面應處理橫切關注點，而非核心邏輯
4. **記錄切面**：特別是複雜的切入點
5. **考慮效能**：環繞通知可能影響效能
6. **測試切面**：切面需要像其他程式碼一樣進行測試
7. **使用註解**：自定義註解使切面更具宣告性
8. **謹慎使用 execution() 與 @annotation()**：了解何時使用每種方式

## 效能考量

1. **編譯時織入**通常是速度最快的選項
2. **載入時織入**在類別載入期間會增加一些開銷
3. **執行時織入**（Spring AOP）開銷最大
4. **複雜的切入點**可能影響效能
5. **環繞通知**比其他通知類型成本更高

為實現生產環境中的最佳效能：
- 盡可能使用編譯時織入
- 保持切入點簡單
- 避免過於寬泛的切入點表達式

## 結論

AspectJ 提供了一種強大的方式來在 Java 和 Spring Boot 應用程式中實作橫切關注點。雖然 Spring AOP 更簡單且足以應對許多情況，但當您需要超越方法攔截時，AspectJ 提供了更多功能。通過遵循本指南中概述的模式和最佳實踐，您可以有效地使用 AspectJ 來建立更模組化、更易維護的應用程式。