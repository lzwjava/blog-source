---
audio: false
generated: true
lang: hant
layout: post
title: 樹莓派 Pico MicroPython 版 VSCode
translated: true
type: note
---

是的，你可以使用 Visual Studio Code（VSCode）來編寫、上傳並在 Raspberry Pi Pico 上運行 MicroPython 程式，就像使用 Thonny 一樣。VSCode 是一款功能強大的編輯器，透過合適的擴充功能和工具，它能有效處理 MicroPython 開發。以下是一步一步的指南，幫助你在 VSCode 中設定環境，將簡單的 MicroPython 程式上傳到 Pico，假設 MicroPython 已經刷入（正如你使用 `.uf2` 檔案所完成的）。

---

### 先決條件
1. **已刷入 MicroPython**：你的 Pico 已安裝 MicroPython（例如從 `RPI_PICO-20250415-v1.25.0.uf2` 檔案）。
2. **已安裝 VSCode**：如果尚未安裝，請從 [code.visualstudio.com](https://code.visualstudio.com) 下載並安裝 VSCode。
3. **已安裝 Python**：透過以下指令安裝 Python（MicroPython 工具所需）：
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
4. **USB 連接**：Pico 透過支援數據傳輸的 USB 線連接到你的電腦。

---

### 使用 VSCode 在 Raspberry Pi Pico 上開發 MicroPython 的逐步指南

1. **安裝必要的 VSCode 擴充功能**：
   - 開啟 VSCode。
   - 前往擴充功能檢視（`Ctrl+Shift+X` 或 macOS 上的 `Cmd+Shift+X`）。
   - 安裝以下擴充功能：
     - **Python**（由 Microsoft 提供）：用於 Python 和 MicroPython 的語法突顯和 IntelliSense。
     - **Pico-W-Go**（可選但推薦）：專為 Raspberry Pi Pico 的 MicroPython 開發設計的擴充功能。搜尋 “Pico-W-Go” 並安裝。
       - 注意：Pico-W-Go 簡化了檔案傳輸和 REPL 存取，但需要額外設定（如下所述）。
     - 或者，如果你偏好手動控制，可以使用通用擴充功能如 **Remote-SSH** 或 **Serial Monitor**。

2. **設定 Pico-W-Go（推薦）**：
   - **安裝依賴項**：Pico-W-Go 需要 `pyserial` 和 `esptool`。透過 pip 安裝：
     ```bash
     pip3 install pyserial esptool
     ```
   - **設定 Pico-W-Go**：
     - 開啟 VSCode 的命令選擇區（`Ctrl+Shift+P` 或 `Cmd+Shift+P`）。
     - 輸入並選擇 **Pico-W-Go > Configure Project**。
     - 按照提示設定你的專案：
       - 選擇 Pico 的序列埠（例如 `/dev/ttyACM0`）。在終端機中執行 `ls /dev/tty*` 來尋找。
       - 選擇 MicroPython 作為直譯器。
       - 建立新的專案資料夾或使用現有的。
     - Pico-W-Go 會建立一個包含 `.picowgo` 設定檔的工作區。

3. **編寫簡單的 MicroPython 程式**：
   - 在 VSCode 中，於你的專案資料夾建立新檔案（例如 `main.py`）。
   - 編寫一個簡單的程式，例如閃爍板載 LED：
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)  # Pico W 使用 "LED"
     while True:
         led.on()
         time.sleep(0.5)
         led.off()
         time.sleep(0.5)
     ```
   - 儲存檔案（`Ctrl+S` 或 `Cmd+S`）。

4. **將程式上傳到 Pico**：
   - **使用 Pico-W-Go**：
     - 確保 Pico 已連接且選擇了正確的埠（如有需要，在 `Pico-W-Go > Configure Project` 中檢查）。
     - 開啟命令選擇區（`Ctrl+Shift+P`）。
     - 選擇 **Pico-W-Go > Upload Project to Pico**。
     - 這會將你專案資料夾中的所有檔案（例如 `main.py`）上傳到 Pico 的檔案系統。
     - 如果你將檔案命名為 `main.py`，它會在啟動時自動運行。
   - **使用 `rshell` 手動上傳**（如果不使用 Pico-W-Go）：
     - 安裝 `rshell`：
       ```bash
       pip3 install rshell
       ```
     - 連接到 Pico：
       ```bash
       rshell --port /dev/ttyACM0
       ```
     - 複製檔案到 Pico：
       ```bash
       cp main.py /pyboard/main.py
       ```
     - 使用 `exit` 離開 `rshell`。

5. **運行和測試程式**：
   - **使用 Pico-W-Go**：
     - 開啟命令選擇區並選擇 **Pico-W-Go > Run**。
     - 這會執行當前檔案或開啟 REPL 進行手動指令操作。
     - 如果使用上述範例，你應該會看到 LED 閃爍。
   - **使用 VSCode 的終端機或 REPL**：
     - 使用 Pico-W-Go 開啟 REPL（`Pico-W-Go > Open REPL`）或使用 `rshell`：
       ```bash
       rshell --port /dev/ttyACM0 repl
       ```
     - 直接測試指令，例如：
       ```python
       from machine import Pin
       led = Pin(25, Pin.OUT)
       led.on()
       ```
     - 在 REPL 中按 `Ctrl+C` 停止正在運行的程式。
   - 如果檔案是 `main.py`，重置 Pico（拔插 USB 線或按下 RESET 按鈕）以自動運行它。

6. **除錯和管理檔案**：
   - **Pico-W-Go**：使用 **Pico-W-Go > Download Project from Pico** 從 Pico 下載檔案，或使用 **Pico-W-Go > Delete All Files** 清除檔案系統。
   - **rshell**：使用以下指令列出檔案：
     ```bash
     rshell ls /pyboard
     ```
     使用以下指令刪除檔案：
     ```bash
     rshell rm /pyboard/main.py
     ```
   - 在 VSCode 終端機或 REPL 中檢查程式輸出。

---

### 替代方案：不使用 Pico-W-Go 的手動工作流程
如果你偏好不使用 Pico-W-Go，可以手動管理 MicroPython 開發：
1. 在 VSCode 中編寫程式碼並儲存為 `main.py`。
2. 使用 `ampy`（另一個 MicroPython 工具）上傳：
   ```bash
   pip3 install adafruit-ampy
   ampy --port /dev/ttyACM0 put main.py
   ```
3. 使用終端機工具如 `minicom` 或 `screen` 存取 REPL：
   ```bash
   screen /dev/ttyACM0 115200
   ```
   按 `Ctrl+C` 停止正在運行的程式並進入 REPL。

---

### 疑難排解
- **找不到埠**：執行 `ls /dev/tty*` 來確認 Pico 的埠（例如 `/dev/ttyACM0`）。確保 Pico 已連接且 MicroPython 已刷入。
- **Pico-W-Go 錯誤**：檢查 `pyserial` 和 `esptool` 是否已安裝且選擇了正確的埠。如有需要，重新啟動 VSCode。
- **程式未運行**：確保檔案儲存為 `main.py` 以自動執行，或透過 REPL 或 `ampy run main.py` 手動運行。
- **LED 未閃爍**：確認 GPIO 引腳（Pico 為 `25`，Pico W 為 `"LED"`）。在 REPL 中測試：
  ```python
  from machine import Pin
  led = Pin(25, Pin.OUT)
  led.on()
  ```

---

### VSCode 相對於 Thonny 的優勢
- 更好的程式碼編輯功能（例如 IntelliSense、Git 整合、可自訂的工作流程）。
- 支援具有多個檔案的大型專案。
- Pico-W-Go 提供了類似 Thonny 的體驗，但具備 VSCode 的強大功能。

### 限制
- 設定比 Thonny 稍微複雜。
- REPL 整合可能不如 Thonny 的一體化界面無縫。

如果你需要有關特定 VSCode 設定、安裝工具或編寫更複雜的 MicroPython 程式的幫助，請告訴我！