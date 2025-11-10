---
audio: false
generated: true
lang: hant
layout: post
title: Raspberry Pi 與 Arduino 在洗衣機監控及 Telegram 警報應用之比較
translated: true
type: note
---

使用樹莓派（Raspberry Pi）替代 Arduino（如 ESP32-CAM）來偵測您的 Maytag MHW8630HW 洗衣機何時停止運作並發送 Telegram 通知，是一個可行的替代方案。這種方式能提供更強大的處理能力和靈活性，但代價是增加了系統複雜度和功耗。以下我將比較樹莓派與 Arduino 解決方案，概述其他微控制器選項，並提供使用樹莓派實作系統的詳細指南。我還將討論替代方法（例如其他硬體或感測器），以確保回應的全面性。

---

### 比較：樹莓派 vs. Arduino vs. 其他選項

| **功能特性**             | **樹莓派**                                                                      | **Arduino (ESP32-CAM)**                                                  | **其他選項 (例如 NodeMCU, ESP8266)**                           |
|--------------------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------|
| **處理能力**             | 強大（四核 CPU，1-8GB RAM）– 支援進階影像處理、OpenCV。                          | 有限（雙核，520KB SRAM）– 僅能進行基礎影像處理。                           | 非常有限 – 不適用於基於攝影機的處理。                            |
| **攝影機支援**           | 可輕鬆使用 USB 網路攝影機或 Pi Camera 模組（例如 8MP Pi Camera v2）。            | 內建 OV2640（2MP）攝影機，但解析度和品質較低。                             | 需外接攝影機模組，整合複雜。                                    |
| **Wi-Fi**                | 內建（大多數型號，例如 Pi 4, Zero 2 W）。                                        | 內建（ESP32-CAM）。                                                       | 內建（例如 ESP8266），但無原生攝影機支援。                       |
| **程式設計**             | Python, OpenCV，功能多樣但需作業系統設定（Raspberry Pi OS）。                    | 使用 Arduino IDE 的 C++，對初學者較簡單。                                 | C++ 或 Lua（例如 NodeMCU），影像處理函式庫有限。                 |
| **功耗**                 | 較高（Pi Zero 約 2.5W，Pi 4 約 5-10W）。                                         | 較低（ESP32-CAM 約 1-2W）。                                               | 最低（ESP8266 約 0.5-1W）。                                     |
| **成本**                 | $10（Pi Zero W）至 $35+（Pi 4） + $15（Pi Camera）。                             | ~$10（含攝影機的 ESP32-CAM）。                                            | ~$5-10（ESP8266/NodeMCU）+ 感測器成本。                         |
| **設定簡易度**           | 中等（需設定作業系統、Python 環境）。                                            | 簡單（Arduino IDE，單一程式草稿碼）。                                     | 對簡單感測器容易，對攝影機整合則複雜。                          |
| **最佳使用情境**         | 進階影像處理，未來擴充靈活（例如 ML 模型）。                                     | 簡單、低成本的燈光偵測與 Telegram 整合。                                  | 非攝影機解決方案（例如震動或電流感測器）。                      |

**樹莓派優勢**：
- 透過 OpenCV 實現卓越的影像處理，使燈光偵測更可靠。
- 更容易除錯和擴充（例如添加網頁介面或多種感測器）。
- 支援更高品質的攝影機，在不同光線條件下提供更佳準確性。

**樹莓派劣勢**：
- 需要更多設定（作業系統安裝、Python 環境）。
- 功耗較高，較不適合電池供電的設置。
- 比 ESP32-CAM 更昂貴。

**其他選項**：
- **NodeMCU/ESP8266**：適用於非攝影機解決方案（例如使用震動感測器或電流感測器）。有限的處理能力使攝影機整合不切實際。
- **震動感測器**：偵測機器震動而非面板燈光。簡單但可能錯過細微的週期變化。
- **電流感測器**：測量耗電量（例如 ACS712 模組）以偵測機器何時停止。非侵入式但需要電氣設定。

---

### 樹莓派實作指南

#### 技術堆疊
**硬體**：
1. **樹莓派**：
   - **Raspberry Pi Zero 2 W**（$15，緊湊，具 Wi-Fi）或 **Raspberry Pi 4**（$35+，更強大）。
