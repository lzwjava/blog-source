---
audio: false
generated: true
lang: fr
layout: post
title: Codeforces 2108F
translated: true
type: note
---

Plongeons dans les raisons pour lesquelles le code Java fourni résout le problème des "Fallen Towers". Le problème implique un tableau de \\( n \\) tours, chacune ayant une hauteur \\( a_i \geq 0 \\). Vous pouvez abattre la tour à la position \\( i \\), ce qui augmente les hauteurs des \\( a_i \\) tours suivantes de 1 (ou moins s'il n'y a pas assez de tours restantes), puis fixe \\( a_i \\) à 0. L'objectif est d'abattre les \\( n \\) tours exactement une fois dans n'importe quel ordre, en garantissant que le tableau final est non décroissant (c'est-à-dire que pour tout \\( i < j \\), la hauteur à la position \\( i \\) est au plus égale à la hauteur à la position \\( j \\)). La sortie est le MEX maximum du tableau final, où le MEX est le plus petit entier non négatif absent du tableau.

---

### Analyse du Problème

1. **Définition de l'Opération** :
   - Abattre la tour \\( i \\) avec une hauteur \\( a_i \\) :
     - Augmente les hauteurs des tours aux positions \\( i+1, i+2, \dots, i+a_i \\) de 1 (si elles existent).
     - Fixe \\( a_i = 0 \\).
   - Chaque tour doit être abattue exactement une fois, dans n'importe quel ordre.
   - Si \\( a_i = 0 \\), abattre la tour \\( i \\) n'a aucun effet sur les autres tours.

2. **Tableau Final Non Décroissant** :
   - Après toutes les opérations, le tableau final \\( b_1, b_2, \dots, b_n \\) doit satisfaire \\( b_i \leq b_{i+1} \\) pour tout \\( i < n \\).

3. **MEX** :
   - Le MEX du tableau final est le plus petit entier non négatif \\( m \\) absent de \\( \{b_1, b_2, \dots, b_n\} \\).
   - Puisque le tableau est non décroissant, si le tableau contient les valeurs \\( 0, 1, 2, \dots, k-1 \\) (éventuellement avec des répétitions) mais pas \\( k \\), le MEX est \\( k \\).
   - L'objectif est de maximiser ce MEX.

4. **Interprétation du MEX** :
   - Pour que le MEX soit \\( m \\), le tableau final doit inclure tous les entiers de 0 à \\( m-1 \\) au moins une fois, et \\( m \\) ne doit pas apparaître.
   - Puisque le tableau est non décroissant, atteindre un MEX de \\( m \\) implique que le tableau final a des valeurs comme \\( 0, 0, \dots, 1, 1, \dots, m-1, m-1 \\), avec chaque entier de 0 à \\( m-1 \\) apparaissant au moins une fois, et aucune valeur \\( m \\) ou supérieure.

