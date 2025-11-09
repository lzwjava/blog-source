---
audio: false
date: 2025-09-07
generated: true
image: false
lang: fr
layout: post
title: Choisir la Bonne Version d'IntelliJ
translated: true
type: note
---

À partir de votre sortie `uname -a` :

```
Linux to 6.8.0-60-generic ... x86_64 x86_64 x86_64 GNU/Linux
```

Ce `x86_64` signifie que l'architecture de votre CPU est **Intel/AMD 64 bits (x86-64)**, et non ARM.

Donc, lorsque vous téléchargez IntelliJ IDEA (ou n'importe quel IDE JetBrains), vous devez choisir la version **Linux (x64 / x86-64)**, et non celle pour ARM64.

Les versions **Linux ARM64** sont uniquement destinées aux appareils avec des processeurs ARM (comme les Mac Apple Silicon, certains serveurs récents ou les ordinateurs portables ARM).

👉 En bref :

* **Votre machine** → `x86_64` → utilisez **Linux x64**
* **Pas votre machine** → Puces ARM (Mac M1/M2, certains serveurs ARM) → utilisez **Linux ARM64**

Voulez-vous que je vous montre aussi une commande rapide pour revérifier le type de votre CPU (par exemple, `lscpu` ou `arch`) afin que vous soyez sûr à 100 % ?