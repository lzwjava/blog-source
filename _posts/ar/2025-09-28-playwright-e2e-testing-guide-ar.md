---
audio: false
generated: true
image: false
lang: ar
layout: post
model: anthropic/claude-sonnet-4
title: دليل الاختبار الشامل لبرنامج بلاي رايت
translated: true
type: note
---

## ما هو Playwright؟

Playwright هو إطار عمل حديث للاختبار الشامل (End-to-End) طورته Microsoft، يتيح اختبار تطبيقات الويب بشكل موثوق عبر متصفحات متعددة (Chromium، Firefox، وWebKit). يوفر واجهة برمجة موحدة لأتمتة صفحات الويب ومصمم لمعالجة تحديات تطبيقات الويب الحديثة مثل تطبيقات الصفحة الواحدة، والمحتوى الديناميكي، وتفاعلات المستخدم المعقدة.

## الميزات الرئيسية

- **الاختبار عبر المتصفحات**: يدعم Chromium، Firefox، وWebKit
- **تنفيذ سريع**: يشغل الاختبارات بشكل متوازي افتراضيًا
- **الانتظار التلقائي**: ينتظر تلقائيًا حتى تصبح العناصر جاهزة
- **اعتراض الشبكة**: محاكاة واجهات برمجة التطبيقات (APIs) والتقاط طلبات الشبكة
- **اختبار الجوال**: اختبار تطبيقات الويب للجوال مع محاكاة الجهاز
- **لقطات الشاشة والفيديوهات**: قدرات اختبار مرئي مدمجة
- **أدوات التصحيح**: تصحيح شامل مع عارض التتبع (Trace Viewer)

## التثبيت والإعداد

### التثبيت الأساسي

```bash
# تثبيت Playwright
npm init playwright@latest

# أو إضافة إلى مشروع موجود
npm install -D @playwright/test

# تثبيت المتصفحات
npx playwright install
```

### هيكل المشروع
```
tests/
  example.spec.js
playwright.config.js
package.json
```

### التهيئة (playwright.config.js)

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

## كتابة أول اختبار لك

### الهيكل الأساسي للاختبار

```javascript
import { test, expect } from '@playwright/test';

test('basic test example', async ({ page }) => {
  // الانتقال إلى الصفحة
  await page.goto('https://example.com');
  
  // التفاعل مع العناصر
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // التأكيدات (Assertions)
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### الإجراءات الشائعة

#### التنقل
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### التفاعل مع العناصر
```javascript
// النقر على العناصر
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// ملء النماذج
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// تحديد/إلغاء تحديد
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### الانتظار و المهلات (Timeouts)
```javascript
// الانتظار للعناصر
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// الانتظار لشروط مخصصة
await page.waitForFunction(() => window.myApp.isReady);
```

## أنماط الاختبار المتقدمة

### نموذج كائن الصفحة (Page Object Model)

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

