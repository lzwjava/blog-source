---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 從命令行開啟 Sublime Text
translated: true
type: note
---

### 從命令列 (CLI) 開啟 Sublime Text

根據你使用 `open -a` 的參考，聽起來你正在使用 macOS，而 Sublime Text 在 macOS 上預設並沒有內建 `sublime`（或 `subl`）指令。不過，有一個官方且簡單的方法，可以使用 Sublime 內附的 `subl` 腳本來添加這個指令。這比依賴 `open` 指令更為簡潔。我將在下面逐步介紹選項，從推薦的方法開始。

#### 1. **安裝官方的 `subl` CLI 指令（推薦）**
Sublime Text 在其應用程式套件中包含了一個 `subl` 可執行檔，你可以將其符號連結（symlink）到你的 PATH 中的某個目錄（例如 `/usr/local/bin`）。這樣你就可以在終端機的任何地方執行 `subl .`（開啟當前目錄）或 `subl file.txt`。

**macOS 步驟（Sublime Text 3 或 4）：**
- 開啟 Terminal。
- 執行以下指令來建立符號連結（需要管理員權限，因此系統會提示你輸入密碼）：
  ```
  sudo ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl
  ```
  - 如果你使用的是 Sublime Text 3，路徑可能略有不同：`"/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"`（請根據版本號調整）。
  - 如果 `/usr/local/bin` 不在你的 PATH 中，請將其添加到你的 shell 設定檔中（例如 `~/.zshrc` 或 `~/.bash_profile`）：
    ```
    echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```

- 測試：導航到一個目錄（例如 `cd ~/Desktop`）並執行：
  ```
  subl .
  ```
  這應該會開啟 Sublime Text 並載入當前資料夾。

如果符號連結路徑無效（例如由於版本差異），請檢查確切位置：
- 執行 `find /Applications/Sublime\ Text.app -name subl` 來定位二進位檔。

**這個方法的好處：**
- 它是官方且輕量的——不需要第三方工具。
- 像真正的 CLI 一樣在全系統範圍內工作。
- Sublime Text 4 甚至在控制台（View > Show Console）中有一個選項可以執行 `sublime_installation` 或類似的指令，但符號連結是最可靠的方法。

**如果你在 Linux 或 Windows 上：**
- Linux：類似的符號連結過程——例如 `sudo ln -s /opt/sublime_text/sublime_text /usr/local/bin/subl`。
- Windows：將 `C:\Program Files\Sublime Text\sublime_text.exe` 添加到你的 PATH，或使用批次檔來實現 `subl`。

#### 2. **備用方案：使用 `open` 指令（無需安裝）**
如果你不想處理符號連結或 PATH，macOS 內建的 `open` 指令對於基本使用來說非常有效。它已經隨處可用。

- 在 Sublime 中開啟當前目錄：
  ```
  open -a "Sublime Text" .
  ```
  - 注意：如果你的應用程式名稱是 `"Sublime Text"`（帶有空格），請使用這個名稱。如果只是 "Sublime.app"，請相應調整。你可以在 `/Applications/` 中檢查確切名稱。

- 開啟特定檔案：
  ```
  open -a "Sublime Text" filename.txt
  ```

- 為方便起見，可以設定別名：將以下內容添加到你的 shell 設定檔（`~/.zshrc` 或 `~/.bash_profile`）來模擬 `subl`：
  ```
  alias subl='open -a "Sublime Text"'
  ```
  然後使用 `source ~/.zshrc` 重新載入，並像平常一樣使用 `subl .`。

**優點/缺點：**
- 超級簡單且無需設定。
- 但僅限於 macOS，且靈活性較低（例如，無法像 `subl` 那樣輕鬆指定行數或專案）。

#### 疑難排解
- **指令找不到？** 確保你的 PATH 包含 `/usr/local/bin`（執行 `echo $PATH` 檢查）。
- **應用程式找不到？** 確認 Sublime 在 `/Applications/` 中。如果它在其他地方（例如透過 Homebrew：`brew install --cask sublime-text`），請調整路徑。
- **權限問題？** 符號連結需要 sudo，但一旦設定完成就沒問題了。
- 如果你使用像 Homebrew 這樣的套件管理器，你可以透過 `brew install --cask sublime-text` 安裝 Sublime，它可能會為你處理 CLI 指令。

這應該能讓你順利運作！如果你遇到錯誤或指定你的作業系統/版本，我可以進一步調整步驟。