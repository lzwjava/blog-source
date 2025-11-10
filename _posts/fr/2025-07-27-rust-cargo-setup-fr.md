---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction de la configuration d'un projet Rust
translated: true
type: note
---

Il semble que vous essayiez de configurer et d'exécuter un projet Rust simple basé sur l'extrait `Cargo.toml` fourni et la structure de fichiers (un sous-répertoire `rust` contenant `example.rs`). Cependant, quelques problèmes empêchent que cela fonctionne immédiatement :

- Le répertoire `/Users/lzwjava/projects/lzwjava.github.io` (la racine de votre GitHub Pages) ne semble pas encore être configuré comme un espace de travail Rust valide, ce qui explique l'échec antérieur de rust-analyzer.
- Le `edition = "2025"` dans `Cargo.toml` est invalide — les éditions actuelles de Rust sont 2015, 2018, 2021 et 2024 (publiée début 2025). Il n'existe pas d'édition 2025 disponible.
- Les projets Rust gérés par Cargo s'attendent à une structure standard : `Cargo.toml` à la racine, avec les fichiers source dans un sous-répertoire `src/` (par exemple, `src/main.rs` pour un exécutable binaire). Votre `example.rs` se trouve dans un sous-répertoire `rust/`, qui n'est pas reconnu par défaut.
- En supposant que `example.rs` contienne un programme exécutable simple (par exemple, un "Hello, World!" avec `fn main()`), vous avez deux options principales : l'exécuter comme un script à fichier unique (sans Cargo) ou le configurer comme un projet Cargo approprié.

Je vais vous guider à travers les deux approches étape par étape. Utilisez un terminal dans le répertoire racine de votre projet (`lzwjava.github.io`).

### Option 1 : Exécuter comme un Script à Fichier Unique (Le Plus Rapide, Sans Cargo)
Cette méthode compile et exécute `example.rs` directement en utilisant le compilateur Rust (`rustc`). C'est idéal si vous n'avez pas besoin de dépendances ou d'une configuration de projet complète.

1. Naviguez vers le répertoire contenant le fichier :
   ```
   cd rust
   ```

2. Compilez le fichier :
   ```
   rustc example.rs
   ```
   - Cela génère un exécutable nommé `example` (sur macOS/Linux) ou `example.exe` (sur Windows).
   - Si la compilation échoue (par exemple, à cause d'erreurs de syntaxe dans `example.rs`), corrigez le code et réessayez.

3. Exécutez l'exécutable :
   ```
   ./example
   ```
   - La sortie dépendra du contenu de `example.rs` (par exemple, "Hello, World!").

Si `example.rs` est une bibliothèque (sans `fn main()`), cela ne fonctionnera pas — utilisez plutôt `cargo test` dans une configuration de projet.

### Option 2 : Configurer et Exécuter comme un Projet Cargo (Recommandé pour rust-analyzer et l'Évolutivité)
Cette méthode corrige l'erreur rust-analyzer en créant un espace de travail valide. Elle permet également d'utiliser `cargo run` pour une construction/exécution plus facile.

1. Créez ou déplacez-vous vers un répertoire de projet dédié (pour éviter d'encombrer la racine de votre GitHub Pages) :
   ```
   mkdir rust_project
   cd rust_project
   ```
   - Si vous tenez à utiliser le répertoire `rust` existant, faites `cd rust` à la place et poursuivez.

2. Créez `Cargo.toml` avec le contenu que vous avez fourni, mais corrigez l'édition :
   ```
   [package]
   name = "example"
   version = "0.1.0"
   edition = "2024"  # Changé de "2025" invalide
   authors = ["lzwjava@gmail.com"]
   description = "A simple Rust example project"

   [dependencies]
   ```
   - Enregistrez ceci sous le nom `Cargo.toml` dans le répertoire courant.

3. Configurez le répertoire source et déplacez votre fichier :
   ```
   mkdir src
   mv ../rust/example.rs src/main.rs  # Ajustez le chemin si nécessaire ; le renomme en main.rs pour l'exécution binaire
   ```
   - Si `example.rs` n'est pas destiné à être le point d'entrée principal, renommez-le plutôt en `lib.rs` et ajoutez `[lib]` à `Cargo.toml` pour une crate bibliothèque.

4. Construisez le projet :
   ```
   cargo build
   ```
   - Cela télécharge les crates nécessaires (aucune ici) et compile. Si cela échoue, vérifiez les erreurs dans `src/main.rs`.

5. Exécutez le projet :
   ```
   cargo run
   ```
   - Cela construit si nécessaire et exécute `src/main.rs`.

6. Pour résoudre l'erreur rust-analyzer dans VS Code (ou un éditeur similaire) :
   - Ouvrez le dossier `rust_project` comme racine de votre espace de travail (**Fichier > Ouvrir un dossier**).
   - Rechargez la fenêtre (**Cmd+Shift+P** > **Developer: Reload Window**).
   - rust-analyzer devrait maintenant détecter le projet via `Cargo.toml`.

### Conseils de Dépannage
- **Si `cargo` n'est pas installé** : Exécutez `rustup update` (en supposant que vous avez Rust installé via rustup). Sinon, installez Rust depuis https://rustup.rs/.
- **Erreur d'édition** : Si vous gardez "2025", Cargo se plaindra : "error: invalid edition: '2025'". Restez sur "2024".
- **Pas de `fn main()` dans `example.rs`** : Ajoutez-en une, par exemple :
  ```
  fn main() {
      println!("Hello, World!");
  }
  ```
- **Des dépendances sont nécessaires ?** : Ajoutez-les sous `[dependencies]` dans `Cargo.toml`, par exemple `rand = "0.8"`, puis `cargo build`.
- **rust-analyzer échoue toujours ?** : Assurez-vous que l'extension Rust de votre éditeur est à jour, et ajoutez `"rust-analyzer.linkedProjects": ["./Cargo.toml"]` à votre `settings.json` d'espace de travail si le projet est dans un sous-répertoire.
- Pour des configurations plus complexes (par exemple, plusieurs crates), utilisez `cargo new --bin example` pour générer un modèle.

Si cela ne correspond pas à votre configuration (par exemple, fournissez le contenu de `example.rs` ou plus de détails), faites-le moi savoir pour des étapes affinées.

[Annonce de Rust 1.88.0](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)  
[Rust | endoflife.date](https://endoflife.date/rust)