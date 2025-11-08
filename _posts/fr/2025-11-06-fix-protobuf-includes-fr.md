---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Correction des Fichiers d'Inclusion Protobuf Manquants
translated: true
type: note
---

### Comprendre l'erreur

Cet échec dans `greptime-proto` (épinglé au commit `14b9dc40` du dépôt GreptimeTeam) se produit lors de la compilation des protobufs. Plus précisément, `protoc` ne parvient pas à localiser le type standard bien connu de Google `google/protobuf/duration.proto` (et probablement d'autres comme `timestamp.proto`). Cela entraîne des erreurs d'importation en cascade dans les propres protos de GreptimeDB (par exemple, `ddl.proto` importe Duration, ce qui provoque des erreurs de type non défini dans `database.proto`).

La cause racine : Votre installation de `protoc` (provenant de la mise à niveau manuelle) inclut uniquement le binaire (`/usr/local/bin/protoc`), mais pas les fichiers d'en-tête contenant les protos de base de Google. `prost-build` dans le `build.rs` de la crate exécute `protoc` sans définir explicitement `--proto_path` vers les includes de Google, donc il échoue sur les imports relatifs comme `"google/protobuf/duration.proto"`.

Ceci est courant avec les installations de protobuf binaires uniquement ; le SDK complet fournit `/usr/include/google/protobuf/` (ou équivalent).

### Correction rapide : Installer les Includes Protobuf

Puisque vous avez déjà un binaire `protoc` récent, ajoutez les includes manquants sans procéder à une rétrogradation :

1. **Téléchargez la Version Complète de Protobuf** (correspondant à votre version de protoc, par exemple 27.3 ou la dernière) :
   ```
   wget https://github.com/protocolbuffers/protobuf/releases/download/v27.3/protoc-27.3-linux-x86_64.zip
   unzip protoc-27.3-linux-x86_64.zip -d protoc-full
   ```

2. **Installez les Fichiers d'En-tête** :
   ```
   sudo mkdir -p /usr/local/include/google/protobuf
   sudo cp -r protoc-full/include/google /usr/local/include/
   sudo chmod -R a+r /usr/local/include/google/protobuf  # Assure la lisibilité
   rm -rf protoc-full protoc-*.zip  # Nettoyage
   ```

3. **Vérifiez** :
   - Vérifiez protoc : `protoc --version` (devrait être ≥3.21).
   - Testez les includes : `ls /usr/local/include/google/protobuf/duration.proto` (devrait exister).
   - Test rapide de fonctionnement : `protoc --proto_path=/usr/local/include proto/greptime/v1/ddl.proto --decode_raw=stdin < /dev/null` (depuis votre répertoire de projet ; ignorez la sortie, vérifiez juste l'absence de "File not found").

4. **Relancez la Construction** :
   ```
   make clean  # Efface les constructions partielles
   make
   ```

Si vous êtes sur une distribution avec `apt` (par exemple, Ubuntu), une alternative est `sudo apt install libprotobuf-dev`—mais cela pourrait installer une version plus ancienne (par exemple, 3.12), entrant en conflit avec votre protoc manuel. Si c'est le cas, utilisez la copie manuelle des includes et définissez explicitement `PROTOC=/usr/local/bin/protoc`.

### Conseils supplémentaires
- Si les erreurs persistent (par exemple, d'autres protos manquants comme `wrappers.proto`), la copie complète de `include/google/` devrait les inclure.
- Pour les constructions conteneurisées (Docker), ajoutez ces étapes à votre Dockerfile.
- Après la construction, testez avec `cargo run --bin greptime -- standalone start` pour vous assurer que les protos s'intègrent correctement.
- Cette révision de greptime-proto est récente (environ Oct 2024) ; si des problèmes persistent, vérifiez les correctifs en amont dans le dépôt.

[Documentation de construction GreptimeDB](https://github.com/GreptimeTeam/greptimedb#build-from-source)  
[Types bien connus Protobuf](https://protobuf.dev/reference/protobuf/google.protobuf/)