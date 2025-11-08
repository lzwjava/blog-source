---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction de l'Erreur de Compilation du Compilateur Protobuf
translated: true
type: note
---

### Comprendre l'erreur

Cette erreur de compilation se produit lors de la compilation des fichiers Protocol Buffers (`.proto`) dans la crate `greptime-proto`. Le script de build (utilisant `prost-build`) nécessite le binaire `protoc` pour générer le code Rust à partir de ces définitions proto, mais il ne parvient pas à le trouver sur votre système. Il s'agit d'un prérequis souvent négligé lors de la compilation de projets comme GreptimeDB qui reposent sur gRPC et protobuf pour la communication interne.

Les fichiers `.proto` listés (par exemple `database.proto`, `health.proto`) sont les définitions principales de GreptimeDB pour les métadonnées, les régions, le WAL, etc. Ignorer cette étape bloque donc l'intégralité de la compilation.

### Correction rapide

1. **Installez le compilateur Protobuf** (version ≥ 3.15 requise) :
   - Sur Debian/Ubuntu (ce qui correspond à l'indice de votre erreur) :
     ```
     sudo apt update
     sudo apt install protobuf-compiler
     ```
   - Sur Fedora/RHEL :
     ```
     sudo dnf install protobuf-compiler
     ```
   - Sur macOS (le cas échéant) :
     ```
     brew install protobuf
     ```
   - Téléchargement manuel (multi-plateforme) : Récupérez la dernière version sur [Protocol Buffers releases](https://github.com/protocolbuffers/protobuf/releases), extrayez-la et ajoutez `bin/protoc` à votre variable d'environnement PATH.

2. **Vérifiez l'installation** :
   ```
   protoc --version
   ```
   Cela devrait afficher quelque chose comme `libprotoc 3.21.12` (ou supérieur ; toute version ≥ 3.15 fonctionne).

3. **Relancez la compilation** :
   ```
   make clean  # Optionnel, pour effacer les artefacts partiels
   make
   ```
   Si `protoc` est installé mais toujours introuvable (problème de PATH par exemple), définissez la variable d'environnement :
   ```
   export PROTOC=/usr/bin/protoc  # Ajustez le chemin si nécessaire
   make
   ```

### Conseils supplémentaires

- Assurez-vous d'avoir les autres prérequis : Rust Nightly (que vous semblez avoir d'après l'erreur précédente), GCC/G++ (installez-les via `sudo apt install build-essential`) et les en-têtes de développement de glibc (`sudo apt install libc6-dev`).
- Si vous êtes dans un conteneur ou un environnement personnalisé, ajoutez l'étape d'installation à cet endroit.
- Pour tester après la compilation : `cargo run --bin greptime -- standalone start`.

Cela devrait vous permettre de passer l'étape de compilation des fichiers proto. Si l'erreur persiste sur autre chose (dépendances C++ par exemple), vérifiez la liste complète des prérequis.

### Références

- [GreptimeDB GitHub : Build from Source](https://github.com/GreptimeTeam/greptimedb#build-from-source)
- [Documentation prost-build : Sourcing Protoc](https://docs.rs/prost-build/#sourcing-protoc)