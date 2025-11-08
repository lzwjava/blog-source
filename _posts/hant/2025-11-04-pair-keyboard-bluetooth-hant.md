---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 透過藍牙指令列配對羅技鍵盤
translated: true
type: note
---

### 前置準備
- 確保您的 Bluetooth 5.3 發射器（dongle）已插入 USB 3.0 埠並被 Ubuntu 識別。在終端機中執行 `lsusb` 檢查是否出現（尋找類似「Bluetooth」或供應商 ID 的項目）。如果沒有，請嘗試其他 USB 埠或重新啟動。
- 如果尚未安裝，請安裝 Bluetooth 工具：  
  ```
  sudo apt update
  sudo apt install bluez bluetooth bluez-tools
  ```
- 如有需要，解除 Bluetooth 封鎖：  
  ```
  rfkill unblock bluetooth
  ```
- 重新啟動 Bluetooth 服務：  
  ```
  sudo systemctl restart bluetooth
  ```

### 使用 bluetoothctl 進行配對步驟（建議用於 CLI）
`bluetoothctl` 工具是在 Linux/Ubuntu 中管理 Bluetooth 的標準方式。Logitech 鍵盤（如 MX Keys、K380 或類似型號）通常需要在實體鍵盤上輸入配對 PIN 碼。

1. **開啟 Bluetooth 控制台**：  
   ```
   bluetoothctl
   ```
   這會進入互動式 shell（提示符號變為 `[bluetooth]#`）。

2. **啟用適配器**：  
   ```
   power on
   ```
   （如果顯示「No default controller available」，請執行 `list` 查看您的適配器，如果有多個則執行 `select <adapter_MAC>`。）

3. **設定配對代理**：  
   ```
   agent on
   default-agent
   ```
   這會啟用 PIN 碼處理，並將您的 session 設為預設配對對象。

4. **開始掃描裝置**：  
   ```
   scan on
   ```
   保持此指令執行。您的 Logitech 鍵盤應在約 10-20 秒後出現（例如顯示為「Logitech K380」或類似名稱，並帶有 MAC 位址如 `XX:XX:XX:XX:XX:XX`）。

5. **將 Logitech 鍵盤設為配對模式**：  
   - 開啟電源（如果有電源開關）。  
   - 按住 Bluetooth 配對按鈕（通常在側面或頂部—請查看您的型號；對於多裝置型號如 MX Keys，請按住頻道按鈕 1/2/3 約 3-5 秒，直到 LED 快速閃爍）。  
   - 如果是單一裝置型號，請按住主配對按鈕。

6. **配對裝置**：  
   一旦掃描中顯示裝置（按 Enter 重新整理），執行：  
   ```
   pair <MAC_ADDRESS>
   ```
   - 範例：`pair 12:34:56:78:9A:BC`  
   - Ubuntu 將提示輸入 PIN 碼（Logitech 通常為 0000 或 1234—請先嘗試預設值）。  
   - **Logitech 關鍵步驟**：直接在*實體鍵盤*上輸入 PIN 碼並按 Enter。（如果沒有出現 GUI 通知，這一步至關重要—有些用戶回報需要透過 `gnome-control-center` > 通知啟用系統通知，但 CLI 通常可繞過此問題。）

7. **信任並連線**：  
   ```
   trust <MAC_ADDRESS>
   connect <MAC_ADDRESS>
   ```
   - 這會讓裝置在未來自動連線。

8. **離開控制台**：  
   ```
   exit
   ```

### 疑難排解
- **裝置未掃描到**：確保鍵盤處於配對模式（LED 閃爍）。執行 `scan off` 然後再次執行 `scan on`。等待最多 30 秒。
- **配對失敗（例如「AuthenticationCanceled」）**：先移除裝置（`remove <MAC>`），然後重試。對於頑固的 Logitech 型號，請嘗試按住配對按鈕更長時間或切換頻道。
- **沒有 PIN 碼提示**：有些鍵盤無需 PIN 碼即可配對—直接進行連線。如果卡住，請檢查日誌：配對時執行 `sudo journalctl -u bluetooth -f`。
- **適配器問題**：如果使用 USB Bluetooth 5.3 dongle，請確認核心支援（Ubuntu 22.04+ 對 BT 5.3 支援良好）。如果使用較舊的 Ubuntu，請更新核心：`sudo apt install linux-generic-hwe-22.04`。
- **GUI 替代方案**：開啟設定 > Bluetooth，切換開啟並從那裡配對—但對於 Logitech 的特殊情況，CLI 更可靠。
- 測試：配對後，在終端機中輸入文字。如果正常運作，可透過 `bluetoothctl` 或 crontab 將其加入開機自動連線。

如果您的特定 Logitech 型號（例如 MX Keys Mini）有獨特問題，請提供確切型號以獲取量身訂製的步驟。

### 參考資料
- [在 Ubuntu 20.04 中配對 LOGITECH K380](https://unix.stackexchange.com/questions/590221/pairing-logitech-k380-in-ubuntu-20-04)  
- [Logitech MX Keys 無法透過 Bluetooth 配對](https://askubuntu.com/questions/1270419/20-04-logitech-mx-keys-wont-pair-with-bluetooth)  
- [透過 Bluetooth 將 Logitech MX Keys 與 Xubuntu 配對](https://zroupas.github.io/linux/2021/08/25/pair_mxkeys_xubuntu_bt.html)  
- [Ubuntu 20.04 無法配對 Bluetooth 鍵盤](https://askubuntu.com/questions/1398096/ubuntu-20-04-cannot-pair-bluetooth-keyboard)