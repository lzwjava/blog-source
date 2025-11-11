---
audio: false
generated: true
lang: de
layout: post
title: Wie man GitHub Copilot aus einer VSCode-Erweiterung aufruft
translated: true
type: note
---

GitHub Copilot ist ein leistungsstarker, KI-gestützter Coding-Assistent, der über entsprechende Plugins in Visual Studio Code (VSCode) und IntelliJ IDEA integriert ist. Während es keine öffentliche REST-API für den direkten Aufruf von Copilot gibt, können Entwickler programmgesteuert innerhalb einer VSCode-Erweiterung über die VSCode Chat API, die Language Model API oder befehlsbasierte Interaktionen auf seine Fähigkeiten zugreifen. Dieser Blogbeitrag führt durch die Erstellung einer VSCode-Erweiterung, die die Chat-Funktionalität von Copilot mit einer benutzerdefinierten Eingabeaufforderung auslöst, effektiv einen "API-Aufruf" an Copilot simuliert, und erklärt, wie man Copilot selbst zur Beschleunigung der Entwicklung nutzen kann.

## Verständnis der Copilot-Integration in VSCode

GitHub Copilot bietet keine traditionelle API (z.B. REST-Endpunkte) für den direkten programmgesteuerten Zugriff. Stattdessen ist seine Funktionalität verfügbar über:
- **VSCode Chat API**: Ermöglicht Erweiterungen, benutzerdefinierte Chat-Teilnehmer zu erstellen, die mit dem Chat-System von Copilot für natürliche Sprachabfragen interagieren.
- **VSCode Language Model API**: Ermöglicht Erweiterungen den Zugriff auf die Large Language Models (LLMs) von Copilot für Aufgaben wie Code-Generierung oder -Analyse.
- **VSCode-Befehle**: Erlaubt das Auslösen integrierter Funktionen von Copilot, wie das Öffnen des Chat-Fensters mit einer vordefinierten Eingabeaufforderung.

Dieser Leitfaden konzentriert sich auf die Verwendung des Befehls `workbench.action.chat.open`, um die Chat-Oberfläche von Copilot auszulösen, da dies der einfachste Weg ist, Copilots Fähigkeiten in eine Erweiterung zu integrieren.

## Schritt-für-Schritt: Erstellen einer VSCode-Erweiterung zum Auslösen des Copilot-Chats

Im Folgenden finden Sie eine Schritt-für-Schritt-Anleitung zur Erstellung einer VSCode-Erweiterung, die das Copilot-Chat-Fenster mit einer benutzerdefinierten Eingabeaufforderung öffnet und Copilot so effektiv "aufruft", um eine benutzerdefinierte Abfrage zu verarbeiten.

### 1. Richten Sie die VSCode-Erweiterung ein

1. **Projektgerüst erstellen**:
   - Installieren Sie den Yeoman VSCode-Erweiterungs-Generator: `npm install -g yo generator-code`.
   - Führen Sie `yo code` aus und wählen Sie "New Extension (TypeScript)", um eine TypeScript-basierte Erweiterung zu erstellen.
   - Benennen Sie die Erweiterung, z.B. `copilot-api-caller`.

2. **`package.json` konfigurieren**:
   - Definieren Sie einen Befehl, um den Copilot-Chat auszulösen.
   - Beispiel `package.json`:

```json
{
  "name": "copilot-api-caller",
  "displayName": "Copilot API Caller",
  "description": "Triggers GitHub Copilot Chat with a custom prompt",
  "version": "0.0.1",
  "engines": {
    "vscode": "^1.85.0"
  },
  "categories": ["Other"],
  "activationEvents": [
    "onCommand:copilot-api-caller.triggerCopilotChat"
  ],
  "main": "./out/extension.js",
  "contributes": {
    "commands": [
      {
        "command": "copilot-api-caller.triggerCopilotChat",
        "title": "Trigger Copilot Chat"
      }
    ]
  },
  "scripts": {
    "vscode:prepublish": "npm run compile",
    "compile": "tsc -p ./",
    "watch": "tsc -watch -p ./"
  },
  "devDependencies": {
    "@types/vscode": "^1.85.0",
    "@types/node": "^20.2.5",
    "typescript": "^5.1.3"
  }
}
```

   - **Verwendung von Copilot**: Während der Bearbeitung von `package.json` schlägt Copilot möglicherweise Felder wie `contributes.commands` oder `activationEvents` vor, während Sie tippen. Nehmen Sie diese mit `Tab` an, um die Einrichtung zu beschleunigen.

### 2. Schreiben des Erweiterungscodes

Erstellen Sie die Erweiterungslogik, um einen Befehl zu registrieren, der den Copilot-Chat mit einer vom Benutzer bereitgestellten Eingabeaufforderung öffnet.

