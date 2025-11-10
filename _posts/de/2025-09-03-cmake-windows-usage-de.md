---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: CMake Verwendung und Erklärung unter Windows
translated: true
type: note
---

Gute Frage! Lassen Sie uns durchgehen, was **CMake** ist, wie man es verwendet – insbesondere unter **Windows**, und was Befehle wie `cmake --build` tatsächlich bedeuten.

---

### 🔹 Was ist CMake?
- **CMake** ist ein plattformübergreifender Build-System-Generator.
- Es baut Projekte **nicht** selbst – es erstellt die entsprechenden Build-Dateien (wie Visual Studio-Projektmappen, Makefiles, Ninja-Dateien etc.) für Ihre Plattform und Ihren Compiler.
- Anschließend verwenden Sie diese generierten Dateien (oder den eigenen Build-Treiber von CMake), um Ihr Projekt tatsächlich zu kompilieren.

---

### 🔹 CMake unter Windows installieren
1. Laden Sie es herunter von: [https://cmake.org/download/](https://cmake.org/download/)
2. Führen Sie die Installation aus und stellen Sie sicher, dass **"Add CMake to system PATH"** aktiviert ist (oder fügen Sie es manuell hinzu).
3. Überprüfen Sie die Installation in einem Terminal (PowerShell oder CMD):
   ```sh
   cmake --version
   ```

---

### 🔹 Typischer CMake-Workflow unter Windows

Angenommen, Ihr Projekt hat folgende Struktur:
```
project_root/
 ├─ CMakeLists.txt
 └─ src/
     └─ main.cpp
```

#### 1. Öffnen Sie ein Terminal
(Sie können **x64 Native Tools Command Prompt for VS** verwenden, wenn Sie MSVC nutzen, oder einfach die normale PowerShell, wenn Sie `MinGW`/`Ninja` verwenden.)

#### 2. Erstellen Sie ein Build-Verzeichnis
Es ist am besten, Quelle und Build zu trennen:
```sh
cd project_root
mkdir build
cd build
```

#### 3. Build-System-Dateien generieren
Beispiel mit Visual Studio:
```sh
cmake .. -G "Visual Studio 17 2022" -A x64
```

Beispiel mit Ninja:
```sh
cmake .. -G Ninja
```

Dieser Schritt liest `../CMakeLists.txt` und generiert die notwendigen Build-Definitionen.

#### 4. Das Projekt bauen
Jetzt können Sie verwenden:
```sh
cmake --build .
```

- Unter Windows mit Visual Studio ruft dies im Hintergrund `MSBuild` auf.
- Mit Ninja ruft es das `ninja`-Tool auf.

Sie können CMake auch anweisen, im **Release**-Modus zu bauen:
```sh
cmake --build . --config Release
```
⚠ Hinweis: `--config` wird nur bei Multi-Konfig-Generatoren (Visual Studio, Xcode) verwendet. Wenn Sie Ninja oder Makefiles verwenden, geben Sie dies bei der Konfiguration an:
```sh
cmake .. -DCMAKE_BUILD_TYPE=Release
```

#### 5. Ihre ausführbare Datei ausführen
Suchen Sie nach dem Bauen im entsprechenden Verzeichnis:
- Für **Visual Studio**: `build/Debug/` oder `build/Release/`
- Für **Ninja**: direkt innerhalb von `build/`

---

### 🔹 Häufige Befehle – Spickzettel
```sh
# Projekt konfigurieren (Build-Dateien generieren)
cmake -S . -B build

# Konfigurieren mit Release-Build-Typ (Single-Konfig-Generator)
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release

# Projekt bauen
cmake --build build

# Bauen mit spezifischer Konfiguration (für Visual Studio/Xcode)
cmake --build build --config Release

# Kompilierte Ausgaben installieren (falls in CMakeLists definiert)
cmake --install build
```

---

✅ **Zusammenfassung**:  
- **`cmake ..`** → Konfiguriert und generiert plattformspezifische Projekt-/Build-Dateien.  
- **`cmake --build .`** → Kompiliert tatsächlich unter Verwendung des gewählten Build-Tools.  
- Unter Windows verwenden Sie oft **Visual Studio-Generatoren** oder **Ninja** für eine bessere Leistung.  

---

Möchten Sie, dass ich Ihnen ein **minimales Beispiel-CMakeLists.txt** gebe und den Bau eines einfachen C++ "Hello World"-Projekts unter Windows Schritt für Schritt durchgehe?