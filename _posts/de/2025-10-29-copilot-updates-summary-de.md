---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Zusammenfassung der GitHub Copilot-Erweiterungsupdates
translated: true
type: note
---

### GitHub Copilot-Erweiterung für VS Code (Version 1.388.0)

Version 1.388.0 der GitHub Copilot-Erweiterung wurde am 24. Oktober 2025 veröffentlicht. Dies scheint ein kleines Update zu sein, das sich auf Stabilitäts- und Kompatibilitätsverbesserungen konzentriert, insbesondere mit der neuesten VS Code-Version (1.105). Spezifische Versionshinweise sind im Marketplace oder im GitHub-Blog nicht öffentlich detailliert, aber Benutzerberichte deuten auf Korrekturen für Probleme wie unerwünschte Code-Einfügungen während der Inline-Generierung und zusätzliche Tag-Vervollständigungen beim Abbrechen von Vorschlägen hin. Es integriert sich nahtlos in die neuesten Copilot-Funktionen, einschließlich erweiterter Agent-Modi und Modellauswahlen.

#### Wichtige Updates der letzten 6 Monate (Mai–Oktober 2025)
Die wichtigsten Verbesserungen für GitHub Copilot werden in der Regel zusammen mit den monatlichen VS Code-Veröffentlichungen angekündigt. Hier ist eine Zusammenfassung der bedeutenden Updates für die Erweiterung und verwandte Funktionen in diesem Zeitraum:

-   **Oktober 2025 (VS Code 1.105 / Erweiterung ~1.388)**:
    -   OpenAI Codex-Integration jetzt in VS Code Insiders für Copilot Pro+-Abonnenten verfügbar, ermöglicht erweiterte Codesynthese direkt im Editor.
    -   Neue "Mission Control"-Oberfläche zum Zuweisen, Steuern und Verfolgen von Copilot-Coding-Agent-Aufgaben über Sitzungen hinweg.
    -   Agent Sessions-Ansicht erweitert, um die GitHub Copilot CLI für die Verwaltung lokaler und cloudbasierter Agents zu unterstützen.

-   **September 2025 (VS Code 1.104 / Erweiterung ~1.38x)**:
    -   Rollout des experimentellen GitHub Copilot-SWE-Modells für VS Code Insiders, optimiert für Code-Bearbeitung, Refactoring und kleine Transformationen. Es ist aufgabenorientiert und funktioniert in jedem Chat-Modus; detaillierte Prompts werden für die besten Ergebnisse empfohlen.
    -   Verbesserter Inline-Chat für Terminalfehler, mit besseren Erklärungen und Korrekturen.

-   **August 2025 (VS Code 1.103 / Erweiterung ~1.37x)**:
    -   Verbesserte Commit-Nachrichten-Vorschläge mit Mehrzeilen-Kontextbewusstsein und Integration mit @workspace für die Generierung gesamter Projektstrukturen.
    -   Leichtgewichtige Inline-Chat-Upgrades für schnellere Interaktionen ohne Öffnen vollständiger Ansichten.

-   **Juli 2025 (VS Code 1.102 / Erweiterung ~1.36x)**:
    -   Bessere Koordination von Multi-File-Bearbeitungen über einzelne Prompts, analysiert die Projektstruktur für konsistente Änderungen.
    -   Veraltete ältere Modelle (ausgewählte Claude-, OpenAI- und Gemini-Varianten) zugunsten neuerer, schnellerer Optionen wie GPT-4.1 eingestellt.

-   **Juni 2025 (VS Code 1.101 / Erweiterung ~1.35x)**:
    -   Einführung von Prompt- und Anweisungsdateien zur Anpassung des Copilot-Verhaltens mit wiederverwendbaren Richtlinien und Organisationswissen.
    -   Erweiterte GitHub Pull Requests-Integration: Weisen Sie PRs/Issues Copilot direkt aus den VS Code-Ansichten zu, mit neuer "Copilot on My Behalf"-Abfrage zur Verfolgung.

-   **Mai 2025 (VS Code 1.100 / Erweiterung ~1.34x)**:
    -   Model Context Protocol (MCP)-Unterstützung für den Agent-Modus hinzugefügt, ermöglicht benutzerdefinierte API-Schlüssel für Drittanbietermodelle.
    -   Schnellere Agent-Bearbeitungen, unterstützt durch OpenAI GPT-4.1 und Anthropic Claude Sonnet, insbesondere für große Dateien.
    -   Verbesserungen bei der Repository-Suche für semantische Code-Entdeckung und codebasenweite Vorschläge.

Diese Updates betonen agentenbasierte Workflows, Modellleistung und nahtlose Integration in das VS Code-Ökosystem. Für die vollständige Erweiterungshistorie besuchen Sie den VS Code Marketplace. Wichtige Ankündigungen sind oft an die monatlichen Zyklen von VS Code gebunden.

[GitHub Copilot in VS Code wird upgegradet](https://github.blog/changelog/2025-10-28-github-copilot-in-visual-studio-code-gets-upgraded/)  
[Copilot-SWE-Modell rollt für Visual Studio Code Insiders aus](https://github.blog/changelog/2025-09-22-copilot-swe-model-rolling-out-to-visual-studio-code-insiders/)  
[GitHub Copilot in VS Code April Release (v1.100)](https://github.blog/changelog/2025-05-08-github-copilot-in-vs-code-april-release-v1-100/)  
[GitHub Copilot in VS Code März Release (v1.99)](https://github.blog/changelog/2025-04-03-github-copilot-in-vs-code-march-release-v1-99/)  
[September 2025 (Version 1.105) - Visual Studio Code](https://code.visualstudio.com/updates)  
[GitHub Copilot Marketplace-Seite](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)