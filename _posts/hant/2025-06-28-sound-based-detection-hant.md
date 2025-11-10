---
audio: false
generated: true
lang: hant
layout: post
title: 基於聲音檢測的美泰洗衣機
translated: true
type: note
---

使用聲音檢測您的 Maytag MHW8630HW 洗衣機何時停止運轉，是基於攝像頭方法的可行替代方案。通過將聲音傳感器靠近洗衣機放置，您可以監控運轉期間產生的噪音（例如馬達嗡鳴、水流或滾筒轉動），並檢測其停止時刻，從而判斷洗滌週期是否結束。以下我將說明如何調整先前的專案，改用聲音傳感器替代攝像頭，重點介紹硬體、演算法和程式碼的變更，同時保留 Telegram 通知系統。

---

### 技術堆疊
#### 硬體
1. **Arduino 開發板**：
   - **ESP32-CAM**（仍可使用）– 保留 Wi-Fi 功能以用於 Telegram 整合，雖然不需要攝像頭。
   - 替代方案：**ESP8266 NodeMCU** 或帶有 ESP8266 模組的 **Arduino Uno**（若不需要攝像頭，更簡單）。
2. **聲音傳感器**：
   - **KY-038 麥克風聲音傳感器**或類似型號 – 價格實惠，透過類比輸出檢測聲音水平。
   - 替代方案：**MAX9814 電容式麥克風放大器** – 更靈敏，具有可調增益，利於更好檢測。
3. **電源供應**：
   - 用於 ESP32 或其他開發板的 5V USB 電源適配器或電池組。
4. **安裝**：
   - 將聲音傳感器靠近洗衣機放置（例如貼在側面或頂部），使其能檢測運轉聲音，但避免直接接觸水。
   - 使用小型外殼保護傳感器和開發板。
5. **Wi-Fi 路由器**：
   - 用於網路連接以發送 Telegram 通知。

#### 軟體
- **Arduino IDE**：用於編程 ESP32 或其他開發板。
- **函式庫**：
  - **Universal Arduino Telegram Bot Library** by Brian Lough – 用於 Telegram 整合。
  - **ArduinoJson** – 用於處理 Telegram API 通訊中的 JSON 資料。
- **Telegram Bot**：與之前相同，使用 BotFather 取得 bot token 和 chat ID。
- **程式語言**：C++（Arduino 草稿碼）。

---

### 使用聲音檢測洗衣機狀態的演算法
聲音傳感器將檢測洗衣機產生的噪音水平。當機器運轉時，會產生持續的聲音（例如馬達、水流或滾筒聲）。當其停止時，聲音水平會顯著下降。該演算法處理這些聲音水平以判斷機器狀態。

#### 檢測演算法
1. **聲音取樣**：
   - 持續讀取聲音傳感器的類比輸出以測量噪音水平。
2. **訊號處理**：
   - **平均計算**：在短時間窗口內（例如 1-2 秒）計算平均聲音水平，以平滑瞬態噪音（例如關門聲）。
   - **閾值比較**：將平均聲音水平與預定義閾值比較。高水平表示機器運轉中，低水平則表示已停止。
3. **狀態機**：
   - 根據聲音水平追蹤機器狀態（開啟或關閉）。
   - 若聲音水平連續多個週期超過閾值，則假定機器正在運轉。
   - 若聲音水平下降至閾值以下並持續一段設定時間（例如 5 分鐘），則假定洗滌週期已完成。
4. **防抖動處理**：
   - 實施延遲（例如 5 分鐘）以確認機器已停止，避免在靜默階段（例如浸泡或週期間暫停）誤發通知。
5. **通知**：
   - 當確認機器停止時，發送 Telegram 訊息（例如「洗衣機已停止！該晾衣服了。」）。

#### 為何選擇聲音檢測？
- 聲音檢測比影像處理更簡單，因為不需要複雜演算法或高計算資源。
- 與基於攝像頭的檢測相比，對環境光線變化較不敏感。
- 然而，它可能受背景噪音（例如大聲的電視）影響，因此傳感器放置和閾值調校至關重要。

---

