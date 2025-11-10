---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Exécution d'un programme Rust depuis un répertoire
translated: true
type: note
---

Pour exécuter un programme Rust simple à partir de la structure de répertoire que vous avez fournie, il semble que vous travailliez sur un projet Rust (`lzwjava.github.io/rust`) avec un dossier `src` contenant `main.rs` et `simple.rs`. Voici comment vous pouvez exécuter un programme Rust simple, en supposant que vous souhaitiez exécuter le code dans `main.rs` ou `simple.rs`.

### Étapes pour exécuter un programme Rust

1.  **Vérifier la structure du projet** :
    - Votre projet a un fichier `Cargo.toml`, indiquant qu'il s'agit d'un projet Rust géré par Cargo, l'outil de build de Rust.
    - Le fichier `src/main.rs` est le point d'entrée par défaut pour une application binaire Rust.
    - Le fichier `simple.rs` est probablement un module ou un autre fichier source, mais il ne s'exécutera pas directement à moins d'être référencé dans `main.rs` ou configuré comme un binaire dans `Cargo.toml`.

2.  **Exécuter le programme avec Cargo** :
    - Si vous voulez exécuter le code dans `src/main.rs`, utilisez la commande suivante depuis la racine du projet (`~/projects/lzwjava.github.io/rust`) :
      ```bash
      cargo run
      ```
      Cette commande :
      - Compile le projet (résout les dépendances et construit le code).
      - Exécute le binaire généré à partir de `src/main.rs`.
      - Le résultat apparaîtra dans le terminal.

3.  **Si vous voulez exécuter `simple.rs`** :
    - Par défaut, Cargo s'attend à ce que le point d'entrée principal soit `src/main.rs`. Si `simple.rs` est un module, vous devez le référencer dans `main.rs`. Par exemple, dans `src/main.rs` :
      ```rust
      mod simple; // Déclare le module simple

      fn main() {
          simple::some_function(); // Appelle une fonction de simple.rs
      }
      ```
      Ensuite, exécutez `cargo run` comme ci-dessus.
    - Si `simple.rs` est destiné à être un binaire autonome, vous devez le configurer dans `Cargo.toml`. Ajoutez ce qui suit à `Cargo.toml` :
      ```toml
      [[bin]]
      name = "simple"
      path = "src/simple.rs"
      ```
      Ensuite, exécutez :
      ```bash
      cargo run --bin simple
      ```

4.  **Alternative : Exécuter sans Cargo** :
    - Si vous voulez compiler et exécuter un seul fichier (par exemple, `simple.rs`) sans Cargo, assurez-vous qu'il a une fonction `main` et utilisez le compilateur `rustc` :
      ```bash
      rustc src/simple.rs
      ./simple
      ```
      Cela génère un exécutable nommé `simple` dans le répertoire courant et l'exécute. Remarque : Cette approche ne gère pas les dépendances, elle n'est donc adaptée qu'aux programmes simples et autonomes.

5.  **Vérifier les erreurs** :
    - Si vous rencontrez des erreurs, assurez-vous que :
      - Rust et Cargo sont installés (vérifiez avec `rustc --version` et `cargo --version`).
      - `Cargo.toml` est correctement configuré avec les dépendances nécessaires.
      - Le code dans `main.rs` ou `simple.rs` a une fonction `fn main()` valide.
    - Exécutez `cargo check` pour vérifier le code sans construire le binaire :
      ```bash
      cargo check
      ```

6.  **Exemple `simple.rs`** :
    Si `simple.rs` contient quelque chose comme :
    ```rust
    fn main() {
        println!("Hello from simple!");
    }
    ```
    Et que vous l'avez ajouté comme un binaire dans `Cargo.toml`, l'exécution de `cargo run --bin simple` affichera `Hello from simple!`.

### Notes
- Le répertoire `target/debug` contient les artefacts compilés. Vous pouvez exécuter le binaire directement avec `./target/debug/<nom_du_projet>` (remplacez `<nom_du_projet>` par le nom dans `Cargo.toml`), mais `cargo run` est préférable car il gère la compilation et l'exécution.
- Si `simple.rs` est un module, assurez-vous qu'il est correctement intégré dans `main.rs` avec `mod simple;`.
- Pour des configurations plus complexes ou un code spécifique dans `simple.rs`, partagez le contenu de `simple.rs` ou de `Cargo.toml` pour obtenir des conseils adaptés.

Si vous aviez quelque chose de spécifique en disant "run simple here" (par exemple, une fonction ou une configuration spécifique), veuillez fournir plus de détails et j'affinerai la réponse !