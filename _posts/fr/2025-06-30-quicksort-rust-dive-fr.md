---
audio: false
generated: true
lang: fr
layout: post
title: Tri Rapide en Rust pour Développeurs Expérimentés
translated: true
type: note
---

Parfait, étant donné votre solide expérience en algorithmes, en développement full-stack et même en ingénierie mobile, l'approche de Rust en matière de sécurité mémoire et de contrôle explicite vous semblera conceptuellement assez familière, même si la syntaxe et la rigueur sont nouvelles. Décomposons cette implémentation du Quicksort en Rust.

-----

### Quicksort en Rust : Une Plongée pour les Développeurs Expérimentés

Ce code Rust implémente le classique **algorithme Quicksort**. L'idée centrale du Quicksort est de choisir un élément comme pivot et de partitionner le tableau autour de celui-ci, de sorte que les éléments plus petits que le pivot se trouvent d'un côté et les éléments plus grands de l'autre. Ce processus est ensuite appliqué récursivement aux sous-tableaux.

Passons en revue les fonctions :

-----

### `fn quick_sort(arr: &mut [i32])`

```rust
fn quick_sort(arr: &mut [i32]) {
    if arr.len() <= 1 {
        return;
    }
    let pivot_index = partition(arr);
    let (left, right) = arr.split_at_mut(pivot_index);
    quick_sort(left);
    quick_sort(&mut right[1..]);
}
```

  * **`arr: &mut [i32]`** : C'est ici que le système de types de Rust montre immédiatement ses couleurs.
      * `&mut` signifie une **référence mutable**. Cela signifie que la fonction `quick_sort` obtient une référence empruntée au tableau `arr`, et qu'elle est autorisée à modifier le contenu de ce tableau *sur place*.
      * `[i32]` est une **tranche (slice)** d'entiers `i32`. En Rust, `[T]` est le type d'une tranche, qui est une vue sur une séquence contiguë d'éléments. Elle ne possède pas les données ; elle pointe simplement vers une partie d'un tableau ou d'un `Vec`. Ceci est crucial pour l'efficacité, car cela évite de copier les données. Vous connaissez les pointeurs et les sections de tableaux grâce à votre expérience en C/C++/Java ; considérez cela comme la manière sûre et explicite de Rust de gérer cela.
  * **Cas de base `if arr.len() <= 1`** : Cas de base récursif standard pour Quicksort. Si la tranche a 0 ou 1 élément, elle est déjà triée, donc on retourne simplement.
  * **`let pivot_index = partition(arr);`** : Appelle la fonction `partition` (que nous examinerons ensuite) pour réarranger la tranche. Elle retourne la position finale de l'élément pivot.
  * **`let (left, right) = arr.split_at_mut(pivot_index);`** : C'est une fonctionnalité clé de Rust pour l'aliasing mutable sûr.
      * `split_at_mut` est une méthode sur les tranches mutables. Elle prend un index et divise la tranche mutable en deux tranches mutables *disjointes*.
      * `left` sera `arr[0..pivot_index]` et `right` sera `arr[pivot_index..len]`.
      * Ceci est fondamental pour le **vérificateur d'emprunt (borrow checker)** de Rust. Vous ne pouvez pas avoir deux références mutables vers les *mêmes données* en même temps. `split_at_mut` garantit que `left` et `right` font référence à des parties complètement séparées du tableau d'origine, satisfaisant le vérificateur d'emprunt et empêchant les courses aux données dans un contexte multi-thread (même si celui-ci est mono-thread, le principe s'applique).
  * **`quick_sort(left);`** : Trie récursivement la sous-tranche `left`.
  * **`quick_sort(&mut right[1..]);`** : Trie récursivement la sous-tranche `right`.
      * `right[1..]` est important : La tranche `right` commence à `pivot_index`. Puisque `arr[pivot_index]` est maintenant l'élément pivot correctement positionné, nous l'excluons de l'appel récursif sur le côté droit.
      * `&mut` ré-emprunte explicitement une tranche mutable à partir de `right`.

-----

### `fn partition(arr: &mut [i32]) -> usize`

```rust
fn partition(arr: &mut [i32]) -> usize {
    let len = arr.len();
    let pivot = arr[len - 1];
    let mut i = 0;
    for j in 0..len - 1 {
        if arr[j] <= pivot {
            arr.swap(i, j);
            i += 1;
        }
    }
    arr.swap(i, len - 1);
    i
}
```

