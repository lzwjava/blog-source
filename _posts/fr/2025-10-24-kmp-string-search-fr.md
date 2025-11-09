---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Algorithme KMP Recherche Efficace de Chaînes
translated: true
type: note
---

### Comprendre l'algorithme de Knuth-Morris-Pratt (KMP)

Votre intuition est tout à fait juste : KMP consiste à **ne pas gaspiller les correspondances partielles** lors de la recherche de chaînes. Lorsque vous cherchez un motif (comme "abc") dans un texte plus long (comme "ababcabc"), l'approche naïve recommence depuis le début à chaque fois qu'il y a une non-correspondance, ce qui est inefficace. KMP "se souvient" intelligemment de la partie du motif que vous avez déjà fait correspondre et saute en avant, évitant ainsi les comparaisons redondantes. Cela le rend super rapide—temps linéaire, O(n + m), où n est la longueur du texte et m la longueur du motif.

Je vais le décomposer étape par étape avec un exemple simple. Nous allons chercher le motif `P = "abab"` dans le texte `T = "ababababc"`. (Il apparaît aux positions 0, 2 et 4.)

#### Étape 1 : Le Problème et l'Approche Naïve
- **Objectif** : Trouver toutes les positions de départ où `P` correspond entièrement dans `T`.
- **Manière naïve** : Faire glisser `P` sur `T`, en comparant caractère par caractère. Si non-correspondance à la position i dans `P`, décaler `P` de 1 et réessayer depuis le début de `P`.
  - Pour notre exemple :
    - Commencer à T[0] : "a"=="a" (correspond), "b"=="b" (correspond), "a"=="a" (correspond), "b"=="b" (correspond) → Trouvé à 0.
    - Décaler vers T[1] : "b"=="a" ? Non → Redémarrer `P` au début. Gaspillage !
    - T[2] : "a"=="a", "b"=="b", "a"=="a", "b"=="b" → Trouvé à 2.
    - T[3] : "a"=="a", "b"=="b", "a"=="a", "b"=="a" ? Non → Redémarrer.
    - Et ainsi de suite. Beaucoup de retour en arrière vers le char 0 de `P`.

Cela peut être O(n*m) dans le pire des cas (par exemple, chercher "aaaaa...a" pour "aaa...ab").

#### Étape 2 : L'Idée Clé de KMP – La Table des Préfixes (ou "Fonction d'Échec")
KMP précalcule une table `π` (pi) pour le motif `P`. Cette table vous indique, pour chaque position i dans `P`, **le plus long préfixe propre de `P[0..i]` qui est aussi un suffixe**. En d'autres termes : "Si nous avons une non-correspondance ici, quelle partie de la correspondance partielle pouvons-nous réutiliser en sautant vers ce préfixe qui se chevauche ?"

- **Préfixe/suffixe propre** : Un préfixe/suffixe qui n'est pas la chaîne entière (par exemple, pour "aba", le préfixe "a" correspond au suffixe "a").
- Pourquoi ? Cela vous permet de "faire glisser" le motif de plus de 1 en cas de non-correspondance, en réutilisant le chevauchement au lieu de redémarrer.

Pour `P = "abab"` :
- Construire `π` étape par étape (nous allons bientôt le coder).

| Position i | P[0..i] | Plus long préfixe propre = suffixe | π[i] |
|------------|---------|------------------------------------|------|
| 0          | "a"     | Aucun (caractère unique)           | 0    |
| 1          | "ab"    | Aucun                              | 0    |
| 2          | "aba"   | "a" (préfixe "a" == suffixe "a")   | 1    |
| 3          | "abab"  | "ab" (préfixe "ab" == suffixe "ab") | 2  |

- π[2] = 1 signifie : Si vous avez fait correspondre "aba" mais que le caractère suivant ne correspond pas, faites comme si vous aviez fait correspondre le préfixe "a" (longueur 1) jusqu'à présent.
- π[3] = 2 signifie : Pour "abab" entier, chevauchement de "ab".

#### Étape 3 : Construction de la Table des Préfixes (π)
Cela se fait en temps O(m). C'est comme chercher `P` contre lui-même, en utilisant une logique similaire.

