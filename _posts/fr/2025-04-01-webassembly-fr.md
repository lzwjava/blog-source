---
audio: false
generated: true
lang: fr
layout: post
title: WebAssembly
translated: true
type: note
---

Plongeons dans un guide complet sur WebAssembly (Wasm). Je vais le décomposer en sections digestes : ce que c'est, comment ça fonctionne, pourquoi c'est important, comment l'utiliser et son avenir. À la fin, vous aurez une solide compréhension de WebAssembly et saurez comment commencer à l'utiliser.

---

### **1. Qu'est-ce que WebAssembly ?**
WebAssembly est un format d'instructions binaires conçu comme une cible de compilation portable et performante pour les langages de programmation. C'est un langage de bas niveau, semblable à l'assembleur, avec une représentation binaire compacte, mais il n'est pas destiné à être écrit directement par des humains – il est plutôt généré en compilant des langages de plus haut niveau comme le C, C++, Rust, Go, ou même Python.

- **Caractéristiques principales :**
  - **Performance :** S'exécute à une vitesse proche du natif en tirant parti des capacités matérielles.
  - **Portabilité :** Fonctionne de manière cohérente sur toutes les plateformes (navigateurs, serveurs, appareils IoT, etc.).
  - **Sécurité :** Fonctionne dans un environnement sandboxé, l'isolant du système hôte.
  - **Interopérabilité :** Fonctionne aux côtés de JavaScript, et non contre lui.

- **Historique :**
  - Introduit en 2015 grâce à une collaboration entre Mozilla, Google, Microsoft et Apple.
  - Devenu une recommandation du W3C en 2019, le marquant comme un standard web officiel.

- **Cas d'utilisation :**
  - Jeux web (par exemple, les exports Unity ou Unreal Engine).
  - Applications critiques en performance (par exemple, éditeurs vidéo comme Figma ou outils de type Photoshop).
  - Applications côté serveur (par exemple, avec Node.js).
  - Exécution de bases de code legacy dans des environnements modernes.

---

### **2. Comment fonctionne WebAssembly ?**
WebAssembly comble le fossé entre le code de haut niveau et l'exécution machine. Voici le processus :

1. **Code source :** Vous écrivez du code dans un langage comme C++ ou Rust.
2. **Compilation :** Un compilateur (par exemple, Emscripten pour C/C++ ou `wasm-pack` pour Rust) le traduit dans le format binaire de WebAssembly (fichiers `.wasm`).
3. **Exécution :**
   - Dans les navigateurs, le fichier `.wasm` est récupéré (souvent via JavaScript), validé et compilé en code machine par le runtime Wasm du navigateur.
   - Le runtime l'exécute dans un sandbox, garantissant la sécurité.

- **Format texte (WAT) :** WebAssembly a également une représentation texte lisible par l'homme (`.wat`), utile pour le débogage ou l'apprentissage. Par exemple :
  ```wat
  (module
    (func (export "add") (param i32 i32) (result i32)
      local.get 0
      local.get 1
      i32.add)
  )
  ```
  Ceci définit une fonction `add` qui prend deux entiers 32 bits et retourne leur somme.

- **Modèle de mémoire :** Wasm utilise un modèle de mémoire linéaire – un tableau plat d'octets que le programme peut lire/écrire. Il est géré manuellement ou via le runtime du langage source.

- **Interaction avec JavaScript :** Vous chargez les modules Wasm en JavaScript en utilisant `WebAssembly.instantiate()` ou `fetch()` et appelez les fonctions exportées. Wasm peut également rappeler JavaScript.

---

### **3. Pourquoi utiliser WebAssembly ?**
- **Vitesse :** Les binaires pré-compilés s'exécutent plus vite que le JavaScript interprété.
- **Flexibilité des langages :** Utilisez le C, Rust, etc., au lieu d'être limité au JavaScript.
- **Efficacité de taille :** Les fichiers `.wasm` sont plus petits que le JavaScript équivalent, réduisant les temps de chargement.
- **Multi-plateforme :** Écrivez une fois, exécutez partout – navigateurs, serveurs ou appareils embarqués.
- **Sécurité :** Le sandboxing empêche le code malveillant d'accéder au système hôte.

**Compromis :**
- Pas d'accès direct au DOM (vous avez besoin de JavaScript pour cela).
- L'outillage peut être complexe pour les débutants.
- Le débogage est plus délicat qu'avec JavaScript.

---

