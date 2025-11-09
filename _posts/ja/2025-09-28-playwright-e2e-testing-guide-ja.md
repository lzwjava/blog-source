---
audio: false
generated: true
image: false
lang: ja
layout: post
model: anthropic/claude-sonnet-4
title: Playwrightエンドツーエンドテストガイド
translated: true
type: note
---

## Playwrightとは？

PlaywrightはMicrosoftによって開発されたモダンなエンドツーエンドテストフレームワークで、複数のブラウザ（Chromium、Firefox、WebKit）にわたるWebアプリケーションの信頼性の高いテストを可能にします。Webページの自動化のための統一されたAPIを提供し、シングルページアプリケーション、動的コンテンツ、複雑なユーザーインタラクションといったモダンなWebアプリの課題に対処するように設計されています。

## 主な機能

- **クロスブラウザテスト**: Chromium、Firefox、WebKitをサポート
- **高速実行**: デフォルトで並列テスト実行
- **自動待機**: 要素の準備ができるまで自動的に待機
- **ネットワークインターセプション**: APIのモックとネットワークリクエストのキャプチャ
- **モバイルテスト**: デバイスエミュレーションによるモバイルWebアプリのテスト
- **スクリーンショットと動画**: 組み込みのビジュアルテスト機能
- **デバッグツール**: トレースビューアーによる包括的なデバッグ

## インストールとセットアップ

### 基本インストール

```bash
# Playwrightのインストール
npm init playwright@latest

# 既存プロジェクトへの追加
npm install -D @playwright/test

# ブラウザのインストール
npx playwright install
```

### プロジェクト構造
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

## 最初のテストを書く

### 基本的なテスト構造

```javascript
import { test, expect } from '@playwright/test';

test('基本的なテスト例', async ({ page }) => {
  // ページに移動
  await page.goto('https://example.com');
  
  // 要素とのインタラクション
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // アサーション
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### 一般的なアクション

#### ナビゲーション
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### 要素インタラクション
```javascript
// 要素のクリック
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// フォーム入力
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// チェック/チェック解除
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### 待機とタイムアウト
```javascript
// 要素の待機
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// カスタム条件の待機
await page.waitForFunction(() => window.myApp.isReady);
```

## 高度なテストパターン

### ページオブジェクトモデル

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

