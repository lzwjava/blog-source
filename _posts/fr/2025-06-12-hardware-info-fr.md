---
audio: false
generated: true
lang: fr
layout: post
title: Informations Matérielles Ubuntu Linux
translated: true
type: note
---

Pour obtenir des informations complètes sur le matériel de votre ordinateur portable (RAM, CPU, etc.) sur un système Ubuntu Linux, vous pouvez utiliser une combinaison de commandes et d'outils en terminal. Voici un guide étape par étape pour récupérer des informations détaillées sur le système :

---

### 1. Vérifier les informations du CPU
Pour obtenir les détails sur votre CPU (type de processeur, vitesse, cœurs, etc.) :
- Ouvrez un terminal (Ctrl + Alt + T).
- Exécutez la commande suivante :
  ```bash
  lscpu
  ```
  - **Sortie** : Affiche l'architecture du CPU, le nombre de cœurs, de threads, la vitesse d'horloge, la taille des caches, etc.
- Pour des informations CPU plus détaillées, incluant le nom du modèle :
  ```bash
  cat /proc/cpuinfo
  ```
  - Recherchez les champs comme `model name`, `cpu MHz` et `cpu cores`.

---

### 2. Vérifier les informations de la RAM (Mémoire)
Pour visualiser la RAM totale et utilisée :
- Exécutez :
  ```bash
  free -h
  ```
  - **Sortie** : Affiche la mémoire totale, utilisée et libre dans un format lisible (par ex., Go ou Mo).
- Pour des informations détaillées sur la mémoire (par ex., type, vitesse et emplacements) :
  ```bash
  sudo dmidecode -t memory
  ```
  - **Sortie** : Fournit des détails sur la mémoire physique, comme la taille, le type (par ex., DDR4), la vitesse et l'utilisation des emplacements. Nécessite les privilèges root.

---

### 3. Vérifier les informations du stockage (HDD/SSD)
Pour obtenir des détails sur vos périphériques de stockage :
- Exécutez :
  ```bash
  lsblk
  ```
  - **Sortie** : Liste tous les périphériques de bloc (par ex., SSD, HDD) avec leurs tailles et points de montage.
- Pour des informations détaillées sur les disques :
  ```bash
  sudo fdisk -l
  ```
  - **Sortie** : Affiche les partitions des disques et leurs tailles. Nécessite les privilèges root.
- Pour vérifier le type de disque (par ex., HDD ou SSD) et le modèle :
  ```bash
  sudo hdparm -I /dev/sda
  ```
  - Remplacez `/dev/sda` par votre périphérique de disque (trouvez-le en utilisant `lsblk`).

---

### 4. Vérifier les informations du GPU (Carte graphique)
Pour trouver les détails sur votre carte graphique :
- Exécutez :
  ```bash
  lspci | grep -i vga
  ```
  ou
  ```bash
  lspci | grep -i nvidia
  ```
  - **Sortie** : Affiche le modèle de la carte graphique (par ex., Intel, NVIDIA, AMD).
- Pour des informations GPU plus détaillées :
  ```bash
  glxinfo | grep "OpenGL renderer"
  ```
  - Nécessite le paquet `mesa-utils` (`sudo apt install mesa-utils` s'il n'est pas installé).
- Pour les GPU NVIDIA, utilisez :
  ```bash
  nvidia-smi
  ```
  - **Sortie** : Affiche l'utilisation du GPU, la version du pilote et la VRAM (si les pilotes NVIDIA sont installés).

---

### 5. Vérifier l'Aperçu du Système
Pour un aperçu complet de votre système (CPU, RAM, carte mère, etc.) :
- Exécutez :
  ```bash
  sudo lshw
  ```
  - **Sortie** : Liste les informations matérielles détaillées, incluant le CPU, la RAM, le stockage et plus. Utilisez `sudo lshw -short` pour une version concise.
- Alternativement, installez et utilisez `hardinfo` pour une interface graphique :
  ```bash
  sudo apt install hardinfo
  hardinfo
  ```
  - **Sortie** : Ouvre une interface graphique montrant des informations système détaillées (CPU, RAM, stockage, capteurs, etc.).

---

### 6. Vérifier les informations du BIOS/UEFI et de la Carte Mère
Pour obtenir les détails du BIOS/UEFI et de la carte mère :
- Exécutez :
  ```bash
  sudo dmidecode -t bios
  ```
  - **Sortie** : Affiche la version du BIOS, le vendeur et la date de sortie.
- Pour les détails de la carte mère :
  ```bash
  sudo dmidecode -t baseboard
  ```
  - **Sortie** : Affiche le fabricant de la carte mère, le modèle et le numéro de série.

---

### 7. Vérifier les détails du Système d'Exploitation et du Noyau
Pour vérifier votre version d'Ubuntu et le noyau :
- Exécutez :
  ```bash
  lsb_release -a
  ```
  - **Sortie** : Affiche la version d'Ubuntu et les détails de la release.
- Pour les informations du noyau :
  ```bash
  uname -r
  ```
  - **Sortie** : Affiche la version du noyau Linux.

---

### 8. Surveiller les Ressources Système en Temps Réel
Pour surveiller l'utilisation du CPU, de la RAM et des processus en temps réel :
- Exécutez :
  ```bash
  top
  ```
  ou
  ```bash
  htop
  ```
  - **Note** : Installez `htop` s'il n'est pas présent (`sudo apt install htop`). Il fournit une interface plus conviviale.

---

### 9. Rapport Système Complet avec `inxi`
Pour une commande unique qui rassemble des informations système étendues :
- Installez `inxi` :
  ```bash
  sudo apt install inxi
  ```
- Exécutez :
  ```bash
  inxi -Fxz
  ```
  - **Sortie** : Fournit un rapport détaillé incluant le CPU, la RAM, le GPU, le stockage, le réseau et plus. L'option `-F` donne un rapport complet, `-x` ajoute des détails supplémentaires et `-z` filtre les informations sensibles.

---

### Exemple de Sortie (Utilisant `inxi -Fxz`)
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

### Notes
- Certaines commandes (par ex., `dmidecode`, `fdisk`) nécessitent les privilèges root (`sudo`).
- Si une commande n'est pas installée (par ex., `inxi`, `htop`, `mesa-utils`), installez-la en utilisant `sudo apt install <nom-du-paquet>`.
- Pour un outil graphique, `hardinfo` ou `gnome-system-monitor` (pré-installé sur Ubuntu) peut fournir une interface conviviale.
- Si vous avez besoin de détails spécifiques (par ex., informations sur la batterie, adaptateurs réseau), faites-le-moi savoir et je peux fournir des commandes supplémentaires.

N'hésitez pas à me demander de l'aide pour interpréter la sortie ou si vous souhaitez vous concentrer sur un composant spécifique !