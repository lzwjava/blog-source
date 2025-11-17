---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 停用 VS Code 覆寫模式
translated: true
type: note
---

在 Visual Studio Code 中，預設行為是**插入模式**（輸入文字時會將現有文字向後推移）。  
當您按下鍵盤上的 **Insert** 鍵時，會啟動**取代模式**（輸入文字會直接覆蓋現有文字）——這可在插入模式與取代/覆寫模式之間切換。

### 如何從取代（覆寫）模式切換回插入模式

1. 只需按下鍵盤上的 **Insert** 鍵一次。  
   → 右下角的狀態列會從 **OVR**（覆寫）變為 **INS**（插入）。

### 如果您希望完全避免意外進入覆寫模式

您可以完全停用 Insert 鍵的切換功能：

#### 方法 1：鍵盤快捷鍵（推薦）
按下 `Ctrl + Shift + P` → 輸入 **"Toggle Insert/Overwrite"** → 您會看到指令  
`Preferences: Toggle Insert on Paste and Overtype` 或類似選項。  
更可靠的方法是使用以下直接設定：

#### 方法 2：將以下內容新增至您的 `settings.json`
```json
// 停用 Insert 鍵切換覆寫模式的功能
"editor.occurencesHighlight": true,
"editor.overtypeMode": false,

// 這是關鍵設定：
"keyboard.dispatch": "keyCode"
```

實際上最常用且最有效的解決方案：

```json
// 在 VS Code 中完全停用 Insert 鍵
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite",
    "when": "editorTextFocus"
}
```

或直接全域關閉覆寫模式：

```json
"editor.occurrencesHighlight": true,
"editor.overwriteMode": false   // 此設定不存在，可忽略

// 停用覆寫切換的實際設定：
"editor.insertSpaces": true,  // 無關設定

// 正確方式：
{
    "key": "insert",
    "command": "noop"   // 或移除預設綁定
}
```

#### 最簡單的永久解決方案（多數人使用此方法）：
1. 開啟設定（`Ctrl + ,`）
2. 搜尋 **"overwrite"**
3. 取消勾選 **Editor: Overtype**（如果存在）或更好的做法：
4. 將此行新增至您的 `settings.json`（Ctrl + Shift + P → "Preferences: Open Settings (JSON)"）：

```json
// 完全停用 Insert 鍵切換覆寫模式的功能
{
    "key": "insert",
    "command": "-editor.action.toggleOverwrite"
}
```

新增此設定後，Insert 鍵在 VS Code 中將無任何作用，您會始終保持在插入模式。

這是開發者最常使用且最可靠的解決方案，特別適用於經常意外觸碰 Insert 鍵的情況（尤其是在台灣/亞洲地區使用小型鍵盤的筆記型電腦用戶，Insert 鍵很容易被誤觸）。

如果您使用的是 macOS（使用不同按鍵）或需要狀態列點擊解決方案，請告訴我！