Pseudocode :
```
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0  # Longueur de la correspondance préfixe-suffixe actuelle
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k-1]  # Sauter vers le chevauchement précédent (réutiliser !)
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi
```

- Commencer avec π[0] = 0.
- Pour chaque i=1 à m-1 :
  - Essayer d'étendre la longueur de correspondance actuelle k.
  - En cas de non-correspondance, revenir à π[k-1] (ne pas gaspiller—réutiliser le chevauchement précédent).
  - En cas de correspondance, k++.

Pour "abab" :
- i=1: P[0]='a' != P[1]='b' → k=0, π[1]=0.
- i=2: P[0]='a' == P[2]='a' → k=1, π[2]=1.
- i=3: P[1]='b' == P[3]='b' → k=2, π[3]=2.

#### Étape 4 : Recherche avec la Table des Préfixes
Maintenant, rechercher `T` avec `P` et `π` :
- Garder une variable `q` = état actuel (longueur du préfixe correspondant jusqu'à présent).
- Pour chaque caractère dans `T` :
  - Tant que non-correspondance et q>0, définir q = π[q-1] (reculer intelligemment).
  - Si correspondance, q++.
  - Si q == m, trouvé ! Puis q = π[q-1] pour continuer pour les chevauchements.

Pseudocode :
```
def kmp_search(T, P):
    n, m = len(T), len(P)
    if m == 0: return []
    pi = compute_prefix_function(P)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q-1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)  # Position de départ
            q = pi[q-1]  # Chevauchement pour la recherche suivante
    return matches
```

Pour `T = "ababababc"`, `P = "abab"` :
- i=0: 'a'=='a' → q=1
- i=1: 'b'=='b' → q=2
- i=2: 'a'=='a' → q=3
- i=3: 'b'=='b' → q=4 == m → Correspondance à 0, q=π[3]=2
- i=4: Maintenant q=2, T[4]='a' == P[2]='a' → q=3
- i=5: 'b'=='b' → q=4 == m → Correspondance à 2, q=2
- i=6: q=2, 'a'=='a' → q=3
- i=7: q=3, 'b' == P[3]='b' → q=4 == m → Correspondance à 4, q=2
- i=8: q=2, 'c' != P[2]='a' → q = π[1]=0

Voir ? Sur les non-correspondances (comme s'il y en avait une), il saute q=π[q-1] au lieu de q=0.

#### Pourquoi Cela Semble Magique
- Aucun retour en arrière dans `T`—vous ne vous déplacez que vers l'avant.
- La boucle "while" pour les non-correspondances s'exécute en temps amorti O(1) au total, car chaque saut diminue q, et q augmente au plus n fois.

#### Essayez Par Vous-Même : Code Python Simple
```python
def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and P[k] != P[i]:
            k = pi[k - 1]
        if P[k] == P[i]:
            k += 1
        pi[i] = k
    return pi

def kmp_search(T, P):
    n, m = len(T), len(P)
    if m == 0: return []
    pi = compute_prefix_function(P)
    q = 0
    matches = []
    for i in range(n):
        while q > 0 and P[q] != T[i]:
            q = pi[q - 1]
        if P[q] == T[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches

# Test
T = "ababababc"
P = "abab"
print(kmp_search(T, P))  # Sortie : [0, 2, 4]
```

Exécutez ceci—modifiez P/T pour voir les sauts en action (ajoutez des impressions pour q).

#### Pièges Courants & Conseils
- π[0] est toujours 0.
- Pour les motifs sans auto-chevauchements (par exemple, "abc"), π est tout à 0—revient à la méthode naïve.
- Excellent pour les séquences d'ADN ou la saisie semi-automatique de code.
- Si c'est encore flou, visualisez π comme une "machine à états" : chaque état est une longueur correspondante, transitions sur correspondance/non-correspondance.

Cela devrait maintenant faire sens—c'est juste un saut intelligent via des chevauchements précalculés. Si vous avez un exemple spécifique qui vous bloque, partagez-le !

[GeeksforGeeks: KMP Algorithm](https://www.geeksforgeeks.org/dsa/kmp-algorithm-for-pattern-searching/)  
[Wikipedia: Knuth–Morris–Pratt Algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm)