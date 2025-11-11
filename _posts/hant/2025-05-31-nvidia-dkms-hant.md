---
audio: false
generated: true
lang: hant
layout: post
title: NVIDIA DKMS 建構問題
translated: true
type: note
---

看起來你遇到了一個問題：NVIDIA DKMS（動態核心模組支援）模組無法為你的新核心 `6.8.0-60-generic` 成功建置。這在更新核心時是常見問題，因為驅動程式模組需要針對新核心版本重新編譯，而有時會出現相容性或建置問題。

關鍵錯誤訊息包括：
* `Building module(s)......(bad exit status: 2)`
* `Error! Bad return status for module build on kernel: 6.8.0-60-generic (x86_64)`
* `Consult /var/lib/dkms/nvidia/535.183.06/build/make.log for more information.`
* `dpkg: error processing package linux-image-6.8.0-60-generic (--configure):`
* `E: Sub-process /usr/bin/dpkg returned an error code (1)`

這表示 NVIDIA 驅動程式版本 `535.183.06` 無法針對核心 `6.8.0-60-generic` 成功編譯，進而導致核心映像檔及相關套件無法正確設定。

以下是你可以嘗試的解決方法：

---

### 1. 檢查建置記錄檔 🪵

最重要的一步是檢查詳細的建置記錄檔，找出具體的錯誤訊息。這個記錄檔會告訴你編譯失敗的*原因*。
開啟終端機並執行：
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```
尋找以 `error:` 或 `fatal error:` 開頭的行。這些通常會指向遺失的檔案、編譯器問題或與核心原始碼的相容性問題。錯誤訊息 `Applying patch disable_fstack-clash-protection_fcf-protection.patch... done.` 後緊接著建置失敗，表示該修補程式可能不完全相容，或者存在其他修補程式未解決的問題。

---

### 2. 清理並嘗試修復損壞的套件 🛠️

首先，你可以嘗試讓 `apt` 修復損壞的相依性並完成套件設定。
```bash
sudo rm /var/crash/nvidia-dkms-535.0.crash # 移除舊的當機報告以允許新的報告產生
sudo apt --fix-broken install
sudo dpkg --configure -a
```
這可能會重新觸發 DKMS 建置。如果再次失敗，請繼續下一步。

---

### 3. 確保核心標頭檔正確安裝 🧠

DKMS 建置過程需要你嘗試建置的核心所對應的正確核心標頭檔。
```bash
sudo apt update
sudo apt install --reinstall linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04
```
如果你尚未執行 `6.8.0-60-generic` 核心（例如，更新過程被中斷），你也可以指定目前執行中核心的標頭檔，但這裡的主要目標是 `6.8.0-60-generic`。

---

### 4. 移除有問題的 DKMS 模組並重新設定 ♻️

你可以手動從 DKMS 中移除有問題的 NVIDIA 模組版本，然後讓系統嘗試重新建置它。
```bash
sudo dkms remove nvidia/535.183.06 --all
```
然後，再次嘗試重新設定套件：
```bash
sudo dpkg --configure -a
sudo apt update && sudo apt upgrade
```
這個過程應該會提示 DKMS 嘗試為 `6.8.0-60-generic` 核心重新建置模組。

---

### 5. 重新安裝 NVIDIA 驅動程式 💻

如果模組仍然無法建置，驅動程式版本 `535.183.06` 可能與核心 `6.8.0-60-generic` 存在相容性問題。

* **清除目前有問題的驅動程式：**
    ```bash
    sudo apt-get purge nvidia-dkms-535 nvidia-driver-535
    sudo apt autoremove
    sudo apt clean
    ```

* **安裝合適的驅動程式：**
    你可以讓 Ubuntu 嘗試安裝建議的驅動程式：
    ```bash
    sudo ubuntu-drivers autoinstall
    ```
    或者，你可以嘗試安裝相同版本（如果軟體庫現在認為它相容）或潛在更新、相容性更好的版本。例如，嘗試重新安裝 535 系列驅動程式：
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-535
    ```
    （套件管理員應該會選擇合適的 DKMS 版本。）

    之後，系統會再次嘗試建置 DKMS 模組。

