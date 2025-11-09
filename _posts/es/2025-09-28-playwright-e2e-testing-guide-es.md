---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-sonnet-4
title: Guía de Pruebas Integrales de Playwright
translated: true
type: note
---

## ¿Qué es Playwright?

Playwright es un framework moderno de pruebas end-to-end desarrollado por Microsoft que permite realizar pruebas confiables de aplicaciones web en múltiples navegadores (Chromium, Firefox y WebKit). Proporciona una API unificada para automatizar páginas web y está diseñado para manejar los desafíos de las aplicaciones web modernas como single-page applications, contenido dinámico e interacciones de usuario complejas.

## Características Principales

- **Pruebas multi-navegador**: Soporta Chromium, Firefox y WebKit
- **Ejecución rápida**: Ejecuta pruebas en paralelo por defecto
- **Auto-wait**: Espera automáticamente a que los elementos estén listos
- **Interceptación de red**: Mock APIs y captura de solicitudes de red
- **Pruebas móviles**: Prueba aplicaciones web móviles con emulación de dispositivos
- **Capturas de pantalla y videos**: Capacidades integradas de pruebas visuales
- **Herramientas de debugging**: Depuración integral con visor de trazas

## Instalación y Configuración

### Instalación Básica

```bash
# Instalar Playwright
npm init playwright@latest

# O agregar a proyecto existente
npm install -D @playwright/test

# Instalar navegadores
npx playwright install
```

### Estructura del Proyecto
```
tests/
  example.spec.js
playwright.config.js
package.json
```

### Configuración (playwright.config.js)

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

## Escribiendo Tu Primera Prueba

### Estructura Básica de Prueba

```javascript
import { test, expect } from '@playwright/test';

test('ejemplo de prueba básica', async ({ page }) => {
  // Navegar a la página
  await page.goto('https://example.com');
  
  // Interactuar con elementos
  await page.click('button');
  await page.fill('input[name="username"]', 'testuser');
  
  // Aserciones
  await expect(page.locator('h1')).toHaveText('Welcome');
  await expect(page).toHaveURL(/dashboard/);
});
```

### Acciones Comunes

#### Navegación
```javascript
await page.goto('https://example.com');
await page.goBack();
await page.goForward();
await page.reload();
```

#### Interacciones con Elementos
```javascript
// Hacer clic en elementos
await page.click('button');
await page.click('text=Submit');
await page.click('#login-btn');

// Llenar formularios
await page.fill('input[name="email"]', 'user@example.com');
await page.type('textarea', 'Hello world');
await page.selectOption('select', 'option-value');

// Check/uncheck
await page.check('input[type="checkbox"]');
await page.uncheck('input[type="checkbox"]');
```

#### Esperas y Timeouts
```javascript
// Esperar elementos
await page.waitForSelector('.loading-spinner', { state: 'hidden' });
await page.waitForURL('**/dashboard');
await page.waitForResponse('**/api/users');

// Esperar condiciones personalizadas
await page.waitForFunction(() => window.myApp.isReady);
```

## Patrones Avanzados de Pruebas

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

