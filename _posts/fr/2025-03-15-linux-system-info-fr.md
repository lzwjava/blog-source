---
audio: false
generated: true
lang: fr
layout: post
title: Informations Système Linux
translated: true
type: note
---

Sous Ubuntu, vous pouvez récupérer des informations système telles que l'architecture (32 ou 64 bits), la version du système d'exploitation, la quantité de RAM et la taille du disque en utilisant les commandes suivantes. Voici un guide étape par étape :

### 1. Déterminer si le système est 32 bits ou 64 bits
- **Commande** : `uname -m`
- **Explication** : Cette commande affiche le nom du matériel de la machine.
  - Si la sortie est `x86_64`, votre système est **64 bits**.
  - Si la sortie est `i686` ou `i386`, votre système est **32 bits**.
- **Exemple de sortie** :
  ```
  x86_64
  ```
  Cela indique un système 64 bits.

### 2. Obtenir la version du système d'exploitation (OS)
- **Commande** : `lsb_release -a`
- **Explication** : Cette commande fournit des informations détaillées sur la Linux Standard Base (LSB) et la distribution.
  - Recherchez la ligne `Description` pour voir la version d'Ubuntu.
- **Exemple de sortie** :
  ```
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 20.04.3 LTS
  Release:        20.04
  Codename:       focal
  ```
  Ici, le système d'exploitation est **Ubuntu 20.04.3 LTS**.

### 3. Obtenir la taille de la RAM
- **Commande** : `free -h`
- **Explication** : Cette commande affiche l'utilisation de la mémoire dans un format lisible par un humain (par exemple, Go ou Mo).
  - Regardez la colonne `total` sous la ligne `Mem:` pour trouver la RAM totale installée.
- **Exemple de sortie** :
  ```
              total        used        free      shared  buff/cache   available
  Mem:          15Gi       2.3Gi       9.5Gi       300Mi       3.8Gi        12Gi
  Swap:        2.0Gi         0B       2.0Gi
  ```
  Dans ce cas, la RAM totale est de **15 Go**.

### 4. Obtenir la taille du disque
- **Commande** : `lsblk -d -o NAME,SIZE`
- **Explication** : Cette commande liste tous les disques (à l'exclusion des partitions) avec leurs tailles.
  - L'option `-d` garantit que seuls les disques (par exemple, `/dev/sda`) sont affichés, et non leurs partitions.
  - Recherchez le nom du disque (par exemple, `sda`) et sa taille correspondante.
- **Exemple de sortie** :
  ```
  NAME   SIZE
  sda    1T
  sdb    500G
  ```
  Ici, le système a deux disques : `/dev/sda` d'une taille de **1 téraoctet** et `/dev/sdb` de **500 gigaoctets**. Si vous n'avez qu'un seul disque, ce sera typiquement `sda`.

### Notes
- Ces commandes utilisent des outils standard disponibles sous Ubuntu et ne nécessitent aucune installation supplémentaire.
- Pour la taille du disque, si votre système a plusieurs disques, la sortie les listera tous. Typiquement, `/dev/sda` est le disque principal.
- Exécutez ces commandes dans un terminal pour voir les résultats spécifiques à votre système.

Avec ces commandes, vous pouvez rapidement recueillir les informations système essentielles dont vous avez besoin sur votre machine Ubuntu !