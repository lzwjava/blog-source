---
audio: false
generated: true
lang: de
layout: post
title: Installieren von qBittorrent auf Ubuntu
translated: true
type: note
---

Die Installation von qBittorrent auf Ubuntu ist unkompliziert. Hier sind die Schritte:

### **Methode 1: qBittorrent über APT installieren (Empfohlen)**
1. **Aktualisieren Sie Ihre Paketliste**:
   ```bash
   sudo apt update
   ```

2. **Installieren Sie qBittorrent**:
   ```bash
   sudo apt install qbittorrent
   ```

3. **Starten Sie qBittorrent**:
   - Über das Terminal:
     ```bash
     qbittorrent
     ```
   - Oder suchen Sie nach "qBittorrent" im Ubuntu-Anwendungsmenü.

---

### **Methode 2: Die neueste Version über PPA installieren (Optional)**
Wenn Sie eine neuere Version wünschen, als die Standard-Repositorys von Ubuntu bieten, können Sie das offizielle PPA verwenden:

1. **Fügen Sie das qBittorrent PPA hinzu**:
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **Paketlisten aktualisieren**:
   ```bash
   sudo apt update
   ```

3. **Installieren Sie qBittorrent**:
   ```bash
   sudo apt install qbittorrent
   ```

4. **Starten Sie qBittorrent**:
   ```bash
   qbittorrent
   ```

---

### **Methode 3: qBittorrent über Flatpak installieren (Alternative)**
Wenn Sie Flatpak bevorzugen:

1. **Installieren Sie Flatpak (falls noch nicht installiert)**:
   ```bash
   sudo apt install flatpak
   ```

2. **Fügen Sie das Flathub-Repository hinzu**:
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **Installieren Sie qBittorrent**:
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **Starten Sie qBittorrent**:
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **Deinstallation von qBittorrent (falls benötigt)**
- **Bei Installation über APT oder PPA**:
  ```bash
   sudo apt remove qbittorrent
   ```
- **Bei Installation über Flatpak**:
   ```bash
   flatpak uninstall org.qbittorrent.qBittorrent
   ```

Das war's! Sie haben qBittorrent nun auf Ubuntu installiert. 🚀 Lass mich wissen, wenn du Hilfe benötigst!