### 實施指南
#### 步驟 1：設定 Telegram Bot
- 遵循與原始指南相同的步驟：
  - 使用 **@BotFather** 建立 bot 以取得 **Bot Token**。
  - 使用 **@GetIDsBot** 或檢查傳入訊息來取得您的 **Chat ID**。
  - 確保手機上已設定 Telegram 以接收通知。

#### 步驟 2：硬體設定
1. **選擇聲音傳感器**：
   - **KY-038**：提供類比輸出（ESP32 的 10 位元 ADC 為 0-1023），與聲音強度成正比。它也有數位輸出，但類比更適合細微檢測。
   - **MAX9814**：更靈敏，可透過電位器調整增益。連接至類比引腳。
2. **連接聲音傳感器**：
   - 對於 KY-038：
     - **VCC** 接 5V（或 3.3V，取決於開發板）。
     - **GND** 接 GND。
     - **類比輸出 (A0)** 接 ESP32 的類比引腳（例如 GPIO 4）。
   - 對於 MAX9814：
     - 連接方式類似，但使用板上電位器調整增益以獲得最佳靈敏度。
3. **放置傳感器**：
   - 將傳感器靠近洗衣機放置（例如在側面或頂部），使其能檢測馬達或滾筒噪音。避免可能接觸水的區域。
   - 在洗滌週期中監控聲音水平以測試放置位置（使用 Serial Monitor 記錄數值）。
4. **為開發板供電**：
   - 將 5V USB 電源適配器或電池組連接到 ESP32 或其他開發板。
   - 確保電源穩定，因為 Wi-Fi 通訊需要穩定電壓。
5. **安裝**：
   - 使用小型外殼或膠帶固定傳感器和開發板，確保麥克風暴露以捕捉聲音。

#### 步驟 3：軟體設定
- **Arduino IDE**：如原始指南所述安裝。
- **ESP32 開發板支援**：透過 Boards Manager 添加 ESP32 開發板套件（與之前 URL 相同）。
- **函式庫**：
  - 安裝 **Universal Arduino Telegram Bot Library** 和 **ArduinoJson** 如前所述。
- **Wi-Fi**：確保開發板能連接到您的 2.4GHz Wi-Fi 網路。

#### 步驟 4：編寫 Arduino 程式碼
以下是適用於 ESP32（或 ESP8266）的範例 Arduino 草稿碼，用於檢測聲音水平並發送 Telegram 通知。此程式碼假設 KY-038 聲音傳感器連接到 GPIO 4。

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Wi-Fi 憑證
#define WIFI_SSID "您的_wifi_ssid"
#define WIFI_PASSWORD "您的_wifi_密碼"

// Telegram Bot 憑證
#define BOT_TOKEN "您的_bot_token"
#define CHAT_ID "您的_chat_id"

// 聲音傳感器引腳
#define SOUND_PIN 4 // 用於類比輸入的 GPIO 4

// 聲音檢測參數
#define SOUND_THRESHOLD 300 // 根據測試調整 (0-1023)
#define SAMPLE_WINDOW 2000 // 2 秒用於平均計算
#define STOP_DELAY 300000 // 5 分鐘（毫秒）

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // 連接到 Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi 已連接");

  // 設定 Telegram 客戶端
  client.setInsecure(); // 為簡化起見；在生產環境中考慮使用適當的 SSL

  // 設定聲音傳感器引腳
  pinMode(SOUND_PIN, INPUT);
}