- **Datei**: `src/extension.ts`
- **Code**:

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Register the command to trigger Copilot Chat
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Get user input for the prompt
    const prompt = await vscode.window.showInputBox({
      prompt: 'Enter your query for GitHub Copilot',
      placeHolder: 'e.g., Write a JavaScript function to sort an array'
    });

    if (prompt) {
      try {
        // Execute the command to open Copilot Chat with the prompt
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Sent prompt to Copilot Chat!');
      } catch (error) {
        vscode.window.showErrorMessage(`Failed to trigger Copilot Chat: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **Funktionsweise**:
  - Registriert einen Befehl `copilot-api-caller.triggerCopilotChat`.
  - Fordert den Benutzer zu einer Abfrage auf (z.B. "Write a Python function to reverse a string").
  - Verwendet `vscode.commands.executeCommand('workbench.action.chat.open', prompt)`, um das Copilot-Chat-Fenster mit der Eingabeaufforderung zu öffnen.
- **Verwendung von Copilot**: Geben Sie in VSCode `import * as vscode` ein und Copilot schlägt den vollständigen Import vor. Fügen Sie einen Kommentar wie `// Register a command to open Copilot Chat` hinzu, und Copilot könnte die `vscode.commands.registerCommand`-Struktur vorschlagen. Für die Befehlsausführung geben Sie `// Open Copilot Chat with a prompt` ein, und Copilot könnte den `executeCommand`-Aufruf vorschlagen.

### 3. Erweiterung um Kontext (Optional)

Um die Erweiterung leistungsfähiger zu machen, beziehen Sie Kontext aus dem Editor mit ein, wie z.B. ausgewählten Code, um Copilot mit zusätzlichen Informationen zu versorgen.

- **Modifizierter Code** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  let disposable = vscode.commands.registerCommand('copilot-api-caller.triggerCopilotChat', async () => {
    // Get selected text from the active editor
    const editor = vscode.window.activeTextEditor;
    let context = '';
    if (editor) {
      const selection = editor.selection;
      context = editor.document.getText(selection);
    }

    // Prompt for user input
    const prompt = await vscode.window.showInputBox({
      prompt: 'Enter your query for GitHub Copilot',
      placeHolder: 'e.g., Explain this code',
      value: context ? `Regarding this code: \n\`\`\`\n${context}\n\`\`\`\n` : ''
    });

    if (prompt) {
      try {
        await vscode.commands.executeCommand('workbench.action.chat.open', prompt);
        vscode.window.showInformationMessage('Sent prompt to Copilot Chat!');
      } catch (error) {
        vscode.window.showErrorMessage(`Failed to trigger Copilot Chat: ${error}`);
      }
    }
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
```

- **Funktionsweise**:
  - Ruft den ausgewählten Text aus dem aktiven Editor ab und fügt ihn als Kontext in die Eingabeaufforderung ein.
  - Füllt das Eingabefeld vorab mit dem ausgewählten Code, formatiert als Markdown-Codeblock.
  - Sendet die kombinierte Eingabeaufforderung an die Copilot-Chat-Oberfläche.
- **Verwendung von Copilot**: Kommentieren Sie `// Get selected text from editor`, und Copilot könnte `vscode.window.activeTextEditor` vorschlagen. Für die Formatierung geben Sie `// Format code as markdown` ein, und Copilot könnte die Triple-Backtick-Syntax vorschlagen.

### 4. Testen der Erweiterung

1. Drücken Sie `F5` in VSCode, um den Extension Development Host zu starten.
2. Öffnen Sie die Befehlspalette (`Ctrl+Shift+P` oder `Cmd+Shift+P`) und führen Sie `Trigger Copilot Chat` aus.
3. Geben Sie eine Eingabeaufforderung ein (z.B. "Generate a REST API client in TypeScript") oder wählen Sie Code aus und führen Sie den Befehl aus.
4. Verifizieren Sie, dass sich das Copilot-Chat-Fenster mit Ihrer Eingabeaufforderung öffnet und eine Antwort liefert.
5. **Verwendung von Copilot**: Treten Fehler auf, fügen Sie einen Kommentar wie `// Handle errors for command execution` hinzu, und Copilot könnte Try-Catch-Blöcke oder Fehlermeldungen vorschlagen.

### 5. Erweitert: Verwendung der VSCode Chat API

Für mehr Kontrolle verwenden Sie die VSCode Chat API, um einen benutzerdefinierten Chat-Teilnehmer zu erstellen, der sich in Copilots Sprachmodelle integriert und die Verarbeitung natürlicher Sprache innerhalb Ihrer Erweiterung ermöglicht.

- **Beispielcode** (`src/extension.ts`):

```typescript
import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
  // Register a chat participant
  const participant = vscode.chat.createChatParticipant('copilot-api-caller.myParticipant', async (request, context, stream, token) => {
    stream.markdown('Processing your query...\n');
    // Use the Language Model API to generate a response
    const model = await vscode.lm.selectChatModels({ family: 'gpt-4' })[0];
    if (model) {
      const response = await model.sendRequest([{ text: request.prompt }], {}, token);
      for await (const chunk of response.stream) {
        stream.markdown(chunk);
      }
    } else {
      stream.markdown('No suitable model available.');
    }
  });

  participant.iconPath = new vscode.ThemeIcon('sparkle');
  context.subscriptions.push(participant);
}

export function deactivate() {}
```

- **Funktionsweise**:
  - Erstellt einen Chat-Teilnehmer (`@copilot-api-caller.myParticipant`), der in der Copilot-Chat-Ansicht aufrufbar ist.
  - Verwendet die Language Model API, um auf Copilots `gpt-4`-Modell (oder ein anderes verfügbares Modell) zuzugreifen, um die Eingabeaufforderung zu verarbeiten.
  - Streamt die Antwort zurück in die Chat-Ansicht.
- **Verwendung von Copilot**: Kommentieren Sie `// Create a chat participant for Copilot`, und Copilot könnte die `vscode.chat.createChatParticipant`-Struktur vorschlagen. Für die Language Model API kommentieren Sie `// Access Copilot’s LLM`, und Copilot könnte `vscode.lm.selectChatModels` vorschlagen.

### 6. Paketieren und Bereitstellen

1. Installieren Sie `vsce`: `npm install -g @vscode/vsce`.
2. Führen Sie `vsce package` aus, um eine `.vsix`-Datei zu erstellen.
3. Installieren Sie die Erweiterung in VSCode über die Erweiterungsansicht oder teilen Sie die `.vsix`-Datei mit anderen.
4. **Verwendung von Copilot**: Fügen Sie einen Kommentar wie `// Add script to package extension` in `package.json` hinzu, und Copilot könnte das `vscode:prepublish`-Skript vorschlagen.

## Nutzung von Copilot während der Entwicklung

GitHub Copilot kann die Entwicklung von Erweiterungen erheblich beschleunigen:
- **Code-Vorschläge**: Während Sie in `src/extension.ts` tippen, schlägt Copilot Importe, Befehlsregistrierungen und Fehlerbehandlung vor. Zum Beispiel löst die Eingabe von `vscode.commands.` Vorschläge wie `registerCommand` aus.
- **Prompt Engineering**: Verwenden Sie klare Kommentare wie `// Trigger Copilot Chat with a user prompt`, um die Vorschläge von Copilot zu steuern. Verfeinern Sie Kommentare, wenn Vorschläge ungenau sind.
- **Debugging**: Schlägt die Erweiterung fehl, fügen Sie Kommentare wie `// Log error details` hinzu, und Copilot könnte `console.log` oder `vscode.window.showErrorMessage` vorschlagen.

## Einschränkungen

- **Kein direkter API-Zugriff**: Copilot bietet keine öffentliche REST-API. Die VSCode Chat und Language Model APIs sind die primären programmatischen Schnittstellen.
- **Authentifizierung**: Benutzer müssen ein aktives Copilot-Abonnement (kostenlos oder kostenpflichtig) haben und in VSCode mit einem GitHub-Konto angemeldet sein.
- **Chat-API-Umfang**: Die Chat-API ist auf die Chat-Oberfläche beschränkt; direkter Zugriff auf Copilots Code-Vervollständigungs-Engine ist programmatisch nicht verfügbar.
- **Umgebung**: Stellen Sie sicher, dass die Erweiterung mit den organisatorischen Richtlinien bezüglich benutzerdefinierter VSCode-Erweiterungen konform ist.

## Fazit

Durch die Verwendung des VSCode-Befehlssystems oder der Chat-API können Entwickler GitHub Copilot effektiv aus einer benutzerdefinierten Erweiterung "aufrufen", was eine programmgesteuerte Interaktion mit seinen KI-Fähigkeiten ermöglicht. Das obige Beispiel demonstriert das Auslösen des Copilot-Chats mit einer benutzerdefinierten Eingabeaufforderung, erweitert um Editor-Kontext, und bietet eine Grundlage für erweiterte Integrationen unter Verwendung der Language Model API. Mit Copilots Unterstützung während der Entwicklung wird die Erstellung solcher Erweiterungen schneller und intuitiver.

Für weitere Erkundungen können Sie Experimente mit der Chat-API für benutzerdefinierte Teilnehmer in Betracht ziehen oder die Integration zusätzlicher Editor-Kontexte für reichhaltigere Eingabeaufforderungen. Happy Coding!