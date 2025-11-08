---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 解讀 ip addr show enp4s0 輸出結果
translated: true
type: note
---

### 解構你的 `ip addr show enp4s0` 輸出結果

這個指令顯示了你的乙太網路介面（enp4s0）的詳細資訊，該介面負責處理我們之前討論的路由表中的本地區域網路連接。它目前正常運作中——這對基礎連線來說非常理想。我將逐行解析，然後進行總結。

#### 關鍵部分解析
- **介面狀態**：  
  `2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000`  
  - 索引 2（第二個介面，位於 lo 之後）。  
  - 標誌：支援廣播/多播，完全啟動（鏈路已偵測且運作中）。  
  - MTU：1500 位元組（標準乙太網路框架大小——無巨型框架）。  
  - 佇列規則：fq_codel（為低延遲流量設計的公平佇列，常見於現代 Linux 系統）。  
  - 狀態：UP（準備好發送/接收）。

- **鏈路層（MAC 位址）**：  
  `link/ether 04:7c:16:d9:54:5b brd ff:ff:ff:ff:ff:ff`  
  - 你的硬體 MAC：04:7c:16:d9:54:5b（此網路卡獨有）。  
  - 廣播位址：ff:ff:ff:ff:ff:ff（乙太網路廣播的全 1 位址）。

- **IPv4 位址**：  
  `inet 192.168.1.35/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0`  
  `valid_lft 4790sec preferred_lft 4790sec`  
  - IP：192.168.1.35，子網路遮罩為 /24（255.255.255.0）。與你路由表中的 "src 192.168.1.35" 相符。  
  - 廣播位址：192.168.1.255（用於子網路內的廣播）。  
  - 範圍：global（可在此主機之外路由）。  
  - 動態分配：透過 DHCP 分配（來自你的路由器 192.168.1.1）。  
  - 無前綴路由：不會自動添加連接路由（但核心仍然添加了，如 `ip route` 所示）。  
  - 租約：約 79 分鐘後到期（4790 秒），然後會續約。

- **IPv6 位址**：  
  `inet6 fe80::a884:a0f6:e8b4:4a7d/64 scope link noprefixroute`  
  `valid_lft forever preferred_lft forever`  
  - 本地鏈路 IPv6：fe80::...（由 MAC 自動生成；僅用於本地鏈路通訊，如鄰居發現）。  
  - 前綴長度 /64，範圍為 link（無法在此介面之外路由）。  
  - 永久有效（不會過期）。

#### 快速總結表格

| 項目         | 數值/詳細資訊                   | 意義說明 |
|--------------|--------------------------------|---------------|
| **狀態**     | UP, MTU 1500                  | 介面處於活動狀態，處理標準封包。 |
| **MAC**      | 04:7c:16:d9:54:5b             | 你的裝置在網路上的硬體位址。 |
| **IPv4**     | 192.168.1.35/24 (DHCP)        | 本地區域網路 IP；前往此子網路的路由會透過 enp4s0。 |
| **IPv6**     | fe80::a884:a0f6:e8b4:4a7d/64  | 僅限本地的 IPv6；對 IPv6 鄰居相關功能有用。 |
| **租約**     | 剩餘約 79 分鐘                | DHCP 即將更新——如有需要，可使用 `dhclient -r enp4s0 && dhclient enp4s0` 檢查。 |

這個設定解釋了為什麼你的預設路由指向這裡以存取網際網路，以及為什麼本地的 192.168.1.x 流量是直接的。如果你在區域網路內進行 ping，它會透過 ARP 查詢 MAC 並從這個介面發送框架。

一切看起來都正常嗎，還是有什麼問題（例如沒有 IPv6 全域位址，或連線中斷）？如果你分享其他介面的 `ip addr` 或 `ping` 結果，我可以進一步分析。接下來要做什麼——測試 Docker 橋接，還是其他事情？