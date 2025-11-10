---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 實用測試分層指南
translated: true
type: note
---

好問題。一個合理的測試策略主要關乎**風險與回饋速度**。以下是一個實用的方法來決定**在各層級該測試什麼**——不用表格，只有清晰的規則和範例。

---

# 核心原則

* **測試行為，而非實作細節**。優先使用公開 API，而非私有細節。
* **將大多數檢查下推到能捕捉錯誤的最快層級**。
* **僅在風險值得時才使用真實依賴**（資料庫、佇列、瀏覽器）。
* **端到端覆蓋關鍵路徑，但要節制**。UI 測試最脆弱且最慢；留給真正重要的部分。

---

# 各層級該測試什麼（快速經驗法則）

## 1) 單元測試（快速、隔離）

**使用時機：** 純/領域邏輯無需 I/O（資料庫、HTTP、檔案系統）即可測試。

* 業務規則、定價/費用計算、驗證器、映射器、工具程式。
* 服務方法，其中儲存庫/客戶端**被模擬**。
* 目標：大量小測試；在毫秒級內失敗。

**Java/Spring 範例**

```java
@ExtendWith(MockitoExtension.class)
class FeeServiceTest {
  @Mock AccountRepo repo;
  @InjectMocks FeeService svc;

  @Test void vipGetsDiscount() {
    when(repo.tier("u1")).thenReturn("VIP");
    assertEquals(Money.of(90), svc.charge("u1", Money.of(100)));
    verify(repo).tier("u1");
  }
}
```

## 2) 整合 / 組件測試（真實連線，最少模擬）

**使用時機：** 你需要驗證 Spring 連線、序列化、過濾器、資料庫查詢、交易。

* **無網路的 HTTP 層**：`@WebMvcTest`（控制器 + JSON），或 `@SpringBootTest(webEnvironment=RANDOM_PORT)` 用於完整堆疊。
* **資料庫正確性**：使用 **Testcontainers** 執行真實資料庫；檢查 SQL、索引、遷移。
* **訊息傳遞**：使用真實代理容器（Kafka/RabbitMQ）測試消費者/生產者。

**HTTP 切片範例**

```java
@WebMvcTest(controllers = OrderController.class)
class OrderControllerTest {
  @Autowired MockMvc mvc;
  @MockBean OrderService svc;

  @Test void createsOrder() throws Exception {
    when(svc.create(any())).thenReturn(new Order("id1", 100));
    mvc.perform(post("/orders").contentType("application/json")
        .content("{\"amount\":100}"))
      .andExpect(status().isCreated())
      .andExpect(jsonPath("$.id").value("id1"));
  }
}
```

**使用 Testcontainers 的資料庫測試**

```java
@Testcontainers
@SpringBootTest
class RepoIT {
  @Container static PostgreSQLContainer<?> db = new PostgreSQLContainer<>("postgres:16");
  @Autowired OrderRepo repo;

  @Test void persistsAndQueries() {
    var saved = repo.save(new OrderEntity(null, 100));
    assertTrue(repo.findById(saved.getId()).isPresent());
  }
}
```

## 3) API 合約與端到端 API 測試

**使用時機：** 你必須保證**向後相容的合約**或完整系統工作流程。

* **合約測試**（例如，OpenAPI 結構描述驗證或 Pact）可在沒有 UI 的情況下捕捉破壞性變更。
* **端到端 API 流程**：使用真實資料庫啟動應用程式，並透過 HTTP（RestAssured）呼叫它。專注於快樂路徑 + 少數關鍵邊緣案例。

**API 端到端範例**

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
class ApiFlowIT {
  @LocalServerPort int port;
  @Test void happyPath() {
    given().port(port).contentType("application/json")
      .body("{\"amount\":100}")
      .when().post("/orders")
      .then().statusCode(201)
      .body("amount", equalTo(100));
  }
}
```

## 4) UI 端到端測試（瀏覽器）

**使用時機：** 只有**少數**關鍵使用者旅程必須在真實瀏覽器中驗證：

* 認證 + 結帳；資金流動；PII 流程；檔案上傳。
* 保持 **3–10 個關鍵場景**。其他所有情況：在單元/整合/API 層級覆蓋。

**Selenium 還是 Playwright/Cypress？**

* **對於現代的 Angular 應用，優先選擇 Playwright**（或 Cypress）：自動等待、更簡單的選擇器、並行處理、內建追蹤檢視器、跨 Chromium/Firefox/WebKit 的穩定無頭執行。
* **如果你必須在自定義網格中驅動真實供應商瀏覽器**，與**傳統/企業**設定互動，或者你已經擁有成熟的 Selenium 基礎設施，則**使用 Selenium**。它需要更多設定；你需要明確的等待和一個網格來提升速度。

**Playwright (TypeScript) 範例**

```ts
import { test, expect } from '@playwright/test';

