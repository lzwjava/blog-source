---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 解決Logitech藍牙配對問題
translated: true
type: note
---

### 疑難排解 AuthenticationCanceled 錯誤

此錯誤常見於 Logitech 藍牙鍵盤（你的 MAC `F4:73:35:78:28:4E` 符合 Logitech 的 OUI 前綴）在 Ubuntu 配對過程中，因認證逾時、缺少 PIN 碼提示或 BlueZ 代理處理不當而發生。記錄中短暫的連線/斷線顯示鍵盤有回應，但程序在完成前逾時。其他裝置（如 `54:2B:FC:F1:1C:D8`）可能造成干擾——請先清除它們。

#### 快速準備步驟
1. **移除所有已配對裝置** 以避免衝突：  
   在 `bluetoothctl` 中執行 `devices` 列出裝置，然後對每個裝置執行 `remove <MAC>`（例如 `remove 54:2B:FC:F1:1C:D8`）。最後輸入 `exit` 離開。

2. **重啟藍牙服務**：  
   ```
   sudo systemctl restart bluetooth
   sudo systemctl status bluetooth  # 確認服務處於活動狀態
   ```

3. **將鍵盤設為配對模式**：長按配對按鈕（例如 Easy-Switch 頻道或藍牙按鈕），直到 LED 快速閃爍。每次嘗試時都需重新執行此操作。

#### 在 bluetoothctl 中的增強配對步驟
重新開啟 `bluetoothctl` 並嚴格按照以下步驟操作——代理設定至關重要，先行信任裝置通常能避開部分逾時問題。對於 Logitech 型號（如 K380、K480、MX Keys），在輸入 `pair` 指令後需立即在實體鍵盤上盲打輸入任意 PIN 碼（畫面上不會顯示輸入內容）。

1. **進入 bluetoothctl**：  
   ```
   bluetoothctl
   ```

2. **開啟電源並設定代理**：  
   ```
   power on
   agent on
   default-agent
   ```

3. **掃描並確認裝置**：  
   ```
   scan on
   ```  
   等待 `F4:73:35:78:28:4E` 出現（如有需要可按 Enter 刷新）。接著：  
   ```
   scan off  # 停止掃描以專注操作
   ```

4. **信任裝置**（有助於重新連線時自動接受）：  
   ```
   trust F4:73:35:78:28:4E
   ```

5. **配對**：  
   ```
   pair F4:73:35:78:28:4E
   ```  
   - 若出現 PIN 碼/通行金鑰（例如 `[agent] PIN code: 390412` 或 `[agent] Passkey: 299595`），請立即在實體鍵盤上輸入該數字並按 Enter。即使沒有提示顯示也請盲打輸入。  
   - 若未顯示 PIN 碼（某些 Logitech 裝置常見），可嘗試在鍵盤輸入 `0000` 或 `1234` 後按 Enter。  
   - 注意觀察 `[CHG] Paired: yes` 訊息。若短暫連線後中斷，請立即重新執行 `connect F4:73:35:78:28:4E`。

6. **連線並信任**：  
   ```
   connect F4:73:35:78:28:4E
   trust F4:73:35:78:28:4E  # 若之前未執行
   ```

7. **退出並測試**：  
   ```
   exit
   ```  
   開啟文字編輯器或終端機——輸入文字驗證功能。若成功運作，喚醒時應會自動重新連線。

#### 若仍失敗
- **圖形介面備援方案**：使用 Ubuntu 設定 > 藍牙（切換開啟，選擇裝置）。此方式通常會顯示可見的 PIN 碼提示。若指令列代理失敗，圖形介面的 pinentry 處理效果更佳。
- **盲打 PIN 碼重試**：即使未顯示代碼，部分使用者在輸入 `pair` 後立即輸入 `0000` + Enter 仍能成功——鍵盤會以靜默方式完成認證。
- **查看記錄線索**：在配對期間於另一個終端機執行 `sudo journalctl -u bluetooth -f`。尋找 "PIN code" 或逾時相關訊息。
- **更新 BlueZ**：確保使用最新版本（Ubuntu 24.04+ 搭載 BlueZ 5.72+，對 Logitech 支援更佳）：  
  ```
  sudo apt update && sudo apt upgrade bluez
  ```
- **USB 接收器特殊情況**：你的 USB 3.0 介面 BT 5.3 發射器正常，但可嘗試改用 USB 2.0 連接埠——偶有干擾報告。
- **型號特定處理**：若為 K480/MX Keys 型號，請長按配對按鈕 5 秒以上。對於多裝置鍵盤，請先切換至未使用的頻道。

以上步驟應能解決問題——多數 Logitech 案例根源於盲打 PIN 碼步驟。若你提供具體型號或完整記錄，我可進一步優化建議。

[Bluetooth Pairing - AuthenticationCanceled (AskUbuntu)](https://askubuntu.com/questions/1373574/bluetooth-pairing-authenticationcanceled)  
[[SOLVED] Bluetooth keyboard: Unable to pair (Arch Linux Forums)](https://bbs.archlinux.org/viewtopic.php?id=174239)  
[Barely able to pair Logitech K480 on bluez 5.72 (GitHub)](https://github.com/bluez/bluez/issues/654)