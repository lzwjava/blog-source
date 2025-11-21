---
audio: false
generated: true
image: false
lang: de
layout: post
model: google/gemini-3-pro-preview
title: Kategorie der Code-Assistent-Tools
translated: true
type: note
---

Die typischen **Tool-Aufrufe** oder **Aktionen** in einem leistungsstarken Code-Assistenten wie Claude Code drehen sich darum, ihm die Interaktion mit einer realen Coding-Umgebung zu ermöglichen und die Aufgaben auszuführen, die ein menschlicher Entwickler erledigen würde.

Diese Tool-Aufrufe lassen sich in einige primäre Kategorien einteilen:

### 1. Dateisystem- und Codebase-Interaktion

Diese sind wesentlich, damit der Assistent das Projekt versteht, vorhandenen Code liest und Änderungen vornimmt.

| Tool/Aktion | Typischer Anwendungsfall |
| :--- | :--- |
| **`read_file`** (oder Dateireferenz wie `@dateiname`) | Abrufen des Inhalts einer bestimmten Datei, um deren Logik, Abhängigkeiten oder Kontext zu verstehen. |
| **`list_directory`** | Erhalten einer Dateistruktur oder einer Liste von Dateien in einem Verzeichnis, um relevante Module zu identifizieren oder eine bestimmte Datei zu finden. |
| **`edit_file` / `write_file`** | Die Kernaktion zum Implementieren einer Lösung, Refactoring, Hinzufügen eines Features oder Beheben eines Fehlers im Code. |
| **`create_file`** | Erstellen neuer Dateien, wie z.B. einer neuen Testdatei, Konfigurationsdatei oder einer neuen Komponente. |
| **`search_files`** | Finden aller Dateien in der Codebase, die eine bestimmte Zeichenkette enthalten (z.B. ein Funktionsname, ein Klassenname oder eine Fehlermeldung). |

### 2. Ausführung und Debugging

Um seine Arbeit zu überprüfen, Fehler zu beheben und Echtzeit-Feedback zu erhalten, muss der Assistent Befehle ausführen.

| Tool/Aktion | Typischer Anwendungsfall |
| :--- | :--- |
| **`bash` / `run_command`** | Ausführen von Shell-Befehlen wie das Ausführen eines Builds (`npm build`), Ausführen von Tests (`pytest`, `npm test`), Linting des Codes (`eslint`) oder Ausführen eines Skripts. |
| **`code_interpreter`** | Ausführen eines kleinen Code-Snippets in einer sandboxed Umgebung, um etwas schnell zu berechnen, eine Bibliotheksfunktion zu testen oder einen kleinen Datensatz zu analysieren. |

### 3. Versionskontrolle (Git)

Ein agentischer Coding-Assistent kann den Entwicklungs-Workflow durch Interaktion mit Git verwalten.

| Tool/Aktion | Typischer Anwendungsfall |
| :--- | :--- |
| **`git status`** | Überprüfen des aktuellen Zustands des Arbeitsverzeichnisses. |
| **`git diff`** | Anzeigen der vorgenommenen Änderungen, um die eigene Arbeit zu überprüfen. |
| **`git commit`** | Speichern von Änderungen im Repository, oft mit einer generierten Commit-Nachricht. |
| **`git checkout`** | Wechseln von Branches oder Verwerfen von uncommitteten Änderungen. |
| **`create_pull_request`** | Automatisieren des letzten Schritts eines Features oder einer Fehlerbehebung. |

### 4. Externe Informationen

Für aktuelle Informationen, Dokumentation oder die Verbindung zu externen Diensten werden spezielle Tools verwendet.

| Tool/Aktion | Typischer Anwendungsfall |
| :--- | :--- |
| **`web_search`** | Nachschlagen der neuesten Syntax, Lesen offizieller API-Dokumentation oder Finden von Troubleshooting-Guides für einen bestimmten Fehler. |
| **Custom APIs / MCP Server** | Verbinden mit externen Diensten unter Verwendung des Model Context Protocol (MCP), wie z.B. das Abrufen von Daten aus einem Google Drive, die Interaktion mit einer Datenbank (PostgreSQL) oder das Senden einer Nachricht an ein Kommunikationstool (Slack). |

Im Wesentlichen ermöglichen diese "Tool-Aufrufe" dem Large Language Model (LLM), sich von einem Textgenerator zu einem vollwertigen **Agenten** zu entwickeln, der seine Umgebung beobachten (Dateien lesen, Befehle ausführen), denken (die Arbeit planen) und handeln (Dateien bearbeiten, Code committen) kann.

Möchten Sie ein schrittweises Beispiel sehen, wie ein Code-Assistent diese Tools verwenden könnte, um einen einfachen Bug zu beheben?