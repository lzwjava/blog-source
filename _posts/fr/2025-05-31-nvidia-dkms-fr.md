---
audio: false
generated: true
lang: fr
layout: post
title: Problème de compilation NVIDIA DKMS
translated: true
type: note
---

Il semble que vous rencontriez une erreur où le module NVIDIA DKMS (Dynamic Kernel Module Support) ne parvient pas à se compiler pour votre nouveau noyau, `6.8.0-60-generic`. C'est un problème courant lors des mises à jour de noyau, car le module du pilote doit être recompilé pour la nouvelle version du noyau, et des incompatibilités ou des problèmes de compilation surviennent parfois.

Les messages d'erreur clés sont :
* `Building module(s)......(bad exit status: 2)`
* `Error! Bad return status for module build on kernel: 6.8.0-60-generic (x86_64)`
* `Consultez /var/lib/dkms/nvidia/535.183.06/build/make.log pour plus d'informations.`
* `dpkg: error processing package linux-image-6.8.0-60-generic (--configure):`
* `E: Sub-process /usr/bin/dpkg returned an error code (1)`

Cela signifie que le pilote NVIDIA version `535.183.06` n'a pas pu être compilé avec succès pour le noyau `6.8.0-60-generic`, ce qui a à son tour empêché l'image du noyau et les paquets associés d'être configurés correctement.

Voici comment vous pouvez essayer de résoudre ce problème :

---

### 1. Examiner le journal de compilation 🪵

L'étape la plus cruciale est de vérifier le journal de compilation détaillé pour des messages d'erreur spécifiques. Ce journal vous dira *pourquoi* la compilation a échoué.
Ouvrez un terminal et exécutez :
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```
Recherchez les lignes commençant par `error:` ou `fatal error:`. Elles indiquent souvent des fichiers manquants, des problèmes de compilateur ou des incompatibilités avec le code source du noyau. L'erreur `Applying patch disable_fstack-clash-protection_fcf-protection.patch... done.` suivie d'un échec de compilation suggère que le correctif pourrait ne pas être entièrement compatible, ou qu'il existe d'autres problèmes que le correctif ne résout pas.

---

### 2. Nettoyer et tenter de réparer les paquets cassés 🛠️

Premièrement, vous pouvez essayer de laisser `apt` tenter de réparer les dépendances cassées et terminer la configuration des paquets.
```bash
sudo rm /var/crash/nvidia-dkms-535.0.crash # Supprimer l'ancien rapport de plantage pour permettre de nouveaux rapports
sudo apt --fix-broken install
sudo dpkg --configure -a
```
Cela pourrait redéclencher la compilation DKMS. Si cela échoue à nouveau, passez aux étapes suivantes.

---

### 3. S'assurer que les en-têtes du noyau sont correctement installés 🧠

Le processus de compilation DKMS nécessite les bonnes en-têtes du noyau pour la version du noyau contre laquelle vous essayez de compiler.
```bash
sudo apt update
sudo apt install --reinstall linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04
```
Si vous n'utilisez pas encore le noyau `6.8.0-60-generic` (par exemple, si la mise à jour a été interrompue), vous pouvez également spécifier les en-têtes pour votre noyau actuellement en cours d'exécution, mais l'objectif principal ici est `6.8.0-60-generic`.

---

### 4. Supprimer le module DKMS défaillant et reconfigurer ♻️

Vous pouvez supprimer manuellement la version problématique du module NVIDIA de DKMS, puis laisser le système le recompiler.
```bash
sudo dkms remove nvidia/535.183.06 --all
```
Ensuite, essayez de reconfigurer les paquets à nouveau :
```bash
sudo dpkg --configure -a
sudo apt update && sudo apt upgrade
```
Ce processus devrait inciter DKMS à essayer de recompiler le module pour le noyau `6.8.0-60-generic`.

---

### 5. Réinstaller le pilote NVIDIA 💻

Si le module ne parvient toujours pas à se compiler, la version du pilote `535.183.06` pourrait avoir des problèmes de compatibilité avec le noyau `6.8.0-60-generic`.

* **Purger le pilote actuel problématique :**
    ```bash
    sudo apt-get purge nvidia-dkms-535 nvidia-driver-535
    sudo apt autoremove
    sudo apt clean
    ```

* **Installer un pilote approprié :**
    Vous pouvez laisser Ubuntu essayer d'installer le pilote recommandé :
    ```bash
    sudo ubuntu-drivers autoinstall
    ```
    Alternativement, vous pouvez essayer d'installer la même version (si elle est maintenant considérée comme compatible par les dépôts) ou une version potentiellement plus récente et plus compatible. Par exemple, pour essayer de réinstaller le pilote de la série 535 :
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-535
    ```
    (Le gestionnaire de paquets devrait choisir la version DKMS appropriée.)

    Après cela, le système tentera de compiler à nouveau le module DKMS.

