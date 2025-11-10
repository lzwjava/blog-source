---
audio: false
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: 特定のChrome実行ファイルを使用したPlaywrightの設定
translated: true
type: note
---

了解しました。**Playwright** を Windows で設定し、特定の **Chrome 実行ファイル** を特定の **起動オプション**（例: `headless: true`）で直接 `playwright.config.js` から起動したいのですね。

以下の方法で実現できます：

---

### 1. Playwright 設定で `executablePath` を使用する
デフォルトでは Playwright は同梱の Chromium を使用しますが、**Google Chrome**（自身でインストールしたもの）を使用したい場合は、Playwright に `chrome.exe` ファイルの場所を伝える必要があります。

`playwright.config.js` の例：

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
        // Windows では、chrome.exe へのフルパスを指定します
        channel: undefined, // executablePath を使用するため、channel は未設定にします
        executablePath: 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        headless: true,  // ヘッドレスモードで実行
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

### 2. 注意点
- **Windows** では、通常の Chrome のパスは以下の通りです：
  - `C:\Program Files\Google\Chrome\Application\chrome.exe`
  - または `C:\Program Files (x86)\Google\Chrome\Application\chrome.exe`
- JS の文字列ではバックスラッシュをエスケープ (`\\`) することを忘れないでください。
- ヘッドレスモードを強制するには `headless: true` を使用します。
- `args` に Chromium の CLI フラグを追加できます。

---

### 3. 設定を実行する
以下のコマンドでテストを実行できます：

```bash
npx playwright test --project="Google Chrome"
```

---

✅ これで、指定した **Chrome 実行ファイル** が **ヘッドレスモード** と指定された引数で起動されます。

---

CI 環境とローカル開発環境などで、**条件付きで切り替え**（同梱の Playwright Chromium とインストール済みの `chrome.exe` の切り替え）を行う方法もご紹介しましょうか？