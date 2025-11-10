---
audio: false
generated: true
lang: hant
layout: post
title: 檢查 Ubuntu 中的 APT 代理設定
translated: true
type: note
---

要檢查 Ubuntu 中的 `apt` 是否使用代理伺服器，請按照以下步驟操作：

1. **檢查 APT 設定檔**：
   - 開啟位於 `/etc/apt/apt.conf` 或 `/etc/apt/apt.conf.d/` 的 APT 設定檔（此目錄中的檔案，如 `70debconf` 或 `proxy.conf`，可能包含代理設定）。
   - 使用指令：
     ```bash
     sudo cat /etc/apt/apt.conf
     ```
     或
     ```bash
     sudo grep -r Proxy /etc/apt/apt.conf.d/
     ```
   - 尋找類似以下的行：
     ```
     Acquire::http::Proxy "http://proxy-server:port";
     Acquire::https::Proxy "https://proxy-server:port";
     Acquire::ftp::Proxy "ftp://proxy-server:port";
     ```
     如果存在這些行，表示 `apt` 已設定使用代理伺服器。

2. **檢查環境變數**：
   - `apt` 可能會使用環境變數中定義的代理設定，例如 `http_proxy`、`https_proxy` 或 `ftp_proxy`。
   - 執行：
     ```bash
     env | grep -i proxy
     ```
   - 如果看到類似 `http_proxy=http://proxy-server:port` 的輸出，表示 `apt` 可能正在使用這些設定。

3. **檢查系統全域代理設定**：
   - 如果您使用桌面環境（例如 GNOME），請檢查系統代理設定：
     - 前往 *設定 > 網路 > 代理* 或類似選項，具體取決於您的桌面環境。
     - 如果未設定特定的 APT 代理，這些設定可能會套用至 `apt`。

4. **使用指令測試 APT**：
   - 執行 `apt` 指令並觀察行為：
     ```bash
     sudo apt update
     ```
   - 如果 `apt` 透過代理連線，您可能會看到延遲、特定錯誤訊息或代理相關的記錄。若要進一步除錯，請使用：
     ```bash
     sudo apt -o Debug::pkgProblemResolver=yes update
     ```
     這將提供詳細輸出，可能顯示代理使用情況。

5. **檢查 `/etc/environment` 中的代理設定**：
   - 某些系統會在 `/etc/environment` 中定義代理。請使用以下指令檢查：
     ```bash
     cat /etc/environment
     ```
   - 尋找類似以下的行：
     ```
     http_proxy="http://proxy-server:port"
     ```

如果以上檢查均未顯示代理設定，則 `apt` 很可能未使用代理。若要即時確認，您可以使用 `tcpdump` 或 `wireshark` 等工具監控網路流量，查看 `apt` 連線是否透過代理伺服器路由。

如果您需要協助分析特定輸出或設定代理，請告訴我！