---
audio: false
generated: true
lang: zh
layout: post
title: 在 Ubuntu 系统上安装 qBittorrent
translated: true
type: note
---

在 Ubuntu 系统上安装 qBittorrent 非常简单。以下是具体步骤：

### **方法一：通过 APT 安装（推荐）**
1. **更新软件包列表**：
   ```bash
   sudo apt update
   ```

2. **安装 qBittorrent**：
   ```bash
   sudo apt install qbittorrent
   ```

3. **启动 qBittorrent**：
   - 通过终端启动：
     ```bash
     qbittorrent
     ```
   - 或在 Ubuntu 应用程序菜单中搜索 "qBittorrent"

---

### **方法二：通过 PPA 安装最新版本（可选）**
如需比 Ubuntu 默认仓库更新的版本，可使用官方 PPA：

1. **添加 qBittorrent PPA**：
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **更新软件包列表**：
   ```bash
   sudo apt update
   ```

3. **安装 qBittorrent**：
   ```bash
   sudo apt install qbittorrent
   ```

4. **运行 qBittorrent**：
   ```bash
   qbittorrent
   ```

---

### **方法三：通过 Flatpak 安装（替代方案）**
若偏好使用 Flatpak：

1. **安装 Flatpak（如未安装）**：
   ```bash
   sudo apt install flatpak
   ```

2. **添加 Flathub 仓库**：
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **安装 qBittorrent**：
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **运行 qBittorrent**：
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **卸载 qBittorrent（如需要）**
- **通过 APT 或 PPA 安装的版本**：
  ```bash
   sudo apt remove qbittorrent
   ```
- **通过 Flatpak 安装的版本**：
  ```bash
   flatpak uninstall org.qbittorrent.qBittorrent
   ```

完成！现在您已在 Ubuntu 系统上成功安装 qBittorrent。🚀 如需任何帮助请随时告知！