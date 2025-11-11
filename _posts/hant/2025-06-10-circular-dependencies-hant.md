---
audio: false
generated: true
lang: hant
layout: post
title: Spring 中的循環依賴
translated: true
type: note
---

Spring 或 Spring Boot 中的循環依賴問題發生於兩個或多個 Bean 在初始化過程中直接或間接相互依賴時。這會形成一個循環鏈，導致 Spring 的依賴注入機制無法解析依賴關係——因為每個 Bean 都要求對方必須先完成初始化。此問題通常出現在 Spring 應用上下文創建 Bean 的過程中，並會引發 `BeanCurrentlyInCreationException`。

### 循環依賴的成因
Spring 在依賴注入容器中管理 Bean，並根據依賴關係按特定順序創建 Bean。當 Bean 以循環方式相互引用時（例如 Bean A 依賴 Bean B，而 Bean B 又依賴 Bean A），Spring 會在初始化過程中陷入無限循環而無法實例化它們。這種情況在具有緊密耦合元件的複雜應用中尤其常見。

以下情境更容易觸發此問題：
1. **建構函式注入**：當通過建構函式裝配 Bean 時，Spring 必須在實例化時解析依賴關係，若 Bean 相互引用則會引發循環問題
2. **字段或 Setter 注入配合立即初始化**：若 Bean 採用立即初始化（單例 Bean 的默認行為），Spring 會立即嘗試解析依賴關係，從而暴露循環依賴
3. **配置錯誤或過度複雜的 Bean 關聯**：不良設計或關注點分離不足可能導致意外循環
4. **使用 `@Autowired` 或 `@Component` 等註解**：在緊密耦合的元件中使用自動依賴注入可能無意間形成循環

### 循環依賴常見範例

#### 範例 1：建構函式注入循環
```java
@Component
public class BeanA {
    private final BeanB beanB;

    @Autowired
    public BeanA(BeanB beanB) {
        this.beanB = beanB;
    }
}

@Component
public class BeanB {
    private final BeanA beanA;

    @Autowired
    public BeanB(BeanA beanA) {
        this.beanA = beanA;
    }
}
```
**問題**：`BeanA` 需要在其建構函式中注入 `BeanB`，而 `BeanB` 又需要在其建構函式中注入 `BeanA`。由於每個 Bean 都要求對方先完成初始化，Spring 無法創建任一 Bean。

**錯誤**：`BeanCurrentlyInCreationException: Error creating bean with name 'beanA': Requested bean is currently in creation: Is there an unresolvable circular reference?`

#### 範例 2：字段注入循環
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanA beanA;
}
```
**問題**：`BeanA` 和 `BeanB` 都通過字段注入相互依賴。即使字段注入比建構函式注入更靈活，若兩者均為單例 Bean（默認作用域），Spring 在 Bean 初始化過程中仍會檢測到循環。

#### 範例 3：間接循環依賴
```java
@Component
public class BeanA {
    @Autowired
    private BeanB beanB;
}

@Component
public class BeanB {
    @Autowired
    private BeanC beanC;
}

@Component
public class BeanC {
    @Autowired
    private BeanA beanA;
}
```
**問題**：`BeanA` 依賴 `BeanB`，`BeanB` 依賴 `BeanC`，而 `BeanC` 又依賴 `BeanA`，形成循環鏈。這種間接依賴較難察覺，但會導致相同問題。

#### 範例 4：配置類循環引用
```java
@Configuration
public class ConfigA {
    @Autowired
    private ConfigB configB;

    @Bean
    public ServiceA serviceA() {
        return new ServiceA(configB);
    }
}

@Configuration
public class ConfigB {
    @Autowired
    private ConfigA configA;

