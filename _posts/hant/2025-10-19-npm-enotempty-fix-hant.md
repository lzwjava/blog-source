---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 npm ENOTEMPTY 安裝錯誤
translated: true
type: note
---

### 理解錯誤原因

你的 `sudo npm i -g @anthropic-ai/claude-code --verbose` 指令在安裝過程中因 `ENOTEMPTY` 錯誤而失敗。這是 npm 常見問題，通常發生在 npm 嘗試重新命名（或移動）現有目錄作為更新或重新安裝套件的一部分時，但該目錄並非空目錄。此案例中，具體是無法將 `/usr/lib/node_modules/@anthropic-ai/claude-code` 重新命名至暫存備份位置（`/usr/lib/node_modules/@anthropic-ai/.claude-code-ZjqcDZyQ`）。

這通常由以下原因引起：
- 先前不完整或中斷的安裝遺留了檔案或子目錄
- 其他行程的檔案鎖定（例如套件被部分載入或其他 npm 指令正在執行）
- 極少情況下，使用 `sudo` 進行全域安裝時的權限異常

該套件本身（`@anthropic-ai/claude-code`）是正規的——它是 Anthropic 官方的 CLI 工具，用於「Claude Code」，這是一個能整合至終端機與程式碼庫的主動式編碼助手。

### 快速修復方法

請依序嘗試以下步驟。由於這是全域安裝，請在需要時使用 root 權限或 `sudo` 執行。

1. **手動移除現有目錄**  
   這能清除有問題的不完整安裝：  
   ```
   sudo rm -rf /usr/lib/node_modules/@anthropic-ai/claude-code
   ```  
   - 若上層作用域目錄（`@anthropic-ai`）現在已空，可一併移除：  
     ```
     sudo rm -rf /usr/lib/node_modules/@anthropic-ai
     ```  
   接著重試原始指令：  
   ```
   sudo npm i -g @anthropic-ai/claude-code --verbose
   ```

2. **清除 npm 快取**  
   若上述方法無效，可能是快取資料損毀：  
   ```
   sudo npm cache clean --force
   sudo npm cache verify
   ```  
   完成後重新嘗試安裝。

3. **檢查執行中的行程**  
   確認沒有其他 npm/Node 行程正在使用該目錄：  
   ```
   ps aux | grep npm
   ```  
   如有殘留行程請終止（例如 `sudo kill <PID>`），然後重試。

4. **替代方案：使用 npx 測試**  
   若只想測試工具而不進行完整全域安裝，可嘗試：  
   ```
   npx @anthropic-ai/claude-code --help
   ```  
   這會暫時下載並執行，不會修改全域模組。

### 補充建議
- **權限最佳實踐**：使用 `sudo` 進行全域安裝可能導致後續擁有權問題。建議使用 node 版本管理器如 `nvm` 來完全避免 `sudo`，或設定自訂全域前綴：  
  ```
  mkdir ~/.npm-global
  npm config set prefix '~/.npm-global'
  export PATH=~/.npm-global/bin:$PATH
  ```  
  之後即可無需 `sudo` 進行安裝。
- **安裝後驗證**：安裝完成後，請透過 `claude-code --version` 檢查（請確認二進位檔名稱是否符合文件說明）。
- 若問題持續，請提供 `npm ls -g @anthropic-ai/claude-code` 的輸出以獲取進一步診斷資訊。

這些步驟應能助你快速恢復正常。若再遇阻礙，請貼上新的紀錄！

[Claude Code on npm](https://www.npmjs.com/package/@anthropic-ai/claude-code)  
[Anthropic Docs: Set up Claude Code](https://docs.claude.com/en/docs/claude-code/setup)