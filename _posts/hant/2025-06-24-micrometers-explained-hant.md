---
audio: false
generated: true
lang: hant
layout: post
title: 微米計使用指南：工具與可觀測性
translated: true
type: note
---

這份綜合指南涵蓋兩個截然不同的主題：**千分尺（測量工具）** 以及 **Micrometer（適用於 Java 應用程式，特別是 Spring Boot 的可觀測性外觀），著重於追蹤解決方案。**

讓我們逐一分解：

-----

## 第一部分：關於千分尺（測量工具）的綜合指南

千分尺，常稱為螺旋測微器，是一種精密測量儀器，用於獲取極高精度的小距離測量值，通常範圍在千分之一英寸或百分之一毫米。它廣泛應用於工程、機械加工、製造和科學領域，這些領域的精確尺寸至關重要。

### 1. 什麼是千分尺？

千分尺的核心是利用精密加工的螺絲機構，將旋轉運動轉換為線性移動。這允許透過將物件夾在固定的砧座和可移動的主軸之間，進行微調並精確讀取物件的尺寸。

### 2. 千分尺的關鍵組件：

  * **框架：** C 形主體，用於固定所有其他組件。它提供穩定性，需要小心處理以避免熱膨脹誤差。
  * **砧座：** 固定的測量面，物件緊靠此面放置。
  * **主軸：** 可移動的測量面，當旋轉套筒時，它會朝向或遠離砧座移動。
  * **套筒（或筒身）：** 千分尺的固定部分，容納主線性刻度，顯示整數和半增量（例如，以英寸或毫米為單位）。
  * **套筒：** 旋轉部件，用於移動主軸，並具有精細刻度以便進行更精確的讀數。
  * **棘輪停止器：** 位於套筒末端，透過在施加正確力道時滑動來確保一致的測量壓力，防止過度鎖緊和工件變形。
  * **鎖定螺母（或鎖定桿）：** 用於在取得測量值後鎖定主軸位置，防止意外移動並保留讀數。

### 3. 千分尺的類型：

千分尺有多種類型，每種專為特定的測量任務設計：

  * **外徑千分尺（外部千分尺）：** 最常見的類型，用於測量外部尺寸，例如軸的直徑或板的厚度。
  * **內徑千分尺（內部千分尺）：** 用於測量內部尺寸，例如孔或內孔的直徑。它們通常有不同的設計，例如管式或爪式千分尺。
  * **深度千分尺：** 用於測量孔、槽或階梯的深度。
  * **螺紋千分尺：** 設計用於測量螺紋的節圓直徑。
  * **球面千分尺：** 具有球面砧座/主軸，用於測量曲面或特定特徵（如管壁）的厚度。
  * **盤式千分尺：** 具有平坦的圓盤形測量面，用於測量薄材料、紙張或齒輪齒。
  * **數位千分尺：** 具有電子顯示屏，可直接讀取數位讀數，消除視差並使讀數更容易。
  * **類比千分尺：** 需要手動讀取套筒和套筒上的刻度。
  * **游標千分尺：** 包含一個額外的游標刻度，以實現更高的精度，允許讀取超出套筒主刻度的讀數。

### 4. 如何讀取千分尺（類比/英制範例）：

雖然具體讀數在英制（英寸）和公制（毫米）以及類比/數位之間有所不同，但類比千分尺的一般原則是：

