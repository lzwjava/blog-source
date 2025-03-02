---
audio: false
generated: false
lang: hant
layout: post
title: 紅襪隊在行動
translated: true
---

當然可以！我將指導您如何使用您的Mac電腦設置Shadowsocks代理，並配置您的OpenWRT路由器，以將所有連接設備的流量通過此代理路由。此設置涉及以下主要步驟：

1. 在macOS上設置Shadowsocks客戶端（使用Shadowsocks-NG或Clash）
2. 配置macOS以允許外部代理連接
3. 為您的Mac分配靜態IP
4. 在OpenWRT上安裝和配置Redsocks
5. 將OpenWRT的流量重定向通過macOS代理
6. 測試代理設置

讓我們詳細介紹每個步驟。

---

## 1. 在macOS上設置Shadowsocks客戶端

您可以使用Shadowsocks-NG或Clash作為您的Shadowsocks客戶端。以下是兩者的說明。

### 選項A：使用Shadowsocks-NG

Shadowsocks-NG是macOS上流行且用戶友好的Shadowsocks客戶端。

#### 步驟1：下載並安裝Shadowsocks-NG

1. 下載Shadowsocks-NG：
   - 訪問[Shadowsocks-NG GitHub Releases頁面](https://github.com/shadowsocks/ShadowsocksX-NG/releases)。
   - 下載最新的`.dmg`文件。

2. 安裝應用程序：
   - 打開下載的`.dmg`文件。
   - 將ShadowsocksX-NG應用程序拖到您的應用程序文件夾中。

3. 啟動Shadowsocks-NG：
   - 從您的應用程序文件夾中打開ShadowsocksX-NG。
   - 您可能需要在系統偏好設置中授予應用程序必要的權限。

#### 步驟2：配置Shadowsocks-NG

1. 打開偏好設置：
   - 點擊菜單欄中的ShadowsocksX-NG圖標。
   - 選擇“打開ShadowsocksX-NG” > “偏好設置”。

2. 添加新服務器：
   - 導航到“服務器”選項卡。
   - 點擊“+”按鈕以添加新服務器。

3. 導入Shadowsocks URL：
   - 複製您的Shadowsocks URL：
     ```
     ss://[ENCRYPTED_PASSWORD]@xxx.xxx.xxx.xxx:xxxxx/?outline=1
     ```
   - 導入方法：
     - 點擊“導入”。
     - 粘貼您的Shadowsocks URL。
     - Shadowsocks-NG應自動解析並填寫服務器詳細信息。

4. 設置本地代理：
   - 確保“啟用SOCKS5代理”已勾選。
   - 記下本地端口（默認通常為`1080`）。

5. 保存並激活：
   - 點擊“確定”以保存服務器。
   - 切換“啟用Shadowsocks”開關為ON。

### 選項B：使用Clash

Clash是一個支持多種協議（包括Shadowsocks）的多功能代理客戶端。

#### 步驟1：下載並安裝Clash

1. 下載Clash for macOS：
   - 訪問[Clash GitHub Releases頁面](https://github.com/Dreamacro/clash/releases)。
   - 下載最新的Clash for macOS二進制文件。

2. 安裝應用程序：
   - 將下載的Clash應用程序移動到您的應用程序文件夾中。

3. 啟動Clash：
   - 從您的應用程序文件夾中打開Clash。
   - 您可能需要在系統偏好設置中授予必要的權限。

#### 步驟2：配置Clash

1. 訪問配置文件：
   - Clash使用YAML配置文件。您可以使用TextEdit或Visual Studio Code等文本編輯器創建或編輯它。

2. 添加您的Shadowsocks服務器：
   - 創建一個配置文件（例如，`config.yaml`），內容如下：

     ```yaml
     port: 7890
     socks-port: 7891
     allow-lan: true
     mode: Rule
     log-level: info

     proxies:
       - name: "MyShadowsocks"
         type: ss
         server: xxx.xxx.xxx.xxx
         port: xxxxx
         cipher: chacha20-ietf-poly1305
         password: "xxxxxx"

     proxy-groups:
       - name: "Default"
         type: select
         proxies:
           - "MyShadowsocks"
           - "DIRECT"

     rules:
       - MATCH,Default
     ```

     注意：
     - `port`和`socks-port`定義Clash將監聽的HTTP和SOCKS5代理端口。
     - `allow-lan: true`允許LAN設備使用代理。
     - `proxies`部分包括您的Shadowsocks服務器詳細信息。
     - `proxy-groups`和`rules`確定流量如何路由。

3. 使用配置啟動Clash：
   - 啟動Clash並確保它使用您的`config.yaml`文件。
   - 啟動Clash時可能需要指定配置路徑。

4. 驗證代理是否運行：
   - 確保Clash已激活並連接到您的Shadowsocks服務器。
   - 檢查菜單欄圖標以獲取狀態。

---

## 2. 配置macOS以允許外部代理連接

默認情況下，Shadowsocks客戶端將代理綁定到`localhost`（`127.0.0.1`），這意味著只有Mac可以使用代理。要允許您的OpenWRT路由器使用此代理，您需要將代理綁定到Mac的LAN IP。

### 對於Shadowsocks-NG：

1. 打開偏好設置：
   - 點擊菜單欄中的ShadowsocksX-NG圖標。
   - 選擇“打開ShadowsocksX-NG” > “偏好設置”。

2. 轉到高級選項卡：
   - 導航到“高級”選項卡。

3. 設置監聽地址：
   - 將“監聽地址”從`127.0.0.1`更改為`0.0.0.0`以允許來自任何接口的連接。
   - 或者，指定Mac的LAN IP（例如，`192.168.1.xxx`）。

4. 保存並重新啟動Shadowsocks-NG：
   - 點擊“確定”以保存更改。
   - 重新啟動Shadowsocks-NG客戶端以應用新設置。

### 對於Clash：

1. 編輯配置文件：
   - 確保在您的`config.yaml`中啟用了`allow-lan: true`設置。

2. 綁定到所有接口：
   - 在配置中，設置`allow-lan: true`通常會將代理綁定到所有可用接口，包括LAN。

3. 重新啟動Clash：
   - 重新啟動Clash客戶端以應用更改。

---

## 3. 為您的Mac分配靜態IP

為了確保OpenWRT路由器和Mac之間的連接穩定，請為您的Mac分配一個靜態IP。

### 在macOS上分配靜態IP的步驟：

1. 打開系統偏好設置：
   - 點擊Apple菜單並選擇“系統偏好設置”。

2. 導航到網絡設置：
   - 點擊“網絡”。

3. 選擇您的活動連接：
   - 從左側邊欄中選擇“Wi-Fi”或“以太網”，具體取決於您的Mac如何連接到路由器。

4. 配置IPv4設置：
   - 點擊“高級...”。
   - 轉到“TCP/IP”選項卡。
   - 將“配置IPv4”從“使用DHCP”更改為“手動”。

5. 設置靜態IP地址：
   - IP地址：選擇一個在路由器DHCP範圍之外的IP以防止衝突（例如，`192.168.1.xxx`）。
   - 子網掩碼：通常為`255.255.255.0`。
   - 路由器：您的路由器IP地址（例如，`192.168.1.1`）。
   - DNS服務器：您可以使用路由器的IP或其他DNS服務，如`8.8.8.8`。

6. 應用設置：
   - 點擊“確定”，然後點擊“應用”以保存更改。

---

## 4. 在OpenWRT上安裝和配置Redsocks

Redsocks是一個透明的socks重定向器，允許您通過SOCKS5代理路由網絡流量。我們將使用Redsocks將OpenWRT的流量重定向通過在您的Mac上運行的Shadowsocks代理。

### 步驟1：安裝Redsocks

1. 更新軟件包列表：

   ```bash
   ssh root@<router_ip>
   opkg update
   ```

2. 安裝Redsocks：

   ```bash
   opkg install redsocks
   ```

   *如果Redsocks在您的OpenWRT存儲庫中不可用，您可能需要手動編譯或使用替代軟件包。*

### 步驟2：配置Redsocks

1. 創建或編輯Redsocks配置文件：

   ```bash
   vi /etc/redsocks.conf
   ```

2. 添加以下配置：

   ```conf
   base {
       log_debug = on;
       log_info = on;
       log = "file:/var/log/redsocks.log";
       daemon = on;
       redirector = iptables;
   }

   redsocks {
       local_ip = 0.0.0.0;
       local_port = 12345;  # Redsocks監聽的本地端口
       ip = xxx.xxx.xxx.xxx;  # Mac的靜態IP
       port = xxxxx;          # Shadowsocks-NG的本地SOCKS5代理端口
       type = socks5;
       login = "";           # 如果您的代理需要身份驗證
       password = "";
   }
   ```

   注意：
   - `local_port`：Redsocks監聽來自iptables重定向的傳入連接的端口。
   - `ip`和`port`：指向您的Mac的Shadowsocks SOCKS5代理（基於之前的步驟的`xxx.xxx.xxx.xxx:xxxxx`）。
   - `type`：設置為`socks5`，因為Shadowsocks提供SOCKS5代理。

3. 保存並退出：
   - 按`ESC`，輸入`:wq`，然後按`Enter`。

4. 創建日誌文件：

   ```bash
   touch /var/log/redsocks.log
   chmod 644 /var/log/redsocks.log
   ```

### 步驟3：啟動Redsocks服務

1. 啟用Redsocks在啟動時啟動：

   ```bash
   /etc/init.d/redsocks enable
   ```

2. 啟動Redsocks：

   ```bash
   /etc/init.d/redsocks start
   ```

3. 驗證Redsocks是否運行：

   ```bash
   ps | grep redsocks
   ```

   您應該看到一個Redsocks進程正在運行。

---

## 5. 將OpenWRT的流量重定向通過macOS代理

現在Redsocks已在OpenWRT上設置完畢，配置iptables以將所有出站TCP流量重定向通過Redsocks，Redsocks再將其路由通過您的Mac的Shadowsocks代理。

### 步驟1：配置iptables規則

1. 添加iptables規則以重定向流量：

   ```bash
   # 將所有TCP流量重定向到Redsocks（除了代理本身的流量）
   iptables -t nat -N REDSOCKS
   iptables -t nat -A REDSOCKS -d xxx.xxx.xxx.xxx -p tcp --dport xxxxx -j RETURN
   iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345

   # 將REDSOCKS鏈應用於所有出站流量
   iptables -t nat -A OUTPUT -p tcp -j REDSOCKS
   iptables -t nat -A PREROUTING -p tcp -j REDSOCKS
   ```

   解釋：
   - 創建新鏈：`REDSOCKS`
   - 排除代理流量：確保目的地為代理本身的流量不被重定向。
   - 重定向其他TCP流量：將其他TCP流量轉發到Redsocks的監聽端口（`12345`）。

2. 保存iptables規則：

   要使這些規則在重啟後持久化，請將它們添加到防火牆配置中。

   ```bash
   vi /etc/firewall.user
   ```

   添加iptables規則：

   ```bash
   # 將所有TCP流量重定向到Redsocks（除了代理）
   iptables -t nat -N REDSOCKS
   iptables -t nat -A REDSOCKS -d xxx.xxx.xxx.xxx -p tcp --dport xxxxx -j RETURN
   iptables -t nat -A REDSOCKS -p tcp -j REDIRECT --to-ports 12345

   # 應用REDSOCKS鏈
   iptables -t nat -A OUTPUT -p tcp -j REDSOCKS
   iptables -t nat -A PREROUTING -p tcp -j REDSOCKS
   ```

   保存並退出：
   - 按`ESC`，輸入`:wq`，然後按`Enter`。

3. 重新啟動防火牆以應用更改：

   ```bash
   /etc/init.d/firewall restart
   ```

### 步驟2：驗證流量是否被重定向

1. 檢查Redsocks日誌：

   ```bash
   cat /var/log/redsocks.log
   ```

   您應該看到日誌指示流量正在通過Redsocks處理。

2. 從客戶端設備測試：
   - 將設備連接到您的OpenWRT路由器。
   - 訪問網站或執行使用互聯網的操作。
   - 通過檢查外部IP地址（例如，通過[WhatIsMyIP.com](https://www.whatismyip.com/)）驗證流量是否通過Shadowsocks代理路由，以查看是否反映代理的IP。

---

## 6. 測試代理設置

通過執行以下測試確保整個設置按預期工作。

### 步驟1：在Mac上驗證Shadowsocks連接

1. 檢查Shadowsocks客戶端狀態：
   - 確保Shadowsocks-NG或Clash已主動連接到Shadowsocks服務器。
   - 驗證本地代理（例如，`xxx.xxx.xxx.xxx:xxxxx`）是否可訪問。

2. 本地測試代理：
   - 在您的Mac上，打開瀏覽器並將其配置為使用`localhost:1080`作為SOCKS5代理。
   - 訪問[WhatIsMyIP.com](https://www.whatismyip.com/)以確認IP是否匹配Shadowsocks服務器。

### 步驟2：驗證OpenWRT的流量是否通過代理路由

1. 檢查OpenWRT的外部IP：
   - 從連接到OpenWRT的設備，訪問[WhatIsMyIP.com](https://www.whatismyip.com/)以查看IP是否反映Shadowsocks服務器的IP。

2. 監控Redsocks日誌：
   - 在OpenWRT上，監控Redsocks日誌以確保流量正在被重定向。
   
   ```bash
   tail -f /var/log/redsocks.log
   ```

3. 如有必要進行故障排除：
   - 如果流量未正確路由：
     - 確保Mac上的Shadowsocks客戶端正在運行且可訪問。
     - 驗證iptables規則是否正確設置。
     - 檢查Mac和OpenWRT上的防火牆設置。

---

## 其他注意事項

### 1. 安全性

- 保護您的代理：
  - 確保只有受信任的設備可以訪問代理。由於您正在通過Redsocks重定向所有流量，請確保Mac的防火牆僅允許來自OpenWRT路由器的連接。

  在macOS上：
  
  - 轉到系統偏好設置 > 安全與隱私 > 防火牆。
  - 配置防火牆以僅允許來自OpenWRT路由器IP的代理端口（`xxxxx`）的傳入連接。

- 身份驗證：
  - Shadowsocks已經通過加密提供了一定程度的安全性。確保使用強密碼和加密方法。

### 2. 性能

- 路由器資源：
  - 運行Redsocks等代理服務可能會消耗OpenWRT路由器上的額外CPU和內存。確保您的路由器有足夠的資源。

- Mac性能：
  - 確保您的Mac保持開機並連接到網絡以維持代理可用性。

### 3. 維護

- 監控日誌：
  - 定期檢查Redsocks和Shadowsocks日誌以查找任何異常活動或錯誤。

- 更新軟件：
  - 保持OpenWRT、Redsocks和您的Shadowsocks客戶端更新，以受益於安全補丁和性能改進。

### 4. 替代方法

雖然使用Mac作為中介代理服務器是可行的，但考慮以下替代方案以實現更簡單的設置：

- 直接在OpenWRT上配置Shadowsocks客戶端：
  - OpenWRT通過`shadowsocks-libev`等軟件包直接支持Shadowsocks。此方法消除了對Mac中介的需求。

- 使用專用代理/VPN設備：
  - 像Raspberry Pi這樣的設備可以運行代理服務並充當專用網關。

---

## 結論

通過按照上述步驟操作，您已將Mac設置為Shadowsocks代理服務器，並配置了OpenWRT路由器以將所有連接設備的流量通過此代理路由。此設置通過利用Shadowsocks協議增強了網絡的隱私和控制。

關鍵點回顧：

1. Mac上的Shadowsocks客戶端：
   - 安裝並配置了Shadowsocks-NG或Clash與您提供的Shadowsocks URL。
   - 配置客戶端以監聽Mac的LAN IP。

2. 代理可訪問性：
   - 為Mac分配了靜態IP以確保一致的代理訪問。
   - 配置了macOS防火牆以允許傳入代理連接。

3. OpenWRT配置：
   - 安裝並配置了Redsocks以將所有出站TCP流量重定向通過Shadowsocks代理。
   - 應用了必要的iptables規則以強制流量重定向。

4. 測試：
   - 通過檢查外部IP地址驗證了來自連接設備的流量