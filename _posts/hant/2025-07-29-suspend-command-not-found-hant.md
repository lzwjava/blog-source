---
audio: false
generated: true
image: false
lang: hant
layout: post
title: 解決暫停指令錯誤
translated: true
type: note
---

錯誤 `sudo: suspend: command not found` 表示您的系統上沒有 `suspend` 指令或未安裝。`suspend` 指令通常用於將 Linux 系統置於暫停（睡眠）狀態，但根據您的發行版，該指令可能預設不存在或有不同名稱。

以下是解決此問題的方法：

### 1. **使用正確的指令**
在許多 Linux 發行版中，暫停系統的指令並非 `suspend`，而是以下其中之一：

- **`systemctl suspend`**：
  這是使用 `systemd` 的系統（例如 Ubuntu、Debian、Fedora 等）的標準指令。
  ```bash
  sudo systemctl suspend
  ```

- **`pm-suspend`**：
  如果您的系統使用 `pm-utils` 套件，可以使用：
  ```bash
  sudo pm-suspend
  ```
  注意：如果未安裝 `pm-utils`，您可能需要先安裝：
  ```bash
  sudo apt-get install pm-utils  # 適用於 Debian/Ubuntu
  sudo dnf install pm-utils      # 適用於 Fedora
  ```

- **`echo mem > /sys/power/state`**：
  若需底層操作，可直接寫入系統電源狀態：
  ```bash
  echo mem | sudo tee /sys/power/state
  ```
  此操作需要 root 權限，且根據核心配置，可能無法在所有系統上運作。

### 2. **檢查 `systemd` 是否可用**
由於 `systemctl suspend` 是現代 Linux 發行版最常用的方法，請驗證 `systemd` 是否正在執行：
```bash
pidof systemd
```
若返回 PID，表示您的系統使用 `systemd`，且 `systemctl suspend` 應可運作。若無，您可能需要使用 `pm-suspend` 或其他方法。

### 3. **安裝缺失工具**
如果 `systemctl` 和 `pm-suspend` 皆不可用，您可能需要安裝相應套件：
- 適用 Ubuntu/Debian：
  ```bash
  sudo apt-get update
  sudo apt-get install pm-utils
  ```
- 適用 Fedora：
  ```bash
  sudo dnf install pm-utils
  ```

### 4. **檢查權限**
確保您擁有足夠權限。`sudo` 指令表示您嘗試以管理員身份執行，但請再次確認您的用戶是否在 `sudoers` 檔案中：
```bash
sudo -l
```
若缺乏權限，您可能需要聯繫系統管理員。

### 5. **替代方案：使用桌面環境**
若您執行圖形桌面環境（例如 GNOME、KDE），可透過 GUI 暫停系統（例如點擊電源選單並選擇「暫停」）。或使用：
- 適用 GNOME：
  ```bash
  gnome-session-quit --power-off
  ```
- 適用 KDE：
  ```bash
  qdbus org.kde.ksmserver /KSMServer org.kde.KSMServerInterface.logout 0 1 0
  ```

### 6. **驗證硬體支援**
部分系統可能因硬體或核心問題而不支援暫停。檢查是否支援暫停功能：
```bash
cat /sys/power/state
```
若輸出中包含 `mem`，表示支援暫停。若無，您可能需要排查硬體或核心設定。

### 7. **若您特別需要 `suspend` 指令**
若您尋找的是特定 `suspend` 指令（例如自訂腳本或套件的一部分），可能未安裝。請搜尋：
```bash
sudo apt-cache search suspend
```
或檢查是否屬於其他套件。若您指的是自訂腳本或別名，請驗證其位置並確保可執行：
```bash
which suspend
```

### 範例工作流程
在典型的 Ubuntu 設定中暫停系統：
```bash
sudo systemctl suspend
```
此操作應使系統進入低功耗睡眠狀態。恢復時，您可能需要解鎖工作階段。

若問題仍存在，請告知您的 Linux 發行版及任何其他設定細節，我將提供更針對性的建議。

[Ubuntu 電源管理文件](https://help.ubuntu.com/stable/ubuntu-help/power-suspend.html)
[systemd suspend 手冊頁](https://www.freedesktop.org/software/systemd/man/systemctl.html)