---

### 6. 考慮使用更新的 NVIDIA 驅動程式版本 🚀

核心 6.8 相對較新。NVIDIA 535 系列驅動程式可能與此核心版本存在限制。你可能需要更新的驅動程式系列（例如 545、550 或更新版本，如果軟體庫或 NVIDIA 官方管道/PPA 提供）。

* 檢查可用的驅動程式：
    ```bash
    sudo apt search nvidia-driver
    ```
* 如果有更新的專有驅動程式可用（例如 `nvidia-driver-550`），你可以嘗試安裝它來取代 `nvidia-driver-535`。
    ```bash
    sudo apt install nvidia-driver-VERSION_NUMBER # 替換 VERSION_NUMBER
    ```

---

### 7. 如果你陷入開機循環或沒有圖形介面 📉

如果系統無法開機進入圖形環境：
* 開機進入恢復模式或較舊的核心（通常可以在開機時的 GRUB 選單中找到）。
* 進入命令列環境後，你可以嘗試上述步驟。
* 如果你需要暫時使用開源驅動程式來恢復圖形介面，同時修復 NVIDIA 驅動程式：
    ```bash
    sudo apt-get purge nvidia*
    sudo apt autoremove
    sudo apt install xserver-xorg-video-nouveau
    sudo reboot
    ```
    然後，再次嘗試安裝 NVIDIA 驅動程式。

---

**關鍵要點：** `/var/lib/dkms/nvidia/535.183.06/build/make.log` 的內容非常重要。如果上述步驟無效，該檔案中的錯誤將提供更具體的線索，你可能需要在網上搜尋這些特定錯誤，並結合你的核心版本和 NVIDIA 驅動程式版本進行查詢。

---

這個輸出顯示你的 Ubuntu 系統存在一系列相依性和設定問題，很可能與核心更新和 NVIDIA 驅動程式有關。讓我們分析問題並提出潛在解決方案。

**主要問題：**

1.  **`linux-generic-hwe-22.04` 的相依性問題：**
    * 它依賴於特定版本（`= 6.8.0-60.63~22.04.1`）的 `linux-headers-generic-hwe-22.04`。
    * `linux-headers-generic-hwe-22.04` 尚未設定完成，導致 `linux-generic-hwe-22.04` 的設定失敗。

2.  **`linux-image-6.8.0-60-generic` 設定失敗：**
    * 此核心映像檔的安裝後指令碼以退出狀態 1 失敗。
    * 錯誤記錄檔顯示這與 NVIDIA 驅動程式（`nvidia/535.183.06`）無法針對此特定核心版本（`6.8.0-60-generic`）成功建置有關。
    * NVIDIA 驅動程式的 DKMS（動態核心模組支援）建置過程失敗。記錄檔 `/var/lib/dkms/nvidia/535.183.06/build/make.log` 將包含建置錯誤的更多詳細資訊。
    * 還有一個與建立 NVIDIA DKMS 失敗的當機報告相關的錯誤，表明系統的當機報告機制或檔案系統權限可能存在問題。

3.  **`linux-headers-6.8.0-60-generic` 和 `linux-headers-generic-hwe-22.04` 設定失敗：**
    * 這些套件設定失敗可能是因為 `linux-image-6.8.0-60-generic` 套件設定失敗，而它們可能依賴於該套件。

**潛在原因：**

* **不完整或中斷的核心更新：** 系統可能在某次核心升級過程中被中斷，導致一些套件處於不一致狀態。
* **NVIDIA 驅動程式不相容：** 已安裝的 NVIDIA 驅動程式版本（`535.183.06`）可能與新核心版本（`6.8.0-60-generic`）存在建置問題。
* **DKMS 問題：** DKMS 框架本身可能存在問題，阻止了 NVIDIA 驅動程式的建置。
* **檔案系統問題：** 關於無法建立當機報告的錯誤可能表示 `/var/crash/` 目錄的磁碟空間或檔案權限存在問題。

**疑難排解步驟：**

