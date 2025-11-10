---
audio: false
generated: true
lang: hant
layout: post
title: 透過UF2快閃Pico韌體
translated: true
type: note
---

要將韌體刷入您的 Raspberry Pi Pico（或基於 RP2040 的開發板）的 BOOTSEL 模式，只需將 `.uf2` 檔案複製到 `RPI-RP2` 磁碟機，請按照以下步驟操作：

### 逐步指南
1. **確認裝置處於 BOOTSEL 模式**：
   - 當裝置連接到電腦時，應顯示為名為 `RPI-RP2` 的 USB 磁碟機。這確認其處於 BOOTSEL 模式（如 `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot` 所示）。
   - 如果未處於 BOOTSEL 模式，請拔下裝置，按住 Pico 上的 BOOTSEL 按鈕，然後在按住按鈕的同時將其插入電腦的 USB 端口。幾秒後釋放按鈕。

2. **取得有效的 `.uf2` 檔案**：
   - **MicroPython**：從 [官方 MicroPython 網站](https://micropython.org/download/rp2-pico/) 下載適用於 Raspberry Pi Pico 的最新 MicroPython 韌體。選擇 Pico 或 Pico W 的 `.uf2` 檔案（例如 `rp2-pico-latest.uf2`）。
   - **CircuitPython**：從 [CircuitPython 網站](https://circuitpython.org/board/raspberry_pi_pico/) 下載適用於 Pico 或 Pico W 的 CircuitPython 韌體。
   - **自訂程式**：如果您已編寫程式（例如使用 Pico SDK 以 C/C++ 編寫），請編譯它以生成 `.uf2` 檔案。例如，使用 Pico SDK 或 Arduino IDE 來構建您的專案。
   - 將 `.uf2` 檔案儲存到電腦上易於存取的位置（例如桌面或下載資料夾）。

3. **定位 RPI-RP2 磁碟機**：
   - 在電腦上開啟檔案總管：
     - **Windows**：在「本機」下尋找 `RPI-RP2` 作為可移動磁碟機。
     - **macOS**：磁碟機應出現在桌面上或在 Finder 的「裝置」下。
     - **Linux**：在 `/media` 或 `/mnt` 下檢查，或使用 `lsblk` 列出連接的磁碟機。
   - 如果磁碟機未出現，請確保 USB 線支援數據傳輸（不僅供電），並嘗試不同的 USB 端口或線材。

4. **將 `.uf2` 檔案複製到 RPI-RP2 磁碟機**：
   - 將 `.uf2` 檔案拖放到 `RPI-RP2` 磁碟機上，或使用檔案總管複製並貼上。
   - 或者，使用終端指令（在 Linux/macOS 上）：
     ```bash
     cp /path/to/your/file.uf2 /media/your_username/RPI-RP2/
     ```
     將 `/path/to/your/file.uf2` 替換為您的 `.uf2` 檔案路徑，並根據需要調整掛載點。

5. **等待刷寫過程完成**：
   - 一旦 `.uf2` 檔案被複製，Raspberry Pi Pico 會自動刷寫韌體。`RPI-RP2` 磁碟機將在裝置重啟時消失（卸載），表示過程已完成。
   - 這通常需要幾秒鐘。在此期間請勿拔下裝置。

6. **驗證裝置**：
   - 刷寫後，Pico 應退出 BOOTSEL 模式並運行新韌體。
   - 對於 MicroPython 或 CircuitPython，使用終端（例如 PuTTY、screen 或 Thonny IDE）透過 USB 序列端口（例如 Windows 上的 `COM3` 或 Linux/macOS 上的 `/dev/ttyACM0`）連接到裝置。您應該會看到 Python REPL 提示符。
   - 對於自訂程式，檢查預期行為（例如 LED 閃爍、序列輸出等）。
   - 如果 `RPI-RP2` 磁碟機重新出現，則刷寫可能失敗。嘗試使用不同的 `.uf2` 檔案或檢查硬體問題（例如 USB 線、快閃記憶體晶片）。

### 疑難排解
- **磁碟機未顯示**：確保 Pico 處於 BOOTSEL 模式且 USB 線支援數據傳輸。嘗試按住 BOOTSEL，然後在連接時短按 RESET 按鈕（如果可用）。
- **複製失敗或磁碟機重新出現**：`.uf2` 檔案可能損壞，或快閃記憶體可能故障。下載新的 `.uf2` 檔案或使用最小檔案（如 MicroPython）進行測試。如果問題持續，使用 `picotool` 進行診斷：
  ```bash
  picotool info
  ```
  從 [Raspberry Pi Pico SDK](https://github.com/raspberrypi/picotool) 安裝 `picotool`。
- **刷寫後無回應**：如果使用 MicroPython/CircuitPython，請確保您的 IDE（例如 Thonny）設定為正確的序列端口。對於自訂程式，請驗證程式碼是否正確編譯。

### 範例：刷寫 MicroPython
1. 從 [micropython.org](https://micropython.org/download/rp2-pico/) 下載 MicroPython `.uf2` 檔案。
2. 按住 BOOTSEL，插入 Pico，然後釋放 BOOTSEL。
3. 開啟檔案總管，找到 `RPI-RP2` 磁碟機，並將 `.uf2` 檔案複製到其中。
4. 等待磁碟機消失。
5. 開啟 Thonny IDE，選擇 Pico 的序列端口，然後開始使用 MicroPython 編碼。

如果您需要有關特定 `.uf2` 檔案、工具或設定（例如安裝 `picotool` 或使用 Thonny）的幫助，請告訴我！