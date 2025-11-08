---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Corriger l'Erreur de Version de Protoc dans la Construction Substrait
translated: true
type: note
---

### Comprendre l'erreur

Cet échec de compilation se produit dans la crate `substrait` (v0.58.0), dont GreptimeDB dépend pour la planification de requêtes interlangues. L'erreur provient du compilateur protobuf (`protoc`) qui rejette le fichier `substrait/algebra.proto` car il utilise des champs "optionnels" dans la syntaxe proto3—une fonctionnalité qui nécessite soit :

- Une version de Protoc ≥3.21 (où la prise en charge est stable et aucun drapeau spécial n'est nécessaire), soit
- Une version plus ancienne de protoc (par exemple, 3.15–3.20) avec le drapeau `--experimental_allow_proto3_optional` passé pendant la compilation.

L'outil `prost-build` dans le script de construction de `substrait` ne passe pas ce drapeau, il suppose donc une version compatible de protoc. Le `protobuf-compiler` de votre système (probablement provenant de `apt` sur Ubuntu 22.04 ou antérieur, donnant ~3.12.4) est trop ancien et ne possède pas ce drapeau, ce qui provoque le panic.

La documentation de GreptimeDB spécifie protoc ≥3.15, mais pour cette dépendance, ≥3.21 est effectivement requis.

### Correction rapide : Mettre à niveau Protoc vers ≥3.21

Le moyen le plus simple, sans droits root, est de télécharger et d'installer la version binaire officielle (aucune compilation nécessaire). Voici comment :

1.  **Télécharger la dernière version de Protoc** :
    - Allez sur [Protocol Buffers Releases](https://github.com/protocolbuffers/protobuf/releases).
    - Récupérez le dernier `protoc-<version>-linux-x86_64.zip` (par exemple, `protoc-28.1-linux-x86_64.zip` ou quel que soit le plus récent—tout ce qui est ≥3.21 fonctionne).
    - Exemple de lien direct (ajuster la version) :  
      `wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip`

2.  **Installez-le** :
    ```
    unzip protoc-*.zip -d protoc-install
    sudo mv protoc-install/bin/protoc /usr/local/bin/
    sudo chmod +x /usr/local/bin/protoc
    rm -rf protoc-install protoc-*.zip  # Nettoyage
    ```

3.  **Vérifiez** :
    ```
    protoc --version
    ```
    Devrait afficher `libprotoc 27.3` (ou supérieur). Si c'est toujours l'ancienne version, vérifiez votre PATH (`echo $PATH`)—`/usr/local/bin` devrait venir avant `/usr/bin`.

4.  **Relancez la construction** :
    ```
    make clean  # Efface les cibles obsolètes
    make
    ```

Cela remplace le `protoc` du système sans entrer en conflit avec les paquets `apt`. Si vous êtes sur une distribution plus récente comme Ubuntu 24.04+, `apt install protobuf-compiler` pourrait déjà donner ≥3.21—vérifiez d'abord votre version.

### Si vous ne pouvez pas mettre à niveau (cas rares)
- Si vous êtes bloqué sur un ancien système, vous devriez patcher le `build.rs` de `substrait` pour ajouter le drapeau (via `Command::new(protoc).arg("--experimental_allow_proto3_optional")`), mais cela nécessite de forker la crate et de mettre à jour le `Cargo.toml` de GreptimeDB—complexe et non recommandé.
- Alternativement, certaines crates offrent une fonctionnalité `protobuf-src` pour inclure un protoc récent, mais `substrait` ne l'active pas par défaut.

### Conseils supplémentaires
- Assurez-vous d'avoir les autres prérequis : `build-essential` (pour GCC), `libc6-dev` (en-têtes glibc).
- Si la compilation réussit mais échoue plus tard sur des dépendances C++ (par exemple, Arrow), installez `libarrow-dev` via conda ou apt.
- Pour CI/CD ou Docker : Ajoutez l'étape de téléchargement à votre environnement.

Cela devrait résoudre le problème—`substrait` se compile sans erreur sur les configurations modernes. Si vous rencontrez un autre problème, partagez `protoc --version` et votre distribution.

[GreptimeDB Build Docs](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Protobuf Releases](https://github.com/protocolbuffers/protobuf/releases)  
[Proto3 Optional Fields](https://protobuf.dev/programming-guides/proto3/#optional)