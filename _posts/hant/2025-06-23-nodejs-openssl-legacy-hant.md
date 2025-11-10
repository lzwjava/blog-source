---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Node.js OpenSSL 傳統供應程式標記
translated: true
type: note
---

### 理解問題
Node.js 16（及更早版本）使用 OpenSSL 1.x，而 Node.js 22 引入了 OpenSSL 3.x，其安全性預設更為嚴格。這可能會導致某些應用程式出現錯誤，特別是依賴舊版加密供應商或已棄用演算法（例如 MD4 雜湊）的應用程式。`--openssl-legacy-provider` 旗標能暫時啟用與 OpenSSL 1.x 行為的相容性，以便在升級期間修復這些問題。

**注意**：此旗標為臨時解決方案，可能在未來的 Node.js 版本中被移除。它最適合用於短期修復——請盡可能更新您的程式碼以使用現代的 OpenSSL 3.x API。

### 如何使用此旗標
您可以在直接執行 Node.js 或透過 npm/yarn 指令碼時應用此旗標。這是一個執行時選項，而非永久配置。

#### 用於直接 Node 指令
在您的指令碼或指令前添加此旗標。範例：
- 基本指令碼執行：`node --openssl-legacy-provider app.js`
- REPL（互動模式）：`node --openssl-legacy-provider`
- 若執行模組：`node --openssl-legacy-provider --input-type=module index.mjs`
- 帶有其他旗標：`node --openssl-legacy-provider --max-old-space-size=4096 script.js`

這將啟用舊版供應商支援，避免常見錯誤，例如「digital envelope routines unsupported」（與過時的雜湊或加密方式相關）。

#### 用於 npm/Yarn 指令碼
修改您的 `package.json` 中的 `"scripts"` 部分，在相關指令中包含此旗標。範例：
```json
{
  "scripts": {
    "start": "node --openssl-legacy-provider app.js",
    "dev": "node --openssl-legacy-provider --watch app.js"
  }
}
```
然後照常執行：`npm start` 或 `yarn dev`。

若使用如 nodemon 或 vite 這類會衍生 Node 程序的工具，請在其配置中預先添加此旗標（例如，在 nodemon.json 中：`"exec": "node --openssl-legacy-provider"`）。

#### 用於全域指令（例如透過 nvm 或系統 Node）
若您使用 nvm 管理 Node 版本，請切換至 Node 22 並按照所示方式在指令中加入此旗標執行。對於 Docker 或 CI/CD，請將其加入您的執行指令碼中（例如 `CMD ["node", "--openssl-legacy-provider", "app.js"]`）。

### 疑難排解與替代方案
- **驗證旗標是否生效**：執行 `node --openssl-legacy-provider --version`——它應能無錯誤地輸出 Node 22 的版本。
- **已修復的常見問題**：與 `require()` 加密模組、webpack 構建或應用程式啟動相關的錯誤。若問題持續，請檢查是否有 OpenSSL 特定程式碼（例如，使用 `crypto.createCipher` 的替代方案，如 `crypto.createCipheriv`）。
- **長期解決方案**：掃描已棄用的加密使用情況（使用如 ESLint 插件等工具），並更新至與 OpenSSL 3.x 相容的方法。Node 22 文件推薦使用如 `bcrypt` 或 `crypto.scrypt` 等函式庫進行雜湊處理。
- **效能/相容性注意事項**：舊版供應商模式可能會輕微影響安全性/功能，但在遷移期間有所幫助。請徹底測試，因為某些 OpenSSL 3 功能（例如增強的熵源）將無法使用。

更多詳細資訊，請參閱 nodejs.org/api/crypto.html 上的 Node.js OpenSSL 文件。若您分享具體的錯誤訊息，我可以提供更具針對性的建議！