---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Problèmes d'Installation et de Lancement de Ghostty
translated: true
type: note
---

### Diagnostic du problème

D'après les logs que vous avez partagés, l'installation de Ghostty 1.1.3 via le package `.deb` a réussi, mais son lancement échoue pour deux raisons principales :

1. **Erreur d'argument CLI** : La commande `ghostty .` traite le `.` comme un champ de configuration invalide (probablement destiné à être un répertoire, mais Ghostty ne prend pas en charge cette syntaxe). Cela provoque la fermeture immédiate avec "invalid field".

2. **Problème de compatibilité OpenGL/GTK** : Lors de l'exécution de `ghostty` sans arguments, l'application s'initialise mais plante à cause de "OpenGL version is too old. Ghostty requires OpenGL 3.3" (votre système rapporte la version 3.2 à Ghostty). C'est un problème connu sur Ubuntu 22.04, particulièrement avec les pilotes NVIDIA sous X11. Bien que `glxinfo` affiche souvent OpenGL 4.6+, l'environnement d'exécution GTK 4.6 de Ghostty ne peut pas accéder correctement aux versions supérieures avec le GL NVIDIA. L'avertissement "GDK_DEBUG=vulkan-disable" est une tentative de contournement mais ne résout pas le problème fondamental. L'erreur Gtk-CRITICAL finale est un symptôme de l'échec de la réalisation de la surface.

Ce problème affecte de nombreux utilisateurs sur Ubuntu 22.04 (et ses dérivés comme Pop!_OS) en raison de l'ancienne version de GTK (4.6 par rapport à la version 4.12+ plus récente nécessaire pour une compatibilité complète avec NVIDIA).

### Vérifications rapides
- Vérifiez votre support OpenGL réel (installez `mesa-utils` si nécessaire : `sudo apt install mesa-utils`) :
  ```
  glxinfo | grep "OpenGL version"
  ```
  S'il rapporte 3.3+, le problème est bien spécifique à GTK/NVIDIA.
- Vérifiez votre type de session : `echo $XDG_SESSION_TYPE`. Si c'est `x11`, cela y contribue probablement.

### Solutions
Voici des corrections étape par étape, en commençant par la plus simple :

1. **Passer à Wayland (si vous avez des graphiques hybrides, par ex. Intel + NVIDIA)** :
   - Déconnectez-vous et sélectionnez une session Wayland à la connexion (ou ajoutez `WaylandEnable=true` dans `/etc/gdm3/custom.conf` et redémarrez GDM).
   - Exécutez Ghostty avec les graphiques intégrés : `prime-run --gpu intel ghostty` (installez `nvidia-prime` si nécessaire).
   - Cela contourne les problèmes NVIDIA X11 pour certains utilisateurs.

2. **Installer via Snap (Package alternatif plus simple)** :
   - Le `.deb` non officiel que vous avez utilisé peut hériter des particularités du système. Essayez le Snap officiel, qui regroupe les dépendances :
     ```
     sudo snap install ghostty --classic
     ```
   - Lancez avec `snap run ghostty`. Si OpenGL échoue toujours, passez aux mises à niveau.

3. **Mettre à niveau vers Ubuntu 24.04 (Recommandé pour une correction à long terme)** :
   - Ubuntu 24.04 inclut GTK 4.14+, résolvant la compatibilité NVIDIA.
   - Suivez le guide de mise à niveau officiel : `sudo do-release-upgrade`.
   - Après la mise à niveau, réinstallez Ghostty via le même `.deb` ou Snap. Les utilisateurs rapportent qu'il fonctionne parfaitement après la mise à niveau.

4. **Compiler à partir des sources avec le backend GLFW (Solution de contournement temporaire)** :
   - Cela utilise un environnement d'exécution non-GTK pour contourner le problème OpenGL (note : pas d'onglets, pour test uniquement).
     ```
     sudo apt install git zig libgtk-4-dev libadwaita-1-dev libharfbuzz-dev libpango1.0-dev libcairo2-dev libgdk-pixbuf-2.0-dev libglib2.0-dev libwayland-dev libxkbcommon-dev libinput-dev libudev-dev libseat-dev libpipewire-0.3-dev libsystemd-dev libx11-dev libxext-dev libxfixes-dev libxi-dev libxrandr-dev libxtst-dev libxdamage-dev libxcomposite-dev libxrender-dev libxcursor-dev libxinerama-dev libxss-dev libxv-dev libxxf86vm-dev libgl1-mesa-dev libegl1-mesa-dev libgles2-mesa-dev libgbm-dev libdrm-dev libvulkan-dev libclang-dev
     git clone https://github.com/ghostty-org/ghostty.git
     cd ghostty
     zig build -Doptimize=ReleaseFast -Dapp-runtime=glfw
     sudo cp zig-out/bin/ghostty /usr/local/bin/
     ```
   - Exécutez `ghostty`. Pour les fonctionnalités complètes, revenez à GTK une fois la mise à niveau effectuée.

### Conseils supplémentaires
- Mettez à jour vos pilotes NVIDIA : `sudo ubuntu-drivers autoinstall` (ou utilisez manuellement la série 550+).
- Si vous êtes sur AMD/Intel uniquement, assurez-vous que Mesa est à jour : `sudo apt update && sudo apt upgrade mesa-vulkan-drivers`.
- Pour l'avertissement de configuration dans votre fichier de modèle (`~/.config/ghostty/config`), modifiez-le pour supprimer les lignes invalides (par ex., un `.` isolé).

Si aucune de ces solutions ne fonctionne, partagez votre sortie `glxinfo` ou les détails de votre GPU (`lspci | grep VGA`) pour des conseils plus personnalisés.

[OpenGL Too Old Discussion](https://github.com/ghostty-org/ghostty/discussions/3159)  
[Ghostty Ubuntu Builds](https://github.com/mkasberg/ghostty-ubuntu)  
[Ghostty Snap](https://snapcraft.io/ghostty)