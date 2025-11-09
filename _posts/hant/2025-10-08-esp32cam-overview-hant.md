---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: ESP32-CAM 緊湊型開發板概述
translated: true
type: note
---

### 什麼是 ESP32-CAM？

ESP32-CAM 是樂鑫科技推出的一款緊湊型低成本開發板，結合了強大的 ESP32 微控制器與集成攝像頭模組。它專為物聯網項目設計，特別適用於圖像捕捉、視頻串流和電腦視覺應用。「CAM」部分指的是內置的 OV2640 攝像頭傳感器，支援最高 2MP 解析度（1600x1200 像素）。

#### 主要特點：
- **處理器與連接性**：採用雙核 ESP32 芯片（Xtensa LX6 架構，最高 240 MHz），配備 520KB SRAM 和 4MB PSRAM。包含 Wi-Fi（802.11 b/g/n）和雙模藍牙（經典與低功耗）無線通信功能。
- **攝像頭**：OV2640 CMOS 圖像傳感器，配備可調焦鏡頭，支援 JPEG、BMP 和灰度等格式。
- **電源與尺寸**：工作電壓為 3.3V（或通過穩壓器使用 5V），功耗低（拍攝時低於 200mA），尺寸僅為 27x40.5x4.5毫米，非常適合嵌入式項目。
- **I/O 介面**：10 個 GPIO 引腳（部分與攝像頭共用），microSD 卡插槽用於存儲，並支援通過擴展連接傳感器。
- **編程**：兼容 Arduino IDE、ESP-IDF 或 MicroPython。可使用如 esp32-camera（GitHub 上的庫）等庫處理圖像處理和串流。

#### 常見用途：
- **DIY 安全監控鏡頭**：通過 Wi-Fi 將實時視頻串流至手機或瀏覽器，並支援運動檢測。
- **圖像識別**：與 TensorFlow Lite 等 AI 工具整合，實現物體檢測功能。
- **監控與記錄**：遠程照片拍攝、縮時攝影或野生動物監測。
- **原型開發**：機械人、智能家居設備或擴增實境實驗。

由於其價格實惠（通常低於 10 美元）且設置簡便，深受創客歡迎——但初學者可能需要 USB 轉串口適配器進行初始編程。若需更高品質的視頻，可選擇如 ESP32-S3-CAM 等新型號，但原始 ESP32-CAM 仍是簡單項目的首選。

#### 參考資料：
- [ESP32-CAM 攝像頭模組於亞馬遜](https://www.amazon.com/HiLetgo-ESP32-CAM-Development-Bluetooth-Raspberry/dp/B07RXPHYNM)
- [樂鑫 ESP32-Camera GitHub 存儲庫](https://github.com/espressif/esp32-camera)
- [M5Stack ESP32-CAM 文檔](https://docs.m5stack.com/en/unit/esp32cam)
- [Instructables：使用 ESP32-CAM 製作超低成本安全監控鏡頭](https://www.instructables.com/Super-Cheap-Security-Camera-With-ESP32-cam/)
- [DFRobot ESP32-CAM 數據手冊 (PDF)](https://media.digikey.com/pdf/Data%2520Sheets/DFRobot%2520PDFs/DFR0602_Web.pdf)