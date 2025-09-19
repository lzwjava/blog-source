---
audio: true
generated: false
image: false
lang: hant
layout: post
title: 安裝Ubuntu
translated: true
---

## 安裝

我之前寫過一篇關於 [如何組裝電腦](./computer-en) 的文章。讓我們嘗試一些不同的東西。今天，我在一台預裝 Windows 10 的 Lenovo Xiaoxing 14IAH8 筆記型電腦上安裝 Ubuntu 24.04。

```bash
sudo dd if=ubuntu-24.04.1-desktop-amd64.iso of=/dev/rdisk6 bs=1m
```

由於 Ubuntu 安裝程式需要，必須前往設定並停用裝置加密。

如果裝置加密已啟用且 BIOS 中已停用安全啟動，Windows 將提示輸入 BitLocker 復原密碼。

因此，必須先在 BIOS 中啟用安全啟動，登入 Windows，然後前往設定停用裝置加密。之後，可以再次停用安全啟動以啟動 Ubuntu 安裝程式。

## 卡住

當 Ubuntu 啟動 `gdm.service` (GNOME 顯示管理器) 並卡住時，通常表示圖形使用者介面 (GUI) 或顯示管理器本身出現問題。以下是一些可以採取的步驟來排除故障並解決問題：

1. **存取虛擬終端機：**
   - 如果您的系統卡在 GDM 螢幕上，您可以嘗試存取終端機來診斷問題。
   - 按下 `Ctrl + Alt + F2` (或 `F3`、`F4` 等) 切換到虛擬終端機。

2. **登入：**
   - 使用您的使用者名稱和密碼登入。

3. **檢查系統日誌：**
   - 使用以下命令檢查系統日誌中是否有任何錯誤或警告，這些錯誤或警告可能表示問題的原因：
     ```bash
     sudo journalctl -xe
     ```
4. **重新安裝 GDM 服務：**
   - 清除並重新安裝 GDM3。這將移除組態檔案並確保乾淨安裝：
     ```bash
     sudo apt remove --purge gdm3
     sudo apt install gdm3
     ```

5. **重新啟動系統：**
   - 重新啟動系統以套用變更：
     ```bash
     sudo reboot
     ```

## LightDM

如果 GDM3 失敗，LightDM 可用作替代顯示管理器。但是，安裝 LightDM 後，您可能會遇到登入畫面出現，但您輸入的任何密碼都被拒絕為不正確的問題。

1. **安裝和組態 LightDM：**
   - 安裝 LightDM：
     ```bash
     sudo apt-get install lightdm
     ```
   - 安裝期間，系統會提示您選擇預設顯示管理器。選擇 LightDM。
