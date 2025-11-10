---
audio: false
generated: true
lang: hant
layout: post
title: 解決藍牙鍵盤連接問題
translated: true
type: note
---

根據 `bluetoothctl` 輸出顯示嘗試連接時出現 `[DEL] Device`，以下是精確解決方案：

### 立即修復連接刪除問題
1. **移除現有裝置記錄**（對過時配置至關重要）：
   ```bash
   bluetoothctl
   remove F4:73:35:78:28:4E  # 移除鍵盤
   remove 24:27:30:24:C8:31   # 移除可能干擾的裝置
   exit
   ```

2. **重設藍牙堆疊**：
   ```bash
   sudo systemctl stop bluetooth
   sudo rm -rf /var/lib/bluetooth/*
   sudo systemctl start bluetooth
   ```

3. **使用正確順序重新配對**：
   ```bash
   bluetoothctl
   power on
   discoverable on
   pairable on
   agent on  # 啟用密碼代理
   scan on
   ```
   - **將 K380 置於配對模式**（LED 快速閃爍）
   - 當鍵盤出現時：
     ```bash
     pair F4:73:35:78:28:4E
     ```
   - **立即在鍵盤上輸入**螢幕顯示的 6 位數密碼（例如 `123456`）並按 Enter

4. **僅在成功配對後連接**：
   ```bash
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E
   scan off
   quit
   ```

### 問題發生原因
- 出現 `[DEL] Device` 是因為：
  - 藍牙堆疊檢測到連接失敗並清除裝置記錄
  - 嘗試連接前**缺少配對步驟**
  - 可能受到其他裝置（如 `midea` 裝置）的 RF 干擾

### 其他關鍵檢查
1. **驗證天線連接**：
   - 確保藍牙天線已旋入 MSI 主機板後置 I/O 面板

2. **檢查核心驅動程式**：
   ```bash
   dmesg | grep -i bluetooth
   ```
   尋找錯誤訊息如 `hci0: command timeout` 或 `Firmware failed to start`

3. **更新韌體**（若出現超時錯誤）：
   ```bash
   sudo apt install linux-firmware
   ```

4. **最小環境測試**：
   ```bash
   sudo rfkill unblock all
   sudo systemctl stop NetworkManager  # 暫時停止
   sudo systemctl restart bluetooth
   ```

### 若仍失敗
1. **替代配對方法**（繞過代理）：
   ```bash
   echo -e 'remove F4:73:35:78:28:4E\npair F4:73:35:78:28:4E\nconnect F4:73:35:78:28:4E\ntrust F4:73:35:78:28:4E' | bluetoothctl
   ```

2. **檢查鍵盤電池**（對藍牙連接至關重要）：
   - 若電壓過低請更換電池（K380 使用 CR2032 x 2）

3. **USB 藍牙適配器測試**：
   - 若內建藍牙有問題，可嘗試使用 $10 的 CSR4.0 USB 適配器

**預期成功指標**：
- 出現 `Pairing successful` 訊息
- `bluetoothctl` 中顯示 `Connection successful`
- `dmesg` 顯示 `HIDP: Bluetooth HID device driver`

配對完成後，您的 K380 應能重啟後保持連接。若再次斷線，請檢查 `journalctl -u bluetooth -f` 以獲取即時錯誤資訊。