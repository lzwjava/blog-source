---
audio: true
generated: true
lang: fr
layout: post
title: Configuration SSH
translated: true
---

Ce fichier `ssh-config` configure le comportement du client SSH. Décomposons chaque partie :

-   `Host * !192.*.*.*`: Cette section s'applique à tous les hôtes *sauf* ceux correspondant au modèle `192.*.*.*` (généralement, les adresses du réseau local).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: C'est la partie clé. Elle indique à SSH d'utiliser le programme `corkscrew` pour se connecter à l'hôte cible.
        -   `corkscrew`: Un outil qui permet de tunneler les connexions SSH à travers des proxys HTTP ou HTTPS.
        -   `localhost 7890`: Spécifie l'adresse du serveur proxy (`localhost`) et le port (`7890`). Cela suppose que vous avez un serveur proxy en cours d'exécution sur votre machine locale, à l'écoute sur le port 7890 (par exemple, Shadowsocks, un proxy SOCKS, ou une autre solution de tunneling).
        -   `%h`: Une variable SSH spéciale qui se développe en nom d'hôte cible auquel vous essayez de vous connecter.
        -   `%p`: Une autre variable SSH qui se développe en port cible (généralement 22 pour SSH).
    - En résumé, ce bloc `Host` configure SSH pour utiliser le proxy `corkscrew` pour toutes les connexions *sauf* celles vers le réseau local.

-   `Host *`: Cette section s'applique à *tous* les hôtes.
    -   `UseKeychain yes`: Sur macOS, cela indique à SSH de stocker et de récupérer les clés SSH dans votre Keychain, afin que vous n'ayez pas à entrer votre mot de passe à chaque fois.
    -   `AddKeysToAgent yes`: Cela ajoute automatiquement vos clés SSH à l'agent SSH, afin que vous n'ayez pas à les ajouter manuellement après chaque redémarrage.
    -   `IdentityFile ~/.ssh/id_rsa`: Spécifie le chemin vers votre fichier de clé SSH privée. `~/.ssh/id_rsa` est l'emplacement par défaut pour la clé privée RSA.

**En résumé, cette configuration configure un proxy pour toutes les connexions SSH sauf celles sur le réseau local, et elle configure la gestion des clés pour plus de commodité.**

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```