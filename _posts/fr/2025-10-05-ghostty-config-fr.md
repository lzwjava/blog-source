---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Configuration du Shell Ghostty
translated: true
type: note
---

### Ghostty et .bashrc sur Ubuntu

Ghostty se comporte de manière similaire au GNOME Terminal par défaut sur Ubuntu (et autres distributions Linux) en ce qui concerne le chargement de `.bashrc`. Par défaut, Ghostty lance des **shells interactifs non-login** pour bash, ce qui signifie qu'il source directement `~/.bashrc`—tout comme GNOME Terminal. C'est le comportement standard pour la plupart des terminaux Linux, où `.bashrc` gère la configuration du shell interactif (par exemple, les alias, les invites de commande, les variables d'environnement pour les sessions non-login).

#### Comment il charge .bashrc
- Lorsque vous ouvrez une nouvelle fenêtre ou un nouvel onglet Ghostty, il exécute `bash` (ou votre shell par défaut) en tant que shell non-login.
- Bash vérifie et source `~/.bashrc` si le shell est interactif (ce qui est le cas par défaut).
- Si vous avez un `~/.bash_profile` (typiquement pour les shells login), il ne sera pas sourcé à moins que vous ne configuriez explicitement Ghostty pour lancer un shell login (par exemple, en ajoutant `initial-command = bash --login` à `~/.config/ghostty/config`).
- Problèmes potentiels : Certains utilisateurs signalent que `.bashrc` ne se charge pas au premier lancement pour les nouveaux utilisateurs ou dans des configurations spécifiques (par exemple, les sessions SSH distantes sur Ubuntu). Cela peut souvent être résolu en s'assurant qu'aucun `~/.bash_profile` conflictuel n'existe, ou en le sourçant manuellement dans votre configuration. Ajouter une garde dans `.bashrc` comme `[[ $- != *i* ]] && return` peut éviter des problèmes dans des contextes non interactifs.

En bref, oui—Ghostty est identique au Terminal par défaut pour l'utilisation de `.bashrc` sur Ubuntu, avec le même comportement non-login par défaut.

### Ghostty sur macOS : .zprofile ou .bash_profile ?

Sur macOS, Ghostty suit la tradition de la plateforme (comme Terminal.app) et lance par défaut des **shells login**, quel que soit le shell. Cela affecte quel profil est chargé :

- **Si vous utilisez zsh (par défaut sur macOS depuis Catalina)** : Il source `~/.zprofile` (pour la configuration login) *et* `~/.zshrc` (pour la configuration interactive) à chaque fois qu'un nouveau terminal s'ouvre.
- **Si vous utilisez bash** : Il source `~/.bash_profile` (shell login). Bash ne sourcera pas `~/.bashrc` directement ici—`~/.bashrc` est uniquement pour les shells interactifs non-login. Pour inclure le contenu de `.bashrc`, ajoutez ceci à votre `~/.bash_profile` :
  ```
  if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
  ```

Ainsi, il charge `~/.zprofile` pour la configuration zsh par défaut, ou `~/.bash_profile` si vous utilisez bash. Vous pouvez changer de shell ou ajuster via la configuration de Ghostty si nécessaire.

[Intégration du Shell - Ghostty](https://ghostty.org/docs/features/shell-integration)  
[Shells Login macOS - Ghostty](https://ghostty.org/docs/help/macos-login-shells)  
[Bug potentiel, .bashrc non lu au démarrage - Discussion GitHub](https://github.com/ghostty-org/ghostty/discussions/3437)  
[Fichiers de Démarrage Bash - Manuel GNU](https://www.gnu.org/software/bash/manual/bash.html#Bash-Startup-Files)