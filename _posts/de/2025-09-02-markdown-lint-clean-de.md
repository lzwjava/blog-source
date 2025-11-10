---
audio: false
generated: true
image: false
lang: de
layout: post
title: Markdown-Linting für konsistente saubere Dateien
translated: true
type: note
---

Hier ist eine übersichtliche, leserfreundliche Einführung in das **markdownlint**-Projekt von David Anson:

---

## Was ist **markdownlint**?

**markdownlint** ist ein Static-Analysis-Tool für Markdown/CommonMark-Dateien, das auf Node.js basiert. Sein Hauptzweck ist es, Konsistenz und Stilregeln für Markdown-Inhalte durchzusetzen – es hilft Autoren dabei, ein sauberes, einheitliches Format beizubehalten und Konstrukte zu vermeiden, die in verschiedenen Parsern fehlschlagen oder inkonsistent dargestellt werden könnten ([GitHub][1]).

Inspiriert von dem Ruby-basierten markdownlint (markdownlint/mdl), nutzt dieses Tool eine umfangreiche Bibliothek von Linting-Regeln. Es verwendet den micromark-Parser für CommonMark-Unterstützung und erweitert diesen um GitHub Flavored Markdown (GFM)-Funktionen wie Tabellen, Autolinks, Direktiven, Fußnoten und Mathe ([GitHub][1]).

## Wichtige Funktionen & Integrationen

* **Regelabdeckung**: Bietet einen umfassenden Satz an integrierten Regeln – von Überschriften-Stilen und Listen-Einzügen bis hin zu Leerzeichen am Zeilenende und Zeilenlänge (z.B. MD001, MD009, MD013…) ([GitHub][1]).
* **Ökosystem-Kompatibilität**:

  * **Kommandozeilen-Tools**:

    * `markdownlint-cli` – eine traditionelle CLI-Oberfläche.
    * `markdownlint-cli2` – eine schnellere, konfigurationsbasierte CLI mit flexiblen Formatierungsoptionen und Unterstützung für Globs, Ausgabeformate, Autofixing und Integration in CI-Workflows ([GitHub][2], [GitHub][3]).
  * **VS Code-Erweiterung**:

    * `vscode‑markdownlint` bringt Echtzeit-Linting in Ihren Editor. Verstöße werden inline markiert (unterstrichen), mit einblendbaren Tooltips und Schnellkorrektur-Vorschlägen ([GitHub][4]).
  * **GitHub Action**:

    * `markdownlint‑cli2‑action` ermöglicht es, markdownlint in Ihre CI-Pipeline einzubetten, was automatische Prüfungen (und optionales Autofixing) während GitHub-Workflows erlaubt ([GitHub][5]).

---

## Warum sollte man es verwenden?

* **Konsistenz**: Stellt sicher, dass Markdown-Dateien einem definierten Styleguide folgen und reduziert Formatierungsabweichungen in einem Projekt.
* **Editor-Unterstützung**: Inline-Feedback in VS Code und anderen Integrationen erleichtert und beschleunigt das Schreiben von sauberem Code.
* **Automatisierung**: Einsatz in CI-Pipelines mit Lint-Tools oder GitHub Actions, um Standards vor Merges durchzusetzen.
* **Anpassbar**: Sie können Regelsätze anpassen oder sogar Regeln über Konfigurationsdateien oder Inline-Kommentare deaktivieren (z.B. das Deaktivieren von MD013 für lange Zeilen) ([GitHub][5], [Software Recommendations Stack Exchange][6]).

---

Möchten Sie eine Kurzanleitung zur Einrichtung mit npm, zur Verwendung der VS Code-Erweiterung oder zur Integration in CI-Workflows?

[1]: https://github.com/DavidAnson/markdownlint?utm_source=chatgpt.com "DavidAnson/markdownlint: A Node.js style checker and lint ..."
[2]: https://github.com/markdownlint/markdownlint?utm_source=chatgpt.com "Markdown lint tool"
[3]: https://github.com/DavidAnson/markdownlint-cli2?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2"
[4]: https://github.com/DavidAnson/vscode-markdownlint?utm_source=chatgpt.com "DavidAnson/vscode-markdownlint: Markdown linting and ..."
[5]: https://github.com/DavidAnson/markdownlint-cli2-action?utm_source=chatgpt.com "DavidAnson/markdownlint-cli2-action"
[6]: https://softwarerecs.stackexchange.com/questions/7138/markdown-lint-tool?utm_source=chatgpt.com "validation - Markdown lint tool"