    @Bean
    public ServiceB serviceB() {
        return new ServiceB(configA);
    }
}
```
**問題**：配置類 `ConfigA` 和 `ConfigB` 相互依賴，當 Spring 嘗試初始化這些類中定義的 Bean 時會形成循環。

### Spring Boot 中的常見成因
- **自動配置**：Spring Boot 的自動配置有時會引入導致循環的依賴，特別是在自定義 Bean 與自動配置的 Bean 互動時
- **元件掃描**：過度使用 `@ComponentScan` 或配置錯誤的套件路徑可能掃描到非預期的 Bean，引發循環依賴
- **緊密耦合設計**：業務邏輯中緊密耦合的服務層、儲存庫或控制器可能無意間形成循環
- **原型作用域誤用**：雖然原型作用域的 Bean 有時可避免循環依賴，但與單例 Bean 在循環鏈中混合使用仍可能引發問題

### 解決循環依賴的方法
1. **使用 `@Lazy` 註解**：
   - 在其中一个依賴項添加 `@Lazy` 註解，延遲其實例化直到實際需要時
   ```java
   @Component
   public class BeanA {
       @Autowired
       @Lazy
       private BeanB beanB;
   }
   ```
   通過允許 `BeanA` 在 `BeanB` 解析前部分初始化來打破循環

2. **改用 Setter 或字段注入**：
   - 對其中一個 Bean 使用 Setter 或字段注入替代建構函式注入，讓 Spring 先初始化 Bean 再注入依賴
   ```java
   @Component
   public class BeanA {
       private BeanB beanB;

       @Autowired
       public void setBeanB(BeanB beanB) {
           this.beanB = beanB;
       }
   }
   ```

3. **重構程式碼打破循環**：
   - 引入介面或中間元件來解耦 Bean
   - 範例：將共同依賴提取至第三個 Bean，或使用服務層中介互動
   ```java
   public interface Service {
       void performAction();
   }

   @Component
   public class BeanA implements Service {
       @Autowired
       private BeanB beanB;

       public void performAction() {
           // 業務邏輯
       }
   }

   @Component
   public class BeanB {
       @Autowired
       private Service service; // 依賴介面而非直接依賴 BeanA
   }
   ```

4. **使用 `@DependsOn` 註解**：
   - 在特定情況下顯式控制 Bean 初始化順序以避免循環
   ```java
   @Component
   @DependsOn("beanB")
   public class BeanA {
       @Autowired
       private BeanB beanB;
   }
   ```

5. **啟用 `@EnableAspectJAutoProxy` 代理**：
   - 確保 Spring 使用代理（CGLIB 或 JDK 動態代理）處理依賴，通過注入代理而非實際 Bean 來解決部分循環問題

6. **重新評估設計**：
   - 循環依賴通常意味著設計缺陷。考慮遵循單一職責原則或依賴反轉原則進行重構

### 偵錯循環依賴技巧
- **檢查堆疊追蹤**：`BeanCurrentlyInCreationException` 的堆疊追蹤會顯示參與循環的 Bean
- **啟用偵錯日誌**：設置 `spring.main.lazy-initialization=true` 或為 `org.springframework` 啟用偵錯日誌以查看 Bean 創建詳情
- **使用工具**：Spring Boot Actuator 或 IDE 外掛（如 Spring Tools Suite）可視化 Bean 依賴關係

### 預防循環依賴
- **遵循最佳實踐**：使用介面或抽象類等依賴注入模式減少緊密耦合
- **模組化程式碼**：將大型應用拆分為鬆散耦合的小型模組
- **早期測試**：執行整合測試在開發階段捕捉循環依賴
- **限制元件掃描範圍**：精確設定 `@ComponentScan` 避免掃描非必要 Bean

### 較少出現循環依賴的情境
- **原型作用域**：按需創建的原型作用域 Bean 可降低循環發生機率（但無法完全避免）
- **延遲初始化**：啟用全域延遲初始化（`spring.main.lazy-initialization=true`）可推遲 Bean 創建，但可能僅是掩蓋問題

### 總結
Spring/Spring Boot 中的循環依賴源於 Bean 間的緊密耦合，常因建構函式注入或複雜配置而加劇。常見解決方案包括使用 `@Lazy`、改用 Setter/字段注入或重構打破循環鏈。透過理解根本成因並應用最佳實踐，即可有效預防或解決這類問題。若遇到具體的循環依賴情況，歡迎分享相關程式碼或錯誤詳情，我將協助進一步分析！