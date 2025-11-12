---
audio: false
generated: false
lang: fr
layout: post
title: Deepseek - Conversation
translated: true
type: note
---

A : Je parcourais le rapport technique de DeepSeek-V3, et je suis vraiment impressionné par l'échelle de ce modèle. 671 milliards de paramètres, mais seulement 37 milliards activés par token ? C'est une architecture MoE massive. Comment est-ce que cela fonctionne ?

B : Oui, c'est tout un exploit ! DeepSeek-V3 est construit sur le framework Mixture-of-Experts (MoE), qui lui permet de n'activer qu'un sous-ensemble de paramètres pour chaque token. Plus précisément, il utilise 256 experts routés, mais seulement 8 sont activés par token. Cela le rend inc