---

### 6. Envisager une version plus récente du pilote NVIDIA 🚀

Le noyau 6.8 est relativement nouveau. Il est possible que le pilote NVIDIA série 535 ait des limitations avec cette version de noyau. Vous pourriez avoir besoin d'une série de pilotes plus récente (par exemple, 545, 550 ou plus récent, si disponible dans vos dépôts ou via les canaux officiels/PPA de NVIDIA).

* Vérifier les pilotes disponibles :
    ```bash
    sudo apt search nvidia-driver
    ```
* Si un pilote propriétaire plus récent est disponible (par exemple, `nvidia-driver-550`), vous pourriez essayer de l'installer à la place de `nvidia-driver-535`.
    ```bash
    sudo apt install nvidia-driver-NUMERO_VERSION # Remplacez NUMERO_VERSION
    ```

---

### 7. Si vous êtes bloqué dans une boucle de démarrage ou n'avez pas d'interface graphique 📉

Si le système ne parvient pas à démarrer dans un environnement graphique :
* Démarrez en mode récupération ou avec un ancien noyau (généralement accessible depuis le menu GRUB lors du démarrage).
* Une fois dans un environnement en ligne de commande, vous pouvez essayer les étapes ci-dessus.
* Si vous avez besoin d'utiliser temporairement un pilote open source pour retrouver une interface graphique pendant que vous réparez le pilote NVIDIA :
    ```bash
    sudo apt-get purge nvidia*
    sudo apt autoremove
    sudo apt install xserver-xorg-video-nouveau
    sudo reboot
    ```
    Ensuite, retentez l'installation du pilote NVIDIA.

---

**Point clé à retenir :** Le contenu de `/var/lib/dkms/nvidia/535.183.06/build/make.log` est très important. Si les étapes ci-dessus ne fonctionnent pas, les erreurs dans ce fichier fourniront des indices plus spécifiques, et vous devrez peut-être rechercher en ligne ces erreurs spécifiques en conjonction avec votre version de noyau et votre version de pilote NVIDIA.

---

Cette sortie indique une série de problèmes de dépendances et de configuration dans votre système Ubuntu, probablement liés aux mises à jour du noyau et au pilote NVIDIA. Décomposons les problèmes et suggérons des solutions potentielles.

**Problèmes principaux :**

1.  **Problèmes de dépendances avec `linux-generic-hwe-22.04` :**
    * Il dépend de `linux-headers-generic-hwe-22.04` avec une version spécifique (`= 6.8.0-60.63~22.04.1`).
    * `linux-headers-generic-hwe-22.04` n'est pas encore configuré, ce qui entraîne l'échec de la configuration de `linux-generic-hwe-22.04`.

2.  **Échec de la configuration de `linux-image-6.8.0-60-generic` :**
    * Le script post-installation pour cette image de noyau a échoué avec un statut de sortie 1.
    * Le journal d'erreurs suggère que cela est lié à l'échec de la compilation du pilote NVIDIA (`nvidia/535.183.06`) pour cette version spécifique du noyau (`6.8.0-60-generic`).
    * Le processus de compilation DKMS (Dynamic Kernel Module Support) pour le pilote NVIDIA a échoué. Le fichier journal `/var/lib/dkms/nvidia/535.183.06/build/make.log` contiendra plus de détails sur l'erreur de compilation.
    * Il y a également une erreur liée à la création d'un rapport de plantage pour l'échec de NVIDIA DKMS, indiquant un problème potentiel avec le mécanisme de rapport de plantage du système ou les permissions du système de fichiers.

