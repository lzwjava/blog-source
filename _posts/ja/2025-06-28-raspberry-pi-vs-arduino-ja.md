---
audio: false
generated: true
lang: ja
layout: post
title: ラズベリーパイ対アルドゥイーノ：テレグラムアラート付き洗濯機監視システム
translated: true
type: note
---

Maytag MHW8630HW洗濯機の停止を検出してTelegram通知を送信するために、Arduino（ESP32-CAMなど）の代わりにRaspberry Piを使用することは、複雑さと消費電力が増加する代償により多くの処理能力と柔軟性を提供する実行可能な代替案です。以下では、Raspberry PiアプローチとArduinoソリューションを比較し、他のマイクロコントローラオプションの概要を説明し、Raspberry Piを使用してシステムを実装するための詳細なガイドを提供します。また、包括的な回答を確保するために、他のアプローチ（例えば、他のハードウェアやセンサー）についても議論します。

---

### 比較: Raspberry Pi vs. Arduino vs. その他のオプション

| **機能**                 | **Raspberry Pi**                                                                 | **Arduino (ESP32-CAM)**                                                  | **その他のオプション (例: NodeMCU, ESP8266)**                           |
|-------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **処理能力**            | 高い（クアッドコアCPU、1-8GB RAM） – 高度な画像処理、OpenCVをサポート。         | 限定的（デュアルコア、520KB SRAM） – 基本的な画像処理のみ。              | 非常に限定的 – カメラベースの処理には不向き。                           |
| **カメラサポート**      | USBウェブカムまたはPi Camera Module（例: 8MP Pi Camera v2）で容易。             | 内蔵OV2640（2MP）カメラ、ただし解像度と品質は低い。                      | 外部カメラモジュールが必要、統合が複雑。                               |
| **Wi-Fi**               | 内蔵（ほとんどのモデル、例: Pi 4, Zero 2 W）。                                  | 内蔵（ESP32-CAM）。                                                     | 内蔵（例: ESP8266）、ただしネイティブのカメラサポートなし。            |
| **プログラミング**       | Python, OpenCV、汎用的だがOSセットアップ（Raspberry Pi OS）が必要。             | Arduino IDEでのC++、初心者向けにシンプル。                              | C++またはLua（例: NodeMCU）、画像処理用のライブラリが限定的。          |
| **消費電力**            | 高い（~2.5W for Pi Zero, ~5-10W for Pi 4）。                                    | 低い（~1-2W for ESP32-CAM）。                                           | 最低（~0.5-1W for ESP8266）。                                          |
| **コスト**              | $10（Pi Zero W）から$35以上（Pi 4）+ Pi Camera $15。                           | ~$10（カメラ付きESP32-CAM）。                                           | ~$5-10（ESP8266/NodeMCU）+ センサーコスト。                            |
| **セットアップの容易さ** | 中程度（OSセットアップ、Pythonコーディング）。                                 | 容易（Arduino IDE、単一スケッチ）。                                     | 単純なセンサーには容易、カメラには複雑。                               |
| **最適な使用例**        | 高度な画像処理、将来の拡張（例: MLモデル）に柔軟。                             | シンプルで低コストな光検出とTelegram統合。                              | 非カメラソリューション（例: 振動センサーまたは電流センサー）。         |

**Raspberry Piの利点**:
- 堅牢な光検出のためのOpenCVによる優れた画像処理。
- デバッグと拡張が容易（例: Webインターフェースや複数センサーの追加）。
- 様々な照明条件での精度向上のため、高品質なカメラをサポート。

**Raspberry Piの欠点**:
- より多くのセットアップが必要（OSインストール、Python環境）。
- 消費電力が高く、バッテリー駆動セットアップには理想的ではない。
- ESP32-CAMよりも高価。

**その他のオプション**:
- **NodeMCU/ESP8266**: 非カメラソリューション（例: 振動センサーや電流センサーの使用）に適している。処理能力が限られるため、カメラ統合は非現実的。
- **振動センサー**: パネルライトの代わりに機械の振動を検出。シンプルだが、微妙なサイクルの変化を見逃す可能性がある。
- **電流センサー**: 電力消費を測定（例: ACS712モジュール）して機械の停止を検出。非侵襲的だが、電気的セットアップが必要。

