---
audio: false
generated: true
lang: hant
layout: post
title: 以Arduino控制的MOSFET開關
translated: true
type: note
---

看來您的問題可能存在一些誤解。Arduino 無法用於*製造*金屬氧化物半導體場效電晶體（MOSFET），因為 MOSFET 是基礎的半導體元件，需要透過光刻和摻雜等複雜製程在無塵室環境中生產。不過，我猜測您的本意可能是「如何使用 Arduino 來搭建*運用* MOSFET 的電路」或「如何在 Arduino 專案中使用 MOSFET」。若我理解有誤，還請進一步說明！

我將以實際電路應用來說明如何用 Arduino 控制 MOSFET，例如簡單的開關或放大電路。MOSFET 作為多功能元件，常被用作電子開關或放大電路，並能完美搭配 Arduino 的數位輸出功能。以下我將針對常見應用場景提供逐步指南：使用 N 通道 MOSFET（例如 IRF540 或 2N7000）作為由 Arduino 控制的高功率開關。

---

### **專案：透過 Arduino 控制 MOSFET 開關**

#### **概述**
- **目的**：利用 Arduino 透過 MOSFET 控制高功率負載（如 LED 燈條、馬達或燈具）的開關
- **為何選用 MOSFET**：與 BJT 不同，MOSFET 是電壓控制元件，僅需極小電流即可驅動，且能承受比 Arduino 接腳（最高 40mA，5V）更高的電流/電壓

#### **所需元件**
- Arduino（如 Uno 型號）
- N 通道 MOSFET（如 IRF540 或 2N7000；高功率應用建議選用 IRF540）
- 電阻：R1 = 10kΩ（下拉電阻），R2 = 220Ω（閘極保護電阻，可選）
- 負載：如 12V LED 燈條、直流馬達或燈具（需搭配合適電源）
- 二極體（如 1N4007，用於電感性負載如馬達）
- 麵包板、跳線
- 外部電源（如用於負載的 12V 電源）

#### **電路示意圖**
```
Arduino 第 9 腳 ---- R2 (220Ω) ---- 閘極 (G)
                             |
                             |
負載電源 (如 12V) ---- 負載 ---- 汲極 (D)
                             | 
                             |
                           源極 (S) ---- GND
                             |
                            R1 (10kΩ)
                             |
                            GND
```
- **電感性負載（如馬達）**：需在負載兩端並聯飛輪二極體（1N4007）（陰極接 V_load，陽極接汲極）以保護 MOSFET 免受電壓突波衝擊
- **電源配置**：Arduino 透過 USB 或 5V 供電；負載由外部電源供電（如 12V）。所有 GND 需共接

#### **運作原理**
- **MOSFET 功能**：作為汲極與源極間的開關，由閘極電壓控制
- **Arduino 功能**：透過第 9 腳輸出 HIGH（5V）或 LOW（0V）訊號至閘極
- **邏輯控制**：
  - 閘極 HIGH（5V）→ MOSFET 導通 → 負載通電
  - 閘極 LOW（0V）→ MOSFET 斷開 → 負載斷電
- **R1（下拉電阻）**：確保 Arduino 關閉或腳位浮接時閘極保持 LOW
- **R2（可選）**：限制閘極電流（對於邏輯位準 MOSFET 通常非必要）

---

### **步驟 1：搭建電路**

1. **連接 MOSFET**：
   - **閘極 (G)**：透過 R2（220Ω，可選）連接至 Arduino 第 9 腳
   - **汲極 (D)**：連接至負載負極（如 LED 燈條陰極）
   - **源極 (S)**：連接至 GND
2. **負載與電源**：
   - 將負載正極連接至 V_load（如 12V 電源）
   - 將 12V 電源 GND 連接至 Arduino GND
3. **安全措施**：
   - 在閘極與 GND 間添加 R1（10kΩ）
   - 若驅動馬達，需在負載兩端並聯二極體

---

### **步驟 2：Arduino 程式碼**

#### **簡易開關控制**
```cpp
const int mosfetPin = 9; // 支援 PWM 的腳位

void setup() {
  pinMode(mosfetPin, OUTPUT); // 設定腳位為輸出模式
}

void loop() {
  digitalWrite(mosfetPin, HIGH); // 開啟 MOSFET
  delay(1000);                   // 延遲 1 秒
  digitalWrite(mosfetPin, LOW);  // 關閉 MOSFET
  delay(1000);                   // 延遲 1 秒
}
```
- **輸出效果**：負載每秒開關一次

#### **PWM 調光（適用 LED/馬達）**
```cpp
const int mosfetPin = 9;

void setup() {
  pinMode(mosfetPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness += 5) {
    analogWrite(mosfetPin, brightness); // 增強亮度
    delay(50);
  }
  for (int brightness = 255; brightness >= 0; brightness -= 5) {
    analogWrite(mosfetPin, brightness); // 減弱亮度
    delay(50);
  }
}
```
- **輸出效果**：負載（如 LED）呈現淡入淡出效果

---

### **步驟 3：測試驗證**

1. **上傳程式碼**：使用 Arduino IDE 上傳任一段程式
2. **啟動電源**：連接 Arduino USB 線與負載外部電源
3. **觀察現象**：
   - 執行開關程式時，負載應每秒切換狀態
   - 執行 PWM 程式時，負載應呈現漸明漸暗效果
4. **量測檢驗**：使用三用電表檢測：
   - 閘極電壓（0V 或 5V）
   - 負載兩端電壓（0V 或 V_load）

---

### **選擇合適的 MOSFET**
- **邏輯位準 MOSFET（如 IRL540、2N7000）**：可被 Arduino 的 5V 電壓完全導通，為本專案首選
- **標準 MOSFET（如 IRF540）**：需要約 10V 閘極電壓才能完全導通。若使用 5V 驅動可能僅部分導通——此時需搭配電晶體或驅動器（如 BJT 或 TC4420 晶片）提升閘極電壓
- **規格考量**：確認 V_DS（最大耐壓）與 I_D（最大電流）符合負載需求（例如 IRF540：100V，33A）

---

### **替代方案：MOSFET 放大電路**
若您實際需要的是 MOSFET 放大電路（例如共源極放大電路），以下是簡要說明：
- **配置**：類似 CE 放大電路，但改用 MOSFET（如 2N7000）
- **示意圖**：Vcc → RD（汲極電阻）→ 汲極；源極 → GND；閘極 → 輸入訊號（透過電容耦合）
- **Arduino 功能**：產生小型交流訊號（如同 CE 放大電路範例）
- **增益公式**：\\( A_v = -g_m \cdot R_D \\)，其中 \\( g_m \\) 為轉導率
- **挑戰**：需要精確偏壓設定；相較於 BJT 放大電路更不適合初學者

若有需要轉向此應用，請隨時告知！

---

### **技巧與故障排除**
- **過熱處理**：若 MOSFET 發燙，可能是未完全導通（檢查邏輯位準相容性）或負載超標——可加裝散熱片或降低電流
- **無反應檢修**：檢查接線、MOSFET 接腳定義（GDS）與電源供應
- **雜訊處理**：馬達在 PWM 切換時可能產生可聞噪音——可嘗試調整頻率（進階技巧）
- **高電壓應用**：驅動 >5V 負載時，需確保滿足 MOSFET 的 V_GS 臨界電壓

本專案展示了如何將 MOSFET 與 Arduino 整合實現實際控制功能。是否需要擴展應用（如馬達調速）或改探討放大電路？歡迎隨時提出！