---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 以管理員權限監控網絡活動
translated: true
type: note
---

### 以管理員權限監控 HTTP 請求與 TCP 連線

假設您正在使用具有 root/管理員權限的 Linux/Unix 類系統（例如 Ubuntu、CentOS），您可以基於故障排除、安全審計或滲透測試的目的進行合乎道德的網路活動監控。**重要提示：僅在您擁有或已獲得明確授權的系統上執行此操作——未經授權的監控屬違法行為。** 我將重點介紹命令列工具，這些工具輕量且無需圖形介面。

#### 1. **監控所有 TCP 連線**
   使用內建工具如 `ss`（現代版的 `netstat` 替代品）或 `tcpdump` 進行即時擷取。這些工具可顯示活動連線、連接埠及行程。

   - **列出所有當前 TCP 連線（靜態視圖）：**
     ```
     sudo ss -tunap
     ```
     - `-t`：僅顯示 TCP。
     - `-u`：如需 UDP（但您要求的是 TCP）。
     - `-n`：數字格式的連接埠（不進行 DNS 解析）。
     - `-a`：所有狀態（已建立、監聽中等）。
     - `-p`：顯示所屬行程。
     輸出範例：
     ```
     tcp   ESTAB  0      0      192.168.1.10:80     10.0.0.5:54321    users:(("nginx",pid=1234,fd=5))
     ```
     僅顯示監聽中的 socket：`sudo ss -tlnp`。

   - **使用 watch 進行即時監控：**
     ```
     watch -n 1 'sudo ss -tunap'
     ```
     每秒刷新一次。

   - **擷取即時 TCP 流量（封包層級）：**
     若未安裝 `tcpdump`，請先安裝：`sudo apt update && sudo apt install tcpdump`（Debian/Ubuntu）或 `sudo yum install tcpdump`（RHEL/CentOS）。
     ```
     sudo tcpdump -i any tcp -n -v
     ```
     - `-i any`：所有介面。
     - `-n`：不進行名稱解析。
     - `-v`：詳細模式。
     新增 `port 80 or port 443` 以過濾 HTTP/HTTPS：`sudo tcpdump -i any tcp port 80 or tcp port 443 -n -v -A`（`-A` 用於以 ASCII 顯示負載，可查看 HTTP 標頭）。

     儲存至檔案以供後續分析：`sudo tcpdump -i any tcp -w capture.pcap`。

#### 2. **監控 HTTP 請求日誌**
   HTTP 日誌取決於您的網頁伺服器（Apache、Nginx 等）。若未運行網頁伺服器，請使用網路擷取（如上所述）來檢查 HTTP 流量。針對特定伺服器的日誌：

   - **Apache (httpd)：**
     日誌通常位於 `/var/log/apache2/access.log`（Ubuntu）或 `/var/log/httpd/access_log`（CentOS）。
     ```
     sudo tail -f /var/log/apache2/access.log
     ```
     - 即時顯示請求：IP、時間戳記、方法（GET/POST）、URL、狀態碼。
     範例行：`192.168.1.100 - - [08/Oct/2025:10:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234`。

     查看所有日誌：`sudo grep "GET\|POST" /var/log/apache2/access.log | less`。

   - **Nginx：**
     日誌位於 `/var/log/nginx/access.log`。
     ```
     sudo tail -f /var/log/nginx/access.log
     ```
     格式與 Apache 類似。

   - **若無網頁伺服器（通用 HTTP 嗅探）：**
     使用帶有 `-A` 選項的 `tcpdump` 來傾印 HTTP 負載，或安裝 `ngrep` 進行正規表示式匹配：
     ```
     sudo apt install ngrep  # 如需則安裝
     sudo ngrep -d any 'GET|POST|HTTP' -O http_capture.pcap
     ```
     此命令會過濾並記錄 HTTP 方法。

   - **進階：設定透明代理以完整記錄日誌。**
     安裝 Squid 代理：`sudo apt install squid`。
     配置 `/etc/squid/squid.conf` 以記錄所有 HTTP（新增 `access_log /var/log/squid/access.log squid`）。
     透過 iptables 重導流量：`sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 3128`。
     然後追蹤 Squid 日誌：`sudo tail -f /var/log/squid/access.log`。

#### 「駭客」技巧（道德滲透測試）
- **結合工具：** 將 `tcpdump` 輸出導向 `grep` 以搜尋特定模式，例如 `sudo tcpdump -i any tcp port 80 -A | grep "User-Agent"`。
- **使用 Wireshark 視覺化分析：** 安裝 Wireshark（`sudo apt install wireshark`），以 root 權限執行，並開啟您的 `.pcap` 檔案。
- **安全強化：** 監控完成後，若日誌含敏感資訊請清除：`sudo truncate -s 0 /var/log/access.log`。
- **跨平台注意事項：** 在 Windows 上（需管理員權限），使用 `netstat -anob` 查看 TCP 連線，並使用事件檢視器查看日誌。在 macOS 上，使用 `netstat -an` 和 `tcpdump`。

此設定無需外部工具即可提供全面的可視性。建議先在虛擬機器中測試。

[Linux ss 指令手冊頁](https://man7.org/linux/man-pages/man8/ss.8.html)  
[Tcpdump 教學](https://www.tcpdump.org/manpages/tcpdump.1.html)  
[Apache 存取日誌格式](https://httpd.apache.org/docs/2.4/logs.html)