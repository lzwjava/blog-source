---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 NVIDIA 驅動程式版本不符
translated: true
type: note
---

### 理解錯誤原因
`nvidia-smi` 指令執行失敗是由於 NVIDIA 核心驅動程式（載入於作業系統核心）與用戶空間 NVML（NVIDIA 管理程式庫）元件之間的版本不匹配所致。這種情況通常發生在核心更新、驅動程式部分安裝或系統升級後未完整重新安裝驅動程式時。回報的 NVML 版本 (535.274) 顯示您正在使用較新的 NVIDIA 驅動程式系列（可能屬於 535 系列），但核心模組未能同步。

請放心——此問題可在不丟失資料的情況下修復。以下是逐步疑難排解與解決方案，從最簡單的方法開始。

### 快速修復（優先嘗試）
1. **重新啟動系統**  
   最常見的原因是核心模組狀態過時。重新啟動可徹底重新載入所有元件。  
   ```
   sudo reboot
   ```  
   重啟後再次執行 `nvidia-smi`。若運作正常，即完成修復！

2. **檢查當前驅動程式與核心版本**  
   驗證已安裝的版本：  
   ```
   # 檢查核心驅動程式版本
   cat /proc/driver/nvidia/version

   # 檢查已載入的核心模組
   lsmod | grep nvidia

   # 檢查當前核心版本
   uname -r
   ```  
   將此處的驅動程式版本與 535.274 比對。若版本不符（例如核心顯示 535.x 但 x ≠ 274），請繼續進行重新安裝。

### 完整解決方案：重新安裝 NVIDIA 驅動程式
若重新啟動無效，請重新安裝驅動程式以同步所有元件。以下步驟假設您使用 Ubuntu/Debian 系統（nanoGPT 環境常見配置，其他發行版如 Fedora 請調整指令）。

#### 選項 1：透過套件管理員安裝（推薦，穩定性最佳）
1. **清除現有驅動程式**（移除版本衝突）：  
   ```
   sudo apt update
   sudo apt purge 'nvidia*'
   sudo apt autoremove
   sudo rm -rf /usr/lib/nvidia*  # 可選步驟：清理殘留檔案
   ```

2. **重新啟動以清除模組**：  
   ```
   sudo reboot
   ```

3. **安裝匹配的驅動程式**：  
   由於您的 NVML 版本為 535.274，請安裝 535 系列（或更新版本）。請至 NVIDIA 官網根據您的 GPU 型號確認，若安裝 535 系列：  
   ```
   sudo apt install nvidia-driver-535 nvidia-utils-535
   ```  
   （若使用其他發行版請替換套件名稱，例如 Fedora 使用 `dnf`）

4. **重新啟動並驗證**：  
   ```
   sudo reboot
   nvidia-smi  # 此時應正常運作
   ```

#### 選項 2：直接使用 NVIDIA 官方安裝檔（適用最新/自訂版本）
1. 從 [NVIDIA 驅動程式檔案庫](https://www.nvidia.com/Download/driverResults.aspx/227xxx/en-us/) 下載 535.274 版執行檔（請搜尋您的 GPU 型號與 535.274）。  
   ```
   wget https://us.download.nvidia.com/XFree86/Linux-x86_64/535.274.05/NVIDIA-Linux-x86_64-535.274.05.run
   chmod +x NVIDIA-Linux-x86_64-535.274.05.run
   ```

2. **停止顯示管理員**（切換至控制台）：  
   ```
   sudo systemctl stop gdm  # 或 lightdm/sddm
   sudo telinit 3  # 或使用 Ctrl+Alt+F3 切換 TTY
   ```

3. **執行安裝**：  
   ```
   sudo ./NVIDIA-Linux-x86_64-535.274.05.run --no-questions
   ```  
   遵循提示步驟；安裝過程可能出現版本不匹配警告——請繼續執行。

4. **重新啟動**：  
   ```
   sudo reboot
   ```

### 若問題持續存在
- **是否啟用安全啟動？** 請至 BIOS/UEFI 設定中停用此功能，因其會阻擋未簽署的核心模組。
- **核心版本不匹配？** 若近期更新過核心，請透過 GRUB 開機選單（開機時按住 Shift 鍵）選擇舊版核心開機，並重新安裝驅動程式。
- **檢查紀錄檔線索**：執行 `dmesg | grep nvidia` 或查閱 `/var/log/Xorg.0.log` 尋找錯誤訊息。
- **GPU 特定問題？** 執行 `lspci | grep -i nvidia` 確認系統是否偵測到您的 GPU。

修復完成後，`nvidia-smi` 應顯示 GPU 使用率、記憶體狀態等資訊。若您正在 nanoGPT 中訓練模型，此修復將解除 CUDA 功能限制。如果您能提供更多詳細資訊（例如發行版版本、GPU 型號或版本檢查輸出結果），我可以進一步提供具體建議！