---
audio: false
generated: true
image: false
lang: hant
layout: post
model: openai/gpt-5
title: 設定 Playwright 使用指定 Chrome 執行檔
translated: true
type: note
---

瞭解。您想要在 Windows 上配置 **Playwright**，使其能在 `playwright.config.js` 中直接啟動**特定的 Chrome 執行檔**並帶有某些**啟動選項**（例如 `headless: true`）。  

做法如下：

---

### 1. 在 Playwright 配置中使用 `executablePath`
預設情況下，Playwright 使用其內建的 Chromium，但如果您想使用 **Google Chrome**（您自己安裝的版本），則必須告訴 Playwright `chrome.exe` 檔案的位置。

範例 `playwright.config.js`：

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
        // 在 Windows 上，提供 chrome.exe 的完整路徑
        channel: undefined, // 確保取消設定 channel，因為我們將使用 executablePath
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // 以無頭模式執行
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

### 2. 注意事項
- 在 **Windows** 上，Chrome 的通常路徑為：
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - 或 `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- 請確保在 JS 字串中**對反斜線進行轉義**（`\\`）。
- 使用 `headless: true` 來強制啟用無頭模式。
- 您也可以在 `args` 中傳遞任何 Chromium 命令行標記。

---

### 3. 執行配置
現在您可以使用以下指令執行測試：

```bash
npx playwright test --project="Google Chrome"
```

---

✅ 這將使用**特定的 Chrome 執行檔**，以**無頭模式**並帶有指定的參數來啟動。

---

您是否還想瞭解如何**根據條件切換**使用內建的 Playwright Chromium 與您安裝的 `chrome.exe`（例如用於 CI 與本地開發）？