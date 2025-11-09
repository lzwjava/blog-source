---
audio: false
generated: true
image: false
lang: hi
layout: post
model: anthropic/claude-sonnet-4
title: प्लेराइट एंड-टू-एंड टेस्टिंग गाइड
translated: true
type: note
---

## Playwright क्या है?

Playwright Microsoft द्वारा विकसित एक आधुनिक एंड-टू-एंड टेस्टिंग फ्रेमवर्क है जो कई ब्राउज़र (Chromium, Firefox, और WebKit) में वेब एप्लिकेशन के विश्वसनीय परीक्षण को सक्षम बनाता है। यह वेब पेजों को ऑटोमेट करने के लिए एक एकीकृत API प्रदान करता है और आधुनिक वेब ऐप चुनौतियों जैसे सिंगल-पेज एप्लिकेशन, डायनामिक कंटेंट और जटिल यूजर इंटरैक्शन को हैंडल करने के लिए डिज़ाइन किया गया है।

## प्रमुख विशेषताएं

- **क्रॉस-ब्राउज़र टेस्टिंग**: Chromium, Firefox, और WebKit का समर्थन करता है
- **तेज़ एक्सेक्यूशन**: डिफ़ॉल्ट रूप से समानांतर में टेस्ट चलाता है
- **ऑटो-वेट**: एलिमेंट्स के तैयार होने का स्वचालित रूप से इंतज़ार करता है
- **नेटवर्क इंटरसेप्शन**: API मॉक करें और नेटवर्क रिक्वेस्ट कैप्चर करें
- **मोबाइल टेस्टिंग**: डिवाइस एमुलेशन के साथ मोबाइल वेब ऐप्स का परीक्षण करें
- **स्क्रीनशॉट और वीडियो**: इन-बिल्ट विजुअल टेस्टिंग क्षमताएं
- **डीबगिंग टूल्स**: ट्रेस व्यूअर के साथ व्यापक डीबगिंग

## इंस्टालेशन और सेटअप

### बेसिक इंस्टालेशन

```bash
# Playwright इंस्टॉल करें
npm init playwright@latest

# या मौजूदा प्रोजेक्ट में जोड़ें
npm install -D @playwright/test

# ब्राउज़र इंस्टॉल करें
npx playwright install
```

### प्रोजेक्ट स्ट्रक्चर
```
tests/
  example.spec.js
playwright.config.js
package.json
```

### कॉन्फ़िगरेशन (playwright.config.js)

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

## अपना पहला टेस्ट लिखना

### बेसिक टेस्ट स्ट्रक्चर

```javascript
import { test, expect } from '@playwright/test';

test('basic test example', async ({ page }) => {
  // पेज पर नेविगेट करें
  await page.goto('https://example.com');
  
  // एलिमेंट्स के साथ इंटरैक्ट करें
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // असेर्शन
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### कॉमन एक्शन

#### नेविगेशन
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### एलिमेंट इंटरैक्शन
```javascript
// एलिमेंट्स पर क्लिक करें
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// फॉर्म भरें
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// चेक/अनचेक करें
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### वेटिंग और टाइमआउट
```javascript
// एलिमेंट्स के लिए इंतज़ार करें
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// कस्टम कंडीशन के लिए इंतज़ार करें
await page.waitForFunction(() => window.myApp.isReady);
```

## एडवांस्ड टेस्टिंग पैटर्न

### पेज ऑब्जेक्ट मॉडल

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