1.  **嘗試重新設定套件：**
    開啟終端機並執行以下指令：
    ```bash
    sudo dpkg --configure -a
    ```
    此指令嘗試設定所有處於半設定狀態的套件。

2.  **檢查 NVIDIA DKMS 建置記錄檔：**
    檢查記錄檔，了解 NVIDIA 驅動程式建置期間的詳細錯誤訊息：
    ```bash
    less /var/lib/dkms/nvidia/535.183.06/build/make.log
    ```
    此記錄檔可能提供關於遺失相依性或編譯錯誤的線索。

3.  **嘗試重新安裝 NVIDIA 驅動程式：**
    你可以嘗試移除然後重新安裝 NVIDIA 驅動程式。首先，嘗試清除它：
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    ```
    然後，嘗試重新安裝。如果目前版本有問題，你可能想嘗試不同的版本：
    ```bash
    sudo apt install nvidia-driver-535  # 或另一個建議的版本
    ```
    安裝後，重新啟動系統。

4.  **清理套件快取並重試：**
    ```bash
    sudo apt clean
    sudo apt update
    sudo apt upgrade
    sudo dpkg --configure -a
    ```

5.  **重新安裝有問題的核心和標頭檔：**
    你可以嘗試重新安裝導致問題的特定核心和標頭檔套件：
    ```bash
    sudo apt install --reinstall linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
    ```
    之後，再次嘗試設定：
    ```bash
    sudo dpkg --configure -a
    ```

6.  **檢查磁碟空間：**
    確保你的根分割區（`/`）有足夠的可用空間，因為這有時會導致套件安裝和設定期間出現問題。
    ```bash
    df -h /
    ```

7.  **處理當機報告錯誤（如果持續存在）：**
    如果關於 `/var/crash/nvidia-dkms-535.0.crash` 的錯誤持續存在，你可以嘗試移除該檔案（如果它存在且你不需要它來除錯）或檢查 `/var/crash/` 目錄的權限。
    ```bash
    sudo rm -f /var/crash/nvidia-dkms-535.0.crash
    sudo chmod 777 /var/crash  # 對寬鬆權限要小心，如果不需要請復原
    ```

8.  **開機進入先前的核心：**
    如果你安裝了先前的核心版本，可以嘗試從 GRUB 選單開機進入該核心。這可以讓你在穩定的環境中執行疑難排解步驟。如果系統在較舊的核心下運作正常，問題很可能特定於 `6.8.0-60-generic` 核心或其與 NVIDIA 驅動程式的互動。

**重要注意事項：**

* **備份：** 在進行重大變更，特別是涉及套件移除之前，備份重要資料始終是個好主意。
* **保持耐心：** 套件設定和安裝可能需要一些時間。
* **查閱記錄檔：** 錯誤訊息和記錄檔（尤其是 NVIDIA DKMS 建置記錄檔）對於診斷問題的確切原因至關重要。

從前幾個步驟開始，看看它們是否能解決問題。如果不行，再繼續進行更深入的解決方案，並仔細檢查遇到的任何錯誤訊息。祝你好運！

---

這個來自 NVIDIA DKMS 建置記錄檔的輸出顯示，編譯失敗的原因是**無法識別的命令列選項：`-ftrivial-auto-var-init=zero`**。

這個編譯器選項是 GCC（可能是版本 12 或更新版本）和 Clang 中相對較新的功能。看起來用於為你的核心（6.8.0-60-generic）建置 NVIDIA 驅動程式的編譯器無法識別此選項。

**可能的原因和解決方案：**

1.  **過時的編譯器：** 你的系統可能安裝了較舊版本的 GCC 或 Clang 作為預設編譯器。核心標頭檔可能是用使用此選項的較新編譯器編譯的，但 NVIDIA 驅動程式建置系統卻使用了較舊的編譯器。

    **解決方案：**
    * **安裝更新的編譯器：** 你可以嘗試安裝更新版本的 GCC。
        ```bash
        sudo apt update
        sudo apt install gcc-12  # 或更新版本如 gcc-13
        ```
    * **更新建置環境：** 確保你的建置工具是最新的。
        ```bash
        sudo apt update
        sudo apt install build-essential
        ```
    * **指定編譯器（如果可能）：** 一些建置系統允許你指定要使用的編譯器。檢查 NVIDIA 驅動程式建置說明或設定檔中與編譯器相關的選項（例如 `CC` 環境變數）。

2.  **與核心建置設定的不相容性：** 你使用的核心可能是用啟用了此選項的編譯器建置的，而 NVIDIA 驅動程式建置系統以某種方式繼承或遇到它，導致與其自身的編譯器發生失敗。

    **解決方案：**
    * **嘗試不同的 NVIDIA 驅動程式版本：** 最新的 NVIDIA 驅動程式可能對較新的核心和編譯器功能有更好的相容性。你可以嘗試安裝更新的穩定版本。
        ```bash
        sudo apt update
        sudo apt install nvidia-driver-<latest-version>
        ```
        將 `<latest-version>` 替換為你系統上最新的建議驅動程式套件名稱。通常可以透過搜尋 `apt search nvidia-driver` 找到。
    * **降級你的核心（作為臨時解決方法）：** 如果你安裝了先前能與 NVIDIA 驅動程式配合使用的核心版本，可以從 GRUB 選單開機進入該核心。這不是永久解決方案，但可以在你針對新核心疑難排解驅動程式問題時提供一個可運作的系統。

3.  **NVIDIA 驅動程式套件的問題：** 你嘗試安裝的特定 NVIDIA 驅動程式套件可能與你的核心和編譯器設定存在問題。

    **解決方案：**
    * **嘗試不同的安裝方法：** 如果你透過 `apt` 安裝驅動程式，可以嘗試直接從 NVIDIA 網站下載驅動程式，並使用 `.run` 檔案進行安裝。請仔細遵循 NVIDIA 提供的說明。
    * **檢查已知問題：** 在線上論壇或 NVIDIA 支援網站搜尋你使用的特定驅動程式版本和核心組合的已知問題。

**嘗試步驟：**

1.  **檢查你的 GCC 版本：**
    ```bash
    gcc --version
    ```
    將其與用於建置核心的 GCC 版本進行比較（你可能可以在網上找到你 Ubuntu 版本的核心建置環境資訊）。

2.  **嘗試安裝更新的 NVIDIA 驅動程式：**
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-550  # 範例：嘗試更新版本
    sudo reboot
    ```

