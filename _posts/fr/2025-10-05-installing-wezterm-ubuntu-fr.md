---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation de WezTerm sur Ubuntu
translated: true
type: note
---

L'erreur "Unable to locate package wezterm" se produit car WezTerm n'est pas disponible dans les dépôts par défaut d'Ubuntu. Vous devez d'abord ajouter le dépôt tiers officiel. Voici la solution étape par étape en utilisant la méthode APT native (recommandée pour une intégration transparente) :

1.  Ajoutez la clé GPG pour le dépôt :
    ```
    curl -fsSL https://apt.fury.io/wez/gpg.key | sudo gpg --yes --dearmor -o /usr/share/keyrings/wezterm-fury.gpg
    ```

2.  Ajoutez le dépôt à vos sources :
    ```
    echo 'deb [signed-by=/usr/share/keyrings/wezterm-fury.gpg] https://apt.fury.io/wez/ * *' | sudo tee /etc/apt/sources.list.d/wezterm.list
    ```

3.  Définissez les permissions correctes sur le fichier de clé :
    ```
    sudo chmod 644 /usr/share/keyrings/wezterm-fury.gpg
    ```

4.  Mettez à jour votre liste de paquets :
    ```
    sudo apt update
    ```

5.  Maintenant, installez WezTerm :
    ```
    sudo apt install wezterm
    ```

Une fois installé, vous pouvez l'exécuter avec `wezterm` depuis le terminal. Si vous voulez la version nightly (la plus récente) à la place, utilisez `sudo apt install wezterm-nightly` à l'étape 5—mais notez qu'elle ne peut pas coexister avec la version stable.

### Alternative : Flatpak (Aucun Dépôt Nécessaire)
Si vous préférez une installation sandboxée sans modifier les sources APT :
1.  Installez Flatpak s'il n'est pas déjà présent : `sudo apt install flatpak`.
2.  Ajoutez Flathub : `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3.  Installez : `flatpak install flathub org.wezfurlong.wezterm`.
4.  Exécutez : `flatpak run org.wezfurlong.wezterm` (ou ajoutez un alias : `alias wezterm='flatpak run org.wezfurlong.wezterm'`).

Flatpak est isolé, donc il pourrait limiter certaines fonctionnalités avancées, mais c'est plus simple pour les tests.

[Guide d'installation de WezTerm sur Linux](https://wezterm.org/install/linux.html)