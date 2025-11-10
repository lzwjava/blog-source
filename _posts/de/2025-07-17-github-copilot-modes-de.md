---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: GitHub Copilot Modi im Vergleich
translated: true
type: note
---

### Übersicht
GitHub Copilot bietet mehrere Modi für Code-Unterstützung in IDEs wie VS Code und Visual Studio, darunter den Edit-Modus (der Ihrer Beschreibung des "Fix-Modus" entspricht, um bestimmte Zeilen oder Funktionen auszuwählen und zu reparieren) und den Agent-Modus (der umfassendere, autonome Änderungen über ganze Dateien oder Projekte hinweg vornimmt). Der Edit-Modus ist präzise und benutergesteuert, ideal für gezielte Korrekturen, während der Agent-Modus wie ein KI-Pair-Programmierer agiert, der komplexe Aufgaben durchdenkt und Änderungen über mehrere Dateien hinweg vornimmt, ohne ständige Eingabe zu benötigen.[1][1] Beide Modi steigern die Produktivität, unterscheiden sich jedoch in Umfang, Autonomie und Workflow.

### Wichtige Unterschiede
Der Edit-Modus konzentriert sich auf vom Benutzer ausgewählte Code-Snippets und liefert Vorschläge zur Überprüfung und Genehmigung, bevor Änderungen übernommen werden. Im Gegensatz dazu arbeitet der Agent-Modus auf einer höheren Ebene, analysiert den vollständigen Codebase-Kontext, um Änderungen autonom zu planen, auszuführen und zu iterieren, und modifiziert oft ganze Dateien oder verwandte Komponenten, um Konsistenz zu wahren.[2][1] Hier ein direkter Vergleich:

| Merkmal                  | Edit-Modus (Fix-Modus)                                                                 | Agent-Modus                                                                 |
|--------------------------|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Umfang**                | Beschränkt auf ausgewählte Zeilen, Funktionen oder eine einzelne Datei. Sie markieren Code, um Fehler zu beheben, zu refaktorisieren oder spezifische Teile zu verbessern.[1] | Ganzer Workspace oder Projekt. Er identifiziert und bearbeitet automatisch verwandte Dateien, die über Ihre Auswahl hinausgehen.[2][3] |
| **Benutzerkontrolle**         | Hoch: Schlägt Änderungen zu Ihrer Überprüfung und expliziten Genehmigung vor. Sie definieren genau, was bearbeitet werden soll.[4] | Mittel: Wendet Änderungen automatisch an, kennzeichnet aber riskante Befehle (z.B. Terminal-Ausführungen) zur Überprüfung. Sie setzen das Ziel über natürliche Sprachbefehle.[1][1] |
| **Autonomie**             | Niedrig: Liefert gezielte Vorschläge; denkt nicht dateiübergreifend oder führt unabhängige Aktionen aus.[1] | Hoch: Denkt schrittweise, führt Tests/Befehle aus, erkennt Fehler und korrigiert sich selbst. Behält den Kontext über Sitzungen hinweg bei.[2][3] |
| **Antwortzeit**        | Schnell: Schnelle Analyse nur der Auswahl.[2] | Langsamer: Analysiert den vollständigen Projektkontext, was bei großen Codebasen länger dauern kann.[2] |
| **Am besten geeignet für**             | Schnelle Korrekturen wie das Debuggen einer Funktion, Optimieren einer Schleife oder Umschreiben einer Methode ohne weitere Auswirkungen.[1] | Komplexe Aufgaben wie Refaktorisierung über Dateien hinweg, Generieren von Tests für ein Modul, Migrieren von Code oder Erstellen von Features von Grund auf.[3][5] |
| **Beispiele**             | - Wählen Sie eine fehlerhafte Funktion aus: "Fix this null check."<br>- Zeilen markieren: "Make this async." [2] | - Prompt: "Refactor the entire service layer to use async/await and update all dependencies."<br>- Oder: "Modernize this Java project to JDK 21 across files." [5][6] |
| **Risiken/Einschränkungen**    | Minimales Risiko, da Änderungen isoliert sind; erfordert aber manuelle Auswahl für jede Korrektur.[1] | Höhere Autonomie kann zu unbeabsichtigten Änderungen führen; immer Diffs überprüfen. Nicht ideal für hochkontrollierte Umgebungen.[7][4] |

