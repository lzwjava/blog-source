---
audio: false
generated: true
lang: hant
layout: post
title: MicroPython：微控制器的 Python 語言
translated: true
type: note
---

MicroPython 是一種精簡高效的 Python 3 程式語言實作版本，專為微控制器、嵌入式系統與資源受限環境優化。它將 Python 的簡潔性與多功能性帶入硬體程式設計領域，讓開發者能為記憶體和處理能力有限的小型裝置編寫程式碼。以下是關於 MicroPython 的全面介紹，涵蓋其起源、特性、應用等範疇。

### 1. **什麼是 MicroPython？**
MicroPython 是專為微控制器與嵌入式裝置設計的輕量級開源 Python 3 版本。它保留了大多數 Python 語法與核心功能，但針對僅有 16KB RAM 與 256KB 儲存空間的環境進行了適配。由 Damien George 於 2013 年創建，旨在透過 Python 的高可讀性語法取代 C 或組合語言等底層語言，降低嵌入式程式設計的門檻。

與運行於資源充足的通用電腦的標準 Python 不同，MicroPython 經過深度優化，能在物聯網裝置、感測器、機器人等嵌入式系統常見的微控制器限制下運作。它包含精簡直譯器、Python 標準庫子集，以及用於控制 GPIO 引腳、I2C、SPI、UART、PWM 等周邊裝置的硬體專用模組。

### 2. **MicroPython 主要特性**
MicroPython 融合了 Python 的易用性與嵌入式系統專屬功能：
- **Python 3 語法**：支援大多數 Python 3 語法，包含函式、類別、列表、字典與異常處理，讓 Python 開發者能快速上手
- **小巧記憶體佔用**：優化至可在最低 16KB RAM 與 256KB 儲存空間的裝置上運行
- **互動式 REPL**：透過序列連接或 USB 提供即時編程與除錯的讀取-執行-輸出循環環境
- **硬體專用模組**：內建 `machine` 與 `micropython` 等程式庫，用於控制硬體元件（如 GPIO、ADC、計時器與通訊協定）
- **檔案系統支援**：多數 MicroPython 移植版本包含小型檔案系統，可於快閃記憶體或 SD 卡儲存腳本與資料
- **跨平台支援**：相容於多種微控制器平台，包含 ESP8266、ESP32、STM32、Raspberry Pi Pico 等
- **可擴充架構**：支援自訂模組，並可整合 C/C++ 以處理效能關鍵任務
- **低功耗設計**：針對能源效率優化，適用於電池供電的物聯網裝置
- **開源授權**：採用 MIT 授權，可免費使用、修改與分發

### 3. **發展歷程**
MicroPython 由澳洲物理學家兼程式設計師 Damien George 透過 2013 年成功募資的 Kickstarter 專案創建。目標是將 Python 的簡潔性引入微控制器領域，讓業餘愛好者、教育者與專業人員更容易接觸嵌入式程式設計。首個穩定版於 2014 年發布，針對專為 MicroPython 設計的 PyBoard 微控制器開發板。

此後 MicroPython 社群持續成長，匯聚全球開發者的貢獻。現已支援眾多微控制器平台，其生態系涵蓋工具、程式庫與技術文件。該專案持續積極維護，定期更新以提升效能、新增功能並支援新硬體。

### 4. **運作原理**
MicroPython 由兩大核心元件構成：
- **直譯器**：精簡的 Python 3 直譯器，可在微控制器上執行 Python 程式碼。它會將 Python 腳本編譯為位元組碼，並在輕量級虛擬機器中運行
- **執行環境與程式庫**：執行環境提供核心 Python 功能，並包含與微控制器周邊裝置互動的硬體專用模組

當 MicroPython 腳本運行時，可實現以下功能：
- 直接控制硬體（如點亮 LED、讀取感測器）
- 透過 I2C、SPI 或 MQTT 等通訊協定傳輸資料
- 從裝置檔案系統儲存與執行腳本
- 透過 REPL 進行即時除錯或指令操作

MicroPython 韌體會針對特定微控制器架構（如 ARM Cortex-M、ESP32）進行適配。使用者需將韌體刷入裝置，再透過 `ampy`、`rshell` 等工具或 Thonny、Mu 等整合開發環境上傳 Python 腳本。

### 5. **支援硬體**
MicroPython 可在多種微控制器平台上運行，包含：
- **ESP8266 與 ESP32**：因低成本與網路功能，廣泛應用於物聯網及 Wi-Fi 專案
- **Raspberry Pi Pico (RP2040)**：具雙核 ARM Cortex-M0+ 的多功能低成本開發板
- **STM32 系列**：常用於工業與高效能嵌入式應用
- **PyBoard**：原創 MicroPython 開發板，專為開發與原型設計打造
- **其他平台**：包含 BBC micro:bit、Arduino 與各種 ARM 架構微控制器

