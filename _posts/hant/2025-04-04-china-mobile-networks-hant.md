---
audio: false
generated: true
lang: hant
layout: post
title: 為何在中國移動網絡上Git操作會失敗
translated: true
type: note
---

這是在中國使用某些行動網路時常見的問題，特別是對於依賴特定端口和協定的服務如 Git。以下將分析問題成因及解決方法：

**為何在中國行動網路上 Git 操作會失敗：**

* **端口封鎖/流量限制：**
    * 中國的行動網路運營商有時會實施流量整形或端口封鎖，特別是針對 Git 使用的非標準端口（如 SSH 端口 22）。這通常是為了管理網路頻寬或安全考量。
    * 即使端口 22 未被完全封鎖，也可能被嚴重限速，導致連接極慢或超時，使 Git 操作看似「卡住」。
* **DNS 問題：**
    * 雖然你能存取 GitHub 和 Google 等網站，但 Git 操作需透過 DNS 解析特定主機名稱（如 `github.com`）。若 DNS 解析緩慢或不穩定，會導致 Git 停頓。
* **封包遺失/延遲：**
    * 行動網路（特別是作為熱點使用時）相較有線連接可能具有更高延遲和封包遺失率，這會擾亂 Git 使用的 SSH 連接。
* **防火牆干擾：**
    * 中國的「防火長城」可能干擾 SSH 連接，即使未被明確封鎖。防火牆的深度封包檢測有時會導致連接不穩定。
* **MTU 問題：**
    * 最大傳輸單元（MTU）問題可能導致資料傳輸異常，而行動網路的 MTU 值通常比有線網路小。

**解決中國行動網路上 Git 推送/拉取問題的方法：**

1.  **改用 HTTPS 替代 SSH：**
    * Git over HTTPS 使用端口 443（通常開放於網路流量），這是最可靠的解決方案。
    * 更改 Git remote 為 HTTPS：
        * 開啟終端機
        * 進入 Git 儲存庫
        * 執行以下指令（替換為你的 GitHub 資訊）：
            ```bash
            git remote set-url origin https://github.com/your_username/your_repository.git
            ```
    * 如需輸入帳號密碼，可使用 git credential helper 或個人存取權杖。
2.  **使用 VPN：**
    * 可靠的 VPN 可繞過網路限制并提供更穩定連接。
    * 進行 Git 操作前先連接至中國境外的 VPN 伺服器。
    * 請注意 VPN 也可能出現不穩定及速度問題。
3.  **設定 SSH 端口（如需使用 SSH）：**
    * 若必須使用 SSH，可嘗試將 Git 設定為使用較不易被封鎖的端口（如 443）。
    * 編輯 `~/.ssh/config` 檔案：
        ```
        Host github.com
            Hostname ssh.github.com
            Port 443
            User git
        ```
    * 接著將 git remote url 改為使用 ssh.github.com：
        ```bash
        git remote set-url origin git@ssh.github.com:your_username/your_repository.git
        ```
4.  **檢查 MTU 設定：**
    * 若懷疑 MTU 問題，可嘗試降低 MTU 值。
    * macOS 系統可使用 `networksetup` 指令調整 MTU。
    * 但需注意修改 MTU 屬於進階除錯步驟，應謹慎操作。
5.  **檢查 DNS 設定：**
    * 嘗試使用公共 DNS 伺服器，如 Google DNS（8.8.8.8 與 8.8.4.4）或 Cloudflare DNS（1.1.1.1 與 1.0.0.1）。
    * 可在 macOS 網路偏好設定中配置 DNS。
6.  **使用 Git 代理：**
    * 若有可用的代理伺服器，可設定 Git 使用代理。
    * 設定 `http.proxy` 與 `https.proxy`  Git 配置變數：
        ```bash
        git config --global http.proxy http://proxy_address:proxy_port
        git config --global https.proxy https://proxy_address:proxy_port
        ```
    * 若代理需要驗證，可在代理 URL 中包含帳號密碼。
7.  **嘗試使用 Websockets 傳輸 SSH：**
    * 某些工具和服務允許透過 websockets 隧道傳輸 SSH 流量，當標準 SSH 端口被封鎖時特別有用。
    * 此為進階技術，需設定支援 SSH over websockets 的伺服器。

**重要注意事項：**

* 行動網路狀況變異性大，在某地某時有效的方法未必適用其他情境。
* 請留意行動網路供應商的服務條款，以及使用 VPN 等解決方案可能存在的限制。
* 對多數用戶而言，HTTPS 通常是最佳解決方案。