---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Estimation de la consommation électrique et du coût des GPU
translated: true
type: note
---

En utilisant le nombre affiché dans votre sortie :

Votre GPU consomme **environ 205 watts** pendant l'exécution.

Un « degré d'électricité » = **1 kWh**.

**Si seul le GPU était pris en compte :**

* **1 heure :** 205 W ≈ **0,205 kWh**
* **24 heures :** 0,205 × 24 ≈ **4,92 kWh**

Cependant, une machine réelle inclut également le CPU, la carte mère, la RAM, les ventilateurs, le SSD, les pertes de l'alimentation, etc.
Une configuration type pour l'entraînement avec une 4070 consomme généralement **300–380 W au total** à la prise.

Si nous utilisons une estimation plus réaliste de l'ensemble du système, disons environ **320 W** en moyenne :

* **1 heure :** 0,32 kWh
* **24 heures :** 7,68 kWh

Si votre charge de travail maintient le GPU à 100 % tout le temps, attendez-vous à ce que votre facture réelle se situe dans cette fourchette pour l'ensemble du système plutôt que sur le chiffre du GPU seul.

Si vous le souhaitez, vous pouvez me communiquer votre modèle d'alimentation, votre type de CPU et le nombre de ventilateurs/disques, et je pourrai l'estimer plus précisément.