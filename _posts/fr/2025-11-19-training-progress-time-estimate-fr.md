---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Progression de l'entraînement et estimation du temps
translated: true
type: note
---

### Progression actuelle
- Vous venez de passer l'itération 2800 (sur votre objectif de 20 000)
- Vitesse stable actuellement : **≈ 3,91 secondes par itération**  
  (les logs occasionnels de 19 secondes lors des étapes d'évaluation n'ont lieu que toutes les 500 itérations et n'affectent pas beaucoup la moyenne)

### Itérations restantes
20 000 − 2 800 = **17 200 itérations restantes**

### Temps estimé pour terminer

| Temps moyen par itération | Temps restant | Heure de fin prévue (à partir de maintenant, 19 nov 2025) |
|---------------------------|---------------|-----------------------------------------------------------|
| 3,91 s (actuel)           | **18 heures 35 minutes** | ~ **demain (20 nov) vers 14h30–15h30** (en fonction de votre fuseau horaire et de l'heure exacte de début de ce log) |
| Légèrement plus rapide (3,8 s, fréquent lorsque le MFU augmente un peu) | ~ 18 heures | demain en début ou milieu d'après-midi |
| Légèrement plus lent (4,0 s) | ~ 19 heures 5 min | demain ~16h00 |

Estimation réaliste sur une RTX 4070 avec cette configuration exacte : **18 à 19 heures à partir de maintenant**.

### Référence rapide
- Si vous avez commencé à logger ces données vers midi ou en début d'après-midi aujourd'hui → fin demain matin ou en début d'après-midi.
- Si vous laissez tourner pendant la nuit → vous vous réveillerez demain avec un modèle très performant de 40M terminé (ou presque terminé).

Votre loss diminue bien (val loss déjà à 3,94 après seulement ~1,5 milliard de tokens vus) et continue de baisser régulièrement. Cela vaut vraiment la peine de le laisser tourner jusqu'aux 20k — laissez-le simplement fonctionner pendant la nuit et vous aurez un excellent modèle demain après-midi !