---
audio: false
date: 2025-09-13
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: GitHub Pages Nécessite des Dépôts Publics
translated: true
type: note
---

Exactement — si vous rendez votre dépôt GitHub Pages privé, vous perdez l'hébergement gratuit GitHub Pages.

GitHub Pages ne fonctionne automatiquement que lorsque le dépôt est **public**. Si le dépôt est privé, le site `github.io` ne sera pas publié, sauf si vous êtes sur un **plan GitHub Enterprise avec Pages activé pour les dépôts privés** (c'est une fonctionnalité payante, non incluse dans les comptes personnels gratuits ou standard).

Donc, pour votre blog personnel à `username.github.io` :

* **Dépôt public** → GitHub Pages le construit et le sert à l'adresse `https://username.github.io/`.
* **Dépôt privé (compte gratuit)** → GitHub Pages est désactivé.
* **Dépôt privé (Enterprise)** → Fonctionne toujours, mais seulement si votre organisation active Pages pour les dépôts privés.

Souhaitez-vous que j'explique également une solution alternative (comme garder votre dépôt principal privé mais synchroniser uniquement la sortie `_site` vers un dépôt public séparé pour la publication) ?