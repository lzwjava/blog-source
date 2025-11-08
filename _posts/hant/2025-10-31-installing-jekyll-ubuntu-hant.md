---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 在 Ubuntu 上安裝 Jekyll
translated: true
type: note
---

### 在 Ubuntu 上設定和運行 Jekyll

根據你的錯誤信息（"未找到指令 'bundle'"）以及你嘗試運行的指令，看來你需要先正確安裝 Ruby、Bundler 和 Jekyll。Ubuntu 預設並不包含這些工具，但按照官方 Jekyll 指南操作很簡單。我將逐步引導你完成完整設定，然後再說明如何運行你的特定指令。

#### 步驟 1：安裝系統依賴套件
打開終端機並運行以下指令來安裝 Ruby 和建置工具（這包括透過 `ruby-full` 安裝 Ruby 3.x）：

```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

- 這會設定好 Ruby（可用 `ruby -v` 檢查——應該會顯示類似 3.0+ 的版本）。
- 如果你使用的是較新的 Ubuntu（例如 22.04+），這可以直接運行。請盡可能避免使用 Snap 安裝 Ruby，因為可能會導致路徑問題。

#### 步驟 2：設定用戶 Gem 目錄（建議避免使用 Sudo）
為了在無需 root 權限的情況下安裝 gems（防止後續出現權限錯誤）：

```bash
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

- 驗證：運行 `gem env`——它應該顯示你的 `GEM_HOME` 為 `~/gems`。

#### 步驟 3：安裝 Jekyll 和 Bundler
現在安裝工具：

```bash
gem install jekyll bundler
```

- 這會將 `gem`、`jekyll` 和 `bundle` 指令添加到你的路徑中。
- 如果遇到權限錯誤，請再次檢查步驟 2 或暫時使用 `sudo`（但長期不建議）。

#### 步驟 4：建立和運行你的部落格
現在你可以運行你片段中的指令了。我將逐一解釋：

1. **建立新的 Jekyll 網站**：
   ```bash
   jekyll new myblog
   ```
   - 這會在 `myblog` 資料夾中生成一個基本網站。

2. **進入目錄**：
   ```bash
   cd myblog
   ```

3. **安裝依賴套件**（這是你原本 `bundle install` 失敗的地方——現在應該可以運行了）：
   ```bash
   bundle install
   ```
   - 會拉取像 Jekyll 插件這樣的 gems。

4. **啟動網站伺服器**（在 http://127.0.0.1:4000 啟動本地伺服器）：
   ```bash
   bundle exec jekyll serve
   ```
   - 在瀏覽器中打開該 URL 即可看到你的網站。

5. **使用增量重建模式啟動伺服器**（開發時更快，只重建更改過的檔案）：
   ```bash
   bundle exec jekyll serve --incremental
   ```

6. **啟動伺服器並包含草稿**（顯示未發佈的文章）：
   ```bash
   bundle exec jekyll serve --draft
   ```

7. **如果遇到 "webrick" 錯誤**（在 Ruby 3+ 上常見，因為它不再預設綑綁）：
   ```bash
   bundle add webrick
   ```
   - 然後重啟伺服器指令：`bundle exec jekyll serve`。
   - 或者，將 `gem "webrick"` 添加到你的 `Gemfile` 並運行 `bundle install`。

8. **不使用 Bundler 快速啟動伺服器**（如果你跳過 `bundle exec`）：
   ```bash
   jekyll serve
   ```
   - 但在專案中建議使用 `bundle exec` 以保持一致。

#### 疑難排解
- **仍然顯示「未找到 bundle」？** 確保步驟 2 正確載入了你的 `~/.bashrc`（`source ~/.bashrc`），然後重啟終端機或運行 `hash -r`。用 `which bundle` 檢查。
- **gems 的權限問題？** 請堅持使用步驟 2 中的用戶目錄設定。
- **Ruby 版本太舊？** 如果 `ruby -v` 顯示版本 <3.0，考慮使用 rbenv 來安裝新版本（透過 `curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash` 安裝，然後 `rbenv install 3.2.0`）。
- **防火牆阻擋了連接埠 4000？** Ubuntu 通常不會，但可以用 `curl http://127.0.0.1:4000` 測試。
- 你的專案在 `~/projects/blog-source` 中——請從那裡運行這些指令或調整路徑。

一旦伺服器啟動，編輯 `_posts/` 或 `_config.yml` 中的檔案並儲存——Jekyll 會自動重建。用於生產環境時，使用 `jekyll build` 建置並部署到 GitHub Pages 或 Netlify。

[Jekyll Ubuntu 安裝指南](https://jekyllrb.com/docs/installation/ubuntu/)