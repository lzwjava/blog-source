---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Éditeurs de texte par défaut dans RHEL Minimal
translated: true
type: note
---

Dans Red Hat Enterprise Linux (RHEL), particulièrement dans une installation minimale (la valeur par défaut pour les serveurs et les configurations légères), le seul éditeur de texte disponible nativement est **vi**, fourni par le paquet `vim-minimal`. Cela vous donne une implémentation basique et compatible de la commande classique `vi` pour éditer des fichiers dans le terminal.

- **`vim` complet** (la version améliorée avec plus de fonctionnalités, la coloration syntaxique, etc.) n'est pas installé par défaut. Vous pouvez l'ajouter avec `sudo dnf install vim-enhanced`.
- **Nano** et **Emacs** ne sont pas inclus dans l'installation minimale. Ils sont disponibles dans les dépôts mais nécessitent une installation explicite :
  - Pour Nano : `sudo dnf install nano`
  - Pour Emacs : `sudo dnf install emacs`

Cela permet de garder l'installation minimale légère (environ 200-300 paquets au total) pour privilégier la sécurité et les performances. Si vous effectuez une installation de bureau ou de serveur complète (non minimale), plus d'outils pourraient être inclus en fonction de l'environnement sélectionné.

[Prise en main de Nano (Red Hat)](https://www.redhat.com/en/blog/getting-started-nano)  
[Pourquoi RHEL a-t-il deux vim installés par défaut ?](https://unix.stackexchange.com/questions/699071/why-rhel-has-two-vim-installed-by-default)  
[Manifeste des paquets RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)