各平台均有專屬韌體建置版本，以最佳化硬體功能運用。例如 ESP32 韌體包含 Wi-Fi 與藍牙支援，STM32 韌體則支援 CAN 匯流排等進階周邊裝置。

### 6. **應用領域**
MicroPython 的多功能性使其適用於廣泛場景：
- **物聯網**：建構透過 Wi-Fi 或藍牙連接網路的智能裝置（如家庭自動化、氣象站）
- **機器人技術**：控制機器人系統中的馬達、感測器與致動器
- **教育領域**：憑藉其簡潔性與互動性，成為程式設計與電子學教學利器
- **原型開發**：快速建立嵌入式系統的概念驗證專案
- **穿戴式裝置**：驅動智能手錶、健身追蹤器等小型電池供電裝置
- **感測器網路**：收集並處理環境感測器資料
- **家庭自動化**：控制燈光、家電或安防系統

### 7. **優勢分析**
- **易用性**：相較於 C/C++，Python 的可讀語法大幅降低嵌入式程式設計門檻
- **快速開發**：REPL 與高階抽象化加速原型設計與除錯流程
- **社群與生態**：持續成長的社群提供豐富程式庫、教學與支援資源
- **可攜性**：為某 MicroPython 平台編寫的程式碼通常只需少量修改即可移植至其他平台
- **靈活性**：同時適合初學者與進階開發者使用

### 8. **技術限制**
- **資源限制**：有限的記憶體與處理能力限制了應用複雜度，無法與標準 Python 相比
- **執行效能**：因直譯式語言特性，對時效性要求高的任務處理速度不如 C/C++
- **Python 功能子集**：因資源限制，無法使用 NumPy、Pandas 等所有 Python 程式庫
- **韌體管理**：需為不同微控制器刷入特定韌體，對新手較具挑戰性

### 9. **與其他嵌入式方案比較**
- **MicroPython vs. C/C++ (Arduino)**：MicroPython 更易學習且原型開發更快，但對於底層高速任務的處理效能較弱
- **MicroPython vs. CircuitPython**：CircuitPython 作為 Adafruit 的 MicroPython 分支，更側重初學者友好性與 USB 連接功能，但硬體生態系較小
- **MicroPython vs. Lua (NodeMCU)**：MicroPython 為 Python 開發者提供更熟悉的程式語言環境與更廣泛的程式庫支援

### 10. **入門指南**
開始使用 MicroPython 的步驟：
1. **選擇相容開發板**：常見選擇包含 ESP32、Raspberry Pi Pico 或 PyBoard
2. **下載韌體**：從官方網站 micropython.org 取得對應開發板的 MicroPython 韌體
3. **刷入韌體**：使用 `esptool.py` 或開發板專用燒錄工具安裝 MicroPython
4. **編寫與上傳程式碼**：使用 Thonny 等 IDE 或 `ampy` 等工具傳輸 Python 腳本至裝置
5. **嘗試 REPL 操作**：透過序列終端機（如 PuTTY、screen）連接開發板進行互動操作
6. **探索程式庫**：運用 `machine`、`network`、`utime` 等模組控制硬體與實作功能

### 11. **生態系統與社群資源**
MicroPython 擁有活躍社群與豐富資源：
- **官方文件**：於 docs.micropython.org 提供完整指南與 API 參考
- **論壇與群組**：MicroPython 論壇、Reddit 與 X（搜尋 #MicroPython）上的熱烈討論
- **教學與專案**：YouTube、Hackster.io 與社群部落格上的大量教學資源
- **程式庫資源**：社群貢獻的感測器、顯示器與通訊協定程式庫

### 12. **未來發展**
MicroPython 持續演進的方向包含：
- 支援新微控制器與功能（如藍牙低功耗、進階網路功能）
- 與 MQTT、Home Assistant 等物聯網框架整合
- 效能與記憶體優化的持續改進
- 在教育與產業領域的快速原型開發與物聯網應用中持續擴大採用

### 13. **程式碼範例**
以下為在 Raspberry Pi Pico 上閃爍 LED 的簡單 MicroPython 腳本：
```python
from machine import Pin
import utime

led = Pin(25, Pin.OUT)  # Pico 板載 LED
while True:
    led.toggle()
    utime.sleep(0.5)  # 每 0.5 秒閃爍一次
```

### 14. **總結**
MicroPython 是連接高階 Python 開發與底層硬體控制的重要橋樑，為嵌入式程式設計提供了強大且易用的工具。其輕量設計、Python 語法與廣泛硬體支援，使其成為物聯網、機器人、教育與原型開發領域的理想選擇。雖然在效能與程式庫支援方面不如標準 Python 或 C，但其易用性與快速開發能力，仍使其成為業餘愛好者與專業開發者的首選方案。

如需更多資訊，請造訪 MicroPython 官方網站（micropython.org）或探索 X 與 GitHub 上的社群資源。若您有關於 MicroPython 的具體問題或專案需要協助，歡迎隨時提出！