### Anwendungsfälle und Workflows
- **Edit-Modus für gezielte Korrekturen**: Verwenden Sie diesen, wenn Sie genau wissen, was falsch ist, z.B. das Auswählen von fehleranfälligem Code in einer Funktion, um einen Bug zu beheben oder die Leistung zu verbessern. Es ist wie ein "Spot-Edit"-Tool – wählen Sie den Code in Ihrer IDE aus, prompten Sie Copilot über den Chat (z.B. "@workspace /fix") und wenden Sie die Diff-Vorschau an. Dieser Modus glänzt bei iterativer Entwicklung, bei der Sie die volle Kontrolle behalten und unberührte Bereiche nicht überarbeiten möchten. In einem .NET-Projekt könnten Sie beispielsweise eine Methode auswählen und "Identify null reference exceptions and suggest fixes" nur für dieses Snippet anfragen.[2][8] Er ist in VS Code und Visual Studio mit GitHub Copilot-Erweiterungen verfügbar.

- **Agent-Modus für projektweite Änderungen**: Aktivieren Sie diesen für ganzheitliche Änderungen, z.B. wenn Sie ganze Dateien bearbeiten oder Updates in einer Codebase koordinieren müssen. Starten Sie eine Sitzung im Copilot Chat (z.B. "#agentmode" oder über das Dropdown-Menü), geben Sie einen High-Level-Prompt wie "Find all uses of deprecated API and migrate to the new one in this project" und beobachten Sie, wie es Schritte plant: Dateien analysieren, Änderungen vorschlagen, Tests ausführen und iterieren. Es kann neue Dateien erstellen, Namespaces aktualisieren oder sogar Teile einer App scaffolden. Bei der Java-Modernisierung scannt es beispielsweise ein Legacy-Projekt, aktualisiert Gradle-Abhängigkeiten und validiert Änderungen über mehrere Dateien hinweg.[5][3] Dieser Modus ist besonders leistungsstark für Refactoring, Bug-Suche im großen Maßstab oder das Automatisieren repetitiver Aufgaben wie das Hinzufügen von Dokumentation oder Tests.[6][9]

Der Agent-Modus baut auf der Grundlage des Edit-Modus auf, erweitert ihn aber – betrachten Sie Edit als Skalpell für präzise Schnitte und Agent als Chirurg, der die gesamte Operation durchführt.[1] Benutzerdefinierte Anweisungen (z.B. über VS Code-Einstellungen) können den Agent-Modus für Konsistenz lenken, wie z.B. die Durchsetzung von Namenskonventionen über alle Änderungen hinweg.[1]

### Wann man welchen Modus wählt
- Entscheiden Sie sich für den **Edit/Fix-Modus**, wenn Ihre Aufgabe lokalisiert ist (z.B. das Reparieren einer einzelnen Funktion), um die Dinge einfach und schnell zu halten.
- Wechseln Sie zum **Agent-Modus** für Effizienz bei größeren Aufgaben, wie z.B. Bearbeitungen ganzer Dateien oder mehrstufige Refaktorisierungen, aber beginnen Sie klein, um Vertrauen in seine Ausgaben aufzubauen.[2][1] Beide erfordern ein GitHub Copilot-Abonnement (Pro oder höher) und sind in VS Code/Visual Studio integriert. Für die besten Ergebnisse kombinieren Sie sie: Verwenden Sie Edit für erste Korrekturen, dann Agent, um Änderungen projektweit zu verbreiten.[8] Wenn Sie mit sensiblen Code arbeiten, überprüfen Sie alle Agent-Vorschläge sorgfältig, um Überraschungen zu vermeiden.[7]

Zitate:
[1] https://github.blog/ai-and-ml/github-copilot/copilot-ask-edit-and-agent-modes-what-they-do-and-when-to-use-they/
[2] https://devblogs.microsoft.com/dotnet/ask-mode-vs-agent-mode/
[3] https://github.blog/ai-and-ml/github-copilot/agent-mode-101-all-about-github-copilots-powerful-mode/
[4] https://github.blog/developer-skills/github/less-todo-more-done-the-difference-between-coding-agent-and-agent-mode-in-github-copilot/
[5] https://github.blog/ai-and-ml/github-copilot/a-step-by-step-guide-to-modernizing-java-projects-with-github-copilot-agent-mode/
[6] https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode
[7] https://www.reddit.com/r/GithubCopilot/comments/1je448f/after_playing-with_agent_mode_i_think_my_favorite/
[8] https://visualstudiomagazine.com/articles/2025/06/18/copilot-compared-advanced-ai-features-in-visual-studio-2022-vs-vs-code.aspx
[9] https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/