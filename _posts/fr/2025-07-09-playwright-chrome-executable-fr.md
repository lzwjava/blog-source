---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Configuration de Playwright avec un exécutable Chrome spécifique
translated: true
type: note
---

Compris. Vous souhaitez configurer **Playwright** sur Windows pour qu'il lance un **exécutable Chrome spécifique** avec certaines **options de lancement** (comme `headless: true`) directement dans votre fichier `playwright.config.js`.

Voici comment procéder :

---

### 1. Utiliser `executablePath` dans votre configuration Playwright
Par défaut, Playwright utilise son Chromium intégré, mais si vous voulez **Google Chrome** (votre propre installation), vous devez indiquer à Playwright où se trouve le fichier `chrome.exe`.

Exemple de `playwright.config.js` :

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
        // Sur Windows, fournissez le chemin complet vers chrome.exe
        channel: undefined, // assurez-vous que channel n'est pas défini, car nous utiliserons executablePath
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // exécuter en mode headless
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

### 2. Notes
- Sur **Windows**, le chemin habituel de Chrome est :
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - ou `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- Assurez-vous d'**échapper les barres obliques inverses** (`\\`) dans les chaînes de caractères JS.
- Utilisez `headless: true` pour forcer le mode headless.
- Vous pouvez également passer des arguments en ligne de commande Chromium dans `args`.

---

### 3. Exécuter la configuration
Vous pouvez maintenant exécuter les tests avec :

```bash
npx playwright test --project="Google Chrome"
```

---

✅ Cela lancera votre **exécutable Chrome spécifique** en **mode headless** avec les arguments donnés.

---

Souhaitez-vous également que je vous montre comment **basculer conditionnellement** entre le Chromium intégré à Playwright et votre `chrome.exe` installé (par exemple, pour CI vs développement local) ?