test('checkout happy path', async ({ page }) => {
  await page.goto('http://localhost:4200');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.getByLabel('Email').fill('u@example.com');
  await page.getByLabel('Password').fill('secret');
  await page.getByRole('button', { name: 'Login' }).click();

  await page.getByText('Add to cart', { exact: true }).first().click();
  await page.getByRole('button', { name: 'Checkout' }).click();
  await expect(page.getByText('Order confirmed')).toBeVisible();
});
```

**如果你必須使用 Selenium (Java)**

```java
WebDriver d = new ChromeDriver();
d.get("http://localhost:4200");
new WebDriverWait(d, Duration.ofSeconds(10))
  .until(ExpectedConditions.elementToBeClickable(By.id("loginBtn"))).click();
```

---

# 逐層決策（快速流程）

1. **能否在沒有 I/O 的情況下測試？**
   → 是：進行**單元測試**。

2. **它是否依賴於框架連線/序列化或資料庫查詢？**
   → 是：進行**整合/組件**測試（Spring 切片，Testcontainers）。

3. **這是一個跨服務/公開 API 合約嗎？**
   → 是：進行**合約測試**（結構描述/Pact） + 幾個 **API 端到端**流程。

4. **其價值是否僅在 UI 中可見或屬於關鍵 UX？**
   → 是：進行 **UI 端到端**測試，但僅限核心旅程。

---

# 合理的比例與預算

* 目標大致為 **70–80% 單元**，**15–25% 整合/API**，**5–10% UI 端到端**。
* 保持每次提交的 CI 快速：單元測試 <2–3 分鐘，整合測試並行化；在 PR 上執行**小型 UI 煙霧測試**，**更廣泛的 UI 套件每晚執行**。

---

# 優先順序（基於風險的檢查清單）

* 資金流動、認證、權限、合規性 → **API 與一個 UI 快樂路徑**。
* 複雜計算、定價規則 → **單元**（多種案例） + 幾個帶有真實資料庫四捨五入/時區的**整合**測試。
* 持久化邏輯、遷移、複雜聯結 → **使用 Testcontainers 的儲存庫測試**。
* 跨團隊合約 → **合約測試**在 CI 中阻止破壞性變更。
* 無障礙功能、國際化 → **組件測試**用於 ARIA/地區設定 + 在關鍵頁面上**定期 UI 掃描**（axe）。

---

# CI 流水線形狀（實用主義）

* **每次推送時：** 單元 + 切片測試；少量 API 端到端；極少 UI 煙霧測試（1–3）。
* **每晚：** 完整 API 端到端、更廣泛的 UI 套件、效能煙霧測試（k6）、基本安全掃描（ZAP）。
* **快速隔離不穩定的測試**；修復或刪除——不要忽略。

---

# 測試資料與不穩定性提示

* 使用**工廠方法/建造者模式**；避免共享的可變固定裝置。
* **使用 SQL/資料初始化 Testcontainers**；保持測試**冪等**。
* 在 UI 中，優先使用**角色/標籤選擇器**而非 CSS/XPath；避免睡眠，使用與使用者可見條件掛鉤的等待。
* **記錄追蹤**（Playwright 追蹤、Selenium 日誌）以除錯 CI 失敗。

---

# 簡而言之的經驗法則

* 如果一個錯誤本可以由**更快**的層級捕捉到，**就將測試下移**。
* 只保留**少數、關鍵的** UI 旅程。
* 使用 **Testcontainers** 使整合測試有意義。
* 除非 Selenium 是硬性要求，否則優先選擇 **Playwright**。

如果你願意，告訴我你的**前 3–5 個業務關鍵流程**，我會為每個層級草擬確切的測試清單（包含工具選擇和 CI 門控）。