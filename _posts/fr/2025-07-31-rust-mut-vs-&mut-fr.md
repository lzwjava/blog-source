---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'Rust : mut et &mut expliqués'
translated: true
type: note
---

En Rust, les mots-clés `mut` et `&mut` ont des objectifs liés mais distincts, et ils ne sont pas directement équivalents aux concepts de copie profonde/superficielle de Java ou aux pointeurs du C—bien que nous puissions établir certaines analogies pour plus de clarté. Je vais décomposer cela étape par étape, expliquer les différences et répondre à vos questions sur le passage par valeur vs le passage par référence, la mutabilité, et comment les modifications affectent les données originales. J'utiliserai des exemples basés sur votre code fourni pour illustrer.

### 1. **Comprendre `mut` dans les déclarations de variables**
   - Lorsque vous déclarez une variable avec `let mut`, vous rendez la *liaison* (le nom de la variable) mutable. Cela signifie que vous pouvez réassigner la variable ou modifier son contenu directement, mais uniquement dans la portée où elle est déclarée.
   - Exemple tiré de votre code :
     ```rust
     let mut arr = [3, 6, 8, 10, 1, 2, 1];
     ```
     Ici, `arr` est mutable, donc vous pourriez faire `arr[0] = 99;` ou même réassigner `arr = [1, 2, 3];` plus tard si vous le souhaitiez. Sans `mut`, Rust se plaindrait de toute tentative de modification d'une variable immuable (Rust privilégie l'immuabilité par défaut pour la sécurité).
   - Ce `mut` concerne la variable elle-même, pas la façon dont elle est passée aux fonctions. Cela n'implique pas de copie ou de référence—c'est simplement une autorisation de changer la variable sur place.