### **4. Commencer avec WebAssembly**
Parcourons un exemple simple : compiler une fonction C en WebAssembly et l'exécuter dans un navigateur.

#### **Étape 1 : Installer les outils**
- **Emscripten :** Une chaîne d'outils pour compiler C/C++ vers WebAssembly.
  - Installation : Suivez le [guide d'Emscripten](https://emscripten.org/docs/getting_started/downloads.html) (nécessite Python, CMake, etc.).
- **Node.js :** Optionnel, pour exécuter Wasm en dehors du navigateur.
- **Un serveur web :** Les navigateurs exigent que les fichiers `.wasm` soient servis via HTTP (par exemple, utilisez `python -m http.server`).

#### **Étape 2 : Écrire le code**
Créez un fichier `add.c` :
```c
int add(int a, int b) {
    return a + b;
}
```

#### **Étape 3 : Compiler vers WebAssembly**
Exécutez cette commande Emscripten :
```bash
emcc add.c -s EXPORTED_FUNCTIONS='["_add"]' -s EXPORT_ES6=1 -s MODULARIZE=1 -o add.js
```
- Produit `add.js` (un script de liaison) et `add.wasm` (le binaire).

#### **Étape 4 : Utiliser en HTML**
Créez `index.html` :
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <script type="module">
        import init, { add } from './add.js';
        async function run() {
            await init();
            console.log(add(5, 3)); // Affiche 8
        }
        run();
    </script>
</body>
</html>
```

#### **Étape 5 : Servir et tester**
- Démarrez un serveur local : `python -m http.server 8080`
- Ouvrez `http://localhost:8080` dans un navigateur et vérifiez la console.

Pour Rust, vous utiliseriez `cargo` et `wasm-pack` – processus similaire, chaîne d'outils différente.

---

### **5. Écosystème et outils**
- **Langages :**
  - **C/C++ :** Emscripten.
  - **Rust :** `wasm-pack`, `wasm-bindgen`.
  - **Go :** Support Wasm intégré (`GOOS=js GOARCH=wasm`).
  - **AssemblyScript :** Syntaxe de type TypeScript pour Wasm.

- **Runtimes :**
  - **Navigateurs :** Chrome, Firefox, Safari, Edge.
  - **Node.js :** Avec `--experimental-wasm-modules`.
  - **Autonomes :** Wasmtime, Wasmer, WasmEdge.

- **Bibliothèques :**
  - **WebGL :** Pour les graphismes (par exemple, les jeux).
  - **WASI :** WebAssembly System Interface pour les cas d'utilisation non web (E/S de fichiers, etc.).

---

### **6. Fonctionnalités avancées**
- **Threads :** Pris en charge avec SharedArrayBuffer pour le parallélisme.
- **SIMD :** Instructions vectorielles pour les tâches lourdes en calcul (par exemple, traitement d'image).
- **WASI :** Étend Wasm au-delà du web, en ajoutant des appels système.
- **Liaison dynamique :** Chargez plusieurs modules `.wasm` et liez-les à l'exécution.

---

### **7. L'avenir de WebAssembly**
- **Adoption plus large :** De plus en plus de langages et frameworks ajoutent le support Wasm.
- **Serverless Computing :** La nature légère de Wasm convient au edge computing.
- **Standardisation :** Des propositions comme le garbage collection et la gestion des exceptions sont en cours.
- **Croissance hors web :** WASI et les runtimes comme Wasmer poussent Wasm dans l'IoT, les applications de bureau, et plus encore.

---

### **8. Ressources pour en savoir plus**
- **Site officiel :** [webassembly.org](https://webassembly.org/)
- **Documentation MDN :** [WebAssembly sur MDN](https://developer.mozilla.org/fr/docs/WebAssembly)
- **Tutoriels :** Le livre "Rust and WebAssembly" (rustwasm.github.io/book) ou la documentation d'Emscripten.
- **Posts X :** Recherchez #WebAssembly sur X pour des exemples concrets et des discussions.

---

### **Récapitulatif rapide**
WebAssembly est un changement majeur pour la performance et la portabilité. Vous écrivez dans votre langage préféré, compilez en `.wasm`, et l'exécutez partout – rapidement. Ce n'est pas une solution miracle (JavaScript règne toujours sur l'interactivité du web), mais c'est un outil puissant dans la boîte à outils du développeur moderne.

Vous voulez essayer un exemple spécifique, explorer un cas d'utilisation ou résoudre un problème ? Faites-le moi savoir !