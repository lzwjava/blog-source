---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上設定 Raspberry Pi Pico
translated: true
type: note
---

要在 **Ubuntu** 上使用 **Raspberry Pi Pico**，您需要設定開發環境、安裝必要軟體，並配置工具來為 Pico 編程。Pico 支援使用 **MicroPython**、**C/C++** 或 **CircuitPython** 進行編程。以下我將概述每種方法的步驟和所需軟體，並聚焦於最常見的設定。

### 一般先決條件
- **Raspberry Pi Pico**（或 Pico W）及 USB 線（Pico 使用 Micro-USB，Pico 2 使用 USB-C）。
- **Ubuntu** 系統（例如 Ubuntu 20.04、22.04 或更新版本；這些說明假設使用較新版本如 24.04）。
- 對終端機有基本認識。

### 選項 1：使用 MicroPython 編程
MicroPython 是為 Pico 編程最適合初學者的方式。它是一個專為微控制器設計的輕量級 Python 實作。

#### 需安裝的軟體
1. **MicroPython 韌體**
   - 從 [官方 MicroPython 網站](https://micropython.org/download/rp2-pico/) 或 [Raspberry Pi Pico 頁面](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) 下載最新的 MicroPython UF2 韌體檔案。
   - 對於 Pico W 或 Pico 2，請確保選擇相應的韌體（例如，Pico W 使用 `rp2-pico-w`）。

2. **Python 3**
   - Ubuntu 通常預設包含 Python 3。請使用以下指令驗證：
     ```bash
     python3 --version
     ```
   - 如果未安裝，請安裝：
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

3. **Thonny IDE**（推薦給初學者）
   - Thonny 是一個用於以 MicroPython 為 Pico 編程的簡單 IDE。
   - 安裝 Thonny：
     ```bash
     sudo apt install thonny
     ```
   - 或者，使用 `pip` 安裝最新版本：
     ```bash
     pip3 install thonny
     ```

4. **可選：`picotool`（用於進階管理）**
   - 對於管理 MicroPython 韌體或檢查 Pico 很有用。
   - 安裝 `picotool`：
     ```bash
     sudo apt install picotool
     ```

#### 設定步驟
1. **安裝 MicroPython 韌體**
   - 在按住 **BOOTSEL** 按鈕的同時，透過 USB 將 Pico 連接到您的 Ubuntu 機器（這會使 Pico 進入 bootloader 模式）。
   - Pico 會顯示為一個 USB 儲存裝置（例如 `RPI-RP2`）。
   - 將下載的 MicroPython `.uf2` 檔案拖放到 Pico 的儲存空間中。Pico 將自動重新啟動並安裝好 MicroPython。

2. **配置 Thonny**
   - 開啟 Thonny：在終端機中輸入 `thonny` 或透過應用程式選單。
   - 前往 **Tools > Options > Interpreter**。
   - 選擇 **MicroPython (Raspberry Pi Pico)** 作為直譯器。
   - 選擇正確的連接埠（例如 `/dev/ttyACM0`）。如果需要，可以在終端機中執行 `ls /dev/tty*` 來識別連接埠。
   - Thonny 現在應該已連接到 Pico，允許您編寫和執行 Python 腳本。

3. **測試程式**
   - 在 Thonny 中，編寫一個簡單的腳本，例如：
     ```python
     from machine import Pin
     led = Pin(25, Pin.OUT)  # 板載 LED（Pico 使用 GP25）
     led.toggle()  # 切換 LED 開/關
     ```
   - 點擊 **Run** 按鈕以在 Pico 上執行程式碼。

4. **可選：使用 `picotool`**
   - 驗證 Pico 的狀態：
     ```bash
     picotool info
     ```
   - 確保 Pico 已連接，並在需要時處於 bootloader 模式。

### 選項 2：使用 C/C++ 編程
對於進階使用者，可以使用官方的 **Pico SDK** 以 C/C++ 為 Pico 編程。

#### 需安裝的軟體
1. **Pico SDK 和工具鏈**
   - 安裝建置 C/C++ 程式所需的工具：
     ```bash
     sudo apt update
     sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
     ```

2. **Pico SDK**
   - 複製 Pico SDK 儲存庫：
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-sdk.git
     cd pico-sdk
     git submodule update --init
     ```
   - 設定 `PICO_SDK_PATH` 環境變數：
     ```bash
     export PICO_SDK_PATH=~/pico-sdk
     echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
     ```

3. **可選：Pico 範例**
   - 複製 Pico 範例以供參考：
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-examples.git
     ```

4. **Visual Studio Code（可選）**
   - 為了獲得更好的開發體驗，安裝 VS Code：
     ```bash
     sudo snap install code --classic
     ```
   - 在 VS Code 中安裝 **CMake Tools** 和 **C/C++** 擴充功能。

#### 設定步驟
1. **設定專案**
   - 為您的專案建立一個新目錄，例如 `my-pico-project`。
   - 從 `pico-examples` 複製一個範例 `CMakeLists.txt` 或建立一個：
     ```cmake
     cmake_minimum_required(VERSION 3.13)
     include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
     project(my_project C CXX ASM)
     pico_sdk_init()
     add_executable(my_project main.c)
     pico_add_extra_outputs(my_project)
     target_link_libraries(my_project pico_stdlib)
     ```
   - 編寫一個簡單的 C 程式（例如 `main.c`）：
     ```c
     #include "pico/stdlib.h"
     int main() {
         const uint LED_PIN = 25;
         gpio_init(LED_PIN);
         gpio_set_dir(LED_PIN, GPIO_OUT);
         while (true) {
             gpio_put(LED_PIN, 1);
             sleep_ms(500);
             gpio_put(LED_PIN, 0);
             sleep_ms(500);
         }
     }
     ```

2. **建置和燒錄**
   - 導航到您的專案目錄：
     ```bash
     cd my-pico-project
     mkdir build && cd build
     cmake ..
     make
     ```
   - 這會產生一個 `.uf2` 檔案（例如 `my_project.uf2`）。
   - 按住 Pico 上的 **BOOTSEL** 按鈕，透過 USB 連接它，並將 `.uf2` 檔案複製到 Pico 的儲存空間：
     ```bash
     cp my_project.uf2 /media/$USER/RPI-RP2/
     ```

3. **除錯（可選）**
   - 安裝 `openocd` 進行除錯：
     ```bash
     sudo apt install openocd
     ```
   - 使用除錯器（例如另一個 Pico 作為除錯探針）並執行：
     ```bash
     openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
     ```

### 選項 3：使用 CircuitPython 編程
CircuitPython 是另一個基於 Python 的選項，類似於 MicroPython，但更專注於 Adafruit 的生態系統。

#### 需安裝的軟體
1. **CircuitPython 韌體**
   - 從 [Adafruit CircuitPython 網站](https://circuitpython.org/board/raspberry_pi_pico/) 下載適用於 Pico 的 CircuitPython UF2 檔案。
   - 對於 Pico W 或 Pico 2，請選擇相應的韌體。

2. **Python 3 和工具**
   - 與 MicroPython 相同（Python 3、Thonny 等）。

#### 設定步驟
1. **安裝 CircuitPython 韌體**
   - 與 MicroPython 類似：按住 **BOOTSEL**，連接 Pico，並將 CircuitPython `.uf2` 檔案複製到 Pico 的儲存空間。
   - Pico 將重新啟動為一個名為 `CIRCUITPY` 的 USB 磁碟機。

2. **使用 Thonny 或文字編輯器編程**
   - 如 MicroPython 部分所述使用 Thonny，選擇 **CircuitPython** 作為直譯器。
   - 或者，使用任何文字編輯器直接在 `CIRCUITPY` 磁碟機上編輯 `code.py`。
   - 範例 `code.py`：
     ```python
     import board
     import digitalio
     import time
     led = digitalio.DigitalInOut(board.LED)
     led.direction = digitalio.Direction.OUTPUT
     while True:
         led.value = True
         time.sleep(0.5)
         led.value = False
         time.sleep(0.5)
     ```

### 補充說明
- **權限**：如果無法存取 Pico 的連接埠（例如 `/dev/ttyACM0`），請將您的使用者加入 `dialout` 群組：
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  登出並重新登入以套用變更。

- **Pico W 注意事項**：對於 Pico W，請確保使用其專用韌體（例如具有 Wi-Fi 支援的 MicroPython）。Wi-Fi 編程需要額外的函式庫，例如 MicroPython 的 `network`。

- **Pico 2**：較新的 Raspberry Pi Pico 2（使用 RP2350）可能需要更新的韌體或 SDK 版本。請查閱官方 Raspberry Pi 文件以了解相容性。

- **疑難排解**：
  - 如果 Pico 未出現在 bootloader 模式，請再次檢查 USB 線（必須支援數據傳輸，而不僅是供電）。
  - 執行 `lsusb` 或 `dmesg` 以確認 Ubuntu 已偵測到 Pico。
  - 對於 C/C++ 建置，請確保 Pico SDK 路徑設定正確。

### 推薦方法
- 對於**初學者**：使用 **MicroPython 與 Thonny**，因為設定簡單快速。
- 對於**進階使用者**：使用 **C/C++ 與 Pico SDK**，以獲得效能和低階控制。
- 對於**Adafruit 生態系統使用者**：如果您計劃使用 Adafruit 函式庫或硬體，請使用 **CircuitPython**。

如果您有特定的專案或編程偏好，請告訴我，我可以進一步調整說明！