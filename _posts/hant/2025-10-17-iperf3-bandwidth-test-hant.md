---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: iPerf3 網絡頻寬測試工具
translated: true
type: note
---

### 什麼是 iPerf3？

iPerf3 是一款開源命令行工具，專為測量網絡頻寬和效能而設計。它通常用於通過在兩個端點（一個作為伺服器，另一個作為客戶端）之間模擬流量來測試 IP 網絡上可達到的最大吞吐量。這有助於診斷本地或廣域網絡中的延遲、封包遺失和瓶頸等問題。

#### 主要功能：
- **支援的協定**：TCP、UDP 和 SCTP，適用於靈活的測試場景。
- **自訂設定**：允許調整緩衝區大小、測試持續時間和雙向流量等參數。
- **輸出結果**：提供有關頻寬、抖動和數據報遺失的詳細統計數據。

#### 基本使用範例：
要測試兩台機器之間的頻寬：
1. 在伺服器上：`iperf3 -s`（啟動伺服器）。
2. 在客戶端：`iperf3 -c <伺服器_IP>`（連接並預設運行 10 秒測試）。

它輕量、跨平台（適用於 Linux、Windows、macOS），並被網絡管理員、開發人員和 IT 專業人士廣泛用於故障排除。

#### 歷史背景：
iPerf3 是對原始 iPerf 工具的完全重寫，由 ESnet（能源科學網絡）於 2009 年啟動，並於 2014 年首次發布。這次重新設計旨在實現更小、更易維護的程式碼庫，同時提高準確性。

欲了解更多詳情，請查閱官方網站或 GitHub 存儲庫。

### 參考資料
- [iPerf - The TCP, UDP and SCTP network bandwidth measurement tool](https://iperf.fr/)
- [iperf3: A TCP, UDP, and SCTP network bandwidth measurement tool](https://github.com/esnet/iperf)
- [Iperf - Wikipedia](https://en.wikipedia.org/wiki/Iperf)