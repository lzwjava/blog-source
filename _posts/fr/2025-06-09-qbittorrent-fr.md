---
audio: false
generated: true
lang: fr
layout: post
title: Installer qBittorrent sur Ubuntu
translated: true
type: note
---

L'installation de qBittorrent sur Ubuntu est simple. Voici les étapes :

### **Méthode 1 : Installer qBittorrent via APT (Recommandée)**
1. **Mettre à jour la liste des paquets** :
   ```bash
   sudo apt update
   ```

2. **Installer qBittorrent** :
   ```bash
   sudo apt install qbittorrent
   ```

3. **Lancer qBittorrent** :
   - Depuis le terminal :
     ```bash
     qbittorrent
     ```
   - Ou recherchez "qBittorrent" dans le menu des applications Ubuntu.

---

### **Méthode 2 : Installer la dernière version via PPA (Optionnelle)**
Si vous voulez une version plus récente que celle fournie par le dépôt par défaut d'Ubuntu, vous pouvez utiliser le PPA officiel :

1. **Ajouter le PPA qBittorrent** :
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **Mettre à jour les listes de paquets** :
   ```bash
   sudo apt update
   ```

3. **Installer qBittorrent** :
   ```bash
   sudo apt install qbittorrent
   ```

4. **Exécuter qBittorrent** :
   ```bash
   qbittorrent
   ```

---

### **Méthode 3 : Installer qBittorrent via Flatpak (Alternative)**
Si vous préférez Flatpak :

1. **Installer Flatpak (s'il n'est pas déjà installé)** :
   ```bash
   sudo apt install flatpak
   ```

2. **Ajouter le dépôt Flathub** :
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **Installer qBittorrent** :
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **Exécuter qBittorrent** :
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **Désinstaller qBittorrent (si nécessaire)**
- **Si installé via APT ou PPA** :
  ```bash
   sudo apt remove qbittorrent
   ```
- **Si installé via Flatpak** :
  ```bash
   flatpak uninstall org.qbittorrent.qBittorrent
   ```

C'est fait ! Vous avez maintenant qBittorrent installé sur Ubuntu. 🚀 Faites-moi savoir si vous avez besoin d'aide !