---
audio: false
generated: true
lang: de
layout: post
title: Ubuntu Linux Hardware-Informationen
translated: true
type: note
---

Um umfassende Informationen über die Hardware Ihres Laptops (RAM, CPU usw.) auf einem Ubuntu-Linux-System zu erhalten, können Sie eine Kombination aus Terminalbefehlen und Tools verwenden. Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zum Abrufen detaillierter Systeminformationen:

---

### 1. CPU-Informationen überprüfen
Um Details zu Ihrer CPU (Prozessortyp, Geschwindigkeit, Kerne usw.) zu erhalten:
- Öffnen Sie ein Terminal (Strg + Alt + T).
- Führen Sie den folgenden Befehl aus:
  ```bash
  lscpu
  ```
  - **Ausgabe**: Zeigt die CPU-Architektur, Anzahl der Kerne, Threads, Taktrate, Cache-Größen usw. an.
- Für detailliertere CPU-Informationen, einschließlich des Modellnamens:
  ```bash
  cat /proc/cpuinfo
  ```
  - Suchen Sie nach Feldern wie `model name`, `cpu MHz` und `cpu cores`.

---

### 2. RAM-Informationen überprüfen
Um den gesamten und verwendeten Arbeitsspeicher anzuzeigen:
- Führen Sie aus:
  ```bash
  free -h
  ```
  - **Ausgabe**: Zeigt den gesamten, verwendeten und freien Speicher in einem menschenlesbaren Format an (z.B. GB oder MB).
- Für detaillierte Speicherinformationen (z.B. Typ, Geschwindigkeit und Steckplätze):
  ```bash
  sudo dmidecode -t memory
  ```
  - **Ausgabe**: Bietet Details zum physischen Speicher, wie Größe, Typ (z.B. DDR4), Geschwindigkeit und Steckplatzbelegung. Erfordert Root-Rechte.

---

### 3. Speicherinformationen (HDD/SSD) überprüfen
Um Details zu Ihren Speichergeräten zu erhalten:
- Führen Sie aus:
  ```bash
  lsblk
  ```
  - **Ausgabe**: Listet alle Blockgeräte (z.B. SSD, HDD) mit deren Größen und Einhängepunkten auf.
- Für detaillierte Informationen zu Festplatten:
  ```bash
  sudo fdisk -l
  ```
  - **Ausgabe**: Zeigt Festplattenpartitionen und -größen an. Erfordert Root-Rechte.
- Um den Festplattentyp (z.B. HDD oder SSD) und das Modell zu überprüfen:
  ```bash
  sudo hdparm -I /dev/sda
  ```
  - Ersetzen Sie `/dev/sda` durch Ihr Festplattengerät (finden Sie es mit `lsblk`).

---

### 4. GPU-Informationen (Grafikkarte) überprüfen
Um Details zu Ihrer Grafikkarte zu finden:
- Führen Sie aus:
  ```bash
  lspci | grep -i vga
  ```
  oder
  ```bash
  lspci | grep -i nvidia
  ```
  - **Ausgabe**: Zeigt das Grafikkartenmodell an (z.B. Intel, NVIDIA, AMD).
- Für detailliertere GPU-Informationen:
  ```bash
  glxinfo | grep "OpenGL renderer"
  ```
  - Erfordert das Paket `mesa-utils` (`sudo apt install mesa-utils`, falls nicht installiert).
- Für NVIDIA-GPUs verwenden Sie:
  ```bash
  nvidia-smi
  ```
  - **Ausgabe**: Zeigt die GPU-Auslastung, Treiberversion und den VRAM an (falls NVIDIA-Treiber installiert sind).

---

### 5. Systemübersicht überprüfen
Für einen umfassenden Überblick über Ihr System (CPU, RAM, Motherboard usw.):
- Führen Sie aus:
  ```bash
  sudo lshw
  ```
  - **Ausgabe**: Listet detaillierte Hardwareinformationen auf, einschließlich CPU, RAM, Speicher und mehr. Verwenden Sie `sudo lshw -short` für eine knappe Version.
- Alternativ können Sie `hardinfo` für eine grafische Oberfläche installieren und verwenden:
  ```bash
  sudo apt install hardinfo
  hardinfo
  ```
  - **Ausgabe**: Öffnet eine GUI, die detaillierte Systeminformationen anzeigt (CPU, RAM, Speicher, Sensoren usw.).

---

### 6. BIOS/UEFI- und Motherboard-Informationen überprüfen
Um BIOS/UEFI- und Motherboard-Details zu erhalten:
- Führen Sie aus:
  ```bash
  sudo dmidecode -t bios
  ```
  - **Ausgabe**: Zeigt die BIOS-Version, den Hersteller und das Veröffentlichungsdatum an.
