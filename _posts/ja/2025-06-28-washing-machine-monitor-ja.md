---
audio: false
generated: true
lang: ja
layout: post
title: ArduinoとTelegramアラート搭載スマート洗濯機モニター
translated: true
type: note
---

Maytag MHW8630HW洗濯機が停止したことを（パネルライトを指標として）検知し、Telegramボットを通じて洗濯物を干すよう通知するシステムを作成するには、カメラモジュールを搭載したArduinoを使用して洗濯機の状態を監視することができます。以下に、技術スタック、ハードウェア設定、アルゴリズム、実装手順に関する詳細なガイドを示します。

---

### 技術スタック
#### ハードウェア
1. **Arduinoボード**:
   - **ESP32-CAM**（推奨）– マイクロコントローラと内蔵OV2640カメラ、Wi-Fi機能を組み合わせたもので、画像処理とTelegram連携に最適です。
   - 代替案: Arduino Uno + 別途カメラモジュール（例: OV7670）とWi-Fi用ESP8266ですが、設定がより複雑になります。
2. **カメラモジュール**:
   - OV2640（ESP32-CAMに同梱）– パネルライトの検出に十分な2MPカメラです。
3. **光センサー（オプション）**:
   - フォトレジスタ（LDR）またはTSL2561 – カメラベースの光検出を補完するため、または冗長性やよりシンプルな設定のために使用します。
4. **電源**:
   - ESP32-CAM用の5V USB電源アダプタまたはバッテリーパック。
5. **取り付け**:
   - ESP32-CAMを収納する小型エンクロージャーまたは3Dプリントケース。洗濯機の操作パネルがはっきり見える位置に設置します。
6. **Wi-Fiルーター**:
   - ESP32-CAMがインターネットに接続し、Telegramボットと通信するために使用します。

#### ソフトウェア
1. **Arduino IDE**:
   - ESP32-CAMのプログラミングに使用します。
2. **ライブラリ**:
   - **Universal Arduino Telegram Bot Library** by Brian Lough – Telegramボット連携用。
   - **ArduinoJson** – Telegram API通信のためのJSONデータを扱います。
   - **ESP32-CAM Camera Libraries** – 画像のキャプチャと処理用の内蔵ライブラリ。
3. **Telegram Bot**:
   - TelegramでBotFatherを使用してボットを作成し、ボットトークンとチャットIDを取得します。
4. **プログラミング言語**:
   - C++（Arduinoスケッチ）。
5. **オプションツール**:
   - OpenCV（Python）– Arduinoへの移植前にコンピュータ上で画像処理アルゴリズムをプロトタイピングする場合に使用（ESP32-CAM用に簡略化）。

---

### 洗濯機状態検知のアルゴリズム
Maytag MHW8630HWには、電源が入っていることを示すパネルライトがあるため、カメラを使用してこのライトを検出できます。このアルゴリズムは、ライトの点灯/消灯を示す画像を処理して、洗濯機の状態を判断します。

#### 検知アルゴリズム
1. **画像キャプチャ**:
   - ESP32-CAMを使用して、洗濯機の操作パネルの画像を定期的にキャプチャします。
2. **関心領域（ROI）の選択**:
   - 画像内でパネルライトが位置する特定の領域（例: 電源インジケーター周辺の矩形領域）を定義します。
3. **画像処理**:
   - **グレースケール変換**: 処理を単純化するため、キャプチャした画像をグレースケールに変換します。
   - **二値化**: 輝度の閾値を適用してライトの存在を検出します。パネルライトは点灯時に明るいスポットを、消灯時には暗い領域を生成します。
   - **画素強度分析**: ROI内の平均画素強度を計算します。強度が高い場合はライトが点灯、低い場合は消灯を示します。
4. **状態機械**:
   - 連続した読み取りに基づいて洗濯機の状態（ONまたはOFF）を追跡します。
   - ライトが数サイクルにわたってONとして検出された場合、洗濯機が動作中と見なします。
   - ライトがOFFに遷移し、設定された時間（例: 5分間）OFFのままの場合、洗濯サイクルが完了したと見なします。
5. **デバウンス**:
   - 洗濯サイクル中の一時停止（例: 浸けおきや給水）による誤通知を避けるため、確認用の遅延（例: 5分）を実装します。
