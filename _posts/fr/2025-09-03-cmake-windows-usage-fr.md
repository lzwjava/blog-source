---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Utilisation et Explication de CMake sur Windows
translated: true
type: note
---

Excellente question ! Voyons ce qu'est **CMake**, comment l'utiliser — particulièrement sur **Windows**, et ce que signifient des commandes comme `cmake --build`.

---

### 🔹 Qu'est-ce que CMake ?
- **CMake** est un générateur de système de build multiplateforme.
- Il ne construit **pas** les projets lui-même — il crée les fichiers de build appropriés (comme des solutions Visual Studio, des Makefiles, des fichiers Ninja, etc.) pour votre plateforme et votre compilateur.
- Ensuite, vous utilisez ces fichiers générés (ou le pilote de build intégré de CMake) pour compiler réellement votre projet.

---

### 🔹 Installer CMake sur Windows
1. Téléchargez-le depuis : [https://cmake.org/download/](https://cmake.org/download/)
2. Installez-le, et assurez-vous que l'option **"Add CMake to system PATH"** est cochée (ou ajoutez-le manuellement).
3. Vérifiez dans un terminal (PowerShell ou CMD) :
   ```sh
   cmake --version
   ```

---

### 🔹 Workflow typique de CMake sur Windows

Imaginons que votre projet ait cette structure :
```
project_root/
 ├─ CMakeLists.txt
 └─ src/
     └─ main.cpp
```

#### 1. Ouvrez un terminal
(Vous pouvez utiliser **x64 Native Tools Command Prompt for VS** si vous utilisez MSVC, ou simplement PowerShell normal si vous utilisez `MinGW`/`Ninja`.)

#### 2. Créez un répertoire de build
Il est préférable de séparer le code source et le build :
```sh
cd project_root
mkdir build
cd build
```

#### 3. Générez les fichiers du système de build
Exemple avec Visual Studio :
```sh
cmake .. -G "Visual Studio 17 2022" -A x64
```

Exemple avec Ninja :
```sh
cmake .. -G Ninja
```

Cette étape lit `../CMakeLists.txt` et génère les définitions de build nécessaires.

#### 4. Construisez le projet
Maintenant, vous pouvez utiliser :
```sh
cmake --build .
```

- Sur Windows avec Visual Studio, cette commande appelle en réalité `MSBuild` en arrière-plan.
- Avec Ninja, elle appelle l'outil `ninja`.

Vous pouvez aussi demander à CMake de construire en mode **Release** :
```sh
cmake --build . --config Release
```
⚠ Note : `--config` n'est utilisé qu'avec les générateurs multi-configuration (Visual Studio, Xcode). Si vous utilisez Ninja ou Makefiles, vous devez le spécifier lors de la configuration :
```sh
cmake .. -DCMAKE_BUILD_TYPE=Release
```

#### 5. Exécutez votre binaire
Après la construction, cherchez dans le répertoire approprié :
- Pour **Visual Studio** : `build/Debug/` ou `build/Release/`
- Pour **Ninja** : directement dans `build/`

---

### 🔹 Aide-mémoire des commandes courantes
```sh
# Configurer le projet (générer les fichiers de build)
cmake -S . -B build

# Configurer avec le type de build Release (générateur mono-configuration)
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release

# Construire le projet
cmake --build build

# Construire avec une configuration spécifique (pour Visual Studio/Xcode)
cmake --build build --config Release

# Installer les sorties compilées (si défini dans CMakeLists)
cmake --install build
```

---

✅ **Résumé** :  
- **`cmake ..`** → Configure et génère les fichiers de projet/build spécifiques à la plateforme.  
- **`cmake --build .`** → Compile réellement en utilisant l'outil de build choisi.  
- Sur Windows, vous utiliserez souvent les **générateurs Visual Studio** ou **Ninja** pour de meilleures performances.  

---

Souhaitez-vous que je vous donne un exemple **minimal de CMakeLists.txt** et que je vous guide pas à pas pour construire un simple projet C++ "Hello World" sur Windows ?