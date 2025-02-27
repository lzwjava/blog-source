---
audio: false
lang: hant
layout: post
title: 啟用特定檔案副檔名的自動換行
translated: true
---

我假設你在問如何配置 Visual Studio Code (VS Code) 以便僅對特定的檔案擴展名啟用自動換行。以下是如何實現的方法：

1. **打開 VS Code 設定**：
   - 按 `Ctrl + ,`（或 macOS 上的 `Cmd + ,`）打開設定，或前往 `File > Preferences > Settings`。

2. **使用 JSON 設定檔**：
   - 在設定介面中，點擊右上角的 `{}` 圖標以打開 `settings.json` 檔案。這樣可以更精細地控制設定。

3. **依檔案類型配置自動換行**：
   - 使用 `"[filetype]": {}` 語法添加配置，以指定特定檔案擴展名的設定。例如，僅對 `.md`（Markdown）和 `.txt`（純文字）檔案啟用自動換行，可以添加如下內容：

   ```json
   {
       "editor.wordWrap": "off", // 默認：所有檔案不換行
       "[markdown]": {
           "editor.wordWrap": "on" // 僅對 .md 檔案換行
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // 僅對 .txt 檔案換行
       }
   }
   ```

4. **說明**：
   - `"editor.wordWrap": "off"` 將全域預設設為不換行。
   - `"[markdown]"` 和 `"[plaintext]"` 是 Markdown 和純文字檔案的語言識別碼，分別。你可以將它們替換為其他語言識別碼，例如 `[javascript]`、`[python]` 等，根據你想要針對的檔案擴展名。
   - `"editor.wordWrap": "on"` 為這些特定檔案類型啟用換行。

5. **查找語言識別碼**：
   - 如果你不確定某檔案擴展名的語言識別碼，可以在 VS Code 中打開該類型的檔案，點擊右下角的語言模式（例如 "Plain Text" 或 "Python"），並在選擇語言時的命令面板中注意顯示的識別碼。

6. **儲存並測試**：
   - 儲存 `settings.json` 檔案，VS Code 會立即應用這些設定。打開不同擴展名的檔案以確認行為。

這種方法確保自動換行僅對你指定的檔案類型啟用，其他檔案則不受影響。如果你需要幫助處理特定的擴展名，請告訴我！