2. **攝影機**：
   - **Raspberry Pi Camera Module v2**（$15，8MP）或 USB 網路攝影機。
3. **電源供應器**：
   - 5V USB-C（Pi 4）或 micro-USB（Pi Zero），輸出 2-3A。
4. **安裝**：
   - 外殼或黏性支架，用於將攝影機對準洗衣機的面板燈光。

**軟體**：
1. **作業系統**：Raspberry Pi OS（Lite 版效率高，Full 版設定較易）。
2. **程式語言**：Python。
3. **函式庫**：
   - **OpenCV**：用於影像處理以偵測面板燈光。
   - **python-telegram-bot**：用於 Telegram 通知。
   - **picamera2**（用於 Pi Camera）或 **fswebcam**（用於 USB 網路攝影機）。
4. **Telegram Bot**：設定與 Arduino 相同（使用 BotFather 取得 bot token 和 chat ID）。

#### 演算法
演算法與 Arduino 方法類似，但利用 OpenCV 實現更穩健的影像處理：
1. **影像擷取**：使用 Pi Camera 或網路攝影機定期擷取影像（例如每 10 秒）。
2. **感興趣區域 (ROI)**：在影像中定義面板燈光周圍的矩形區域。
3. **影像處理**：
   - 轉換為灰階。
   - 應用高斯模糊以減少雜訊。
   - 使用自適應閾值處理來偵測背景中的明亮面板燈光。
   - 計算 ROI 內的平均像素強度或計算明亮像素的數量。
4. **狀態機**：
   - 如果 ROI 明亮（燈光 ON），標記機器為運轉中。
   - 如果 ROI 變暗（燈光 OFF）持續 5 分鐘，標記機器為已停止並發送 Telegram 通知。
5. **防抖動**：實作 5 分鐘延遲以確認機器已停止。

#### 實作步驟
1. **設定樹莓派**：
   - 使用 Raspberry Pi Imager 下載並將 **Raspberry Pi OS**（Lite 或 Full）燒錄到 SD 卡。
   - 透過編輯 `/etc/wpa_supplicant/wpa_supplicant.conf` 或使用 GUI 將 Pi 連接到 Wi-Fi。
   - 透過 `raspi-config` 啟用攝影機介面（Interfacing Options > Camera）。

2. **安裝相依套件**：
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-picamera2 python3-pip
   pip3 install python-telegram-bot
   ```

3. **定位攝影機**：
   - 安裝 Pi Camera 或 USB 網路攝影機，使其對準洗衣機的面板燈光。
   - 使用以下指令測試攝影機：
     ```bash
     libcamera-still -o test.jpg
     ```
     或對於 USB 網路攝影機：
     ```bash
     fswebcam test.jpg
     ```

4. **Python 腳本**：
以下是樹莓派用於偵測面板燈光並發送 Telegram 通知的範例 Python 腳本。

```python
import cv2
import numpy as np
from picamera2 import Picamera2
import telegram
import asyncio
import time

# Telegram bot 設定
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
bot = telegram.Bot(token=BOT_TOKEN)

# 攝影機設定
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))
picam2.start()

# ROI 設定（根據攝影機視角調整）
ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT = 200, 150, 50, 50
THRESHOLD = 150  # 亮度閾值 (0-255)
STOP_DELAY = 300  # 5 分鐘，以秒為單位

machine_running = False
last_on_time = 0

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def is_light_on(frame):
    # 轉換為灰階
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 應用高斯模糊
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # 提取 ROI
    roi = gray[ROI_Y:ROI_Y+ROI_HEIGHT, ROI_X:ROI_X+ROI_WIDTH]
    # 計算平均亮度
    avg_brightness = np.mean(roi)
    return avg_brightness > THRESHOLD

async def main():
    global machine_running, last_on_time
    while True:
        # 擷取影像
        frame = picam2.capture_array()
        # 檢查燈光是否亮起
        if is_light_on(frame):
            if not machine_running:
                machine_running = True
                print("Machine is ON")
            last_on_time = time.time()
        else:
            if machine_running and (time.time() - last_on_time > STOP_DELAY):
                machine_running = False
                print("Machine stopped")
                await send_telegram_message("Washing machine stopped! Time to hang up clothes.")
        time.sleep(10)  # 每 10 秒檢查一次

if __name__ == "__main__":
    asyncio.run(main())
