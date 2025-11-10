---
audio: false
generated: true
lang: hant
layout: post
title: 基於Arduino與Telegram通知的智能洗衣機監測器
translated: true
type: note
---

要建立一個系統來偵測您的 Maytag MHW8630HW 洗衣機何時停止（使用其面板燈作為指示器），並透過 Telegram 機器人通知您晾衣服，您可以使用 Arduino 配合相機模組來監控洗衣機的狀態。以下是關於技術堆疊、硬體設定、演算法和實作步驟的詳細指南。

---

### 技術堆疊
#### 硬體
1. **Arduino 開發板**：
   - **ESP32-CAM**（推薦）– 結合了微控制器與內建的 OV2640 相機和 Wi-Fi 功能，非常適合用於影像處理和 Telegram 整合。
   - 替代方案：Arduino Uno + 獨立的相機模組（例如 OV7670）和 ESP8266 用於 Wi-Fi，但設定起來較為複雜。
2. **相機模組**：
   - OV2640（隨 ESP32-CAM 附帶）– 2MP 相機，足以偵測面板燈。
3. **光感測器（可選）**：
   - 光敏電阻（LDR）或 TSL2561 – 用於輔助基於相機的光線偵測，以實現冗餘或更簡單的設定。
4. **電源供應**：
   - 5V USB 電源轉接器或電池組，用於供電給 ESP32-CAM。
5. **安裝**：
   - 小型外殼或 3D 列印外殼，用於固定 ESP32-CAM，並確保其能清晰看到洗衣機的控制面板。
6. **Wi-Fi 路由器**：
   - 用於讓 ESP32-CAM 連接到互聯網並與 Telegram 機器人通訊。

#### 軟體
1. **Arduino IDE**：
   - 用於編程 ESP32-CAM。
2. **函式庫**：
   - **Universal Arduino Telegram Bot Library** by Brian Lough – 用於 Telegram 機器人整合。
   - **ArduinoJson** – 用於處理 Telegram API 通訊的 JSON 資料。
   - **ESP32-CAM Camera Libraries** – 內建的函式庫，用於捕捉和處理影像。
3. **Telegram 機器人**：
   - 在 Telegram 上使用 BotFather 建立一個機器人，並取得機器人令牌和聊天 ID。
4. **程式語言**：
   - C++（Arduino 草圖碼）。
5. **可選工具**：
   - OpenCV（Python）用於在將影像處理演算法移植到 Arduino 之前，在電腦上進行原型設計（針對 ESP32-CAM 進行了簡化）。

---

### 偵測洗衣機狀態的演算法
由於 Maytag MHW8630HW 有一個面板燈指示機器是否開啟，您可以使用相機來偵測這個燈光。該演算法將處理影像以確定燈光是亮起還是熄滅，從而指示機器的狀態。

#### 偵測演算法
1. **影像捕捉**：
   - 使用 ESP32-CAM 定期捕捉洗衣機控制面板的影像。
2. **感興趣區域（ROI）選擇**：
   - 在影像中定義面板燈所在的特定區域（例如，電源指示器周圍的矩形區域）。
3. **影像處理**：
   - **灰階轉換**：將捕捉的影像轉換為灰階以簡化處理。
   - **閾值處理**：應用亮度閾值來偵測燈光的存在。當面板燈亮起時，會產生一個亮點，與熄滅時的較暗區域形成對比。
   - **像素強度分析**：計算 ROI 內的平均像素強度。高強度表示燈亮，低強度表示燈滅。
4. **狀態機**：
   - 根據連續讀數追蹤機器的狀態（開啟或關閉）。
   - 如果燈光在多個週期內被偵測為亮起，則假定機器正在運行。
   - 如果燈光轉變為熄滅並在設定的時間內（例如 5 分鐘）保持熄滅，則假定洗衣週期已完成。
5. **防抖動**：
   - 實施延遲（例如 5 分鐘）以確認機器已停止，避免在洗衣週期暫停期間（例如浸泡或注水）產生錯誤通知。
6. **通知**：
   - 當確認機器停止時，發送 Telegram 訊息（例如「洗衣機已停止！該晾衣服了。」）。

#### 為什麼不使用更複雜的演算法？
- 進階演算法如機器學習（例如用於物件偵測的 CNN）對於此任務來說過於複雜，且對 ESP32-CAM 有限的處理能力來說資源消耗過大。
- 簡單的閾值處理已足夠，因為面板燈是一個清晰的三元指示器（亮起/熄滅）。

