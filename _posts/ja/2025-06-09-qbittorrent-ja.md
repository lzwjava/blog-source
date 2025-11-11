---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuにqBittorrentをインストールする方法
translated: true
type: note
---

UbuntuにqBittorrentをインストールする方法は簡単です。以下の手順に従ってください。

### **方法1: APT経由でqBittorrentをインストール（推奨）**
1. **パッケージリストを更新**:
   ```bash
   sudo apt update
   ```

2. **qBittorrentをインストール**:
   ```bash
   sudo apt install qbittorrent
   ```

3. **qBittorrentを起動**:
   - ターミナルから:
     ```bash
     qbittorrent
     ```
   - またはUbuntuのアプリケーションメニューで「qBittorrent」を検索。

---

### **方法2: PPA経由で最新版をインストール（オプション）**
Ubuntuのデフォルトリポジトリより新しいバージョンが必要な場合は、公式PPAを使用できます:

1. **qBittorrent PPAを追加**:
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **パッケージリストを更新**:
   ```bash
   sudo apt update
   ```

3. **qBittorrentをインストール**:
   ```bash
   sudo apt install qbittorrent
   ```

4. **qBittorrentを実行**:
   ```bash
   qbittorrent
   ```

---

### **方法3: Flatpak経由でqBittorrentをインストール（代替方法）**
Flatpakを優先する場合:

1. **Flatpakをインストール（未インストールの場合）**:
   ```bash
   sudo apt install flatpak
   ```

2. **Flathubリポジトリを追加**:
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **qBittorrentをインストール**:
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **qBittorrentを実行**:
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **qBittorrentのアンインストール（必要な場合）**
- **APTまたはPPA経由でインストールした場合**:
  ```bash
  sudo apt remove qbittorrent
  ```
- **Flatpak経由でインストールした場合**:
  ```bash
  flatpak uninstall org.qbittorrent.qBittorrent
  ```

以上です！これでUbuntuにqBittorrentがインストールされました。🚀 何かヘルプが必要な場合はお知らせください！