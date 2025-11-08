---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Visual Studio Code August 2025 Update
translated: true
type: note
---

### Visual Studio Code 1.104 (August 2025)

Dieses Release konzentriert sich stark auf KI-Verbesserungen für GitHub Copilot, verbesserte Sicherheit für KI-Tools und Produktivitätssteigerungen im Editor und Terminal. Hier ist eine Übersicht der wichtigsten Aktualisierungen:

#### KI-Funktionen
- **Automatische Modellauswahl (Vorschau)**: Der Chat wählt automatisch das beste Modell (z. B. Claude Sonnet 4, GPT-5-Varianten) basierend auf Leistung und Ratenlimits aus, wenn "Auto" ausgewählt ist; beinhaltet einen 10 % Anfrage-Rabatt für zahlende Nutzer.
- **Bestätigung von Bearbeitungen an sensiblen Dateien**: Der Agent-Modus erfordert eine Benutzerbestätigung, bevor Systemdateien, Dotfiles oder etwas außerhalb des Arbeitsbereichs bearbeitet werden; anpassbar über Einstellungen.
- **Unterstützung für AGENTS.md-Dateien (Experimentell)**: Bindet automatisch die Arbeitsbereichs-`AGENTS.md` als Kontext für Chat-Anfragen ein.
- **Verbesserte Zusammenarbeit von Coding Agents (Experimentell)**: Besseres Sitzungsmanagement, GitHub-Integration und Delegierung von TODO-Kommentaren oder dem Chat.
- **Terminal Auto Approve**: Opt-in für sicherere Befehlsausführung mit Warnungen für riskante Aktionen wie `curl` oder `wget`; neue Regeln für Genehmigungen.
- **Math Rendering**: KaTeX-Gleichungen werden standardmäßig inline in Chat-Antworten gerendert.
- **Verbessertes #codebase Tool**: Verwendet ein neues Embeddings-Modell für eine schnellere, effizientere semantische Codesuche.
- **KI-Funktionen deaktivieren**: Neue Einstellung, um Copilot Chat, Completions und Vorschläge global oder pro Arbeitsbereich auszublenden und zu deaktivieren.
- **Python-spezifische KI-Tools (Experimentell/Vorschau)**: KI-gestützte Hover-Zusammenfassungen für undokumentierte Symbole und ein "Run Code Snippet"-Tool für In-Memory-Ausführung.

#### Sicherheit
- **Sicherheitsvorkehrungen für KI-Tools**: Erweiterte Bestätigungen für sensible Bearbeitungen, Terminalbefehle und globale Auto-Genehmigungen, mit Warnungen und konfigurierbaren Regeln zur Risikominderung.
- **Dokumentation**: Neue Anleitungen zu Sicherheitsüberlegungen für KI-gestützte Entwicklung.

#### Produktivität
- **Chat-Ansicht Standardeinstellungen**: Der Chat öffnet standardmäßig in der Sekundären Seitenleiste; Sichtbarkeit anpassbar.
- **Terminalverbesserungen**: Bessere IntelliSense (z. B. Git-Completions, Symbole), Sticky Scroll und Aktionen in Terminal-Editoren/Fenstern.
- **Python-Umgebungen**: Verbesserte Pipenv-Unterstützung, Einfügen von Umgebungsvariablen aus `.env`-Dateien und vollständige IntelliSense in allen Python-Dokumenten.
- **Editor-Anpassungen**: Konfigurierbare Verzögerung für Inline-Vorschläge, Tab-Index für Tastaturnavigation und Fensterrahmenfarben unter Windows.
- **GitHub Pull Requests**: Zuklappbare Seitenleiste, TODO-Aktionen für Copilot und Ignorieren-Optionen für Submodule.
- **Task- und Terminalunterstützung**: Verbessertes Input-Handling, Fehleranzeige und Timeouts für Shell-Integration.

#### Weitere bemerkenswerte Änderungen
- **Barrierefreiheit**: Fokus-Befehl für Chat-Bestätigungen zur Unterstützung von Screen Readern.
- **Sprachen**: Eingebaute Bower.json IntelliSense entfernt (veraltetes Tool; Migration zu npm/yarn).
- **Extension Authoring**: Vorgeschlagene APIs für Authentifizierungs-Herausforderungen und Beiträge zur sekundären Seitenleiste.
- **Veraltungen**: Einstellungen wie `chat.mcp.enabled` migriert; Bower-Unterstützung eingestellt.

Weitere Details finden Sie in den offiziellen Release Notes.

[August 2025 (Version 1.104)](https://code.visualstudio.com/updates/v1_104)