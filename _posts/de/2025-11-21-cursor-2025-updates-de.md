---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Cursor 2025 Funktionen und Updates
translated: true
type: note
---

### Überblick über die neuesten Funktionen von Cursor

Cursor, der auf VS Code basierende, KI-gestützte Code-Editor, hat sich 2025 rasant weiterentwickelt, mit einem Schwerpunkt auf agentenbasierten Workflows, Multi-Modell-Support und nahtlosen Integrationen. Das größte Update ist **Cursor 2.0** (veröffentlicht am 29. Oktober 2025), das Composer – ein eigenes Codierungsmodell – und eine neu gestaltete Oberfläche zur Verwaltung mehrerer KI-Agenten parallel einführt. Dies wandelt den Editor von traditionellem Codiervorgang hin zur Orchestrierung KI-gesteuerter Aufgaben, wie dem autonomen Erstellen von Features oder Debugging across Codebases. Im Folgenden werde ich die wichtigsten neuen Funktionen, gruppiert nach Veröffentlichung und Kategorie, basierend auf offiziellen Ankündigungen und Nutzerberichten bis zum 21. November 2025, aufschlüsseln.

### Wichtige Veröffentlichungen und Kernneuerungen

#### Cursor 2.0 (29. Oktober 2025) – Agentenzentrierte Überarbeitung
Diese Version stellt Cursor als "Agent Fleet Manager" neu vor und betont Delegation statt manueller Codierung. Wichtige Ergänzungen:
- **Composer Model**: Cursors erstes hauseigenes Codierungsmodell, optimiert für Geschwindigkeit und große Codebasen. Es verwendet semantische Suche für kontextbewusste Bearbeitungen und ermöglicht die Generierung/Änderung von Code mittels natürlicher Sprache. Es ist 21 % selektiver bei Vorschlägen, hat aber eine 28 % höhere Akzeptanzrate als vorherige Modelle.
- **Multi-Agent Interface**: Führen Sie bis zu 8 Agenten gleichzeitig für dieselbe Aufgabe aus (z.B. einer für die Planung, ein anderer für Tests). Beinhaltet eine "Inbox"-Seitenleiste zur Überwachung des Fortschritts, zur Überprüfung von Diffs wie bei Pull Requests und zum Starten von Agenten mit verschiedenen Modellen (z.B. Claude Sonnet 4.5 vs. GPT-5.1).
- **Integrierte Browser-Steuerung**: Agenten können nun eine eingebettete Chrome-Instanz steuern – Screenshots machen, UI-Probleme debuggen oder End-to-End-Tests durchführen. Dies ist nach der Beta-Phase allgemein verfügbar (GA), mit Enterprise-Support für sichere Nutzung.
- **Plan Mode (Erweitert)**: Agenten generieren automatisch bearbeitbare Pläne für Aufgaben, mit Tools für Codebase-Recherche und langlaufende Ausführungen. Drücken Sie Shift + Tab zum Starten; es beinhaltet klärende Fragen für bessere Ergebnisse.
- **Voice Mode**: Diktieren Sie Prompts via Sprach-zu-Text; benutzerdefinierte Sende-Keywords lösen Agentenläufe aus. Unterstützt MCP-Abfrage für strukturierte Benutzereingaben (z.B. JSON-Schemata für Präferenzen).
- **Automatische Code-Review**: Integrierte Diff-Überprüfungen für jede KI-generierte Änderung, die Bugs vor dem Merge erkennt.
- **Cloud Agents**: Führen Sie Agenten remote aus (schnellerer Start, verbesserte Zuverlässigkeit), ohne Ihren lokalen Rechner zu belasten. Verwalten Sie Flotten im Editor, ideal für Offline-Arbeit.

