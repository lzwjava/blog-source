---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Traceroute non installé par défaut
translated: true
type: note
---

Traceroute est définitivement disponible sur Linux — c'est un outil de diagnostic réseau standard qui trace l'itinéraire que prennent les paquets pour atteindre une destination. Cependant, il est souvent **non installé par défaut** dans de nombreuses distributions modernes (comme Ubuntu, Fedora, ou les installations minimales de Debian) pour garder les systèmes de base légers. C'est pourquoi il n'apparaît pas dans votre complétion par tabulation pour "trac".

### Correction Rapide
Installez-le via votre gestionnaire de paquets :
- **Debian/Ubuntu** : `sudo apt update && sudo apt install traceroute`
- **Fedora/RHEL/CentOS** : `sudo dnf install traceroute` (ou `sudo yum install traceroute` sur les anciennes versions)
- **Arch** : `sudo pacman -S traceroute`

Une fois installé, taper `trac` + Tab devrait maintenant inclure `traceroute` dans la liste. Vous pouvez ensuite l'exécuter comme `traceroute example.com` pour tester.

Si vous êtes sur une configuration conteneurisée ou super-minimale (par exemple, Alpine Linux), elle pourrait utiliser `tr` comme alias ou nécessiter un paquet différent — faites-moi savoir votre distribution pour plus de détails !