### 2. **Comprendre `&mut` dans les paramètres de fonction et les références**
   - `&mut` crée une *référence mutable* (également appelée emprunt mutable). C'est comme un pointeur en C qui permet la lecture *et* l'écriture des données pointées, mais avec le vérificateur d'emprunt strict de Rust garantissant la sécurité (pas de course aux données, pas de pointeurs pendants).
   - Dans votre code :
     ```rust
     fn quick_sort(arr: &mut [i32]) { ... }
     ```
     - Le paramètre `arr` est une référence mutable vers une tranche de `i32` (`&mut [i32]`). Les tranches en Rust sont des vues dans des tableaux ou des vecteurs (comme un pointeur + une longueur), et elles sont presque toujours passées comme références car les tranches sont des types "non dimensionnés" (leur taille n'est pas connue au moment de la compilation).
     - Lorsque vous appelez `quick_sort(&mut arr);`, vous passez une référence mutable vers le `arr` original. Cela permet à la fonction de modifier les éléments du tableau original via la référence (par exemple, via des échanges dans `partition`).
     - À l'intérieur de la fonction, des opérations comme `arr.swap(i, j);` affectent directement les données originales car `arr` est une référence pointant vers elles.
   - Sans le `&`, vous ne pourriez pas passer une tranche comme `[i32]` directement en paramètre de cette façon—Rust exige des références pour les types non dimensionnés. Mais plus généralement, `&mut` permet un passage par référence avec des droits de mutation.

### 3. **Passage par valeur vs passage par référence en Rust**
   - Rust utilise la *propriété* comme modèle central, ce qui est différent de Java (qui est principalement basé sur les références avec ramasse-miettes) ou du C (pointeurs manuels).
     - **Passage par valeur (transfert de propriété)** : Lorsque vous passez une valeur sans `&` (par exemple, `fn foo(x: i32)` ou `fn bar(mut v: Vec<i32>)`), la propriété des données est transférée à la fonction. La fonction peut la modifier localement, mais les changements n'affectent pas l'original de l'appelant (car l'appelant n'en est plus propriétaire). Si le type implémente `Copy` (comme les primitives telles que `i32`), il est automatiquement copié au lieu d'être déplacé—pas de copie profonde sauf si vous clonez explicitement.
       - Exemple :
         ```rust
         fn foo(mut x: i32) {
             x += 1;  // Modifie le x local, mais l'original de l'appelant reste inchangé (ou est déplacé/copié).
             println!("À l'intérieur : {}", x);
         }

         let y = 5;
         foo(y);  // Passe par valeur (copie, car i32 est Copy).
         println!("Après : {}", y);  // Toujours 5.
         ```
       - C'est comme le "passage par valeur" dans d'autres langages : les primitives sont copiées, les types plus volumineux (comme les tableaux/vecteurs) sont déplacés (efficace, pas de copie sauf clonage).
     - **Passage par référence (emprunt)** : Utiliser `&` (référence immuable) ou `&mut` (référence mutable) "emprunte" les données sans transférer la propriété. La fonction obtient une vue temporaire (comme un pointeur), et le propriétaire original garde le contrôle.
       - `&` : Emprunt en lecture seule. Impossible de modifier l'original.
       - `&mut` : Emprunt en lecture-écriture. *Peut* modifier l'original, comme le passage par référence en C++ ou un pointeur mutable en C.
       - Exemple :
         ```rust
         fn bar(x: &mut i32) {
             *x += 1;  // Déréférence et modifie l'original.
         }

         let mut y = 5;
         bar(&mut y);  // Passe une référence mutable.
         println!("Après : {}", y);  // Maintenant 6, l'original a changé.
         ```
       - Dans votre code de tri rapide, c'est un passage par référence avec `&mut`, donc les échanges modifient le tableau original. Si c'était juste `& [i32]`, vous ne pourriez pas le modifier (emprunt immuable).

   - Pour répondre à votre point : Oui, `&mut` permet de changer les valeurs originales (passage par référence avec mutation), tandis que passer sans `&` (passage par valeur) soit copie/déplace les données, donc les modifications sont locales et n'affectent pas l'original. Mais :
     - Tous les types ne sont pas copiés automatiquement—uniquement ceux qui implémentent `Copy` (par exemple, `i32`, pas les tableaux ou vecteurs). Pour les types non-`Copy` comme votre tableau, passer par valeur *déplacerait* la propriété, et vous devriez la retourner pour la "rendre" à l'appelant.
     - Rust évite les copies inutiles pour l'efficacité. Votre tableau n'est pas copié lorsqu'il est passé comme `&mut [i32]`—c'est juste une référence (superficielle, comme un pointeur).

### 4. **Comparaison avec Java et C**
   - **Java** : Tout ce qui n'est pas primitif est passé par référence (superficielle—les objets sont partagés, mais réassigner le paramètre n'affecte pas l'appelant). Les primitifs sont passés par valeur (copie). Aucun équivalent direct à `mut` ou `&mut` ; la mutabilité est contrôlée par la conception des classes (par exemple, les champs finaux). Java n'a pas le système de propriété de Rust, il est donc plus sujet aux problèmes d'état mutable partagé. Une copie profonde nécessite un clonage manuel.
   - **C** : `&mut` est comme passer un pointeur (`int*`) où vous pouvez déréférencer et modifier (`*ptr = 10;`). Un simple `mut` (dans les déclarations) est comme les variables non constantes. Mais le C n'a pas de vérificateur d'emprunt, donc vous gérez les durées de vie manuellement (source d'erreurs). Le passage par valeur en C copie les données (superficiel pour les structures sauf si vous effectuez une copie profonde).
   - Différence clé : Rust impose "une référence mutable à la fois" (ou plusieurs références immuables), empêchant les bogues. Pas de null, pas de pointeurs sauvages.

### 5. **Pourquoi `mut` parfois et `&mut` parfois dans votre code ?**
   - `mut` seul : Utilisé pour les variables locales qui doivent pouvoir être modifiées, comme `let mut arr` (pour pouvoir passer `&mut arr` plus tard ou la modifier directement).
   - `&mut` : Utilisé dans les paramètres lorsque la fonction a besoin d'emprunter et de modifier les données de l'appelant sans en prendre la propriété. Dans `quick_sort` et `partition`, `&mut [i32]` leur permet de trier le tableau sur place sans le déplacer/le copier.
   - Si vous essayiez `fn quick_sort(mut arr: [i32])`, cela ne compilerait pas—les tranches ne peuvent pas être passées par valeur de cette façon. Vous auriez besoin d'un tableau de taille fixe (par exemple, `[i32; 7]`) et cela transférerait la propriété.
   - Dans `partition`, la boucle utilise `mut i` en interne—c'est une variable mutable locale, sans rapport avec le passage.

### 6. **Est-ce que cela change les valeurs originales ?**
   - Oui pour `&mut` : Les changements se propagent à l'original (passage par référence).
   - Non pour le passage par valeur (sans `&`) : Les changements sont uniquement locaux (sauf si vous retournez la valeur modifiée).
   - Dans votre `quick_sort_interact()`, le `println!("After: {:?}", arr);` montrera le tableau trié car `&mut` a été utilisé.

Si vous exécutez votre code, il devrait afficher :
```
Before: [3, 6, 8, 10, 1, 2, 1]
After: [1, 1, 2, 3, 6, 8, 10]
```
(Le `mod simple;` et le `simple::run_simple();` semblent sans rapport—peut-être un espace réservé ? S'il y a une erreur là, c'est peut-être parce que `simple` n'est pas défini.)

Si cela ne clarifie pas ou si vous avez une partie spécifique du code à ajuster/tester, faites-le moi savoir !