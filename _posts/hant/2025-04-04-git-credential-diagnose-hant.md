---
audio: false
generated: true
lang: hant
layout: post
title: Git 憑證管理員診斷
translated: true
type: note
---

`git credential-manager diagnose` 的輸出現在除了 TLS 憑證驗證警告外，還明確顯示了**網絡連接故障**。讓我們來分析錯誤並找出解決方法：

**關鍵發現：**

* **網絡連接故障：**
    * 診斷測試失敗，錯誤訊息為：`System.Net.Http.HttpRequestException: nodename nor servname provided, or not known (example.com:443)`。
    * 此錯誤表示 Git Credential Manager 無法將主機名稱 `example.com` 解析為 IP 地址，或者無法連接到該主機的 443 端口。
    * 診斷日誌顯示，對 `https://example.com` 的 HEAD 請求失敗。
* **代理伺服器干擾（可能原因）：**
    * 存在 `HTTP_PROXY: http://127.0.0.1:7890` 和 `HTTPS_PROXY: http://127.0.0.1:7890` 的設定，強烈表明代理伺服器是網絡故障的根本原因。
    * 診斷能夠訪問 [http://httpforever.com](http://httpforever.com)，卻無法訪問 [https://example.com](https://example.com)，這表明代理伺服器在處理 HTTPS 請求時出現問題。
* **TLS 憑證驗證已停用（安全風險）：**
    * 如前所述，TLS 憑證驗證已被停用，這是一個重大的安全隱患。

**故障排除步驟：**

1.  **代理伺服器驗證：**
    * **測試代理伺服器：** 打開網頁瀏覽器，嘗試直接訪問 `https://example.com`。如果您遇到「無法連接」或「找不到主機」錯誤，則您的代理伺服器可能配置錯誤。
    * **代理軟體問題：**
        * 重新啟動您的代理軟體（Shadowsocks、Clash 等）。
        * 檢查代理軟體的日誌以獲取錯誤訊息。
        * 確保代理伺服器配置為能正確處理 HTTPS 流量。
        * 確保代理軟體正在運行。
    * **代理伺服器配置：**
        * 仔細檢查您作業系統網絡偏好設定以及任何 Git 配置檔案中的代理設定。
        * 驗證代理地址 (`127.0.0.1`) 和端口 (`7890`) 是否正確。
        * 在您的作業系統網絡設定中暫時停用代理，然後重新運行 `git credential-manager diagnose`。
2.  **DNS 解析：**
    * 儘管錯誤訊息暗示了主機名稱解析問題，但代理伺服器仍是最可能的罪魁禍首。不過，檢查您的 DNS 設定仍然是值得的。
    * 嘗試使用公共 DNS 伺服器（例如 8.8.8.8、1.1.1.1）。
3.  **TLS 憑證驗證：**
    * **重新啟用憑證驗證：** 這對安全性至關重要。請遵循 `https://aka.ms/gcm/tlsverify` 連結中提供的說明。
    * 如果您的代理軟體旨在攔截 HTTPS 流量，請確保將代理的根憑證安裝到您作業系統的受信任根憑證存放區中。這是讓代理正常工作的安全方法。
4.  **Git 配置：**
    * 運行 `git config --global --list` 來檢查您的 Git 配置。
    * 暫時從 Git 中移除代理設定以隔離問題：
        ```bash
        git config --global --unset http.proxy
        git config --global --unset https.proxy
        ```
    * 移除代理設定後，重新運行 `git credential-manager diagnose` 命令。
5.  **防火牆：**
    * 暫時停用電腦上的任何防火牆，以排除防火牆干擾。
6.  **網絡連接：**
    * 使用其他網絡應用程式測試您的網絡連接，以確保網絡本身穩定。
    * 如果使用移動熱點，請移至信號強度更好的位置。

**關鍵要點：** 代理伺服器幾乎可以肯定地導致了網絡連接故障。正確配置代理伺服器並重新啟用 TLS 憑證驗證是最重要的步驟。