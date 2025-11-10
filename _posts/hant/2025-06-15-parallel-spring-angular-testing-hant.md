---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 平行式彈簧角度瀏覽器測試
translated: true
type: note
---

明白了——你需要一個實用的方法來**並行測試**你的 Spring (Java) + Angular 網站，主要在 **Edge 和 Chrome 上進行手動測試**（並在需要時輔以輕量自動化）。以下是一個經過實戰檢驗的工作流程，能避免寬表格問題。

---

# 1) 設定乾淨、可比較的瀏覽器

* **安裝最新穩定版** Chrome 和 Edge。記錄版本號。
* 為每個瀏覽器建立**獨立的乾淨設定檔**以供測試：

  * Chrome：`chrome --user-data-dir=/tmp/chrome-qa --no-first-run`
  * Edge：`msedge --user-data-dir=/tmp/edge-qa --no-first-run`
* 匹配**縮放比例 (100%)**、**設備像素比 (DPR)**、**語言**、**作業系統主題**、**字型包**，並關閉所有擴充功能。
* 將兩個瀏覽器並排固定（如果可能，使用雙螢幕）。使用相同的**視窗大小**（例如 1440×900）。

---

# 2) 準備穩定的後端 + 真實的數據

* 在**預發佈模式**下啟動你的 Spring 後端，並使用確定的種子數據。
* 優先使用**不可變的測試帳戶**和**已知數據集**（例如，使用 Testcontainers 進行數據庫快照，或使用 Flyway/Liquibase 種子腳本）。
* 對於不穩定的依賴項，使用 **WireMock** 樁（HTTP）以使 UI 行為可重複。

---

# 3) 跨瀏覽器鏡像互動（手動，但同步）

要進行真正的並行手動測試，將一個瀏覽器中的點擊、滾動、輸入操作鏡像到另一個瀏覽器：

* 使用 **Browsersync** 作為本地代理來**同步互動**：

  ```bash
  npm i -g browser-sync
  browser-sync start --proxy "http://localhost:4200" --files "dist/**/*" --open "external"
  ```

  在 **Chrome** 和 **Edge** 中打開代理後的 URL；滾動、點擊和表單輸入將會同步鏡像。
  （非常適合檢查佈局差異、懸停/焦點狀態以及快速流程。）

> 如果無法使用代理（由於驗證限制、公司網絡），則打開兩個視窗，並嚴格遵循**步驟列表**（見下文），同時使用分屏錄影。

---

# 4) 跨瀏覽器檢查清單（同時運行）

**並行執行**此清單——在兩個瀏覽器中完成同一步驟後再繼續下一步。

* **引導與字型：** 無樣式內容閃爍 (FOUC)、圖示字型、後備字型。
* **佈局：** Flex/Grid 間距、固定標頭/頁尾、溢出/省略號、RTL/本地化文本換行。
* **表單：** 自動填充、佔位符、驗證訊息、數字/日期輸入、IME/中文輸入、複製/貼上。
* **焦點/鍵盤：** Tab 鍵順序、焦點環可見性、`:focus-visible` 與 `:focus` 的區別、Enter/Esc 行為、快捷鍵。
* **懸停/啟動狀態：** 選單、工具提示、漣漪效果、Angular Material 狀態類別。
* **檔案與下載：** 檔案輸入接受篩選器、拖放、下載提示。
* **驗證/工作階段：** Cookie、SameSite 屬性、跨分頁儲存隔離、工作階段超時和刷新令牌流程。
* **路由：** 深層連結、在嵌套路由上硬重新整理、404 後備頁面。
* **快取：** Service Worker 更新週期、過時資源清除、離線頁面行為。
* **媒體與 API：** getUserMedia/剪貼簿、通知權限。
* **無障礙功能快速檢查：** 地標/角色、顏色對比度（開發人員工具）、僅鍵盤導航。
* **效能初步檢查：** 在**兩個**瀏覽器中使用開發人員工具的 Performance 面板檢查長時間任務，並運行 Lighthouse。

提示：在兩個瀏覽器中都保持**開發人員工具**打開 (F12)，停靠在底部，並比較**控制台**警告（框架、CSP 和棄用訊息）。

---

# 5) Angular 特有的常見差異點

* **變更檢測與非同步操作：** 微任務計時可能在不同瀏覽器中引發競態條件；注意載入指示器和「儲存」按鈕的雙擊問題。
* **Zone.js 錯誤：** 未處理的 Promise 拒絕可能在一個瀏覽器中出現，而在另一個中沒有——檢查控制台。
* **Angular Material 主題：** 驗證深色/淺色主題令牌、高對比度模式以及焦點輪廓（Edge 的焦點渲染通常略有不同）。
* **i18n 管道與日期格式：** 不同 Chromium 變體中 `DatePipe` 和 `Intl` 的區域設定差異。

