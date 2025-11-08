---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 NVIDIA 驅動程式套件衝突
translated: true
type: note
---

這看起來像是 Ubuntu（從套件版本推測可能是 22.04）在更新 NVIDIA 驅動程式時常見的套件衝突問題。`nvidia-kernel-common-535` 套件試圖覆寫一個已由 `nvidia-firmware-535` 佔用的韌體檔案（`gsp_ga10x.bin`），導致 dpkg 中止執行。這是 Ubuntu 軟體庫中 NVIDIA 535 系列驅動程式的已知問題。

請保持冷靜——您的系統應該仍能啟動（不過如果驅動程式部分損毀，圖形介面可能會處於軟體渲染模式）。以下是安全解決問題的逐步操作說明。請在終端機中執行這些指令（如果圖形介面不穩定，請使用 TTY：按 Ctrl+Alt+F3 切換）。

### 快速修復嘗試（優先嘗試最安全的方法）
1. 嘗試自動修復損毀的套件：
   ```
   sudo apt --fix-broken install
   ```
   這通常能自動解決依賴性/解包問題，無需手動干預。

2. 如果上述方法失敗（或部分成功但仍有錯誤），請清理中斷的安裝：
   ```
   sudo dpkg --configure -a
   sudo apt update
   sudo apt upgrade
   ```

### 如果問題依舊：強制覆寫衝突檔案
錯誤特別出現在 `nvidia-kernel-common-535` 的 deb 檔案上。強制 dpkg 覆寫重複的檔案：
```
sudo dpkg -i --force-overwrite /var/cache/apt/archives/nvidia-kernel-common-535_535.274.02-0ubuntu1_amd64.deb
```
- 這會無視檔案衝突，僅安裝該套件。
- 接著執行：
  ```
  sudo apt --fix-broken install
  sudo apt autoremove
  sudo apt upgrade
  ```
- 最後重新啟動：`sudo reboot`。

### 最終手段：清除並重新安裝 NVIDIA 套件
如果上述方法無效（例如存在更深層的版本衝突），請移除衝突的 NVIDIA 組件後重新安裝：
1. 清除有問題的套件（如需調整版本，請用 `dpkg -l | grep nvidia` 檢查）：
   ```
   sudo dpkg --force-all -P nvidia-firmware-535-535.274.02 nvidia-kernel-common-535
   ```
2. 清理系統：
   ```
   sudo apt autoremove --purge
   sudo apt autoclean
   ```
3. 重新安裝驅動程式：
   ```
   sudo apt update
   sudo apt install nvidia-driver-535
   ```
4. 重新啟動。

### 預防與建議
- 加入 graphics-drivers PPA 以獲得更穩定的 NVIDIA 更新：`sudo add-apt-repository ppa:graphics-drivers/ppa && sudo apt update`。
- 如果您使用筆記型電腦，請在安裝驅動程式前確認 BIOS 中的 Secure Boot 已停用。
- 重新啟動後，使用 `nvidia-smi`（應顯示您的 GPU）或 `prime-select query`（若使用 NVIDIA Optimus）測試。
- 若此操作導致顯示完全失效，請啟動至恢復模式並在那裡執行修復指令。

如果所有方法均無效或出現新錯誤，請將完整輸出內容貼至此處以進行進一步調整。

### 參考資料
- [Unmet dependencies nvidia-dkms-535 - package conflict breaks Ubuntu 22.04 install](https://forums.developer.nvidia.com/t/unmet-dependencies-nvidia-dkms-535-package-conflict-breaks-ubuntu-22-04-install/265788)
- [Ubuntu and NVIDIA-provided packages conflict, breaking installation](https://forums.developer.nvidia.com/t/ubuntu-and-nvidia-provided-packages-conflict-breaking-installation/259150)
- [Problem with nvidia package dependencies](https://askubuntu.com/questions/1491916/problem-with-nvidia-package-dependencies)
- [nvidia-kernel-common-535 conflicts with nvidia-firmware-535](https://superuser.com/questions/1833427/nvidia-kernel-common-535-conflicts-with-nvidia-firmware-535-535-161-07-535-161-0)