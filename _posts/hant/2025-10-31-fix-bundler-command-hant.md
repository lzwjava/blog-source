---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修正 Bundler 指令不存在
translated: true
type: note
---

### 理解問題
你的 `gem install jekyll bundler` 已成功執行（安裝了 30 個 gems，包括 Bundler 2.7.2），但系統找不到 `bundle` 指令。這在 Ubuntu/Debian 系統上，在使用全域性的 `sudo gem install` 後，是常見的 PATH/環境變數問題。Gems 會將二進位檔安裝到 `/usr/local/bin`（或類似路徑），但你的 shell 的 `$PATH` 可能未包含該路徑，或者變更尚未生效（例如需要重新載入設定檔）。

系統建議的 `apt install ruby-bundler` 會透過 apt 安裝較舊的版本 (2.4.20)，這可能會與你透過 gem 安裝的 Bundler 2.7.2 衝突——暫時請避免這樣做。同樣地，snap 也可能會以破壞 gem 路徑的方式隔離 Ruby。

### 快速修復：驗證並使用已安裝的 Bundler
1. **檢查 `bundle` 安裝位置**：
   ```
   gem environment
   ```
   - 尋找 "EXECUTABLE DIRECTORY"（可能是 `/usr/local/bin`）。請記下該路徑。

2. **定位並直接測試 `bundle`**：
   ```
   which bundle  # 如果沒有輸出，請嘗試：find /usr/local -name bundle 2>/dev/null
   /usr/local/bin/bundle --version  # 應該輸出 "Bundler version 2.7.2"
   ```
   - 如果運作正常，太好了！暫時使用完整路徑：`/usr/local/bin/bundle install`

3. **使用完整路徑執行你的 Jekyll 設定**：
   - 在 `~/projects/blog-source` 目錄下（假設該目錄有 `Gemfile`）：
     ```
     /usr/local/bin/bundle install
     /usr/local/bin/bundle exec jekyll serve
     ```
   - 這應該會安裝 Jekyll 相依套件並啟動伺服器（通常位於 http://127.0.0.1:4000）。

### 永久修復：更新你的 PATH
如果 `/usr/local/bin` 不在你的 `$PATH` 中，請將其加入：
1. 編輯 `~/.bashrc`（或針對登入 shell 的 `~/.profile`）：
   ```
   nano ~/.bashrc
   ```
   在檔案末尾加入這一行：
   ```
   export PATH="/usr/local/bin:$PATH"
   ```

2. 重新載入你的 shell：
   ```
   source ~/.bashrc
   ```

3. 驗證：
   ```
   echo $PATH  # 現在應該包含 /usr/local/bin
   bundle --version  # 應該無需完整路徑即可運作
   ```

現在重新嘗試：
```
bundle install
bundle exec jekyll serve
```

### 如果仍然無效
- **權限問題？**（較少見，但 sudo 可能導致此問題。）嘗試不使用 sudo 重新安裝（使用者本機安裝）：
  ```
  gem install --user-install bundler jekyll
  ```
  然後將 `export PATH="$HOME/.local/share/gem/ruby/*/bin:$PATH"` 加入 `~/.bashrc`（請根據 `gem environment` 的輸出調整路徑）。

- **Ruby 版本不符？** 使用 `ruby --version` 檢查。如果是系統 Ruby（例如 2.7.x），請考慮使用 Ruby 版本管理器，例如 `rbenv`（可透過 `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash` 安裝，然後按照設定步驟操作）。這能從長遠角度避免系統衝突。

- **代理設定仍在作用？** 如果你的環境變數（`http_proxy` 等）已設定，Bundler 應該會繼承它們——只需確保在執行前已匯出這些變數。

在調整 PATH 後，你的設定應該能順利運作。如果遇到錯誤（例如，分享 `gem environment` 的輸出），請貼上它們以獲得更有針對性的幫助！