3.  **Échec de la configuration de `linux-headers-6.8.0-60-generic` et `linux-headers-generic-hwe-22.04` :**
    * Ces échecs sont probablement dus à l'échec de la configuration du paquet `linux-image-6.8.0-60-generic`, dont ils pourraient dépendre.

**Causes potentielles :**

* **Mise à jour du noyau incomplète ou interrompue :** Le système a pu être interrompu lors d'une mise à niveau du noyau, laissant certains paquets dans un état incohérent.
* **Incompatibilité du pilote NVIDIA :** La version installée du pilote NVIDIA (`535.183.06`) pourrait avoir des problèmes de compilation avec la nouvelle version du noyau (`6.8.0-60-generic`).
* **Problèmes DKMS :** Il pourrait y avoir des problèmes avec le framework DKMS lui-même, empêchant la compilation du pilote NVIDIA.
* **Problèmes de système de fichiers :** L'erreur concernant l'impossibilité de créer un rapport de plantage pourrait indiquer un problème d'espace disque ou de permissions dans le répertoire `/var/crash/`.

**Étapes de dépannage :**

1.  **Essayer de reconfigurer les paquets :**
    Ouvrez votre terminal et exécutez la commande suivante :
    ```bash
    sudo dpkg --configure -a
    ```
    Cette commande tente de configurer tous les paquets qui sont dans un état semi-configuré.

2.  **Vérifier le journal de compilation NVIDIA DKMS :**
    Examinez le fichier journal pour des messages d'erreur détaillés lors de la compilation du pilote NVIDIA :
    ```bash
    less /var/lib/dkms/nvidia/535.183.06/build/make.log
    ```
    Ce journal pourrait fournir des indices sur des dépendances manquantes ou des erreurs de compilation.

