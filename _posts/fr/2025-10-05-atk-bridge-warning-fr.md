---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre le message d'avertissement atk-bridge
translated: true
type: note
---

Ce message d'avertissement apparaît dans les applications basées sur GTK (comme Firefox, Snap Store ou GitHub CLI) sur les systèmes Linux, en particulier Ubuntu. Ce n'est pas une erreur — c'est simplement informatif. Le module "atk-bridge" était autrefois utilisé pour connecter le Accessibility Toolkit (ATK) pour les lecteurs d'écran et autres fonctionnalités d'accessibilité, mais les versions plus récentes de GTK (à partir d'environ la version 3.22) incluent cette fonctionnalité directement. Le chargement du module séparé est redondant, donc GTK l'ignore et enregistre cette note.

Il est inoffensif et n'affecte pas les performances de l'application, mais si il encombre la sortie de votre terminal, vous pouvez le supprimer en définissant la variable d'environnement `NO_AT_BRIDGE=1` avant d'exécuter l'application. Par exemple :

```bash
export NO_AT_BRIDGE=1
firefox  # Ou toute autre application qui le déclenche
```

Pour le rendre permanent, ajoutez cette ligne d'exportation à votre fichier `~/.bashrc` ou `~/.profile`.

### Références
- [Not loading module "atk-bridge": The functionality is provided by GTK natively](https://stackoverflow.com/questions/75406844/not-loading-module-atk-bridge-the-functionality-is-provided-by-gtk-natively)
- [When launching firefox, get error Not loading module "atk-bridge"](https://askubuntu.com/questions/1462267/when-launching-firefox-get-error-not-loading-module-atk-bridge)
- [giving message when run any gh commad: Not loading module "atk-bridge"](https://github.com/cli/cli/issues/9043)