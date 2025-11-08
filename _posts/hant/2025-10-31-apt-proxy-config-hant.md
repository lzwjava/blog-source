---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 檢查APT代理配置與使用
translated: true
type: note
---

### 檢查 APT 是否使用代理

要確認 APT（Debian/Ubuntu 系統上的套件管理員）是否設定使用代理 — 以及操作時是否實際應用 — 您可以按照以下步驟進行。這涉及檢查設定檔和測試連線能力。請注意，APT 不會以簡單的方式明確記錄代理使用情況，因此「確認」通常意味著驗證設定並在測試運行期間觀察行為。

#### 1. **檢查 APT 的代理設定**
   APT 代理設定儲存在 `/etc/apt/apt.conf` 或 `/etc/apt/apt.conf.d/` 中的檔案（例如 `99proxy` 或類似名稱）。尋找定義 `Acquire::http::Proxy` 或 `Acquire::https::Proxy` 的行。

   - **檢查所有代理相關設定的指令**：
     ```
     apt-config dump | grep -i proxy
     ```
     - **作用**：傾印 APT 的有效設定並篩選出代理條目。如果您看到像 `Acquire::http::Proxy "http://proxy.example.com:8080/"` 這樣的輸出，則表示已設定代理。
     - **如果設定了代理的範例輸出**：
       ```
       Acquire::http::Proxy "http://username:password@proxy.example.com:8080";
       Acquire::https::Proxy "http://proxy.example.com:8080";
       ```

   - **手動檢查檔案**：
     ```
     grep -r "Proxy" /etc/apt/apt.conf* /etc/apt/apt.conf.d/
     ```
     - **作用**：在所有 APT 設定檔中搜尋「Proxy」關鍵字。

   如果沒有出現代理相關的行，則 APT **沒有**使用代理（直接連線）。

#### 2. **測試代理是否實際被使用**
   僅有設定並不能確認使用情況 — 透過模擬從儲存庫獲取資料的 APT 操作來測試（如果設定了代理，則會透過代理路由）。

   - **基本測試：執行更新**：
     ```
     sudo apt update
     ```
     - **作用**：從儲存庫獲取套件清單。觀察輸出：
       - 成功（例如「Hit:1 http://archive.ubuntu.com ...」）表示連線能力，如果已設定代理，則可能透過代理連線。
       - 像「Failed to fetch」或逾時等錯誤表示代理問題（例如錯誤的憑證或無法連線的代理）。
     - 要查看更多詳細資訊，請增加詳細程度：`sudo apt update -o Debug::Acquire::http=true`。

   - **僅下載測試（不變更系統）**：
     ```
     sudo apt clean
     sudo apt -d --reinstall install hostname
     ```
     - **作用**：清除快取，然後僅下載（`-d` 標誌）而不實際安裝，假裝重新安裝內建的 `hostname` 小套件。檢查輸出是否成功獲取。如果成功，則表示使用了代理（假設已設定）。

   - **進階：追蹤網路呼叫（需要 `strace`）**：
     如果您想在運行期間確認代理連線：
     ```
     sudo strace -e trace=connect sudo apt update 2>&1 | grep -i proxy
     ```
     - **作用**：追蹤網路連線的系統呼叫。尋找連線到您的代理 IP/端口，而不是直接連線到儲存庫伺服器（例如 `archive.ubuntu.com`）。

#### 常見問題與修復
- **如果代理需要驗證**：確保設定使用 `http://username:password@proxyhost:port`。
- **環境變數**：APT 會忽略 Shell 代理（`$http_proxy`），因此請依賴 APT 特定的設定。
- **關於您的指令 `sudo apt --fix-broken install`**：此指令透過重新安裝套件來修復損壞的相依性。如果失敗（例如網路錯誤），請在透過上述測試確認代理後執行。代理問題通常表現為獲取失敗 — 請先修復設定，然後重試。

如果這些方法無法解決問題，請分享錯誤輸出以獲得更多幫助。

**參考資料**：
- [How to check if apt proxy configuration is correct? (Unix Stack Exchange)](https://unix.stackexchange.com/questions/49781/how-to-check-if-apt-proxy-configuration-is-correct)
- [How to Use APT with Proxy on Ubuntu and Debian (Linuxiac)](https://linuxiac.com/how-to-use-apt-with-proxy/)