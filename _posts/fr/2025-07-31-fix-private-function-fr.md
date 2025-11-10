---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Correction d'Erreur de Fonction Privée
translated: true
type: note
---

L'erreur `E0603: function run_simple is private` indique que la fonction `run_simple` dans `simple.rs` est privée (elle manque le mot-clé `pub`), donc elle ne peut pas être accessible depuis `main.rs`. Dans Rust, les fonctions sont privées par défaut et doivent être explicitement rendues publiques avec `pub` pour être accessibles en dehors de leur module.

### Étapes pour Corriger l'Erreur

1. **Rendre `run_simple` Publique** :
   - Ouvrez `src/simple.rs`.
   - Ajoutez le mot-clé `pub` à la fonction `run_simple` pour la rendre accessible publiquement.
   - Exemple :
     ```rust
     pub fn run_simple() {
         // Corps existant de la fonction
         println!("Hello from run_simple!");
     }
     ```

2. **S'assurer d'une Déclaration de Module Correcte** :
   - Dans `src/main.rs`, assurez-vous d'avoir déclaré le module `simple` correctement :
     ```rust
     mod simple; // Déclare le module simple

     fn main() {
         simple::run_simple(); // Appelle la fonction publique
     }
     ```

3. **Reconstruire et Exécuter** :
   - Après avoir rendu la fonction publique, reconstruisez le projet :
     ```bash
     cargo build
     ```
   - Si la construction réussit, exécutez le programme :
     ```bash
     cargo run
     ```

4. **Vérifier la Présence d'Autres Problèmes** :
   - L'erreur mentionne `src/simple.rs:47:1`, alors vérifiez que la fonction `run_simple` à cette ligne est correctement définie et n'a pas d'autres problèmes (par exemple, des erreurs de syntaxe ou des dépendances manquantes).
   - Si `simple.rs` utilise des crates externes, assurez-vous qu'elles sont listées dans `Cargo.toml` sous `[dependencies]`.

5. **Avertissement de Cargo** :
   - L'avertissement concernant `edition2024` suggère que vous utilisez un flag de fonctionnalité dans `Cargo.toml` qui n'est plus nécessaire depuis que Rust 1.85 a stabilisé l'édition 2024. Pour nettoyer cela, ouvrez `Cargo.toml` et supprimez la fonctionnalité `edition2024` si elle est présente (par exemple, sous `[features]` ou `cargo-features`). À la place, définissez l'édition directement :
     ```toml
     [package]
     name = "example"
     version = "0.1.0"
     edition = "2024"
     ```
   - Cela garantit que votre projet utilise l'édition 2024 sans le flag de fonctionnalité déprécié.

### Exemples de Fichiers

Pour clarifier, voici comment vos fichiers devraient ressembler :

**`src/simple.rs`** :
```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

**`src/main.rs`** :
```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

**`Cargo.toml`** (exemple minimal) :
```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### Notes Supplémentaires
- Si `run_simple` dépend d'autre code ou d'autres modules, assurez-vous qu'ils sont également publics s'ils sont accédés depuis `main.rs`.
- Si l'erreur persiste, partagez le contenu de `src/simple.rs` (surtout autour de la ligne 47) et de `src/main.rs` pour obtenir des conseils plus spécifiques.
- La commande `rustc --explain E0603` fournit une documentation détaillée sur cette erreur, que vous pouvez exécuter pour plus d'informations.
- Le répertoire `target/debug` contiendra le binaire compilé (`example`) après une construction réussie.

Essayez ces étapes et faites-moi savoir si vous rencontrez d'autres problèmes !