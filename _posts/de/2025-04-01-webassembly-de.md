---
audio: false
generated: true
lang: de
layout: post
title: WebAssembly
translated: true
type: note
---

Lassen Sie uns in einen umfassenden Leitfaden zu WebAssembly (Wasm) eintauchen. Ich werde es in verdauliche Abschnitte unterteilen: was es ist, wie es funktioniert, warum es wichtig ist, wie man es verwendet und wohin die Reise geht. Am Ende werden Sie ein solides Verständnis von WebAssembly haben und wissen, wie Sie damit beginnen können.

---

### **1. Was ist WebAssembly?**
WebAssembly ist ein binäres Instruktionsformat, das als portables, leistungsstarkes Kompilierungsziel für Programmiersprachen entwickelt wurde. Es ist eine low-level, assemblerähnliche Sprache mit einer kompakten binären Repräsentation, die jedoch nicht direkt von Menschen geschrieben werden soll – stattdessen wird sie durch das Kompilieren höherer Sprachen wie C, C++, Rust, Go oder sogar Python erzeugt.

- **Schlüsselmerkmale:**
  - **Leistung:** Führt Code mit nahezu nativer Geschwindigkeit aus, indem Hardware-Fähigkeiten genutzt werden.
  - **Portabilität:** Läuft konsistent über verschiedene Plattformen hinweg (Browser, Server, IoT-Geräte usw.).
  - **Sicherheit:** Operiert in einer Sandbox-Umgebung, die es vom Host-System isoliert.
  - **Interoperabilität:** Funktioniert zusammen mit JavaScript, nicht gegen es.

- **Geschichte:**
  - Eingeführt im Jahr 2015 durch eine Zusammenarbeit von Mozilla, Google, Microsoft und Apple.
  - Wurde 2019 eine W3C-Empfehlung, was es zu einem offiziellen Web-Standard machte.

- **Anwendungsfälle:**
  - Web-Spiele (z.B. Unity- oder Unreal Engine-Exporte).
  - Leistungskritische Anwendungen (z.B. Video-Editoren wie Figma oder Photoshop-ähnliche Tools).
  - Server-seitige Anwendungen (z.B. mit Node.js).
  - Ausführen von Legacy-Codebasen in modernen Umgebungen.

---

### **2. Wie funktioniert WebAssembly?**
WebAssembly überbrückt die Lücke zwischen High-Level-Code und Maschinenausführung. So läuft der Prozess ab:

1. **Quellcode:** Sie schreiben Code in einer Sprache wie C++ oder Rust.
2. **Kompilierung:** Ein Compiler (z.B. Emscripten für C/C++ oder `wasm-pack` für Rust) übersetzt ihn in das binäre Format von WebAssembly (`.wasm`-Dateien).
3. **Ausführung:**
   - In Browsern wird die `.wasm`-Datei abgerufen (oft via JavaScript), validiert und durch die Wasm-Laufzeitumgebung des Browsers in Maschinencode kompiliert.
   - Die Laufzeitumgebung führt ihn in einer Sandbox aus, was Sicherheit gewährleistet.

- **Textformat (WAT):** WebAssembly hat auch eine menschenlesbare Textdarstellung (`.wat`), nützlich für Debugging oder zum Lernen. Zum Beispiel:
  ```wat
  (module
    (func (export "add") (param i32 i32) (result i32)
      local.get 0
      local.get 1
      i32.add)
  )
  ```
  Dies definiert eine Funktion `add`, die zwei 32-Bit-Ganzzahlen entgegennimmt und ihre Summe zurückgibt.

- **Speichermodell:** Wasm verwendet ein lineares Speichermodell – ein flaches Byte-Array, das das Programm lesen und beschreiben kann. Es wird manuell oder über die Laufzeitumgebung der Quellsprache verwaltet.

- **Interaktion mit JavaScript:** Sie laden Wasm-Module in JavaScript mit `WebAssembly.instantiate()` oder `fetch()` und rufen exportierte Funktionen auf. Wasm kann auch zurück in JavaScript aufrufen.

---

### **3. Warum WebAssembly verwenden?**
- **Geschwindigkeit:** Vorkompilierte Binärdateien laufen schneller als interpretiertes JavaScript.
- **Sprachflexibilität:** Verwenden Sie C, Rust usw., anstatt auf JavaScript festgelegt zu sein.
- **Größeneffizienz:** `.wasm`-Dateien sind kleiner als äquivalenter JavaScript-Code, was Ladezeiten reduziert.
- **Plattformübergreifend:** Einmal schreiben, überall ausführen – Browser, Server oder eingebettete Geräte.
- **Sicherheit:** Sandboxing verhindert, dass bösartiger Code auf das Host-System zugreift.

**Kompromisse:**
- Kein direkter DOM-Zugriff (dafür benötigen Sie JavaScript).
- Die Tooling-Umgebung kann für Anfänger komplex sein.
- Debugging ist schwieriger als mit JavaScript.

