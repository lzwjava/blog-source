---
audio: false
generated: true
lang: hant
layout: post
title: GNOME 終端機自訂目錄標題
translated: true
type: note
---

要自訂 GNOME Terminal 分頁標題，使其僅顯示目前目錄（例如 `blog-server`），而非預設格式（例如 `lzw@lzw-MS:~/Projects/blog-server`），您可以修改終端機的提示符或標題設定。具體操作如下：

### 設定 GNOME Terminal 分頁標題僅顯示目前目錄的步驟

1. **編輯 Bash 設定檔**：
   GNOME Terminal 預設使用 Bash shell，分頁標題通常源自 `PS1`（提示符）或特定的標題設定指令。要自訂標題，您可以修改 `~/.bashrc` 檔案。

2. **修改終端機標題**：
   在 `~/.bashrc` 中加入設定終端機標題為目前目錄的指令。使用文字編輯器開啟檔案：

   ```bash
   nano ~/.bashrc
   ```

   在檔案末尾加入以下內容：

   ```bash
   # 設定終端機分頁標題為目前目錄
   case "$TERM" in
   xterm*|rxvt*)
       PS1="\[\e]0;\W\a\]$PS1"
       ;;
   *)
       ;;
   esac
   ```

   **說明**：
   - `\e]0;...` 用於設定終端機標題。
   - `\W` 代表目前目錄的基底名稱（例如 `blog-server` 而非完整路徑 `~/Projects/blog-server`）。
   - `\a` 是終止標題字串的響鈴字元。
   - 此程式碼會先檢查終端機是否為 `xterm` 相容（GNOME Terminal 符合此條件），再套用變更。

3. **套用變更**：
   儲存檔案後重新載入 Bash 設定：

   ```bash
   source ~/.bashrc
   ```

   或關閉並重新開啟終端機以套用變更。

4. **驗證結果**：
   切換至某個目錄（例如 `cd ~/Projects/blog-server`），終端機分頁標題現在應僅顯示 `blog-server`。

### 替代方案：修改 GNOME Terminal 設定檔
若想進一步自訂標題或避免編輯 `~/.bashrc`，可使用 GNOME Terminal 的設定檔功能：

1. 開啟 GNOME Terminal。
2. 前往 **編輯** > **偏好設定**（或 **終端機** > **偏好設定**，依版本而定）。
3. 選擇您使用的設定檔（例如「未命名」或自訂設定檔）。
4. 切換至 **指令** 分頁。
5. 在 **標題與指令** 區塊中設定：
   - **初始標題**：留空或設定為通用名稱。
   - **當指令結束時**：選擇 **保持初始標題** 或 **以指令輸出取代**。
6. 在 **指令** 區塊中，啟用 **執行自訂指令而非我的 shell** 並設定指令為：

   ```bash
   bash --rcfile <(echo '. ~/.bashrc; PS1="\[\e]0;\W\a\]$PS1"')
   ```

   此設定可確保終端機使用會將標題設為目前目錄的自訂提示符。

7. 關閉對話框後，透過開啟新分頁或切換目錄進行測試。

### 注意事項
- 若使用 Bash 以外的 shell（例如 Zsh），需修改對應的設定檔（例如 `~/.zshrc`）並調整語法。對於 Zsh，可加入：

  ```zsh
  precmd() { echo -ne "\e]0;${PWD##*/}\a" }
  ```

- 若標題未如預期更新，請確認您的終端機模擬器是否為 `xterm` 相容，且沒有其他指令稿（例如 `~/.bashrc` 中的自訂 `PS1` 設定）覆寫標題。
- 若要讓變更在所有終端機中持續生效，請確保設定已加入使用者的 shell 設定檔或 GNOME Terminal 設定中。

完成後，分頁標題將僅顯示目前目錄名稱，例如 `blog-server`。如有任何疑問，歡迎提出！