3.  **如果上述方法無效，嘗試清除並重新安裝建議的驅動程式：**
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    sudo apt update
    sudo ubuntu-drivers autoinstall  # 安裝建議的驅動程式
    sudo reboot
    ```

4.  **如果你仍然遇到問題，考慮安裝更新的 GCC 版本（請小心，因為這有時會產生意外副作用）：**
    ```bash
    sudo apt install gcc-12 g++-12
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 12
    # 你可能也想保留舊版本，並在需要時切換回來
    # 要切換回來：sudo update-alternatives --config gcc 和 sudo update-alternatives --config g++
    sudo apt install build-essential # 確保在編譯器變更後更新建置工具
    sudo dpkg --configure -a # 重新設定套件
    sudo reboot
    ```

記住在嘗試任何驅動程式安裝或重大系統變更後重新啟動系統。仔細監控輸出以尋找任何新的錯誤訊息。如果你持續遇到問題，提供更多關於你 Ubuntu 版本的詳細資訊可能有助於找到更具體的解決方案。

---

看起來你在嘗試設定 Linux 核心套件時遇到了相依性和 DKMS（動態核心模組支援）問題，特別是 NVIDIA 驅動程式模組無法為新核心 (6.8.0-60-generic) 成功建置。

### 以下是解決方法：

---

### **1. 修復相依性並設定套件**
首先，嘗試修復相依性問題並設定套件：

```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
```

如果無效，手動強制設定有問題的套件：

```bash
sudo apt install -f linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
```

---

### **2. 重新安裝 NVIDIA 驅動程式**
錯誤顯示 NVIDIA DKMS 模組 (`nvidia/535.183.06`) 無法為核心 `6.8.0-60-generic` 成功建置。修復方法：

#### **選項 A：重新安裝 NVIDIA 驅動程式**
```bash
sudo apt install --reinstall nvidia-dkms-535 nvidia-driver-535
```

#### **選項 B：清除並重新安裝 NVIDIA 驅動程式**
如果重新安裝無效，嘗試乾淨重新安裝：
```bash
sudo apt purge nvidia-*
sudo apt autoremove
sudo apt install nvidia-driver-535
```

#### **選項 C：暫時開機進入較舊的核心**
如果系統無法開機，重新啟動進入較舊的核心（在 GRUB 中選擇），然後：
```bash
sudo apt remove linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo update-grub
```

---

### **3. 檢查 DKMS 建置記錄檔**
錯誤提到 `/var/lib/dkms/nvidia/535.183.06/build/make.log`。檢查它以取得詳細資訊：
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```

