---
audio: false
generated: true
lang: hant
layout: post
title: 樹莓派 Pico 處於 BOOTSEL 模式
translated: true
type: note
---

裝置列表中顯示的 `Bus 001 Device 009: ID 2e8a:0003 Raspberry Pi RP2 Boot` 是處於 BOOTSEL 模式的 Raspberry Pi Pico（或類似的 RP2040 開發板）。以下為詳細說明：

- **ID 2e8a:0003**：這是 Raspberry Pi 為 RP2040 微控制器在 BOOTSEL 模式下分配的 USB 供應商 ID (2e8a) 和產品 ID (0003)。
- **Raspberry Pi RP2 Boot**：表示該裝置是 Raspberry Pi Pico（或其他基於 RP2040 的開發板，如 Pico W 或自訂開發板）已進入其 bootloader 模式。在此模式下，裝置會顯示為 USB 大容量儲存裝置，讓您可以透過將韌體檔案（例如 .uf2 檔案）複製到磁碟機來上傳。

### 什麼是 BOOTSEL 模式？
BOOTSEL 模式是透過在將 Raspberry Pi Pico 插入 USB 連接埠時按住 BOOTSEL 按鈕，或在按住按鈕的同時重設裝置來啟動的。此模式用於將新韌體或程式燒錄到 RP2040 微控制器上。在此模式下，Pico 會在電腦上顯示為可卸除式磁碟機（名為 `RPI-RP2`）。

### 為什麼會顯示這個狀態？
您的裝置可能處於 BOOTSEL 模式的原因如下：
1. 您刻意按下 BOOTSEL 按鈕以更新或燒錄韌體。
2. 裝置未執行程式，並預設進入 bootloader 模式（例如，在燒錄失敗或重設後）。
3. 可能因韌體或連接問題導致裝置持續處於 bootloader 模式。例如，快閃記憶體問題或燒錄不當可能導致裝置還原至此模式。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)

### 接下來該怎麼做？
- **如果您想燒錄韌體**：將有效的 `.uf2` 檔案（例如 MicroPython 或 CircuitPython 韌體，或已編譯的程式）複製到 `RPI-RP2` 磁碟機。裝置會自動燒錄韌體並重新啟動，退出 BOOTSEL 模式。[](https://forum.arduino.cc/t/solved-nano-rp2040-connect-does-not-accept-uf2/888152)
- **如果裝置卡在 BOOTSEL 模式**：這可能表示快閃記憶體或韌體出現問題。請嘗試：
  1. 重新燒錄已知可正常運作的 `.uf2` 檔案，例如從 Raspberry Pi 官方網站下載的 MicroPython 韌體。
  2. 檢查 USB 線和連接埠，因為故障的傳輸線可能導致問題。[](https://raspberrypi.stackexchange.com/questions/139506/raspberry-pi-pico-doesnt-create-tty-file)
  3. 使用如 `picotool` 等工具來驗證裝置狀態或重設裝置。例如，執行 `picotool info` 來檢查裝置狀態。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)
  4. 如果使用自訂的 RP2040 開發板，請確保快閃晶片已正確連接和配置，因為 QSPI 訊號或快閃 IC 的問題可能導致燒錄失敗。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)
- **如果您想退出 BOOTSEL 模式**：如果已燒錄有效的韌體，請拔下裝置，確保 BOOTSEL 按鈕未被按下，然後重新插入。裝置應啟動至其程式設計模式（例如執行 MicroPython 腳本或 C 程式）。

### 補充說明
- RP2040 是用於 Raspberry Pi Pico、Pico W 和其他開發板的微控制器。`RP2 Boot` 標識特指 RP2040 晶片的 bootloader 模式。[](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- 如果您使用的是 Raspberry Pi Pico W，請注意它具備無線功能，但這些功能在 BOOTSEL 模式下並未啟動。[](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)
- 如果您遇到錯誤（例如 `picotool` 驗證或載入失敗），可能是由於硬體問題（例如自訂開發板上的快閃晶片故障或焊接問題）或損毀的韌體檔案所致。[](https://forums.raspberrypi.com/viewtopic.php?p=2078375)

如果您需要特定協助（例如燒錄韌體、疑難排解或識別確切開發板型號），請提供更多關於您的設定或目標的詳細資訊！