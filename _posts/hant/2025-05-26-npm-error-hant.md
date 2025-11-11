---
audio: false
generated: true
lang: hant
layout: post
title: 解決 npm ENOTEMPTY 錯誤
translated: true
type: note
---

npm 中的 `ENOTEMPTY` 錯誤發生於嘗試重新命名目錄時（此例為 `/opt/homebrew/lib/node_modules/@anthropic-ai/claude-code` 重新命名為 `/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V`），但目標目錄非空目錄。這通常發生在套件安裝或更新過程中，因現有檔案導致 npm 無法覆寫或移動目錄。

### 解決步驟

1. **清除 npm 快取**：
   執行以下指令清除 npm 快取，可解決因損毀或過時快取資料導致的問題：
   ```bash
   npm cache clean --force
   ```

2. **移除問題目錄**：
   錯誤指向 `@anthropic-ai/claude-code` 目錄。手動刪除以確保無殘留衝突檔案：
   ```bash
   rm -rf /opt/homebrew/lib/node_modules/@anthropic-ai/claude-code
   ```

3. **檢查部分安裝檔案**：
   同時檢查錯誤中提到的暫存目錄 (`/opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V`) 並移除：
   ```bash
   rm -rf /opt/homebrew/lib/node_modules/@anthropic-ai/.claude-code-2DTsDk1V
   ```

4. **重新安裝套件**：
   清除問題目錄後，嘗試重新安裝套件：
   ```bash
   npm install
   ```

5. **檢查權限**：
   錯誤可能因權限不足導致。請確保對 `/opt/homebrew/lib/node_modules` 具寫入權限。若無，請調整權限或使用 `sudo`：
   ```bash
   sudo npm install
   ```
   或修正權限：
   ```bash
   sudo chown -R $(whoami):admin /opt/homebrew/lib/node_modules
   ```

6. **檢視除錯記錄**：
   檢查 `/Users/lzwjava/.npm/_logs/2025-05-25T19_07_29_589Z-debug-0.log` 記錄檔獲取詳細資訊。可透過以下指令檢視：
   ```bash
   cat /Users/lzwjava/.npm/_logs/2025-05-25T19_07_29_589Z-debug-0.log
   ```
   從中尋找關於衝突檔案或程序的額外線索。

7. **更新 npm**：
   確保使用最新版 npm 以避免舊版錯誤：
   ```bash
   npm install -g npm@latest
   ```

8. **檢查執行中程序**：
   有時執行中的程序會鎖定目錄。請確認無其他 npm 程序正在執行：
   ```bash
   ps aux | grep npm
   ```
   若發現 npm 程序正在執行，請終止它們：
   ```bash
   kill -9 <process-id>
   ```

9. **嘗試全新安裝**：
   若問題持續，可考慮移除整個 `node_modules` 目錄與 `package-lock.json` 檔案，然後重新安裝依賴項：
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```

### 補充說明
- 若使用如 `@anthropic-ai/claude-code` 的套件，請確認其與 Node.js 及 npm 版本相容
- 若問題重複出現，請檢查磁碟空間問題或檔案系統損毀
- 若使用 macOS（如 `/opt/homebrew` 路徑所示），請確保 Homebrew 為最新版本：`brew update` 與 `brew upgrade`

若以上步驟未能解決問題，請分享除錯記錄中的相關細節或關於套件與執行指令的具體背景資訊。