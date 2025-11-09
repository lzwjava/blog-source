---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: 劇作家端對端測試指南
translated: true
type: note
---

## 什麼是 Playwright？

Playwright 是由 Microsoft 開發的現代端到端測試框架，能夠在多種瀏覽器（Chromium、Firefox 和 WebKit）上可靠地測試 Web 應用程式。它提供了統一的 API 來自動化網頁操作，專為處理現代 Web 應用程式的挑戰而設計，例如單頁應用程式、動態內容和複雜的使用者互動。

## 主要功能

- **跨瀏覽器測試**：支援 Chromium、Firefox 和 WebKit
- **快速執行**：預設並行執行測試
- **自動等待**：自動等待元素準備就緒
- **網路攔截**：模擬 API 並捕獲網路請求
- **行動裝置測試**：透過裝置模擬測試行動 Web 應用程式
- **螢幕截圖和影片**：內建視覺測試功能
- **除錯工具**：提供包含追蹤檢視器的全面除錯功能

## 安裝與設定

### 基本安裝

```bash
# 安裝 Playwright
npm init playwright@latest

# 或添加到現有專案
npm install -D @playwright/test

# 安裝瀏覽器
npx playwright install
```

### 專案結構
```
tests/
  example.spec.js
playwright.config.js
package.json
```

### 設定 (playwright.config.js)

```javascript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html',
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],

  webServer: {
    command: 'npm run start',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
  },
});
```

## 編寫第一個測試

### 基本測試結構

```javascript
import { test, expect } from '@playwright/test';

test('basic test example', async ({ page }) => {
  // 導航到頁面
  await page.goto('https://example.com');
  
  // 與元素互動
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // 斷言
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### 常見操作

#### 導航
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### 元素互動
```javascript
// 點擊元素
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// 填寫表單
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// 勾選/取消勾選
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### 等待與逾時
```javascript
// 等待元素
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// 等待自訂條件
await page.waitForFunction(() => window.myApp.isReady);
```

## 進階測試模式

### 頁面物件模型

```javascript
// pages/LoginPage.js
export class LoginPage {
  constructor(page) {
    this.page = page;
    this.emailInput = page.locator('input[name="email"]');
    this.passwordInput = page.locator('input[name="password"]');
    this.loginButton = page.locator('button[type="submit"]');
  }

  async login(email, password) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }
}

// tests/login.spec.js
import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';

test('user can login', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await page.goto('/login');
  await loginPage.login('user@example.com', 'password123');
  await expect(page).toHaveURL('/dashboard');
});
```

### API 測試
```javascript
test('API testing', async ({ request }) => {
  // POST 請求
  const response = await request.post('/api/users', {
    data: {
      name: 'John Doe',
      email: 'john@example.com'
    }
  });
  
  expect(response.ok()).toBeTruthy();
  const userData = await response.json();
  expect(userData.name).toBe('John Doe');
});
```

### 網路模擬
```javascript
test('mock API responses', async ({ page }) => {
  // 模擬 API 回應
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### 視覺測試
```javascript
test('visual comparison', async ({ page }) => {
  await page.goto('/dashboard');
  
  // 全頁螢幕截圖
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // 元素螢幕截圖
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## 測試組織與最佳實踐

### 測試鉤子
```javascript
import { test, expect } from '@playwright/test';

test.describe('User Management', () => {
  test.beforeEach(async ({ page }) => {
    // 在每個測試前執行
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // 在每個測試後清理
    await page.evaluate(() => localStorage.clear());
  });

  test('should create new user', async ({ page }) => {
    // 測試實作
  });
});
```

### 夾具與測試上下文
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // 測試前登入
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // 測試後清理
    await page.goto('/logout');
  },
});

// 在測試檔案中
import { test, expect } from '../fixtures/auth';

test('authenticated user actions', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## 執行測試

### 命令列選項
```bash
# 執行所有測試
npx playwright test

# 執行特定測試檔案
npx playwright test tests/login.spec.js

# 在 headed 模式下執行測試
npx playwright test --headed

# 在特定瀏覽器中執行測試
npx playwright test --project=firefox

# 在除錯模式下執行測試
npx playwright test --debug

# 並行執行測試
npx playwright test --workers=4
```

### 測試報告
```bash
# 產生 HTML 報告
npx playwright show-report

# 檢視追蹤檔案
npx playwright show-trace trace.zip
```

## Playwright 與 Selenium 比較

### 架構差異

| 功能 | Playwright | Selenium |
|---------|------------|----------|
| **架構** | 直接瀏覽器通訊 | WebDriver 協定 |
| **瀏覽器支援** | Chromium、Firefox、WebKit | Chrome、Firefox、Safari、Edge、IE |
| **安裝** | 單一套件包含瀏覽器 | 需單獨下載驅動程式 |
| **語言支援** | JavaScript、Python、Java、C# | 大多數程式語言 |

### 效能比較

**Playwright 優勢：**
- **執行速度更快**：直接瀏覽器 API 通訊消除了 WebDriver 開銷
- **預設並行**：內建並行測試執行
- **自動等待**：無需明確等待的智慧等待機制
- **網路控制**：內建請求/回應攔截功能

**Selenium 優勢：**
- **成熟生態系統**：廣泛的社群和第三方工具
- **語言靈活性**：支援更多程式語言
- **瀏覽器覆蓋率**：支援舊版瀏覽器如 Internet Explorer
- **業界標準**：廣泛採用且文件豐富

### 功能比較

#### 測試可靠性
```javascript
// Playwright - 內建自動等待
await page.click('button'); // 等待元素可點擊

// Selenium - 需要手動等待
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### 行動裝置測試
```javascript
// Playwright - 內建行動裝置模擬
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - 需要額外設定
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### 網路處理
```javascript
// Playwright - 原生網路攔截
await page.route('**/api/**', route => route.abort());

// Selenium - 需要代理伺服器設定
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```

### 遷移考量

**何時選擇 Playwright：**
- 新專案或全新應用程式
- 具有 SPA 架構的現代 Web 應用程式
- 需要快速、可靠的測試執行
- 團隊主要使用 JavaScript/TypeScript
- 需要內建視覺測試功能

**何時堅持使用 Selenium：**
- 大型現有測試套件
- 需要特定的瀏覽器/作業系統組合
- 團隊擅長非 JavaScript 語言
- 與現有 CI/CD 管線整合
- 測試傳統應用程式

### 程式碼比較範例

```javascript
// Playwright
import { test, expect } from '@playwright/test';

test('login flow', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name="email"]', 'user@example.com');
  await page.fill('[name="password"]', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});

// Selenium (JavaScript)
const { Builder, By, until } = require('selenium-webdriver');

describe('login flow', () => {
  let driver;
  
  beforeEach(async () => {
    driver = await new Builder().forBrowser('chrome').build();
  });
  
  afterEach(async () => {
    await driver.quit();
  });
  
  it('should login successfully', async () => {
    await driver.get('http://localhost:3000/login');
    await driver.findElement(By.name('email')).sendKeys('user@example.com');
    await driver.findElement(By.name('password')).sendKeys('password');
    await driver.findElement(By.css('button[type="submit"]')).click();
    await driver.wait(until.urlContains('/dashboard'));
  });
});
```

## 結論

Playwright 代表了端到端測試的現代化方法，在速度、可靠性和開發者體驗方面具有顯著優勢。雖然 Selenium 對於已建立的專案和特定使用場景仍然是穩固的選擇，但 Playwright 的架構和功能集使其特別適合測試現代 Web 應用程式。兩者之間的選擇應基於您的具體專案需求、現有基礎設施和團隊專業知識。