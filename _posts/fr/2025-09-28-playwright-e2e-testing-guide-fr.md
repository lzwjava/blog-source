---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Guide de Test End-to-End avec Playwright
translated: true
type: note
---

## Qu'est-ce que Playwright ?

Playwright est un framework moderne de tests end-to-end développé par Microsoft qui permet de tester de manière fiable des applications web sur plusieurs navigateurs (Chromium, Firefox et WebKit). Il fournit une API unifiée pour automatiser les pages web et est conçu pour gérer les défis des applications web modernes comme les applications single-page, le contenu dynamique et les interactions utilisateur complexes.

## Fonctionnalités principales

- **Tests cross-browser** : Prend en charge Chromium, Firefox et WebKit
- **Exécution rapide** : Exécute les tests en parallèle par défaut
- **Auto-wait** : Attend automatiquement que les éléments soient prêts
- **Interception réseau** : Mock des APIs et capture des requêtes réseau
- **Tests mobiles** : Teste les applications web mobiles avec émulation d'appareil
- **Captures d'écran et vidéos** : Capacités de tests visuels intégrées
- **Outils de débogage** : Débogage complet avec trace viewer

## Installation et configuration

### Installation de base

```bash
# Installer Playwright
npm init playwright@latest

# Ou ajouter à un projet existant
npm install -D @playwright/test

# Installer les navigateurs
npx playwright install
```

### Structure du projet
```
tests/
  example.spec.js
playwright.config.js
package.json
```

### Configuration (playwright.config.js)

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

## Écrire votre premier test

### Structure de test basique

```javascript
import { test, expect } from '@playwright/test';

test('exemple de test basique', async ({ page }) => {
  // Naviguer vers la page
  await page.goto('https://example.com');
  
  // Interagir avec les éléments
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // Assertions
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### Actions courantes

#### Navigation
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### Interactions avec les éléments
```javascript
// Cliquer sur des éléments
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// Remplir des formulaires
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// Cocher/décocher
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### Attentes et timeouts
```javascript
// Attendre des éléments
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// Attendre des conditions personnalisées
await page.waitForFunction(() => window.myApp.isReady);
```

## Patterns de test avancés

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

### Tests API
```javascript
test('API testing', async ({ request }) => {
  // Requête POST
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

### Mocking réseau
```javascript
test('mock API responses', async ({ page }) => {
  // Mock de réponse API
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### Tests visuels
```javascript
test('visual comparison', async ({ page }) => {
  await page.goto('/dashboard');
  
  // Capture d'écran complète
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // Capture d'écran d'élément
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## Organisation des tests et bonnes pratiques

### Hooks de test
```javascript
import { test, expect } from '@playwright/test';

test.describe('User Management', () => {
  test.beforeEach(async ({ page }) => {
    // Exécuter avant chaque test
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // Nettoyer après chaque test
    await page.evaluate(() => localStorage.clear());
  });

  test('should create new user', async ({ page }) => {
    // Implémentation du test
  });
});
```

### Fixtures et contexte de test
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // Login avant le test
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // Cleanup après le test
    await page.goto('/logout');
  },
});

// Dans le fichier de test
import { test, expect } from '../fixtures/auth';

test('authenticated user actions', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## Exécution des tests

### Options en ligne de commande
```bash
# Exécuter tous les tests
npx playwright test

# Exécuter un fichier de test spécifique
npx playwright test tests/login.spec.js

# Exécuter les tests en mode headed
npx playwright test --headed

# Exécuter les tests dans un navigateur spécifique
npx playwright test --project=firefox

# Exécuter les tests avec débogage
npx playwright test --debug

# Exécuter les tests en parallèle
npx playwright test --workers=4
```

### Rapports de test
```bash
# Générer un rapport HTML
npx playwright show-report

# Voir les fichiers trace
npx playwright show-trace trace.zip
```

## Playwright vs Selenium

### Différences d'architecture

| Fonctionnalité | Playwright | Selenium |
|---------|------------|----------|
| **Architecture** | Communication directe avec le navigateur | Protocole WebDriver |
| **Support navigateur** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge, IE |
| **Installation** | Package unique avec navigateurs | Téléchargements séparés des drivers |
| **Support langage** | JavaScript, Python, Java, C# | La plupart des langages de programmation |

### Comparaison de performance

**Avantages de Playwright :**
- **Exécution plus rapide** : La communication directe avec l'API du navigateur élimine la surcharge WebDriver
- **Parallèle par défaut** : Exécution parallèle des tests intégrée
- **Auto-wait** : Attente intelligente sans attentes explicites
- **Contrôle réseau** : Interception requête/réponse intégrée

**Avantages de Selenium :**
- **Écosystème mature** : Communauté étendue et outils tiers
- **Flexibilité langage** : Support de plus de langages de programmation
- **Couverture navigateur** : Support des anciens navigateurs comme Internet Explorer
- **Standard industriel** : Large adoption avec documentation étendue

### Comparaison des fonctionnalités

#### Fiabilité des tests
```javascript
// Playwright - Auto-wait intégré
await page.click('button'); // Attend que l'élément soit cliquable

// Selenium - Attentes manuelles requises
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### Tests mobiles
```javascript
// Playwright - Émulation mobile intégrée
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - Requiert une configuration supplémentaire
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### Gestion réseau
```javascript
// Playwright - Interception réseau native
await page.route('**/api/**', route => route.abort());

// Selenium - Requiert une configuration proxy
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```

### Considérations de migration

**Quand choisir Playwright :**
- Nouveaux projets ou applications greenfield
- Applications web modernes avec architecture SPA
- Besoin d'une exécution de tests rapide et fiable
- L'équipe utilise principalement JavaScript/TypeScript
- Exigence de tests visuels intégrés

**Quand rester avec Selenium :**
- Grandes suites de tests existantes
- Besoin de combinaisons spécifiques navigateur/OS
- Expertise de l'équipe dans des langages non-JavaScript
- Intégration avec des pipelines CI/CD existants
- Tests d'applications legacy

### Exemple de comparaison de code

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

## Conclusion

Playwright représente une approche moderne des tests end-to-end avec des avantages significatifs en vitesse, fiabilité et expérience développeur. Bien que Selenium reste un choix solide pour les projets établis et des cas d'utilisation spécifiques, l'architecture et l'ensemble de fonctionnalités de Playwright le rendent particulièrement adapté pour tester les applications web modernes. Le choix entre eux devrait être basé sur vos exigences de projet spécifiques, l'infrastructure existante et l'expertise de l'équipe.