---
audio: false
generated: true
lang: fr
layout: post
title: Installer VLC Media Player sur Ubuntu
translated: true
type: note
---

Pour installer VLC media player sur votre système Ubuntu, vous pouvez utiliser soit le terminal (ligne de commande) soit le Ubuntu Software Center (interface graphique). Vous trouverez ci-dessous des instructions détaillées pour les deux méthodes.

---

### **Méthode 1 : Installer VLC en utilisant le Terminal**

Cette méthode est rapide et efficace, surtout si vous êtes à l'aise avec la ligne de commande. Suivez ces étapes :

1. **Ouvrez le Terminal**
   - Recherchez "Terminal" dans le menu des applications Ubuntu, ou appuyez sur `Ctrl + Alt + T` pour l'ouvrir.

2. **Mettez à jour la liste des paquets**
   - Avant d'installer un logiciel, il est recommandé de s'assurer que votre liste de paquets est à jour. Exécutez cette commande :
     ```bash
     sudo apt update
     ```
   - Entrez votre mot de passe lorsqu'il vous est demandé. Cette commande actualise la liste des paquets logiciels disponibles.

3. **Installez VLC**
   - Une fois la liste des paquets mise à jour, installez VLC en exécutant :
     ```bash
     sudo apt install vlc
     ```
   - Vous devrez à nouveau entrer votre mot de passe. Le système peut vous demander de confirmer l'installation en tapant `y` et en appuyant sur Entrée. Cela téléchargera et installera VLC ainsi que ses dépendances nécessaires.

4. **Vérifiez l'installation**
   - Après l'installation, vérifiez si VLC est installé en tapant :
     ```bash
     vlc
     ```
   - Cela devrait lancer le lecteur multimédia VLC. S'il s'ouvre, l'installation a réussi.
   - Alternativement, vous pouvez vérifier la version de VLC en exécutant :
     ```bash
     vlc --version
     ```
   - Cela affichera quelque chose comme "VLC media player 3.0.11.1 Vetinari" (le numéro de version peut varier).

5. **Optionnel : Testez VLC**
   - Pour vous assurer que VLC fonctionne correctement, essayez de lire un fichier multimédia. Par exemple, si vous avez un fichier MP4 sur votre bureau, faites un clic droit dessus et sélectionnez "Ouvrir avec VLC media player". S'il se lit, VLC est pleinement fonctionnel.

---

### **Méthode 2 : Installer VLC en utilisant le Ubuntu Software Center**

Si vous préférez une interface graphique plutôt que le terminal, utilisez le Ubuntu Software Center :

1. **Ouvrez le Ubuntu Software Center**
   - Recherchez "Ubuntu Software" dans le menu des applications et cliquez pour l'ouvrir.

2. **Recherchez VLC**
   - Dans le Software Center, cliquez sur l'icône de recherche (généralement une loupe) et tapez "VLC" dans la barre de recherche.

3. **Installez VLC**
   - Trouvez "VLC media player" dans les résultats de recherche, cliquez dessus, puis cliquez sur le bouton "Installer". Vous devrez peut-être entrer votre mot de passe pour autoriser l'installation.

4. **Lancez VLC**
   - Une fois installé, vous pouvez lancer VLC directement depuis le Software Center en cliquant sur "Ouvrir" (si disponible) ou en recherchant "VLC" dans le menu des applications.

---

### **Notes supplémentaires**

- **Maintenir VLC à jour**
   - Si vous avez installé VLC en utilisant le terminal, vous pouvez le maintenir à jour en exécutant périodiquement :
     ```bash
     sudo apt update
     sudo apt upgrade
     ```
   - Cela met à jour VLC ainsi que les autres paquets système. Si vous avez utilisé le Software Center, les mises à jour sont généralement gérées via la même interface.

- **Plugins et codecs**
   - L'installation par défaut de VLC via `sudo apt install vlc` inclut les plugins essentiels (comme `vlc-plugin-base`) et les codecs, elle devrait donc lire la plupart des formats multimédias courants (par exemple, MP4, AVI) dès l'installation. Si vous rencontrez des problèmes avec des types de fichiers spécifiques, vous pouvez installer des codecs supplémentaires plus tard, tels que `ubuntu-restricted-extras`, en utilisant :
     ```bash
     sudo apt install ubuntu-restricted-extras
     ```

- **Installation alternative via Snap**
   - VLC est également disponible en tant que paquet Snap. Si vous préférez cette méthode, exécutez :
     ```bash
     sudo snap install vlc
     ```
   - Cependant, la méthode `apt` est recommandée pour la plupart des utilisateurs car elle s'intègre bien avec le système.

---