test('ユーザーログイン', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await page.goto('/login');
  await loginPage.login('user@example.com', 'password123');
  await expect(page).toHaveURL('/dashboard');
});
```

### APIテスト
```javascript
test('APIテスト', async ({ request }) => {
  // POSTリクエスト
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

### ネットワークモッキング
```javascript
test('APIレスポンスのモック', async ({ page }) => {
  // APIレスポンスのモック
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### ビジュアルテスト
```javascript
test('ビジュアル比較', async ({ page }) => {
  await page.goto('/dashboard');
  
  // フルページスクリーンショット
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // 要素スクリーンショット
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## テストの構成とベストプラクティス

### テストフック
```javascript
import { test, expect } from '@playwright/test';

test.describe('ユーザー管理', () => {
  test.beforeEach(async ({ page }) => {
    // 各テストの前に実行
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // 各テストの後にクリーンアップ
    await page.evaluate(() => localStorage.clear());
  });

  test('新規ユーザー作成', async ({ page }) => {
    // テスト実装
  });
});
```

### フィクスチャとテストコンテキスト
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // テスト前のログイン
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // テスト後のクリーンアップ
    await page.goto('/logout');
  },
});

// テストファイル内
import { test, expect } from '../fixtures/auth';

test('認証済みユーザーのアクション', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## テストの実行

### コマンドラインオプション
```bash
# すべてのテストを実行
npx playwright test

# 特定のテストファイルを実行
npx playwright test tests/login.spec.js

# ヘッデッドモードで実行
npx playwright test --headed

# 特定のブラウザで実行
npx playwright test --project=firefox

# デバッグモードで実行
npx playwright test --debug

# 並列実行
npx playwright test --workers=4
```

### テストレポート
```bash
# HTMLレポートの生成
npx playwright show-report

# トレースファイルの表示
npx playwright show-trace trace.zip
```

## Playwright vs Selenium

### アーキテクチャの違い

| 機能 | Playwright | Selenium |
|---------|------------|----------|
| **アーキテクチャ** | 直接ブラウザ通信 | WebDriverプロトコル |
| **ブラウザサポート** | Chromium、Firefox、WebKit | Chrome、Firefox、Safari、Edge、IE |
| **インストール** | ブラウザを含む単一パッケージ | 個別のドライバーダウンロード |
| **言語サポート** | JavaScript、Python、Java、C# | ほとんどのプログラミング言語 |

### パフォーマンス比較

**Playwrightの利点:**
- **高速実行**: 直接ブラウザAPI通信によりWebDriverのオーバーヘッドを排除
- **デフォルト並列**: 組み込みの並列テスト実行
- **自動待機**: 明示的な待機なしのインテリジェントな待機
- **ネットワーク制御**: 組み込みのリクエスト/レスポンスインターセプション

**Seleniumの利点:**
- **成熟したエコシステム**: 広範なコミュニティとサードパーティツール
- **言語柔軟性**: より多くのプログラミング言語のサポート
- **ブラウザカバレッジ**: Internet Explorerなどの古いブラウザをサポート
- **業界標準**: 広く採用され、包括的なドキュメント

### 機能比較

#### テスト信頼性
```javascript
// Playwright - 自動待機が組み込み
await page.click('button'); // 要素がクリック可能になるまで待機

// Selenium - 手動待機が必要
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### モバイルテスト
```javascript
// Playwright - 組み込みのモバイルエミュレーション
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - 追加のセットアップが必要
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### ネットワーク処理
```javascript
// Playwright - ネイティブのネットワークインターセプション
await page.route('**/api/**', route => route.abort());

// Selenium - プロキシ設定が必要
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```
```

### 移行の考慮事項

**Playwrightを選択する場合:**
- 新規プロジェクトまたはグリーンフィールドアプリケーション
- SPAアーキテクチャのモダンなWebアプリ
- 高速で信頼性の高いテスト実行の必要性
- チームが主にJavaScript/TypeScriptを使用
- 組み込みのビジュアルテストの要件

**Seleniumを継続する場合:**
- 大規模な既存テストスイート
- 特定のブラウザ/OSの組み合わせの必要性
- 非JavaScript言語のチーム専門知識
- 既存のCI/CDパイプラインとの統合
- レガシーアプリケーションのテスト

### コード比較例

```javascript
// Playwright
import { test, expect } from '@playwright/test';

test('ログインフロー', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name="email"]', 'user@example.com');
  await page.fill('[name="password"]', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});

// Selenium (JavaScript)
const { Builder, By, until } = require('selenium-webdriver');

describe('ログインフロー', () => {
  let driver;
  
  beforeEach(async () => {
    driver = await new Builder().forBrowser('chrome').build();
  });
  
  afterEach(async () => {
    await driver.quit();
  });
  
  it('ログイン成功', async () => {
    await driver.get('http://localhost:3000/login');
    await driver.findElement(By.name('email')).sendKeys('user@example.com');
    await driver.findElement(By.name('password')).sendKeys('password');
    await driver.findElement(By.css('button[type="submit"]')).click();
    await driver.wait(until.urlContains('/dashboard'));
  });
});
```

## 結論

Playwrightは、速度、信頼性、開発者エクスペリエンスにおいて大きな利点を持つ、モダンなエンドツーエンドテストへのアプローチを表しています。Seleniumは確立されたプロジェクトや特定のユースケースにおいて堅実な選択肢であり続けますが、Playwrightのアーキテクチャと機能セットは、モダンなWebアプリケーションのテストに特に適しています。これらを選択する際は、特定のプロジェクト要件、既存のインフラストラクチャ、チームの専門知識に基づいて決定すべきです。