1.  **讀取套筒刻度（主刻度）：**
      * **整英寸：** 注意可見的最大整英寸標記。
      * **十分之一英寸 (0.100")：** 套筒上的每個編號線代表 0.100 英寸。
      * **二十五千分之一英寸 (0.025")：** 十分之一標記之間的每個未編號線代表 0.025 英寸。
2.  **讀取套筒刻度：**
      * 套筒有 25 個刻度，每個刻度代表 0.001 英寸。
      * 讀取與套筒上索引線對齊的套筒上的線。
3.  **合併讀數：** 將套筒（整英寸、十分之一和二十五千分之一）和套筒（千分之一）的值相加，得到最終測量值。

**範例（英制）：**

  * 套筒：
      * 假設您看到 "1"（代表 1.000"）
      * 然後在 "1" 之後有 3 條線 (3 x 0.100" = 0.300")
      * 並且在主線下方有 2 條線 (2 x 0.025" = 0.050")
      * 套筒總計：1.000 + 0.300 + 0.050 = 1.350"
  * 套筒：
      * 套筒上的第 15 個刻度與索引線對齊 (0.015")
  * **總讀數：** 1.350" + 0.015" = **1.365"**

### 5. 正確使用和最佳實踐：

  * **清潔度：** 始終確保測量面（砧座和主軸）清潔，沒有灰塵、油污或碎屑。
  * **歸零：** 使用前，務必將千分尺"歸零"。使用棘輪停止器輕輕關閉測量面，直到它們接觸。讀數應為 0.000（或起始範圍，例如 25-50mm）。如果不是，請調整千分尺的零點誤差。數位千分尺通常有一個重設按鈕。
  * **溫度：** 握住千分尺的絕緣框架或戴手套，因為體熱會導致熱膨脹並影響精度，尤其是較大的千分尺。讓工具和物件都達到室溫。
  * **一致的壓力：** 始終使用棘輪停止器施加一致且適當的測量壓力。過度鎖緊會使物件或千分尺變形。
  * **物件定位：** 將物件垂直放置在砧座和主軸之間，以避免讀數偏差。
  * **多次測量：** 對於關鍵尺寸，請在物件的不同點進行多次測量，以考慮變異。
  * **儲存：** 將千分尺存放在保護盒中，以防止損壞。
  * **校準：** 定期對照已知標準（例如，量塊）檢查和校準千分尺，以確保其準確性。

-----

## 第二部分：Micrometer 作為 Spring Java 專案的追蹤解決方案

在 Spring Java 專案的背景下，"Micrometer" 指的是一個**應用程式可觀測性外觀**，它提供了一個與供應商無關的 API，用於檢測基於 JVM 的應用程式。它允許您收集和匯出各種遙測數據，包括指標、日誌記錄和**分散式追蹤**。

Micrometer Tracing 是 Spring Cloud Sleuth 的後繼者，旨在透過跨多個服務追蹤請求來提供對複雜分散式系統的洞察。

### 1. 什麼是分散式追蹤？

在微服務架構中，單一使用者請求通常會遍歷多個服務。分散式追蹤允許您：

  * **追蹤流程：** 查看請求在系統中經過的完整路徑。
  * **識別瓶頸：** 準確找出哪個服務或操作導致延遲。
  * **理解依賴關係：** 視覺化不同服務之間的互動。
  * **簡化除錯：** 將日誌與特定請求關聯，使故障排除更加容易。

分散式追蹤由**跨度**組成。一個**跨度**代表追蹤中的單一操作或工作單元（例如，對服務的 HTTP 請求、資料庫查詢、方法執行）。跨度具有唯一 ID、開始和結束時間，並且可以包含標籤（鍵值對）和事件以獲取額外的元數據。跨度按層次結構組織，具有父子關係，形成一個追蹤。

### 2. Spring Boot 3.x+ 中的 Micrometer Tracing

Spring Boot 3.x+ 與 Micrometer 的 Observation API 和 Micrometer Tracing 深度整合，使得實作分散式追蹤變得更加容易。

#### 2.1. 核心概念：

  * **Observation API：** Micrometer 的統一 API，用於檢測您的程式碼，能夠從單一檢測點產生指標、追蹤和日誌。
  * **Micrometer Tracing：** 一個外觀，封裝了流行的追蹤器庫，如 OpenTelemetry 和 OpenZipkin Brave。它處理跨度的生命週期、上下文傳播和向追蹤後端的報告。
  * **追蹤器橋接：** Micrometer Tracing 提供"橋接"以將其 API 連接到特定的追蹤實作（例如，用於 OpenTelemetry 的 `micrometer-tracing-bridge-otel`，用於 OpenZipkin Brave 的 `micrometer-tracing-bridge-brave`）。
  * **報告器/匯出器：** 這些組件將收集的追蹤數據發送到追蹤後端（例如，Zipkin、Jaeger、Grafana Tempo）。

#### 2.2. 在 Spring Boot Java 專案中設定 Micrometer Tracing：

以下是逐步指南：

**步驟 1：新增依賴項**

您需要 `spring-boot-starter-actuator` 用於可觀測性功能、一個 Micrometer Tracing 橋接器，以及用於您選擇的追蹤後端的報告器/匯出器。

**使用 OpenTelemetry 和 Zipkin 的範例（常見選擇）：**

在您的 `pom.xml` (Maven) 中：

```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-actuator</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-observation</artifactId>
    </dependency>

    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-tracing-bridge-otel</artifactId>
    </dependency>

    <dependency>
        <groupId>io.opentelemetry</groupId>
        <artifactId>opentelemetry-exporter-zipkin</artifactId>
    </dependency>

    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
</dependencies>
```

**步驟 2：設定追蹤屬性**

在 `application.properties` 或 `application.yml` 中，您可以設定追蹤行為。

```properties
# 啟用追蹤（通常預設為 true，當有 actuator 和 tracing 依賴項時）
management.tracing.enabled=true

# 設定取樣概率 (1.0 = 100% 的請求被追蹤)
# 預設通常為 0.1 (10%)，開發/測試時設為 1.0
management.tracing.sampling.probability=1.0

# 設定 Zipkin 基礎 URL（如果使用 Zipkin）
spring.zipkin.base-url=http://localhost:9411
```

**步驟 3：執行追蹤後端（例如，Zipkin）**

您需要一個追蹤伺服器來收集和視覺化您的追蹤。Zipkin 是本地開發的熱門選擇。

您可以透過 Docker 執行 Zipkin：

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

執行後，您可以在 `http://localhost:9411` 存取 Zipkin UI。

**步驟 4：自動檢測（Spring Boot 的魔力！）**

對於 Spring Boot 中的許多常見組件（如 `RestController` 端點、`RestTemplate`、`WebClient`、`JdbcTemplate`、Kafka 監聽器/生產者等），Micrometer Tracing 提供**自動檢測**。這意味著您通常不需要編寫任何明確的追蹤程式碼，基本的請求追蹤即可工作。

Spring Boot 確保：

  * 傳入的 HTTP 請求會自動建立新的追蹤，或者如果存在追蹤標頭，則繼續現有的追蹤。
  * 使用自動設定的 `RestTemplateBuilder`、`RestClient.Builder` 或 `WebClient.Builder` 發出的傳出請求會將追蹤上下文傳播到下游服務。
  * 日誌語句自動包含 `traceId` 和 `spanId`（如果您設定了日誌模式）。

**日誌模式範例（在 `application.properties` 中）：**

```properties
logging.pattern.level=%5p [${spring.application.name:},%X{traceId:-},%X{spanId:-}] %c{1.}:%M:%L - %m%n
```

此模式會將 `traceId` 和 `spanId` 注入到您的日誌行中，從而輕鬆將日誌與特定追蹤關聯起來。

**步驟 5：手動檢測（用於自訂邏輯）**

雖然自動檢測涵蓋了許多方面，但您通常會希望追蹤應用程式內的特定業務邏輯或關鍵操作。您可以使用以下方式實現：

  * **`@Observed` 註解（推薦用於 Spring Boot 3.x+）：**
    此註解是 Micrometer Observation API 的一部分，是建立觀測（可以產生指標和追蹤）的首選方法。

    ```java
    import io.micrometer.observation.annotation.Observed;
    import org.springframework.stereotype.Service;

    @Service
    public class MyService {

        @Observed(name = "myService.processData", contextualName = "processing-data")
        public String processData(String input) {
            // ... 您的業務邏輯 ...
            System.out.println("Processing data: " + input);
            return "Processed: " + input;
        }
    }
    ```

    `name` 屬性定義了觀測的名稱（該名稱將成為指標名稱和追蹤跨度名稱）。`contextualName` 為追蹤工具中的跨度提供了更易讀的名稱。

  * **程式化 API（用於更多控制）：**
    您可以直接使用 Spring Boot 提供的 `ObservationRegistry` 和 `Tracer` bean。

    ```java
    import io.micrometer.observation.Observation;
    import io.micrometer.observation.ObservationRegistry;
    import org.springframework.stereotype.Service;

    @Service
    public class AnotherService {

        private final ObservationRegistry observationRegistry;

        public AnotherService(ObservationRegistry observationRegistry) {
            this.observationRegistry = observationRegistry;
        }

        public String performComplexOperation(String id) {
            return Observation.createNotStarted("complex.operation", observationRegistry)
                    .lowCardinalityKeyValue("operation.id", id) // 新增一個標籤
                    .observe(() -> {
                        // ... 複雜的邏輯在這裡 ...
                        try {
                            Thread.sleep(100); // 模擬工作
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                        }
                        return "Completed complex operation for " + id;
                    });
        }
    }
    ```

    在這裡，`observe()` 包裝了程式碼塊，而 `lowCardinalityKeyValue` 向跨度新增了一個標籤。

### 3. 微服務中的分散式追蹤：

當您擁有多個 Spring Boot 服務時，Micrometer Tracing 會為 `RestTemplate`、`WebClient` 和其他已檢測的客戶端自動促進上下文傳播。這意味著 `traceId` 和 `spanId` 會在服務之間透過 HTTP 標頭傳遞（例如，用於 W3C Trace Context 的 `traceparent` 標頭）。

當請求進入下游服務時，Micrometer Tracing 會檢測到這些標頭並繼續現有的追蹤，建立新的跨度，這些跨度是呼叫服務的父跨度的子項。這形成了完整的端到端追蹤。

### 4. 視覺化追蹤：

一旦您的應用程式經過檢測並將追蹤發送到後端（如 Zipkin、Jaeger、Lightstep 等），您可以：

1.  **存取 UI：** 前往追蹤後端的 Web UI（例如，Zipkin 的 `http://localhost:9411`）。
2.  **尋找追蹤：** 使用篩選器（服務名稱、跨度名稱、追蹤 ID）來尋找特定的追蹤。
3.  **分析追蹤詳細資訊：** 點擊追蹤以查看其時間軸、個別跨度、它們的持續時間、標籤和事件。
4.  **依賴關係圖：** 大多數追蹤後端可以根據收集的追蹤視覺化服務依賴關係。

### 5. Micrometer Tracing 的最佳實踐：

  * **為您的跨度命名有意義：** 為您的跨度使用清晰、簡潔且低基數的名稱（例如，"userService.getUser"、"productService.updateStock"）。避免在跨度名稱中包含高度動態的數據。
  * **使用標籤獲取詳細資訊（高基數數據）：** 不要將動態數據放在跨度名稱中，而是使用標籤（鍵值對）來獲取額外的上下文。例如，`userId`、`orderId`、`customerType`。請注意**高基數**標籤，因為它們會顯著增加追蹤後端的儲存成本和查詢時間。請謹慎使用它們。
  * **保持跨度細粒度但不過度：** 為重要的操作建立跨度，但避免建立太多微小的跨度，因為這會增加開銷。旨在取得平衡，提供足夠的可見性而不會使系統不堪重負。
  * **傳播上下文：** 確保追蹤上下文在服務邊界之間正確傳播。Spring Boot 的自動配置處理了常見情境，但在使用自訂客戶端或非同步操作時要注意。
  * **取樣：** 對於高流量的生產環境，請考慮使用取樣策略來減少發送到後端的追蹤數據量。Spring Boot 允許配置 `management.tracing.sampling.probability`。
  * **關聯日誌：** 利用注入到日誌中的 `traceId` 和 `spanId`，以便更輕鬆地除錯並將應用程式行為與特定請求關聯起來。
  * **監控您的追蹤後端：** 確保您的追蹤後端（例如，Zipkin 伺服器）擁有足夠的資源來處理傳入的追蹤量。
  * **與其他可觀測性工具整合：** 追蹤是可觀測性的一部分。將其與指標（同樣透過 Micrometer）和結構化日誌記錄結合，以全面了解應用程式的健康狀況和效能。

透過遵循這些指南，您可以有效地利用 Micrometer Tracing 來深入了解您的 Spring Boot 應用程式，特別是在分散式環境中。