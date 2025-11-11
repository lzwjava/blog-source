---
audio: false
generated: true
lang: de
layout: post
title: Verwenden von GitHub Copilot in Visual Studio Code
translated: true
type: note
---

GitHub Copilot ist ein KI-gesteuerter Coding-Assistent, der von GitHub und OpenAI entwickelt wurde, um die Produktivität von Entwicklern in Visual Studio Code (VS Code) zu steigern. Er bietet kontextbewusste Code-Vervollständigungen, einen Chat mit natürlicher Sprache und erweiterte Bearbeitungsfunktionen. Diese Anleitung führt Sie durch die Einrichtung von Copilot, erkundet seine Funktionen und optimiert Ihren Workflow mit Tipps und Best Practices.

## 1. Einführung in GitHub Copilot
GitHub Copilot fungiert als ein KI-Pair-Programmierer, der Echtzeit-Code-Vorschläge bietet, Coding-Fragen beantwortet und repetitive Aufgaben automatisiert. Er wird von großen Sprachmodellen angetrieben, die mit riesigen Datensätzen von öffentlichem Code trainiert wurden, was ihn in der Lage macht, zahlreiche Programmiersprachen und Frameworks zu unterstützen, einschließlich Python, JavaScript, TypeScript, Ruby, Go, C# und C++.

Zu den Hauptfunktionen gehören:
- **Code Completions**: Schlägt Code-Snippets während der Eingabe vor, von einzelnen Zeilen bis hin zu ganzen Funktionen.
- **Copilot Chat**: Ermöglicht Abfragen in natürlicher Sprache, um Code zu erklären, Snippets zu generieren oder Probleme zu debuggen.
- **Agent Mode**: Automatisiert mehrstufige Coding-Aufgaben, wie Refactoring oder das Erstellen von Apps.
- **Custom Instructions**: Passt Vorschläge an Ihren Coding-Stil oder Projektanforderungen an.

## 2. Einrichtung von GitHub Copilot in VS Code

