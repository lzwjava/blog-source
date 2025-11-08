---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation de DirB Sans Modifications du Code Source
translated: true
type: note
---

### Alternatives à la modification du code source de DirB

Si la modification du code source (comme `variables.h`) n'est pas une option—peut-être en raison d'une configuration en lecture seule, d'une politique ou simplement d'une préférence—voici des moyens simples pour exécuter DirB sans compilation. Ces méthodes exploitent des paquets pré-construits ou des réimplémentations. Je privilégierai Linux (sur la base de votre chemin de build), mais notez les ajustements spécifiques au système d'exploitation.

#### 1. **Installer via le gestionnaire de paquets (Le plus simple pour Debian/Ubuntu/Kali)**
   DirB est disponible en tant que paquet pré-compilé dans de nombreux dépôts de distro, donc aucun changement de source ou de build n'est nécessaire.
   - **Sur Kali Linux** (recommandé pour les outils de pentesting comme celui-ci) :
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Il est officiellement supporté et maintenu dans les dépôts Kali. [Page des outils Kali](https://www.kali.org/tools/dirb/)
   - **Sur Ubuntu/Debian** :
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - Si non trouvé (les versions plus anciennes pourraient ne pas l'avoir), activez le dépôt universe : `sudo add-apt-repository universe && sudo apt update`.
   - **Vérification** : Exécutez `dirb --help` après l'installation. Les listes de mots se trouvent dans `/usr/share/dirb/wordlists/`.
   - **Pourquoi cela fonctionne** : Les paquets gèrent tous les correctifs (y compris les définitions multiples) en amont.

   Si vous êtes sur une autre distribution :
   - **Fedora/RHEL** : `sudo dnf install dirb` (s'il est dans les dépôts EPEL ; ajoutez EPEL si nécessaire : `sudo dnf install epel-release`).
   - **Arch** : `sudo pacman -S dirb`.

#### 2. **Utiliser une réimplémentation Python (Multiplateforme, Pas de compilation C)**
   Le DirB original est basé sur C et capricieux à compiler, mais il existe un port Python moderne qui est fonctionnellement identique (ou meilleur) et s'installe via pip—aucun ajustement de source requis.
   - **Dépôt** : [ct-Open-Source/dirb sur GitHub](https://github.com/ct-Open-Source/dirb)
   - **Installation** :
     ```
     pip install git+https://github.com/ct-Open-Source/dirb.git
     ```
     - Ou clonez : `git clone https://github.com/ct-Open-Source/dirb.git && cd dirb && pip install .`
   - **Utilisation** : Identique à l'original, par exemple : `dirb https://example.com /usr/share/wordlists/dirb/common.txt`.
   - **Avantages** : Activement maintenu, plus rapide dans certains cas, fonctionne sur Mac/Windows/Linux. Inclut des extras comme l'analyse récursive.
   - **Inconvénients** : Ce n'est pas le binaire "officiel", mais la sortie correspond étroitement.

#### 3. **Télécharger un binaire pré-construit (Disponibilité limitée)**
   - Les versions officielles sur SourceForge sont principalement des archives source (par exemple, dirb222.tar.gz), qui nécessitent toujours un build.
   - Aucun binaire universel, mais si vous êtes sur Kali/Parrot OS, la méthode par paquet est la meilleure.
   - En tant que bidouille : Si vous avez Docker, tirez une image Kali et exécutez DirB à l'intérieur :
     ```
     docker run -it kalilinux/kali-rolling dirb http://example.com
     ```
     - Aucune installation nécessaire ; les conteneurs sont pré-construits.

#### Comparaison rapide

| Méthode              | Support OS          | Effort | Notes |
|---------------------|---------------------|--------|-------|
| **Apt/DNF/Pacman** | Linux (Debian/Fedora/Arch) | Faible | Pré-compilé ; listes de mots incluses. |
| **Port Python**    | Tous (Python 3+)    | Faible | Alternative moderne ; pip uniquement. |
| **Docker**         | Tous (avec Docker)  | Moyen | Isolé ; aucune installation sur l'hôte. |

Si aucune ne convient (par exemple, environnement restreint), envisagez des alternatives comme Gobuster (`go install github.com/OJ/gobuster/v3@latest`)—il est basé sur Go, se compile facilement sans problèmes et effectue un bruteforce de répertoires similaire.

Sur quel système d'exploitation êtes-vous ? Cela aidera à affiner le choix. Si vous rencontrez des problèmes, partagez l'erreur/la sortie.