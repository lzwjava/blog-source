---
audio: true
generated: true
lang: hant
layout: post
title: 啟用特定檔案副檔名的文字自動換行
translated: true
---

我假設你在問如何配置 Visual Studio Code (VS Code) 以便僅對特定的文件擴展名啟用自動換行。以下是如何實現的方法：

1. **打開 VS Code 設定**：
   - 按 `Ctrl + ,`（或在 macOS 上按 `Cmd + ,`）打開設定，或者前往 `File > Preferences > Settings`。

2. **使用 JSON 設定文件**：
   - 在設定界面中，點擊右上角的 `{}` 圖標打開 `settings.json` 文件。這樣可以更精細地控制設定。

3. **按文件類型配置自動換行**：
   - 使用 `"[filetype]": {}` 語法添加配置，以指定特定文件擴展名的設定。例如，要僅對 `.md`（Markdown）和 `.txt`（純文本）文件啟用自動換行，可以添加以下內容：

   ```json
   {
       "editor.wordWrap": "off", // 默認：所有文件不換行
       "[markdown]": {
           "editor.wordWrap": "on" // 僅對 .md 文件換行
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // 僅對 .txt 文件換行
       }
   }
   ```

4. **說明**：
   - `"editor.wordWrap": "off"` 將全局默認設置為不換行。
   - `"[markdown]"` 和 `"[plaintext]"` 是 Markdown 和純文本文件的語言識別符，可以根據你想要針對的文件擴展名替換為其他語言識別符，例如 `[javascript]`、`[python]` 等。
   - `"editor.wordWrap": "on"` 為這些特定文件類型啟用換行。

5. **查找語言識別符**：
   - 如果你不確定某個文件擴展名的語言識別符，可以在 VS Code 中打開該類型的文件，點擊右下角的語言模式（例如 "Plain Text" 或 "Python"），並在選擇語言時注意命令面板中顯示的識別符。

6. **保存並測試**：
   - 保存 `settings.json` 文件，VS Code 會立即應用這些設定。打開不同擴展名的文件以確認行為。

這種方法確保自動換行僅對你指定的文件類型啟用，其他文件不受影響。如果你需要幫助處理特定擴展名，請告訴我！

---

如果你在 Visual Studio Code 中處理 `.log` 文件並希望僅對它們啟用自動換行，你需要確保 VS Code 將這些文件識別為獨特的語言模式。默認情況下，`.log` 文件可能沒有像 `[log]` 這樣的獨特語言識別符——它們通常被視為純文本（`[plaintext]`）。然而，你可以配置這種行為。以下是如何處理的方法：

### 選項 1：使用 `[plaintext]` 如果 `.log` 文件是純文本
如果你的 `.log` 文件被識別為純文本（在 VS Code 右下角打開 `.log` 文件時檢查語言模式），可以簡單地使用 `[plaintext]`：

```json
{
    "editor.wordWrap": "off", // 默認：不換行
    "[plaintext]": {
        "editor.wordWrap": "on" // 為 .txt 和 .log 文件（如果被識別為純文本）啟用換行
    }
}
```

- **注意**：這將應用於所有純文本文件（例如 `.txt`、`.log`），而不僅僅是 `.log` 文件。如果這樣太廣泛，請參考選項 2。

### 選項 2：將 `.log` 文件與自定義語言模式關聯
如果你希望 `[log]` 作為特定識別符，需要告訴 VS Code 將 `.log` 文件與 "Log" 語言模式關聯。以下是如何操作的：

1. **安裝日誌文件擴展（可選）**：
   - 從 VS Code Marketplace 安裝像 "Log File Highlighter" 這樣的擴展。這個擴展通常將 `.log` 文件分配給特定語言模式（例如 `log`）。
   - 安裝後，檢查 `.log` 文件的語言模式（右下角）。如果顯示 "Log" 或類似，可以直接使用 `[log]`。

2. **手動關聯 `.log` 文件**：
   - 如果不想安裝擴展，可以通過 `files.associations` 在 `settings.json` 中手動將 `.log` 關聯到語言模式：
   ```json
   {
       "files.associations": {
           "*.log": "log" // 將 .log 關聯到 "log" 語言模式
       },
       "editor.wordWrap": "off", // 默認：不換行
       "[log]": {
           "editor.wordWrap": "on" // 僅對 .log 文件啟用換行
       }
   }
   ```
   - **注意**：`log` 語言模式必須存在（例如由擴展或 VS Code 提供）。如果不存在，VS Code 可能會回退到純文本，`[log]` 可能無法按預期工作。

3. **驗證語言模式**：
   - 打開一個 `.log` 文件，點擊右下角的語言模式，查看它的設置。如果是 `log`，`[log]` 將有效。如果仍然是 `plaintext`，使用 `[plaintext]` 或調整關聯。

### 選項 3：使用文件模式進行精細調整（最精確）
為了獲得最終控制，可以使用 `"files.associations"` 設定來特定針對 `.log` 文件，然後依賴於像 `plaintext` 這樣的回退語言模式：

```json
{
    "files.associations": {
        "*.log": "plaintext" // 強制 .log 文件被視為純文本
    },
    "editor.wordWrap": "off", // 默認：不換行
    "[plaintext]": {
        "editor.wordWrap": "on" // 為 .log（和 .txt，如果需要）啟用換行
    }
}
```

- **排除 `.txt`**：如果你想要 `.log` 但不想要 `.txt` 換行，你需要一個自定義擴展或更高級的設置（例如 VS Code 擴展來定義獨特的 `log` 模式），因為 VS Code 默認情況下無法區分 `.log` 和 `.txt` 而不進行額外配置。

### 測試 `[log]` 直接
如果你不確定 `[log]` 是否直接有效（由於擴展或 VS Code 的內建行為），可以嘗試這個：

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

打開一個 `.log` 文件，查看是否應用了換行。如果沒有，語言模式不是 `log`，你需要使用上述選項之一。

### 推薦
- **最簡單**：如果你對 `.txt` 和 `.log` 都換行沒問題，使用 `[plaintext]`。
- **特定**：安裝 "Log File Highlighter" 擴展，確認模式是 `log`，然後使用 `[log]`。
- 讓我知道你的 `.log` 文件顯示的語言模式，我可以進一步完善解決方案！

---

我測試了以下配置，效果很好。

```json
   {
       "editor.wordWrap": "off", // 默認：不換行
       "[log]": {
           "editor.wordWrap": "on" // 僅對 .log 文件啟用換行
       }
   }
```