---

### **4. Erste Schritte mit WebAssembly**
Lassen Sie uns ein einfaches Beispiel durchgehen: Kompilieren einer C-Funktion nach WebAssembly und Ausführen in einem Browser.

#### **Schritt 1: Tools installieren**
- **Emscripten:** Eine Toolchain zum Kompilieren von C/C++ zu WebAssembly.
  - Installation: Befolgen Sie die [Anleitung von Emscripten](https://emscripten.org/docs/getting_started/downloads.html) (benötigt Python, CMake, etc.).
- **Node.js:** Optional, zum Ausführen von Wasm außerhalb des Browsers.
- **Ein Web-Server:** Browser benötigen, dass `.wasm`-Dateien über HTTP bereitgestellt werden (z.B. mit `python -m http.server`).

#### **Schritt 2: Code schreiben**
Erstellen Sie eine Datei `add.c`:
```c
int add(int a, int b) {
    return a + b;
}
```

#### **Schritt 3: Nach WebAssembly kompilieren**
Führen Sie diesen Emscripten-Befehl aus:
```bash
emcc add.c -s EXPORTED_FUNCTIONS='["_add"]' -s EXPORT_ES6=1 -s MODULARIZE=1 -o add.js
```
- Erzeugt `add.js` (ein Verbindungsskript) und `add.wasm` (das Binärformat).

#### **Schritt 4: In HTML verwenden**
Erstellen Sie `index.html`:
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
            console.log(add(5, 3)); // Gibt 8 aus
        }
        run();
    </script>
</body>
</html>
```

#### **Schritt 5: Bereitstellen und Testen**
- Starten Sie einen lokalen Server: `python -m http.server 8080`
- Öffnen Sie `http://localhost:8080` in einem Browser und prüfen Sie die Konsole.

Für Rust würden Sie `cargo` und `wasm-pack` verwenden – ähnlicher Prozess, andere Toolchain.

---

### **5. Ökosystem und Tools**
- **Sprachen:**
  - **C/C++:** Emscripten.
  - **Rust:** `wasm-pack`, `wasm-bindgen`.
  - **Go:** Eingebaute Wasm-Unterstützung (`GOOS=js GOARCH=wasm`).
  - **AssemblyScript:** TypeScript-ähnliche Syntax für Wasm.

- **Laufzeitumgebungen:**
  - **Browser:** Chrome, Firefox, Safari, Edge.
  - **Node.js:** Mit `--experimental-wasm-modules`.
  - **Standalone:** Wasmtime, Wasmer, WasmEdge.

- **Bibliotheken:**
  - **WebGL:** Für Grafik (z.B. Spiele).
  - **WASI:** WebAssembly System Interface für Nicht-Web-Anwendungsfälle (Datei-I/O, etc.).

---

### **6. Erweiterte Funktionen**
- **Threads:** Unterstützt mit SharedArrayBuffer für Parallelität.
- **SIMD:** Vektorinstruktionen für mathelastige Aufgaben (z.B. Bildverarbeitung).
- **WASI:** Erweitert Wasm über das Web hinaus und fügt Systemaufrufe hinzu.
- **Dynamisches Linking:** Lädt mehrere `.wasm`-Module und verbindet sie zur Laufzeit.

---

### **7. Die Zukunft von WebAssembly**
- **Breitere Adoption:** Immer mehr Sprachen und Frameworks fügen Wasm-Unterstützung hinzu.
- **Serverless Computing:** Die schlanke Natur von Wasm eignet sich für Edge Computing.
- **Standardisierung:** Vorschläge wie Garbage Collection und Exception Handling sind in Arbeit.
- **Wachstum außerhalb des Webs:** WASI und Laufzeitumgebungen wie Wasmer treiben Wasm in IoT, Desktop-Apps und mehr.

---

### **8. Ressourcen zum Weiterlernen**
- **Offizielle Seite:** [webassembly.org](https://webassembly.org/)
- **MDN-Dokumentation:** [WebAssembly auf MDN](https://developer.mozilla.org/en-US/docs/WebAssembly)
- **Tutorials:** „Rust and WebAssembly“ Buch (rustwasm.github.io/book) oder Emscripten-Dokumentation.
- **X Posts:** Suchen Sie nach #WebAssembly auf X für Beispiele aus der Praxis und Diskussionen.

---

### **Kurze Zusammenfassung**
WebAssembly ist ein Game-Changer für Leistung und Portabilität. Sie schreiben in Ihrer Lieblingssprache, kompilieren zu `.wasm` und führen es überall aus – und das schnell. Es ist kein Allheilmittel (JavaScript regiert nach wie vor die Interaktivität im Web), aber es ist ein mächtiges Werkzeug im Werkzeugkasten des modernen Entwicklers.

Möchten Sie ein bestimmtes Beispiel ausprobieren, einen Anwendungsfall erkunden oder etwas debuggen? Lassen Sie es mich wissen!