---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Estimation du temps de formation : 57 minutes'
translated: true
type: note
---

### Progression actuelle
- L'entraînement a terminé 1300 itérations sur 20 000 au total (`max_iters = 20000`).
- Itérations restantes : 18 700.
- Temps moyen par itération sans évaluation : ~170 ms (basé sur les logs pour les itérations 100–1300).
- L'évaluation a lieu toutes les 500 itérations (`eval_interval = 500`), avec `eval_iters = 200` échantillons. Celles-ci ajoutent une surcharge significative, rendant les temps des "itérations d'évaluation" ~5.7–6 secondes (les logs indiquent 5.7s à l'itération 1000 et 6s à l'itération 500, incluant le batch d'entraînement + l'évaluation).

### Évaluations restantes
- Prochaine évaluation à l'itération 1500, puis 2000, ..., jusqu'à 20 000.
- Total des évaluations restantes : 38.
- Temps supplémentaire par évaluation : ~5.8 secondes (au-delà de l'étape d'entraînement standard de 170 ms).

### Estimation du temps
- Temps pour 18 662 itérations normales : ~3 172 secondes (53 minutes).
- Temps pour 38 itérations d'évaluation : ~228 secondes (3.8 minutes, durée complète).
- **Temps restant total : ~3 400 secondes (57 minutes)**.
  - Ceci suppose un matériel constant (RTX 4070 à 100% d'utilisation, comme indiqué dans `nvidia-smi`), aucune interruption et aucune sauvegarde/point de contrôle supplémentaire (qui ajoute une surcharge mineure si la validation s'améliore).
  - Fourchette : 50–65 minutes, tenant compte de légères variations dans les temps d'itération (les logs montrent 168–186 ms) ou d'un écrêtage thermique du GPU.

L'entraînement devrait se terminer vers 03:25–03:35 heure locale (sur la base de votre horodatage `nvidia-smi` de 02:30). Surveillez toute erreur OOM ou ralentissement, mais avec votre configuration (batch_size=16, gradient_accumulation_steps=4, block_size=512) et une utilisation de 12 Go de VRAM (6.5 Go / 12 Go), cela semble stable.