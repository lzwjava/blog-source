---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上檢測樹莓派 Pico
translated: true
type: note
---

要檢查 Raspberry Pi Pico 插入後是否被 Ubuntu 偵測到，請按照以下步驟操作：

1. **檢查 USB 裝置**：
   - 開啟終端機並執行：
     ```bash
     lsusb
     ```
   - 尋找類似 `Raspberry Pi Pico` 的條目，或供應商 ID 為 `2E8A` 的裝置（Raspberry Pi 的供應商 ID）。例如：
     ```
     Bus XXX Device XXX: ID 2e8a:0003 Raspberry Pi Pico
     ```

2. **檢查序列埠**：
   - 如果 Pico 處於 BOOTSEL 模式（用於燒錄韌體）或正在執行具有序列輸出的 MicroPython/Arduino 程式，請檢查序列埠：
     ```bash
     ls /dev/tty*
     ```
   - 尋找類似 `/dev/ttyACM0` 或 `/dev/ttyUSB0` 的裝置。執行 MicroPython 時，Pico 通常會顯示為 `/dev/ttyACM0`。

3. **檢查磁碟裝置（BOOTSEL 模式）**：
   - 如果 Pico 處於 BOOTSEL 模式（插入時按住 BOOTSEL 按鈕），它應該會顯示為大容量儲存裝置。執行：
     ```bash
     lsblk
     ```
   - 尋找類似 `/dev/sdb`（或類似名稱）且帶有掛載點的裝置，通常標記為 `RPI-RP2`。

4. **使用 `dmesg` 查看核心日誌**：
   - 執行：
     ```bash
     dmesg | tail -n 20
     ```
   - 檢查是否出現偵測到 Pico 的訊息，例如：
     ```
     [1234.567890] usb 1-1: New USB device found, idVendor=2e8a, idProduct=0003
     [1234.567891] usb 1-1: Product: Pico
     [1234.567892] cdc_acm 1-1:1.0: ttyACM0: USB ACM device
     ```
   - 這確認了 Pico 已被識別並分配了埠號（例如 `ttyACM0`）。

5. **使用 MicroPython 測試（如已安裝）**：
   - 如果你使用 MicroPython，請安裝 `picocom` 或 `minicom` 等工具：
     ```bash
     sudo apt install picocom
     ```
   - 連接到 Pico 的序列埠：
     ```bash
     picocom /dev/ttyACM0
     ```
   - 如果偵測成功，你應該會看到 MicroPython REPL 提示符號（>>>）。按 `Ctrl+C` 即可退出。

**注意事項**：
- 請確保 Pico 透過優質的 USB 傳輸線正確連接（需支援資料傳輸，而非僅供電）。
- 若處於 BOOTSEL 模式，Pico 會顯示為儲存裝置，而非序列裝置。
- 如果無法偵測，請嘗試更換 USB 埠、傳輸線，或檢查驅動程式（例如序列通訊用的 `cdc_acm`）是否已載入：
  ```bash
  lsmod | grep cdc_acm
  ```

如果在以上檢查中均未發現 Pico，請提供更多詳細資訊（例如 Pico 的模式、你嘗試執行的操作），我將協助進一步排查問題！