---
audio: true
lang: hant
layout: post
title: 安裝Ubuntu
translated: true
---

## 安裝

我之前寫過一篇關於[如何組裝電腦](./computer-en)的文章。讓我們嘗試一些不同的東西。今天，我正在一台預裝 Windows 10 的聯想小新 14IAH8 筆記本電腦上安裝 Ubuntu 24.04。

```bash
sudo dd if=ubuntu-24.04.1-desktop-amd64.iso of=/dev/rdisk6 bs=1m
```

需要進入設定並關閉裝置加密，因為 Ubuntu 安裝程式需要這樣做。

如果裝置加密已啟用且 BIOS 中的安全啟動已禁用，Windows 將提示輸入 BitLocker 復原密碼。

因此，需要先在 BIOS 中啟用安全啟動，登入 Windows，然後進入設定關閉裝置加密。之後，可以再次禁用安全啟動以啟動 Ubuntu 安裝程式。

## 卡住了

當 Ubuntu 啟動 `gdm.service` (GNOME 顯示管理器) 並卡住時，通常表示圖形使用者介面 (GUI) 或顯示管理器本身出現問題。以下是一些可以採取的步驟來排除故障並解決問題：

1. **存取虛擬終端機：**
   - 如果您的系統卡在 GDM 螢幕上，您可以嘗試存取終端機來診斷問題。
   - 按下 `Ctrl + Alt + F2` (或 `F3`、`F4` 等) 切換到虛擬終端機。

2. **登入：**
   - 使用您的使用者名稱和密碼登入。

3. **檢查系統日誌：**
   - 使用以下命令檢查系統日誌中是否有任何錯誤或警告，這些錯誤或警告可能表明問題的原因：
     ```bash
     sudo journalctl -xe
     ```

4. **重新啟動 GDM 服務：**
   - 嘗試重新啟動 GDM 服務，看看是否能解決問題：
     ```bash
     sudo systemctl restart gdm
     ```

5. **重新啟動系統：**
   - 進行更改後，重新啟動系統以應用更改：
     ```bash
     sudo reboot
     ```
