---
audio: false
generated: true
lang: fr
layout: post
title: Résoudre les Coupures Wi-Fi sur Ubuntu
translated: true
type: note
---

Les déconnexions Wi-Fi sur Ubuntu alors que les connexions filaires restent stables peuvent être causées par plusieurs facteurs. Voici un guide étape par étape pour diagnostiquer et résoudre le problème :

---

### **1. Vérifier les problèmes de pilote**
Votre carte mère MSI B760M Mortar WiFi utilise probablement une carte **Intel Wi-Fi 6E AX211/AX210**. Bien que les pilotes Intel soient généralement bien pris en charge sous Linux, des problèmes peuvent survenir.

#### **Étapes :**
- **Identifier votre puce Wi-Fi :**  
  Exécutez dans le terminal :  
  ```bash
  lspci -knn | grep -iA3 net
  ```
  Cherchez l'adaptateur Wi-Fi (probablement `Intel Corporation Device [8086:...]`).

- **Vérifier si le bon pilote est chargé :**  
  ```bash
  lsmod | grep iwlwifi
  ```
  Si rien n'apparaît, le pilote n'est pas chargé.

- **Installer/Mettre à jour les pilotes :**  
  Les pilotes Wi-Fi Intel (`iwlwifi`) sont inclus dans le noyau Linux, mais vous pourriez avoir besoin de mises à jour du firmware :
  ```bash
  sudo apt update && sudo apt install --reinstall linux-firmware
  ```

---

### **2. Désactiver l'économie d'énergie pour le Wi-Fi**
Linux réduit parfois agressivement la puissance de la carte Wi-Fi pour économiser l'énergie, ce qui provoque des déconnexions.

#### **Étapes :**
- Désactiver temporairement l'économie d'énergie :  
  ```bash
  sudo sed -i 's/wifi.powersave = 3/wifi.powersave = 2/' /etc/NetworkManager/conf.d/default-wifi-powersave-on.conf
  ```
  Ou vérifier manuellement avec :
  ```bash
  iw dev wlan0 get power_save
  ```
  (Remplacez `wlan0` par le nom de votre interface depuis `ip a`.)

- **Appliquer les changements :**  
  ```bash
  sudo systemctl restart NetworkManager
  ```

---

### **3. Vérifier les interférences ou les problèmes de routeur**
- **Tester avec un autre appareil** (téléphone/ordinateur portable) pour voir si le problème persiste.
- **Changer le canal Wi-Fi** (utilisez `iwlist` pour scanner les canaux encombrés) :
  ```bash
  sudo iwlist wlan0 scan | grep Frequency
  ```
- Essayer la **bande 5GHz** (si disponible) pour moins d'interférences.

---

### **4. Désactiver IPv6**
Certains routeurs/FAI ont des problèmes de compatibilité IPv6.

#### **Étapes :**
- Éditez `/etc/sysctl.conf` et ajoutez :
  ```plaintext
  net.ipv6.conf.all.disable_ipv6=1
  net.ipv6.conf.default.disable_ipv6=1
  ```
- Appliquez :
  ```bash
  sudo sysctl -p
  ```

---

### **5. Mettre à jour le noyau et NetworkManager**
Les nouveaux noyaux corrigent souvent les problèmes Wi-Fi.
```bash
sudo apt update && sudo apt upgrade
```
Si nécessaire, installez un **noyau mainline** (par ex. 6.5+) :
```bash
sudo apt install linux-image-generic-hwe-22.04
```

---

### **6. Désactiver le chiffrement matériel (le cas échéant)**
Certaines cartes Wi-Fi Intel ont des problèmes avec le chiffrement matériel.  
Éditez `/etc/modprobe.d/iwlwifi.conf` (créez le fichier s'il n'existe pas) :
```plaintext
options iwlwifi 11n_disable=1
```
Puis :
```bash
sudo modprobe -r iwlwifi && sudo modprobe iwlwifi
```

---

### **7. Vérifier RFKill ou le blocage Wi-Fi**
```bash
rfkill list
```
Si le Wi-Fi est bloqué (par ex., `soft blocked: yes`), débloquez-le :
```bash
sudo rfkill unblock wifi
```

---

### **8. Tester avec un adaptateur Wi-Fi USB**
Si le problème persiste, essayez un **adaptateur Wi-Fi USB compatible Linux** (par ex., TP-Link Archer T4U) pour isoler si le problème vient de la carte Intel.

---

### **9. Vérifier les logs pour les erreurs**
```bash
journalctl -u NetworkManager --no-pager -n 50
```
Cherchez les erreurs `iwlwifi` ou les événements de déconnexion.

---

### **Notes finales**
- Si rien de ce qui précède ne fonctionne, envisagez un **double démarrage avec Windows** pour vérifier si le problème est lié au matériel.
- Alternativement, utilisez un **adaptateur USB vers Ethernet** si le Wi-Fi reste peu fiable.

N'hésitez pas à me dire si vous avez besoin d'aide pour le débogage !