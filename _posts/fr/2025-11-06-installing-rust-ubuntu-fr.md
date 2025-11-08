---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Installation de Rust sur Ubuntu
translated: true
type: note
---

### Installation de Rust sur Ubuntu 22.04 LTS

Rust est mieux installé en utilisant `rustup`, l'installateur officiel de la toolchain. Cette méthode est simple, prend en charge les mises à jour faciles et fonctionne sur votre système Ubuntu 22.04 64 bits. Aucune dépendance supplémentaire n'est généralement nécessaire au-delà d'une configuration Ubuntu de base.

#### Instructions détaillées

1. **Mettez à jour votre liste de paquets** (optionnel mais recommandé) :
   ```
   sudo apt update
   ```

2. **Installez Rust en utilisant rustup** :
   Exécutez la commande suivante pour télécharger et exécuter le script d'installation :
   ```
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```
   - Cela téléchargera le script de manière sécurisée via HTTPS.
   - Lorsque vous y êtes invité, choisissez l'option d'installation par défaut (appuyez sur `1` puis Entrée).
   - L'installateur ajoutera les binaires Rust à `~/.cargo/bin` et mettra à jour votre profil shell (par exemple, `~/.bashrc` ou `~/.profile`).

3. **Rechargez votre configuration shell** :
   Pour que les modifications prennent effet immédiatement sans redémarrer votre terminal :
   ```
   source ~/.cargo/env
   ```
   Alternativement, fermez et rouvrez votre terminal.

4. **Vérifiez l'installation** :
   Vérifiez que Rust est correctement installé :
   ```
   rustc --version
   cargo --version
   ```
   Vous devriez voir une sortie similaire à `rustc 1.82.0` (ou la dernière version stable) et similaire pour Cargo.

#### Notes supplémentaires
- **Désinstallation** : Si nécessaire, exécutez `rustup self uninstall`.
- **Mise à jour de Rust** : Utilisez `rustup update` pour obtenir la dernière version.
- **IDE/Support** : Pour le développement, envisagez d'installer `rust-analyzer` via votre éditeur (par exemple, l'extension VS Code) pour une meilleure complétion de code.
- Ceci installe la chaîne stable par défaut. Pour nightly ou beta, utilisez `rustup install nightly` après la configuration.

Si vous rencontrez des erreurs (par exemple, curl introuvable), installez-le avec `sudo apt install curl`.

[Guide d'installation officiel de Rust](https://www.rust-lang.org/tools/install)