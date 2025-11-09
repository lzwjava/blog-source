---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Clash代理後繼者與Linux支援
translated: true
type: note
---

Clash，一款類似 Shadowsocks 的基於規則的代理工具，其原始儲存庫於 2023 年因中國監管壓力被作者刪除。社群透過分支和後繼項目（如 Clash.Meta，現正式名稱為 Mihomo）持續開發，該項目被廣泛認為是最可靠且積極維護的替代方案。它支援 Linux 二進位檔案（包括 Ubuntu），並具備 DNS over HTTPS (DoH)、隧道傳輸及基於規則的路由等功能。

對於 Linux/Ubuntu 的可靠 GitHub 儲存庫，我推薦主要的延續項目。以下是基於社群採用度、更新頻率和 Linux 支援度的頂尖選項摘要：

### 推薦儲存庫
- **MetaCubeX/mihomo (Clash.Meta 核心)**：這是 Clash 的主要後繼項目，在原始項目刪除後由社群分支並維護。它提供完整的代理功能、頻繁更新，以及適用於 Linux（x86_64 和 arm64）的預編譯二進位檔案。Ubuntu 相容性極佳，二進位檔案已在 18.04+ 版本中通過測試。它開源、無廣告，並可透過 YAML 配置檔案高度自訂。  
  - GitHub：https://github.com/MetaCubeX/mihomo  
  - 可靠性原因：超過 1.4 萬星標、活躍社群，且二進位檔案包含用於路由的 GeoIP 資料庫。可直接在發布區下載 Linux CLI 二進位檔案。  
  - Ubuntu 安裝方式：從發布區下載最新的 "mihomo-linux-amd64" 二進位檔案，設為可執行（`chmod +x mihomo`）並運行。需搭配包含代理規則的 config.yaml 檔案。[1][2]  
  - 若核心版本不適用時的替代方案：  
    - **CarlDegio/verge**：基於 Tauri 的 Clash.Meta GUI 封裝，為 Linux（包含 Ubuntu）提供直觀的儀表板。底層使用 Mihomo 以確保穩定性。  
      - GitHub：https://github.com/CarlDegio/verge  
      - 可靠性原因：支援桌面 GUI、超過 2 千星標、簡易設定檔切換及系統匣圖示。可下載 AppImage 用於 Ubuntu。[3]  
    - **chen08209/FlClash**：基於 Clash.Meta 的多平台客戶端（包含 Linux 二進位檔案）。專注於簡潔性與無廣告設計，並提供簡易配置介面。  
      - GitHub：https://github.com/chen08209/FlClash  
      - 可靠性原因：輕量級、透過 deb/AppImage 構建支援 Ubuntu，並整合 Mihomo 綁定功能。[4]  
  - 舊版備份：Kuingsmile/clash-core 提供刪除前核心的存檔構建，若偏好未維護但具歷史意義的版本，可下載其 Linux 發布檔。[5]  

### 補充說明
- **安裝提示**：確保 Ubuntu 具備 libc（glibc 2.17+）。可使用 `systemd` 或 `screen` 等工具作為後台服務運行。為確保安全，請透過 SHA256 雜湊值驗證下載檔案。
- **可靠性標準**：這些儲存庫擁有活躍貢獻者、龐大用戶群（高星標/分支數），並避免了 2023 年後項目棄置的風險。Clash.Premin（可能為 Premium 的筆誤）是付費分支，但較不專注於開源。
- **法律/使用提醒**：Clash 用於繞過網路審查；請確保符合當地法律，因其在受限區域使用可能引起關注。
- 若需要 UI 或特定功能（例如多平台支援），verge 或 FlClash 比核心 Mihomo CLI 更易使用。詳情請查閱各儲存庫的 README。若遇到問題，Mihomo 儲存庫提供詳盡文件。[6][7][1][8]  

若無合適選項或需要 Ubuntu 逐步指南，請提供更多細節！

引用來源：
[1] https://github.com/djoeni/Clash.Meta
[2] https://discussion.fedoraproject.org/t/rhbz-2305079-review-request-clash-meta-a-rule-based-network-proxy-tool-aka-mihomo/146312
[3] https://github.com/CarlDegio/verge
[4] https://github.com/chen08209/FlClash
[5] https://github.com/Kuingsmile/clash-core/releases
[6] https://github.com/fengwz17/Clash-For-Ubuntu
[7] https://news.ycombinator.com/item?id=38126160
[8] https://github.com/hiddify/Clash.Meta