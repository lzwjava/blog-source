---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Clé GPG de vérification de l'ISO d'Arch Linux
translated: true
type: note
---

Vous avez cette clé GPG (celle appartenant à Pierre Schmitz, avec l'empreinte `3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C`) dans votre trousseau de clés car c'est la clé de signature officielle utilisée par les développeurs d'Arch Linux pour signer cryptographiquement leurs images ISO. Cela garantit que le téléchargement est authentique et n'a pas été altéré.

Lorsque vous prépariez un lecteur USB amorçable pour installer Arch Linux sur macOS (probablement en suivant le guide officiel du wiki Arch), le processus standard implique deux étapes pour la vérification :
1. Télécharger l'ISO et son fichier `.sig`.
2. Importer la clé GPG du développeur concerné (dans ce cas, celle de Pierre Schmitz, car il est l'un des signataires principaux pour les ISO récentes) pour vérifier la signature avec une commande comme `gpg --verify archlinux-AAAA.MM.JJ-x86_64.iso.sig`.

Vous avez probablement exécuté quelque chose comme `gpg --keyserver hkps://keys.openpgp.org --recv-keys 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C` pour récupérer et l'importer, ce qui l'a ajoutée de façon permanente à votre trousseau de clés GPG local. C'est pourquoi elle apparaît dans `gpg --list-keys`.

C'est inoffensif — les clés GPG sont juste des données publiques à des fins de vérification — et de nombreux utilisateurs d'Arch se retrouvent avec quelques-unes de ces clés après avoir vérifié des ISO. Si vous n'en avez plus besoin et souhaitez la supprimer, exécutez :
```
gpg --delete-key 3E80CA1A8B89F69CBA57D98A76A5EF9054449A5C
```
(Il vous sera demandé de confirmer ; cela supprime uniquement la clé publique, pas les signatures que vous avez déjà vérifiées.)

[Page de téléchargement des ISO d'Arch Linux](https://archlinux.org/download/)  
[Arch Wiki : Installer Arch Linux sur un Mac](https://wiki.archlinux.org/title/Install_Arch_Linux_on_Mac)  
[Clés GPG de Pierre Schmitz](https://pierre-schmitz.com/gpg-keys/)