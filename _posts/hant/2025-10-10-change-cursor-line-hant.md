---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 將 VS Code 游標更改為線條
translated: true
type: note
---

### 修復 VS Code 中的區塊（矩形）游標

明白了——看來你的游標切換成了區塊/矩形樣式（常見於覆寫模式或預設設定），但你想要細長的垂直**線條**樣式以便於編輯。這只需快速調整設定即可。請嚴格按照以下步驟操作：

#### 透過設定介面（最簡單）：
1. 開啟 VS Code。
2. 按下 `Ctrl + ,`（Windows/Linux）或 `Cmd + ,`（macOS）開啟設定。
3. 在頂部的搜尋框中輸入：**cursor style**。
4. 尋找 **Editor: Cursor Style**（位於 Text Editor > Cursor 下方）。
5. 點擊下拉選單並選擇 **Line**（目前可能顯示為 "Block"）。
6. 變更會立即生效——試著在檔案中輸入文字以查看細線游標。

若仍未更新，請關閉並重新開啟 VS Code，或完全重啟。

#### 透過 settings.json（精確設定）：
1. 開啟命令選擇區：`Ctrl + Shift + P`（macOS 為 `Cmd + Shift + P`）。
2. 輸入並選擇：**Preferences: Open User Settings (JSON)**。
3. 在 `{}` 內新增或更新此行（若為空則建立）：
   ```json:disable-run
   "editor.cursorStyle": "line"
   ```
4. 儲存檔案（`Ctrl + S` 或 `Cmd + S`）。

#### 額外提示：
- **覆寫模式？** 若你不慎進入「覆寫」模式（會遮蓋字元），請按下鍵盤上的 **Insert** 鍵切換回插入模式。
- **閃爍問題？** 若游標線條顯示不流暢，請在設定中搜尋 **cursor blinking** 並設為 **Blink** 或 **Smooth**。
- **擴充功能干擾？** 暫時停用 Vim 等擴充功能（擴充功能檢視 > 右鍵點擊 > Disable）進行測試。

這樣應該能立即恢復清晰的線條游標。若完成後仍是矩形樣式，請提供你的作業系統或截圖以獲得更針對性的協助！

[VS Code 游標文件](https://code.visualstudio.com/docs/editor/codebasics#_cursor-style)