---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 Bundler 權限錯誤
translated: true
type: note
---

### 理解錯誤原因

這是一個在使用 Bundler（Ruby 的依賴管理工具）搭配系統預裝 Ruby（此處為 3.2.0 版本）時常見的權限問題。錯誤發生的原因是 Bundler 試圖在系統全域的 gem 目錄 `/var/lib/gems/3.2.0/cache/` 下載並快取 `rake` gem（可能還包括其他套件），而此操作需要 root 寫入權限。您的 Bundler 本身安裝在使用者本地目錄（位於 `~/.local/share/gem/`），但預設卻使用系統的 gem 路徑進行安裝。

您 `Gemfile` 中的依賴鏈（Jekyll + 相依套件如 `minima`、`jekyll-feed` 等）只是觸發了 `rake` 作為深層依賴的安裝——您的設定並無問題，純屬權限限制。

### 快速解決方案（按推薦順序排列）

1. **本地安裝 Gems（推薦 - 無需 Sudo）**  
   此方法將所有內容保留在您的家目錄中，完全避開系統路徑。請執行：
   ```
   bundle config set --local path 'vendor/bundle'
   bundle install
   ```
   - 這會在您的專案中建立 `vendor/bundle` 資料夾來存放 gems。
   - 後續執行 Jekyll 網站時請使用 `bundle exec jekyll serve`（`exec` 可確保使用本地 gems）。
   - 若希望全域適用所有專案：將 `--local` 替換為 `--global` 並使用 `~/.bundle` 作為路徑。

2. **使用 Sudo（快速但非理想方案）**  
   若需一次性安裝且不介意系統級 gems：
   ```
   sudo bundle install
   ```
   - **警告**：此操作會以 root 身份全域安裝 gems，可能導致後續所有權問題（例如未來更新時需使用 `sudo`）。請盡可能避免。

3. **修復系統權限（進階方案 - 請謹慎使用）**  
   若希望繼續使用系統 gem 目錄而無需 sudo：
   ```
   sudo chown -R $USER:$USER /var/lib/gems/3.2.0/
   ```
   - 然後重新執行 `bundle install`。
   - **警告**：此操作會變更系統 gems 的所有權，可能破壞由發行版管理的套件（如 Ubuntu）。僅在您具備除錯能力時使用。

### 長期建議
對於 Ruby/Jekyll 開發，建議改用使用者管理的 Ruby 安裝工具，例如 [rbenv](https://github.com/rbenv/rbenv) 或 [RVM](https://rvm.io/)。這能透過將 Ruby 和 gems 完全安裝在家目錄中，徹底避免權限難題：
- 安裝 rbenv：請遵循[官方指南](https://github.com/rbenv/rbenv#installation)。
- 接著執行：`rbenv install 3.2.0 && rbenv global 3.2.0 && gem install bundler`。
- 重新執行 `bundle install`——即可無縫運作。

若以上方法均未解決問題或遇到其他錯誤，請提供 `ruby -v`、`gem env` 及您的 `Gemfile.lock`（若存在）的輸出內容，以獲得更針對性的協助！