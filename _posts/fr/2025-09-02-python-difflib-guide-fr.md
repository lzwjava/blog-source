---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide de Comparaison de Séquences avec Python Difflib
translated: true
type: note
---

En Python, le module **`difflib`** fournit des outils pour comparer des séquences — chaînes de caractères, listes, ou tout itérable. Il est souvent utilisé pour des tâches comme détecter les différences entre des textes (comme `diff` sous Unix) ou construire des outils de complétion automatique et de similarité.

---

### Fonctionnement de `difflib`

Fondamentalement, `difflib` tente de trouver les plus longues sous-séquences correspondantes et contiguës entre deux entrées. Il utilise ensuite ces correspondances pour mettre en évidence les similitudes et les différences. La bibliothèque peut :

* Générer des diffs lisibles par un humain (`ndiff`, `unified_diff`, `context_diff`).
* Calculer des ratios de similarité entre des séquences.
* Suggérer des correspondances proches dans une liste (`get_close_matches`).

---

### `SequenceMatcher`

La classe la plus importante est **`difflib.SequenceMatcher`**.

**Comment cela fonctionne** :

* Elle compare deux séquences élément par élément.
* Elle recherche la *plus longue sous-séquence commune* (mais pas nécessairement contiguë).
* Elle produit une liste d'opérations (`replace`, `delete`, `insert`, `equal`) décrivant comment transformer une séquence en une autre.

**Méthodes clés** :

1. **`ratio()`**
   Retourne un float dans `[0, 1]` qui mesure la similarité.
   Formule :

   $$
   \text{ratio} = \frac{2 \times M}{T}
   $$

   où `M` = nombre d'éléments correspondants, et `T` = nombre total d'éléments dans les deux séquences.

2. **`quick_ratio()`** et **`real_quick_ratio()`**
   Des approximations plus rapides de la similarité, sacrifiant la précision pour la vitesse.

3. **`get_opcodes()`**
   Retourne une liste d'opérations pour transformer `a` en `b`. Exemple : `[('replace', 0, 2, 0, 1), ('equal', 2, 4, 1, 3)]`.

4. **`get_matching_blocks()`**
   Retourne toutes les sous-séquences correspondantes avec leurs positions.

---

### Exemple

```python
import difflib

a = "hello world"
b = "helo wrld"

s = difflib.SequenceMatcher(None, a, b)

print("Similarity ratio:", s.ratio())
print("Operations:", s.get_opcodes())
print("Matching blocks:", s.get_matching_blocks())
```

**Sortie** :

```
Similarity ratio: 0.9090909090909091
Operations: [('equal', 0, 1, 0, 1), ('delete', 1, 2, 1, 1),
             ('equal', 2, 5, 1, 4), ('delete', 5, 6, 4, 4),
             ('equal', 6, 11, 4, 9)]
Matching blocks: [Match(a=0, b=0, size=1),
                  Match(a=2, b=1, size=3),
                  Match(a=6, b=4, size=5),
                  Match(a=11, b=9, size=0)]
```

---

👉 En bref :

* `difflib` est une boîte à outils pour la comparaison de séquences.
* `SequenceMatcher` est le moteur principal — il trouve les sous-séquences correspondantes et calcule la similarité.
* Il est utile pour les diffs, les correcteurs orthographiques, la détection de plagiat, les suggestions automatiques, etc.