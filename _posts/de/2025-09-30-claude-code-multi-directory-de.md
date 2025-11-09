---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Claude Code Mehrfachverzeichnisunterstützung
translated: true
type: note
---

Claude Code, Anthropics KI-gestützter Coding-Assistent, arbeitet primär aus Sicherheits- und Fokussierungsgründen innerhalb seines initialisierten Arbeitsverzeichnisses, unterstützt nun jedoch vollständig funktionsübergreifende Projekte durch eine in kürzlichen Updates eingeführte Multi-Verzeichnis-Funktion (z.B. Version 1.0.18 und höher). Dies ermöglicht es einer einzelnen Sitzung, auf Dateien mehrerer unabhängiger Projekte oder Verzeichnisse außerhalb des ursprünglichen zuzugreifen und mit diesen zu arbeiten. Dadurch werden Aufgaben wie das Referenzieren gemeinsamer Konfigurationen, die Integration von Frontend-/Backend-Code oder die Handhabung von Monorepo-Setups ohne Kontextwechsel möglich.[1][2][3]

### So funktioniert die projektübergreifende Funktionalität
- **Kernmechanismus**: Claude Code startet in einem Stammverzeichnis (Ihr "primäres" Projekt), kann jedoch Berechtigungen zum Lesen, Bearbeiten und Ausführen von Befehlen in zusätzlichen Verzeichnissen erweitern. Dies geschieht über das `--add-dir`-Flag oder den interaktiven `/add-dir`-Befehl während einer Sitzung. Hinzugefügte Verzeichnisse werden als Erweiterungen des Arbeitsbereichs behandelt, was nahtlose Dateioperationen ermöglicht (z.B. können Sie Dateien aus Projekt A linten, während Sie in Projekt B arbeiten).[3][4]
- **Sitzungsumfang**: Jede Projekt-Hinzufügung ist temporär, sofern sie nicht über eine Konfiguration persistent gespeichert wird. Git Worktrees können gleichzeitige Sitzungen an Teilen eines Projekts für eine tiefere Zusammenarbeit ermöglichen.[5][6]
- **Einschränkungen**: Claude Code beschränkt den Dateizugriff auf hinzugefügte Verzeichnisse – es werden nicht automatisch unabhängige Pfade erkannt. Für persistente Multi-Projekt-Setups (z.B. Monorepos) sollte Claude Code aus einem übergeordneten Verzeichnis gestartet werden, das die Unterordner enthält.[3][7]
- **Anwendungsfälle**:
  - **Monorepos**: Fügen Sie Unterverzeichnisse für Frontend/Backend-Aufteilungen hinzu.[3][5][7][8]
  - **Gemeinsame Ressourcen**: Verweisen Sie auf Konfigurationen oder Bibliotheken aus einem separaten Projekt.[3][6]
  - **Projektübergreifende Zusammenarbeit**: Integrieren Sie Code aus Bibliotheken oder Tools in verschiedenen Repositories.[1][3]

### So weisen Sie Claude Code an, ein anderes Projekt einzubeziehen
Um ein Projekt außerhalb des aktuellen Verzeichnisses hinzuzufügen (z.B. `${another_project_path}`):

1. **Starten Sie Claude Code** in Ihrem primären Projektverzeichnis (z.B. `cd /pfad/zum/primären/projekt && claude`).
2. **Fügen Sie das zusätzliche Verzeichnis interaktiv hinzu**:
   - Geben Sie während der Sitzung `/add-dir /vollständiger/pfad/zu/anderem/projekt` oder einen relativen Pfad (z.B. `../anderes-projekt`) ein.
   - Claude Code bestätigt den Zugriff – antworten Sie mit "ja", wenn Sie dazu aufgefordert werden.[2][3][4]
3. **Beim Start über die CLI (für sofortiges Multi-Verzeichnis-Setup)**:
   - Führen Sie aus: `claude --add-dir /pfad/zu/anderem/projekt` (mehrere mit wiederholten Flags hinzufügen).[4][5][7]
4. **Weisen Sie Claude Bots/Agents an**: Sobald hinzugefügt, geben Sie natürliche Sprachaufforderungen wie "Referenzieren Sie die API-Dateien aus dem hinzugefügten Verzeichnis in `/pfad/zu/anderem/projekt`" oder "Integrieren Sie diese gemeinsame Konfiguration aus Projekt B." Claudes agentenbasierte Architektur versteht diese Anfragen innerhalb des erweiterten Kontexts.[3][5][6]

### Best Practices und Tipps
- **Pfadangabe**: Verwenden Sie absolute Pfade für Klarheit über verschiedene Umgebungen hinweg. Vermeiden Sie das Hinzufügen zu vieler Verzeichnisse, um Leistungseinbußen zu verhindern.[3][7]
- **Arbeitsbereichseinrichtung**: Für Teams sollten Konfigurationsdateien für wiederverwendbare Setups in Betracht gezogen werden. Kombinieren Sie dies mit Tools wie Apidog für API-Tests über Verzeichnisse hinweg.[3][8]
- **Fehlerbehebung**: Wenn die Pfadauflösung fehlschlägt, stellen Sie Schreibberechtigungen sicher. Starten Sie Sitzungen für Änderungen neu. Bei anhaltenden Problemen, überprüfen Sie die Protokolle oder führen Sie Claude Code aus einem übergeordneten Verzeichnis heraus.[3][7]
- **Team-Workflows**: Nutzen Sie diese Funktion für Microservices oder gemeinsame Bibliotheken; synchronisieren Sie diese via Git für die Versionierung.[5][6][8]

Diese Funktion transformiert Workflows für komplexe Setups und reduziert die Reibung im Vergleich zum Führen separater Sitzungen in jedem Verzeichnis.[3][6] Wenn Sie auf Probleme stoßen oder Beispiele für bestimmte Tools benötigen, geben Sie bitte weitere Details an!

Zitate:
[1] https://www.reddit.com/r/ClaudeAI/comments/1l896ek/claude_code_v1018_we_can_now_specify_additional/
[2] https://www.threads.com/@boris_cherny/post/DMtFLWOzKAS/video-claude-code-can-now-work-across-multiple-directories-in-a-single-sessiontype-add?hl=en
[3] https://apidog.com/blog/claude-code-multi-directory-support/
[4] https://claudelog.com/faqs/--add-dir/
[5] https://www.anthropic.com/engineering/claude-code-best-practices
[6] https://www.linkedin.com/posts/valokafor_how-to-set-up-claude-code-the-right-way-for-activity-7353146981034201089-dhdX
[7] https://stackoverflow.com/questions/79763754/best-practices-for-multi-project-workspaces-in-claude-code
[8] https://www.siddharthbharath.com/claude-code-the-complete-guide/