En suivant l'une ou l'autre méthode, vous aurez VLC installé et prêt à l'emploi sur votre système Ubuntu. La méthode du terminal est plus rapide pour les utilisateurs de ligne de commande, tandis que le Software Center est idéal pour ceux qui préfèrent une approche graphique. Bonne lecture multimédia !

---

Pour corriger l'erreur que vous rencontrez lors de la lecture d'un fichier MKV dans VLC sur Ubuntu—spécifiquement le message concernant les décodeurs MPEG-4 AAC et H.265 manquants—suivez les étapes ci-dessous. Ce problème se produit généralement parce qu'Ubuntu n'inclut pas certains codecs propriétaires par défaut en raison de restrictions de licence. L'installation de paquets de codecs supplémentaires devrait résoudre le problème.

---

### **Solution**

#### **Étape 1 : Installer le paquet `ubuntu-restricted-extras`**
Ce paquet fournit la prise en charge d'une variété de codecs, y compris MPEG-4 AAC (audio) et H.265 (HEVC) vidéo, qui manquent probablement à votre installation VLC.

1. **Ouvrez le Terminal**
   - Recherchez "Terminal" dans le menu des applications Ubuntu ou appuyez sur `Ctrl + Alt + T`.

2. **Mettez à jour la liste des paquets**
   - Exécutez cette commande pour vous assurer que la liste des paquets de votre système est à jour :
     ```bash
     sudo apt update
     ```

3. **Installez `ubuntu-restricted-extras`**
   - Exécutez la commande suivante :
     ```bash
     sudo apt install ubuntu-restricted-extras
     ```
   - Vous devrez peut-être entrer votre mot de passe. Pendant l'installation, vous pourriez être invité à accepter le contrat de licence utilisateur final (EULA) pour certains composants—suivez les instructions à l'écran pour accepter et poursuivre.

4. **Redémarrez VLC**
   - Fermez VLC s'il est ouvert, puis rouvrez-le et essayez de lire à nouveau le fichier MKV.

---

#### **Étape 2 : Installer des paquets de codecs supplémentaires (si nécessaire)**
Si l'erreur persiste après l'Étape 1, installez des paquets spécifiques qui fournissent une prise en charge supplémentaire pour H.265 et d'autres codecs.

1. **Installez `libde265-0` et `libavcodec-extra`**
   - Exécutez cette commande pour installer les bibliothèques pour le décodage H.265 et le support de codecs supplémentaires :
     ```bash
     sudo apt install libde265-0 libavcodec-extra
     ```

2. **Redémarrez VLC**
   - Fermez et rouvrez VLC, puis tentez de lire à nouveau le fichier MKV.

---

#### **Étape 3 : Dépannage supplémentaire (si nécessaire)**
Si le problème n'est toujours pas résolu, essayez ces étapes supplémentaires :

- **Vérifiez la version de VLC**
  - Assurez-vous d'utiliser la dernière version de VLC. Vérifiez votre version actuelle avec :
    ```bash
    vlc --version
    ```
  - Si elle est obsolète, mettez-la à jour en exécutant :
    ```bash
    sudo apt update
    sudo apt upgrade vlc
    ```

- **Testez un autre fichier MKV**
  - Lisez un autre fichier MKV pour voir si le problème est spécifique à un fichier. Si d'autres fichiers fonctionnent, le fichier problématique est peut-être corrompu ou utilise un encodage non pris en charge.

- **Consultez les journaux VLC pour plus de détails**
  - Pour un dépannage avancé, exécutez VLC depuis le terminal avec une sortie verbeuse :
    ```bash
    vlc --verbose 2
    ```
  - Essayez de lire le fichier et recherchez des messages d'erreur détaillés concernant les codecs manquants.

---

### **Notes supplémentaires**
- **Pourquoi cela arrive** : MKV est un format conteneur qui peut utiliser divers codecs comme MPEG-4 AAC pour l'audio et H.265 pour la vidéo. L'installation par défaut de VLC sous Ubuntu peut en être dépourvue en raison des restrictions légales sur les logiciels propriétaires.
- **Accélération matérielle** : Si votre système prend en charge le décodage matériel H.265 (par exemple, via un GPU moderne), assurez-vous que vos pilotes graphiques sont à jour. Cependant, cette erreur suggère un décodeur logiciel manquant, donc l'accélération matérielle n'est probablement pas le problème principal.
- **Prochaines étapes** : Si rien de ce qui précède ne fonctionne, envisagez de réinstaller VLC ou de demander de l'aide sur les forums Ubuntu ou VLC avec des détails sur votre système et le fichier MKV spécifique.

---

En suivant ces étapes, vous devriez pouvoir corriger les erreurs de décodeurs manquants et lire vos fichiers MKV dans VLC avec succès. Commencez par l'Étape 1, car c'est la solution la plus simple et la plus probable.