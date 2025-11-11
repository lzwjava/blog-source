---
audio: false
generated: true
lang: hant
layout: post
title: 移除 Ubuntu 上的 Outline VPN 客戶端
translated: true
type: note
---

看來 `apt` 找不到名為 `outline-client` 的套件。這通常意味著以下兩種情況之一：

1. **您並非使用 `apt` 安裝 Outline（即不是以 .deb 套件形式安裝）**。這是 Outline 最常出現此錯誤的原因，因為許多用戶是透過 AppImage 安裝的。
2. **套件名稱不同，或軟體庫未正確配置**。雖然對 Outline 而言可能性較低，但其他軟體可能會出現這種情況。

根據您之前的操作，您很可能是以 **AppImage** 形式安裝的。在這種情況下，您需要手動移除它。

請按以下步驟操作：

**1. 尋找並刪除 AppImage 檔案：**

當 Outline 用戶端以 AppImage 形式安裝時，通常只是一個單獨的可執行檔。您可能將其下載到 `Downloads` 資料夾，或可能移動到您家目錄中的 `bin` 或 `Applications` 資料夾。

* **常見的檢查位置：**
    * `~/Downloads/`
    * `~/Applications/`（如果您曾建立此資料夾）
    * `~/bin/`（如果您曾建立此資料夾）
    * 您最初執行它的目錄。

* **如何尋找：** 您可以使用 `find` 指令在家目錄中搜尋：
    ```bash
    find ~ -name "Outline-Client*.AppImage" 2>/dev/null
    ```
    此指令會在家目錄中搜尋任何以 "Outline-Client" 開頭且以 ".AppImage" 結尾的檔案。
    找到後，將其刪除：
    ```bash
    rm /path/to/Outline-Client.AppImage
    ```
    （請將 `/path/to/` 替換為 `find` 指令找到的實際路徑。）

**2. 移除殘留的配置檔案和自動啟動檔案：**

即使您刪除了 AppImage，Outline 可能仍建立了一些配置檔案和自動啟動項目。

* **移除配置目錄：**
    ```bash
    rm -rf ~/.config/Outline/
    ```
    此指令會移除您用戶配置資料夾內的整個 `Outline` 目錄。

* **移除自動啟動項目（如果有的話）：**
    如果 Outline 被設定為在您登入時自動啟動，可能會有一個對應的 `.desktop` 檔案。
    ```bash
    rm -f ~/.config/autostart/Outline-Client.AppImage.desktop
    ```

* **移除桌面圖示（如果有的話）：**
    有時 AppImage 會在您的本機圖示目錄中建立桌面圖示。
    ```bash
    find ~/.local/share/icons -name "appimagekit-outline-client*.png" -delete
    ```
    這將刪除與 Outline AppImage 相關的任何 PNG 圖示。

**3. 檢查並恢復網路配置（如有需要）：**

與其他 VPN 一樣，Outline 可能會修改您的 DNS 設定。如果在移除 AppImage 後遇到網路連線問題，請檢查您的 `/etc/resolv.conf` 檔案。

* **檢查 `resolv.conf`：**
    ```bash
    cat /etc/resolv.conf
    ```
    尋找看起來像是 Outline 所加入的行（例如，您不認識的特定名稱伺服器 IP 位址，而非您的路由器或 ISP 的 DNS）。

* **還原 `resolv.conf`（如果需要）：**
    如果看起來 Outline 修改了它：
    * **選項 A（適用於現代 Ubuntu 的推薦方法）：** 如果您的系統使用 `systemd-resolved`（在近期的 Ubuntu 版本中很常見），通常可以透過重新建立符號連結來修復：
        ```bash
        sudo rm /etc/resolv.conf
        sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
        ```
    * **選項 B（手動編輯 - 如果選項 A 無效或適用於舊系統）：**
        首先，建立備份：
        ```bash
        sudo cp /etc/resolv.conf /etc/resolv.conf.bak
        ```
        然後，編輯該檔案：
        ```bash
        sudo nano /etc/resolv.conf
        ```
        將任何由 Outline 加入的 `nameserver` 行註解掉或移除。如果不確定您的 ISP 的 DNS，通常可以填入公共 DNS 伺服器，例如 Google 的 (`8.8.8.8` 和 `8.8.4.4`) 或 Cloudflare 的 (`1.1.1.1` 和 `1.0.0.1`)。

**4. 重新啟動系統：**

完成這些步驟後，強烈建議您重新啟動 Ubuntu 系統，以確保所有變更生效，並且與 Outline 相關的任何背景程序完全終止。

```bash
sudo reboot
```

按照這些手動移除步驟操作，您應該能夠從 Ubuntu 系統中完全移除 Outline VPN 用戶端。