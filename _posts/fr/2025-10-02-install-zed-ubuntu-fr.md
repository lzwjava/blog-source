---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Installer Zed sur Ubuntu 24.04
translated: true
type: note
---

Pour Ubuntu 24.04 LTS, la méthode d'installation la plus simple et officielle pour Zed (l'éditeur de code haute performance) est via leur script shell fourni, qui fonctionne nativement sur la plupart des distributions Linux, y compris celles basées sur Debian comme Ubuntu. Il gère les dépendances automatiquement et garantit que vous obtenez la dernière version stable.

### Installation Recommandée : Script Officiel
Exécutez ceci dans votre terminal :
```
curl -f https://zed.dev/install.sh | sh
```
- Ceci installe Zed dans `~/.local/bin/zed` (ajoutez-le à votre PATH si nécessaire : `export PATH="$HOME/.local/bin:$PATH"` dans `~/.bashrc` ou similaire).
- Prérequis : Votre système (glibc 2.39 sur le noyau 6.14) répond aux exigences (x86_64 glibc >= 2.31).
- Après l'installation, lancez avec `zed` ou depuis le menu d'applications de GNOME.
- Pour le canal de préversion (versions nocturnes) : `curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`.

Si vous préférez un package universel et sandboxé (aucune dépendance native à gérer), utilisez l'option Flathub de votre liste (`dev.zed.Zed`) via Flatpak :
1. Installez Flatpak s'il n'est pas présent : `sudo apt update && sudo apt install flatpak`.
2. Ajoutez le dépôt Flathub : `flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`.
3. Installez : `flatpak install flathub dev.zed.Zed`.
4. Exécutez : `flatpak run dev.zed.Zed`.

Le script est généralement plus rapide et mieux intégré pour un bureau comme GNOME, mais Flatpak est excellent si vous souhaitez l'isolation ou l'utilisez déjà pour d'autres applications. Évitez les autres options de votre liste, car elles sont destinées à des distributions non-Debian et ne fonctionneront pas directement sur Ubuntu sans configuration supplémentaire.

### Références
- [Documentation d'installation de Zed sur Linux](https://zed.dev/docs/linux)
- [Annonce de Zed sur Linux](https://zed.dev/linux)
- [Packages Zed sur Repology](https://repology.org/project/zed-editor/versions)