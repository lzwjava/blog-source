---
audio: false
generated: true
lang: de
layout: post
title: Behebung von Wi-Fi-Verbindungsabbrüchen unter Ubuntu
translated: true
type: note
---

Wi-Fi-Verbindungsabbrüche unter Ubuntu, während kabelgebundene Verbindungen stabil bleiben, können durch mehrere Faktoren verursacht werden. Hier ist eine Schritt-für-Schritt-Anleitung zur Diagnose und Behebung des Problems:

---

### **1. Treiberprobleme überprüfen**
Ihr MSI B760M Mortar WiFi Mainboard verwendet wahrscheinlich eine **Intel Wi-Fi 6E AX211/AX210** Karte. Obwohl Intel-Treiber unter Linux generell gut unterstützt werden, können dennoch Probleme auftreten.

#### **Schritte:**
- **Identifizieren Sie Ihren Wi-Fi-Chipsatz:**  
  Führen Sie im Terminal aus:  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  Suchen Sie nach dem Wi-Fi-Adapter (wahrscheinlich `Intel Corporation Device [8086:...]`).

- **Überprüfen Sie, ob der korrekte Treiber geladen ist:**  
  ```bash
  lsmod | grep iwlwifi
  ```
  Wenn nichts angezeigt wird, ist der Treiber nicht geladen.

- **Treiber installieren/aktualisieren:**  
  Intel Wi-Fi-Treiber (`iwlwifi`) sind im Linux-Kernel enthalten, aber Sie benötigen möglicherweise Firmware-Updates:
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. Energiesparmodus für Wi-Fi deaktivieren**
Linux fährt die Wi-Fi-Karte manchmal aggressiv herunter, um Energie zu sparen, was zu Abbrüchen führen kann.

#### **Schritte:**
- Energiesparmodus vorübergehend deaktivieren:  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  Oder manuell überprüfen mit:
  ```bash
  iw dev wlan0 get power_save
  ```
  (Ersetzen Sie `wlan0` mit Ihrem Interface-Namen von `ip a`.)

- **Änderungen übernehmen:**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. Auf Interferenzen oder Router-Probleme prüfen**
- **Testen Sie mit einem anderen Gerät** (Telefon/Laptop), um zu sehen, ob das Problem bestehen bleibt.
- **Wechseln Sie den Wi-Fi-Kanal** (verwenden Sie `iwlist`, um überlastete Kanäle zu scannen):
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- Probieren Sie das **5GHz-Band** (falls verfügbar) für weniger Interferenzen.

---

### **4. IPv6 deaktivieren**
Einige Router/ISPs haben IPv6-Kompatibilitätsprobleme.

#### **Schritte:**
- Bearbeiten Sie `/etc/sysctl.conf` und fügen Sie hinzu:
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- Anwenden:
  ```bash
  sudo sysctl -p
  ```

---

### **5. Kernel & NetworkManager aktualisieren**
Neuere Kernel beheben oft Wi-Fi-Probleme.
```bash
sudo apt update && sudo apt upgrade
```
Falls nötig, installieren Sie einen **Mainline-Kernel** (z.B. 6.5+):
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. Hardware-Verschlüsselung deaktivieren (falls zutreffend)**
Einige Intel Wi-Fi-Karten haben Probleme mit Hardware-Verschlüsselung.  
Bearbeiten Sie `/etc/modprobe.d/iwlwifi.conf` (erstellen, falls nicht vorhanden):
```plaintext
options iwlwifi 11n_disable=1
```
Dann:
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. Auf RFKill oder blockiertes Wi-Fi prüfen**
```bash
rfkill list
```
Wenn Wi-Fi blockiert ist (z.B. `soft blocked: yes`), entsperren Sie es:
```bash
sudo rfkill unblock wifi
```

---

### **8. Mit einem USB-Wi-Fi-Adapter testen**
Wenn das Problem bestehen bleibt, versuchen Sie einen **Linux-kompatiblen USB-Wi-Fi-Adapter** (z.B. TP-Link Archer T4U), um zu isolieren, ob das Problem bei der Intel-Karte liegt.

---

### **9. Logs auf Fehler überprüfen**
```bash
journalctl -u NetworkManager --no-pager -n 50
```
Suchen Sie nach `iwlwifi`-Fehlern oder Trennung-Ereignissen.

---

### **Abschließende Hinweise**
- Wenn nichts davon funktioniert, erwägen Sie **Dual-Boot mit Windows**, um zu prüfen, ob das Problem hardwarebedingt ist.
- Alternativ verwenden Sie einen **USB-zu-Ethernet-Adapter**, falls Wi-Fi weiterhin unzuverlässig bleibt.

Lassen Sie mich wissen, wenn Sie weitere Debugging-Hilfe benötigen!