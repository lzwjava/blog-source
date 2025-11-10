---
audio: false
generated: true
lang: fr
layout: post
title: Installer Rust sur macOS avec rustup
translated: true
type: note
---

## Installation de Rust avec rustup

1. **Ouvrir le Terminal**  
   Vous pouvez trouver le Terminal dans **Applications > Utilitaires** ou le rechercher avec Spotlight.

2. **Installer rustup et Rust**  
   Exécutez la commande suivante pour télécharger et lancer le script d'installation de rustup :

    ```sh
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

    Le script vous demandera de continuer. Appuyez sur `1` pour l'installation par défaut.

3. **Configurer votre Shell**  
   Après l'installation, vous devrez peut-être ajouter Rust au `PATH` de votre système. L'installateur fournira une commande similaire à :

    ```sh
    source $HOME/.cargo/env
    ```

    Ajoutez cette ligne à votre fichier de configuration de shell (par exemple, `.zshrc`, `.bashrc`, ou `.bash_profile`) pour rendre Rust disponible dans les sessions futures.

4. **Vérifier l'Installation**  
   Vérifiez que Rust est installé correctement :

    ```sh
    rustc --version
    ```

    Vous devriez voir la version du compilateur Rust si l'installation a réussi.

---

## Utilisation de Homebrew pour Installer Rust

Alternativement, vous pouvez utiliser [Homebrew](https://brew.sh/) pour installer Rust, bien que `rustup` soit généralement recommandé pour des mises à jour et une gestion de version plus faciles.

1. **Installer Homebrew** (s'il n'est pas déjà installé) :

    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Installer Rust avec Homebrew** :

    ```sh
    brew install rust
    ```

3. **Vérifier l'Installation** :

    ```sh
    rustc --version
    ```

---

## Compilation de Code Rust

1. **Écrire un Programme Rust**  
   Créez un fichier nommé `main.rs` avec le contenu suivant :

    ```rust
    fn main() {
         println!("Hello, World!");
    }
    ```

2. **Compiler le Programme**  
   Dans le terminal, naviguez vers le répertoire contenant votre fichier et exécutez :

    ```sh
    rustc main.rs
    ```

3. **Exécuter le Programme Compilé** :

    ```sh
    ./main
    ```

---

Cette configuration devrait vous permettre de commencer le développement avec Rust sur macOS. Si vous rencontrez des problèmes, n'hésitez pas à demander de l'aide !