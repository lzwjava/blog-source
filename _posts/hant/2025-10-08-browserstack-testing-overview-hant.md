---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: BrowserStack 測試平台概覽
translated: true
type: note
---

BrowserStack 是一個領先的雲端軟體測試平台，讓開發人員、QA 團隊和測試人員能夠在數千種真實瀏覽器、作業系統和裝置上驗證網站及流動應用程式。該平台於 2011 年推出，透過提供即時存取超過 3,500 種瀏覽器與裝置組合（包括最新版本的 Chrome、Firefox、Safari、Edge 以及 iOS 和 Android 流動環境），消除了維護實體硬件實驗室的需求。它特別在跨瀏覽器兼容性測試、自動化腳本編寫和手動互動式工作階段方面備受重視，同時支援網頁和原生/混合應用程式。

## 為何選擇 BrowserStack？

在不同環境中進行測試對於確保應用程式表現一致至關重要，但這需要大量資源。BrowserStack 透過以下方式解決此問題：
- 提供真實裝置和瀏覽器（非模擬器）以獲得準確結果。
- 啟用並行測試以加速測試週期。
- 與熱門工具整合，如 Selenium、Appium、Cypress 和 CI/CD 管道（例如 Jenkins、GitHub Actions）。
- 提供 AI 驅動功能，如自我修復測試和故障分析，以減少維護工作。
- 支援團隊進行協作式除錯、錯誤報告和分析。

全球超過 50,000 個團隊使用該平台，包括《財富》500 強公司，以實現更快的發布速度和更高的覆蓋率，而無需處理設置麻煩。

## 註冊與入門指南

1. **創建帳戶**：訪問 BrowserStack 網站，使用電郵、Google 或 GitHub 註冊。提供免費試用，包括有限制的即時測試和自動化功能存取。
2. **儀表板存取**：登入後查看用戶名稱和存取密鑰（位於 Automate > Account Settings 下）。這些對於腳本編寫至關重要。
3. **探索產品**：從頂部選單中選擇 Live（手動測試）、Automate（腳本化網頁/流動測試）、App Live/Automate（應用程式專注）、Percy（視覺測試）等。
4. **本地測試設置**：對於私有應用程式，安裝 BrowserStack Local 工具（適用於 Windows/Mac/Linux 的二進制檔案），以安全地隧道傳輸本地主機流量。
5. **團隊設置**：透過電郵邀請用戶，並配置角色以實現協作存取。

除了本地代理程式外，無需安裝任何軟體——測試在雲端運行。

## 即時測試（手動互動式測試）

即時測試讓您能夠在遠端裝置上即時與應用程式互動，非常適合探索性 QA。

### 測試網頁應用程式
1. 從產品下拉選單中選擇 **Live**。
2. 選擇作業系統（例如 Windows 10、macOS、Android）。
3. 選擇瀏覽器/版本（例如 Chrome 120、Safari 17）。
4. 輸入您的應用程式 URL——工作階段將在新分頁中啟動。
5. 使用內建工具：DevTools、控制台、網絡檢查器、螢幕截圖和響應式檢查器。
6. 透過儀表板側邊欄在中途切換瀏覽器。
7. 報告錯誤：標記問題、添加註釋，並整合到 Jira、Slack 或電郵。

工作階段支援地理位置（100 多個國家）、網絡節流，以及 Pro 計劃中最多 25 分鐘的空閒超時。

### 測試流動網頁（裝置上的瀏覽器）
1. 在 Live 中，選擇流動作業系統（Android/iOS）。
2. 選擇裝置（例如 Samsung Galaxy S24、iPhone 15）和瀏覽器（例如 Android 上的 Chrome）。
3. 載入 URL 並進行互動——支援手勢如縮放。
4. 使用流動專用工具進行除錯：觸控模擬、方向變更和性能指標。

### 測試原生/混合流動應用程式
1. 前往 **App Live**。
2. 上傳您的應用程式（Android 為 .apk，iOS 為 .ipa；最大 500MB）或從 App Center/HockeyApp 同步。
3. 從 30,000 多種真實選項中選擇裝置（例如 iOS 18 上的 iPad Pro）。
4. 啟動應用程式並進行測試：滑動、點擊、搖動或使用硬件如 GPS/相機。
5. 進階功能：注入 QR 碼、模擬生物識別、測試 Apple Pay/Google Pay，或變更時區/深色模式。
6. 結束工作階段並檢視影片錄製/日誌。

| 功能 | Web Live | App Live |
|---------|----------|----------|
| 裝置 | 3,000+ 瀏覽器 | 30,000+ 真實流動裝置 |
| 上傳 | 僅限 URL | 應用程式二進制檔案 |
| 工具 | DevTools、解析度 | 手勢、生物識別、音訊輸入 |
| 限制 | 無限分鐘（付費） | 10-25 分鐘空閒超時 |

## 自動化測試

使用真實環境中的腳本自動化重複性測試，並擴展至數千個並行測試。

### 設置
1. 選擇框架：Selenium（Java/Python/JS）、Cypress、Playwright 或用於流動的 Appium。
2. 獲取憑證：從 Automate 儀表板取得用戶名稱和存取密鑰。
3. 配置能力：使用 JSON 指定瀏覽器、作業系統、裝置（例如 {"browser": "Chrome", "os": "Windows", "os_version": "10", "real_mobile": true}）。