#### 1.7 Update (29. September 2025) – Workflow-Booster
- **Slash Commands**: Schnellaktionen wie `/summarize` für bedarfsgerechte Kontextkomprimierung (gibt Tokenlimits frei, ohne neue Chats zu starten).
- **Custom Hooks**: Automatisieren Sie Agentenverhalten, z.B. Pre-/Post-Task-Skripte für Linting oder Tests.
- **Teamweite Regeln**: Teilen Sie Codebase-Regeln (z.B. Bugbot für automatische Reviews) teamsübergreifend via `.cursorrules`-Dateien.
- **Menüleisten-Support und Deeplinks**: Einfachere Navigation und externe Integrationen.

#### Frühere Highlights 2025 (Mai–August)
- **Hintergrund-Agenten (0.50, 15. Mai)**: Parallele Aufgabenausführung (z.B. ein Agent refaktoriert, während ein anderer testet). Vorschau auf macOS/Linux.
- **Verbessertes Tab-Modell (Mehrere Updates)**: Dateiübergreifende Bearbeitungen, Kontextfenster mit 1M+ Token und Online-RL-Training für intelligentere, schnellere Autovervollständigungen (z.B. React Hooks, SQL-Abfragen).
- **@folders und Inline Edits**: Verweisen Sie in Prompts auf ganze Verzeichnisse; erneuertes CMD+K für gesamte Dateiänderungen mit präziser Suchen/Ersetzen-Funktion.
- **YOLO Mode (Agenten-Verbesserungen)**: Autonome Terminalbefehle, Linting-Korrekturen und Selbst-Debugging bis zur Lösung.

### Modell-Integrationen
Cursor unterstützt nun modernste Modelle für verschiedene Aufgaben:
- **OpenAI (13. November 2025)**: GPT-5.1 (Planung/Debugging), GPT-5.1 Codex (anspruchsvolle Codierung), GPT-5.1 Codex Mini (effiziente Bearbeitungen).
- **Anthropic**: Sonnet 4 (22. Mai 2025) und Sonnet-3.7 (24. Februar 2025) für überlegenes Codebase-Verständnis.
- **Google**: Gemini 2.5 Pro (10. Juni 2025) für schnelles Wachstum in Integrationen.
- **Andere**: o3/o4-mini (17. April 2025) für verbessertes Coding.

| Kategorie | Wichtige neue Funktion | Vorteil | Veröffentlichung |
|-----------|------------------------|---------|------------------|
| **Agenten** | Multi-Agent Parallelismus | Delegieren Sie Aufgaben an 2–8 Agenten; vergleichen Sie Ausgaben | 2.0 (Okt) |
| **Modelle** | Composer + GPT-5.1 Suite | Schnellere, kontextbewusste Generierung | 2.0/Nov |
| **UI/Workflow** | Plan Mode + Integrierter Browser | Automatische Planung + End-to-End-Tests | 2.0/Sep |
| **Bearbeitungen** | Dateiübergreifendes Tab + Inline Refresh | Intelligentere Refactors; Präzision für ganze Dateien | Mai–Okt |
| **Zusammenarbeit** | Teamregeln + Cloud Agents | Gemeinsame Richtlinien; Remote-Ausführung | Sep/Okt |

### Preise und Barrierefreiheit Updates
- **Vereinfachte Tarife (16. Juni 2025)**: Pro (20 $/Monat Compute-Basis, unbegrenzte Tool-Aufrufe); neu Ultra (200 $/Monat, 20-fache Nutzung) für Power-User.
- **Max Mode**: Token-basierter Zugriff auf volle Modellfähigkeiten (z.B. lange Kontexte) über alle Top-Modelle hinweg.

Diese Funktionen machen Cursor ideal für agentengesteuerte Entwicklung und reduzieren manuelle Arbeit um bis zu 39 % bei PR-Merges (laut einer Studie der University of Chicago). Den vollständigen Changelog finden Sie auf [Cursors offizieller Website](https://cursor.com/changelog). Wenn Sie VS Code nutzen, ist die Migration nahtlos – laden Sie es herunter und experimentieren Sie mit der Agenten-Ansicht von 2.0 für einen schnellen Erfolg.