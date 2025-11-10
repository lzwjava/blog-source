---
audio: false
generated: true
lang: fr
layout: post
title: Corriger l'Erreur de l'Édition Rust 2024
translated: true
type: note
---

Le message d'erreur `feature edition2024 is required` indique que votre projet est configuré pour utiliser l'édition `edition2024` de Rust, mais votre version actuelle de Cargo (1.84.1) ne la prend pas encore en charge dans une version stable. L'édition 2024 est toujours considérée comme une fonctionnalité instable/nightly.

Voici comment résoudre le problème et des informations sur la dernière version de Cargo :

### Comment corriger

Vous avez deux options principales :

**1. Utiliser une toolchain Rust Nightly (Recommandé pour `edition2024`)**

Étant donné que `edition2024` est une fonctionnalité instable, vous devez utiliser une version nightly de Rust et Cargo pour compiler votre projet.

  * **Installer la toolchain Nightly :** Si vous ne l'avez pas déjà, utilisez `rustup` pour installer la toolchain nightly :
    ```bash
    rustup toolchain install nightly
    ```
  * **Utiliser la toolchain Nightly pour votre build :** Vous pouvez demander à Cargo d'utiliser spécifiquement la toolchain nightly pour cette commande :
    ```bash
    OPENSSL_STATIC=yes cargo +nightly build --release
    ```
  * **(Optionnel) Définir Nightly par défaut pour le projet :** Si vous voulez que ce projet utilise toujours nightly, vous pouvez créer un fichier `rust-toolchain.toml` à la racine de votre projet avec le contenu suivant :
    ```toml
    [toolchain]
    channel = "nightly"
    ```
    Ensuite, vous pouvez simplement exécuter `OPENSSL_STATIC=yes cargo build --release` comme d'habitude, et `rustup` sélectionnera automatiquement la toolchain nightly pour ce projet.

**2. Rétrograder l'édition de votre projet (Si les fonctionnalités `edition2024` ne sont pas critiques)**

Si votre projet ne dépend pas strictement des fonctionnalités `edition2024`, vous pourriez changer l'édition pour `2021` (l'édition stable actuelle) dans votre `Cargo.toml`.

  * **Modifier `Cargo.toml` :** Ouvrez le fichier `Cargo.toml` de votre projet (spécifiquement `/Users/lzwjava/projects/seeker/seeker/Cargo.toml` comme indiqué dans l'erreur) et changez le champ `edition` :
    ```toml
    [package]
    name = "your-package-name"
    version = "0.1.0"
    edition = "2021" # Changez ceci de "2024" à "2021"
    ```
  * **Exécuter `cargo fix --edition` (Optionnel mais recommandé) :** Après avoir changé l'édition, vous devrez peut-être exécuter `cargo fix --edition` pour mettre à jour automatiquement certains codes afin qu'ils soient compatibles avec l'ancienne édition.

### Quelle est la dernière version de Cargo ?

En juillet 2025, la dernière version **stable** de Cargo (et Rust) est **1.88.0**.

La fonctionnalité `edition2024` est toujours dans le canal nightly, ce qui signifie qu'elle est en cours de développement actif et ne fait pas encore partie d'une version stable. Elle devrait être stabilisée dans une future version, probablement Rust 1.89.0 (actuellement en bêta).