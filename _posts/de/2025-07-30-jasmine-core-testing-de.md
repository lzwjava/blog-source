---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Übersicht des Jasmine Core Testframeworks
translated: true
type: note
---

### Jasmine-Core
Jasmine-core ist die Kernbibliothek von Jasmine, einem beliebten JavaScript-Testing-Framework. Es bietet Werkzeuge für das Schreiben von Behavior-Driven Development (BDD)-Tests, einschließlich Funktionen wie Test-Suites (describe-Blöcke), einzelne Tests (it-Blöcke) und Matchers für Assertions (z.B. expect().toBe()). Es ist eigenständig und kann in Browsern oder Node.js-Umgebungen ausgeführt werden.

- **Zweck**: Ermöglicht Entwicklern das Schreiben und Ausführen von Unit-Tests für JavaScript-Anwendungen in einem lesbaren, spezifikationsähnlichen Format.
- **Installation**: Typischerweise über npm (`npm install jasmine-core`).
- **Anwendungsbeispiel**: Tests können manuell eingerichtet oder mit Tools wie Karma integriert werden. Es ist Open-Source und wird auf GitHub gepflegt (https://github.com/jasmine/jasmine), wobei die neueste Version (Stand meiner letzten Aktualisierung) etwa 5.x ist.
- **Relevanznachweis**: Es ist eine grundlegende Abhängigkeit für viele JavaScript-Test-Setups und wird von Projekten wie Angular- und React-Apps für TDD/BDD-Praktiken verwendet.

### Karma-Jasmine-HTML-Reporter
Der karma-jasmine-html-reporter ist ein NPM-Paket, das einen HTML-basierten Reporter-Plugin für Karma, den JavaScript-Test-Runner, bereitstellt. Es integriert sich in Jasmine-Tests, indem es die Ergebnisse in einer benutzerfreundlichen Web-Oberfläche anzeigt, bestandene/fehlgeschlagene Tests, Stack Traces und Zeitinformationen darstellt, die alle in einer HTML-Seite gerendert werden, die während der Testausführung in Echtzeit aktualisiert wird.

- **Zweck**: Verbessert das Test-Feedback durch eine browserbasierte HTML-Oberfläche anstelle einer Konsolenausgabe, was das Debuggen für Entwickler erleichtert. Es ist für die Testlogik auf jasmine-core und für die Testausführung über mehrere Browser auf karma angewiesen.
- **Installation**: Über npm (`npm install karma-jasmine-html-reporter --save-dev`).
- **Konfiguration**: Wird der Konfigurationsdatei von Karma (z.B. `karma.conf.js`) als Plugin und Reporter hinzugefügt. Erfordert, dass sowohl karma als auch karma-jasmine eingerichtet sind.
- **Relevanznachweis**: Es ist eine beliebte Wahl für Karma-Benutzer, mit Dokumentation auf der offiziellen Karma-Website (https://karma-runner.github.io) und häufigen Updates. Es verändert die Testausführung nicht, verbessert aber die Visualisierung, wie in vielen Entwickler-Workflows zu sehen ist.

Beide Tools werden oft zusammen verwendet: jasmine-core übernimmt die Testlogik, während karma-jasmine-html-reporter die Ergebnisse in einer Karma-gesteuerten Test-Suite visualisiert. Wenn Sie ein JS-Testing-Setup einrichten, beginnen Sie mit der Dokumentation von Karma für die Integration.