---
audio: false
generated: true
lang: fr
layout: post
title: Suppression du client VPN Outline sur Ubuntu
translated: true
type: note
---

Il semble que `apt` ne trouve pas de paquet nommé `outline-client`. Cela signifie généralement l'une des deux choses suivantes :

1.  **Vous n'avez pas installé Outline en utilisant `apt` (c'est-à-dire qu'il n'a pas été installé en tant que paquet .deb).** C'est la raison la plus courante de cette erreur avec Outline, car de nombreux utilisateurs l'installent via l'AppImage.
2.  **Le nom du paquet est différent, ou le dépôt n'est pas configuré.** Bien que moins probable pour Outline, c'est une possibilité pour d'autres logiciels.

Compte tenu de votre tentative précédente, il est très probable que vous l'ayez installé en tant qu'**AppImage**. Dans ce cas, vous devrez le supprimer manuellement.

Voici comment procéder :

**1. Localiser et supprimer le fichier AppImage :**

Le client Outline, lorsqu'il est installé en tant qu'AppImage, est généralement un seul fichier exécutable. Vous l'avez probablement téléchargé dans votre dossier `Téléchargements`, ou peut-être déplacé vers un dossier `bin` ou `Applications` dans votre répertoire personnel.

* **Emplacements courants à vérifier :**
    * `~/Téléchargements/`
    * `~/Applications/` (si vous en avez créé un)
    * `~/bin/` (si vous en avez créé un)
    * Le répertoire depuis lequel vous l'avez exécuté à l'origine.

* **Comment le trouver :** Vous pouvez utiliser la commande `find` pour le rechercher dans votre répertoire personnel :
    ```bash
    find ~ -name "Outline-Client*.AppImage" 2>/dev/null
    ```
    Cette commande recherchera dans votre répertoire personnel tout fichier commençant par "Outline-Client" et se terminant par ".AppImage".
    Une fois trouvé, supprimez-le :
    ```bash
    rm /chemin/vers/Outline-Client.AppImage
    ```
    (Remplacez `/chemin/vers/` par le chemin réel trouvé par la commande `find`.)

**2. Supprimer les fichiers de configuration résiduels et de démarrage automatique :**

Même si vous supprimez l'AppImage, Outline a pu créer des fichiers de configuration et une entrée de démarrage automatique.

* **Supprimer le répertoire de configuration :**
    ```bash
    rm -rf ~/.config/Outline/
    ```
    Cette commande supprime l'intégralité du répertoire `Outline` dans le dossier de configuration de votre utilisateur.

* **Supprimer l'entrée de démarrage automatique (si elle a été créée) :**
    Si Outline était configuré pour démarrer automatiquement à la connexion, il pourrait y avoir un fichier `.desktop` pour lui.
    ```bash
    rm -f ~/.config/autostart/Outline-Client.AppImage.desktop
    ```

* **Supprimer les icônes du bureau (le cas échéant) :**
    Parfois, les AppImages créent une icône sur le bureau dans votre répertoire d'icônes local.
    ```bash
    find ~/.local/share/icons -name "appimagekit-outline-client*.png" -delete
    ```
    Cela supprimera toutes les icônes PNG liées à l'AppImage Outline.

**3. Vérifier et restaurer la configuration réseau (si nécessaire) :**

Outline, comme d'autres VPN, peut modifier vos paramètres DNS. Si vous rencontrez des problèmes de connectivité Internet après avoir supprimé l'AppImage, vérifiez votre fichier `/etc/resolv.conf`.

* **Inspecter `resolv.conf` :**
    ```bash
    cat /etc/resolv.conf
    ```
    Recherchez les lignes qui semblent avoir été ajoutées par Outline (par exemple, des adresses IP spécifiques pour des serveurs de noms que vous ne reconnaissez pas comme étant ceux de votre routeur ou de votre FAI).

* **Restaurer `resolv.conf` (si nécessaire) :**
    S'il semble qu'Outline l'ait modifié :
    * **Option A (Recommandée pour Ubuntu moderne) :** Si votre système utilise `systemd-resolved` (ce qui est courant dans les versions récentes d'Ubuntu), vous pouvez généralement résoudre ce problème en recréant le lien symbolique :
        ```bash
        sudo rm /etc/resolv.conf
        sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
        ```
    * **Option B (Édition manuelle - à utiliser si l'Option A ne fonctionne pas ou pour les systèmes plus anciens) :**
        Commencez par faire une sauvegarde :
        ```bash
        sudo cp /etc/resolv.conf /etc/resolv.conf.bak
        ```
        Ensuite, éditez le fichier :
        ```bash
        sudo nano /etc/resolv.conf
        ```
        Commentez ou supprimez toutes les lignes `nameserver` qui ont été ajoutées par Outline. Vous pouvez généralement indiquer des serveurs DNS publics comme ceux de Google (`8.8.8.8` et `8.8.4.4`) ou de Cloudflare (`1.1.1.1` et `1.0.0.1`) si vous ne connaissez pas ceux de votre FAI.

**4. Redémarrer votre système :**

Après avoir terminé ces étapes, il est fortement recommandé de redémarrer votre système Ubuntu pour vous assurer que tous les changements prennent effet et que tous les processus d'arrière-plan liés à Outline soient complètement terminés.

```bash
sudo reboot
```

En suivant ces étapes de suppression manuelle, vous devriez pouvoir supprimer complètement le client VPN Outline de votre système Ubuntu.