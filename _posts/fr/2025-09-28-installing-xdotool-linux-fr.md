---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Installation et utilisation de xdotool sur Linux
translated: true
type: note
---

Pour installer `xdotool` sur votre système Linux, vous pouvez utiliser le gestionnaire de paquets de votre distribution. D'après votre hostname qui indique "XiaoXin", vous utilisez probablement Ubuntu ou une distribution basée sur Debian. Voici les commandes d'installation pour les distributions Linux courantes :

## Ubuntu/Debian :
```bash
sudo apt update
sudo apt install xdotool
```

## CentOS/RHEL/Fedora :
```bash
# Pour les versions récentes (dnf)
sudo dnf install xdotool

# Pour les versions plus anciennes (yum)
sudo yum install xdotool
```

## Arch Linux :
```bash
sudo pacman -S xdotool
```

## openSUSE :
```bash
sudo zypper install xdotool
```

Après l'installation, vous pouvez vérifier qu'elle fonctionne en exécutant :
```bash
xdotool --version
```

Une fois installé, votre script Python devrait pouvoir utiliser `xdotool` pour récupérer le titre du navigateur. L'utilitaire `xdotool` est couramment utilisé pour automatiser les tâches du bureau X11, y compris l'obtention des titres de fenêtres, ce que votre script semble essayer de faire.

Si vous rencontrez toujours des problèmes après l'installation, assurez-vous que :
1. Vous exécutez le script dans un environnement X11 (pas Wayland)
2. Vous avez une fenêtre de navigateur ouverte
3. La fenêtre du navigateur a le focus ou est visible