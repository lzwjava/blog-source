---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Configuración de Playwright con un Ejecutable Específico de Chrome
translated: true
type: note
---

Entendido. Quieres configurar **Playwright** en Windows para que lance un **ejecutable específico de Chrome** con ciertas **opciones de lanzamiento** (como `headless: true`) directamente en tu `playwright.config.js`.

Aquí te mostramos cómo hacerlo:

---

### 1. Usa `executablePath` en tu configuración de Playwright
Por defecto, Playwright usa su Chromium incluido, pero si quieres **Google Chrome** (tu propia instalación), debes indicarle a Playwright dónde se encuentra el archivo `chrome.exe`.

Ejemplo de `playwright.config.js`:

```js
// playwright.config.js
import { defineConfig, devices } from '@playwright/test';
import path from 'path';

export default defineConfig({
  projects: [
    {
      name: 'Google Chrome',
      use: {
        browserName: 'chromium',
        // En Windows, proporciona la ruta completa a chrome.exe
        channel: undefined, // asegúrate de que channel no esté definido, ya que usaremos executablePath
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // ejecutar en modo headless
        args: [
          '--disable-gpu',
          '--no-sandbox',
          '--disable-dev-shm-usage',
        ],
      },
    },
  ],
});
```

---

### 2. Notas
- En **Windows**, la ruta habitual de Chrome es:
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - o `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- Asegúrate de **escapar las barras invertidas** (`\\`) en las cadenas de texto de JS.
- Usa `headless: true` para forzar el modo headless.
- También puedes pasar cualquier flag de línea de comandos de Chromium en `args`.

---

### 3. Ejecuta la configuración
Ahora puedes ejecutar las pruebas con:

```bash
npx playwright test --project="Google Chrome"
```

---

✅ Esto lanzará tu **ejecutable específico de Chrome** en **modo headless** con los argumentos proporcionados.

---

¿También quieres que te muestre cómo **cambiar condicionalmente** entre el Chromium incluido en Playwright y tu `chrome.exe` instalado (por ejemplo, para CI vs desarrollo local)?