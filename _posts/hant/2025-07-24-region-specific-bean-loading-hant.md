---
audio: false
generated: true
lang: hant
layout: post
title: 動態區域特定Bean
translated: true
type: note
---

### 理解需求

聽起來您正在開發一個需要支援多個區域（或「國籍」）的 Spring Boot/Java Spring 應用程式，例如新加坡 (SG)、香港 (HK) 和台灣 (TW)。您希望使用 `@Autowired` 和 Bean 管理等功能，動態載入或注入不同的 Bean，特別是針對 `CoreController` 類別。

這是**多租戶**或**區域特定配置**的常見場景，其中行為（例如服務、配置或控制器）因區域而異。在 Spring 中，您無法在運行時輕鬆切換整個控制器類別，但您可以：

1. 使用 **Spring Profiles** 進行環境特定的 Bean 載入（例如，每個區域的獨立部署或啟動）。這是編譯時或啟動時的方法。
2. 使用**運行時選擇**與策略模式，透過注入多個 Bean（例如透過 Map），並根據請求參數、標頭或上下文（例如用戶的區域）選擇正確的 Bean。

由於您提到「多國籍開發」以及 SG/HK/TW 等範例，我假設這需要在單一應用程式實例中處理多個區域（運行時切換）。如果是每個區域獨立部署，則使用 Profiles 更簡單。

我將透過程式碼範例解釋這兩種方法。我們假設 `CoreController` 依賴於一個區域特定的服務（例如 `CoreService` 介面，並為每個區域提供實作）。這樣，控制器保持不變，但其行為透過注入的 Bean 改變。

### 方法 1：使用 Spring Profiles 進行區域特定 Bean 載入（啟動時）

如果您為每個區域部署獨立的實例（例如透過環境變數或應用程式屬性），這種方法非常理想。Bean 根據啟動的 Profile 條件式載入。

#### 步驟 1：定義介面與實作
為區域特定邏輯建立介面：

```java
public interface CoreService {
    String getRegionMessage();
}
```

每個區域的實作：

```java
// SgCoreService.java
@Service
@Profile("sg")  // 僅在 'sg' Profile 啟動時載入此 Bean
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service
@Profile("hk")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service
@Profile("tw")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### 步驟 2：在 CoreController 中自動裝配
```java
@RestController
public class CoreController {
    private final CoreService coreService;

    @Autowired
    public CoreController(CoreService coreService) {
        this.coreService = coreService;
    }

    @GetMapping("/message")
    public String getMessage() {
        return coreService.getRegionMessage();
    }
}
```

#### 步驟 3：啟動 Profiles
- 在 `application.properties` 或透過命令列：
  - 使用 `--spring.profiles.active=sg` 執行以載入新加坡 Bean。
  - 這確保僅建立和自動裝配 `SgCoreService` Bean。
- 對於 Profiles 以外的自訂條件，使用 `@ConditionalOnProperty`（例如 `@ConditionalOnProperty(name = "app.region", havingValue = "sg")`）。

這種方法簡單，但需要為每個區域重啟或使用獨立應用程式。不適合在單一運行時實例中處理所有區域。

### 方法 2：使用 @Autowired Map 進行運行時 Bean 選擇（策略模式）

對於單一應用程式動態處理多個區域（例如基於 HTTP 請求標頭如 `X-Region: sg`），使用 Bean 的 Map。Spring 可以將所有實作自動裝配到 Map<String, CoreService> 中，其中鍵是 Bean 的名稱。

#### 步驟 1：定義介面與實作
與上述相同，但無需 `@Profile`：

```java
public interface CoreService {
    String getRegionMessage();
}

// SgCoreService.java
@Service("sgCoreService")  // 明確的 Bean 名稱用於 Map 鍵
public class SgCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Singapore!";
    }
}

// HkCoreService.java
@Service("hkCoreService")
public class HkCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Hong Kong!";
    }
}

// TwCoreService.java
@Service("twCoreService")
public class TwCoreService implements CoreService {
    @Override
    public String getRegionMessage() {
        return "Welcome from Taiwan!";
    }
}
```

#### 步驟 2：在 CoreController 中自動裝配 Map
```java
@RestController
public class CoreController {
    private final Map<String, CoreService> coreServices;

    @Autowired  // Spring 自動填入所有 CoreService Bean，以 Bean 名稱作為鍵
    public CoreController(Map<String, CoreService> coreServices) {
        this.coreServices = coreServices;
    }

    @GetMapping("/message")
    public String getMessage(@RequestHeader("X-Region") String region) {  // 或使用 @RequestParam 如果是查詢參數
        CoreService service = coreServices.get(region.toLowerCase() + "CoreService");
        if (service == null) {
            throw new IllegalArgumentException("Unsupported region: " + region);
        }
        return service.getRegionMessage();
    }
}
```

- 此處，Map 上的 `@Autowired` 會自動注入所有 `CoreService` 實作。
- Bean 名稱必須符合您的鍵邏輯（例如 "sgCoreService"）。
- 對於選擇：使用請求標頭/參數來決定區域。這使得每個請求都是動態的。

#### 可選：使用 @Qualifier 進行特定注入
如果您想手動注入特定 Bean：

```java
@RestController
public class CoreController {
    @Autowired
    @Qualifier("sgCoreService")  // 僅注入 SG Bean
    private CoreService sgCoreService;

    // ... 其他類似
}
```
但這不是動態的；對於運行時切換，請使用 Map。

#### 步驟 3：配置與最佳實踐
- 在您的 Spring Boot 主類別中：`@SpringBootApplication` 已足夠；Spring 會掃描 `@Service` Bean。
- 處理預設值：如果沒有區域匹配，添加後備服務。
- 對於更複雜的條件，在 Bean 上使用 `@ConditionalOnExpression` 或自訂 `@Conditional` 註解。
- 執行緒安全：由於控制器預設是單例，只要服務是無狀態的，Map 就是安全的。
- 測試：使用 `@SpringBootTest` 與模擬請求來測試不同區域。

### 選擇哪種方法？
- 使用 **Profiles** 如果區域是透過部署/環境分開的（例如，SG/HK/TW 有不同的伺服器）。
- 使用 **Map/策略** 對於在運行時處理所有區域的統一應用程式（對微服務更靈活）。

如果這不完全符合您的設定（例如，如果 `CoreController` 本身需要因區域而異），您可以使用多個控制器配合 `@RequestMapping` 條件，或使用工廠動態建立控制器——但這較少見且更複雜。

如果您提供更多細節（例如區域是如何決定的），我可以進一步完善！