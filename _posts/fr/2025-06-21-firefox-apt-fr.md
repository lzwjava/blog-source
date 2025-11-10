---
audio: false
generated: true
lang: fr
layout: post
title: Installation de Firefox via APT sur Ubuntu
translated: true
type: note
---

Ce guide détaille comment installer Firefox à partir du dépôt APT de Mozilla sur Ubuntu, en remplacement du paquet Snap par défaut.

**Pourquoi utiliser la version APT ?**

Bien que la version Snap soit pratique, certains utilisateurs préfèrent la version APT pour une meilleure intégration et de meilleures performances.

**Étapes :**

1.  **Désinstaller le Snap Firefox :**

    ```bash
    sudo snap remove firefox
    ```

2.  **Créer un répertoire keyring pour APT (s'il n'existe pas) :**

    ```bash
    sudo install -d -m 0755 /etc/apt/keyrings
    ```

3.  **Importer la clé de signature du dépôt APT Mozilla :**

    ```bash
    wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
    ```
    *Si `wget` est manquant, installez-le d'abord : `sudo apt install wget`*

4.  **Ajouter le dépôt Mozilla à votre liste de sources :**

    ```bash
    echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
    ```

5.  **Définir la priorité des paquets pour préférer le DEB Mozilla :**

    Cela empêche le paquet de transition d'Ubuntu de réinstaller le Snap.

    ```bash
    echo '
    Package: *
    Pin: origin packages.mozilla.org
    Pin-Priority: 1000

    Package: firefox*
    Pin: release o=Ubuntu
    Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
    ```

6.  **Supprimer le DEB Firefox d'Ubuntu (s'il est présent) et installer la version Mozilla :**

    ```bash
    sudo apt update && sudo apt remove firefox
    sudo apt install firefox
    ```

Vous avez maintenant Firefox installé à partir du dépôt APT officiel de Mozilla !