### API टेस्टिंग
```javascript
test('API testing', async ({ request }) => {
  // POST रिक्वेस्ट
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

### नेटवर्क मॉकिंग
```javascript
test('mock API responses', async ({ page }) => {
  // API रिस्पांस मॉक करें
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### विजुअल टेस्टिंग
```javascript
test('visual comparison', async ({ page }) => {
  await page.goto('/dashboard');
  
  // फुल पेज स्क्रीनशॉट
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // एलिमेंट स्क्रीनशॉट
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## टेस्ट ऑर्गनाइजेशन और बेस्ट प्रैक्टिसेज

### टेस्ट हुक्स
```javascript
import { test, expect } from '@playwright/test';

test.describe('User Management', () => {
  test.beforeEach(async ({ page }) => {
    // प्रत्येक टेस्ट से पहले रन करें
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // प्रत्येक टेस्ट के बाद क्लीन अप करें
    await page.evaluate(() => localStorage.clear());
  });

  test('should create new user', async ({ page }) => {
    // टेस्ट इम्प्लीमेंटेशन
  });
});
```

### फिक्स्चर और टेस्ट कॉन्टेक्स्ट
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // टेस्ट से पहले लॉगिन करें
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // टेस्ट के बाद क्लीनअप
    await page.goto('/logout');
  },
});

// टेस्ट फाइल में
import { test, expect } from '../fixtures/auth';

test('authenticated user actions', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## टेस्ट चलाना

### कमांड लाइन ऑप्शन
```bash
# सभी टेस्ट चलाएं
npx playwright test

# स्पेसिफिक टेस्ट फाइल चलाएं
npx playwright test tests/login.spec.js

# हेडेड मोड में टेस्ट चलाएं
npx playwright test --headed

# स्पेसिफिक ब्राउज़र में टेस्ट चलाएं
npx playwright test --project=firefox

# डीबगिंग के साथ टेस्ट चलाएं
npx playwright test --debug

# समानांतर में टेस्ट चलाएं
npx playwright test --workers=4
```

### टेस्ट रिपोर्ट
```bash
# HTML रिपोर्ट जनरेट करें
npx playwright show-report

# ट्रेस फाइल्स देखें
npx playwright show-trace trace.zip
```

## Playwright बनाम Selenium

### आर्किटेक्चर डिफरेंस

| फीचर | Playwright | Selenium |
|---------|------------|----------|
| **आर्किटेक्चर** | डायरेक्ट ब्राउज़र कम्युनिकेशन | WebDriver प्रोटोकॉल |
| **ब्राउज़र सपोर्ट** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge, IE |
| **इंस्टालेशन** | ब्राउज़र के साथ सिंगल पैकेज | अलग ड्राइवर डाउनलोड |
| **लैंग्वेज सपोर्ट** | JavaScript, Python, Java, C# | अधिकांश प्रोग्रामिंग लैंग्वेज |

### परफॉर्मेंस कम्पेरिजन

**Playwright के फायदे:**
- **तेज़ एक्सेक्यूशन**: डायरेक्ट ब्राउज़र API कम्युनिकेशन WebDriver ओवरहेड को खत्म करता है
- **डिफ़ॉल्ट रूप से समानांतर**: इन-बिल्ट समानांतर टेस्ट एक्सेक्यूशन
- **ऑटो-वेट**: एक्सप्लिसिट वेट के बिना इंटेलिजेंट वेटिंग
- **नेटवर्क कंट्रोल**: इन-बिल्ट रिक्वेस्ट/रिस्पांस इंटरसेप्शन

**Selenium के फायदे:**
- **परिपक्व इकोसिस्टम**: व्यापक कम्युनिटी और थर्ड-पार्टी टूल्स
- **लैंग्वेज फ्लेक्सिबिलिटी**: अधिक प्रोग्रामिंग लैंग्वेज का समर्थन
- **ब्राउज़र कवरेज**: Internet Explorer जैसे पुराने ब्राउज़र सपोर्ट करता है
- **इंडस्ट्री स्टैंडर्ड**: व्यापक डॉक्यूमेंटेशन के साथ व्यापक रूप से अपनाया गया

### फीचर कम्पेरिजन

#### टेस्ट रिलायबिलिटी
```javascript
// Playwright - ऑटो-वेट इन-बिल्ट
await page.click('button'); // एलिमेंट के क्लिक करने योग्य होने का इंतज़ार करता है

// Selenium - मैनुअल वेट आवश्यक
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### मोबाइल टेस्टिंग
```javascript
// Playwright - इन-बिल्ट मोबाइल एमुलेशन
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - अतिरिक्त सेटअप की आवश्यकता
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### नेटवर्क हैंडलिंग
```javascript
// Playwright - नेटिव नेटवर्क इंटरसेप्शन
await page.route('**/api/**', route => route.abort());

// Selenium - प्रॉक्सी सेटअप की आवश्यकता
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```

### माइग्रेशन कंसीडरेशन

**Playwright कब चुनें:**
- नए प्रोजेक्ट या ग्रीनफील्ड एप्लिकेशन
- SPA आर्किटेक्चर वाले मॉडर्न वेब ऐप्स
- तेज़, विश्वसनीय टेस्ट एक्सेक्यूशन की आवश्यकता
- टीम मुख्य रूप से JavaScript/TypeScript का उपयोग करती है
- इन-बिल्ट विजुअल टेस्टिंग की आवश्यकता

**Selenium के साथ कब बने रहें:**
- बड़े मौजूदा टेस्ट सूट
- विशिष्ट ब्राउज़र/OS कॉम्बिनेशन की आवश्यकता
- गैर-जावास्क्रिप्ट भाषाओं में टीम की विशेषज्ञता
- मौजूदा CI/CD पाइपलाइन के साथ एकीकरण
- लीगेसी एप्लिकेशन का परीक्षण

### कोड कम्पेरिजन उदाहरण

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

## निष्कर्ष

Playwright एंड-टू-एंड टेस्टिंग के लिए एक आधुनिक दृष्टिकोण का प्रतिनिधित्व करता है जिसमें गति, विश्वसनीयता और डेवलपर अनुभव में महत्वपूर्ण फायदे हैं। जबकि Selenium स्थापित प्रोजेक्ट्स और विशिष्ट उपयोग के मामलों के लिए एक ठोस विकल्प बना हुआ है, Playwright की आर्किटेक्चर और फीचर सेट इसे आधुनिक वेब एप्लिकेशन के परीक्षण के लिए विशेष रूप से उपयुक्त बनाते हैं। उनके बीच चुनाव आपकी विशिष्ट प्रोजेक्ट आवश्यकताओं, मौजूदा इन्फ्रास्ट्रक्चर और टीम विशेषज्ञता पर आधारित होना चाहिए।