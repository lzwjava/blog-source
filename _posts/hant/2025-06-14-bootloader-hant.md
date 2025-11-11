---
audio: false
generated: true
lang: hant
layout: post
title: 燒錄啟動程式
translated: true
type: note
---

為 Arduino Uno R3 燒錄 bootloader 是必要的，當微控制器 (ATmega328P) 是空白、損壞或需要更換時。這個過程會將韌體程式燒錄到晶片中，使其能與 Arduino IDE 通訊並執行 sketch。以下是使用常見方法燒錄 bootloader 的逐步指南。

---

### **需求**
- **Arduino Uno R3** (需要被燒錄 bootloader 的目標板，其上的 ATmega328P 需被程式化)。
- **燒錄器**：以下其中一項：
  - 另一個可正常工作的 Arduino 板 (例如另一個 Uno R3) 作為 "Arduino as ISP"。
  - 專用燒錄器，例如 **USBasp**、**AVRISP mkII** 或 **Atmel-ICE**。
- **Arduino IDE** (從 [arduino.cc](https://www.arduino.cc/en/software) 下載)。
- **跳線** (如果使用 Arduino as ISP)。
- **USB 線** (用於連接燒錄器或 Arduino 到您的電腦)。

---

### **方法 1：使用另一個 Arduino (Arduino as ISP)**

此方法使用第二個 Arduino 板 (例如另一個 Uno R3) 作為在系統燒錄器 (ISP) 來燒錄 bootloader。

#### **步驟**
1. **準備燒錄器 Arduino**：
   - 將第二個 Arduino (燒錄器) 透過 USB 連接到您的電腦。
   - 開啟 Arduino IDE，前往 **檔案 > 範例 > 11.ArduinoISP > ArduinoISP**，並將此 sketch 上傳到燒錄器 Arduino。這會將其轉變為 ISP。

2. **連接開發板**：
   - 將燒錄器 Arduino 連接到目標 Arduino Uno R3 (需要 bootloader 的那一個)，接線如下：
     - **燒錄器 Arduino** → **目標 Arduino Uno R3**：
       - 5V → 5V
       - GND → GND
       - 腳位 10 → Reset
       - 腳位 11 → 腳位 11 (MOSI)
       - 腳位 12 → 腳位 12 (MISO)
       - 腳位 13 → 腳位 13 (SCK)
   - 或者，如果目標 Uno R3 有 **ICSP 接頭**，請使用跳線直接連接對應的 ICSP 腳位 (MOSI, MISO, SCK, VCC, GND, Reset)。

3. **設定 Arduino IDE**：
   - 在 Arduino IDE 中，前往 **工具 > 開發板** 並選擇 **Arduino Uno** (針對目標 Uno R3)。
   - 前往 **工具 > 燒錄器** 並選擇 **Arduino as ISP**。
   - 確保在 **工具 > 序列埠** 下選擇了燒錄器 Arduino 的正確埠。

4. **燒錄 Bootloader**：
   - 前往 **工具 > 燒錄 bootloader**。
   - IDE 將使用燒錄器 Arduino 將 bootloader 燒錄到目標 Uno R3 的 ATmega328P 上。這可能需要一分鐘。
   - 如果成功，您會看到 "Done burning bootloader" 訊息。如果有錯誤，請雙重檢查連接並確保燒錄器 Arduino 正在執行 ArduinoISP sketch。

5. **測試目標板**：
   - 斷開燒錄器 Arduino 和跳線。
   - 透過 USB 將目標 Uno R3 連接到您的電腦。
   - 上傳一個簡單的 sketch (例如從 **檔案 > 範例 > 01.Basics > Blink** 取得的 Blink) 以確認 bootloader 正常工作。

---

### **方法 2：使用專用 ISP 燒錄器 (例如 USBasp)**

如果您有像 USBasp 這樣的專用燒錄器，過程更簡單且通常更可靠。

#### **步驟**
1. **連接燒錄器**：
   - 透過 USB 將 USBasp (或類似燒錄器) 連接到您的電腦。
   - 使用 6-pin ICSP 線將燒錄器連接到目標 Arduino Uno R3 的 **ICSP 接頭**。確保方向正確 (ICSP 接頭上的第 1 腳通常以圓點或凹口標記)。

2. **設定 Arduino IDE**：
   - 開啟 Arduino IDE。
   - 前往 **工具 > 開發板** 並選擇 **Arduino Uno**。
   - 前往 **工具 > 燒錄器** 並選擇您的燒錄器 (例如 **USBasp** 或 **AVRISP mkII**)。
   - 在 **工具 > 序列埠** 下選擇正確的埠 (如果適用，某些燒錄器不需要選擇埠)。

3. **燒錄 Bootloader**：
   - 前往 **工具 > 燒錄 bootloader**。
   - IDE 將使用燒錄器來燒錄 bootloader。這大約需要 10-30 秒。
   - "Done burning bootloader" 訊息表示成功。如果失敗，請檢查連接並確保您的電腦能識別燒錄器。

4. **測試開發板**：
   - 斷開燒錄器。
   - 透過 USB 將 Uno R3 連接到您的電腦，並上傳一個測試 sketch (例如 Blink) 以驗證功能。

---

### **疑難排解提示**
- **錯誤訊息**：如果您收到如 "avrdude: stk500_getsync()" 或 "not in sync" 等錯誤，請檢查：
  - 所有連接 (跳線或 ICSP 線)。
  - 燒錄器 Arduino 是否正在執行 ArduinoISP sketch (方法 1)。
  - IDE 中是否選擇了正確的燒錄器。
- **驅動程式問題**：對於 USBasp 或其他燒錄器，請確保已安裝驅動程式 (例如在 Windows 上使用 Zadig 安裝 USBasp 驅動)。
- **空白微控制器**：如果 ATmega328P 是新的或空白的，且 Uno R3 板上沒有預先安裝，則可能需要連接一個外部 16 MHz 晶振和兩個 22pF 電容到腳位 9 和 10 (XTAL1/XTAL2)。
- **電源供應**：確保目標板在燒錄過程中有供電 (透過 USB 或 VIN)。

---

### **補充說明**
- **為何要燒錄 Bootloader？**：Bootloader 允許 Arduino Uno R3 透過 USB 與 Arduino IDE 通訊以上傳 sketch。沒有它，開發板將無法回應 USB 上傳。
- **Bootloader 類型**：Uno R3 使用 **Optiboot bootloader**，它體積小巧且支援比舊版 bootloader 更快的上傳速度。
- **更換微控制器**：如果您要更換 ATmega328P，請確保它是 ATmega328P-PU (DIP 封裝) 以用於 Uno R3 的插座。SMD 版本需要進階的焊接技術。
- **替代工具**：您也可以使用 **AVRDUDE** 或 **PlatformIO** 來燒錄 bootloader，但 Arduino IDE 對初學者來說是最容易的。

如果您對任何步驟需要澄清或需要特定燒錄器的幫助，請告訴我！