6. **通知**:
   - 洗濯機の停止が確認されたら、Telegramメッセージ（例: 「洗濯機が停止しました！洗濯物を干す時間です。」）を送信します。

#### より複雑なアルゴリズムを使用しない理由
- 機械学習（例: 物体検出用CNN）などの高度なアルゴリズムは、このタスクには過剰であり、ESP32-CAMの限られた処理能力ではリソースを大量に消費します。
- パネルライトは明確な二値指標（ON/OFF）であるため、単純な二値化で十分です。

---

### 実装ガイド
#### ステップ 1: Telegramボットの設定
1. **Telegramボットの作成**:
   - Telegramを開き、**@BotFather**を検索してチャットを開始します。
   - `/newbot`を送信し、ボットに名前（例: "WasherBot"）を付け、**ボットトークン**を取得します。
   - ボットに`/start`を送信し、`@GetIDsBot`などのサービスを使用するか、コード内の受信メッセージを確認して**チャットID**を取得します。
2. **スマートフォンにTelegramをインストール**:
   - ボットからメッセージを受信できることを確認します。

#### ステップ 2: ハードウェア設定
1. **ESP32-CAMの設置**:
   - ESP32-CAMを小型エンクロージャーまたは粘着テープで固定し、洗濯機の操作パネルに向けます。
   - カメラがパネルライトを明確に視認できることを確認します（サンプル写真でテスト）。
   - 動きによるROIの一貫性への影響を避けるため、設置を確実に行います。
2. **ESP32-CAMへの給電**:
   - 5V USB電源アダプタまたはバッテリーパックをESP32-CAMの5Vピンに接続します。
   - カメラとWi-Fiがかなりの電力を消費するため、安定した電源を確保します。
3. **オプションの光センサー**:
   - フォトレジスタを使用する場合、電圧分割回路（例: 10kΩ抵抗をGNDに接続）を用いて、ESP32-CAMのアナログピン（例: GPIO 4）に接続します。

#### ステップ 3: ソフトウェア設定
1. **Arduino IDEのインストール**:
   - [arduino.cc](https://www.arduino.cc/en/software)からArduino IDEをダウンロードしてインストールします。
2. **ESP32ボードサポートの追加**:
   - Arduino IDEで、**ファイル > 環境設定**に移動し、追加のボードマネージャのURLに以下のURLを追加します:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - **ツール > ボード > ボードマネージャ**に移動し、"ESP32"を検索してESP32パッケージをインストールします。
3. **ライブラリのインストール**:
   - **Universal Arduino Telegram Bot Library**のインストール:
     - [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot)からダウンロードし、**スケッチ > ライブラリをインクルード > .ZIPライブラリを追加**で追加します。
   - **ArduinoJson**のインストール:
     - **スケッチ > ライブラリをインクルード > ライブラリを管理**に移動し、"ArduinoJson"を検索してバージョン6.x.xをインストールします。
4. **Wi-Fiの設定**:
   - ESP32-CAMがご自宅のWi-Fiネットワーク（2.4GHz、5GHzは非対応）に接続できることを確認します。

#### ステップ 4: Arduinoコードの記述
以下は、ESP32-CAMがパネルライトを検出し、Telegram通知を送信するためのサンプルArduinoスケッチです。このコードは、パネルライトのROI座標を特定済みであることを前提としています。

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// Wi-Fi認証情報
#define WIFI_SSID "your_wifi_ssid"
#define WIFI_PASSWORD "your_wifi_password"

// Telegram Bot認証情報
#define BOT_TOKEN "your_bot_token"
#define CHAT_ID "your_chat_id"

// カメラ設定 (ESP32-CAM用)
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

#define ROI_X 100 // カメラビューに基づいて調整 (ROIのX座標)
#define ROI_Y 100 // ROIのY座標
#define ROI_WIDTH 50 // ROIの幅
#define ROI_HEIGHT 50 // ROIの高さ
#define THRESHOLD 150 // 輝度閾値 (0-255)
#define STOP_DELAY 300000 // 5分（ミリ秒）

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // カメラの初期化
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
  config.pixel_format = PIXFORMAT_GRAYSCALE; // 単純化のためグレースケール
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // Wi-Fiに接続
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Telegramクライアントの設定
  client.setInsecure(); // 簡略化のため。本番環境では適切なSSLを構成してください。
}

