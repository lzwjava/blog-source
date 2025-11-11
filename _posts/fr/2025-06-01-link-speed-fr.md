---
audio: false
generated: true
lang: fr
layout: post
title: Vérifier la vitesse de liaison Ethernet dans Ubuntu
translated: true
type: note
---

Sous Ubuntu, vous pouvez vérifier la vitesse de lien Ethernet en utilisant plusieurs outils en ligne de commande. Voici les méthodes les plus courantes :

### **1. Utilisation de `ethtool` (Recommandé)**
`ethtool` est le moyen le plus fiable pour vérifier la vitesse de lien actuelle de votre interface Ethernet.

#### Installer `ethtool` (s'il n'est pas déjà installé) :
```bash
sudo apt install ethtool
```

#### Vérifier la vitesse de lien :
```bash
sudo ethtool <nom_interface>
```
Remplacez `<nom_interface>` par votre interface Ethernet (par exemple, `eth0`, `enp3s0`, `ens33`).

#### Exemple :
```bash
sudo ethtool enp3s0
```
Recherchez les champs `Speed` et `Duplex` dans la sortie :
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
    Speed: 1000Mb/s   # <--- Ceci est votre vitesse de lien actuelle
    Duplex: Full      # <--- Duplex intégral ou semi-duplex
    Port: Twisted Pair
    PHYAD: 1
    Transceiver: internal
    Auto-negotiation: on
    MDI-X: on (auto)
    Supports Wake-on: pumbg
    Wake-on: d
    Current message level: 0x00000007 (7)
                           drv probe link
    Link detected: yes      # <--- Indique si le câble est connecté
```

---

### **2. Utilisation de `ip` ou `ifconfig` (Informations de base)**
Ces commandes indiquent si l'interface est active mais n'affichent pas directement la vitesse de lien.

#### Utilisation de `ip` :
```bash
ip link show <nom_interface>
```
Exemple :
```bash
ip link show enp3s0
```
(Ne montre pas la vitesse, seulement l'état du lien.)

#### Utilisation de `ifconfig` (obsolète mais encore utilisée) :
```bash
ifconfig <nom_interface>
```
Exemple :
```bash
ifconfig enp3s0
```
(Montre si l'interface est active mais pas la vitesse.)

---

### **3. Utilisation de `dmesg` (Vérifier les journaux du pilote)**
Parfois, le pilote Ethernet enregistre la vitesse négociée lors de l'initialisation.
```bash
dmesg | grep <nom_interface>
```
Exemple :
```bash
dmesg | grep enp3s0
```
Recherchez des lignes comme :
```
[    5.123456] e1000e: enp3s0 NIC Link is Up 1000 Mbps Full Duplex
```

---

### **4. Utilisation de `mii-tool` (Anciens systèmes)**
Pour les systèmes très anciens, `mii-tool` peut fonctionner :
```bash
sudo apt install net-tools
sudo mii-tool -v <nom_interface>
```
Exemple :
```bash
sudo mii-tool -v eth0
```
(Non recommandé pour l'Ethernet Gigabit moderne.)

---

### **Résumé**
- **Meilleure méthode :** `sudo ethtool <interface>` (montre la vitesse, le duplex, la négociation automatique).
- **Alternative :** Vérifiez les journaux `dmesg` si `ethtool` n'est pas disponible.
- **Statut de base :** `ip link show` ou `ifconfig` (ne montre pas la vitesse).

N'hésitez pas à demander si vous avez besoin de précisions supplémentaires ! 🚀