---

### Raspberry Pi実装ガイド

#### 技術スタック
**ハードウェア**:
1. **Raspberry Pi**:
   - **Raspberry Pi Zero 2 W**（$15、コンパクト、Wi-Fi内蔵）または**Raspberry Pi 4**（$35以上、より高性能）。
2. **カメラ**:
   - **Raspberry Pi Camera Module v2**（$15、8MP）またはUSBウェブカム。
3. **電源供給**:
   - 5V USB-C（Pi 4）またはmicro-USB（Pi Zero）、2-3A出力。
4. **取り付け**:
   - カメラを洗濯機のパネルライトに向けて配置するためのエンクロージャーまたは粘着マウント。

**ソフトウェア**:
1. **OS**: Raspberry Pi OS（効率性のためLite、セットアップ容易性のためFull）。
2. **プログラミング言語**: Python。
3. **ライブラリ**:
   - **OpenCV**: パネルライトを検出するための画像処理。
   - **python-telegram-bot**: Telegram通知用。
   - **picamera2**（Pi Camera用）または**fswebcam**（USBウェブカム用）。
4. **Telegram Bot**: Arduinoと同じセットアップ（BotFatherを使用してボットトークンとチャットIDを取得）。

#### アルゴリズム
このアルゴリズムはArduinoアプローチと似ていますが、より堅牢な画像処理のためにOpenCVを活用します：
1. **画像キャプチャ**: Pi Cameraまたはウェブカムを使用して、定期的に（例: 10秒ごとに）画像をキャプチャ。
2. **関心領域（ROI）**: 画像内のパネルライト周辺に矩形を定義。
3. **画像処理**:
   - グレースケールに変換。
   - ガウシアンブラーを適用してノイズを低減。
   - 適応的しきい値処理を使用して背景に対して明るいパネルライトを検出。
   - ROI内の平均ピクセル強度を計算するか、明るいピクセルをカウント。
4. **状態機械**:
   - ROIが明るい（ライトON）場合、機械を動作中としてマーク。
   - ROIが暗い（ライトOFF）状態が5分間続いた場合、機械を停止としてマークし、Telegram通知を送信。
5. **デバウンス**: 機械が停止したことを確認するために5分の遅延を実装。

#### 実装ステップ
1. **Raspberry Piのセットアップ**:
   - **Raspberry Pi OS**（LiteまたはFull）をRaspberry Pi Imagerを使用してSDカードにダウンロードおよび書き込み。
   - `/etc/wpa_supplicant/wpa_supplicant.conf`を編集するかGUIを使用してPiをWi-Fiに接続。
   - `raspi-config`（Interfacing Options > Camera）を介してカメラインターフェースを有効化。

2. **依存関係のインストール**:
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-picamera2 python3-pip
   pip3 install python-telegram-bot
   ```

3. **カメラの配置**:
   - Pi CameraまたはUSBウェブカムを洗濯機のパネルライトに向けて取り付け。
   - 以下でカメラをテスト：
     ```bash
     libcamera-still -o test.jpg
     ```
     またはUSBウェブカムの場合：
     ```bash
     fswebcam test.jpg
     ```

4. **Pythonスクリプト**:
以下は、パネルライトを検出してTelegram通知を送信するためのRaspberry Pi用サンプルPythonスクリプトです。

```python
import cv2
import numpy as np
from picamera2 import Picamera2
import telegram
import asyncio
import time

# Telegram bot設定
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
bot = telegram.Bot(token=BOT_TOKEN)

# カメラ設定
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))
picam2.start()

# ROI設定（カメラビューに基づいて調整）
ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT = 200, 150, 50, 50
THRESHOLD = 150  # 明るさのしきい値 (0-255)
STOP_DELAY = 300  # 5分（秒）

