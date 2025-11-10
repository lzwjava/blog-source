---
audio: false
generated: true
lang: hant
layout: post
title: Ubuntu 系統下樹莓派Pico的USB連接線指南
translated: true
type: note
---

針對您從 **Raspberry Pi Foundation** 購入的 **Raspberry Pi Pico（帶排針版本）**（假設「duistou」是筆誤或經銷商品牌），您需要合適的 USB 線材才能在 Ubuntu 系統上進行設定。以下是所需資訊：

### USB 線材需求
1. **類型**：USB 轉 Micro-USB 連接線
   - 原版帶排針的 Raspberry Pi Pico 使用 **Micro-USB** 埠進行供電與資料傳輸
   - 請確認線材支援**資料傳輸**功能，而非僅供充電。部分廉價 Micro-USB 線僅支援充電，無法用於程式燒錄或通訊

2. **線材規格**：
   - **接頭**：USB-A（或依電腦埠口使用 USB-C）轉 Micro-USB
   - **品質**：建議使用高品質線材以避免連線問題，可選用知名品牌（如 Anker、Belkin）或隨手機/平板附贈的原廠線材
   - **長度**：建議使用 1-3 英呎（30-100 公分）線材以減少訊號衰減

3. **電腦埠口**：
   - 若您的 Ubuntu 裝置配備 **USB-A 埠口**，請使用 USB-A 轉 Micro-USB 線材
   - 若僅有 **USB-C 埠口**，請使用 USB-C 轉 Micro-USB 線材，或透過 USB-C 集線器/轉接器搭配 USB-A 轉 Micro-USB 線材

### 設定注意事項
- **連接方式**：將 Micro-USB 端插入 Pico 的 Micro-USB 埠，另一端連接至 Ubuntu 電腦
- **模式切換**：
  - **正常模式**：直接插入 Pico 即可進行程式開發（如 MicroPython、C/C++）
  - **BOOTSEL 模式**：插入時長按 **BOOTSEL** 按鍵進入儲存裝置模式，用於韌體更新（將顯示為 `RPI-RP2` 磁碟）
- **驗證連線**：連接後請參照我先前的回覆步驟，確認 Ubuntu 是否能偵測到 Pico（例如使用 `lsusb`、`ls /dev/tty*` 或 `lsblk` 指令）

### 線材故障排除
- 若無法偵測到 Pico（未出現 `/dev/ttyACM0` 或 `RPI-RP2` 磁碟），請嘗試更換線材或 USB 埠口
- 避免使用 USB 集線器，可能導致裝置偵測異常
- 可透過其他裝置（如手機）測試線材是否支援資料傳輸

若對於線材選擇仍有疑問或持續遇到問題，請提供您的設定環境詳情（如電腦埠口類型、線材種類、連接時的裝置反應），我將進一步為您指引！