---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation d'Emacs sur RHEL
translated: true
type: note
---

### Installation d'Emacs sur Red Hat Enterprise Linux

Red Hat Enterprise Linux (RHEL) utilise principalement le gestionnaire de paquets DNF pour installer des logiciels. Emacs est disponible dans les dépôts par défaut, donc l'installation est simple. Vous trouverez ci-dessous les étapes pour les versions modernes (RHEL 8 et ultérieures). Pour les versions plus anciennes (par exemple, RHEL 7), remplacez `dnf` par `yum`.

#### Prérequis
- Assurez-vous d'avoir les privilèges root (utilisez `sudo`).
- Votre système doit être enregistré auprès de Red Hat Subscription Management si vous utilisez les dépôts officiels RHEL.

#### Étapes d'installation
1. **Mettez à jour le cache des paquets** (recommandé pour obtenir la dernière version disponible) :  
   ```
   sudo dnf update
   ```

2. **Installez Emacs** :  
   ```
   sudo dnf install emacs
   ```  
   Cela installera la dernière version stable disponible dans les dépôts (par exemple, Emacs 28.x ou 29.x, selon votre version de RHEL).

3. **Vérifiez l'installation** :  
   Exécutez la commande suivante pour vérifier la version :  
   ```
   emacs --version
   ```  
   Vous devriez voir une sortie similaire à `GNU Emacs 28.2` (ou équivalent).

#### Notes
- Si vous utilisez une ancienne version de RHEL avec YUM (par exemple, RHEL 7), la commande est `sudo yum install emacs`.
- Pour la toute dernière version d'Emacs (par exemple, 29+), vous devrez peut-être compiler à partir des sources ou utiliser des dépôts tiers comme EPEL, car les dépôts de base peuvent être en retard.
- Pour lancer Emacs, tapez simplement `emacs` dans le terminal.

[FAQ GNU Emacs : Installation d'Emacs](https://www.gnu.org/software/emacs/manual/html_node/efaq/Installing-Emacs.html)  
[Documentation Red Hat : Gestion des logiciels avec DNF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_software_with_the_dnf_tool/index)