```

5. **自訂腳本**：
   - 將 `BOT_TOKEN` 和 `CHAT_ID` 替換為您的 Telegram 憑證。
   - 透過擷取測試影像並使用 GIMP 或 Python 等工具分析來調整 `ROI_X`、`ROI_Y`、`ROI_WIDTH`、`ROI_HEIGHT`，以定位面板燈光。
   - 根據測試影像調整 `THRESHOLD`（亮度越高，數值應設越高）。
   - 如有需要，修改 `STOP_DELAY`。

6. **執行腳本**：
   ```bash
   python3 washer_monitor.py
   ```
   - 使用 `nohup python3 washer_monitor.py &` 在背景執行，或使用 systemd 服務以確保可靠性。

7. **測試與部署**：
   - 啟動洗衣機並監控腳本輸出。
   - 驗證 Telegram 通知。
   - 將 Pi 和攝影機固定在永久設置中。

---

### 其他替代方案
1. **震動感測器**：
   - **硬體**：使用震動感測器（例如 SW-420）搭配 ESP8266 或樹莓派。
   - **設定**：將感測器附著在洗衣機上以偵測震動。
   - **演算法**：監控持續無震動的時間（例如 5 分鐘）以偵測機器何時停止。
   - **優點**：簡單、低成本、不受環境光線影響。
   - **缺點**：可能錯過有長時間暫停的週期（例如浸泡）。
   - **程式碼範例 (ESP8266)**：
     ```cpp
     #include <ESP8266WiFi.h>
     #include <UniversalTelegramBot.h>
     #define VIBRATION_PIN D5
     #define BOT_TOKEN "your_bot_token"
     #define CHAT_ID "your_chat_id"
     WiFiClientSecure client;
     UniversalTelegramBot bot(BOT_TOKEN, client);
     bool machineRunning = false;
     unsigned long lastVibrationTime = 0;
     void setup() {
       pinMode(VIBRATION_PIN, INPUT);
       WiFi.begin("ssid", "password");
       while (WiFi.status() != WL_CONNECTED) delay(500);
       client.setInsecure();
     }
     void loop() {
       if (digitalRead(VIBRATION_PIN)) {
         machineRunning = true;
         lastVibrationTime = millis();
       } else if (machineRunning && (millis() - lastVibrationTime > 300000)) {
         machineRunning = false;
         bot.sendMessage(CHAT_ID, "Washing machine stopped!", "");
       }
       delay(1000);
     }
     ```

2. **電流感測器**：
   - **硬體**：使用 ACS712 電流感測器搭配 ESP8266 或樹莓派。
   - **設定**：非侵入式地將感測器夾在洗衣機的電源線上。
   - **演算法**：偵測電流低於閾值（例如 <0.5A）持續 5 分鐘。
   - **優點**：準確、非侵入式。
   - **缺點**：需要電氣知識、需針對機器耗電進行校準。

3. **麥克風**：
   - **硬體**：使用麥克風模組（例如 KY-038）搭配樹莓派。
   - **演算法**：分析音量水平以偵測機器噪音何時停止。
   - **優點**：非視覺、在低光條件下有效。
   - **缺點**：對環境噪音敏感、需要訊號處理。

---

### 建議
- **樹莓派**：最適合穩健的影像處理和未來擴充性。如果您熟悉 Python 並希望在不同光線條件下實現高可靠性，請使用此方案。
- **Arduino (ESP32-CAM)**：最適合低成本、簡單的設置。如果您希望配置最少且能接受基礎影像處理，這是理想選擇。
- **震動或電流感測器**：最適合非攝影機解決方案，特別是當面板燈光不可靠（例如昏暗或被遮擋）時。與 ESP8266 搭配使用以保持簡單。
- **麥克風**：由於環境噪音，可靠性較低，但可作為輔助感測器。

對於您的兩層樓房屋，由於您位於二樓且需要透過 Telegram 進行可靠的遠端通知，因此帶有攝影機的樹莓派或 ESP32-CAM 是理想的選擇。樹莓派在燈光偵測方面提供更好的準確性，而 ESP32-CAM 則更便宜且部署更簡單。如果您偏好非攝影機方法，帶有 ESP8266 的震動感測器是最簡單的替代方案。

如果您想深入了解任何特定方法、需要設定協助或需要替代感測器的程式碼，請告訴我！