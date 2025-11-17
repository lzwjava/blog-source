---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Surveillance de l'utilisation du GPU avec nvidia-smi
translated: true
type: note
---

Pour surveiller l'utilisation du GPU au fil du temps avec `nvidia-smi`, vous avez seulement besoin de l'option de boucle :

**Rafraîchissement en direct basique**

```
nvidia-smi -l 1
```

Cela se met à jour toutes les 1 seconde. Vous pouvez remplacer `1` par n'importe quel intervalle en secondes.

**Si vous voulez des statistiques plus détaillées (utilisation par processus)**

```
nvidia-smi pmon -s um -d 1
```

Cela affiche l'utilisation du GPU (`u`) et la mémoire (`m`) par processus chaque seconde.

**Si vous voulez des statistiques complètes du GPU de manière répétée**

```
nvidia-smi --query-gpu=timestamp,utilization.gpu,utilization.memory,memory.used,memory.total --format=csv -l 1
```

Cela imprime une ligne compacte chaque seconde avec l'utilisation et la mémoire.

Dites-moi si vous souhaitez que la sortie soit enregistrée dans un fichier ou si vous avez besoin d'un format personnalisé.