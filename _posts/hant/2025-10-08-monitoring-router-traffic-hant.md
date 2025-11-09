---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 監測路由器網絡流量
translated: true
type: note
---

### 監控 360 Wi-Fi 6 路由器 T7 的 HTTP 請求與 TCP 連線

360 T7 運行客製化的基於 Linux 的韌體（出廠時並非完整的 OpenWrt），因此與完整的 Linux shell 相比，原廠設定下的監控功能有限。透過管理員權限（經由網頁 UI），您可以存取基本日誌。若要進行更深層的「駭客」行為，例如即時 HTTP 請求記錄或 TCP 連線追蹤，最符合道德規範的方法是刷入 OpenWrt（官方支援），啟用 SSH，並使用標準的 Linux 工具。**警告：刷入自訂韌體會使保固失效，並有變磚風險 — 請務必先備份並仔細遵循指南。僅在您自己的裝置上進行此操作。**

#### 1. **在原廠韌體上取得管理員權限**
   - 連接到路由器的 Wi-Fi 或透過乙太網路連接。
   - 開啟瀏覽器並前往 `http://ihome.360.cn` 或 `http://192.168.0.1`（預設 IP）。
   - 登入：預設使用者名稱為 `admin`，密碼印在路由器標籤上（通常是 `admin` 或獨特字串如 `360XXXXXX` — 請查看底部貼紙）。
   - 登入後，導航至 **系統 > 日誌** 或 **安全 > 日誌** 以查看基本系統和流量日誌。這會顯示防火牆阻擋、連線以及一些 HTTP 活動（例如被封鎖的網站或入侵嘗試），但不會顯示完整的 HTTP 請求細節。

   **透過網頁 UI 進行基本監控：**
   - **系統日誌**：查看近期事件，包括 TCP 連線嘗試和錯誤。匯出日誌（可能需要標籤上的密碼進行解密）。
   - **流量統計**：在 **狀態 > 網路** 或 **進階 > 流量監控** 下，查看每個裝置/IP 的頻寬使用情況，但無法查看細粒度的 HTTP/TCP 資料。
   - 限制：無法進行即時 HTTP 負載檢查；日誌為高層級且未經授權無法匯出。

#### 2. **進階監控：刷入 OpenWrt 以取得 Shell 存取權限**
   360 T7（MT7981B 晶片組）在 OpenWrt 23.05+ 快照版中獲得支援。刷機後可透過 SSH 獲得完整的 root shell 存取權限，您可以在其中執行如 `tcpdump` 進行封包擷取和 `logread` 查看日誌等工具。

   **刷入 OpenWrt 的步驟（高層級概述；請使用官方指南）：**
   1. 從 OpenWrt 下載頁面下載 factory 映像檔（搜尋 "Qihoo 360T7 sysupgrade.bin" 或 factory 映像檔）。
   2. 備份原廠韌體：在網頁 UI 中，前往 **系統 > 備份** 並下載設定/韌體。
   3. 透過網頁 UI 上傳：**系統 > 韌體升級**，選擇 .bin 檔案並套用（路由器將重新啟動進入 OpenWrt）。
   4. 刷機後：在 `http://192.168.1.1` 存取網頁 UI（LuCI 介面），使用者名稱 `root`，初始無密碼 — 請立即透過 SSH 或 UI 設定密碼。
   5. 啟用 SSH：預設在連接埠 22 上啟用。從您的 PC 連接：`ssh root@192.168.1.1`（在 Windows 上使用 PuTTY）。

   **風險緩解**：若卡住，請使用 TFTP 恢復（在啟動時按住重置按鈕）或序列控制台（需要 UART 轉接器）。

#### 3. **在 OpenWrt 上進行監控（透過 SSH Shell）**
   一旦以 root 身份透過 SSH 登入，路由器就像一個精簡的 Linux 系統。如果需要，可透過 `opkg update && opkg install tcpdump` 安裝套件（內建儲存空間為 128MB，請保持輕量）。

   - **列出所有當前 TCP 連線（靜態檢視）：**
     ```
     ss -tunap
     ```
     - 顯示已建立/監聽中的 TCP socket、連接埠、行程（例如 `tcp ESTAB 0 0 192.168.1.1:80 192.168.1.100:54321 users:(("uhttpd",pid=1234,fd=3))`）。
     - 即時檢視：`watch -n 1 'ss -tunap'`。

   - **即時 TCP 流量擷取：**
     如需安裝：`opkg update && opkg install tcpdump`。
     ```
     tcpdump -i any tcp -n -v
     ```
     - `-i any`：所有介面（br-lan 用於 LAN，eth0.2 用於 WAN）。
     - 過濾 HTTP：`tcpdump -i any tcp port 80 -n -v -A`（`-A` 顯示 HTTP 標頭/請求的 ASCII 負載）。
     - 儲存至檔案：`tcpdump -i any tcp -w /tmp/capture.pcap`（透過 SCP 下載：`scp root@192.168.1.1:/tmp/capture.pcap .`）。
     - 對於 HTTPS（連接埠 443），請注意負載已加密 — 請離線使用 Wireshark 進行分析。

   - **監控 HTTP 請求日誌：**
     - 系統日誌（包括使用 uhttpd 時的網頁伺服器）：`logread | grep uhttpd` 或 `logread -f` 用於即時檢視。
     - 啟用詳細 HTTP 記錄：編輯 `/etc/config/uhttpd`（網頁伺服器設定），加入 `option log_file '/var/log/uhttpd.log'`，然後執行 `/etc/init.d/uhttpd restart`。即時追蹤：`tail -f /var/log/uhttpd.log`（顯示 GET/POST 請求、IP、URL）。
     - 對於完整網路 HTTP：使用上述的 `tcpdump`，或安裝 `ngrep`（`opkg install ngrep`）：`ngrep -d any 'GET|POST|HTTP' -O /tmp/http.pcap`。

   - **防火牆/連線日誌：**
     - 在規則上啟用記錄：`uci set firewall.@rule[0].log='1'; uci commit; /etc/init.d/firewall restart`。
     - 檢視：`logread | grep fw`（顯示丟棄/接受的 TCP 連線）。

#### 道德「駭客」技巧
- **安全性**：設定完成後，請變更 root 密碼（`passwd`），在 `/etc/ssh/sshd_config` 中停用密碼驗證以僅使用金鑰，並將防火牆中的 SSH 限制為僅限 LAN 存取。
- **效能**：T7 具有 256MB RAM — 避免長期進行重度擷取以防止記憶體不足。
- **還原至原廠韌體**：從 360 網站下載官方韌體，透過 OpenWrt 的 sysupgrade 上傳（如果需要，使用 `--force`）。
- 在安全環境中測試；如需 GUI 分析，請將 .pcap 檔案透過 SCP 傳輸到 PC 並在 Wireshark 中開啟。

這提供了全面的可視性。如果原廠 UI 已滿足基本需求，請停留在該環境以避免刷機風險。

[OpenWrt 技術資料：Qihoo 360T7](https://openwrt.org/toh/hwdata/qihoohardware/qihoohardware_360t7)  
[360 T7U 手冊（日誌章節）](https://ipc-pr-cdn.jia.360.cn/ipc-pr/luyouqiT7U.pdf)  
[OpenWrt 記錄指南](https://openwrt.org/docs/guide-user/base-system/log.essentials)  
[360 論壇：日誌匯出](https://bbs.360.cn/forum-7007-1.html)