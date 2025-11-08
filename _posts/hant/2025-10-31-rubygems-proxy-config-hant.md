---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 配置 RubyGems 代理設定
translated: true
type: note
---

為確保 `gem`（RubyGems）在安裝時使用你的代理伺服器（例如位於 `http://127.0.0.1:7890`），請按照以下步驟操作。根據你分享的詳細輸出，它*似乎已經在使用代理*——「Connecting to 127.0.0.1:7890... connected」這行來自底層 HTTP 客戶端（可能是 `net/http` 或類似 `curl` 的詳細模式）的強烈指示。

### 1. **配置代理（如果尚未設定）**
   - **選項 A：使用環境變數（建議用於一次性或 sudo 指令）**  
     這些設定會告訴 `gem` 透過代理路由流量。在安裝前執行：
     ```
     export http_proxy=http://127.0.0.1:7890
     export https_proxy=http://127.0.0.1:7890
     sudo -E gem install jekyll bundler --verbose
     ```
     - `-E` 標誌在使用 `sudo` 時保留你的環境變數。
     - 如需永久設定，請將 `export` 行加入你的 `~/.bashrc` 或 `~/.profile`。

   - **選項 B：在 `~/.gemrc` 中配置（用戶層級，未來安裝無需 sudo）**  
     建立或編輯 `~/.gemrc`：
     ```
     echo 'http_proxy: http://127.0.0.1:7890' >> ~/.gemrc
     echo 'https_proxy: http://127.0.0.1:7890' >> ~/.gemrc
     ```
     然後執行 `gem install jekyll bundler --verbose`（盡可能不使用 `sudo`——`sudo` 可能忽略用戶配置）。如果使用 `sudo`，請堅持使用選項 A。

### 2. **驗證是否使用代理**
   - **使用 `--verbose` 執行（如你所做）**：尋找類似以下的行：
     - `HEAD https://index.rubygems.org/` 後跟代理連接詳細資訊。
     - `Connecting to 127.0.0.1:7890... connected.`（這確認代理使用）。
     - 如果顯示直接連接到 `rubygems.org`（例如，未提及代理的 IP 地址），則表示它繞過了代理。
   
   - **使用乾運行或資訊獲取進行測試**：
     ```
     gem fetch jekyll --verbose --platform=ruby
     ```
     或僅查詢索引：
     ```
     gem search jekyll --verbose
     ```
     檢查輸出中的代理連接。

   - **檢查環境變數**：
     ```
     echo $http_proxy $https_proxy
     ```
     如果它們設定正確，`gem` 應該會繼承它們。

   - **使用 `gem env` 進行除錯**：
     ```
     gem env
     ```
     在「HTTP Proxy」或「HTTPS Proxy」部分尋找你的代理 URL。

### 疑難排解
- **如果 sudo 忽略代理**：使用 `sudo -E` 或在不使用 `sudo` 的情況下執行（安裝到用戶目錄：`gem install --user-install jekyll bundler`）。
- **沒有連接行？** 你的代理可能未啟用詳細模式，或環境變數未設定。單獨測試代理：`curl -v https://rubygems.org/`（應顯示代理跳轉）。
- **企業/嚴格代理？** 如果需要驗證，請使用 `http://user:pass@127.0.0.1:7890`。
- **仍然失敗？** 暫時停用代理（`unset http_proxy https_proxy`）並重試——如果沒有代理可以工作，問題在於配置；如果不行，請檢查你的代理伺服器（例如 Clash/V2Ray 日誌）。

你的安裝已成功（200 OK 回應），所以你很可能沒問題——只需確認下一次運行顯示代理連接以確保安心。如果你分享更多輸出，我可以進一步除錯！