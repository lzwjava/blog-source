---
audio: false
generated: true
lang: fr
layout: post
title: Informations système sur macOS
translated: true
---

Pour obtenir des informations système sur votre macOS, vous pouvez utiliser plusieurs outils et commandes intégrés. Voici quelques méthodes pour récupérer divers types d'informations système :

### 1. **Utilitaire d'informations système**
L'application Informations système fournit une vue d'ensemble complète du matériel et du logiciel de votre Mac.

- Ouvrez **Recherche Spotlight** en appuyant sur `Cmd + Space` et tapez "Informations système", puis appuyez sur Entrée.
- Alternativement, vous pouvez l'ouvrir depuis le **menu Apple** > **À propos de ce Mac** > **Rapport système**.

### 2. **À propos de ce Mac**
Cela fournit un aperçu rapide des spécifications de votre Mac.

- Cliquez sur le **menu Apple** dans le coin supérieur gauche de l'écran.
- Sélectionnez **À propos de ce Mac**. Cela affichera des informations de base comme la version de macOS, le processeur, la mémoire et le numéro de série.

### 3. **Commandes Terminal**
Vous pouvez utiliser le Terminal pour obtenir des informations système détaillées à l'aide de diverses commandes.

- Ouvrez **Terminal** depuis `Applications` > `Utilitaires` > `Terminal` ou en le recherchant dans Spotlight.

#### Informations système de base
```sh
system_profiler SPHardwareDataType
```

#### Informations système détaillées
```sh
system_profiler
```

#### Informations sur le CPU
```sh
sysctl -n machdep.cpu.brand_string
```

#### Informations sur la mémoire
```sh
sysctl hw.memsize
```

#### Utilisation du disque
```sh
df -h
```

#### Informations réseau
```sh
ifconfig
```

#### Informations sur la batterie (pour les ordinateurs portables)
```sh
pmset -g batt
```

#### Liste des logiciels installés
```sh
ls /Applications
```

#### Version de macOS
```sh
sw_vers
```

#### Informations utilisateur
```sh
id
```

#### Liste des processus en cours d'exécution
```sh
ps aux
```

#### Liste des paquets Brew installés
```sh
brew list
```

#### Liste des paquets Pip installés
```sh
pip list
```

#### Liste des paquets Gem installés
```sh
gem list
```

### 4. **Moniteur d'activité**
Cette application fournit des informations en temps réel sur l'utilisation du CPU, de la mémoire, de l'énergie, du disque et du réseau de votre Mac.

- Ouvrez **Moniteur d'activité** depuis `Applications` > `Utilitaires` > `Moniteur d'activité` ou en le recherchant dans Spotlight.

### 5. **Utilitaire de disque**
Cette application fournit des informations sur vos périphériques de stockage.

- Ouvrez **Utilitaire de disque** depuis `Applications` > `Utilitaires` > `Utilitaire de disque` ou en le recherchant dans Spotlight.

### 6. **Outils tiers**
Il existe également des applications tierces comme **iStat Menus** et **CoconutBattery** qui fournissent des informations système détaillées et des capacités de surveillance.

En utilisant ces méthodes, vous pouvez recueillir une large gamme d'informations système sur votre macOS.