---

# 6) Spring 後端的注意事項

* **CORS 與重新導向：** 規則相同，但 **Edge 有時在開發階段更早暴露 CORS 預檢請求問題**；請驗證 `OPTIONS` 回應和標頭。
* **Content-Type 與壓縮：** 檢查 `application/json;charset=UTF-8` 與 `application/json` 的區別；驗證 gzip/br 壓縮——不匹配可能導致某個瀏覽器首先顯示「載入失敗」。
* **安全標頭：** CSP、HSTS、X-Frame-Options——更嚴格的政策可能以不同方式阻止內聯腳本/樣式。

---

# 7) 透過薄自動化層使「手動」測試可重複

即使你不想進行完整的 E2E 測試，也請設定一個**簡短、快速**的瀏覽器測試框架，以便 CI 能在每個 PR 上同時運行 Chrome 和 Edge。這樣可以更早發現回歸問題，並減輕手動測試負擔。

### 選項 A：Playwright（我的首選，適用於 Angular 應用）

* 一個測試運行器，啟動 **Chrome Stable** 和 **Microsoft Edge** 頻道，**並行運行**。
* `npm i -D @playwright/test`
* `npx playwright install chromium`
* `playwright.config.ts` 範例：

  ```ts
  import { defineConfig, devices } from '@playwright/test';

  export default defineConfig({
    testDir: './e2e',
    workers: 4, // 並行度
    use: {
      baseURL: 'http://localhost:4200',
      trace: 'retain-on-failure',
    },
    projects: [
      {
        name: 'Chrome Stable',
        use: { ...devices['Desktop Chrome'], channel: 'chrome' },
      },
      {
        name: 'Microsoft Edge',
        use: { ...devices['Desktop Edge'], channel: 'msedge' },
      },
    ],
  });
  ```

  最小化的煙霧測試規格 (`e2e/smoke.spec.ts`)：

  ```ts
  import { test, expect } from '@playwright/test';

  test('home loads and login works', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('Password123!');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page.getByText('Dashboard')).toBeVisible();
  });
  ```

  運行：`npx playwright test`

### 選項 B：Cypress（Chromium 系列，可運行 Chrome 和 Edge）

* 透過 CI 矩陣（或 Cypress Dashboard）實現並行化。
* 在 CI 中運行：

  * `cypress run --browser chrome`
  * `cypress run --browser edge`
* 保持規格簡短（僅煙霧測試）以維持「手動為主」。

### 選項 C：Selenium Grid（如果你已在使用 Selenium）

* Docker 化的 Grid 可**並行運行 chromium/edge 節點**。

  ```yaml
  # docker-compose.yml
  services:
    selenium-hub:
      image: selenium/hub:4
      ports: ["4444:4444"]
    chrome:
      image: selenium/node-chrome:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
    edge:
      image: selenium/node-edge:4
      shm_size: 2gb
      depends_on: [selenium-hub]
      environment: [SE_EVENT_BUS_HOST=selenium-hub]
  ```

  將你的 WebDriver 測試指向 `http://localhost:4444/wd/hub` 並並行運行測試套件。

---

# 8) CI「預設並行」

* 使用**矩陣**任務（Chrome/Edge）並並行運行你的 Playwright/Cypress 煙霧測試。
* 快速失敗以節省時間；為失敗的瀏覽器附加**追蹤記錄/影片**。
* 每晚運行一個稍廣泛的測試集，並在兩個瀏覽器上運行 **Lighthouse** 檢查。

---

# 9) 出現差異時快速排查

* 從每個瀏覽器獲取 **HAR** 檔案，比較回應（狀態碼、標頭、快取）。
* 比較損壞元素的**計算樣式**（開發人員工具 → Styles → Computed）。
* 切換**減少動畫**和**強制色彩**模式以揭示無障礙功能 CSS 問題。
* 清除**網站數據**（Application 面板）並重新測試以排除過時的 Service Worker/快取。

---

# 10) 需保留的最少工件

* 一份**共享檢查清單** (markdown)，記錄你的跨瀏覽器檢查項。
* 一個**版本記錄**：應用程式提交哈希、Chrome/Edge 版本、作業系統、重要標誌。
* 為任何你接受為「暫不修復」的視覺差異附上**螢幕截圖**（相同視窗大小）。

---

如果你需要，我可以為你的 Angular 應用生成一個可直接運行的 **Playwright 骨架**（包含 `npm scripts`、CI 矩陣和兩個煙霧測試規格），或者一個針對你的開發伺服器設定量身定制的 **Browsersync 腳本**。