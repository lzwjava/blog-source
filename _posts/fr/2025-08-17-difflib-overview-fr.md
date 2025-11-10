---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Présentation du module difflib de Python
translated: true
type: note
---

### Aperçu de difflib
Le module `difflib` dans la bibliothèque standard de Python compare des séquences (par exemple, des chaînes de caractères, des listes) pour trouver les différences. Il est utile pour des tâches comme la comparaison de texte, la génération de correctifs ou les vérifications de similarité. Les classes et fonctions clés incluent `Differ` (pour les différences détaillées), `SequenceMatcher` (pour les ratios et les correspondances) et les générateurs de diff comme `ndiff` et `unified_diff`.

### Importation et configuration de base
Aucune installation nécessaire — il est inclus par défaut.
```python
import difflib
```

### Fonctions et classes courantes

1. **`SequenceMatcher`** : Calcule les ratios de similarité et trouve les sous-séquences correspondantes.
   - À utiliser pour la correspondance approximative ou pour obtenir un score de similarité rapide.
   - Exemple :
     ```python
     seq1 = "abcdef"
     seq2 = "abcefg"
     matcher = difflib.SequenceMatcher(None, seq1, seq2)
     print("Ratio de similarité :", matcher.ratio())  # Sortie : ~0.83 (correspondance proche)
     print("Éléments communs :", matcher.find_longest_match(0, len(seq1), 0, len(seq2)))  # Trouver la plus longue correspondance
     ```
     - `ratio()` retourne un flottant (0 à 1) indiquant la similarité.
     - Des méthodes comme `get_matching_blocks()` listent les correspondances exactes.

2. **`Differ`** : Génère un diff lisible par un humain montrant les ajouts, suppressions et modifications ligne par ligne.
   - Idéal pour comparer des listes ou des chaînes multilignes.
   - Exemple :
     ```python
     text1 = ["ligne1", "ligne2", "ligne3"]
     text2 = ["ligne1", "ligne2 modifiée", "ligne3", "ligne4"]
     d = difflib.Differ()
     diff = list(d.compare(text1, text2))
     print("\n".join(diff))
     # Sortie :
     #   ligne1
     #   ligne2
     # - ligne3
     # + ligne2 modifiée
     # + ligne3  (attendre, la sortie réelle montre les modifications de ligne ; ajuster pour la précision)
     ```
     - Préfixes : `  ` (inchangé), `- ` (supprimé), `+ ` (ajouté), `? ` (différences à l'intérieur des lignes).

3. **`ndiff`** et **`unified_diff`** : Pour générer des diffs dans des formats spécifiques.
   - **`ndiff`** : Diff ligne par ligne simple comme `Differ`.
     ```python
     diff = list(difflib.ndiff(["a", "b"], ["a", "c"]))
     # Sortie : ['  a', '- b', '+ c']
     ```
   - **`unified_diff`** : Crée un format de diff unifié (comme les diffs Git), utile pour les correctifs.
     ```python
     diff = difflib.unified_diff(["a", "b"], ["a", "c"], fromfile='fichier1', tofile='fichier2')
     print("\n".join(diff))
     # Sortie :
     # --- fichier1
     # +++ fichier2
     # @@ -1,2 +1,2 @@
     #  a
     # -b
     # +c
     ```

### Conseils et bonnes pratiques
- **Normalisation** : Pour des comparaisons insensibles à la casse ou ignorant les espaces, prétraitez les entrées (par exemple, `text.lower()` ou `text.splitlines()`).
- **Performance** : Pour les longues séquences, utilisez `SequenceMatcher` avec `autojunk=False` pour désactiver les heuristiques de junk si ce ne sont pas des indésirables.
- **Intégration** : Combinez avec `filecmp` pour les comparaisons de fichiers ou utilisez dans les scripts de contrôle de version.
- **Avancé** : Explorez `HtmlDiff` pour les diffs formatés en HTML (rarement nécessaire mais disponible).

Pour la documentation complète, consultez la [page officielle de difflib de Python](https://docs.python.org/3/library/difflib.html). Si vous avez un cas d'utilisation spécifique, fournissez plus de détails pour des exemples adaptés.