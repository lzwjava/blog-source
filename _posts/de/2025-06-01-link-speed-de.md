---
audio: false
generated: true
lang: de
layout: post
title: Ethernet-Verbindungsgeschwindigkeit in Ubuntu überprüfen
translated: true
type: note
---

In Ubuntu können Sie die Ethernet-Linkgeschwindigkeit mit verschiedenen Befehlszeilen-Tools überprüfen. Hier sind die gängigsten Methoden:

### **1. Verwendung von `ethtool` (Empfohlen)**
`ethtool` ist die zuverlässigste Methode, um die aktuelle Linkgeschwindigkeit Ihrer Ethernet-Schnittstelle zu überprüfen.

#### Installieren Sie `ethtool` (falls nicht bereits installiert):
```bash
sudo apt install ethtool
```

#### Überprüfen Sie die Linkgeschwindigkeit:
```bash
sudo ethtool <Interface_Name>
```
Ersetzen Sie `<Interface_Name>` durch den Namen Ihrer Ethernet-Schnittstelle (z.B. `eth0`, `enp3s0`, `ens33`).

#### Beispiel:
```bash
sudo ethtool enp3s0
```
Suchen Sie nach den Feldern `Speed` und `Duplex` in der Ausgabe:
```
Settings for enp3s0:
    Supported ports: [ TP ]
    Supported link modes:   10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Supported pause frame use: No
    Supports auto-negotiation: Yes
    Supported FEC modes: Not reported
    Advertised link modes:  10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Advertised pause frame use: No
    Advertised auto-negotiation: Yes
    Advertised FEC modes: Not reported
    Speed: 1000Mb/s   # <--- Dies ist Ihre aktuelle Linkgeschwindigkeit
    Duplex: Full      # <--- Full oder Half Duplex
    Port: Twisted Pair
    PHYAD: 1
    Transceiver: internal
    Auto-negotiation: on
    MDI-X: on (auto)
    Supports Wake-on: pumbg
    Wake-on: d
    Current message level: 0x00000007 (7)
                           drv probe link
    Link detected: yes      # <--- Zeigt an, ob das Kabel verbunden ist
```

---

### **2. Verwendung von `ip` oder `ifconfig` (Grundlegende Informationen)**
Diese Befehle zeigen, ob die Schnittstelle aktiv ist, zeigen aber nicht direkt die Linkgeschwindigkeit an.

#### Verwenden von `ip`:
```bash
ip link show <Interface_Name>
```
Beispiel:
```bash
ip link show enp3s0
```
(Zeigt keine Geschwindigkeit, nur den Link-Status.)

#### Verwenden von `ifconfig` (veraltet, aber noch im Gebrauch):
```bash
ifconfig <Interface_Name>
```
Beispiel:
```bash
ifconfig enp3s0
```
(Zeigt, ob die Schnittstelle aktiv ist, aber nicht die Geschwindigkeit.)

---

### **3. Verwendung von `dmesg` (Treiber-Protokolle überprüfen)**
Manchmal protokolliert der Ethernet-Treiber die ausgehandelte Geschwindigkeit während der Initialisierung.
```bash
dmesg | grep <Interface_Name>
```
Beispiel:
```bash
dmesg | grep enp3s0
```
Suchen Sie nach Zeilen wie:
```
[    5.123456] e1000e: enp3s0 NIC Link is Up 1000 Mbps Full Duplex
```

---

### **4. Verwendung von `mii-tool` (Ältere Systeme)**
Für sehr alte Systeme könnte `mii-tool` funktionieren:
```bash
sudo apt install net-tools
sudo mii-tool -v <Interface_Name>
```
Beispiel:
```bash
sudo mii-tool -v eth0
```
(Nicht empfohlen für modernes Gigabit-Ethernet.)

---

### **Zusammenfassung**
- **Beste Methode:** `sudo ethtool <Interface>` (zeigt Geschwindigkeit, Duplex, Auto-Negotiation).
- **Alternative:** Überprüfen Sie `dmesg`-Protokolle, falls `ethtool` nicht verfügbar ist.
- **Grundlegender Status:** `ip link show` oder `ifconfig` (zeigt keine Geschwindigkeit an).

Let me know if you need further clarification! 🚀