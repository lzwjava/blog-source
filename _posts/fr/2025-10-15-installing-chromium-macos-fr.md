---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation de Chromium sur macOS
translated: true
type: note
---

Oui, macOS peut tout à fait installer Chromium comme alternative à Google Chrome. Chromium est le fondement open-source sur lequel Chrome est construit, il est donc très similaire en termes de fonctionnalités mais manque de certaines fonctionnalités propriétaires de Google comme les mises à jour automatiques et certains codecs.

### Comment l'installer
Il existe plusieurs méthodes simples :

1. **Via Homebrew (la plus simple pour la plupart des utilisateurs)** :
   - Installez Homebrew si vous ne l'avez pas déjà fait : `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
   - Puis exécutez : `brew install --cask chromium`.
   - Cela fonctionne sur les Macs Intel et Apple Silicon (M1/M2/M3).

2. **Téléchargement direct** :
   - Allez sur le site officiel de Chromium et téléchargez la dernière version pour Mac.
   - Décompressez le fichier et glissez l'application dans votre dossier Applications.

3. **Pour les développeurs ou les versions personnalisées** :
   - Utilisez des outils comme Woolyss pour les versions pré-compilées, ou compilez à partir des sources si nécessaire (nécessite Xcode).

Une fois installé, vous pouvez définir Chromium comme votre navigateur par défaut dans Réglages Système > Bureau et Dock > Navigateur internet par défaut.

[Télécharger Chromium](https://www.chromium.org/getting-involved/download-chromium/)  
[Formule Homebrew](https://formulae.brew.sh/cask/chromium)  
[Installation sur Apple Silicon](https://dev.to/pixelrena/installing-chromium-on-mac-apple-m2-pro-tutorial-4i4i)  
[Téléchargement MacUpdate](https://chromium.macupdate.com/)  
[Dernières versions](https://chromium.woolyss.com/download/en/)