### 執行
1. 將腳本指向 BrowserStack 的集線器：`https://username:accesskey@hub-cloud.browserstack.com/wd/hub`。
2. 在本地或透過 CI/CD 運行——測試並行執行。
3. 檢視結果：儀表板顯示影片、螢幕截圖、控制台/網絡日誌，以及 AI 分析的故障。
4. 對於流動測試：先透過 API 上傳應用程式，然後在能力中指定。

#### 範例 Selenium 腳本（Java，在 iPhone 上測試 Google）
```java
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.By;
import java.net.URL;

public class BrowserStackSample {
    public static final String USERNAME = "your_username";
    public static final String AUTOMATE_KEY = "your_access_key";
    public static final String URL = "https://" + USERNAME + ":" + AUTOMATE_KEY + "@hub-cloud.browserstack.com/wd/hub";

    public static void main(String[] args) throws Exception {
        DesiredCapabilities caps = new DesiredCapabilities();
        caps.setCapability("browserName", "iPhone");
        caps.setCapability("device", "iPhone 15");
        caps.setCapability("realMobile", "true");
        caps.setCapability("os_version", "17");
        caps.setCapability("name", "Sample Test");

        WebDriver driver = new RemoteWebDriver(new URL(URL), caps);
        driver.get("https://www.google.com");
        WebElement searchBox = driver.findElement(By.name("q"));
        searchBox.sendKeys("BrowserStack");
        searchBox.submit();
        System.out.println("Page title: " + driver.getTitle());
        driver.quit();
    }
}
```
可類似地適應 Python/JS。為穩定性添加等待（例如 WebDriverWait）。

## 測試自動化工作流程

透過以下步驟建立高效管道：
1. **計劃**：識別高價值測試（例如核心流程）；與 Agile 對齊。
2. **選擇工具**：使用 BrowserStack Automate 進行雲端執行；添加 Low Code 以實現無腳本測試。
3. **設計**：創建模組化腳本與可重用組件；利用 AI 進行自然語言編寫。
4. **執行**：透過 CI/CD 觸發；在真實裝置上運行並行測試，並使用自訂網絡/位置。
5. **分析**：檢視 AI 洞察、日誌和趨勢；將缺陷記錄到 Jira。
6. **維護**：應用自我修復以應對 UI 變更；優化不穩定的測試。

這可減少 40% 的維護工作並加速發布。

## 主要功能與整合

- **AI 代理**：自我修復、故障分類、測試生成。
- **視覺/無障礙**：Percy 用於 UI 差異；掃描 WCAG 合規性。
- **報告**：自訂儀表板、警報、1 年保留期。
- **整合**：CI/CD（Jenkins、Travis）、錯誤追蹤器（Jira、Trello）、版本控制（GitHub）和低代碼工具。
- **安全性**：SOC2 合規、數據加密、RBAC。

支援 21 個數據中心以實現低延遲。

## 定價計劃（截至 2025 年 10 月）

計劃為年度（節省 25%），並按用戶/並行數擴展。提供免費層級/有限試用；開源無限。

| 產品 | 入門計劃 | Pro/團隊 | 主要功能 |
|---------|--------------|----------|--------------|
| **Live（桌面/流動）** | $29/用戶/月（桌面） | $39/用戶/月（流動） | 無限分鐘、3,000+ 瀏覽器、地理位置。團隊：$30+/用戶。 |
| **Automate（網頁/流動）** | $99/月（1 並行） | $225/月（Pro，1 並行） | Selenium/Appium、AI 自我修復、影片/日誌。擴展至 25+ 並行。 |
| **App Live/Automate** | $39/月（個人） | $199/月（1 並行） | 30,000+ 裝置、手勢、生物識別。Pro：$249/月。 |
| **Percy（視覺）** | 免費（5K 螢幕截圖） | $199/月（10K） | AI 審查、Figma 整合。流動：$599/月。 |
| **無障礙** | 免費（5 頁/掃描） | $199/月（監控） | 螢幕閱讀器、每日掃描。Automate：$459/月。 |
| **測試管理** | 免費（5 用戶） | $99/月（團隊） | 儲存庫、CI 整合。Pro：$199/月。 |

企業：自訂，包含 SSO 和私有裝置。數量折扣高達 90%。

## 優點與缺點

**優點**：
- 廣泛的真實裝置覆蓋，無需硬件成本。
- 快速設置和並行擴展。
- 強大的除錯和 AI 效率。
- 與 DevOps 的強大整合。

**缺點**：
- 依賴網絡；與本地相比偶有延遲。
- 完整存取僅限付費（無完全免費層）。
- 對於絕對初學者而言，若無教程則較複雜。

## 最佳實踐

- 從高影響力測試開始；自動化 70% 的回歸測試。
- 對預發布應用程式使用本地隧道傳輸。
- 透過 AI 報告監控不穩定性；首先在最新作業系統/瀏覽器上運行。
- 結合手動與自動化測試以實現全面覆蓋。
- 利用影片/螢幕截圖進行快速分類。
- 對於流動測試：早期在各種網絡和方向下進行測試。

本指南讓您能夠有效利用 BrowserStack。如需實際操作，請探索他們的免費試用。

## 參考資料
- [BrowserStack 官方網站](https://www.browserstack.com/)
- [BrowserStack 定價](https://www.browserstack.com/pricing)
- [BrowserStack 教程：應用程式與瀏覽器測試](https://www.softwaretestinghelp.com/browserstack-tutorial/)
- [測試自動化工作流程指南](https://www.browserstack.com/guide/test-automation-workflow)
- [BrowserStack 功能概述](https://www.browserstack.com/guide)