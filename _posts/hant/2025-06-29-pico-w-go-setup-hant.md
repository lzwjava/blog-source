---
audio: false
generated: true
lang: hant
layout: post
title: VSCode Pico-W-Go 用於 MicroPython
translated: true
type: note
---

在 Visual Studio Code (VSCode) 中使用 **Raspberry Pi Pico** 擴充功能，是在您的 Raspberry Pi Pico 上進行 MicroPython 開發的絕佳選擇，因為它在 VSCode 強大的編輯環境中提供了類似 Thonny 的簡化工作流程。您可能指的是 **Pico-W-Go**（或類似的擴充功能如 **Pico-Go**），這是專為使用 MicroPython 開發 Raspberry Pi Pico 和 Pico W 而設計的。以下，我將指導您設定和使用 **Pico-W-Go** 擴充功能（最受歡迎且持續維護的選項），將一個簡單的 MicroPython 程式上傳到您的 Pico，假設 MicroPython 已經刷入（使用您已使用的 `RPI_PICO-20250415-v1.25.0.uf2` 檔案）。

---

### 先決條件
1.  **已刷入 MicroPython**：您的 Pico 已安裝 MicroPython，正如您已刷入。
2.  **已安裝 VSCode**：確保已安裝 VSCode ([code.visualstudio.com](https://code.visualstudio.com))。
3.  **已安裝 Python**：Pico-W-Go 相依項目所需：
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
4.  **USB 連接**：Pico 透過支援資料傳輸的 USB 線連接。

---

### 在 VSCode 中使用 Raspberry Pi Pico (Pico-W-Go) 擴充功能的逐步指南

1.  **安裝 Pico-W-Go 擴充功能**：
    *   開啟 VSCode。
    *   前往擴充功能檢視 (`Ctrl+Shift+X` 或 macOS 上的 `Cmd+Shift+X`)。
    *   搜尋 **Pico-W-Go** 並安裝它（由 Paul Obermeier 等人開發）。
    *   注意：如果您指的是其他擴充功能（例如 Pico-Go），請告知我，但 Pico-W-Go 是 Pico MicroPython 開發最常用的。

2.  **安裝 Pico-W-Go 相依項目**：
    *   Pico-W-Go 需要 `pyserial` 和 `esptool` 來進行序列通訊和刷入：
      ```bash
      pip3 install pyserial esptool
      ```
    *   確保這些套件已安裝在您的 Python 環境中（使用 `pip3 list` 驗證）。

3.  **設定 Pico-W-Go**：
    *   在 VSCode 中開啟命令選擇區 (`Ctrl+Shift+P` 或 `Cmd+Shift+P`)。
    *   輸入並選擇 **Pico-W-Go > Configure Project**。
    *   依照提示操作：
        *   **序列埠**：選擇 Pico 的埠（例如 `/dev/ttyACM0`）。透過執行以下指令尋找：
          ```bash
          ls /dev/tty*
          ```
          尋找 `/dev/ttyACM0` 或類似的名稱，當 Pico 連接時會出現。
        *   **直譯器**：選擇 MicroPython (Raspberry Pi Pico)。
        *   **專案資料夾**：選擇或建立一個專案資料夾（例如 `~/PicoProjects/MyProject`）。
    *   Pico-W-Go 會在您的專案資料夾中建立一個 `.picowgo` 設定檔來儲存設定。

4.  **撰寫簡單的 MicroPython 程式**：
    *   在 VSCode 中，開啟您的專案資料夾（檔案 > 開啟資料夾）。
    *   建立一個名為 `main.py` 的新檔案（MicroPython 在啟動時會自動執行 `main.py`）。
    *   加入一個簡單的程式，例如讓板載 LED 閃爍：
      ```python
      from machine import Pin
      import time

      led = Pin(25, Pin.OUT)  # 對於 Pico W，使用 "LED"
      while True:
          led.on()
          time.sleep(0.5)
          led.off()
          time.sleep(0.5)
      ```
    *   儲存檔案 (`Ctrl+S`)。

5.  **將程式上傳到 Pico**：
    *   確保 Pico 已連接且選擇了正確的埠（如果需要，請重新執行 **Pico-W-Go > Configure Project**）。
    *   開啟命令選擇區 (`Ctrl+Shift+P`)。
    *   選擇 **Pico-W-Go > Upload Project to Pico**。
        *   這會將您專案資料夾中的所有檔案（例如 `main.py`）上傳到 Pico 的檔案系統。
    *   或者，要上傳單一檔案：
        *   在 VSCode 檔案總管中對 `main.py` 按右鍵。
        *   選擇 **Pico-W-Go > Upload File to Pico**。
    *   檔案會傳輸到 Pico，如果是 `main.py`，它將在啟動時自動執行。

6.  **執行和測試程式**：
    *   **自動執行**：如果您上傳了 `main.py`，重置 Pico（拔插 USB 線，或按下可用的 RESET 按鈕）。LED 應該開始閃爍。
    *   **手動執行**：
        *   開啟命令選擇區並選擇 **Pico-W-Go > Run**。
        *   這會在 Pico 上執行當前檔案。
    *   **使用 REPL**：
        *   開啟命令選擇區並選擇 **Pico-W-Go > Open REPL**。
        *   REPL 會出現在 VSCode 的終端機中，您可以在那裡測試指令：
          ```python
          from machine import Pin
          led = Pin(25, Pin.OUT)
          led.on()
          ```
        *   在 REPL 中按 `Ctrl+C` 可以停止正在執行的程式。

7.  **管理 Pico 上的檔案**：
    *   **列出檔案**：使用 **Pico-W-Go > Download Project from Pico** 來檢視或從 Pico 的檔案系統檢索檔案。
    *   **刪除檔案**：開啟命令選擇區並選擇 **Pico-W-Go > Delete All Files** 來清除 Pico 的檔案系統，或使用 REPL：
      ```python
      import os
      os.remove('main.py')
      ```
    *   **檢查輸出**：程式輸出（例如 `print` 陳述式）會出現在 REPL 或 VSCode 的終端機中（如果已設定）。

---

### 疑難排解
*   **未偵測到埠**：
    *   執行 `ls /dev/tty*` 來確認 Pico 的埠（例如 `/dev/ttyACM0`）。
    *   確保 USB 線支援資料傳輸，並嘗試不同的埠。
    *   在 **Pico-W-Go > Configure Project** 中重新設定埠。
*   **上傳失敗**：
    *   驗證 `pyserial` 和 `esptool` 是否已安裝 (`pip3 list`)。
    *   檢查 MicroPython 是否正在執行（應該可以存取 REPL）。
    *   如果需要，透過重新進入 BOOTSEL 模式並複製 `.uf2` 檔案來重新刷入 MicroPython。
*   **LED 不閃爍**：
    *   確認正確的 GPIO 引腳（Pico 為 `25`，Pico W 為 `"LED"`）。
    *   在 REPL 中測試：
      ```python
      from machine import Pin
      led = Pin(25, Pin.OUT)
      led.on()
      ```
*   **缺少 Pico-W-Go 指令**：確保擴充功能已安裝並啟用。如果需要，請重新啟動 VSCode。

---

### 在 VSCode 中使用 Pico-W-Go 的優點
*   **整合的工作流程**：在 VSCode 中結合了程式碼編輯、檔案管理和 REPL 存取。
*   **進階功能**：利用 VSCode 的 Git 整合、擴充功能和自訂選項。
*   **跨平台**：可在 Linux、Windows 和 macOS 上運作。

### 與 Thonny 相比的限制
*   設定稍微複雜一些（例如安裝 `pyserial`、設定埠）。
*   REPL 整合可能不如 Thonny 的一體化介面無縫。
*   對於初次使用 MicroPython 的使用者來說，較不友善。

---

### 替代擴充功能
如果您指的是其他擴充功能（例如 **Pico-Go**），請注意 Pico-Go 是 Pico-W-Go 的舊版替代方案，可能功能較少或更新較少。設定方式類似，但推薦使用 Pico-W-Go，因為它積極開發且同時支援 Pico 和 Pico W。如果您使用的是其他特定擴充功能，請說明，我可以調整指示。

---

### 範例工作流程
1.  安裝 Pico-W-Go 和相依項目。
2.  使用正確的序列埠 (`/dev/ttyACM0`) 設定專案。
3.  撰寫並儲存帶有 LED 閃爍程式碼的 `main.py`。
4.  使用 **Pico-W-Go > Upload Project to Pico** 上傳。
5.  重置 Pico 或使用 **Pico-W-Go > Run** 來查看 LED 閃爍。
6.  使用 REPL 進行互動式測試或除錯。

如果您需要有關特定 Pico-W-Go 指令、其他程式範例或疑難排解（例如埠問題、擴充功能錯誤）的協助，請告知我！