machine_running = False
last_on_time = 0

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def is_light_on(frame):
    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ガウシアンブラーを適用
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # ROIを抽出
    roi = gray[ROI_Y:ROI_Y+ROI_HEIGHT, ROI_X:ROI_X+ROI_WIDTH]
    # 平均輝度を計算
    avg_brightness = np.mean(roi)
    return avg_brightness > THRESHOLD

async def main():
    global machine_running, last_on_time
    while True:
        # 画像をキャプチャ
        frame = picam2.capture_array()
        # ライトがオンかチェック
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
        time.sleep(10)  # 10秒ごとにチェック

if __name__ == "__main__":
    asyncio.run(main())
```

5. **スクリプトのカスタマイズ**:
   - `BOT_TOKEN`と`CHAT_ID`をあなたのTelegram認証情報に置き換え。
   - テスト画像をキャプチャし、GIMPやPythonなどのツールで分析してパネルライトの位置を特定し、`ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT`を調整。
   - テスト画像に基づいて`THRESHOLD`を調整（明るいライトには高い値）。
   - 必要に応じて`STOP_DELAY`を変更。

6. **スクリプトの実行**:
   ```bash
   python3 washer_monitor.py
   ```
   - 信頼性のために、`nohup python3 washer_monitor.py &`でバックグラウンドで実行するか、systemdサービスを使用。

7. **テストとデプロイ**:
   - 洗濯機を起動し、スクリプトの出力を監視。
   - Telegram通知を確認。
   - Piとカメラを恒久的なセットアップで固定。

---

### その他の代替案
1. **振動センサー**:
   - **ハードウェア**: ESP8266またはRaspberry Piで振動センサー（例: SW-420）を使用。
   - **セットアップ**: センサーを洗濯機に取り付けて振動を検出。
   - **アルゴリズム**: 持続的な振動の欠如（例: 5分間）を監視して機械の停止を検出。
   - **利点**: シンプル、低コスト、環境光の影響を受けない。
   - **欠点**: 長い休止（例: 浸けおき）を含むサイクルを見逃す可能性がある。
   - **コード例（ESP8266）**:
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

2. **電流センサー**:
   - **ハードウェア**: ESP8266またはRaspberry PiでACS712電流センサーを使用。
   - **セットアップ**: 洗濯機の電源コード周囲にセンサーを非侵襲的にクランプ。
   - **アルゴリズム**: 電流がしきい値（例: <0.5A）を下回った状態が5分間続くことを検出。
   - **利点**: 正確、非侵襲的。
   - **欠点**: 電気的知識、機械の電力消費に対するキャリブレーションが必要。

3. **マイク**:
   - **ハードウェア**: Raspberry Piでマイクモジュール（例: KY-038）を使用。
   - **アルゴリズム**: サウンドレベルを分析して機械の騒音が止んだことを検出。
   - **利点**: 非視覚的、低照度条件で動作。
   - **欠点**: 環境ノイズに敏感、信号処理が必要。

---

### 推奨
- **Raspberry Pi**: 堅牢な画像処理と将来の拡張性のために最適。Pythonに慣れており、様々な照明条件での高い信頼性を求める場合に使用。
- **Arduino (ESP32-CAM)**: 低コストでシンプルなセットアップに最適。最小限の設定で済み、基本的な画像処理で問題ない場合に理想的。
- **振動または電流センサー**: 非カメラソリューションに最適、特にパネルライトが信頼できない（例: 暗いまたは遮られている）場合。シンプルさのためにESP8266で使用。
- **マイク**: 環境ノイズのため信頼性は低いが、二次センサーとして実行可能。

あなたの二階建ての家では、二階にいるためTelegramを介した信頼性の高いリモート通知が必要です。Raspberry Piは光検出の精度が高く、ESP32-CAMはより安価で導入が簡単です。非カメラアプローチを希望する場合は、ESP8266での振動センサーが最も簡単な代替案です。

特定のアプローチについてより深く掘り下げたい、セットアップのヘルプが必要、または代替センサーのコードが欲しい場合は、お知らせください！