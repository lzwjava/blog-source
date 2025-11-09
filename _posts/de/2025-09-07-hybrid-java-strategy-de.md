---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Hybride Java-Entwicklungsstrategie
translated: true
type: note
---

Kurze Einschätzung: Für große Java-Codebasen funktioniert ein **Hybrid**-Ansatz am besten. Verwende **VS Code** als deine KI-zentrierte Kommandozentrale (Claude Code + Copilot = schnellere Iteration und weniger Boilerplate) und behalte **IntelliJ IDEA** für die „Operationen“ bei (tiefgreifendes Refactoring, Inspektionen, erweiterte Spring/Gradle/Maven-Assistenten). Man muss sich nicht für eine Religion entscheiden. 🙂

So würde ich darüber denken – ohne Tabellen, nur das Wesentliche:

### Wo VS Code glänzt

* **KI-Workflow**: Copilots Inline-Vervollständigungen sind in VS Code immer noch am besten, und Claude Codes repository-weite Analysen fühlen sich hier flotter an. Großartig zum Erstellen von Services, Tests, Mappern, SQL und schnellen Redesigns.
* **Leichtgewichtig & modular**: Du baust nur das ein, was du brauchst. Kalstarts und Speicherverbrauch sind freundlicher für große Monorepos.
* **„Spring zu“ + LSP**: Mit den Java-Erweiterungen sind „Gehe zu Definition/Implementierung“, Typ-Hierarchie, Aufruf-Hierarchie und Symbolsuche für den Alltag solide genug.

Empfohlene Erweiterungen (nach ID suchen):

* `vscjava.vscode-java-pack` (bündelt die meisten der folgenden)
* `redhat.java` (Language Support for Java)
* `vscjava.vscode-java-debug` / `vscjava.vscode-java-test`
* `vscjava.vscode-maven` / `vscjava.vscode-gradle`
* `vscjava.vscode-spring-boot-dashboard` + `vscjava.vscode-spring-initializr`
* `sonarsource.sonarlint-vscode` (statische Prüfungen)
* `streetsidesoftware.code-spell-checker` (überraschend hilfreich in JavaDocs)
* Claude Code + GitHub Copilot

Performance-Optimierungen für große Projekte (in `.vscode/settings.json` einfügen):

```json
{
  "java.maxConcurrentBuilds": 4,
  "java.jdt.ls.vmargs": "-Xms512m -Xmx4g -XX:+UseG1GC -XX:+UseStringDeduplication",
  "java.errors.incompleteClasspath.severity": "ignore",
  "java.referencesCodeLens.enabled": false,
  "java.implementationsCodeLens.enabled": false,
  "files.watcherExclude": {
    "**/target/**": true,
    "**/.gradle/**": true,
    "**/node_modules/**": true
  }
}
```

Tipps:

* Importiere als **Gradle** oder **Maven** Projekt (vermische Builds nach Möglichkeit).
* Aktiviere das **Spring Boot Dashboard** zum Ausführen/Debuggen mehrerer Services.
* Lass Klassen & Tests von Claude/Copilot entwerfen, verwende aber **SonarLint** und deine Unit-Tests als Sicherheitsnetz.

### Wo IntelliJ IDEA immer noch die Nase vorn hat

* **Tiefe & Genauigkeit beim Refactoring**: Umbenennen/Verschieben/Extrahieren über große Hierarchien hinweg, generics-lastige APIs, Lombok, XML-Konfiguration, sogar Spring-Bean-Verwaltung – IDEA's semantisches Modell ist kaum zu schlagen.
* **Inspektionen & Quick-Fixes**: Die eingebauten Code-Inspektionen (und strukturelle Suche/Ersetzung) finden mehr subtile Code-Smells als die meisten VS Code-Setups.
* **UML & Navigations-Kleinigkeiten**: Dataflow to here/from here, Abhängigkeitsdiagramme und erweiterte Suchbereiche sparen Zeit in komplexen Domänen.

Praktisches Muster:

* **Erkundung + Gerüstbau + repetitive Änderungen** in VS Code mit Claude/Copilot erledigen.
* Wenn du ein **nicht-triviales Refactoring** brauchst (z.B. ein Kernmodul teilen, API-Verträge über 40 Module ändern, Spring-Konfiguration migrieren), öffne dasselbe Repo in IDEA, lass es einmal indexieren, führe das Refactoring sicher durch, pushe die Änderungen und gehe zurück zu VS Code.

### Über „Codex“

OpenAIs alte **Codex**-Modelle wurden vor einer Weile eingestellt. Heute verwendest du hauptsächlich **GitHub Copilot** (OpenAI-powered) und **Claude Code**. Betrachte „Codex“ als historisch – dein aktueller Stack sollte **Copilot + Claude Code** sein.

### Statische Analyse & Qualität in VS Code

* **SonarLint** in VS Code gibt dir ein nahezu IDEA-ähnliches Gefühl; kombiniere es mit einer SonarQube/SonarCloud-Integration in deiner CI-Pipeline.
* Füge **SpotBugs** und **Checkstyle** über Gradle/Maven-Plugins hinzu, damit die Qualitätsprüfungen in der CI läuft (nicht nur lokal).
* Verwende den **JUnit** Test Explorer und die **Coverage Gutters** Erweiterung, um einen engen Red-Green-Refactor-Zyklus beizubehalten.

### Spring/Enterprise-Besonderheiten

* Die **Spring-Tools** von VS Code sind gut für Run/Debug, Actuator-Endpoints und Property-Hints. Für komplexe Auto-Konfiguration oder Meta-Annotationen löst IDEA Dinge immer noch zuverlässiger auf – verwende es, wenn Annotationen sich „rätselhaft“ anfühlen.
* Für **Gradle** Multi-Modul-Monster: Daemon + parallele Builds aktiviert lassen und Composite Builds in Betracht ziehen, um die Workspace-Größe zu begrenzen.

### KI-Workflow, der skaliert

* **Copilot Inline** für kleine Änderungen während des Tippens.
* **Claude Code** Chat für repository-weites Verständnis („Was sind die Nebeneffekte, wenn ich den Konstruktor von `LedgerPosting` ändere?“ / „Entwirf einen PR, um unseren eigenen Retry-Mechanismus durch resilience4j zu ersetzen“).
* Bitte das Modell, **Refactoring-Pläne + Checklisten** zu erstellen; wende die Änderungen dann in kleinen, überprüfbaren Commits an.
* Halte **Modell-Ausgaben unter Test**: Fordere Unit/Integration-Test-Diffs im selben PR an, den die KI generiert hat.

### Also… in welchem solltest du leben?

* Wenn dein Tag aus **Coden + Iterieren + vielen KI-Hilfen** besteht → **VS Code** als primärer Editor fühlt sich momentan besser an.
* Wenn dein Tag aus **Architektur + großen Refactorings + Debugging von Framework-Besonderheiten** besteht → behalte **IntelliJ** für diese Momente geöffnet.
* Viele Senior Engineers wechseln zwischen beiden. Das ist keine Ineffizienz; es ist das richtige Werkzeug für das richtige Risikoniveau.

Falls gewünscht, kann ich eine einmalige **VS Code Java Bootstrap**-Konfiguration (extensions.json, settings.json, empfohlene Tasks/Launch-Konfigs) generieren, die auf dein Monorepo abgestimmt ist – und eine kurze IDEA-Checkliste für „ruf die schweren Geschütze“-Momente.