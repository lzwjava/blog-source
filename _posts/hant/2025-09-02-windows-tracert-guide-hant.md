---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Windows Tracert 網絡路徑診斷指南
translated: true
type: note
---

在 Windows 系統中，**`tracert`**（全稱 *trace route*）是一個診斷用的命令行工具，用於追蹤封包從您的電腦到目標主機（如網站或 IP 位址）所經過的路徑。它主要用於識別網絡路由中出現延遲或連接問題的位置。

以下是其逐步運作原理：

### 1. 使用遞增 TTL 的 ICMP 回應請求

* `tracert` 發送 **ICMP 回應請求封包**（類似 `ping` 指令）。
* 它會操控 IP 標頭中的 **存活時間（TTL）** 欄位。
* TTL 從 1 開始，然後隨著每次探測遞增（2、3、4……）。

### 2. TTL 過期與「逾時」回應

* 當路由器收到封包時，會將 TTL 減 1。
* 如果 TTL 變為 **0**，路由器會丟棄該封包，並向發送者返回 **ICMP 逾時** 訊息。
* 這讓 `tracert` 能夠識別該路由器的身份（IP/主機名稱）。

### 3. 建立路由路徑

* 當 TTL = 1 時，您會看到第一跳（您的預設閘道）。
* 當 TTL = 2 時，您會看到下一個路由器，依此類推。
* 此過程將持續直到：

  * 目標主機回應 **ICMP 回應回覆**，或
  * 達到最大跳數限制（預設為 30）。

### 4. 測量延遲

* `tracert` 預設對每一跳發送 **三次探測**。
* 它顯示每次探測的 **往返時間（RTT）**，單位為毫秒。
* 如果路由器未回應，您將看到 `*` 而非時間值。

### 5. 範例輸出

```text
正在追蹤 example.com [93.184.216.34] 的路由
最多 30 個躍點：

  1     1 ms    <1 ms     1 ms  192.168.1.1
  2    10 ms     9 ms    11 ms  isp-gateway.example.net [203.0.113.1]
  3    25 ms    23 ms    24 ms  core-router.example.net [198.51.100.1]
  ...
  8    45 ms    46 ms    47 ms  example.com [93.184.216.34]
```

### 6. 行為注意事項

* 部分路由器可能封鎖或降低 ICMP 回應的優先級，導致出現 `* * *`。
* **Windows** 中的 `tracert` 使用 ICMP 回應請求，而 Linux/Unix 上的 `traceroute` 通常使用 **UDP 探測**（儘管可以更改）。
* 防火牆或 ISP 過濾有時可能隱藏部分路由路徑。

---

👉 您是否還需要我解釋 **如何解讀 `tracert` 結果中像 `* * *` 或大幅延遲的情況**，以便您能實際用於故障排除？