---

### 實作指南
#### 步驟 1：設定 Telegram 機器人
1. **建立 Telegram 機器人**：
   - 打開 Telegram，搜尋 **@BotFather**，並開始聊天。
   - 發送 `/newbot`，為您的機器人命名（例如 "WasherBot"），並取得**機器人令牌**。
   - 向您的機器人發送 `/start`，並使用如 `@GetIDsBot` 的服務或透過在程式碼中檢查傳入訊息來取得您的**聊天 ID**。
2. **在手機上安裝 Telegram**：
   - 確保您可以從您的機器人接收訊息。

#### 步驟 2：硬體設定
1. **定位 ESP32-CAM**：
   - 將 ESP32-CAM 安裝在小型外殼中或用膠帶固定，使其面向洗衣機的控制面板。
   - 確保相機能清晰看到面板燈（透過樣本照片進行測試）。
   - 固定設定以避免移動，因為這可能會影響 ROI 的一致性。
2. **為 ESP32-CAM 供電**：
   - 將 5V USB 電源轉接器或電池組連接到 ESP32-CAM 的 5V 引腳。
   - 確保電源穩定，因為相機和 Wi-Fi 會消耗大量電力。
3. **可選的光感測器**：
   - 如果使用光敏電阻，請將其連接到 ESP32-CAM 的類比引腳（例如 GPIO 4），並搭配分壓電路（例如 10kΩ 電阻接地）。

#### 步驟 3：軟體設定
1. **安裝 Arduino IDE**：
   - 從 [arduino.cc](https://www.arduino.cc/en/software) 下載並安裝 Arduino IDE。
2. **添加 ESP32 開發板支援**：
   - 在 Arduino IDE 中，前往 **File > Preferences**，將以下 URL 添加到 Additional Boards Manager URLs：
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - 前往 **Tools > Board > Boards Manager**，搜尋 "ESP32"，並安裝 ESP32 套件。
3. **安裝函式庫**：
   - 安裝 **Universal Arduino Telegram Bot Library**：
     - 從 [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) 下載，並透過 **Sketch > Include Library > Add .ZIP Library** 添加。
   - 安裝 **ArduinoJson**：
     - 前往 **Sketch > Include Library > Manage Libraries**，搜尋 "ArduinoJson"，並安裝 6.x.x 版本。
4. **配置 Wi-Fi**：
   - 確保您的 ESP32-CAM 可以連接到您的家庭 Wi-Fi 網絡（2.4GHz，因為不支援 5GHz）。

#### 步驟 4：編寫 Arduino 程式碼
以下是 ESP32-CAM 的範例 Arduino 草圖碼，用於偵測面板燈並發送 Telegram 通知。此程式碼假設您已識別出面板燈的 ROI 座標。

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// Wi-Fi 憑證
#define WIFI_SSID "your_wifi_ssid"
#define WIFI_PASSWORD "your_wifi_password"

// Telegram 機器人憑證
#define BOT_TOKEN "your_bot_token"
#define CHAT_ID "your_chat_id"

// 相機配置（適用於 ESP32-CAM）
#define PWDN_GPIO_NUM 32
#define RESET_GPIO_NUM -1
#define XCLK_GPIO_NUM 0
#define SIOD_GPIO_NUM 26
#define SIOC_GPIO_NUM 27
#define Y9_GPIO_NUM 35
#define Y8_GPIO_NUM 34
#define Y7_GPIO_NUM 39
#define Y6_GPIO_NUM 36
#define Y5_GPIO_NUM 21
#define Y4_GPIO_NUM 19
#define Y3_GPIO_NUM 18
#define Y2_GPIO_NUM 5
#define VSYNC_GPIO_NUM 25
#define HREF_GPIO_NUM 23
#define PCLK_GPIO_NUM 22

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

#define ROI_X 100 // 根據相機視圖調整（ROI 的 x 座標）
#define ROI_Y 100 // ROI 的 y 座標
#define ROI_WIDTH 50 // ROI 的寬度
#define ROI_HEIGHT 50 // ROI 的高度
#define THRESHOLD 150 // 亮度閾值（0-255）
#define STOP_DELAY 300000 // 5 分鐘（以毫秒為單位）

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // 初始化相機
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_GRAYSCALE; // 灰階以簡化處理
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // 連接到 Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // 配置 Telegram 客戶端
  client.setInsecure(); // 為求簡單；在生產環境中考慮使用適當的 SSL
}

