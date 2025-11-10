---
audio: false
generated: true
image: false
lang: de
layout: post
title: Copilot in VS Code vs. IntelliJ
translated: true
type: note
---

Hier ist ein besser lesbarer Vergleich (keine sperrigen Tabellen, versprochen) des **GitHub Copilot Plugins in Visual Studio Code** gegenüber **IntelliJ IDEA**:

---

### Installation & Integration

* **VS Code**: Copilot wird wie eine Erstklasse-Erweiterung behandelt – einfach zu installieren, oft automatisch installiert und nach dem GitHub-Login einsatzbereit. ([GitHub Docs][1])

* **IntelliJ IDEA (und andere JetBrains IDEs)**: Copilot funktioniert über ein Plugin aus dem JetBrains Marketplace. Man installiert es, startet die IDE neu und authentifiziert sich dann über GitHub. ([GitHub Docs][1])

---

### Leistung & Reaktionsfähigkeit

* **VS Code**: Da Copilot nativ als Erweiterung läuft, fühlt es sich im Allgemeinen schneller an. ([Augment Code][2])

* **IntelliJ IDEA**: Als Plugin, das auf einer umfangreicheren IDE aufsetzt, kann Copilot mehr Latenz verursachen – besonders spürbar in großen Projekten oder bei komplexen Anfragen (z.B. kann die Generierung einer gesamten Funktion 2–5 Sekunden dauern). ([Augment Code][2])

---

### Workflow & Kompatibilität

* **VS Code**: Copilot unterstützt Inline-Vorschläge, vollständige Code-Generierung und Copilot Chat – alles eng integriert. ([GitHub Docs][3])

* **IntelliJ IDEA**: Copilot bietet ähnliche Funktionen – Inline-Vorschläge und einen Chat-Bereich – obwohl einige Nutzer Einschränkungen feststellen:

  > „[Es] kann Code nicht löschen/umschreiben oder zu verschiedenen Stellen springen.“ ([Medium][4], [Hacker News][5])

---

### Ökosystem-Passform & Funktionstiefe

* **VS Code**: Leichtgewichtig und vielseitig – ideal für schnelles Setup, Projekte mit gemischten Sprachen und diejenigen, die Flexibilität über mehrere Editoren hinweg benötigen.

* **IntelliJ IDEA / JetBrains IDEs**: Während Copilot KI auf den Tisch bringt, könnten JetBrains-Nutzer **JetBrains AI Assistant** (ihr natives KI-Tool) bevorzugen. Es bietet eine tiefere IDE-Integration – erweiterte Refactorings, Generierung von Commit-Nachrichten, enge Synergie mit JetBrains-Workflows und eine bessere Kontrolle über die Code-Nutzung/Datenschutz. ([Engine Labs Blog][6])

---

### Preisgestaltung & Lizenzierung

* **GitHub Copilot**: Abonnementbasiert – Einzelplatzlizenzen beginnen bei etwa 10 $/Monat. Einige kostenlose Optionen für Studenten. ([Techpoint Africa][7])

* **JetBrains AI** (zum Vergleich): Wird gebündelt mit JetBrains-Tools über das All Products Pack angeboten oder separat in Free-, Pro- und Ultimate-Tarifen erhältlich (ca. 10–20 $/Monat), abhängig vom Plan. ([AutoGPT][8])

---

### Zusammenfassung — Was ist besser für Sie?

**VS Code (Copilot plugin)**

* **Vorteile**: Ultra-leicht, schnell einzurichten, editorübergreifende Flexibilität, hervorragend für explorative Programmierung und Multi-Language-Workflows.
* **Nachteile**: Etwas weniger optimiert für schweres Refactoring oder projektweite Wahrnehmung.

**IntelliJ IDEA (Copilot plugin)**

* **Vorteile**: Ermöglicht die Nutzung von Copilot in Ihrer vertrauten JetBrains-Umgebung.
* **Nachteile**: Langsamer, manchmal in den Bearbeitungsfähigkeiten eingeschränkt, die plugin-basierte Architektur kann sich weniger nahtlos anfühlen.

**Zusätzlicher Gedanke**: Wenn Sie in JetBrains IDEs eingebunden sind und Sprachen wie Java oder Kotlin intensiv nutzen, könnte **JetBrains AI** Ihnen besser dienen, mit engerer Integration und erweiterten Funktionen – vorausgesetzt, Sie kommen mit dem anderen Preismodell zurecht.

---

Lassen Sie mich Ihren Workflow oder Projekttyp wissen, und ich kann Ihnen helfen, die beste Passform für einen KI-Coding-Assistenten zu finden!

[1]: https://docs.github.com/copilot/managing-copilot/configure-personal-settings/installing-the-github-copilot-extension-in-your-environment?utm_source=chatgpt.com "Installing the GitHub Copilot extension in your environment"
[2]: https://www.augmentcode.com/guides/github-copilot-vs-jetbrains-ai-ide-depth-latency-and-workflows?utm_source=chatgpt.com "GitHub Copilot vs JetBrains AI: IDE depth, latency, and ..."
[3]: https://docs.github.com/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide?utm_source=chatgpt.com "Asking GitHub Copilot questions in your IDE"
[4]: https://medium.com/%40prakash3210/exploring-github-copilot-a-revolutionary-coding-companion-across-vs-code-intellij-and-eclipse-749409b33a58?utm_source=chatgpt.com "Exploring GitHub Copilot: A Revolutionary Coding ..."
[5]: https://news.ycombinator.com/item?id=42964578&utm_source=chatgpt.com "They'd better get on the IntelliJ integration fast— if I'm going ..."
[6]: https://blog.enginelabs.ai/github-copilot-vs-jetbrains-ai?utm_source=chatgpt.com "Github Copilot vs JetBrains AI - Engine Labs Blog"
[7]: https://techpoint.africa/guide/jetbrains-ai-vs-github-copilot/?utm_source=chatgpt.com "JetBrains AI vs. GitHub Copilot: Which AI coding assistant ..."
[8]: https://autogpt.net/jetbrains-ai-assistant-vs-copilot-which-is-the-better-coding-assistant/?utm_source=chatgpt.com "JetBrains AI Assistant vs Copilot: Which is Better for Coding?"