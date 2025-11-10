---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Redondance d&#39;Exécution de Cargo
translated: true
type: note
---

Vous avez tout à fait raison ! Dans votre exemple de `Makefile` :

```makefile
run:
	cargo build
	cargo run
```

Inclure `cargo build` avant `cargo run` est redondant car `cargo run` inclut déjà l'étape de compilation. Lorsque vous exécutez `cargo run`, Cargo vérifie automatiquement si le projet doit être recompilé (par exemple, si les fichiers source ont changé) et, si nécessaire, compile le projet avant d'exécuter le binaire résultant. Cela rend l'étape explicite `cargo build` inutile dans ce contexte.

### Clarification
- **`cargo run`** :
  - Combine `cargo build` (compile le projet dans `target/debug/<nom_du_projet>`) puis exécute le binaire.
  - Ne recompile que s'il y a des changements dans le code source ou les dépendances.
- **`cargo build`** :
  - Compile uniquement le projet sans exécuter le binaire.
  - Utile si vous voulez vérifier la compilation sans exécuter le programme.

### Correction du `Makefile`
Pour rationaliser votre `Makefile`, vous pouvez supprimer le `cargo build` redondant :

```makefile
run:
	cargo run
```

Cela permet d'obtenir le même résultat : le projet est compilé (si nécessaire) puis exécuté.

### Quand utiliser `cargo build` séparément
Vous pourriez vouloir conserver `cargo build` comme une cible distincte dans le `Makefile` pour les cas où vous souhaitez uniquement compiler sans exécuter, par exemple :
- Vérifier les erreurs de compilation.
- Préparer les binaires pour le déploiement ou les tests sans exécution.

Par exemple :

```makefile
build:
	cargo build

run:
	cargo run

clean:
	cargo clean
```

- Exécutez `make build` pour compiler uniquement.
- Exécutez `make run` pour compiler (si nécessaire) et exécuter.
- Exécutez `make clean` pour effacer les artefacts de compilation.

### Contexte précédent
Comme vous travaillez sur un projet Rust où `main.rs` appelle `run_simple` depuis `simple.rs`, assurez-vous que l'erreur de visibilité (`E0603`) est résolue en rendant `run_simple` public dans `src/simple.rs` :

```rust
pub fn run_simple() {
    println!("Hello from run_simple!");
}
```

Et dans `src/main.rs` :

```rust
mod simple;

fn main() {
    simple::run_simple();
}
```

De plus, mettez à jour `Cargo.toml` pour supprimer l'avertissement `edition2024`, comme discuté précédemment :

```toml
[package]
name = "example"
version = "0.1.0"
edition = "2024"
```

### Test de la configuration
1. Mettez à jour le `Makefile` comme indiqué ci-dessus.
2. Exécutez :
   ```bash
   make run
   ```
   Cela exécutera `cargo run`, qui compilera (si nécessaire) et exécutera le programme, affichant `Hello from run_simple!` (ou toute autre sortie produite par `run_simple`).
3. Si vous voulez vérifier la compilation séparément :
   ```bash
   make build
   ```

### Notes supplémentaires
- Si vous utilisez `cargo run --bin simple` (pour un binaire séparé dans `simple.rs`), assurez-vous que `Cargo.toml` inclut :

  ```toml
  [[bin]]
  name = "simple"
  path = "src/simple.rs"
  ```

  Et que `simple.rs` a une fonction `main` :

  ```rust
  pub fn run_simple() {
      println!("Hello from run_simple!");
  }

  fn main() {
      run_simple();
  }
  ```

- Si vous rencontrez des problèmes, partagez la sortie de `make run` ou `cargo run` pour un débogage plus approfondi.

### Recommandation finale pour le `Makefile`

```makefile
build:
	cargo build

run:
	cargo run

clean:
	cargo clean
```

Cette configuration évite la redondance, prend en charge à la fois la compilation et l'exécution, et garde votre flux de travail propre. Faites-moi savoir si vous avez d'autres questions ou si vous avez besoin d'aide pour des erreurs spécifiques !