void loop() {
  // 捕捉影像
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }

  // 計算 ROI 內的平均亮度
  uint32_t totalBrightness = 0;
  uint16_t pixelCount = 0;
  for (int y = ROI_Y; y < ROI_Y + ROI_HEIGHT; y++) {
    for (int x = ROI_X; x < ROI_X + ROI_WIDTH; x++) {
      if (x < fb->width && y < fb->height) {
        totalBrightness += fb->buf[y * fb->width + x];
        pixelCount++;
      }
    }
  }
  esp_camera_framebuffer_return(fb);

  float avgBrightness = pixelCount > 0 ? (float)totalBrightness / pixelCount : 0;

  // 狀態機
  if (avgBrightness > THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("Machine is ON");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("Machine stopped");
      bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
    }
  }

  delay(10000); // 每 10 秒檢查一次
}
```

#### 步驟 5：自訂程式碼
1. **更新憑證**：
   - 將 `your_wifi_ssid`、`your_wifi_password`、`your_bot_token` 和 `your_chat_id` 替換為您的實際值。
2. **調整 ROI 和閾值**：
   - 使用 ESP32-CAM 捕捉測試影像（修改程式碼以將影像儲存到 SD 卡或進行串流）。
   - 透過分析影像來確定 ROI 座標（`ROI_X`、`ROI_Y`、`ROI_WIDTH`、`ROI_HEIGHT`），以聚焦於面板燈。
   - 根據測試影像調整 `THRESHOLD`（例如，亮起時較亮，熄滅時較暗）。
3. **調整 `STOP_DELAY`**：
   - 設定為 300000（5 分鐘）以避免在週期暫停期間產生錯誤通知。

#### 步驟 6：測試和部署
1. **上傳程式碼**：
   - 透過 USB 轉串口轉接器（例如 FTDI 模組）將 ESP32-CAM 連接到您的電腦。
   - 在 Arduino IDE 中選擇 **ESP32 Wrover Module** 並上傳草圖碼。
2. **測試系統**：
   - 啟動洗衣機並監控序列監視器以查看狀態變化。
   - 驗證機器停止時的 Telegram 通知。
3. **微調**：
   - 如果出現誤報/漏報，請調整 ROI、閾值或延遲。
4. **永久安裝**：
   - 將 ESP32-CAM 固定在其外殼中，並確保電源供應穩定。

---

### 替代方法：光感測器
如果基於相機的偵測過於複雜或不可靠（例如由於環境光線），請使用光敏電阻：
- **設定**：將光敏電阻連接到面板燈（例如用膠帶），並將其連接到類比引腳。
- **程式碼修改**：用類比讀數替換影像處理：
  ```cpp
  int lightValue = analogRead(A0); // 光敏電阻連接至 GPIO 4
  if (lightValue > 500) { // 調整閾值
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
  }
  ```
- **優點**：更簡單，資源消耗更少。
- **缺點**：需要物理連接到燈光，靈活性較差。

---

### 注意事項
- **功耗**：ESP32-CAM 在使用相機和 Wi-Fi 時會消耗大量電力。請確保使用可靠的電源。
- **環境光線**：基於相機的偵測可能會受到室內光線的影響。請在各種條件下測試，或使用光感測器以增強穩健性。
- **安全性**：範例程式碼為求簡單使用了 `setInsecure()`。在生產環境中，請為 Telegram 通訊配置適當的 SSL 憑證。
- **參考資料**：此方法靈感來自於如 ESP32-CAM Telegram 安全系統和使用振動感測器的洗衣監控器等專案，並針對光線偵測進行了調整。[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### 疑難排解
- **相機初始化失敗**：檢查接線，確保電力充足，並驗證相機配置。
- **Wi-Fi 連接問題**：確認 2.4GHz Wi-Fi 和正確的憑證。
- **沒有 Telegram 訊息**：驗證機器人令牌和聊天 ID，檢查序列監視器是否有錯誤。
- **錯誤通知**：調整 `THRESHOLD` 或 `STOP_DELAY` 以應對週期暫停。

此解決方案利用 ESP32-CAM 的功能，以一種經濟高效、非侵入性的方式監控您的洗衣機，並透過 Telegram 通知您。如果您在特定步驟或除錯方面需要幫助，請告訴我！