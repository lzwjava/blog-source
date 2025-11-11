---
audio: false
generated: true
lang: hant
layout: post
title: 使用AspectJ解決循環依賴問題
translated: true
type: note
---

在你的場景中，循環依賴問題之所以出現，是因為 `BlogConfig`、`BlogCore` 和 `BlogWeb` 相互引用，形成了依賴迴圈。此外，如果 `BlogCore`（或可能是 `BlogWeb`）中的 AspectJ `LoggingAspect` 應用於跨模組的方法（包括依賴於 `BlogCore` 的 `BlogConfig`），可能會加劇此問題。讓我們來分析並提供解決方案，以在保持 AspectJ 功能完整的情況下解決循環依賴問題。

### 問題分析
1. **模組依賴關係**：
   - `BlogCore` 依賴於 `BlogConfig`。
   - `BlogWeb` 同時依賴於 `BlogCore` 和 `BlogConfig`。
   - `BlogConfig` 依賴於 `BlogCore`（這就形成了循環依賴：`BlogCore` ↔ `BlogConfig`）。
   - `BlogWeb` 對這兩個模組的依賴可能會引入循環依賴。

2. **AspectJ LoggingAspect**：
   - `BlogCore`（或 `BlogWeb`）中的 `LoggingAspect` 使用了廣泛的切入點（`execution(* *(..))`），這會應用到應用程式上下文中的所有方法執行，包括 `BlogConfig`、`BlogCore` 和 `BlogWeb` 中的方法。
   - 如果 `LoggingAspect` 位於 `BlogCore` 並織入到 `BlogConfig`，而 `BlogConfig` 又依賴於 `BlogCore`，則 AspectJ 的織入過程可能會在初始化期間使循環依賴問題變得更複雜。

3. **循環依賴的影響**：
   - 在 Maven 或 Gradle 等建置系統中，模組間的循環依賴可能導致編譯或執行階段問題（例如，如果使用 Spring，可能會出現 `BeanCurrentlyInCreationException`，或類別載入問題）。
   - 如果 `BlogConfig` 和 `BlogCore` 中的類別相互依賴且未完全初始化，AspectJ 的編譯時或載入時織入可能會失敗或產生非預期的行為。

### 解決方案
為了解決循環依賴並確保 AspectJ `LoggingAspect` 正常運作，請遵循以下步驟：

#### 1. 打破循環依賴
主要問題是 `BlogCore` ↔ `BlogConfig` 的依賴關係。為解決此問題，請將導致 `BlogConfig` 依賴 `BlogCore` 的共享功能或配置提取到新模組中，或重構依賴關係。

**選項 A：引入新模組（`BlogCommon`）**
- 建立一個新模組 `BlogCommon`，用於存放 `BlogCore` 和 `BlogConfig` 都需要的共享介面、配置或工具。
- 將 `BlogConfig` 所依賴的 `BlogCore` 部分（例如介面、常數或共享服務）移至 `BlogCommon`。
- 更新依賴關係：
  - `BlogConfig` 依賴於 `BlogCommon`。
  - `BlogCore` 依賴於 `BlogCommon` 和 `BlogConfig`。
  - `BlogWeb` 依賴於 `BlogCore` 和 `BlogConfig`。

**依賴結構範例**：
```
BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
```

**實作方式**：
- 在 `BlogCommon` 中定義介面或共享元件。例如：
  ```java
  // BlogCommon 模組
  public interface BlogService {
      void performAction();
  }
  ```
- 在 `BlogCore` 中實作該介面：
  ```java
  // BlogCore 模組
  public class BlogCoreService implements BlogService {
      public void performAction() { /* 邏輯 */ }
  }
  ```
