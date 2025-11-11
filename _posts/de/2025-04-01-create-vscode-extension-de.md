---
audio: false
generated: true
lang: de
layout: post
title: Erstellen einer VSCode-Erweiterung
translated: true
type: note
---

Die Erstellung einer Visual Studio Code (VSCode)-Erweiterung kann eine lohnende Möglichkeit sein, Ihren Entwicklungs-Workflow zu verbessern oder zur Community beizutragen. Hier ist eine umfassende Anleitung, die Ihnen den Einstieg in das Schreiben eines VSCode-Plugins erleichtert:

### 1. Voraussetzungen
- **Node.js und npm**: Stellen Sie sicher, dass Node.js und npm installiert sind. Sie können sie von [nodejs.org](https://nodejs.org/) herunterladen.
- **Yeoman und VSCode Extension Generator**: Installieren Sie Yeoman und den VSCode Extension Generator global mit npm.

```bash
npm install -g yo generator-code
```

### 2. Einrichten Ihrer Entwicklungsumgebung
- **Installieren Sie Visual Studio Code**: Stellen Sie sicher, dass VSCode installiert ist. Sie können es von [code.visualstudio.com](https://code.visualstudio.com/) herunterladen.

### 3. Eine neue Erweiterung generieren
Verwenden Sie den Yeoman-Generator, um eine neue Erweiterung zu scaffolden. Öffnen Sie ein Terminal und führen Sie aus:

```bash
yo code
```

Folgen Sie den Eingabeaufforderungen, um Ihre Erweiterung einzurichten. Sie werden gefragt nach:
- Dem Typ der Erweiterung (z. B. New Extension, New Color Theme, etc.)
- Dem Namen Ihrer Erweiterung
- Einer Identifikation (z. B. `my-extension`)
- Einer Beschreibung
- Ein Git-Repository initialisieren
- Der Sprache (TypeScript oder JavaScript)
- Den notwendigen Abhängigkeiten installieren

### 4. Verstehen der Projektstruktur
Ihre neue Erweiterung hat die folgende Struktur:
- `.vscode/`: Enthält Launch-Konfigurationen für das Debugging.
- `src/`: Enthält den Quellcode Ihrer Erweiterung.
- `package.json`: Die Manifest-Datei für Ihre Erweiterung.
- `tsconfig.json`: TypeScript-Konfigurationsdatei (falls TypeScript verwendet wird).

### 5. Schreiben Ihrer Erweiterung
- **Aktivierung**: Definieren Sie, wann Ihre Erweiterung aktiviert werden soll, in `package.json` unter dem Feld `activationEvents`.
- **Beitragspunkte**: Definieren Sie, was Ihre Erweiterung zu VSCode beiträgt, wie Befehle, Ansichten oder Sprachen, im Abschnitt `contributes` von `package.json`.

### 6. Implementieren von Befehlen
Erstellen Sie Befehle, die Benutzer aufrufen können. Definieren Sie sie in `package.json` und implementieren Sie sie in Ihrer Haupt-Erweiterungsdatei (z. B. `src/extension.ts` oder `src/extension.js`).

Beispiel eines Befehls in `package.json`:

```json
"contributes": {
    "commands": [
        {
            "command": "extension.sayHello",
            "title": "Say Hello"
        }
    ]
}
```

Implementieren Sie den Befehl in `src/extension.ts`:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.sayHello', () => {
        vscode.window.showInformationMessage('Hello, World!');
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
```

### 7. Debuggen Ihrer Erweiterung
- Drücken Sie `F5`, um ein neues VSCode-Fenster mit Ihrer geladenen Erweiterung zu öffnen.
- Setzen Sie Breakpoints und verwenden Sie die Debug-Konsole, um Ihre Erweiterung zu testen.

### 8. Verpacken und Veröffentlichen
- **Die Erweiterung verpacken**: Verwenden Sie das `vsce`-Tool, um Ihre Erweiterung zu verpacken.

```bash
npm install -g vsce
vsce package
```

- **Im Marketplace veröffentlichen**: Folgen Sie den Anweisungen auf dem [VSCode Marketplace](https://code.visualstudio.com/api/working-with-extensions/publishing-extension), um Ihre Erweiterung zu veröffentlichen.

### 9. Dokumentation und Best Practices
- **Dokumentation**: Stellen Sie eine klare Dokumentation für Ihre Erweiterung in einer `README.md`-Datei bereit.
- **Tests**: Schreiben Sie Tests, um sicherzustellen, dass Ihre Erweiterung wie erwartet funktioniert.
- **Versionierung**: Befolgen Sie semantische Versionierung für Ihre Erweiterungs-Releases.

### 10. Zusätzliche Ressourcen
- **VSCode API-Dokumentation**: [vscode-api](https://code.visualstudio.com/api)
- **Erweiterungsbeispiele**: [vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples)

Wenn Sie diese Schritte befolgen, sind Sie auf dem besten Weg, eine funktionale und nützliche VSCode-Erweiterung zu erstellen. Viel Spaß beim Programmieren!