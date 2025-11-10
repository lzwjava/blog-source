---
audio: false
generated: true
image: false
lang: de
layout: post
title: Erweiterungs-Host in VSCode starten
translated: true
type: note
---

Um **F5** in Visual Studio Code (VSCode) zu drücken, um den **Extension Development Host** für die Entwicklung einer VSCode-Erweiterung zu starten, befolgen Sie diese Schritte:

1. **Öffnen Sie Ihr Erweiterungsprojekt in VSCode**:
   - Stellen Sie sicher, dass Sie ein VSCode-Erweiterungsprojekt eingerichtet haben. Dies umfasst typischerweise eine `package.json` Datei mit den notwendigen Erweiterungskonfigurationen (z.B. `contributes`, `activationEvents`).
   - Öffnen Sie den Ordner, der Ihr Erweiterungsprojekt enthält, in VSCode, indem Sie `Datei > Ordner öffnen` auswählen oder `Strg+K, Strg+O` (Windows/Linux) bzw. `Befehl+K, Befehl+O` (Mac) verwenden.

2. **Überprüfen Sie Ihr Erweiterungs-Setup**:
   - Stellen Sie sicher, dass Sie eine gültige `package.json` Datei in Ihrem Projektstammverzeichnis haben, die mindestens die folgenden Felder enthält:
     ```json
     {
       "name": "your-extension-name",
       "displayName": "Your Extension Name",
       "description": "Description of your extension",
       "version": "0.0.1",
       "engines": {
         "vscode": "^1.60.0"
       },
       "categories": ["Other"],
       "activationEvents": ["*"],
       "main": "./extension.js",
       "contributes": {}
     }
     ```
   - Stellen Sie sicher, dass Sie eine `extension.js` (oder gleichwertige) Datei als Einstiegspunkt für Ihren Erweiterungscode haben.
   - Installieren Sie Abhängigkeiten, indem Sie `npm install` im integrierten Terminal (`Strg+``) ausführen, falls Ihre Erweiterung Node.js-Module verwendet.

3. **Drücken Sie F5, um den Extension Development Host zu starten**:
   - Drücken Sie **F5** auf Ihrer Tastatur, während Ihr Erweiterungsprojekt in VSCode geöffnet ist.
   - Dies startet den **Extension Development Host**, ein separates VSCode-Fenster, in dem Ihre Erweiterung zum Testen geladen ist.
   - VSCode wird automatisch:
     - Ihre Erweiterung bauen (falls TypeScript verwendet wird, kompiliert es `.ts`-Dateien zu `.js`).
     - Eine neue VSCode-Instanz mit Ihrer aktivierten Erweiterung starten.
     - Einen Debugger starten, der an den Extension Host-Prozess angehängt ist.

4. **Debugging-Konfiguration**:
   - VSCode verwendet eine `launch.json` Datei im `.vscode` Ordner, um das Debugging zu konfigurieren. Wenn sie nicht existiert, wird VSCode sie automatisch erstellen, wenn Sie zum ersten Mal F5 drücken.
   - Eine typische `launch.json` für eine Erweiterung sieht so aus:
     ```json
     {
       "version": "0.2.0",
       "configurations": [
         {
           "name": "Run Extension",
           "type": "extensionHost",
           "request": "launch",
           "args": ["--extensionDevelopmentPath=${workspaceFolder}"],
           "outFiles": ["${workspaceFolder}/out/**/*.js"],
           "preLaunchTask": "npm: watch"
         }
       ]
     }
     ```
   - Stellen Sie sicher, dass die `preLaunchTask` (falls vorhanden) mit einer Aufgabe in Ihrer `tasks.json` übereinstimmt (z.B. für die Kompilierung von TypeScript).

5. **Testen Sie Ihre Erweiterung**:
   - Im Extension Development Host-Fenster sollte Ihre Erweiterung aktiv sein. Testen Sie ihre Funktionalität (z.B. Befehle, UI-Beiträge), wie in Ihrer `package.json` und Ihrem Code definiert.
   - Verwenden Sie die **Debug-Konsole** im Haupt-VSCode-Fenster, um Protokolle oder Fehler Ihrer Erweiterung anzuzeigen.

6. **Problembehandlung**:
   - Wenn F5 nicht funktioniert:
     - Stellen Sie sicher, dass Node.js und npm installiert sind, da sie für die Erweiterungsentwicklung erforderlich sind.
     - Überprüfen Sie, ob Sie die VSCode Extension API-Abhängigkeiten installiert haben (`npm install @types/vscode`).
     - Verifizieren Sie, dass die `launch.json`-Konfiguration auf die korrekten Pfade verweist.
     - Wenn Sie Fehler sehen, überprüfen Sie den **Ausgabe**-Bereich (wählen Sie "Extension" im Dropdown-Menü) im Extension Development Host-Fenster.
   - Wenn der Extension Host nicht startet, stellen Sie sicher, dass Ihr Projekt keine Syntaxfehler in `package.json` oder Ihrer Haupt-Erweiterungsdatei aufweist.

**Zusätzliche Hinweise**:
- Sie können den Extension Development Host auch starten, indem Sie das Panel **Ausführen und Debuggen** (`Strg+Umschalt+D` oder `Befehl+Umschalt+D` auf Mac) öffnen, "Run Extension" aus dem Dropdown-Menü auswählen und dann auf die grüne Wiedergabetaste klicken.
- Um den Extension Host nach Änderungen neu zu laden, verwenden Sie `Strg+R` (Windows/Linux) oder `Befehl+R` (Mac) im Extension Development Host-Fenster oder starten Sie ihn mit F5 neu.

Weitere Details finden Sie im offiziellen VSCode-Erweiterungsentwicklungsleitfaden:  
[VS Code Extension Development](https://code.visualstudio.com/api/get-started/your-first-extension)