test('usuario puede iniciar sesión', async ({ page }) => {
  const loginPage = new LoginPage(page);
  await page.goto('/login');
  await loginPage.login('user@example.com', 'password123');
  await expect(page).toHaveURL('/dashboard');
});
```

### Pruebas de API
```javascript
test('pruebas de API', async ({ request }) => {
  // Solicitud POST
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

### Mocking de Red
```javascript
test('mock respuestas de API', async ({ page }) => {
  // Mock respuesta de API
  await page.route('**/api/users', async route => {
    const json = [{ id: 1, name: 'Mock User' }];
    await route.fulfill({ json });
  });
  
  await page.goto('/users');
  await expect(page.locator('.user-name')).toHaveText('Mock User');
});
```

### Pruebas Visuales
```javascript
test('comparación visual', async ({ page }) => {
  await page.goto('/dashboard');
  
  // Captura de pantalla completa
  await expect(page).toHaveScreenshot('dashboard.png');
  
  // Captura de elemento
  await expect(page.locator('.header')).toHaveScreenshot('header.png');
});
```

## Organización de Pruebas y Mejores Prácticas

### Hooks de Prueba
```javascript
import { test, expect } from '@playwright/test';

test.describe('Gestión de Usuarios', () => {
  test.beforeEach(async ({ page }) => {
    // Ejecutar antes de cada prueba
    await page.goto('/login');
    await page.fill('[name="email"]', 'admin@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
  });

  test.afterEach(async ({ page }) => {
    // Limpiar después de cada prueba
    await page.evaluate(() => localStorage.clear());
  });

  test('debería crear nuevo usuario', async ({ page }) => {
    // Implementación de prueba
  });
});
```

### Fixtures y Contexto de Prueba
```javascript
// fixtures/auth.js
import { test as base } from '@playwright/test';

export const test = base.extend({
  authenticatedPage: async ({ page }, use) => {
    // Login antes de la prueba
    await page.goto('/login');
    await page.fill('[name="email"]', 'user@example.com');
    await page.fill('[name="password"]', 'password');
    await page.click('button[type="submit"]');
    await page.waitForURL('/dashboard');
    
    await use(page);
    
    // Limpieza después de la prueba
    await page.goto('/logout');
  },
});

// En archivo de prueba
import { test, expect } from '../fixtures/auth';

test('acciones de usuario autenticado', async ({ authenticatedPage }) => {
  await expect(authenticatedPage.locator('.welcome')).toBeVisible();
});
```

## Ejecutando Pruebas

### Opciones de Línea de Comandos
```bash
# Ejecutar todas las pruebas
npx playwright test

# Ejecutar archivo de prueba específico
npx playwright test tests/login.spec.js

# Ejecutar pruebas en modo headed
npx playwright test --headed

# Ejecutar pruebas en navegador específico
npx playwright test --project=firefox

# Ejecutar pruebas con debugging
npx playwright test --debug

# Ejecutar pruebas en paralelo
npx playwright test --workers=4
```

### Reportes de Pruebas
```bash
# Generar reporte HTML
npx playwright show-report

# Ver archivos de traza
npx playwright show-trace trace.zip
```

## Playwright vs Selenium

### Diferencias de Arquitectura

| Característica | Playwright | Selenium |
|---------|------------|----------|
| **Arquitectura** | Comunicación directa con navegador | Protocolo WebDriver |
| **Soporte de Navegadores** | Chromium, Firefox, WebKit | Chrome, Firefox, Safari, Edge, IE |
| **Instalación** | Paquete único con navegadores | Descargas separadas de drivers |
| **Soporte de Lenguajes** | JavaScript, Python, Java, C# | La mayoría de lenguajes de programación |

### Comparación de Rendimiento

**Ventajas de Playwright:**
- **Ejecución más rápida**: La comunicación directa con la API del navegador elimina la sobrecarga de WebDriver
- **Paralelo por defecto**: Ejecución de pruebas paralela integrada
- **Auto-wait**: Espera inteligente sin waits explícitos
- **Control de red**: Interceptación integrada de solicitudes/respuestas

**Ventajas de Selenium:**
- **Ecosistema maduro**: Comunidad extensa y herramientas de terceros
- **Flexibilidad de lenguajes**: Soporte para más lenguajes de programación
- **Cobertura de navegadores**: Soporta navegadores antiguos como Internet Explorer
- **Estándar de la industria**: Ampliamente adoptado con documentación extensa

### Comparación de Características

#### Confiabilidad de Pruebas
```javascript
// Playwright - Auto-wait integrado
await page.click('button'); // Espera que el elemento sea clickeable

// Selenium - Esperas manuales requeridas
await driver.wait(until.elementIsVisible(button));
await driver.wait(until.elementToBeClickable(button));
await button.click();
```

#### Pruebas Móviles
```javascript
// Playwright - Emulación móvil integrada
const context = await browser.newContext({
  ...devices['iPhone 13']
});

// Selenium - Requiere configuración adicional
const options = new chrome.Options();
options.addArguments('--user-agent=iPhone...');
```

#### Manejo de Red
```javascript
// Playwright - Interceptación nativa de red
await page.route('**/api/**', route => route.abort());

// Selenium - Requiere configuración de proxy
const proxy = new Proxy();
proxy.setHttpProxy('localhost:8080');
```

### Consideraciones de Migración

**Cuándo Elegir Playwright:**
- Proyectos nuevos o aplicaciones greenfield
- Aplicaciones web modernas con arquitectura SPA
- Necesidad de ejecución de pruebas rápida y confiable
- Equipo que usa principalmente JavaScript/TypeScript
- Requerimiento de pruebas visuales integradas

**Cuándo Mantenerse con Selenium:**
- Suites de pruebas existentes grandes
- Necesidad de combinaciones específicas de navegador/OS
- Experiencia del equipo en lenguajes no JavaScript
- Integración con pipelines CI/CD existentes
- Pruebas de aplicaciones legacy

### Ejemplo de Comparación de Código

```javascript
// Playwright
import { test, expect } from '@playwright/test';

test('flujo de login', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[name="email"]', 'user@example.com');
  await page.fill('[name="password"]', 'password');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
});

// Selenium (JavaScript)
const { Builder, By, until } = require('selenium-webdriver');

describe('flujo de login', () => {
  let driver;
  
  beforeEach(async () => {
    driver = await new Builder().forBrowser('chrome').build();
  });
  
  afterEach(async () => {
    await driver.quit();
  });
  
  it('debería iniciar sesión exitosamente', async () => {
    await driver.get('http://localhost:3000/login');
    await driver.findElement(By.name('email')).sendKeys('user@example.com');
    await driver.findElement(By.name('password')).sendKeys('password');
    await driver.findElement(By.css('button[type="submit"]')).click();
    await driver.wait(until.urlContains('/dashboard'));
  });
});
```

## Conclusión

Playwright representa un enfoque moderno para pruebas end-to-end con ventajas significativas en velocidad, confiabilidad y experiencia del desarrollador. Mientras Selenium sigue siendo una opción sólida para proyectos establecidos y casos de uso específicos, la arquitectura y conjunto de características de Playwright lo hacen particularmente adecuado para probar aplicaciones web modernas. La elección entre ellos debe basarse en los requisitos específicos de tu proyecto, infraestructura existente y experiencia del equipo.