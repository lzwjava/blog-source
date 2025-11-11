---
audio: false
generated: true
lang: es
layout: post
title: Instalar qBittorrent en Ubuntu
translated: true
type: note
---

Instalar qBittorrent en Ubuntu es sencillo. Aquí están los pasos:

### **Método 1: Instalar qBittorrent via APT (Recomendado)**
1. **Actualiza tu lista de paquetes**:
   ```bash
   sudo apt update
   ```

2. **Instala qBittorrent**:
   ```bash
   sudo apt install qbittorrent
   ```

3. **Inicia qBittorrent**:
   - Desde la terminal:
     ```bash
     qbittorrent
     ```
   - O busca "qBittorrent" en el menú de aplicaciones de Ubuntu.

---

### **Método 2: Instalar la versión más reciente via PPA (Opcional)**
Si quieres una versión más nueva que la que proporciona el repositorio por defecto de Ubuntu, puedes usar el PPA oficial:

1. **Añade el PPA de qBittorrent**:
   ```bash
   sudo add-apt-repository ppa:qbittorrent-team/qbittorrent-stable
   ```

2. **Actualiza las listas de paquetes**:
   ```bash
   sudo apt update
   ```

3. **Instala qBittorrent**:
   ```bash
   sudo apt install qbittorrent
   ```

4. **Ejecuta qBittorrent**:
   ```bash
   qbittorrent
   ```

---

### **Método 3: Instalar qBittorrent via Flatpak (Alternativa)**
Si prefieres Flatpak:

1. **Instala Flatpak (si aún no está instalado)**:
   ```bash
   sudo apt install flatpak
   ```

2. **Añade el repositorio Flathub**:
   ```bash
   flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
   ```

3. **Instala qBittorrent**:
   ```bash
   flatpak install flathub org.qbittorrent.qBittorrent
   ```

4. **Ejecuta qBittorrent**:
   ```bash
   flatpak run org.qbittorrent.qBittorrent
   ```

---

### **Desinstalar qBittorrent (si es necesario)**
- **Si se instaló via APT o PPA**:
  ```bash
  sudo apt remove qbittorrent
  ```
- **Si se instaló via Flatpak**:
  ```bash
  flatpak uninstall org.qbittorrent.qBittorrent
  ```

¡Eso es todo! Ya tienes qBittorrent instalado en Ubuntu. 🚀 ¡Avísame si necesitas ayuda!