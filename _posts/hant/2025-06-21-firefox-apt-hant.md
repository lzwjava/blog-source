---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上透過 APT 安裝 Firefox
translated: true
type: note
---

本指南詳細說明如何在 Ubuntu 上從 Mozilla APT 儲存庫安裝 Firefox，以取代預設的 Snap 套件。

**為何選擇 APT 版本？**

雖然 Snap 版本使用方便，但部分使用者偏好 APT 版本以獲得更好的整合性與效能表現。

**安裝步驟：**

1.  **解除安裝 Firefox Snap：**

    ```bash
    sudo snap remove firefox
    ```

2.  **建立 APT 金鑰環目錄（如尚未存在）：**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **匯入 Mozilla APT 儲存庫簽署金鑰：**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *若系統缺少 `wget`，請先執行安裝：`sudo apt install wget`*

4.  **將 Mozilla 儲存庫加入軟體來源清單：**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **設定套件優先級以優先選用 Mozilla DEB：**

    此設定可避免 Ubuntu 的過渡套件重新安裝 Snap 版本。

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **移除 Ubuntu Firefox DEB（如已存在）並安裝 Mozilla 版本：**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

現在您已透過官方 Mozilla APT 儲存庫完成 Firefox 安裝！