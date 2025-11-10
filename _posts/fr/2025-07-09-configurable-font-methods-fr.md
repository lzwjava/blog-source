---
audio: false
generated: true
lang: fr
layout: post
title: Polices configurables dans LaTeX
translated: true
type: note
---

Vous pouvez rendre la police configurable en créant des variables au début de votre document LaTeX. Voici quelques approches :

## Méthode 1 : Variables simples (Recommandée)

## Méthode 2 : Utilisation de conditionnels pour différents systèmes

Permettez-moi de créer une version plus sophistiquée avec une détection automatique du système d'exploitation :

## Méthode 3 : Utilisation d'un fichier de configuration séparé

Vous pouvez également créer un fichier séparé pour la configuration des polices :

Et ensuite, dans votre document principal :

## Alternatives courantes de polices pour Linux

Voici quelques bonnes alternatives de polices pour les systèmes Linux :

**Pour les polices chinoises/CJK :**
- `Noto Sans CJK SC` (recommandé)
- `Source Han Sans SC`
- `WenQuanYi Micro Hei`
- `Droid Sans Fallback`

**Pour les polices anglaises :**
- `Liberation Serif` (alternative à Times New Roman)
- `DejaVu Serif`
- `Linux Libertine`
- `TeX Gyre Termes`

## Utilisation

1. **La méthode 1** est la plus simple - il suffit de décommenter les lignes de polices Linux lorsque nécessaire
2. **La méthode 2** vous permet de changer une seule variable (`\fontsystem`) pour basculer entre différents systèmes
3. **La méthode 3** garde la configuration des polices séparée, facilitant la maintenance de différentes versions

Choisissez la méthode qui correspond le mieux à votre flux de travail !