---
audio: false
generated: true
lang: hant
layout: post
title: 為特定副檔名啟用自動換行
translated: true
type: note
---

我假設你想知道如何在 Visual Studio Code (VS Code) 中設定僅針對特定副檔名啟用自動換行功能。具體操作如下：

1. **開啟 VS Code 設定**：
   - 按下 `Ctrl + ,`（macOS 系統請按 `Cmd + ,`）開啟設定，或前往 `檔案 > 偏好設定 > 設定`。

2. **使用 JSON 設定檔案**：
   - 在設定介面中，點擊右上角的 `{}` 圖示開啟 `settings.json` 檔案，以便進行更精細的設定。

3. **依檔案類型設定換行功能**：
   - 使用 `"[檔案類型]": {}` 語法為特定副檔名設定選項。例如，若想僅對 `.md` (Markdown) 與 `.txt` (文字) 檔案啟用換行功能，可加入以下設定：

   ```json
   {
       "editor.wordWrap": "off", // 預設：所有檔案不換行
       "[markdown]": {
           "editor.wordWrap": "on" // 僅對 .md 檔案換行
       },
       "[plaintext]": {
           "editor.wordWrap": "on" // 僅對 .txt 檔案換行
       }
   }
   ```

4. **設定說明**：
   - `"editor.wordWrap": "off"` 將全域預設設為不換行。
   - `"[markdown]"` 與 `"[plaintext]"` 分別是 Markdown 與純文字檔案的語言識別碼。你可根據目標副檔名替換為其他語言識別碼（如 `[javascript]`、`[python]` 等）。
   - `"editor.wordWrap": "on"` 為指定檔案類型啟用換行功能。

5. **查詢語言識別碼**：
   - 若不確定某副檔名的語言識別碼，可在 VS Code 中開啟該類型檔案，點擊右下角的語言模式（如「Plain Text」或「Python」），在命令選擇區中查看顯示的識別碼。

6. **儲存並測試**：
   - 儲存 `settings.json` 檔案後，VS Code 會立即套用設定。請開啟不同副檔名的檔案驗證效果。

此方法可確保換行功能僅在你指定的檔案類型中啟用，其餘檔案則不受影響。如需特定副檔名的協助請隨時告知！

---

若你需要在 Visual Studio Code 中針對 `.log` 檔案啟用自動換行功能，必須確保 VS Code 能將此類檔案識別為獨立語言模式。預設情況下，`.log` 檔案可能沒有專屬的語言識別碼（如 `[log]`），通常會被視為純文字（`[plaintext]`）。以下是具體處理方式：

### 選項 1：若 `.log` 檔案被識別為純文字時使用 `[plaintext]`
若你的 `.log` 檔案被識別為純文字模式（請在開啟 `.log` 檔案時查看 VS Code 右下角的語言模式），可直接使用 `[plaintext]`：

```json
{
    "editor.wordWrap": "off", // 預設：不換行
    "[plaintext]": {
        "editor.wordWrap": "on" // 為 .txt 與 .log 檔案啟用換行（若被識別為純文字）
    }
}
```

- **注意**：此設定將套用至所有純文字檔案（如 `.txt`、`.log`）。若需更精準控制，請改用選項 2。

### 選項 2：將 `.log` 檔案關聯至自訂語言模式
若想使用 `[log]` 作為專屬識別碼，需透過以下步驟讓 VS Code 將 `.log` 檔案與「Log」語言模式建立關聯：

1. **安裝日誌檔案擴充功能（可選）**：
   - 從 VS Code Marketplace 安裝如 "Log File Highlighter" 的擴充功能，這類擴充通常會為 `.log` 檔案指定專屬語言模式（如 `log`）。
   - 安裝後請檢查 `.log` 檔案的語言模式（右下角）。若顯示「Log」或類似標識，即可直接使用 `[log]`。

2. **手動建立 `.log` 檔案關聯**：
   - 若不想安裝擴充功能，可透過 `settings.json` 中的 `files.associations` 手動設定關聯：
   ```json
   {
       "files.associations": {
           "*.log": "log" // 將 .log 檔案與 "log" 語言模式建立關聯
       },
       "editor.wordWrap": "off", // 預設：不換行
       "[log]": {
           "editor.wordWrap": "on" // 僅對 .log 檔案啟用換行
       }
   }
   ```
   - **注意**：`log` 語言模式必須存在（由擴充功能或 VS Code 內建提供）。若不存在，VS Code 可能會退回純文字模式，此時需進一步設定才能讓 `[log]` 生效。

3. **驗證語言模式**：
   - 開啟 `.log` 檔案並查看右下角的語言模式。若設定後顯示為 `log`，則 `[log]` 會生效；若仍顯示 `plaintext`，請改用 `[plaintext]` 或調整關聯設定。

### 選項 3：透過檔案模式精準控制（最精確）**
若要完全掌控，可透過 `"files.associations"` 設定專門針對 `.log` 檔案，並使其沿用 `plaintext` 語言模式：

```json
{
    "files.associations": {
        "*.log": "plaintext" // 強制將 .log 檔案視為純文字
    },
    "editor.wordWrap": "off", // 預設：不換行
    "[plaintext]": {
        "editor.wordWrap": "on" // 為 .log（及 .txt）檔案啟用換行
    }
}
```

- **排除 `.txt` 檔案**：若想僅對 `.log` 啟用換行而非 `.txt`，需透過自訂擴充功能或進階設定（例如定義專屬 `log` 模式），因為 VS Code 在未額外設定的情況下無法原生區分 `.log` 與 `.txt`。

### 直接測試 `[log]` 模式
若不確定 `[log]` 是否能直接生效（因擴充功能或 VS Code 內建行為），可嘗試以下設定：

```json
{
    "editor.wordWrap": "off",
    "[log]": {
        "editor.wordWrap": "on"
    }
}
```

開啟 `.log` 檔案觀察換行是否生效。若未生效，表示語言模式並非 `log`，此時需採用上述任一選項。

### 實用建議
- **最簡方案**：若不介意 `.txt` 與 `.log` 同時換行，直接使用 `[plaintext]`。
- **精準方案**：安裝 "Log File Highlighter" 擴充功能，確認模式為 `log` 後使用 `[log]`。
- 請告知你的 `.log` 檔案顯示的語言模式，我將協助進一步優化解決方案！

---

我測試了以下配置，效果非常理想。

```json
   {
       "editor.wordWrap": "off", // 預設：不換行
       "[log]": {
           "editor.wordWrap": "on" // 僅對 .log 檔案啟用換行
       }
   }
```