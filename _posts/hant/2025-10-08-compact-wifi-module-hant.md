---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 物聯網用微型WiFi模組
translated: true
type: note
---

ESP-01S 是一款基於樂鑫系統 ESP8266 微控制器晶片的緊湊型 WiFi 模組。作為原始 ESP-01 的升級版本，它主要設計用於物聯網應用場景，可為 Arduino 或 Raspberry Pi 等其他微控制器增添無線連接功能。

### 主要特性：
- **WiFi 能力**：支援 802.11 b/g/n 標準，可作為獨立 WiFi 存取點、工作站或雙模式運行。內建 TCP/IP 協議堆疊，便於網路整合。
- **處理器與記憶體**：搭載 Tensilica L106 32 位元 RISC CPU，運行頻率 80 MHz（可超頻至 160 MHz）。配備 1MB（部分型號為 4MB）SPI 快閃記憶體，用於程式碼與資料儲存。
- **I/O 引腳**：採用 8 針佈局（VCC、GND、CH_PD、RST、TX、RX、GPIO0、GPIO2），支援序列通訊（UART）及基礎 GPIO 控制，例如驅動 LED 或繼電器。
- **電源與尺寸**：工作電壓 3.3V（不兼容 5V），傳輸時功耗約 80mA，尺寸僅 24.75 x 14.5 mm，非常適合小型專案。
- **相較 ESP-01 的改進**：優化 PCB 佈線提升 WiFi 訊號強度、增加快閃記憶體容量（1MB 對比 512KB）、並將狀態指示燈改為 GPIO2 控制的藍色 LED。

### 常見用途：
- 將感測器或裝置連接至網際網路，實現遠端監控/控制
- 透過 Arduino IDE（需安裝 ESP8266 開發板支援）或序列 AT 指令進行程式編寫
- 開發智能家居裝置原型，如 WiFi 開關或氣象站

使用前需準備 USB 轉序列介面卡（如 FTDI）來燒錄韌體，因模組未內建 USB 埠。該模組價格低廉（低於 5 美元）且容易取得，但操作時需小心避免損壞引腳。

[如何使用 ESP-01S 模組](https://www.taydaelectronics.com/datasheets/files/ESP-01S.pdf)  
[ESP8266 ESP-01 入門指南](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/)  
[ESP-01S 模組介紹](https://lonelybinary.com/en-us/blogs/learn/what-is-esp-01s)  
[ESP-01S / ESP01S ESP8266 模組](https://hobbycomponents.com/esp8266/1176-esp-01s-esp01s-esp8266-module)