void loop() {
  // 在時間窗口內取樣聲音水平
  unsigned long startMillis = millis();
  uint32_t totalSound = 0;
  uint16_t sampleCount = 0;

  while (millis() - startMillis < SAMPLE_WINDOW) {
    totalSound += analogRead(SOUND_PIN);
    sampleCount++;
    delay(10); // 取樣間隔小延遲
  }

  float avgSound = sampleCount > 0 ? (float)totalSound / sampleCount : 0;
  Serial.print("平均聲音水平: ");
  Serial.println(avgSound);

  // 狀態機
  if (avgSound > SOUND_THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("機器已啟動");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("機器已停止");
      bot.sendMessage(CHAT_ID, "洗衣機已停止！該晾衣服了。", "");
    }
  }

  delay(10000); // 每 10 秒檢查一次
}
```

#### 步驟 5：自訂程式碼
1. **更新憑證**：
   - 將 `您的_wifi_ssid`、`您的_wifi_密碼`、`您的_bot_token` 和 `您的_chat_id` 替換為實際數值。
2. **調校 `SOUND_THRESHOLD`**：
   - 運行洗衣機並透過 Serial Monitor（`Serial.println(analogRead(SOUND_PIN));`）監控聲音水平。
   - 將 `SOUND_THRESHOLD` 設定為高於環境噪音但低於機器運轉噪音的數值（例如 200-500，取決於您的設定）。
3. **調整 `SAMPLE_WINDOW`**：
   - 2 秒窗口（`2000` 毫秒）可平滑瞬態噪音。若背景噪音導致誤讀，可增加此值。
4. **調整 `STOP_DELAY`**：
   - 設定為 `300000`（5 分鐘）以避免在靜默階段（如浸泡）誤發通知。

#### 步驟 6：測試與部署
1. **上傳程式碼**：
   - 透過 USB 轉序列適配器將 ESP32 連接到電腦。
   - 在 Arduino IDE 中選擇 **ESP32 Wrover Module**（或 ESP8266 的 **NodeMCU**）並上傳草稿碼。
2. **測試系統**：
   - 啟動洗衣機並監控 Serial Monitor 中的聲音水平和狀態變化。
   - 驗證機器停止時是否收到 Telegram 通知。
3. **微調**：
   - 若出現誤報/漏報，調整 `SOUND_THRESHOLD` 或 `STOP_DELAY`。
   - 在不同條件下（例如有背景噪音時）測試以確保可靠性。
4. **永久安裝**：
   - 將傳感器和開發板固定在外殼中並靠近機器，確保麥克風暴露但受保護避免接觸水。

---

### 聲音檢測的優勢
- **處理更簡單**：無需影像處理，減少 ESP32 的計算負載。
- **成本效益高**：如 KY-038 的聲音傳感器價格低廉（通常低於 5 美元）。
- **非侵入性**：無需直接連接到機器的面板燈。

### 挑戰與緩解措施
- **背景噪音**：家庭噪音（例如電視、談話）可能干擾。緩解方法：
  - 將傳感器靠近機器的馬達或滾筒放置。
  - 調校 `SOUND_THRESHOLD` 以忽略環境噪音。
  - 使用指向性麥克風或調整 MAX9814 的增益。
- **靜默階段**：某些洗滌週期有暫停（例如浸泡）。`STOP_DELAY` 確保僅在長時間靜默後才發送通知。
- **水暴露**：確保傳感器置於防水外殼中，因為洗衣機可能會有水花或濕氣。

### 可選增強功能
- **頻率分析**：若背景噪音持續存在，可使用快速傅立葉變換（FFT）函式庫（如 `arduinoFFT`）分析聲音頻率（例如馬達嗡鳴在 50-200 Hz）。這需要更多處理能力，在未優化的基礎 ESP32 上可能不可行。
- **雙傳感器**：結合聲音和振動傳感器（例如 SW-420）以實現冗餘。若兩者均指示機器關閉，則檢測置信度增加。
- **電池供電**：為便攜性，使用可充電 LiPo 電池與充電模組（例如 TP4056）替代 USB 適配器。

---

### 疑難排解
- **無聲音檢測**：檢查傳感器接線，使用 Serial Monitor 測試，並確保傳感器靠近機器的噪音源。
- **誤發通知**：增加 `STOP_DELAY` 或調整 `SOUND_THRESHOLD` 以過濾背景噪音或週期間暫停。
- **Wi-Fi 問題**：驗證 2.4GHz Wi-Fi 憑證和機器附近的訊號強度。
- **無 Telegram 訊息**：確認 bot token 和 chat ID，檢查 Serial Monitor 中的錯誤訊息。

這種基於聲音的方法比基於攝像頭的方法更簡單，且在變化光線條件下更可靠，非常適合用於洗衣機監控。如果您在具體步驟、傳感器校準或整合附加功能方面需要協助，請隨時告知！