5. **Idée Clé** :
   - Le MEX \\( m \\) correspond à avoir au moins une position avec chaque valeur de 0 à \\( m-1 \\).
   - Équivalemment, pour un MEX de \\( m \\), nous avons besoin d'au moins \\( m \\) positions dans le tableau final telles que la position \\( i \\) ait une valeur au moins égale à \\( i - (n - m) \\), car :
     - Les \\( m \\) dernières positions (de l'indice \\( n-m+1 \\) à \\( n \\)) doivent couvrir les valeurs 0 à \\( m-1 \\).
     - La position \\( n-m+1 \\) devrait avoir une valeur au moins égale à 0, la position \\( n-m+2 \\) au moins égale à 1, ..., la position \\( n \\) au moins égale à \\( m-1 \\).
   - Cela se traduit par l'exigence que la hauteur finale à la position \\( i \\) soit au moins \\( \max(0, m - (n - i + 1)) = \max(0, m - n + i) \\).

---

### Approche de la Solution

Le code utilise une recherche binaire pour trouver le MEX maximum possible \\( m \\). Pour chaque candidat \\( m \\), il vérifie s'il est possible d'obtenir un tableau final non décroissant où chaque position \\( i \\) a une hauteur au moins égale à \\( \max(0, m - n + i) \\). Cela garantit que les \\( m \\) dernières positions peuvent couvrir les valeurs 0 à \\( m-1 \\), rendant le MEX au moins égal à \\( m \\).

#### Recherche Binaire
- **Plage** : Le MEX \\( m \\) est au moins 0 (cas d'un tableau vide) et au plus \\( n \\) (puisque nous avons besoin d'au moins \\( m \\) positions pour avoir les valeurs 0 à \\( m-1 \\)). Ainsi, on recherche \\( m \\) dans \\( [0, n] \\).
- **Fonction de Vérification** : Pour un \\( m \\) donné, déterminer s'il existe un ordre pour abattre les tours tel que le tableau final satisfasse :
  - \\( b_i \geq \max(0, m - n + i) \\) pour tout \\( i \\).
  - Le tableau est non décroissant.

#### Fonction de Vérification
La fonction de vérification simule s'il est possible d'atteindre les hauteurs requises en utilisant une approche par tableau de différences, en supposant que les tours peuvent être abattues dans n'importe quel ordre.

1. **Hauteurs Requises** :
   - Pour un MEX \\( m \\), la position \\( i \\) a besoin d'une hauteur finale \\( b_i \geq \text{need}_i \\), où :
     \\[
     \text{need}_i = \max(0, m - n + i)
     \\]
   - Cela garantit que les positions \\( n-m+1 \\) à \\( n \\) ont des hauteurs au moins égales à 0, 1, ..., \\( m-1 \\), respectivement.

2. **Tableau de Différences** :
   - Le code utilise un tableau de différences \\( d \\) pour suivre l'effet cumulatif des opérations.
   - Initialiser \\( d[i] = 0 \\) pour tout \\( i \\).
   - Pour chaque position \\( i \\) :
     - Calculer la somme cumulée : \\( d[i] += d[i-1] \\) (si \\( i > 0 \\)), représentant le nombre actuel de blocs supplémentaires à la position \\( i \\).
     - Vérifier si \\( d[i] \geq \text{need}_i \\). Si ce n'est pas le cas, il est impossible d'atteindre la hauteur requise, donc retourner \\( false \\).
     - Calculer la longueur de la plage affectée par l'abattage de la tour \\( i \\) :
       \\[
       \text{len} = d[i] - \text{need}_i + a_i
       \\]
       - \\( d[i] - \text{need}_i \\) : Blocs supplémentaires disponibles après avoir satisfait l'exigence minimale.
       - \\( a_i \\) : Le nombre de blocs contribués par la hauteur de la tour \\( i \\).
       - Ce \\( \text{len} \\) représente combien de positions à droite de \\( i \\) peuvent être incrémentées lorsque la tour \\( i \\) est abattue.
     - Mettre à jour le tableau de différences :
       - Incrémenter \\( d[i+1] \\) (si \\( i+1 < n \\)) pour démarrer l'effet de l'abattage de la tour \\( i \\).
       - Décrémenter \\( d[i + \text{len} + 1] \\) (si \\( i + \text{len} + 1 < n \\)) pour terminer l'effet après \\( \text{len} \\) positions.

3. **Faisabilité** :
   - Le tableau de différences simule l'effet d'abattre la tour \\( i \\) avec une hauteur modifiée basée sur l'état actuel.
   - Si la boucle se termine sans retourner \\( false \\), il est possible d'atteindre les hauteurs requises pour le MEX \\( m \\).

4. **Pourquoi Cela Fonctionne** :
   - La fonction de vérification ne simule pas l'ordre réel des opérations mais vérifie s'il existe un ordre qui satisfait les exigences de hauteur.
   - L'approche par tableau de différences garantit que le nombre de blocs ajoutés à chaque position est cohérent avec une séquence valide d'opérations.
   - La condition de non-décroissance est implicitement satisfaite car les hauteurs requises \\( \text{need}_i = \max(0, m - n + i) \\) sont non décroissantes (car \\( i \\) augmente, \\( m - n + i \\) augmente ou reste à 0).

#### Boucle Principale
- Lire le nombre de cas de test \\( t \\).
- Pour chaque cas de test :
  - Lire \\( n \\) et le tableau \\( a \\).
  - Effectuer une recherche binaire sur \\( m \\) de 0 à \\( n \\).
  - Utiliser la fonction de vérification pour déterminer si le MEX \\( m \\) est réalisable.
  - Mettre à jour \\( lo \\) (si réalisable) ou \\( hi \\) (si non).
- Afficher le \\( m \\) maximum (c'est-à-dire \\( lo \\)) pour chaque cas de test.

---

### Pourquoi le Code Résout le Problème

1. **Exactitude de la Recherche Binaire** :
   - La recherche binaire trouve le \\( m \\) maximum tel que la fonction de vérification retourne \\( true \\).
   - Puisque la faisabilité du MEX \\( m \\) implique la faisabilité pour toutes les valeurs de MEX plus petites (un \\( m \\) plus faible nécessite moins de positions avec des hauteurs plus basses), la recherche binaire identifie correctement le MEX maximum possible.

2. **Précision de la Fonction de Vérification** :
   - La fonction de vérification garantit que chaque position \\( i \\) peut avoir au moins \\( \max(0, m - n + i) \\) blocs après toutes les opérations.
   - Le tableau de différences simule l'effet cumulatif de l'abattage des tours, en tenant compte du fait que chaque tour contribue \\( a_i \\) blocs aux \\( a_i \\) positions suivantes.
   - En traitant les positions de gauche à droite et en ajustant le tableau de différences, il vérifie si les hauteurs initiales \\( a_i \\) peuvent être redistribuées pour satisfaire les hauteurs requises.

3. **Gestion de la Contrainte de Non-Décroissance** :
   - Les hauteurs requises \\( \max(0, m - n + i) \\) sont non décroissantes, ce qui correspond à l'exigence du problème d'avoir un tableau final non décroissant.
   - Si la fonction de vérification réussit, le tableau résultant peut être rendu non décroissant en garantissant que chaque position satisfait ou dépasse la hauteur requise.

4. **Efficacité** :
   - **Recherche Binaire** : \\( O(\log n) \\) itérations (car \\( m \leq n \\)).
   - **Fonction de Vérification** : \\( O(n) \\) par appel, car elle traite chaque position une fois et met à jour le tableau de différences en temps constant par position.
   - **Total par Cas de Test** : \\( O(n \log n) \\).
   - **Total pour Tous les Cas de Test** : Puisque \\( \sum n \leq 10^5 \\), la complexité globale est \\( O(t \cdot n \log n) \\), ce qui respecte la limite de temps de 3 secondes.

5. **Cas Limites** :
   - **\\( n = 1 \\)** : Si \\( a_1 = 0 \\), MEX = 1 (le tableau devient [0]). Si \\( a_1 > 0 \\), MEX = 0 (le tableau devient [0]). Le code gère cela correctement.
   - **Grands \\( a_i \\)** : Puisque \\( a_i \leq 10^9 \\), mais seules les \\( n-i \\) premières positions sont affectées, le code borne correctement l'effet en utilisant les limites du tableau.
   - **Tous les \\( a_i = 0 \\)** : Le tableau final est entièrement composé de zéros, MEX = 1. La fonction de vérification confirme cela.
   - **Valeurs Mixtes** : La recherche binaire et la fonction de vérification gèrent des \\( a_i \geq 0 \\) arbitraires.

---

### Spécificités du Code Java

Le code Java adapte la logique C++ en utilisant `BufferedReader` et `PrintWriter` pour des entrées/sorties efficaces, comme demandé. Aspects clés :

1. **Gestion des Entrées** :
   - Utilise `BufferedReader` pour lire les lignes et `StringTokenizer` pour analyser les entiers.
   - Lit \\( t \\), puis pour chaque cas de test, lit \\( n \\) et le tableau \\( a \\).

2. **Classe Checker** :
   - Encapsule la logique de vérification pour imiter la fonction lambda C++.
   - Utilise un tableau \\( d \\) pour simuler l'approche par tableau de différences.

3. **Sortie** :
   - Utilise `PrintWriter` pour afficher le résultat de chaque cas de test, avec `out.flush()` pour garantir que toute la sortie est écrite.

4. **Performance** :
   - Le code Java maintient la même complexité \\( O(n \log n) \\) par cas de test.
   - `BufferedReader` et `PrintWriter` garantissent que les entrées/sorties sont suffisamment rapides pour \\( \sum n \leq 10^5 \\).

---

### Conclusion

Le code résout le problème des "Fallen Towers" en :
- Utilisant une recherche binaire pour trouver le MEX maximum \\( m \\).
- Employant une fonction de vérification basée sur un tableau de différences pour vérifier si les hauteurs initiales des tours peuvent être redistribuées pour obtenir un tableau non décroissant avec les hauteurs requises.
- Garantissant l'exactitude grâce à la nature non décroissante des hauteurs requises et à la faisabilité des séquences d'opérations.
- Gérant tous les cas limites et respectant les contraintes de temps et de mémoire.

L'implémentation Java traduit fidèlement la logique C++, en utilisant des entrées/sorties efficaces pour répondre aux exigences du problème.