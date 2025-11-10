---
audio: false
generated: true
lang: fr
layout: post
title: Options d'emplacement de sortie de Rust
translated: true
type: note
---

Vous posez une excellente question qui aborde la structure et la compilation typiques des projets Rust !

Lorsque vous utilisez `rustc` directement, vous avez deux options principales pour spécifier l'emplacement de sortie :

1.  **`-o <nom_fichier_sortie>`** : Cette option spécifie le *chemin et le nom de fichier exacts* pour l'exécutable ou la bibliothèque compilé(e).

    ```bash
    rustc scripts/rust/example.rs -o test/example
    ```

    Cela compilera `example.rs` et placera l'exécutable nommé `example` directement dans le répertoire `test/`. Si `test/` n'existe pas, `rustc` le créera.

2.  **`--out-dir <répertoire_sortie>`** : Cette option spécifie un *répertoire* où `rustc` doit placer tous les fichiers générés (l'exécutable/la bibliothèque, ainsi que tous les fichiers intermédiaires comme `.d`, `.rmeta`, etc.).

    ```bash
    rustc scripts/rust/example.rs --out-dir test/
    ```

    Dans ce cas, `rustc` compilera `example.rs` et placera l'exécutable (qui sera nommé `example` par défaut, d'après le nom du fichier source) à l'intérieur du répertoire `test/`.

**Recommandation : Utilisez Cargo pour les projets**

Bien que `rustc` directement vous donne un contrôle précis, pour la plupart des projets Rust, vous voudrez utiliser **Cargo**. Cargo est le système de build et le gestionnaire de paquets de Rust, et il simplifie la gestion des dépendances, la compilation, les tests et l'exécution de votre code.

Avec Cargo, les binaires de sortie sont généralement placés dans un répertoire `target` à la racine de votre projet. Par exemple, si vous avez un projet configuré avec Cargo :

```
mon_projet/
├── Cargo.toml
└── src/
    └── main.rs
```

Lorsque vous exécutez `cargo build` ou `cargo run`, l'exécutable compilé sera placé dans `mon_projet/target/debug/mon_projet` (pour les builds de débogage) ou `mon_projet/target/release/mon_projet` (pour les builds de release).

Si vous souhaitez contrôler le répertoire `target` pour Cargo, vous pouvez :

  * **Variable d'environnement `CARGO_TARGET_DIR`** :

    ```bash
    CARGO_TARGET_DIR=./test cargo build
    ```

    Cela placera l'intégralité du répertoire `target` (contenant `debug`, `release`, etc.) à l'intérieur de votre répertoire `test/`. L'exécutable se trouverait alors dans `test/debug/mon_projet`.

  * **Option en ligne de commande `--target-dir` pour Cargo** :

    ```bash
    cargo build --target-dir test/
    ```

    Cela fait la même chose que la variable d'environnement.

  * **`.cargo/config.toml`** : Vous pouvez définir un `target-dir` par défaut pour tous les projets Cargo sur votre machine ou pour un workspace spécifique en l'ajoutant dans un fichier `.cargo/config.toml`.

**Pourquoi utiliser Cargo ?**

  * **Structure de projet standardisée :** Cargo impose une structure de projet commune, facilitant la compréhension de votre code par les autres développeurs Rust.
  * **Gestion des dépendances :** Cargo gère le téléchargement et la compilation des dépendances de votre projet automatiquement.
  * **Tests et benchmarking :** Cargo possède des commandes intégrées pour exécuter les tests (`cargo test`) et les benchmarks (`cargo bench`).
  * **Gestion des releases :** Cargo aide à créer des builds de release (`cargo build --release`) et à publier des crates sur crates.io.

À moins d'avoir une raison très spécifique de ne pas le faire, il est fortement recommandé d'organiser votre code Rust dans un projet Cargo.

**Compte tenu de votre sortie `git status` :**

Votre `git status` montre `example` et `scripts/rust/` comme non suivis. Cela suggère que vous compilez peut-être `scripts/rust/example.rs` directement avec `rustc` en dehors d'un projet Cargo.

Si `example` est le binaire compilé, alors la commande précédente `rustc scripts/rust/example.rs` l'a placé dans le répertoire courant (`lzwjava.github.io`).

Pour atteindre votre objectif de le placer dans `test/example` (en supposant que `test` est un répertoire à la racine de `lzwjava.github.io`), vous utiliseriez :

```bash
rustc scripts/rust/example.rs -o test/example
```

C'est le moyen le plus direct d'obtenir le chemin de sortie spécifique que vous avez demandé en utilisant `rustc`.