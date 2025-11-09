---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: 修復 VSCode 交叉游標問題
translated: true
type: note
---

在 VSCode 中，滑鼠游標變成十字/加號符號通常表示 VSCode 處於特殊模式或存在配置問題。以下是最常見的原因和解決方法：

## 常見原因：

1. **欄位選取模式**：您可能意外啟動了欄位/區塊選取模式
   - 嘗試按下 `Alt + Shift + I` 或 `Ctrl + Shift + Alt + 方向鍵` 來退出此模式

2. **擴充功能衝突**：某些擴充功能可能會改變游標行為
   - 嘗試暫時停用擴充功能：`Ctrl + Shift + P` → "Developer: Reload Window"
   - 或在安全模式中啟動 VSCode：`code --disable-extensions`

3. **縮放/選取工具**：您可能啟動了縮放或選取工具
   - 多次按下 `Escape` 鍵
   - 嘗試 `Ctrl + Z` 復原最近的操作

4. **終端機焦點問題**：若終端機處於焦點狀態，可能會改變游標行為
   - 點擊編輯器區域重新聚焦
   - 嘗試 `Ctrl + 1` 將焦點移至編輯器

## 快速修復：

1. **重新啟動 VSCode**：簡單但通常有效
   - `Ctrl + Shift + P` → "Developer: Reload Window"

2. **檢查滑鼠設定**：
   - 前往 File → Preferences → Settings
   - 搜尋 "cursor" 並檢查游標相關設定

3. **重設工作區**：
   - 關閉 VSCode
   - 刪除專案中的 `.vscode` 資料夾（如果存在）
   - 重新開啟專案

4. **檢查系統層面問題**：
   - 測試游標問題是否出現在其他應用程式中
   - 若出現，可能是 GNOME/系統設定問題

請先多次按下 `Escape` 鍵，然後重新啟動 VSCode。這通常能解決十字游標問題。