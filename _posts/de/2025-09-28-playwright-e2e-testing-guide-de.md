---
audio: false
generated: true
image: false
lang: de
layout: post
model: anthropic/claude-sonnet-4
title: Playwright End-to-End-Testing-Leitfaden
translated: true
type: note
---

## Was ist Playwright?

Playwright ist ein modernes End-to-End-Test-Framework, das von Microsoft entwickelt wurde und zuverlässiges Testen von Webanwendungen über mehrere Browser hinweg (Chromium, Firefox und WebKit) ermöglicht. Es bietet eine einheitliche API zur Automatisierung von Webseiten und ist dafür konzipiert, die Herausforderungen moderner Web-Apps wie Single-Page-Anwendungen, dynamische Inhalte und komplexe Benutzerinteraktionen zu bewältigen.

## Hauptmerkmale

- **Cross-Browser-Testing**: Unterstützt Chromium, Firefox und WebKit
- **Schnelle Ausführung**: Führt Tests standardmäßig parallel aus
- **Auto-Wait**: Wartet automatisch, bis Elemente bereit sind
- **Netzwerk-Interception**: API-Mocking und Erfassung von Netzwerkanfragen
- **Mobile Testing**: Testen mobiler Web-Apps mit Device-Emulation
- **Screenshots und Videos**: Integrierte Visual-Testing-Fähigkeiten
- **Debugging-Tools**: Umfangreiches Debugging mit Trace-Viewer

## Installation und Einrichtung

### Grundinstallation

```bash
# Install Playwright
npm init playwright@latest

# Oder zu bestehendem Projekt hinzufügen
npm install -D @playwright/test

# Browser installieren
npx playwright install
```

### Projektstruktur
```
tests/
  example.spec.js
playwright.config.js
package.json
```

### Konfiguration (playwright.config.js)

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

## Deinen ersten Test schreiben

### Grundlegende Teststruktur

```javascript
import { test, expect } from '@playwright/test';

test('basic test example', async ({ page }) => {
  // Zur Seite navigieren
  await page.goto('https://example.com');
  
  // Mit Elementen interagieren
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // Assertions
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### Häufige Aktionen

#### Navigation
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### Element-Interaktionen
```javascript
// Elemente klicken
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// Formulare ausfüllen
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// Checkboxen an-/abwählen
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### Warten und Timeouts
```javascript
// Auf Elemente warten
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// Auf benutzerdefinierte Bedingungen warten
await page.waitForFunction(() => window.myApp.isReady);
```

## Erweiterte Testmuster

### Page Object Model

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

### API-Testing
```javascript
test('API testing', async ({ request }) => {
  // POST-Anfrage
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

### Network Mocking
```javascript
test('mock API responses', async ({ page }) => {
  // API-Antwort mocken
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### Visual Testing
```javascript
test('visual comparison', async ({ page }) => {
  await page.goto('/dashboard');
  
  // Vollständiger Seiten-Screenshot
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // Element-Screenshot
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## Testorganisation und Best Practices

### Test Hooks
```javascript
import { test, expect } from '@playwright/test';

test.describe('User Management', () => {
  test.beforeEach(async ({ page }) => {
    // Vor jedem Test ausführen
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // Nach jedem Test aufräumen
    await page.evaluate(() => localStorage.clear());
  });

  test('should create new user', async ({ page }) => {
    // Testimplementierung
  });
});
```

### Fixtures und Test Context
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // Vor Test einloggen
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // Nach Test aufräumen
    await page.goto('/logout');
  },
});

// In Testdatei
import { test, expect } from '../fixtures/auth';

test('authenticated user actions', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## Tests ausführen

### Befehlszeilenoptionen
```bash
# Alle Tests ausführen
npx playwright test

# Bestimmte Testdatei ausführen
npx playwright test tests/login.spec.js

# Tests im Headed-Modus ausführen
npx playwright test --headed

# Tests in bestimmtem Browser ausführen
npx playwright test --project=firefox

# Tests mit Debugging ausführen
npx playwright test --debug

# Tests parallel ausführen
npx playwright test --workers=4
```

### Testberichte
```bash
# HTML-Bericht generieren
npx playwright show-report

# Trace-Dateien anzeigen
npx playwright show-trace trace.zip
```

## Playwright vs Selenium

### Architekturunterschiede

| Merkmal | Playwright | Selenium |
|---------|------------|----------|
| **Architektur** | Direkte Browser-Kommunikation | WebDriver-Protokoll |
| **Browser-Unterstützung** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge, IE |
| **Installation** | Einzelnes Paket mit Browsern | Separate Driver-Downloads |
| **Sprachunterstützung** | JavaScript, Python, Java, C# | Die meisten Programmiersprachen |

### Leistungsvergleich

**Playwright-Vorteile:**
- **Schnellere Ausführung**: Direkte Browser-API-Kommunikation eliminiert WebDriver-Overhead
- **Parallel standardmäßig**: Integrierte parallele Testausführung
- **Auto-Wait**: Intelligentes Warten ohne explizite Waits
- **Netzwerk-Kontrolle**: Integrierte Request/Response-Interception

**Selenium-Vorteile:**
- **Ausgereiftes Ökosystem**: Umfangreiche Community und Drittanbieter-Tools
- **Sprachflexibilität**: Unterstützung für mehr Programmiersprachen
- **Browser-Abdeckung**: Unterstützt ältere Browser wie Internet Explorer
- **Industriestandard**: Weit verbreitet mit umfangreicher Dokumentation

### Funktionsvergleich

#### Testzuverlässigkeit
```javascript
// Playwright - Auto-Wait integriert
await page.click('button'); // Wartet, bis Element klickbar ist

// Selenium - Manuelle Waits erforderlich
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### Mobile Testing
```javascript
// Playwright - Integrierte Mobile-Emulation
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - Erfordert zusätzliche Einrichtung
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### Netzwerkbehandlung
```javascript
// Playwright - Native Netzwerk-Interception
await page.route('**/api/**', route => route.abort());

// Selenium - Erfordert Proxy-Einrichtung
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```

### Migrationsüberlegungen

**Wann Playwright wählen:**
- Neue Projekte oder Greenfield-Anwendungen
- Moderne Web-Apps mit SPA-Architektur
- Bedarf an schneller, zuverlässiger Testausführung
- Team verwendet primär JavaScript/TypeScript
- Anforderung an integriertes Visual Testing

**Wann bei Selenium bleiben:**
- Große bestehende Testsuites
- Bedarf an spezifischen Browser/OS-Kombinationen
- Team-Expertise in Nicht-JavaScript-Sprachen
- Integration in bestehende CI/CD-Pipelines
- Testen von Legacy-Anwendungen

### Code-Vergleichsbeispiel

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

## Fazit

Playwright repräsentiert einen modernen Ansatz für End-to-End-Tests mit signifikanten Vorteilen in Geschwindigkeit, Zuverlässigkeit und Developer Experience. Während Selenium eine solide Wahl für etablierte Projekte und spezifische Anwendungsfälle bleibt, machen Playwrights Architektur und Funktionsumfang es besonders gut geeignet für das Testen moderner Webanwendungen. Die Wahl zwischen ihnen sollte auf Ihren spezifischen Projektanforderungen, bestehender Infrastruktur und Team-Expertise basieren.