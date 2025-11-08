---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction de l'Erreur du Dépôt APT de Firefox
translated: true
type: note
---

L'erreur que vous voyez est spécifique au dépôt APT de Mozilla Firefox (`https://packages.mozilla.org/apt`), où la récupération du fichier d'index `binary-all/Packages` échoue avec une erreur 400 Bad Request. C'est un problème intermittent connu, signalé par d'autres utilisateurs Ubuntu/Debian, souvent lié à des configurations de proxy (votre proxy local sur `127.0.0.1:7890` suggère qu'un outil comme Clash, V2Ray, ou similaire est en cours d'exécution, ce qui peut altérer les requêtes HTTPS pour APT). La bonne nouvelle est qu'APT ignore l'échec et utilise les index mis en cache ou anciens, donc les mises à jour du système ne sont pas bloquées—mais cela peut empêcher d'obtenir les derniers paquets .deb de Firefox.

### Correctifs rapides à essayer (dans l'ordre)
1.  **Vider le cache d'APT** (cela résout les fichiers d'index corrompus ou obsolètes, ce qui a résolu le problème pour plusieurs utilisateurs) :
    ```
    sudo apt clean
    sudo apt update
    ```

2.  **Contourner temporairement votre proxy pour APT** (puisque l'erreur 400 provient souvent de l'interférence du proxy avec le HTTPS du dépôt) :
    ```
    unset http_proxy https_proxy all_proxy
    sudo -E apt update
    ```
    - Exécutez cette commande dans la même session terminal. Si cela fonctionne, vous pouvez le rendre permanent en ajoutant les lignes `unset` à votre `~/.bashrc` (ou juste avant les commandes APT) ou en désactivant brièvement l'application proxy.
    - Si votre proxy est défini globalement (par exemple, dans `/etc/environment`), modifiez ce fichier pour exclure APT ou commentez les lignes temporairement.

3.  **Désactiver le proxy globalement pour APT** (si la méthode ci-dessus fonctionne mais que vous voulez une option définitive) :
    ```
    echo 'Acquire::http::Proxy "";
    Acquire::https::Proxy "";' | sudo tee /etc/apt/apt.conf.d/99no-proxy
    sudo apt update
    ```
    - Cela indique à APT d'ignorer complètement les proxies. Pour annuler, supprimez le fichier `/etc/apt/apt.conf.d/99no-proxy` si nécessaire.

### Si vous avez besoin de la dernière version de Firefox sans le dépôt
Si le dépôt continue d'échouer et que vous voulez simplement Firefox à jour :
- **Passer à Snap** (version par défaut d'Ubuntu, mises à jour faciles, pas de problème de dépôt) :
  ```
  sudo snap install firefox
  ```
- **Ou Flatpak** (si vous préférez) :
  ```
  sudo apt install flatpak
  flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
  flatpak install flathub org.mozilla.firefox
  ```

### Prévention / Notes
- Le dépôt Mozilla est non officiel pour obtenir les paquets .deb de Firefox les plus récents—envisagez de vous en tenir à la version snap d'Ubuntu, sauf si vous avez spécifiquement besoin du paquet .deb.
- Si rien de tout cela ne fonctionne, vérifiez les journaux de votre proxy (par exemple, le tableau de bord Clash) pour les requêtes rejetées vers `packages.mozilla.org`, ou testez sans le proxy entirely.
- Exécutez `sudo apt update` à nouveau après les correctifs pour vérifier.

Si ces solutions ne résolvent pas le problème, partagez plus de détails comme votre configuration de proxy ou le contenu complet de `/etc/apt/sources.list.d/mozilla.list` pour un dépannage plus approfondi.

[Ubuntu 23.10 - Update Problems](https://askubuntu.com/questions/1507571/ubuntu-23-10-update-problems-some-index-files-failed-to-download)  
[Firefox apt repository error](https://www.reddit.com/r/firefox/comments/1ois308/firefox_apt_repository_error/)