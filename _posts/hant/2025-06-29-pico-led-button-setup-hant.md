---
audio: false
generated: true
lang: hant
layout: post
title: 樹莓派 Pico LED 按鈕設定
translated: true
type: note
---

要設定 Raspberry Pi Pico 執行提供的 MicroPython 程式碼（透過按鈕控制 LED），請按照以下步驟操作：

### 硬體需求
- **Raspberry Pi Pico**（或 Pico W）
- **LED**（需搭配適當限流電阻，例如 220–330 歐姆）
- **按鈕開關**
- **跳線**
- **麵包板**（可選，方便連接）
- **USB 傳輸線**（用於連接 Pico 與電腦）

### 硬體設定
1. **連接 LED**：
   - 將 LED 的陽極（較長接腳）連接至 Pico 的 **GPIO 25**（實體針腳 30）
   - 將 LED 的陰極（較短接腳）透過 220–330 歐姆限流電阻連接至 **接地（GND）** 針腳（例如實體針腳 3）

2. **連接按鈕**：
   - 將按鈕一端連接至 **GPIO 14**（實體針腳 19）
   - 將按鈕另一端連接至 **3.3V** 針腳（例如實體針腳 36，3V3(OUT)）
   - 程式碼使用內部下拉電阻（`Pin.PULL_DOWN`），因此無需外接下拉電阻。當按鈕按下時，GPIO 14 將讀取 HIGH (1)；未按下時讀取 LOW (0)

3. **檢查連接**：
   - 確認所有連接穩固。使用麵包板或直接焊接，並雙重檢查 LED 極性與電阻安裝位置是否正確
   - 請參考 Pico 針腳圖（可於線上或 Pico 資料手冊中取得）確認針腳分配

### 軟體設定
1. **在 Pico 上安裝 MicroPython**：
   - 從 [MicroPython 官方網站](https://micropython.org/download/rp2-pico/) 下載最新版 Raspberry Pi Pico 適用的 MicroPython UF2 韌體
   - 按住 **BOOTSEL** 按鈕的同時，透過 USB 傳輸線將 Pico 連接至電腦
   - Pico 將顯示為 USB 磁碟機（RPI-RP2）。將下載的 `.uf2` 檔案拖放至此磁碟機
   - Pico 將自動重新啟動並完成 MicroPython 安裝

2. **設定開發環境**：
   - 安裝相容 MicroPython 的 IDE，例如 **Thonny**（推薦初學者使用）：
     - 從 [thonny.org](https://thonny.org) 下載並安裝 Thonny
     - 在 Thonny 中前往 **Tools > Options > Interpreter**，選擇 **MicroPython (Raspberry Pi Pico)** 並選取適當連接埠（例如 Windows 的 `COMx` 或 Linux/macOS 的 `/dev/ttyACM0`）
   - 亦可使用其他工具如 `rshell`、`ampy` 或搭配 MicroPython 擴充功能的 Visual Studio Code

3. **上傳並執行程式碼**：
   - 將提供的程式碼複製到名為 `main.py` 的檔案中：
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)
     button = Pin(14, Pin.IN, Pin.PULL_DOWN)

     while True:
         if button.value():
             led.on()
         else:
             led.off()
         time.sleep(0.05)
     ```
   - 在 Thonny 中：
     - 開啟新檔案，貼上程式碼後儲存至 Pico 並命名為 `main.py`（MicroPython 會在啟動時自動執行 `main.py`）
     - 點擊 **Run** 按鈕或按 **F5** 上傳並執行程式碼
   - 亦可使用 `ampy` 上傳檔案：
     ```bash
     ampy --port /dev/ttyACM0 put main.py
     ```
     請將 `/dev/ttyACM0` 替換為您的 Pico 連接埠

4. **測試程式**：
   - 程式碼上傳後，當按鈕按下時 LED 應亮起，放開時則熄滅。`time.sleep(0.05)` 會加入 50ms 延遲以消除按鈕彈跳並降低 CPU 負載

### 疑難排解
- **LED 未亮**：
  - 檢查 LED 極性（陽極接 GPIO 25，陰極經電阻接 GND）
  - 確認 GPIO 針腳（25）與程式碼及實體連接一致
  - 確保 LED 與電阻功能正常（可用三用電錶或其他電路測試）
- **按鈕無反應**：
  - 確認 GPIO 14 連接正確，且按鈕按下時會連接至 3.3V
  - 檢查 `Pin.PULL_DOWN` 設定是否合適；若按鈕接線方式不同（例如連接至 GND），需調整程式碼改用 `Pin.PULL_UP` 並反轉邏輯（`if not button.value()`）
- **程式碼無法執行**：
  - 確認 MicroPython 安裝正確
  - 檢查檔案是否以 `main.py` 名稱儲存於 Pico
  - 確認 USB 連接與 IDE 中的連接埠設定

### 注意事項
- 此程式碼假設按鈕按下時會將 GPIO 14 連接至 3.3V。若您的按鈕改為連接至 GND，請修改程式碼使用 `Pin.PULL_UP` 並反轉邏輯：
  ```python
  button = Pin(14, Pin.IN, Pin.PULL_UP)
  while True:
      if not button.value():  # 按鈕按下 = LOW
          led.on()
      else:
          led.off()
      time.sleep(0.05)
  ```
- 若遇到按鈕彈跳問題（LED 閃爍），可增加 `time.sleep` 數值或實作軟體消彈跳機制
- 對於 Pico W，設定方式完全相同，但請確保使用正確的 GPIO 針腳（針腳配置相同）

如需進一步說明或特定問題協助，請隨時告知！