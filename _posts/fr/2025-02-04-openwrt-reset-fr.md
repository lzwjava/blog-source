---
audio: true
lang: fr
layout: post
title: Réinitialisation OpenWrt
translated: true
---

## Réinitialisation via l'interface Web

Il est recommandé de se connecter au routeur via un câble Ethernet. Après une réinitialisation, le SSID Wi-Fi reviendra à ses paramètres par défaut, ce qui peut différer de vos attentes.

## Réinitialisation via la ligne de commande (SSH)

Vous pouvez réinitialiser OpenWrt à ses paramètres par défaut en utilisant l'interface en ligne de commande (SSH). Voici comment :

1.  Connectez-vous à votre routeur OpenWrt via SSH.
2.  Exécutez la commande suivante :

    ```bash
    root@OpenWrt:~# firstboot
    This will erase all settings and remove any installed packages. Are you sure? [N/y]
    y
    /dev/ubi0_1 is mounted as /overlay, only erasing files
    root@OpenWrt:~# reboot
    ```
3.  Le routeur redémarrera avec les paramètres par défaut.

**Explication des commandes :**

*   `firstboot` : Cette commande lance le processus de réinitialisation, effaçant toutes les configurations et les paquets installés.
*   `reboot` : Cette commande redémarre le routeur, appliquant la réinitialisation.
