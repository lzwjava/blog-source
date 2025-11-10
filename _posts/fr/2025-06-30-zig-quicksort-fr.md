---
audio: false
generated: true
lang: fr
layout: post
title: Implémentation du tri rapide en Zig
translated: true
type: note
---

Voici l'implémentation équivalente du tri rapide en Zig.

```zig
const std = @import("std");

// Fonction de tri rapide
fn quickSort(arr: []i32) void {
    if (arr.len <= 1) {
        return;
    }

    const pivot_index = partition(arr);

    // Diviser le tableau en partitions gauche et droite
    // Remarque : la division des slices en Zig est légèrement différente de celle en Rust
    // Nous devons manipuler soigneusement l'élément pivot
    var left_slice = arr[0..pivot_index];
    var right_slice = arr[pivot_index + 1 .. arr.len]; // Exclure le pivot de la slice droite

    quickSort(left_slice);
    quickSort(right_slice);
}

// Fonction de partition
fn partition(arr: []i32) usize {
    const len = arr.len;
    // Pour simplifier, nous utilisons le dernier élément comme pivot, comme dans l'exemple Rust.
    // Dans un tri rapide de production, vous pourriez choisir un pivot aléatoire ou la médiane de trois pour de meilleures performances en moyenne.
    const pivot = arr[len - 1];
    var i: usize = 0; // Index du plus petit élément

    for (0..(len - 1)) |j| {
        if (arr[j] <= pivot) {
            std.mem.swap(i32, &arr[i], &arr[j]);
            i += 1;
        }
    }

    // Placer le pivot à sa position correcte
    std.mem.swap(i32, &arr[i], &arr[len - 1]);

    return i;
}

pub fn main() !void {
    var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };

    // Créer une slice mutable à partir du tableau pour la fonction quicksort
    var slice: []i32 = &arr;

    std.debug.print("Avant : {any}\n", .{slice});

    quickSort(slice);

    std.debug.print("Après : {any}\n", .{slice});
}

```

### Explication des changements et des concepts Zig :

1.  **`const std = @import("std");`** : Cette ligne importe la bibliothèque standard de Zig, qui fournit des utilitaires utiles comme `std.debug.print` pour l'affichage et `std.mem.swap` pour échanger des éléments.
2.  **`fn quickSort(arr: []i32) void`** :
      * `fn` déclare une fonction.
      * `arr: []i32` déclare `arr` comme une slice de `i32` (entiers 32 bits). En Zig, `[]T` désigne une slice mutable de type `T`. Il n'y a pas de `&mut` séparé comme en Rust ; la mutabilité est implicite selon que la variable contenant la slice est mutable ou non.
      * `void` indique que la fonction ne renvoie pas de valeur.
3.  **`if (arr.len <= 1)`** : Les instructions conditionnelles utilisent des parenthèses autour de la condition.
4.  **`const pivot_index = partition(arr);`** : `const` est utilisé pour les variables immuables.
5.  **Division des slices en Zig** :
      * `var left_slice = arr[0..pivot_index];`
      * `var right_slice = arr[pivot_index + 1 .. arr.len];`
      * Contrairement à `split_at_mut` de Rust qui crée deux slices mutables qui ne se chevauchent pas, le slicing de Zig `arr[start..end]` crée de nouvelles slices (vues) dans le tableau d'origine.
      * Il est crucial, dans les appels récursifs, d'exclure le pivot des sous-tableaux gauche et droit, car le pivot est déjà dans sa position triée finale après `partition`. Dans le code Rust, `right[1..]` réalise cela en sautant efficacement le premier élément de la slice `right`, qui est le pivot. Nous reproduisons cela en utilisant `pivot_index + 1` pour le début de la `right_slice`.
6.  **`std.mem.swap(i32, &arr[i], &arr[j]);`** :
      * `std.mem.swap` est utilisé pour échanger des éléments.
      * Le premier argument (`i32`) est le type des éléments à échanger.
      * Les arguments suivants sont des pointeurs vers les emplacements mémoire à échanger (`&arr[i]` et `&arr[j]`).
7.  **`for (0..(len - 1)) |j| { ... }`** : Il s'agit d'une boucle `for` qui itère de `0` jusqu'à (mais sans inclure) `len - 1`. La variable de boucle est capturée comme `j`.
8.  **`pub fn main() !void { ... }`** :
      * `pub` rend la fonction `main` publiquement accessible.
      * `!void` indique que la fonction peut renvoyer une erreur, mais dans ce cas, nous n'en gérons aucune explicitement. Pour les programmes simples, `void` convient, mais `!void` est souvent vu en Zig car il encourage une gestion robuste des erreurs.
9.  **`var arr = [_]i32{ 3, 6, 8, 10, 1, 2, 1 };`** :
      * `[_]i32` déclare un tableau de taille fixe de `i32`. Le `_` indique au compilateur d'inférer la taille à partir de la liste d'initialisation.
10. **`var slice: []i32 = &arr;`** : Nous créons une slice mutable (`[]i32`) à partir du tableau de taille fixe `arr` car `quickSort` attend une slice.
11. **`std.debug.print("Avant : {any}\n", .{slice});`** :
      * `std.debug.print` est l'équivalent en Zig de `println!` pour la sortie de débogage.
      * `{any}` est un spécificateur de format qui indique à Zig d'afficher la valeur dans un format lisible par l'homme, adapté au débogage.
      * `.{slice}` est un "littéral de structure" (structure anonyme) utilisé pour passer les arguments à la chaîne de format.

Pour compiler et exécuter ce code Zig :

1.  Enregistrez-le sous `quick_sort.zig`.
2.  Ouvrez votre terminal dans le même répertoire.
3.  Exécutez : `zig run quick_sort.zig`