Cette fonction implémente le schéma de partition de Lomuto, une manière courante de partitionner un tableau pour le Quicksort.

  * **`let len = arr.len();`** : Obtient la longueur de la tranche courante.
  * **`let pivot = arr[len - 1];`** : Le **dernier élément** de la tranche est choisi comme pivot.
  * **`let mut i = 0;`** : `i` agit comme un pointeur vers la "frontière" entre les éléments plus petits ou égaux au pivot et les éléments plus grands que le pivot. Les éléments à gauche de `i` seront inférieurs ou égaux au pivot.
  * **`for j in 0..len - 1`** : Cette boucle itère à travers tous les éléments *sauf* le pivot (qui est à `len - 1`).
  * **`if arr[j] <= pivot { ... }`** : Si l'élément courant `arr[j]` est inférieur ou égal au pivot :
      * **`arr.swap(i, j);`** : Échange `arr[j]` avec `arr[i]`. Cela déplace le plus petit élément dans la section "inférieur ou égal".
      * **`i += 1;`** : Incrémente `i` pour étendre la section "inférieur ou égal".
  * **`arr.swap(i, len - 1);`** : Après la boucle, `i` est la position correcte pour le pivot. Nous échangeons le pivot (qui est toujours à `len - 1`) avec sa position triée finale. Maintenant, tous les éléments à gauche de `i` sont inférieurs ou égaux à `arr[i]` (le pivot), et tous les éléments à droite sont plus grands.
  * **`i`** : La fonction retourne `i`, qui est l'index final de l'élément pivot.

-----

### `fn main()`

```rust
fn main() {
    let mut arr = [3, 6, 8, 10, 1, 2, 1];
    println!("Before: {:?}", arr);
    quick_sort(&mut arr);
    println!("After: {:?}", arr);
}
```

  * **`let mut arr = [3, 6, 8, 10, 1, 2, 1];`** :
      * `let mut` déclare une **variable mutable**. Cela vous permet de réassigner la variable ou de modifier son contenu (si c'est un type mutable).
      * `[3, ...]` crée un **tableau de taille fixe** sur la pile. Sa taille est connue à la compilation.
  * **`println!("Before: {:?}", arr);`** : Utilise la macro `println!` pour la sortie.
      * `{:?}` est le spécificateur de format **d'impression de débogage (debug print)**. Il utilise le trait `Debug` pour imprimer une représentation lisible par un humain du tableau.
  * **`quick_sort(&mut arr);`** : Appelle la fonction `quick_sort`, en passant une référence mutable au tableau `arr`.
  * **`println!("After: {:?}", arr);`** : Imprime à nouveau le tableau après le tri.

-----

### Points Clés Spécifiques à Rust pour Vous

  * **Propriété (Ownership) et Emprunt (Borrowing)** : Ce code est un exemple parfait des concepts fondamentaux de Rust. Vous passez des **références (`&` et `&mut`)** plutôt que de copier les données. Les références `&mut` sont critiques pour modifier le tableau sur place, et le **vérificateur d'emprunt** (par exemple, appliqué par `split_at_mut`) garantit que vous n'avez jamais plusieurs références mutables vers les mêmes données, éliminant toute une classe de bogues de concurrence au moment de la compilation. C'est probablement le plus grand changement de paradigme par rapport à des langages comme Java ou Python, mais il offre une sécurité mémoire sans garbage collector.
  * **Tranches (Slices) `[T]`** : Elles sont incroyablement puissantes pour travailler avec des données contiguës. Elles fournissent une vue sûre et efficace sur des parties de tableaux ou de vecteurs sans allouer de nouvelle mémoire.
  * **Macros (`println!`)** : Vous verrez `!` après de nombreuses fonctions de la bibliothèque standard (comme `println!`, `vec!`, `format!`). Cela indique que ce sont des **macros**, et non des fonctions régulières. Les macros développent le code au moment de la compilation, offrant plus de flexibilité et de puissance (comme des arguments variadiques ou la génération de code à la compilation) par rapport aux fonctions régulières.

Compte tenu de votre expérience, vous apprécierez probablement les caractéristiques de performance et les garanties de sécurité que Rust offre, même si la "danse du vérificateur d'emprunt" demande un peu de temps pour s'y habituer. C'est une manière différente de penser la gestion de la mémoire, mais qui conduit à un code hautement robuste et efficace.