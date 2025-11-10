---
audio: false
generated: true
lang: fr
layout: post
title: La relation de Rust avec le C
translated: true
type: note
---

Non, Rust n'est pas "construit sur C" dans le sens où il compilerait vers C ou nécessiterait C comme couche fondamentale pour son propre fonctionnement. Rust est un langage de programmation système moderne et distinct.

Voici une explication de la relation entre Rust et C, et comment Rust interagit avec les bibliothèques C :

**Rust est-il construit sur C ?**

* **Compilateur :** Le compilateur Rust (`rustc`) est principalement écrit en Rust lui-même. Les premières versions du compilateur ont été amorcées en utilisant OCaml, mais il est maintenant auto-hébergé.
* **Interaction bas niveau :** Rust est un langage de bas niveau qui peut interagir directement avec le système d'exploitation et le matériel, un peu comme C ou C++. Il ne repose pas sur C comme intermédiaire pour ces opérations fondamentales.
* **LLVM :** Le compilateur de Rust utilise LLVM (Low Level Virtual Machine) comme backend pour la génération de code et l'optimisation. LLVM lui-même est largement écrit en C++. Cela signifie que le code Rust est finalement traduit en Représentation Intermédiaire LLVM (IR), qui est ensuite optimisée et compilée en code machine. Donc, en ce sens, il existe une dépendance à une chaîne d'outils basée sur C++ (LLVM), mais Rust lui-même n'est pas "construit sur C."

**Rust peut-il utiliser toutes les bibliothèques C ?**

Oui, Rust offre une excellente interopérabilité avec les bibliothèques C via son **Foreign Function Interface (FFI)**. Cela signifie que vous pouvez appeler des fonctions et utiliser des structures de données provenant de bibliothèques C existantes directement depuis votre code Rust.

Voici comment cela fonctionne généralement :

1.  **Blocs `extern "C"` :** Vous définissez un bloc `extern "C"` dans votre code Rust pour déclarer les signatures des fonctions C que vous souhaitez appeler. Cela indique au compilateur Rust que ces fonctions respectent l'Application Binary Interface (ABI) C, qui dicte la manière dont les fonctions sont appelées et les données sont organisées en mémoire.
2.  **Attribut `#[link]` :** Vous utilisez l'attribut `#[link(name = "foo")]` pour indiquer au linker Rust de lier contre la bibliothèque C spécifiée (par exemple, `libfoo.so` ou `foo.lib`).
3.  **Blocs `unsafe` :** Les appels aux fonctions C sont généralement encapsulés dans des blocs `unsafe` en Rust. Ceci est nécessaire car les fortes garanties de sécurité mémoire de Rust ne peuvent pas être appliquées lors de l'interaction avec du code "étranger" qui ne suit pas les règles de Rust. Vous, en tant que programmeur, êtes responsable de garantir la sécurité de ces appels.
4.  **`bindgen` :** Pour les bibliothèques C plus importantes, écrire manuellement toutes les déclarations `extern "C"` peut être fastidieux. Des outils comme `bindgen` peuvent générer automatiquement les bindings Rust FFI à partir des fichiers d'en-tête C, simplifiant grandement le processus.
5.  **Crate `cty` :** La crate `cty` fournit des types primitifs compatibles C (comme `c_int`, `c_char`, etc.) pour garantir un mappage correct des types de données entre Rust et C.

**Pourquoi utiliser des bibliothèques C en Rust ?**

* **Tirer parti du code existant :** Il existe un vaste écosystème de bibliothèques C bien testées et hautement optimisées pour diverses tâches (par exemple, appels système, cryptographie, calcul numérique, graphismes). Rust vous permet d'exploiter cette ressource existante sans tout réécrire à partir de zéro.
* **Interfaces du système d'exploitation :** Les systèmes d'exploitation exposent une grande partie de leurs fonctionnalités via des interfaces compatibles C. Rust doit être capable d'appeler ces fonctions pour interagir avec le SE.
* **Sections critiques pour les performances :** Bien que Rust soit généralement très rapide, certains codes hautement spécialisés et critiques pour les performances peuvent déjà exister en C et peuvent être intégrés directement.

En résumé, Rust n'est pas "construit sur C", mais il fournit des mécanismes robustes (FFI) pour une interopérabilité transparente avec les bibliothèques C, permettant aux développeurs Rust de tirer parti du vaste écosystème C.