---
audio: false
generated: true
lang: hant
layout: post
title: 追蹤路由選項
translated: true
type: note
---

Traceroute 是診斷網路路徑的強大工具，雖然基本用法簡單直接，但它也提供進階選項來客製化行為。以下我將概述常用選項，並透過實際範例說明如何進階使用 traceroute。具體選項取決於作業系統（例如 Windows 使用 `tracert`，而 Linux/macOS 使用 `traceroute`），但我會涵蓋最通用的部分。

### 基本用法
- **Linux/macOS**：`traceroute [目的地]`
  - 範例：`traceroute google.com`
- **Windows**：`tracert [目的地]`
  - 範例：`tracert google.com`

這會顯示您與目標之間經過的節點（路由器），以及每個節點的往返時間（RTT）。

---

### 常用 Traceroute 選項
以下是關鍵選項的概要說明，主要針對 Unix-like 系統（Linux/macOS）的 `traceroute` 指令。Windows 的 `tracert` 選項較少，但部分概念相通。

1. **`-n`（不進行 DNS 查詢）**  
   - 跳過將 IP 位址解析為主機名稱的步驟，加速過程並顯示原始 IP。
   - 用法：`traceroute -n google.com`
   - 用途：當 DNS 解析緩慢或您只關心 IP 時非常實用。

2. **`-m [最大節點數]`（設定最大節點數）**  
   - 限制 traceroute 在放棄前檢查的節點數量（預設通常為 30）。
   - 用法：`traceroute -m 15 google.com`
   - 用途：若目標無法到達或距離過遠，可避免無止境的執行。

3. **`-q [查詢次數]`（每個節點的查詢封包數）**  
   - 設定每個節點發送的封包數量（預設為 3）。每個查詢會顯示一個延遲值。
   - 用法：`traceroute -q 1 google.com`
   - 用途：減少輸出雜亂或加速追蹤；增加查詢次數可獲得更可靠的延遲數據。

4. **`-w [等待時間]`（每個節點的等待時間）**  
   - 設定等待回應的時間（以秒為單位），超過則標記該節點為超時。
   - 用法：`traceroute -w 2 google.com`
   - 用途：針對慢速網路調整或減少快速網路下的延遲。

5. **`-p [通訊埠]`（指定通訊埠，UDP 模式）**  
   - 為基於 UDP 的 traceroute 設定目標通訊埠（預設通常為 33434+）。
   - 用法：`traceroute -p 53 google.com`
   - 用途：針對特定服務（例如 port 53 的 DNS）或繞過阻擋 ICMP 的過濾器。

6. **`-I`（使用 ICMP 替代 UDP）**  
   - 從 UDP（許多系統的預設）切換為 ICMP Echo Request 封包。
   - 用法：`traceroute -I google.com`
   - 用途：某些網路可能阻擋 UDP 但允許 ICMP，從而提高可見性。

7. **`-T`（TCP 模式）**  
   - 使用 TCP 封包替代 UDP 或 ICMP，通常使用 SYN 封包。
   - 用法：`traceroute -T -p 80 google.com`
   - 用途：繞過阻擋 ICMP/UDP 的防火牆；非常適合追蹤到網頁伺服器（port 80 = HTTP）。

8. **`-f [起始_ttl]`（從指定 TTL 開始）**  
   - 設定初始 TTL 值，跳過前面的節點。
   - 用法：`traceroute -f 5 google.com`
   - 用途：專注於路徑的特定部分，例如本地網路之外。

9. **`-g [閘道]`（寬鬆來源路由）**  
   - 強制封包通過指定的閘道（若網路支援）。
   - 用法：`traceroute -g 192.168.1.1 google.com`
   - 用途：測試特定路由或繞過預設路由。

10. **`-4` 或 `-6`（強制使用 IPv4 或 IPv6）**  
    - 限制 traceroute 僅使用 IPv4 或 IPv6。
    - 用法：`traceroute -6 google.com`
    - 用途：確保測試特定協定，對雙協定堆疊網路非常有用。

---

### Windows `tracert` 選項
Windows 的選項較少，但以下為主要選項：
- **`-d`**：不進行 DNS 查詢（類似 `-n`）。
- **`-h [最大節點數]`**：最大節點數（類似 `-m`）。
- **`-w [超時時間]`**：等待時間（毫秒）（類似 `-w`）。
- 範例：`tracert -d -h 20 google.com`

---

### 進階使用範例
以下是如何結合選項以達成特定目的：

1. **診斷慢速連線**  
   - 目標：找出延遲飆升的節點。
   - 指令：`traceroute -I -q 5 -w 1 google.com`
   - 用途：使用 ICMP 提高可靠性，5 次查詢獲得更佳延遲統計，1 秒超時以快速進行。

2. **繞過防火牆限制**  
   - 目標：追蹤到被 ICMP 過濾器阻擋的網頁伺服器。
   - 指令：`traceroute -T -p 443 google.com`
   - 用途：在 port 443（HTTPS）上使用 TCP 模擬合法流量，通常會被防火牆允許。

3. **測試 ISP 之外的節點**  
   - 目標：跳過本地節點，專注於外部路由。
   - 指令：`traceroute -f 3 -m 10 google.com`
   - 用途：從第 3 個節點開始（跳過您的路由器/ISP），總共限制為 10 個節點。

4. **比較 IPv4 與 IPv6 路徑**  
   - 目標：查看協定選擇是否影響路由。
   - 指令： 
     - `traceroute -4 google.com`
     - `traceroute -6 google.com`
   - 用途：識別網路路徑或效能上的差異。

5. **用於腳本的靜默快速追蹤**  
   - 目標：為自動化提供快速輸出。
   - 指令：`traceroute -n -q 1 -w 1 google.com > output.txt`
   - 用途：無 DNS 查詢、單次查詢、短超時，輸出重導向至檔案。

---

### 進階使用技巧
- **結合其他工具**：將 traceroute 與 `ping`（用於延遲）或 `mtr`（即時 traceroute）搭配使用，以獲得更深入的洞察。
- **理解網路環境**：防火牆、NAT 或 VPN 可能遮蔽節點（顯示為星號 `*`）——調整協定（ICMP/TCP）以適應。
- **root 權限**：在 Unix 系統上，部分選項（例如 TCP 模式）可能需要 `sudo` 以取得 raw socket 存取權限：`sudo traceroute -T google.com`。

Traceroute 的強大之處在於其靈活性。透過調整選項，您可以根據需求自訂它以排查特定網路問題、繞過限制或詳細分析路由行為。如果您想深入了解特定情境，請隨時告訴我！