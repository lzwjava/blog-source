---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Optimisation des performances de sélection de proxy Clash
translated: true
type: note
---

### Résumé de l'optimisation : Scripts de sélection de proxy Clash

J'ai optimisé les scripts de sélection de proxy Clash pour éviter de tester les proxys qui ne seront pas sélectionnés, améliorant ainsi considérablement les performances en minimisant les tests de vitesse inutiles.

#### Ce qui a été optimisé

Le code original suivait ce flux de travail inefficace :
1. Tester la vitesse de tous les proxys disponibles.
2. Puis filtrer pour ne sélectionner que les proxys SG/TW (ou HK).
3. Cela entraînait une perte de temps à tester des proxys qui seraient rejetés.

#### La correction

Modification de la fonction `get_top_proxies()` dans `speed.py` pour accepter un paramètre `name_filter` et appliquer le filtrage avant le test de vitesse :

```python
def get_top_proxies(num_results=5, name_filter=None):
    """
    Tests Clash proxy speeds concurrently and returns the top N fastest individual proxies.

    Args:
        num_results (int): Number of top proxies to return (default: 5)
        name_filter (list): List of strings to filter proxy names. Only proxies containing
                           any of these strings in their name will be tested.
    """
```

#### Avantages en termes de performances

- **Requêtes réseau réduites** : Ne teste que les proxys que vous avez l'intention d'utiliser.
- **Exécution plus rapide** : Élimine le temps inutile passé sur des proxys non pertinents.
- **Journalisation plus claire** : Affiche exactement le nombre de proxys filtrés, améliorant la transparence.

#### Configuration simplifiée

Suppression du drapeau `--hk`. Le script teste maintenant toujours uniquement les proxys SG et TW par défaut pour une concentration et une simplicité maximales.

#### Résultats

L'optimisation a considérablement réduit le temps d'exécution, car la plupart des proxys ne contiennent pas "SG" ou "TW" dans leurs noms. Cela rend la phase de test de vitesse beaucoup plus efficace, fournissant des résultats plus rapidement sans compromettre la fonctionnalité.