---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Konfiguration von Playwright mit spezifischer Chrome-Executable
translated: true
type: note
---

Verstanden. Sie möchten **Playwright** unter Windows so konfigurieren, dass es eine **bestimmte Chrome-Executable** mit bestimmten **Launch-Optionen** (wie `headless: true`) direkt in Ihrer `playwright.config.js` startet.

So können Sie das machen:

---

### 1. Verwenden Sie `executablePath` in Ihrer Playwright-Konfiguration
Standardmäßig verwendet Playwright sein gebündeltes Chromium. Wenn Sie jedoch **Google Chrome** (Ihre eigene Installation) verwenden möchten, müssen Sie Playwright mitteilen, wo sich die `chrome.exe` befindet.

Beispiel `playwright.config.js`:

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
        // Unter Windows geben Sie den vollständigen Pfad zur chrome.exe an
        channel: undefined, // Stellen Sie sicher, dass channel nicht gesetzt ist, da wir executablePath verwenden
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // Führe im Headless-Modus aus
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

### 2. Hinweise
- Unter **Windows** ist der übliche Chrome-Pfad:
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - oder `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- Denken Sie daran, **Backslashes** (`\\`) in JS-Strings zu escapen.
- Verwenden Sie `headless: true`, um den Headless-Modus zu erzwingen.
- Sie können auch beliebige Chromium-CLI-Flags in `args` übergeben.

---

### 3. Führen Sie die Konfiguration aus
Sie können Tests jetzt mit folgendem Befehl ausführen:

```bash
npx playwright test --project="Google Chrome"
```

---

✅ Dadurch wird Ihre **spezifische Chrome-Executable** im **Headless-Modus** mit den angegebenen Argumenten gestartet.

---

Möchten Sie auch, dass ich Ihnen zeige, wie man **bedingt zwischen** dem gebündelten Playwright Chromium und Ihrer installierten `chrome.exe` umschaltet (z. B. für CI vs. lokale Entwicklung)?