- Für Motherboard-Details:
  ```bash
  sudo dmidecode -t baseboard
  ```
  - **Ausgabe**: Zeigt den Motherboard-Hersteller, das Modell und die Seriennummer an.

---

### 7. Betriebssystem- und Kernel-Details überprüfen
Um Ihre Ubuntu-Version und den Kernel zu überprüfen:
- Führen Sie aus:
  ```bash
  lsb_release -a
  ```
  - **Ausgabe**: Zeigt die Ubuntu-Version und Releasedetails an.
- Für Kernel-Informationen:
  ```bash
  uname -r
  ```
  - **Ausgabe**: Zeigt die Linux-Kernel-Version an.

---

### 8. Systemressourcen in Echtzeit überwachen
Um CPU, RAM und Prozessauslastung in Echtzeit zu überwachen:
- Führen Sie aus:
  ```bash
  top
  ```
  oder
  ```bash
  htop
  ```
  - **Hinweis**: Installieren Sie `htop`, falls nicht vorhanden (`sudo apt install htop`). Es bietet eine benutzerfreundlichere Oberfläche.

---

### 9. Umfassender Systembericht mit `inxi`
Für einen einzelnen Befehl, der umfangreiche Systeminformationen sammelt:
- Installieren Sie `inxi`:
  ```bash
  sudo apt install inxi
  ```
- Führen Sie aus:
  ```bash
  inxi -Fxz
  ```
  - **Ausgabe**: Bietet einen detaillierten Bericht, einschließlich CPU, RAM, GPU, Speicher, Netzwerk und mehr. Das Flag `-F` gibt einen vollständigen Bericht, `-x` fügt zusätzliche Details hinzu und `-z` filtert sensible Informationen.

---

### Beispielausgabe (mit `inxi -Fxz`)
```plaintext
System:    Host: ubuntu-laptop Kernel: 5.15.0-73-generic x86_64 bits: 64 Desktop: GNOME 42.0
           Distro: Ubuntu 22.04.2 LTS (Jammy Jellyfish)
Machine:   Type: Laptop System: Dell product: Inspiron 15 v: N/A serial: <filter>
           Mobo: Dell model: 0XYZ serial: <filter> UEFI: Dell v: 1.2.3 date: 05/10/2023
CPU:       Info: 8-core model: Intel Core i7-12700H bits: 64 type: MT MCP cache: L2: 11.5 MiB
           Speed: 2500 MHz min/max: 400/4700 MHz Core speeds (MHz): 1: 2500 2: 2400 ...
Memory:    RAM: total: 15.5 GiB used: 3.2 GiB (20.6%)
           Array-1: capacity: 32 GiB slots: 2 EC: None
           Device-1: DIMM A size: 8 GiB speed: 3200 MT/s type: DDR4
           Device-2: DIMM B size: 8 GiB speed: 3200 MT/s type: DDR4
Graphics:  Device-1: Intel Alder Lake-P Integrated Graphics driver: i915 v: kernel
           Device-2: NVIDIA GA107M [GeForce RTX 3050 Mobile] driver: nvidia v: 535.54.03
           Display: x11 server: X.Org v: 1.21.1.4 driver: X: loaded: modesetting,nvidia
           OpenGL: renderer: Mesa Intel UHD Graphics (ADL-S GT2) v: 4.6 Mesa 23.0.4
Drives:    Local Storage: total: 512 GiB used: 120 GiB (23.4%)
           ID-1: /dev/nvme0n1 vendor: Samsung model: SSD 970 EVO Plus 500GB size: 512 GiB
...
```

---

### Hinweise
- Einige Befehle (z.B. `dmidecode`, `fdisk`) erfordern Root-Rechte (`sudo`).
- Wenn ein Befehl nicht installiert ist (z.B. `inxi`, `htop`, `mesa-utils`), installieren Sie ihn mit `sudo apt install <paketname>`.
- Für ein grafisches Tool können `hardinfo` oder `gnome-system-monitor` (vorinstalliert auf Ubuntu) eine benutzerfreundliche Oberfläche bieten.
- Wenn Sie spezifische Details benötigen (z.B. Batterieinformationen, Netzwerkadapter), lassen Sie es mich wissen, und ich kann zusätzliche Befehle bereitstellen.

Lassen Sie mich wissen, wenn Sie Hilfe bei der Interpretation der Ausgabe benötigen oder sich auf eine bestimmte Komponente konzentrieren möchten!