### اختبار واجهة برمجة التطبيقات (API Testing)
```javascript
test('API testing', async ({ request }) => {
  // طلب POST
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

### محاكاة الشبكة (Network Mocking)
```javascript
test('mock API responses', async ({ page }) => {
  // محاكاة استجابة واجهة برمجة التطبيقات (API)
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### الاختبار المرئي (Visual Testing)
```javascript
test('visual comparison', async ({ page }) => {
  await page.goto('/dashboard');
  
  // لقطة شاشة للصفحة كاملة
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // لقطة شاشة للعنصر
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## تنظيم الاختبار والممارسات الأفضل

### خطافات الاختبار (Test Hooks)
```javascript
import { test, expect } from '@playwright/test';

test.describe('User Management', () => {
  test.beforeEach(async ({ page }) => {
    // التشغيل قبل كل اختبار
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // التنظيف بعد كل اختبار
    await page.evaluate(() => localStorage.clear());
  });

  test('should create new user', async ({ page }) => {
    // تنفيذ الاختبار
  });
});
```

### التركيبات والسياق (Fixtures and Test Context)
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // تسجيل الدخول قبل الاختبار
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // التنظيف بعد الاختبار
    await page.goto('/logout');
  },
});

// في ملف الاختبار
import { test, expect } from '../fixtures/auth';

test('authenticated user actions', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## تشغيل الاختبارات

### خيارات سطر الأوامر
```bash
# تشغيل جميع الاختبارات
npx playwright test

# تشغيل ملف اختبار محدد
npx playwright test tests/login.spec.js

# تشغيل الاختبارات في الوضع المرئي (headed)
npx playwright test --headed

# تشغيل الاختبارات في متصفح محدد
npx playwright test --project=firefox

# تشغيل الاختبارات مع التصحيح
npx playwright test --debug

# تشغيل الاختبارات بشكل متوازي
npx playwright test --workers=4
```

### تقارير الاختبار
```bash
# توليد تقرير HTML
npx playwright show-report

# عرض ملفات التتبع (Trace)
npx playwright show-trace trace.zip
```

## Playwright مقابل Selenium

### الاختلافات في البنية

| الميزة | Playwright | Selenium |
|---------|------------|----------|
| **البنية** | اتصال مباشر بالمتصفح | بروتوكول WebDriver |
| **دعم المتصفحات** | Chromium، Firefox، WebKit | Chrome، Firefox، Safari، Edge، IE |
| **التثبيت** | حزمة واحدة مع المتصفحات | تنزيل برامج تشغيل منفصلة |
| **دعم اللغات** | JavaScript، Python، Java، C# | معظم لغات البرمجة |

### مقارنة الأداء

**مزايا Playwright:**
- **تنفيذ أسرع**: الاتصال المباشر بواجهة برمجة تطبيقات المتصفح يلغي عبء WebDriver
- **متوازي افتراضيًا**: تنفيذ اختبارات متوازي مدمج
- **انتظار تلقائي**: انتظار ذكي بدون انتظارات صريحة
- **تحكم في الشبكة**: اعتراض الطلبات والاستجابات مدمج

**مزايا Selenium:**
- **نظام بيئي ناضج**: مجتمع واسع وأدوات تابعة لجهات خارجية
- **مرونة اللغة**: دعم للمزيد من لغات البرمجة
- **تغطية المتصفحات**: يدعم المتصفحات القديمة مثل Internet Explorer
- **معيار الصناعة**: معتمد على نطاق واسع مع توثيق شامل

### مقارنة الميزات

#### موثوقية الاختبار
```javascript
// Playwright - الانتظار التلقائي مدمج
await page.click('button'); // ينتظر حتى يصبح العنصر قابلاً للنقر

// Selenium - يتطلب انتظارات يدوية
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### اختبار الجوال
```javascript
// Playwright - محاكاة الجوال المدمجة
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - يتطلب إعدادًا إضافيًا
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### معالجة الشبكة
```javascript
// Playwright - اعتراض الشبكة الأصلي
await page.route('**/api/**', route => route.abort());

// Selenium - يتطلب إعداد وكيل (Proxy)
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```

### اعتبارات الترحيل

**متى تختار Playwright:**
- المشاريع الجديدة أو التطبيقات الخضراء (Greenfield)
- تطبيقات الويب الحديثة ذات بنية SPA
- الحاجة لتنفيذ اختبار سريع وموثوق
- الفريق يستخدم بشكل أساسي JavaScript/TypeScript
- الحاجة للاختبار المرئي المدمج

**متى تلتزم بـ Selenium:**
- مجموعات الاختبارات الحالية الكبيرة
- الحاجة لتركيبات متصفح/نظام تشغيل محددة
- خبرة الفريق في لغات غير JavaScript
- التكامل مع خطوط أنابيب CI/CD الحالية
- اختبار التطبيقات القديمة (Legacy)

### مثال مقارنة الكود

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

## الخلاصة

يمثل Playwright نهجًا حديثًا للاختبار الشامل (End-to-End) مع مزايا كبيرة في السرعة، والموثوقية، وتجربة المطور. بينما يظل Selenium خيارًا قويًا للمشاريع القائمة وحالات الاستخدام المحددة، فإن بنية Playwright ومجموعة ميزاتها تجعله مناسبًا بشكل خاص لاختبار تطبيقات الويب الحديثة. يجب أن يعتمد الاختيار بينهما على متطلبات مشروعك المحددة، والبنية التحتية الحالية، وخبرة فريقك.