---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Benutzerdefinierte Chat-Modi für GitHub Copilot
translated: true
type: note
---

### Was ist chatmode.md?

In der GitHub Copilot-Erweiterung für Visual Studio Code (VS Code) werden `chatmode.md`-Dateien verwendet, um **benutzerdefinierte Chat-Modi** zu definieren. Diese ermöglichen es Ihnen, den Copilot Chat so zu konfigurieren, dass er spezifische Personas oder Verhaltensweisen für Aufgaben wie Planung, Sicherheitsüberprüfungen oder Code-Implementierung annimmt. Jeder Modus kann Anweisungen, verfügbare Tools (z. B. Suche, Abrufen oder GitHub-Repo-Zugriff) und sogar das zu verwendende KI-Modell festlegen. Diese Funktion befindet sich ab VS Code 1.101 in der Vorschauphase und hilft dabei, Antworten für eine konsistente Arbeitsablauf zu optimieren.

Benutzerdefinierte Modi werden als Markdown-Dateien mit der Erweiterung `.chatmode.md` gespeichert, entweder in Ihrem Arbeitsbereich (für die Teamfreigabe) oder in Ihrem Benutzerprofil (für die persönliche Wiederverwendung).

### Warum benutzerdefinierte Chat-Modi verwenden?
- **Maßgeschneiderte Antworten**: Erzwingen Sie Richtlinien, wie das Generieren von Plänen ohne Codeänderungen.
- **Tool-Kontrolle**: Beschränken Sie Tools auf schreibgeschützt für die Planung oder aktivieren Sie die Bearbeitung für die Implementierung.
- **Effizienz**: Wiederverwenden Sie Setups für gängige Rollen (z. B. Architekt, Reviewer).

### So erstellen Sie eine chatmode.md-Datei

1.  Öffnen Sie die **Chat-Ansicht** in VS Code:
    - Klicken Sie auf das Copilot Chat-Symbol in der Titelleiste oder verwenden Sie `Strg+Alt+I` (Windows/Linux) / `Cmd+Wahltaste+I` (macOS).

2.  Klicken Sie in der Chat-Ansicht auf **Chat konfigurieren > Modi** und wählen Sie dann **Datei für neuen benutzerdefinierten Chat-Modus erstellen**. Alternativ öffnen Sie die Befehlspalette (`Umschalt+Strg+P` / `Umschalt+Cmd+P`) und führen Sie **Chat: New Mode File** aus.

3.  Wählen Sie einen Speicherort:
    - **Arbeitsbereich**: Wird standardmäßig in `.github/chatmodes/` gespeichert (für Ihr Team freigebbar). Passen Sie Ordner über die Einstellung `chat.modeFilesLocations` an.
    - **Benutzerprofil**: Wird in Ihrem Profilordner für die Synchronisierung über Geräte hinweg gespeichert.

4.  Benennen Sie die Datei (z. B. `planning.chatmode.md`) und bearbeiten Sie sie in VS Code.

Um vorhandene Modi zu verwalten, verwenden Sie **Chat konfigurieren > Modi** oder den Befehl **Chat: Configure Chat Modes**.

### Dateistruktur und Syntax

Eine `.chatmode.md`-Datei verwendet Markdown mit optionalem YAML-Frontmatter für Metadaten. Hier ist die grundlegende Struktur:

- **YAML-Frontmatter** (eingeschlossen in `---`-Zeilen, optional):
  - `description`: Kurzer Text, der im Platzhalter der Chat-Eingabe und im Dropdown-Hover angezeigt wird.
  - `tools`: Array von Tool-Namen (z. B. `['fetch', 'search']`). Verwenden Sie integrierte Tools wie `githubRepo` oder Erweiterungs-Tools; konfigurieren Sie sie über **Tools konfigurieren**.
  - `model`: KI-Modell (z. B. `"Claude Sonnet 4"`). Standardmäßig wird Ihr ausgewähltes Modell verwendet.

- **Body**: Markdown-Anweisungen für die KI, einschließlich Prompts, Richtlinien oder Links zu externen Dateien.

Tool-Priorität: Prompt-Datei > Referenzierter Modus > Tools des Standardmodus.

### Beispiel für eine chatmode.md-Datei

Dies erstellt einen "Planungs"-Modus zum Generieren von Implementierungsplänen ohne Codeänderungen:

```
---
description: Erstellen Sie einen Implementierungsplan für neue Funktionen oder die Refaktorisierung von vorhandenem Code.
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: Claude Sonnet 4
---
# Anweisungen für den Planungsmodus

Sie befinden sich im Planungsmodus. Ihre Aufgabe ist es, einen Implementierungsplan für eine neue Funktion oder für die Refaktorisierung von vorhandenem Code zu erstellen. Nehmen Sie keine Code-Änderungen vor – erstellen Sie nur einen Plan.

Der Plan besteht aus einem Markdown-Dokument mit diesen Abschnitten:

*   **Überblick**: Kurze Beschreibung der Funktion oder Refaktorisierung.
*   **Anforderungen**: Liste der Anforderungen.
*   **Implementierungsschritte**: Detaillierte Schritte zur Implementierung.
*   **Tests**: Liste von Tests zur Überprüfung.
```

Speichern Sie die Datei, und sie wird im Chat-Modus-Dropdown erscheinen.

### So verwenden Sie einen benutzerdefinierten Chat-Modus

1.  Öffnen Sie die **Chat-Ansicht** (wie oben beschrieben).

2.  Wählen Sie im Dropdown-Menü oben in der Chat-Ansicht (neben dem Modus-Auswahlfeld) Ihren benutzerdefinierten Modus aus (z. B. "Planning").

3.  Die `description` des Modus erscheint als Platzhalter im Eingabefeld. Geben Sie Ihren Prompt ein (z. B. "Planen Sie eine Benutzerauthentifizierungs-Funktion").

4.  Copilot antwortet gemäß den Anweisungen und Tools des Modus. Sie können den Modus jederzeit über das Dropdown-Menü wechseln – die integrierten Modi (Ask, Edit, Agent) bleiben verfügbar.

Weitere Beispiele finden Sie in den Community-Beiträgen im [Awesome Copilot-Repo](https://github.com/github/awesome-copilot/tree/main).

### Referenzen
- [Benutzerdefinierte Chat-Modi in VS Code](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
- [Erste Schritte mit Chat in VS Code](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)