---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: Wi-Fi 7 概述與主要功能
translated: true
type: note
---

### Wi-Fi 7 概述
Wi-Fi 7，官方名稱為 IEEE 802.11be（極高吞吐量，EHT），是繼 Wi-Fi 6 和 6E 之後的最新無線標準。該標準於 2024 年初獲得 Wi-Fi 聯盟認證，重點在於實現顯著更高的速度、降低延遲，並提升擁擠網絡中的效率。它運作於 2.4 GHz、5 GHz 和 6 GHz 頻段（建立在 Wi-Fi 6E 新增的 6 GHz 基礎上），並向下兼容舊設備，但要充分發揮優勢則需兩端均配備 Wi-Fi 7 硬件。理論峰值速度可達 46 Gbps，比 Wi-Fi 6 快約 4.8 倍，使其成為 8K 串流、AR/VR、雲端遊戲和高密度物聯網環境的理想選擇。

### 主要新功能
- **多鏈路操作 (MLO)**：一項旗艦創新技術，允許設備在單一連線中同時跨越多個頻段（例如 2.4 GHz、5 GHz 和 6 GHz）連接。這可聚合頻寬以實現更高吞吐量，與 Wi-Fi 6 相比延遲降低高達 4 倍，並通過動態避開干擾或擁塞來提高可靠性。與先前標準的單頻段操作不同，MLO 可在網狀網絡中實現無縫切換，並提升實時應用的穩定性。
  
- **更寬的通道頻寬 (320 MHz)**：將 Wi-Fi 6/6E 的 160 MHz 上限加倍，主要在 6 GHz 頻段實現，允許更多數據同時傳輸，如同為高速公路增加額外車道。這使網絡容量提升高達 5 倍，是整體速度提升的關鍵。

- **4096-QAM 調變 (4K-QAM)**：每個符號編碼 12 位元（相較於 Wi-Fi 6 的 1024-QAM 為 10 位元，或 Wi-Fi 5 的 256-QAM 為 8 位元），在每次傳輸中壓縮多 20% 的數據。此技術需要更清晰的信號，因此在低干擾環境中最有效，可提升高頻寬任務的效率。

- **增強型 OFDMA 與多資源單元穿孔技術**：在 Wi-Fi 6 的 OFDMA 基礎上引入多資源單元 (Multi-RU) 分配，允許單一設備使用多個資源單元進行更精細的流量管理。穿孔技術在受干擾的子通道中「打孔」，以挽救可用頻譜，減少繁忙區域的浪費——此功能在早期 Wi-Fi 版本中不可用。

- **16 個空間流與改進的 MU-MIMO**：將 Wi-Fi 6 的 8 個流加倍至 16 個，搭配升級的多用戶 MIMO，可同時服務更多設備而不產生瓶頸。這提升了多設備家庭或辦公室的整體吞吐量。

- **更低延遲與效率優化**：諸如更短的保護間隔（0.8 μs，相較於 Wi-Fi 6 的 3.2 μs）和增強型目標喚醒時間 (TWT) 等功能，可將設備電池壽命延長 20-30%，同時最小化延遲。還包括更好的前向兼容幀格式和隱式通道探測，以實現更快的波束成形。

### 優勢與影響
這些升級使 Wi-Fi 7 在高密度場景（例如體育場館或智慧城市）中更具韌性，並為新興技術提供未來保障。實際速度會有所差異（理想情況下預計為 5-10 Gbps），但早期採用者報告稱 4K/8K 影片更流暢、遊戲無延遲，且能更好地處理 100 多個連接設備。截至 2025 年底，來自 TP-Link、Netgear 和 Intel 等品牌的 Wi-Fi 7 路由器和設備已廣泛上市，完整生態系統的推廣正在加速。

### 參考資料
- [What is Wi-Fi 7? Everything You Need to Know](https://www.wired.com/story/what-is-wi-fi-7/)
- [What is WiFi 7? How Does WiFi 7 Work?](https://www.tp-link.com/us/wifi7/)
- [Wi-Fi 7 - Wikipedia](https://en.wikipedia.org/wiki/Wi-Fi_7)
- [Key Features & Benefits of WiFi 7](https://www.netgear.com/au/hub/wifi/mesh/benefits-wifi-7/)