3.  **Essayer de réinstaller le pilote NVIDIA :**
    Vous pouvez essayer de supprimer puis de réinstaller le pilote NVIDIA. D'abord, essayez de le purger :
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    ```
    Ensuite, essayez de le réinstaller. Vous pourriez essayer une version différente si la version actuelle est problématique :
    ```bash
    sudo apt install nvidia-driver-535  # Ou une autre version recommandée
    ```
    Après l'installation, redémarrez votre système.

4.  **Nettoyer le cache des paquets et réessayer :**
    ```bash
    sudo apt clean
    sudo apt update
    sudo apt upgrade
    sudo dpkg --configure -a
    ```

5.  **Réinstaller le noyau problématique et ses en-têtes :**
    Vous pouvez essayer de réinstaller les paquets de noyau et d'en-têtes spécifiques qui posent problème :
    ```bash
    sudo apt install --reinstall linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
    ```
    Après cela, essayez de reconfigurer à nouveau :
    ```bash
    sudo dpkg --configure -a
    ```

6.  **Vérifier l'espace disque :**
    Assurez-vous d'avoir suffisamment d'espace libre sur votre partition racine (`/`) car cela peut parfois causer des problèmes lors de l'installation et de la configuration des paquets.
    ```bash
    df -h /
    ```

7.  **Traiter l'erreur de rapport de plantage (si persistante) :**
    Si l'erreur concernant `/var/crash/nvidia-dkms-535.0.crash` persiste, vous pouvez essayer de supprimer le fichier (s'il existe et que vous n'en avez pas besoin pour le débogage) ou vérifier les permissions du répertoire `/var/crash/`.
    ```bash
    sudo rm -f /var/crash/nvidia-dkms-535.0.crash
    sudo chmod 777 /var/crash  # Soyez prudent avec les permissions larges, revenez en arrière si inutile
    ```

8.  **Démarrer avec un noyau précédent :**
    Si vous avez une version de noyau précédente installée, vous pouvez essayer de démarrer avec elle depuis le menu GRUB. Cela peut vous permettre d'effectuer les étapes de dépannage depuis un environnement stable. Si le système fonctionne avec un noyau plus ancien, le problème est probablement spécifique au noyau `6.8.0-60-generic` ou à son interaction avec le pilote NVIDIA.

**Considérations importantes :**

* **Sauvegarde :** Avant d'effectuer des changements significatifs, surtout impliquant la suppression de paquets, il est toujours judicieux d'avoir une sauvegarde de vos données importantes.
* **Soyez patient :** La configuration et l'installation des paquets peuvent prendre du temps.
* **Consultez les journaux :** Les messages d'erreur et les fichiers journaux (surtout le journal de compilation NVIDIA DKMS) sont cruciaux pour diagnostiquer la cause exacte du problème.

Commencez par les premières étapes et voyez si elles résolvent le problème. Sinon, passez aux solutions plus complexes et examinez attentivement tous les messages d'erreur que vous rencontrez. Bonne chance !

---

Cette sortie du journal de compilation NVIDIA DKMS indique que la compilation échoue en raison d'une **option de ligne de commande non reconnue : `-ftrivial-auto-var-init=zero`**.

Cette option de compilateur est un ajout relativement récent à GCC (probablement la version 12 ou ultérieure) et Clang. Il semble que le compilateur utilisé pour compiler le pilote NVIDIA pour votre noyau (6.8.0-60-generic) ne reconnaît pas cette option.

**Causes et solutions possibles :**

1.  **Compilateur obsolète :** Votre système pourrait avoir une version plus ancienne de GCC ou Clang installée comme compilateur par défaut. Les en-têtes du noyau pourraient avoir été compilées avec un compilateur plus récent qui utilise cette option, mais le système de compilation du pilote NVIDIA récupère une version plus ancienne.

    **Solution :**
    * **Installer un compilateur plus récent :** Vous pouvez essayer d'installer une version plus récente de GCC.
        ```bash
        sudo apt update
        sudo apt install gcc-12  # Ou une version ultérieure comme gcc-13
        ```
    * **Mettre à jour votre environnement de compilation :** Assurez-vous que vos outils de compilation sont à jour.
        ```bash
        sudo apt update
        sudo apt install build-essential
        ```
    * **Spécifier le compilateur (si possible) :** Certains systèmes de compilation vous permettent de spécifier le compilateur à utiliser. Vérifiez les instructions ou les fichiers de configuration de compilation du pilote NVIDIA pour les options liées au compilateur (par exemple, la variable d'environnement `CC`).

2.  **Incompatibilité avec la configuration de compilation du noyau :** Le noyau que vous utilisez pourrait avoir été compilé avec un compilateur qui a activé cette option, et le système de compilation du pilote NVIDIA l'hérite ou le rencontre d'une manière qui provoque un échec avec son propre compilateur.

    **Solution :**
    * **Essayer une version différente du pilote NVIDIA :** Le dernier pilote NVIDIA pourrait avoir une meilleure compatibilité avec les nouveaux noyaux et les fonctionnalités du compilateur. Vous pourriez essayer d'installer une version stable plus récente.
        ```bash
        sudo apt update
        sudo apt install nvidia-driver-<derniere-version>
        ```
        Remplacez `<derniere-version>` par le nom du paquet de pilote recommandé le plus récent pour votre système. Vous pouvez généralement le trouver en recherchant `apt search nvidia-driver`.
    * **Rétrograder votre noyau (comme solution temporaire) :** Si vous avez une version de noyau précédente installée qui fonctionnait avec votre pilote NVIDIA, vous pouvez démarrer avec ce noyau depuis le menu GRUB. Ce n'est pas une solution permanente mais peut vous donner un système fonctionnel pendant que vous résolvez le problème du pilote avec le nouveau noyau.

3.  **Problème avec le paquet du pilote NVIDIA :** Il pourrait y avoir un problème avec le paquet de pilote NVIDIA spécifique que vous essayez d'installer, en relation avec votre configuration de noyau et de compilateur.

    **Solution :**
    * **Essayer une méthode d'installation différente :** Si vous avez installé le pilote via `apt`, vous pourriez essayer de télécharger le pilote directement depuis le site web de NVIDIA et de l'installer en utilisant le fichier `.run`. Suivez attentivement les instructions fournies par NVIDIA.
    * **Vérifier les problèmes connus :** Recherchez dans les forums en ligne ou sur le site d'assistance NVIDIA les problèmes connus avec la combinaison spécifique de version de pilote et de noyau que vous utilisez.

**Étapes à essayer :**

1.  **Vérifier votre version de GCC :**
    ```bash
    gcc --version
    ```
    Comparez-la à la version de GCC qui aurait pu être utilisée pour compiler le noyau (vous pourriez trouver des informations sur l'environnement de compilation du noyau en ligne pour votre version d'Ubuntu).

2.  **Essayer d'installer un pilote NVIDIA plus récent :**
    ```bash
    sudo apt update
    sudo apt install nvidia-driver-550  # Exemple : essayer une version plus récente
    sudo reboot
    ```

3.  **Si cela ne fonctionne pas, essayer de purger et de réinstaller le pilote recommandé :**
    ```bash
    sudo apt remove --purge nvidia-*
    sudo apt autoremove
    sudo apt update
    sudo ubuntu-drivers autoinstall  # Installe les pilotes recommandés
    sudo reboot
    ```

4.  **Si vous rencontrez toujours des problèmes, envisagez d'installer une version plus récente de GCC (soyez prudent car cela peut parfois avoir des effets secondaires involontaires) :**
    ```bash
    sudo apt install gcc-12 g++-12
    sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-12 12
    sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-12 12
    # Vous voudrez peut-être garder l'ancienne version également et revenir en arrière si nécessaire
    # Pour revenir en arrière : sudo update-alternatives --config gcc et sudo update-alternatives --config g++
    sudo apt install build-essential # S'assurer que les outils de compilation sont mis à jour après le changement de compilateur
    sudo dpkg --configure -a # Reconfigurer les paquets
    sudo reboot
    ```

N'oubliez pas de redémarrer votre système après avoir essayé toute installation de pilote ou changement système significatif. Surveillez attentivement la sortie pour tout nouveau message d'erreur. Si vous continuez à avoir des problèmes, fournir plus de détails sur votre version d'Ubuntu pourrait aider à trouver une solution plus spécifique.

---

Il semble que vous rencontriez des problèmes de dépendances et de DKMS (Dynamic Kernel Module Support) lors de la tentative de configuration des paquets du noyau Linux, en particulier avec le module du pilote NVIDIA qui ne parvient pas à se compiler pour le nouveau noyau (6.8.0-60-generic).

### Voici comment résoudre ceci :

---

### **1. Réparer les dépendances et configurer les paquets**
D'abord, essayez de réparer les problèmes de dépendances et de configurer les paquets :

```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
```

Si cela ne fonctionne pas, forcez manuellement la configuration des paquets problématiques :

```bash
sudo apt install -f linux-headers-generic-hwe-22.04 linux-generic-hwe-22.04
```

---

### **2. Réinstaller les pilotes NVIDIA**
L'erreur montre que le module DKMS NVIDIA (`nvidia/535.183.06`) n'a pas pu se compiler pour le noyau `6.8.0-60-generic`. Pour corriger cela :

#### **Option A : Réinstaller le pilote NVIDIA**
```bash
sudo apt install --reinstall nvidia-dkms-535 nvidia-driver-535
```

#### **Option B : Purger et réinstaller les pilotes NVIDIA**
Si la réinstallation ne fonctionne pas, essayez une réinstallation propre :
```bash
sudo apt purge nvidia-*
sudo apt autoremove
sudo apt install nvidia-driver-535
```

#### **Option C : Démarrer temporairement avec un ancien noyau**
Si le système ne peut pas démarrer, redémarrez avec un ancien noyau (sélectionnez-le dans GRUB) puis :
```bash
sudo apt remove linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo update-grub
```

---

### **3. Vérifier le journal de compilation DKMS**
L'erreur mentionne `/var/lib/dkms/nvidia/535.183.06/build/make.log`. Vérifiez-le pour plus de détails :
```bash
cat /var/lib/dkms/nvidia/535.183.06/build/make.log
```

Cela peut révéler pourquoi le module n'a pas pu se compiler (par exemple, dépendances manquantes, problèmes de compilateur).

---

### **4. Installer manuellement les dépendances manquantes**
Si le journal montre des dépendances manquantes, installez-les :
```bash
sudo apt install build-essential linux-headers-generic
```

---

### **5. Recompiler les modules DKMS**
Après avoir corrigé les dépendances, recompilez manuellement les modules :
```bash
sudo dkms remove nvidia/535.183.06 --all
sudo dkms install nvidia/535.183.06
```

---

### **6. Mettre à jour Initramfs**
Après avoir corrigé le pilote NVIDIA, mettez à jour l'initramfs :
```bash
sudo update-initramfs -u -k all
```

---

### **7. Tentative de correction finale**
Si tout le reste échoue, supprimez le noyau problématique et restez avec un ancien :
```bash
sudo apt purge linux-image-6.8.0-60-generic linux-headers-6.8.0-60-generic
sudo apt autoremove
sudo update-grub
```

Ensuite, attendez un pilote NVIDIA ou un noyau mis à jour avant de réessayer.

---

### **8. Empêcher les problèmes futurs**
Pour éviter des problèmes similaires, envisagez :
- **Désactiver les mises à jour automatiques du noyau** (si vous dépendez des pilotes NVIDIA) :
  ```bash
  sudo apt-mark hold linux-image-generic linux-headers-generic
  ```
- **Utiliser le pilote NVIDIA officiel** (au lieu du paquet Ubuntu) si la compatibilité est un problème récurrent.

---

### **Notes finales**
- Si le système devient incapable de démarrer, utilisez **GRUB** pour sélectionner un ancien noyau.
- Si les pilotes NVIDIA sont critiques pour votre flux de travail, envisagez d'utiliser des **noyaux LTS** (non-HWE) pour une meilleure stabilité.

Faites-moi savoir si vous avez besoin d'une aide supplémentaire !

---

Si vous voulez simplement procéder avec `apt upgrade` et **ignorer les paquets problématiques**, vous pouvez temporairement les exclure du processus de mise à niveau. Voici comment :

### **Option 1 : Ignorer les paquets cassés et continuer la mise à niveau**
Exécutez :
```bash
sudo apt --fix-broken install
sudo apt upgrade -y --ignore-missing --allow-downgrades
```
- `--ignore-missing` ignore les paquets indisponibles.
- `--allow-downgrades` permet à APT de rétrograder les paquets si nécessaire.

### **Option 2 : Mettre en attente (bloquer) les paquets problématiques**
Si le problème persiste, **mettez en attente** (bloquez) les paquets problématiques pour empêcher leur mise à niveau :
```bash
sudo apt-mark hold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04 linux-image-6.8.0-60-generic
```
Puis réessayez :
```bash
sudo apt upgrade -y
```

### **Option 3 : Forcer la mise à niveau (Non recommandée)**
Si vous acceptez de risquer de casser davantage les choses, forcez la mise à niveau :
```bash
sudo apt -o Dpkg::Options::="--force-overwrite" --fix-broken install
sudo apt upgrade -y
```
⚠️ **Avertissement :** Cela peut causer une instabilité si les dépendances ne correspondent pas.

### **Après avoir ignoré :**
- Le système fonctionnera toujours, mais le **pilote NVIDIA pourrait ne pas fonctionner** sur le noyau `6.8.0-60`.
- Vous pouvez **démarrer avec un ancien noyau** (sélectionnez-le dans GRUB) si nécessaire.
- Une fois que NVIDIA publiera une mise à jour compatible, vous pourrez **débloquer** les paquets :
  ```bash
  sudo apt-mark unhold linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04
  ```

Souhaitez-vous de l'aide pour vérifier quel noyau est actuellement actif après la mise à niveau ?