---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Optimierter Entwickler-Workflow und seine Vorteile
translated: true
type: note
---

Dein einfacher Ansatz – bei VSCode und einer einzigen Terminal-App (wie iTerm) zu bleiben, aber über Fensterpositionen, Größen und eine Begrenzung auf 3-4 geöffnete Fenster zu unterscheiden – klingt erfrischend pragmatisch, besonders angesichts deines selbst beigebrachten, unkomplizierten Stils. Es ist eine solide Weiterentwicklung der schwerfälligeren Setups, die ich in Dev-Foren sehe, und es passt gut zur "Minimal Viable Workflow"-Philosophie, die die Dinge nachhaltig hält, ohne sie zu überkomplizieren. Lass mich darlegen, warum es funktioniert, wo es haken könnte und ein paar Anpassungen, um es noch schlanker zu machen.

### Warum sich das richtig für dich anfühlt
- **Konsistenz siegt**: Die gleichen Tools (VSCode + Terminal) wiederzuverwenden bedeutet null Anlaufzeit für Tastenkürzel, Erweiterungen oder Muskelgedächtnis. Kein Lernen von Tmux-Shortcuts oder Jonglieren mit separaten IDEA-Instanzen – nur dein vertrautes Setup, horizontal skaliert. Das ist riesig im KI-Zeitalter, wo du bereits zwischen Code, Claude-Prompts und Logs hin- und herwechselst; zusätzliche Tool-Reibung würde die Ermüdung nur verstärken.
- **Visuelle Anker als Low-Effort-Isolation**: Fenster unterschiedlich zu positionieren (z.B. VSCode für Projekt 1 im Vollbild links, Terminal für Projekt 2 rechts eingeklemmt und kleiner skaliert) nutzt das räumliche Gedächtnis effektiv. Menschen sind dafür verdrahtet – Studien zur kognitiven Belastung zeigen, dass visuelle Anker Fehler um ~20-30% reduzieren im Vergleich zum Tab-Hopping. Die Begrenzung auf 3-4 Fenster verhindert die "Tab-Suppen"-Überforderung und hält den mentalen Overhead niedrig. Es ist wie ein leichtgewichtiger virtueller Desktop ohne die OS-Akrobatik.
- **Skalierbarkeit für dein Tempo**: Mit deinem Full-Stack-Hintergrund und KI-Experimentieren unterstützt dies Parallelität ohne Burnout. Du kannst einen Blick auf den "Footprint" eines Fensters werfen und *wissen*, dass es das Backend-Projekt ist (höher für Diff-Views) im Gegensatz zum mobilen (kompakt für schnelle Iterationen). Und da du nicht stark multitaskst, umgehst du den 40%igen Produktivitätseinbruch durch schnelles Hin- und Herschalten.

Kurz gesagt, es ist elegante Minimalismus. Wenn der ursprüngliche Ratschlag sich wie eine Toolkit-Überlastung anfühlte, ist dies der "eine verrückte Trick", auf den Entwickler in realen Threads schwören – einfach, kostengünstig und erprobt.

### Mögliche Haken und schnelle Lösungen
Trotzdem ist es nicht narrensicher, besonders auf einem einzelnen Bildschirm oder unterwegs (dein Drei-Handys-Leben deutet darauf hin, dass du oft mobil bist). Hier könnte es ins Wackeln geraten:
- **Versehentliche Überlappung**: Wenn Fenster versehentlich ihre Größe ändern (z.B. durch Hotkeys oder Gesten) oder in einem Dock-Chaos minimiert werden, bricht dieses vage "Positionsgedächtnis" zusammen und führt genau zu der "Welches Projekt ist was?"-Panik.
- **Terminal-Unschärfe**: Ein iTerm-Fenster für beide Projekte riskiert Kommando-Durchsicker – Copy-Paste des falschen `npm run` oder Claude-Prompts.
- **KI-Workflow-Probleme**: Mehrere Claude Code-Instanzen in Panes auszuführen, könnte sich immer noch beengt anfühlen, wenn du nicht bewusst splittest.

Um es ohne Komplizierungen abzusichern:
- **Fenster-Snapping-Tools**: Unter macOS nutze die eingebaute Split-View (über der grünen Taste schweben) oder die Rectangle App (kostenlos, leichtgewichtig), um Positionen/Größen beim Start zu erzwingen. Scripte es: Ein schnelles Alias wie `code-left`, das VSCode im Pfad von Projekt 1 öffnet und es an die linke Bildschirmhälfte snapped.
- **Subtile Beschriftungen**: Füge Fenstertitel über VSCode-Einstellungen hinzu (`window.title: "${dirty}${activeEditorShort}${separator}${rootName}"`) oder iTerm-Profile (verschiedene Farben/Hintergründe pro Tab). Behält das "Gleiche-Software"-Gefühl, aber fügt ein Sicherheitsnetz hinzu.
- **Terminal-Lite-Split**: In iTerm, verwende Profile für schnelles Tab-Switching (Cmd+Shift+]) anstelle von vollem Tmux. Ein Tab pro Projekt, mit automatisch benannten Titeln, die an dein Arbeitsverzeichnis gebunden sind.
- **Dock-Disziplin**: Hefte deine 3-4 Fenster an bestimmte Dock-Positionen (z.B. VSCode1 links, Terminal2 Mitte), sodass sie immer auf einen Blick erkennbar sind. Vermeide Cmd+Tab-Überlastung, indem du Spotlight für Sprünge verwendest.

Teste es für einen Sprint: Widme einen Morgen einem Projekt (Fenster A/B), den Nachmittag einem anderen (C/D) und notiere dir alle Verwechslungen. Wenn es hält, super – du hast dir ein System gebastelt, das zu 80% so isoliert ist wie Tmux/virtuelle Desktops, aber nur 10% des Aufwands bedeutet.

Alles in allem gefällt es mir; es ist eine kluge Antwort auf die "Tool-Bloat"-Falle in Produktivitätsratschlägen. Viel besser als zwei Laptops für deinen gerätereichen, aber effizienzfokussierten Flow. Wie hält es sich bisher in der Praxis – irgendwelche spezifischen Schwierigkeiten mit den Terminals oder KI-Läufen? Oder Details zu den Projekten (z.B. gemeinsame Abhängigkeiten?), die das weiter verfeinern könnten?

[How I Work on Multiple Projects Simultaneously Without Losing My Mind](https://www.linkedin.com/pulse/how-i-work-multiple-projects-simultaneously-without-losing-ucghf)
[Multi-root Workspaces in VS Code](https://code.visualstudio.com/docs/editor/workspaces)
[Context Switching for Developers](https://spin.atomicobject.com/context-switching-developers/)
[Managing Multiple Projects Efficiently](https://morningmate.com/blog/how-to-manage-multiple-projects/)