void loop() {
  // 画像キャプチャ
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Camera capture failed");
    return;
  }

  // ROI内の平均輝度を計算
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

  // 状態機械
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

  delay(10000); // 10秒ごとにチェック
}
```

#### ステップ 5: コードのカスタマイズ
1. **認証情報の更新**:
   - `your_wifi_ssid`、`your_wifi_password`、`your_bot_token`、`your_chat_id`を実際の値に置き換えます。
2. **ROIと閾値の調整**:
   - ESP32-CAMを使用してテスト画像をキャプチャします（画像をSDカードに保存またはストリーミングするようにコードを修正）。
   - 画像を分析してパネルライトに焦点を当てるようにROI座標（`ROI_X`、`ROI_Y`、`ROI_WIDTH`、`ROI_HEIGHT`）を決定します。
   - テスト画像に基づいて`THRESHOLD`を調整します（例: ON時に明るく、OFF時に暗い）。
3. **`STOP_DELAY`の調整**:
   - サイクル中の一時停止による誤通知を避けるため、300000（5分）に設定します。

#### ステップ 6: テストとデプロイ
1. **コードのアップロード**:
   - USB-to-シリアル変換アダプタ（例: FTDIモジュール）を介してESP32-CAMをコンピュータに接続します。
   - Arduino IDEで**ESP32 Wrover Module**を選択し、スケッチをアップロードします。
2. **システムのテスト**:
   - 洗濯機を起動し、シリアルモニターで状態変化を監視します。
   - 洗濯機停止時のTelegram通知を確認します。
3. **微調整**:
   - 誤検知/検知漏れが発生する場合、ROI、閾値、遅延を調整します。
4. **恒久的な設置**:
   - ESP32-CAMをエンクロージャー内に固定し、安定した電源を確保します。

---

### 代替アプローチ: 光センサー
カメラベースの検出が複雑すぎる、または信頼性に欠ける場合（例: 環境光の影響）、フォトレジスタを使用します:
- **設定**: フォトレジスタをパネルライトに（テープなどで）取り付け、アナログピンに接続します。
- **コード修正**: 画像処理をアナログ読み取りに置き換えます:
  ```cpp
  int lightValue = analogRead(A0); // GPIO 4のフォトレジスタ
  if (lightValue > 500) { // 閾値を調整
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Washing machine stopped! Time to hang up clothes.", "");
  }
  ```
- **長所**: よりシンプルで、リソース消費が少ない。
- **短所**: ライトへの物理的な取り付けが必要で、柔軟性に欠ける。

---

### 注意点
- **消費電力**: ESP32-CAMは、カメラとWi-Fiを使用する際にかなりの電力を消費します。信頼性の高い電源を確保してください。
- **環境光**: カメラベースの検出は、室内の照明の影響を受ける可能性があります。様々な条件でテストするか、堅牢性のために光センサーを使用してください。
- **セキュリティ**: サンプルコードは簡略化のため`setInsecure()`を使用しています。本番環境では、Telegram通信用に適切なSSL証明書を構成してください。
- **参考情報**: このアプローチは、ESP32-CAM Telegramセキュリティシステムや振動センサーを使用した洗濯監視装置などのプロジェクトに着想を得て、光ベースの検出用に適合させたものです。[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### トラブルシューティング
- **カメラの初期化に失敗**: 配線を確認し、十分な電源を確保し、カメラ設定を検証してください。
- **Wi-Fi接続の問題**: 2.4GHz Wi-Fiと正しい認証情報を確認してください。
- **Telegramメッセージが届かない**: ボットトークンとチャットIDを確認し、シリアルモニターでエラーをチェックしてください。
- **誤通知**: サイクル中の一時停止に対応するため、`THRESHOLD`または`STOP_DELAY`を調整してください。

このソリューションは、ESP32-CAMの機能を活用し、コスト効率が良く非侵襲的な方法で洗濯機を監視し、Telegram経由で通知します。特定のステップやデバッグに助けが必要な場合はお知らせください！