---
audio: false
generated: true
lang: hant
layout: post
title: Arduino 入門指南
translated: true
type: note
---

你的問題似乎有點小混淆。你是指「如何玩 Arduino」還是「如何用 Arduino 進行互動」？我假設你是想了解如何開始使用 Arduino 這個用於建構電子專案的熱門微控制器平台。如果我的理解有誤，請隨時澄清！

Arduino 並非像遊戲那樣「玩」的東西——它是用來創建互動專案的工具。你可以透過編程控制燈光、感測器、馬達等元件。下面我將帶你了解基礎入門知識，並提供一些適合初學者的範例。

---

### **如何開始使用 Arduino**
1. **所需物品：**
   - Arduino 開發板（例如常見的入門板 Arduino Uno）
   - USB 連接線（Uno 通常使用 USB-A 轉 USB-B 線）
   - 已安裝 Arduino IDE（整合開發環境）的電腦——可從 [arduino.cc](https://www.arduino.cc/en/software) 免費下載
   - 基礎元件如 LED、電阻、麵包板和跳線（可選但對範例實作很有幫助）

2. **設定步驟：**
   - 用 USB 線將 Arduino 連接到電腦
   - 開啟 Arduino IDE，在 `工具 > 開發板` 中選擇你的開發板（如「Arduino Uno」），並在 `工具 > 連接埠` 中選擇正確的連接埠

3. **程式編寫：**
   - Arduino 使用簡化版的 C/C++ 語言。你編寫的「sketches」（程式）包含兩個主要函數：
     - `setup()`：在 Arduino 啟動時執行一次
     - `loop()`：在 setup 後重複執行
   - 點擊 IDE 中的「上傳」按鈕將程式碼上傳到開發板

4. **從小專案開始：**
   - 先從簡單專案入手理解運作原理，再逐步提升難度

---

### **範例專案**

#### **1. LED 閃爍（Arduino 的 Hello World）**
此範例使用大多數 Arduino 開發板上內建的 13 號引腳 LED
```cpp
void setup() {
  pinMode(13, OUTPUT); // 將 13 號引腳設為輸出模式
}

void loop() {
  digitalWrite(13, HIGH); // 開啟 LED
  delay(1000);            // 等待 1 秒
  digitalWrite(13, LOW);  // 關閉 LED
  delay(1000);            // 等待 1 秒
}
```
- **運作原理：** LED 會以每秒間隔閃爍
- **硬體需求：** 只需 Arduino 開發板，無需其他元件

#### **2. 按鈕控制 LED**
透過按鈕控制外部 LED
- **所需元件：** LED、220 歐姆電阻、按鈕、麵包板、跳線
- **接線方式：**
  - LED 陽極（較長接腳）透過電阻連接 9 號引腳，陰極連接 GND
  - 按鈕：一側接 2 號引腳，另一側接 GND（使用內部上拉電阻）

```cpp
int ledPin = 9;   // LED 連接至 9 號引腳
int buttonPin = 2; // 按鈕連接至 2 號引腳

void setup() {
  pinMode(ledPin, OUTPUT);      // 設定 LED 引腳為輸出模式
  pinMode(buttonPin, INPUT_PULLUP); // 設定按鈕引腳為輸入模式並啟用上拉電阻
}

void loop() {
  int buttonState = digitalRead(buttonPin); // 讀取按鈕狀態
  if (buttonState == LOW) {     // 按鈕按下時（因上拉電阻呈現 LOW）
    digitalWrite(ledPin, HIGH); // 開啟 LED
  } else {
    digitalWrite(ledPin, LOW);  // 關閉 LED
  }
}
```
- **運作原理：** 按下按鈕點亮 LED，放開後熄滅

#### **3. LED 漸暗效果（PWM 範例）**
使用脈衝寬度調變（PWM）實現 LED 漸亮漸暗效果
- **所需元件：** LED、220 歐姆電阻
- **接線方式：** LED 連接至 9 號引腳（支援 PWM 的引腳），電阻連接 GND

```cpp
int ledPin = 9; // LED 連接至 PWM 引腳 9

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness += 5) {
    analogWrite(ledPin, brightness); // 設定亮度（0-255）
    delay(30);                       // 短暫延遲
  }
  for (int brightness = 255; brightness >= 0; brightness -= 5) {
    analogWrite(ledPin, brightness);
    delay(30);
  }
}
```
- **運作原理：** LED 會從熄滅逐漸增至最亮，再逐漸變暗，循環往復

---

### **給初學者的建議**
- **動手實驗：** 改寫範例——調整延遲時間、更換引腳或增加元件
- **參考教學：** 查閱 Arduino 官方網站（[arduino.cc](https://www.arduino.cc/en/Tutorial/HomePage)）或 YouTube 的視覺化教學
- **入門套件：** 初學者套件（如 Arduino 官方套件）包含多元元件與專案構想
- **疑難排解：** 若運作異常，請仔細檢查接線、引腳編號和程式碼語法

如果你需要更多範例、特定專案的協助，或是電路圖（我無法直接生成圖片，但可以嘗試用文字描述），請隨時告訴我！你打算先嘗試哪個專案呢？