- 在 `BlogConfig` 中使用來自 `BlogCommon` 的介面：
  ```java
  // BlogConfig 模組
  import com.example.blogcommon.BlogService;
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- 在 `BlogWeb` 中按需使用這兩個模組。

這確保了 `BlogConfig` 不再直接依賴 `BlogCore`，從而消除了循環依賴。

**選項 B：使用依賴注入的反轉控制（IoC）**
- 如果使用 Spring 等框架，請重構 `BlogConfig`，使其依賴於 `BlogCore` 中定義的抽象（介面），而不是具體類別。
- 使用依賴注入在執行階段將 `BlogCore` 的實作提供給 `BlogConfig`，避免編譯時的循環依賴。
- 範例：
  ```java
  // BlogCore 模組
  public interface BlogService {
      void performAction();
  }
  @Component
  public class BlogCoreService implements BlogService {
      public void performAction() { /* 邏輯 */ }
  }

  // BlogConfig 模組
  @Configuration
  public class BlogConfiguration {
      private final BlogService blogService;
      public BlogConfiguration(BlogService blogService) {
          this.blogService = blogService;
      }
  }
  ```
- Spring 的 IoC 容器會在執行階段解析依賴關係，從而打破編譯時的循環依賴。

#### 2. 調整 AspectJ 配置
`LoggingAspect` 的廣泛切入點（`execution(* *(..))`）可能會應用到所有模組，包括 `BlogConfig`，這可能會使初始化變複雜。為了使切面更易管理並避免織入問題：

- **縮小切入點範圍**：將切面限制在特定的套件或模組中，避免應用到 `BlogConfig` 或其他基礎設施程式碼。
  ```java
  import org.aspectj.lang.JoinPoint;
  import org.aspectj.lang.annotation.After;
  import org.aspectj.lang.annotation.Aspect;
  import java.util.Arrays;

  @Aspect
  public class LoggingAspect {
      @After("execution(* com.example.blogcore..*(..)) || execution(* com.example.blogweb..*(..))")
      public void logAfter(JoinPoint joinPoint) {
          System.out.println("Method executed: " + joinPoint.getSignature());
          System.out.println("Arguments: " + Arrays.toString(joinPoint.getArgs()));
      }
  }
  ```
  此切入點僅適用於 `BlogCore`（`com.example.blogcore`）和 `BlogWeb`（`com.example.blogweb`）中的方法，排除了 `BlogConfig`。

- **將切面移至獨立模組**：為避免模組初始化期間的織入問題，請將 `LoggingAspect` 置於新模組（例如 `BlogAspects`）中，該模組依賴於 `BlogCore` 和 `BlogWeb`，但不依賴 `BlogConfig`。
  - 依賴結構：
    ```
    BlogCommon ← BlogConfig ← BlogCore ← BlogWeb
                       ↑          ↑
                       └─ BlogAspects ─┘
    ```
  - 更新建置配置（例如 Maven/Gradle），確保 `BlogAspects` 在 `BlogCore` 和 `BlogWeb` 之後織入。

- **使用載入時織入（LTW）**：如果編譯時織入因循環依賴而導致問題，請切換至使用 AspectJ 的載入時織入。在應用程式中配置 LTW（例如透過 Spring 的 `@EnableLoadTimeWeaving` 或 `aop.xml` 檔案），將切面的應用推遲到執行階段類別載入之後。

#### 3. 更新建置配置
確保您的建置工具（Maven、Gradle 等）反映新的模組結構並正確解析依賴關係。

**Maven 範例**：
```xml
<!-- BlogCommon/pom.xml -->
<dependencies>
    <!-- 無依賴 -->
</dependencies>

<!-- BlogConfig/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogCore/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCommon</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogWeb/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogConfig</artifactId>
        <version>1.0</version>
    </dependency>
</dependencies>

<!-- BlogAspects/pom.xml -->
<dependencies>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogCore</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>com.example</groupId>
        <artifactId>BlogWeb</artifactId>
        <version>1.0</version>
    </dependency>
    <dependency>
        <groupId>org.aspectj</groupId>
        <artifactId>aspectjrt</artifactId>
        <version>1.9.7</version>
    </dependency>
</dependencies>
<build>
    <plugins>
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>aspectj-maven-plugin</artifactId>
            <version>1.14.0</version>
            <configuration>
                <complianceLevel>11</complianceLevel>
                <source>11</source>
                <target>11</target>
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
    </plugins>
</build>
```

**Gradle 範例**：
```groovy
// BlogCommon/build.gradle
dependencies {
    // 無依賴
}

// BlogConfig/build.gradle
dependencies {
    implementation project(':BlogCommon')
}

// BlogCore/build.gradle
dependencies {
    implementation project(':BlogCommon')
    implementation project(':BlogConfig')
}

// BlogWeb/build.gradle
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogConfig')
}

// BlogAspects/build.gradle
plugins {
    id 'java'
    id 'aspectj.AspectjGradlePlugin' version '0.2.0'
}
dependencies {
    implementation project(':BlogCore')
    implementation project(':BlogWeb')
    implementation 'org.aspectj:aspectjrt:1.9.7'
}
aspectj {
    version = '1.9.7'
}
```

#### 4. 測試應用程式
- 透過建置和執行應用程式來驗證循環依賴是否已解決。
- 確保 `LoggingAspect` 在 `BlogCore` 和 `BlogWeb` 中記錄方法執行，但不在 `BlogConfig` 中記錄（除非明確需要）。
- 如果使用 Spring，請檢查在上下文初始化期間是否出現 `BeanCurrentlyInCreationException` 或類似錯誤。
- 測試 AspectJ 織入，確認日誌出現在正確的方法中。

#### 5. 額外提示
- **使用依賴分析工具**：使用 Maven 的 `mvn dependency:tree` 或 Gradle 的 `dependencies` 任務來檢測任何殘留的循環依賴。
- **考慮切面的粒度**：如果僅需為特定服務記錄日誌，請進一步細化切入點以針對特定類別或方法（例如 `execution(* com.example.blogcore.service.*.*(..))`）。
- **避免對配置模組使用 AspectJ**：通常，避免將切面應用於配置或基礎設施程式碼（如 `BlogConfig`），以降低複雜性。

### 最終依賴結構
重構後：
```
BlogCommon → BlogConfig → BlogCore → BlogWeb
   ↑                        ↑
   └────── BlogAspects ─────┘
```

### 為何此方案有效
- **打破循環**：將共享依賴移至 `BlogCommon` 或使用 IoC 確保 `BlogConfig` 不依賴 `BlogCore`，從而消除循環依賴。
- **隔離切面**：將 `LoggingAspect` 置於獨立模組（`BlogAspects`）或縮小其切入點範圍，可防止織入問題並使切面邏輯獨立於依賴鏈。
- **建置配置**：正確的建置工具設定可確保模組以正確的順序編譯和織入。

此方法在保持 AspectJ 日誌功能的同時，確保了清晰、可維護的模組結構。如果您有關於設定的更多詳細資訊（例如 Spring 使用情況、導致循環的具體類別），我可以進一步完善解決方案！