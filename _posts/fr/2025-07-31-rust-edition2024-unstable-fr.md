---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Édition 2024 activée en Rust
translated: true
type: note
---

L'erreur se produit parce que votre projet Rust tente d'utiliser la fonctionnalité `edition2024`, qui n'est pas stabilisée dans votre version actuelle de Cargo (1.75.0). Pour résoudre ce problème, vous devez activer explicitement la fonctionnalité instable `edition2024`.

### Étapes pour corriger :

1. **Activer la fonctionnalité `edition2024`** :
   Ouvrez votre fichier `Cargo.toml` et ajoutez la ligne suivante tout en haut, avant la section `[package]` :

   ```toml
   cargo-features = ["edition2024"]
   ```

   Par exemple, votre `Cargo.toml` pourrait ressembler à ceci :

   ```toml
   cargo-features = ["edition2024"]

   [package]
   name = "your_project_name"
   version = "0.1.0"
   edition = "2024"
   ```

2. **Utiliser une toolchain Rust Nightly** :
   Étant donné que `edition2024` est une fonctionnalité instable, vous devez utiliser la toolchain Rust nightly, car les versions stables (comme la 1.75.0) ne la prennent pas en charge. Exécutez les commandes suivantes :

   ```bash
   rustup update nightly
   rustup override set nightly
   ```

   La première commande met à jour la toolchain nightly, et la seconde configure votre répertoire de projet pour utiliser la toolchain nightly.

3. **Relancer la compilation** :
   Après avoir effectué ces modifications, essayez de recompiler votre projet :

   ```bash
   cargo build
   ```

### Notes supplémentaires :
- La fonctionnalité `edition2024` est expérimentale et peut changer. Consultez la documentation Rust pour des mises à jour sur son statut : [Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024).
- Si vous n'avez pas besoin de `edition2024`, vous pouvez revenir à une édition stable (par exemple, `edition = "2021"`) dans `Cargo.toml` pour éviter d'utiliser la toolchain nightly.
- Assurez-vous que votre `rustup` est à jour en exécutant `rustup update`.

Si vous rencontrez d'autres problèmes, partagez le contenu de votre `Cargo.toml` ou tout nouveau message d'erreur pour obtenir des conseils plus spécifiques.

[Rust Edition 2024](https://doc.rust-lang.org/nightly/cargo/reference/unstable.html#edition-2024)