這可能會揭示模組建置失敗的原因（例如，遺失相依性、編譯器問題）。

---

### **4. 手動安裝遺失的相依性**
如果記錄檔顯示遺失相依性，請安裝它們：
```bash
sudo apt install build-essential linux-headers-generic
```

---

### **5. 重新建置 DKMS 模組**
修復相依性後，手動重新建置模組：
```bash
sudo dkms remove nvidia/535.183.06 --all
sudo dkms install nvidia/535.183.06
```

---

### **6. 更新 Initramfs**
修復 NVIDIA 驅動程式後，更新 initramfs：
```bash
sudo update-initramfs -u -k all
```

---

### **7. 最終修復嘗試**
如果所有其他方法都失敗，移除有問題的核心並堅持使用較舊的版本：
```bash
sudo apt purge linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo apt autoremove
sudo update-grub
```

然後，在再次嘗試之前，等待更新的 NVIDIA 驅動程式或核心。

---

### **8. 預防未來問題**
為避免類似問題，考慮：
- **停用自動核心更新**（如果你依賴 NVIDIA 驅動程式）：
  ```bash
  sudo apt-mark hold linux-image-generic linux-headers-generic
  ```
- 如果相容性是一個反覆出現的問題，**使用官方 NVIDIA 驅動程式**（而不是 Ubuntu 的套件）。

---

### **最後注意事項**
- 如果系統變得無法開機，使用 **GRUB** 選擇較舊的核心。
- 如果 NVIDIA 驅動程式對你的工作流程至關重要，考慮使用 **LTS 核心**（非 HWE）以獲得更好的穩定性。

如果你需要進一步協助，請告訴我！

---

如果你只想繼續進行 `apt upgrade` 並**跳過有問題的套件**，你可以暫時將它們從升級過程中排除。方法如下：

### **選項 1：跳過損壞的套件並繼續升級**
執行：
```bash
sudo apt --fix-broken install
sudo apt upgrade -y --ignore-missing --allow-downgrades
```
- `--ignore-missing` 跳過無法取得的套件。
- `--allow-downgrades` 允許 APT 在需要時降級套件。

### **選項 2：保留（阻止）有問題的套件**
如果問題持續存在，**保留**（阻止）有問題的套件以防止它們被升級：
```bash
sudo apt-mark hold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04 linux-image-6.8.0-60-generic
```
然後重試：
```bash
sudo apt upgrade -y
```

### **選項 3：強制升級（不建議）**
如果你不介意可能進一步破壞系統，強制升級：
```bash
sudo apt -o Dpkg::Options::="--force-overwrite" --fix-broken install
sudo apt upgrade -y
```
⚠️ **警告：** 如果相依性不匹配，這可能導致不穩定。

### **跳過之後：**
- 系統仍將運作，但 **NVIDIA 驅動程式可能無法在核心 `6.8.0-60` 上運作**。
- 如果需要，你可以**開機進入較舊的核心**（在 GRUB 中選擇）。
- 一旦 NVIDIA 發布相容的更新，你可以**取消保留**套件：
  ```bash
  sudo apt-mark unhold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04
  ```

升級後需要幫忙檢查目前使用中的核心嗎？