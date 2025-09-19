---
audio: false
generated: false
image: false
lang: de
layout: post
title: Unternehmen sollten AI-Kontext bereitstellen, um die Integration zu erleichtern
translated: true
---

Ich habe einen Freund, der bei Greptime DB arbeitet, und ich habe darüber nachgedacht, wie man ihr Produkt schnell in bestehende Systeme integrieren kann.

## Kontext

Ein möglicher Ansatz besteht darin, mehr KI-Kontext bereitzustellen. Greptime DB könnte seine Dokumentation so organisieren, dass sie mit KI-Tools wie ChatGPT kompatibel ist und den Integrationsprozess vereinfacht.

Greptime DB bietet Dokumentation unter [https://greptime.com](https://greptime.com) an, aber ich frage mich, ob Tools wie ChatGPT oder DeepSeek alle Seiten der Dokumentation effizient verarbeiten können. Darüber hinaus ist eine Fülle von Informationen über GitHub-Repositories, Issues, interne Dokumente, öffentliche Dokumente und andere verstreute Wissensstücke verteilt, die nicht explizit dokumentiert sind.

Um dies zu beheben, könnte Greptime DB mehrere spezialisierte GPTs erstellen. Zum Beispiel könnten sie Prompts wie diesen erstellen:

```

### Greptime Docs:
Die offizielle Dokumentation ist verfügbar unter: [https://docs.greptime.com](https://docs.greptime.com)

* [Quickstart Guide](https://docs.greptime.com/getting-started/quick-start)
* [Benutzerhandbuch](https://docs.greptime.com/user-guide/overview)
* [Demos](https://github.com/GreptimeTeam/demo-scene)
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

### Repository-URLs:
Hier sind die wichtigsten Verzeichnisse und Dateien aus dem Stammverzeichnis des GreptimeDB-Repository:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

Zusätzliche wichtige Dateien:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

Bitte durchsuchen Sie diese Ressourcen, bevor Sie auf Benutzeranfragen antworten.

```

Dies würde es Nutzern ermöglichen, mit einem GPT-basierten Chatbot zu interagieren, der Fragen auf der Grundlage der Dokumentation beantwortet und so genauere Antworten gewährleistet.

Lassen Sie uns diesen GPT erstellen: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

Konnte diese Frage nicht beantworten,

```
was ist `greptimedb/src/query/src/query_engine/context.rs`?
```

## Agent

Ich stelle mir ein Tool namens `greptimedb-agent` vor, um den Integrationsprozess zu vereinfachen.

Stellen Sie sich vor, Sie führen einen einfachen Befehl wie diesen aus:

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` würde intelligent Informationen über das aktuelle System sammeln, wie z. B. die Maschinendetails und den bestehenden Code, um den Kontext zu verstehen und zu entscheiden, wie Greptime DB am besten integriert werden kann.

Dieser Befehl würde automatisch Ihren Code aktualisieren, um Greptime DB zu integrieren, und würde Ihre aktuelle Datenbank nahtlos in wenigen Schritten durch Greptime DB ersetzen.