### Voraussetzungen
- **VS Code**: Laden Sie Visual Studio Code von der [offiziellen Website](https://code.visualstudio.com/) herunter und installieren Sie es. Stellen Sie sicher, dass Sie eine kompatible Version haben (jede aktuelle Version unterstützt Copilot).
- **GitHub-Account**: Sie benötigen einen GitHub-Account mit Zugriff auf Copilot. Optionen sind:
  - **Copilot Free**: Begrenzte Completions und Chat-Interaktionen pro Monat.
  - **Copilot Pro/Pro+**: Bezahlte Pläne mit höheren Limits und erweiterten Funktionen.
  - **Organisationszugriff**: Falls von Ihrer Organisation bereitgestellt, fragen Sie Ihren Administrator nach den Zugangsdaten.
- **Internetverbindung**: Copilot benötigt eine aktive Verbindung, um Vorschläge zu liefern.

### Installationsschritte
1. **Öffnen Sie VS Code**:
   Starten Sie Visual Studio Code auf Ihrem Rechner.

2. **Installieren Sie die GitHub Copilot Extension**:
   - Gehen Sie zur **Extensions**-Ansicht (Strg+Umschalt+X oder Cmd+Umschalt+X auf macOS).
   - Suchen Sie im Extensions Marketplace nach "GitHub Copilot".
   - Klicken Sie auf **Install** für die offizielle GitHub Copilot-Erweiterung. Dadurch wird automatisch auch die Copilot Chat-Erweiterung installiert.

3. **Melden Sie sich bei GitHub an**:
   - Nach der Installation erscheint möglicherweise eine Aufforderung in der VS Code Statusleiste (unten rechts) zur Einrichtung von Copilot.
   - Klicken Sie auf das Copilot-Symbol und wählen Sie **Sign in**, um sich mit Ihrem GitHub-Account zu authentifizieren.
   - Wenn keine Aufforderung erscheint, öffnen Sie die Befehlspalette (Strg+Umschalt+P oder Cmd+Umschalt+P) und führen Sie den Befehl `GitHub Copilot: Sign in` aus.
   - Folgen Sie dem browserbasierten Authentifizierungsvorgang und kopieren Sie den von VS Code bereitgestellten Code zu GitHub.

4. **Aktivierung überprüfen**:
   - Nach dem Anmelden sollte sich das Copilot-Symbol in der Statusleiste grün färben, was einen aktiven Zustand anzeigt.
   - Wenn Sie kein Copilot-Abonnement haben, werden Sie in den Copilot Free-Plan mit begrenzter monatlicher Nutzung aufgenommen.

5. **Optional: Telemetrie deaktivieren**:
   - Standardmäßig sammelt Copilot Telemetriedaten. Um dies zu deaktivieren, gehen Sie zu **Einstellungen** (Strg+, oder Cmd+,), suchen Sie nach `telemetry.telemetryLevel` und setzen Sie es auf `off`. Alternativ können Sie Copilot-spezifische Einstellungen unter `GitHub Copilot Settings` anpassen.

> **Hinweis**: Wenn Ihre Organisation Copilot Chat deaktiviert oder Funktionen eingeschränkt hat, wenden Sie sich an Ihren Administrator. Informationen zur Problembehandlung finden Sie im [GitHub Copilot Troubleshooting Guide](https://docs.github.com/en/copilot/troubleshooting).[](https://code.visualstudio.com/docs/copilot/setup)

## 3. Kernfunktionen von GitHub Copilot in VS Code

### 3.1 Code Completions
Copilot schlägt Code während der Eingabe vor, von einzelnen Zeilen bis hin zu ganzen Funktionen oder Klassen, basierend auf dem Kontext Ihres Codes und der Dateistruktur.
- **So funktioniert es**:
  - Beginnen Sie mit der Eingabe in einer unterstützten Sprache (z.B. JavaScript, Python, C#).
  - Copilot zeigt Vorschläge in abgeblassener "Ghost-Text"-Darstellung an.
  - Drücken Sie **Tab**, um einen Vorschlag zu akzeptieren, oder tippen Sie weiter, um ihn zu ignorieren.
  - Verwenden Sie **Alt+]** (nächster) oder **Alt+[** (vorheriger), um durch mehrere Vorschläge zu blättern.
- **Beispiel**:
  ```javascript
  // Calculate factorial of a number
  function factorial(n) {
  ```
  Copilot könnte vorschlagen:
  ```javascript
  if (n === 0) return 1;
  return n * factorial(n - 1);
  }
  ```
  Drücken Sie **Tab**, um den Vorschlag zu akzeptieren.

- **Tipps**:
  - Verwenden Sie beschreibende Funktionsnamen oder Kommentare, um Copilot zu lenken (z.B. `// Sort an array in ascending order`).
  - Bei mehreren Vorschlägen: Bewegen Sie den Mauszeiger über den Vorschlag, um das Completions Panel (Strg+Eingabe) zu öffnen und alle Optionen anzuzeigen.

### 3.2 Copilot Chat
Copilot Chat ermöglicht es Ihnen, mit Copilot in natürlicher Sprache zu interagieren, um Fragen zu stellen, Code zu generieren oder Probleme zu debuggen.
- **Zugriff auf Chat**:
  - Öffnen Sie die **Chat-Ansicht** von der Aktivitätsleiste aus oder verwenden Sie **Strg+Alt+I** (Windows/Linux) oder **Cmd+Strg+I** (macOS).
  - Alternativ verwenden Sie **Inline Chat** (Strg+I oder Cmd+I) direkt im Editor für kontextspezifische Abfragen.
- **Anwendungsfälle**:
  - **Code erklären**: Wählen Sie einen Codeblock aus, öffnen Sie Inline Chat und geben Sie `explain this code` ein.
  - **Code generieren**: Geben Sie `write a Python function to reverse a string` in der Chat-Ansicht ein.
  - **Debugging**: Fügen Sie eine Fehlermeldung in den Chat ein und bitten Sie um eine Lösung.
- **Beispiel**:
  Geben Sie in der Chat-Ansicht ein:
  ```
  What is recursion?
  ```
  Copilot antwortet mit einer detaillierten Erklärung, oft inklusive Codebeispielen in Markdown.

- **Slash-Befehle**:
  Verwenden Sie Befehle wie `/explain`, `/doc`, `/fix`, `/tests` oder `/optimize`, um Aufgaben zu spezifizieren. Zum Beispiel:
  ```
  /explain this function
  ```
  mit einer ausgewählten Funktion erzeugt eine detaillierte Erklärung.

### 3.3 Agent Mode (Vorschau)
Agent Mode ermöglicht es Copilot, mehrstufige Coding-Aufgaben autonom zu bearbeiten, wie das Erstellen von Apps, Refactoring von Code oder das Schreiben von Tests.
- **Verwendung**:
  - Öffnen Sie die **Copilot Edits-Ansicht** in VS Code Insiders oder Stable (falls verfügbar).
  - Wählen Sie **Agent** aus dem Modus-Dropdown-Menü.
  - Geben Sie eine Eingabeaufforderung ein, z.B. `Create a React form component with name and email fields`.
  - Copilot analysiert Ihre Codebasis, schlägt Änderungen vor und kann Terminalbefehle oder Tests ausführen.
- **Fähigkeiten**:
  - Generiert Code über mehrere Dateien hinweg.
  - Überwacht Fehler und iteriert, um Probleme zu beheben.
  - Integriert neue Bibliotheken oder migriert Code zu modernen Frameworks.

> **Hinweis**: Agent Mode ist experimentell und funktioniert am besten in kleineren Repositories. Geben Sie Feedback über das VS Code GitHub Repo ab.[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 3.4 Custom Instructions
Passen Sie Copilot an Ihren Coding-Stil oder Projektanforderungen an.
- **Einrichtung**:
  - Erstellen Sie eine `.github/copilot-instructions.md` Datei in Ihrem Workspace.
  - Fügen Sie Anweisungen in Markdown hinzu, z.B. `Use snake_case for Python variable names`.
  - Aktivieren Sie benutzerdefinierte Anweisungen in **Einstellungen** > **GitHub** > **Copilot** > **Enable custom instructions** (VS Code 17.12 oder höher).
- **Beispiel**:
  ```markdown
  # Copilot Custom Instructions
  - Use camelCase for JavaScript variables.
  - Prefer async/await over .then() for promises.
  ```
  Copilot wird Vorschläge an diese Präferenzen anpassen.

### 3.5 Workspace Context mit @workspace
Verwenden Sie den `@workspace` Befehl, um Ihre gesamte Codebasis abzufragen.
- **Beispiel**:
  Geben Sie in der Chat-Ansicht ein:
  ```
  @workspace Where is the database connection string configured?
  ```
  Copilot durchsucht Ihren Workspace und verweist auf relevante Dateien.

### 3.6 Next Edit Suggestions (Vorschau)
Copilot sagt die nächste logische Bearbeitung basierend auf Ihren letzten Änderungen vorher und schlägt sie vor.
- **So funktioniert es**:
  - Während Sie Code bearbeiten, hebt Copilot potenzielle nächste Bearbeitungen hervor.
  - Akzeptieren Sie Vorschläge mit **Tab** oder modifizieren Sie sie über Inline Chat.
- **Anwendungsfall**: Ideal für iteratives Refactoring oder das Vervollständigen verwandter Codeänderungen.

## 4. Tipps und Tricks zur Optimierung der Copilot-Nutzung

### 4.1 Schreiben Sie effektive Prompts
- Seien Sie spezifisch: Anstatt `write a function`, versuchen Sie `write a Python function to sort a list of dictionaries by the 'age' key`.
- Geben Sie Kontext: Geben Sie Framework- oder Bibliotheksdetails an (z.B. `use React hooks`).
- Verwenden Sie Kommentare: Schreiben Sie `// Generate a REST API endpoint in Express`, um Completions zu lenken.

### 4.2 Nutzen Sie den Kontext
- **Dateien/Symbole referenzieren**: Verwenden Sie `#filename`, `#folder` oder `#symbol` in Chat-Prompts, um den Kontext einzugrenzen.
  ```
  /explain #src/utils.js
  ```
- **Drag and Drop**: Ziehen Sie Dateien oder Editor-Tabs in den Chat-Prompt, um Kontext hinzuzufügen.
- **Bilder anhängen**: In VS Code 17.14 Preview 1 oder höher können Sie Screenshots anhängen, um Probleme zu veranschaulichen (z.B. UI-Fehler).

### 4.3 Verwenden Sie Slash-Befehle
- `/doc`: Generiert Dokumentation für eine Funktion.
- `/fix`: Schlägt Fehlerbehebungen vor.
- `/tests`: Erstellt Unit-Tests für ausgewählten Code.
- Beispiel:
  ```
  /tests Generate Jest tests for this function
  ```

### 4.4 Speichern und Wiederverwenden von Prompts
- Erstellen Sie eine `.prompt.md` Datei in `.github/prompts/`, um wiederverwendbare Prompts zu speichern.
- Beispiel:
  ```markdown
  # React Component Prompt
  Generate a React functional component with Tailwind CSS styling. Ask for component name and props if not provided.
  ```
- Hängen Sie den Prompt im Chat an, um ihn über Projekte hinweg wiederzuverwenden.

### 4.5 Wählen Sie das richtige Modell
- Copilot unterstützt mehrere Sprachmodelle (z.B. GPT-4o, Claude Sonnet).
- Wählen Sie Modelle im Chat-Ansicht-Dropdown für schnelleres Coding oder tiefergehende Analysen.
- Für komplexe Aufgaben kann Claude Sonnet im Agent Mode besser abschneiden.[](https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode)

### 4.6 Indizieren Sie Ihren Workspace
- Aktivieren Sie die Workspace-Indizierung für schnellere und genauere Codesuchen.
- Verwenden Sie einen Remote-Index für GitHub-Repositories oder einen lokalen Index für große Codebasen.

## 5. Best Practices
- **Überprüfen Sie Vorschläge**: Verifizieren Sie Copilots Vorschläge immer auf Genauigkeit und Übereinstimmung mit den Standards Ihres Projekts.
- **Kombinieren Sie mit IntelliCode**: In Visual Studio ergänzt Copilot IntelliCode für erweiterte Completions.[](https://devblogs.microsoft.com/visualstudio/github-copilot-in-visual-studio-2022/)
- **Prüfen Sie die Sicherheit**: Copilot könnte Code mit Sicherheitslücken vorschlagen. Überprüfen Sie Vorschläge, besonders in sensiblen Projekten, und halten Sie sich an die Richtlinien Ihrer Organisation.[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **Verwenden Sie aussagekräftige Namen**: Beschreibende Variablen- und Funktionsnamen verbessern die Qualität der Vorschläge.
- **Iterieren Sie mit Chat**: Verfeinern Sie Prompts, wenn die ersten Vorschläge nicht treffend sind.
- **Überwachen Sie Nutzungslimits**: Verfolgen Sie mit Copilot Free Ihre monatlichen Completions und Chat-Interaktionen über die GitHub-Kontoeinstellungen oder das Copilot-Abzeichen in VS Code.[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)

## 6. Behandlung häufiger Probleme
- **Copilot inaktiv**: Stellen Sie sicher, dass Sie mit einem GitHub-Account angemeldet sind, der Copilot-Zugriff hat. Aktualisieren Sie die Anmeldedaten über das Copilot-Statusleisten-Dropdown.
- **Keine Vorschläge**: Überprüfen Sie Ihre Internetverbindung oder wechseln Sie zu einer unterstützten Sprache. Passen Sie die Einstellungen unter **Tools** > **Options** > **GitHub Copilot** an.
- **Eingeschränkte Funktionalität**: Wenn Sie das Copilot Free-Nutzungslimit erreichen, wechseln Sie zurück zu IntelliCode-Vorschlägen. Upgraden Sie auf einen bezahlten Plan oder überprüfen Sie Ihren Status.[](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-free-plan?view=vs-2022)
- **Netzwerkprobleme**: Siehe [GitHub Copilot Troubleshooting Guide](https://docs.github.com/en/copilot/troubleshooting).

## 7. Erweiterte Anwendungsfälle
- **Datenbankabfragen**: Bitten Sie Copilot, SQL-Abfragen zu generieren (z.B. `Write a SQL query to join two tables`).
- **API-Entwicklung**: Fordern Sie Code für API-Endpunkte an (z.B. `Create a Flask route to handle POST requests`).
- **Unit-Testing**: Verwenden Sie `/tests`, um Tests für Frameworks wie Jest oder Pytest zu generieren.
- **Refactoring**: Verwenden Sie Agent Mode, um Code über Dateien hinweg zu refaktorisieren (z.B. `Migrate this jQuery code to React`).

## 8. Datenschutz- und Sicherheitsüberlegungen
- **Datennutzung**: Copilot überträgt Code-Snippets in Echtzeit an GitHub-Server, um Vorschläge zu generieren, behält sie aber nicht (Copilot for Business verwirft Snippets sofort).[](https://medium.com/%40codebob75/how-to-use-copilot-in-visual-studio-a-step-by-step-guide-b2a5db3b54ba)
- **Abgleich mit öffentlichem Code**: Copilot könnte Code vorschlagen, der mit öffentlichen GitHub-Repositories übereinstimmt. Aktivieren Sie code referencing, um Lizenzdetails einzusehen.[](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-extension?view=vs-2022)
- **Organisatorische Richtlinien**: Prüfen Sie, ob Ihre Organisation die Nutzung von Copilot erlaubt, da einige Chat deaktivieren oder Vorschläge einschränken.[](https://docs.github.com/en/copilot/quickstart)
- **Telemetrie**: Deaktivieren Sie Telemetrie in den VS Code-Einstellungen, falls gewünscht.[](https://code.visualstudio.com/docs/copilot/setup)

## 9. Ressourcen für weiterführendes Lernen
- [GitHub Copilot Dokumentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Schnellstart](https://code.visualstudio.com/docs/copilot/copilot-quickstart)
- [Copilot Chat Tutorial](https://code.visualstudio.com/docs/copilot/copilot-chat)
- [VS Code Copilot Serie auf YouTube](https://www.youtube.com/playlist?list=PLj6YeMhvp2S6X0vF4TrRkpZ7GIqM3oPWp)
- [GitHub Copilot FAQs](https://docs.github.com/en/copilot/faq)

## 10. Fazit
GitHub Copilot in VS Code ist ein leistungsstarkes Tool, das das Codieren durch intelligente Vorschläge, das Beantworten von Fragen und das Automatisieren komplexer Aufgaben optimiert. Durch korrekte Einrichtung, Nutzung seiner Funktionen und Befolgung von Best Practices können Sie Ihre Produktivität erheblich steigern und sich auf kreative Coding-Aufgaben konzentrieren. Experimentieren Sie mit den Fähigkeiten von Copilot, passen Sie es Ihrem Workflow an und achten Sie auf Sicherheit und Nutzungslimits, um das Beste aus diesem KI-Pair-Programmierer herauszuholen.