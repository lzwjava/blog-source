---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 上安裝 qBittorrent
translated: true
type: note
---

在 Ubuntu 上安裝 qBittorrent 非常簡單。以下是步驟：

### **方法一：透過 APT 安裝 qBittorrent（推薦）**
1. **更新套件清單**：
   ```bash
   sudo apt update
   ```

2. **安裝 qBittorrent**：
   ```bash
   sudo apt install qbittorrent
   ```

3. **啟動 qBittorrent**：
   - 從終端機：
     ```bash
     qbittorrent
     ```
   - 或在 Ubuntu 應用程式選單中搜尋「qBittorrent」。

---

### **方法二：透過 PPA 安裝最新版本（可選）**
如果您需要比 Ubuntu 預設儲存庫更新的版本，可以使用官方 PPA：

1. **新增 qBittorrent PPA**：
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **更新套件清單**：
   ```bash
   sudo apt update
   ```

3. **安裝 qBittorrent**：
   ```bash
   sudo apt install qbittorrent
   ```

4. **執行 qBittorrent**：
   ```bash
   qbittorrent
   ```

---

### **方法三：透過 Flatpak 安裝 qBittorrent（替代方案）**
如果您偏好使用 Flatpak：

1. **安裝 Flatpak（如未安裝）**：
   ```bash
   sudo apt install flatpak
   ```

2. **新增 Flathub 儲存庫**：
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **安裝 qBittorrent**：
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **執行 qBittorrent**：
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **解除安裝 qBittorrent（如有需要）**
- **如透過 APT 或 PPA 安裝**：
  ```bash
  sudo apt remove qbittorrent
  ```
- **如透過 Flatpak 安裝**：
  ```bash
  flatpak uninstall org.qbittorrent.qBittorrent
  ```

完成！您現在已經在 Ubuntu 上安裝了 qBittorrent。🚀 如有任何問題，歡迎隨時詢問！