---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Einzelfenster pro Projekt Vorteile
translated: true
type: note
---

Genau das – das ist eine fantastische Verfeinerung des Window-Positioning-Hacks, den wir besprochen haben. Sich auf *ein* dediziertes Fenster (oder Terminal/VSCode-Instanz) pro Projekt/Aufgabe zu beschränken, erzwingt dieses "Single Responsibility"-Prinzip, ohne den mentalen Aufwand, Duplikate zu jonglieren. Es ist, als ob man jedem Projekt seine eigene kleine Festung gibt: Kein Chaos innerhalb des Projekts bedeutet eine geringere Chance, den Fokus auf Unteraufgaben zu verteilen (z. B. versehentlich zwischen zwei VSCode-Tabs für das gleiche Backend-Tuning hin- und herzuwechseln).

Warum es besonders für dein Setup funktioniert:
-   **Reduziert Entscheidungsmüdigkeit**: Ein zweites Fenster "nur für den Fall" zu öffnen, lädt direkt in die Falle von "Welches hat den neuesten Diff?" – zack, sofortiger Kontextverlust. Ein Fenster hält alles an einem Ort: deine AI Prompts im integrierten Terminal, Logs, die im Output-Panel scrollen, und Code-Diffs direkt da. Das ist reiner Flow-State-Treibstoff.
-   **Einfachere visuelle Hierarchie**: Mit deinem Limit von 3-4 Fenstern verstärkt dies die räumlichen Hinweise. Das VSCode von Projekt 1 bleibt in dieser bevorzugten linken Bildschirmhälfte, ungeteilt; man teilt nur dann Bereiche auf, wenn es eine bewusste Debug-Session ist.
-   **AI-Synergie**: Für Claude Code Runs bedeutet ein Bereich pro Projektfenster, dass Prompts kontextuell bleiben – keine Querverweise von Ideen zwischen unabhängigen Features.

Schneller Enforcement-Hack, falls du in die Multi-Window-Gewohnheit zurückfällst: Lege eine VSCode-Workspace-Einstellung fest (`files.autoSave: "afterDelay"`), die dich zur Single-Instanz zurückführt, oder aliaste deine Launcher-Skripte so, dass sie immer das existierende Fenster verwenden (z.B. `code --reuse-window /pfad/zum/projekt`). Ich habe erlebt, wie Entwickler in ihren Dotfiles darauf schwören, um die Dinge monastisch einfach zu halten.

Ich liebe, wie du das iterativ weiterentwickelst – das fühlt sich nach deinem selbstgelehrten Stil an. Was ist der größte Gewinn, den du bisher vom Limit von einem Fenster pro Projekt bemerkt hast? Oder gibt es irgendwelche tückischen Szenarien, in denen du versucht warst, zu verdoppeln?