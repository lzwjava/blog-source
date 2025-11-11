---
audio: false
generated: true
lang: hant
layout: post
title: 修復 Ubuntu 的 Wi-Fi 斷線問題
translated: true
type: note
---

在 Ubuntu 系統中，當有線連接保持穩定時出現 Wi-Fi 斷線問題，可能由多種因素引起。以下是一步一步的診斷與解決指南：

---

### **1. 檢查驅動程式問題**
您的 MSI B760M Mortar WiFi 主機板很可能使用 **Intel Wi-Fi 6E AX211/AX210** 無線網卡。雖然 Intel 驅動程式在 Linux 中通常有良好支援，但仍可能出現問題。

#### **步驟：**
- **識別您的 Wi-Fi 晶片組：**  
  在終端機中執行：  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  尋找 Wi-Fi 介面卡（可能顯示為 `Intel Corporation Device [8086:...]`）。

- **檢查是否載入正確驅動程式：**  
  ```bash
  lsmod | grep iwlwifi
  ```
  若無任何顯示，表示驅動程式未載入。

- **安裝/更新驅動程式：**  
  Intel Wi-Fi 驅動程式（`iwlwifi`）已包含在 Linux 核心中，但您可能需要更新韌體：
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. 停用 Wi-Fi 省電功能**
Linux 系統有時會過度積極地關閉 Wi-Fi 網卡以節省能源，導致連線中斷。

#### **步驟：**
- 暫時停用省電模式：  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  或手動檢查設定：
  ```bash
  iw dev wlan0 get power_save
  ```
  （請將 `wlan0` 替換為從 `ip a` 指令獲取的介面名稱。）

- **套用變更：**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. 檢查訊號干擾或路由器問題**
- **使用其他裝置測試**（手機/筆電）確認問題是否依然存在。
- **變更 Wi-Fi 頻道**（使用 `iwlist` 掃描擁塞頻道）：
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- 嘗試使用 **5GHz 頻段**（若可用）以減少干擾。

---

### **4. 停用 IPv6**
部分路由器/網路服務供應商存在 IPv6 相容性問題。

#### **步驟：**
- 編輯 `/etc/sysctl.conf` 並新增：
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- 套用設定：
  ```bash
  sudo sysctl -p
  ```

---

### **5. 更新核心與 NetworkManager**
新版核心通常能修復 Wi-Fi 問題。
```bash
sudo apt update && sudo apt upgrade
```
如有需要，可安裝 **主線核心**（例如 6.5+ 版本）：
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. 停用硬體加密功能（若適用）**
部分 Intel Wi-Fi 網卡在硬體加密方面存在問題。  
編輯 `/etc/modprobe.d/iwlwifi.conf`（若不存在請建立）：
```plaintext
options iwlwifi 11n_disable=1
```
接著執行：
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. 檢查 RFKill 或 Wi-Fi 封鎖狀態**
```bash
rfkill list
```
若 Wi-Fi 被封鎖（例如顯示 `soft blocked: yes`），請解除封鎖：
```bash
sudo rfkill unblock wifi
```

---

### **8. 使用 USB Wi-Fi 介面卡測試**
若問題持續存在，可嘗試使用 **相容 Linux 的 USB Wi-Fi 介面卡**（例如 TP-Link Archer T4U）來判斷問題是否源自 Intel 網卡本身。

---

### **9. 檢查系統日誌錯誤**
```bash
journalctl -u NetworkManager --no-pager -n 50
```
尋找 `iwlwifi` 相關錯誤或斷線事件記錄。

---

### **最終建議**
- 若以上方法皆無效，可考慮 **雙系統啟動 Windows** 以確認是否為硬體問題。
- 或者，若 Wi-Fi 持續不穩定，可使用 **USB 轉以太網路轉接器** 作為替代方案。

如需進一步除錯協助，請隨時告知！