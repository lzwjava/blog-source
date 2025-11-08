---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 最大傳輸單元簡介
translated: true
type: note
---

### 什麼是網路中的 MTU？

**MTU** 代表 **最大傳輸單元**。它指的是在無需分割成更小數據包的情況下，能夠透過網路介面或協定傳輸的單一數據封包的最大尺寸（以位元組為單位）。

#### 關鍵細節：
- **典型數值**：
  - 乙太網路通常使用 1500 位元組的 MTU（這是大多數 IP 基礎網路的標準）。
  - 在支援的硬體上，巨型幀可達到 9000 位元組或更多。
  - IPv6 的最小 MTU 為 1280 位元組。
- **為何重要**：
  - **效率**：較大的 MTU 能減少開銷（例如每個數據單元的標頭更少），從而提升吞吐量。
  - **分段問題**：如果封包超過鏈路的 MTU，它可能會被分割（分段）或丟棄，導致延遲、重傳或錯誤（例如「封包過大」的 ICMP 訊息）。
  - **路徑 MTU 探索 (PMTUD)**：裝置使用此過程來找出網路路徑上最小的 MTU，並相應調整封包大小以避免分段。
- **常見問題**：裝置間 MTU 不匹配（例如 VPN 隧道）可能導致連線問題。你可以使用如 `ifconfig`（Linux/macOS）或 `netsh`（Windows）等工具來檢查或設定 MTU。

簡而言之，MTU 定義了封包的「最大承載」限制，在網路設計中平衡了速度與相容性。

深入閱讀：[最大傳輸單元 - 維基百科](https://en.wikipedia.org/wiki/Maximum_transmission_unit)