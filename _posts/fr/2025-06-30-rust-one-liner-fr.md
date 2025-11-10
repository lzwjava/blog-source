---
audio: false
generated: true
lang: fr
layout: post
title: Rust en une ligne avec enchaînement de shell
translated: true
type: note
---

Vous mettez le doigt sur une attente courante chez les développeurs expérimentés venant de langages comme Python, Ruby ou JavaScript, où une simple commande suffit souvent pour exécuter un script directement. Rust, étant un langage compilé, a un flux de travail légèrement différent par défaut.

Cependant, vous pouvez tout à fait obtenir une sensation de "one-liner", surtout pour des scripts simples ou des exercices, en enchaînant les commandes dans votre shell.

### Le "One-Liner" Direct (Enchaînement de Commandes Shell)

Vous avez déjà les composants : `rustc` pour la compilation et `./` pour l'exécution. Vous pouvez les combiner en utilisant les opérateurs du shell :

```bash
rustc scripts/rust/example.rs -o test/example && ./test/example
```

**Explication :**

* `rustc scripts/rust/example.rs -o test/example` : Cette commande compile votre fichier Rust et place l'exécutable à l'emplacement `test/example`.
* `&&` : Il s'agit d'un **séparateur conditionnel de commandes** dans bash (et la plupart des shells de type Unix). La commande *après* `&&` ne s'exécutera que si la commande *avant* `&&` se termine avec succès (c'est-à-dire renvoie un code de sortie 0).
    * Si `rustc` compile sans erreur, il renverra 0, et ensuite `./test/example` s'exécutera.
    * Si `rustc` rencontre une erreur de compilation, il renverra un code de sortie non nul, et `./test/example` ne sera *pas* exécuté. C'est un comportement souhaitable \!

### Pour une Expérience Plus "Script-like" (Cargo)

Bien que l'approche avec `&&` ci-dessus fonctionne bien pour des tests rapides, pour tout ce qui dépasse des scripts triviaux à un seul fichier, l'outil `cargo` de Rust est la méthode recommandée, et il *offre* bien un one-liner similaire à Python pour exécuter du code dans un projet :

1.  **Initialiser un Projet Cargo (si ce n'est pas déjà fait) :**
    Si votre `scripts/rust/example.rs` est juste un fichier autonome, vous devriez généralement commencer par créer un projet Cargo dans son répertoire parent (ou dans un nouveau répertoire dédié).

    ```bash
    # Allez dans le répertoire où vous voulez votre projet (par exemple, scripts/rust)
    cd scripts/rust

    # Initialisez un nouveau projet binaire Cargo
    cargo init --bin .
    ```

    Cela créera un `Cargo.toml` et déplacera votre `example.rs` (s'il s'agissait de `main.rs`) ou ajustera le `Cargo.toml` pour pointer vers lui (si vous renommez `example.rs` en `main.rs` dans `src/`).

2.  **Exécuter avec Cargo :**
    Une fois que vous avez un projet Cargo configuré, vous pouvez compiler et exécuter avec une seule commande :

    ```bash
    # Depuis la racine de votre projet (par exemple, scripts/rust si vous y avez exécuté cargo init)
    cargo run
    ```

    `cargo run` va :

    * Compiler votre code (s'il n'a pas été compilé ou si des modifications ont été apportées).
    * Ensuite, exécuter le binaire résultant.
    * Par défaut, le binaire est placé dans `target/debug/` au sein de votre projet, mais vous n'avez pas à vous soucier de son chemin spécifique.

**Pourquoi Cargo est préféré :**

* **Gestion des Dépendances :** Si votre code a besoin de bibliothèques externes (crates), Cargo s'occupe de les récupérer, de les compiler et de les lier automatiquement. Vous les spécifiez dans `Cargo.toml`.
* **Structure de Projet Standard :** Il encourage une organisation cohérente (`src/main.rs`, `Cargo.toml`), ce qui rend votre code plus facile à comprendre pour les autres (et pour votre vous du futur).
* **Tests :** `cargo test` exécute vos tests unitaires et d'intégration.
* **Builds de Release :** `cargo run --release` (ou `cargo build --release`) compile avec des optimisations pour la production.
* **Pas de Nettoyage Manuel :** Vous n'avez pas à supprimer manuellement les binaires compilés. `cargo clean` s'en charge.

### Qu'en est-il d'une approche de "Scripting" pure comme `python script.py` avec Python ?

Rust n'est pas conçu comme un langage de script interprété. C'est un langage système compilé. Ainsi, vous n'obtiendrez pas de commande directe `rust script.rs` qui compile et exécute sans une étape de compilation explicite.

Cependant, il existe des outils communautaires qui tentent de combler cet écart pour des "scripts" Rust rapides à un seul fichier (bien qu'ils compilent toujours en arrière-plan) :

* **`cargo-script`** : Une sous-commande Cargo qui vous permet d'exécuter des fichiers `.rs` uniques, en gérant les dépendances si elles sont spécifiées via des commentaires. Vous l'installeriez typiquement avec `cargo install cargo-script`. Ensuite, vous pourriez potentiellement exécuter `cargo script scripts/rust/example.rs`.
* **`rust-script`** : Un autre outil populaire pour exécuter des fichiers Rust directement comme des scripts. Installez-le via `cargo install rust-script`. Ensuite, vous pouvez souvent simplement rendre votre fichier `.rs` exécutable (`chmod +x example.rs`) et l'exécuter : `./example.rs`. Il gère la compilation et l'exécution en arrière-plan.

Pour votre cas d'usage qui est de tester rapidement `example.rs`, le one-liner `rustc ... && ./...` est parfaitement adapté et répond directement à votre question sur l'enchaînement des deux commandes. Pour tout développement non trivial, adopter Cargo sera une expérience Rust plus productive et plus idiomatique.