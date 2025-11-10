---
audio: false
generated: true
lang: hant
layout: post
title: 上載 MicroPython 至 Pico
translated: true
type: note
---

在將 MicroPython 刷入您的 Raspberry Pi Pico（使用前述的 `.uf2` 檔案方法）後，您可以使用像 Thonny IDE 這樣的工具上傳並執行簡單的 MicroPython 程式。Thonny IDE 對初學者友好，且廣泛用於 MicroPython 開發。以下是設定 MicroPython 並上傳簡單程式到 Pico 的步驟。

---

### 先決條件
1. **已刷入 MicroPython**：您已將 `RPI_PICO-20250415-v1.25.0.uf2` 複製到 `RPI-RP2` 磁碟機，且 Pico 已重新啟動（`RPI-RP2` 磁碟機應不再顯示）。
2. **USB 連接**：Pico 透過支援資料傳輸的 USB 線連接到您的電腦。
3. **Thonny IDE**：如果尚未安裝，請安裝 Thonny：
   - **Linux**：使用套件管理員安裝 Thonny，或從 [thonny.org](https://thonny.org) 下載。
     ```bash
     sudo apt update
     sudo apt install thonny
     ```
   - 或者，使用 `pip`：
     ```bash
     pip install thonny
     ```
   - 對於 Windows/macOS，請從 [thonny.org](https://thonny.org) 下載並安裝。

---

### 上傳簡單 MicroPython 程式的逐步指南

1. **連接 Pico 並開啟 Thonny**：
   - 將 Pico 插入電腦的 USB 埠。
   - 開啟 Thonny IDE。

2. **為 MicroPython 配置 Thonny**：
   - 在 Thonny 中，前往 **Tools > Options > Interpreter**（或 **Run > Select interpreter**）。
   - 從解譯器下拉選單中選擇 **MicroPython (Raspberry Pi Pico)**。
   - 如果 Pico 的序列埠（例如在 Linux 上為 `/dev/ttyACM0`）未自動出現：
     - 在下拉選單中檢查可用埠，或在終端機中執行 `ls /dev/tty*` 以識別 Pico 的埠（通常是 `/dev/ttyACM0` 或類似）。
     - 手動選擇正確的埠。
   - 點擊 **OK** 儲存。

3. **驗證 MicroPython 正在執行**：
   - 在 Thonny 的 **Shell**（底部面板）中，您應該會看到 MicroPython REPL 提示符，例如：
     ```
     >>> 
     ```
   - 透過輸入簡單指令測試，例如：
     ```python
     print("Hello, Pico!")
     ```
     按 Enter，您應該會在 Shell 中看到輸出。

4. **撰寫簡單的 MicroPython 程式**：
   - 在 Thonny 的主編輯器中，建立新檔案並撰寫簡單程式。例如，一個讓 Pico 板載 LED 閃爍的程式（Pico 使用 GPIO 25，Pico W 使用 "LED"）：
     ```python
     from machine import Pin
     import time

     # 初始化板載 LED
     led = Pin(25, Pin.OUT)  # Pico W 請使用 "LED" 代替 25

     # 閃爍 LED
     while True:
         led.on()           # 開啟 LED
         time.sleep(0.5)    # 等待 0.5 秒
         led.off()          # 關閉 LED
         time.sleep(0.5)    # 等待 0.5 秒
     ```
   - 注意：如果使用 Pico W，請將 `Pin(25, Pin.OUT)` 替換為 `Pin("LED", Pin.OUT)`。

5. **將程式儲存到 Pico**：
   - 點擊 **File > Save As**。
   - 在對話框中，選擇 **Raspberry Pi Pico** 作為目的地（不是您的電腦）。
   - 將檔案命名為 `main.py`（MicroPython 在啟動時會自動執行 `main.py`）或其他名稱如 `blink.py`。
   - 點擊 **OK** 將檔案儲存到 Pico 的檔案系統。

6. **執行程式**：
   - 在 Thonny 中點擊綠色的 **Run** 按鈕（或按 **F5**）來執行程式。
   - 或者，如果您將其儲存為 `main.py`，重置 Pico（拔插 USB 線，或按 RESET 按鈕（如果可用）），程式將自動執行。
   - 您應該會看到板載 LED 每 0.5 秒閃爍一次。

7. **停止程式**（如果需要）：
   - 要停止程式，在 Thonny 的 Shell 中按 **Ctrl+C** 以中斷正在執行的腳本。
   - 要移除自動執行的 `main.py`，請從 Pico 中刪除它：
     - 在 Thonny 中，前往 **View > Files**，選擇 Pico 的檔案系統，右鍵點擊 `main.py`，然後選擇 **Delete**。

---

### 測試與疑難排解
- **沒有 REPL 提示符**：如果 Thonny 沒有顯示 MicroPython REPL：
  - 確保在解譯器設定中選擇了正確的埠。
  - 驗證 MicroPython 是否已正確刷入。如果沒有，請按照先前描述重新刷入 `.uf2` 檔案。
  - 檢查 USB 線（必須支援資料傳輸）並嘗試不同的埠。
- **LED 不閃爍**：確保使用了正確的 GPIO 引腳（Pico 為 `25`，Pico W 為 `"LED"`）。如果仍然無法工作，請使用簡單的 REPL 指令測試 LED：
  ```python
  from machine import Pin
  led = Pin(25, Pin.OUT)
  led.on()
  ```
- **檔案無法儲存**：確保 Thonny 已連接到 Pico 且解譯器設定為 MicroPython (Raspberry Pi Pico)。

---

### 其他提示
- **使用其他工具**：除了 Thonny，您可以使用 `rshell` 或 `ampy` 來管理 Pico 上的檔案：
  ```bash
  pip install rshell
  rshell --port /dev/ttyACM0
  cp blink.py /pyboard/main.py
  ```
- **更多範例程式**：
  - 讀取按鈕按下（例如在 GPIO 14 上）：
    ```python
    from machine import Pin
    button = Pin(14, Pin.IN, Pin.PULL_UP)
    while True:
        print(button.value())
    ```
  - 透過調整 GPIO 引腳編號來控制外部 LED 或其他周邊裝置。
- **自動執行**：將檔案儲存為 `main.py` 會使其在啟動時自動執行。使用 `boot.py` 用於在 `main.py` 之前執行的設定程式碼。

如果您遇到特定問題（例如埠檢測、Thonny 中的錯誤或硬體問題），或想嘗試不同的程式，請告訴我，我將進一步指導您！