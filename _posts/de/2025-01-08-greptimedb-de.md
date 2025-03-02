---
audio: false
generated: false
lang: de
layout: post
title: Unternehmen sollten KI-Kontext oder -Agenten bereitstellen, um die Integration
  zu erleichtern
translated: true
---

Ich habe einen Freund, der bei Greptime DB arbeitet, und ich habe darüber nachgedacht, wie man ihr Produkt schnell in bestehende Systeme integrieren kann.

## Kontext

Ein möglicher Ansatz besteht darin, mehr KI-Kontext bereitzustellen. Greptime DB könnte seine Dokumentation so gestalten, dass sie mit KI-Tools wie ChatGPT kompatibel ist, wodurch der Integrationsprozess vereinfacht wird.

Greptime DB bietet Dokumentation unter [https://greptime.com](https://greptime.com) an, aber ich frage mich, ob Tools wie ChatGPT oder DeepSeek effizient alle Seiten in ihrer Dokumentation verarbeiten können. Darüber hinaus ist eine Fülle von Informationen über GitHub-Repositories, Issues, interne Dokumente, öffentliche Dokumente und andere versteckte Wissensquellen verstreut, die nicht explizit dokumentiert sind.

Um dies zu beheben, könnte Greptime DB mehrere spezialisierte GPTs erstellen müssen. Zum Beispiel könnten sie Eingabeaufforderungen wie diese erstellen:

```
Der Codeblock bleibt unverändert, da es sich um eine spezielle Formatierung handelt, die nicht übersetzt werden sollte.

### Greptime Docs:  
Die offizielle Dokumentation ist verfügbar unter: [https://docs.greptime.com](https://docs.greptime.com)

* [Schnellstart-Anleitung](https://docs.greptime.com/getting-started/quick-start)  
* [Benutzerhandbuch](https://docs.greptime.com/user-guide/overview)  
* [Demos](https://github.com/GreptimeTeam/demo-scene)  
* [FAQ](https://docs.greptime.com/faq-and-others/faq)

### Repository-URLs:
Hier sind die wichtigsten Verzeichnisse und Dateien aus dem Stammverzeichnis des GreptimeDB-Repositorys:

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
Der obige Codeblock bleibt unverändert, da es sich um einen Codeblock handelt und dieser in der Regel nicht übersetzt wird.

Dies würde es Benutzern ermöglichen, mit einem GPT-basierten Chatbot zu interagieren, der Fragen basierend auf der Dokumentation beantwortet und so genauere Antworten gewährleistet.

Lass uns dieses GPT erstellen: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

Konnte diese Frage nicht beantworten,

```
Worum geht es in `greptimedb/src/query/src/query_engine/context.rs`?
```



## Agent

Ich stelle mir ein Tool namens `greptimedb-agent` vor, das den Integrationsprozess vereinfacht.

Stell dir vor, du führst einen einfachen Befehl wie:

```bash
pip install greptimedb-agent
greptimedb-agent
```

(Die Befehle bleiben auf Englisch, da es sich um Code handelt, der nicht übersetzt werden sollte.)

`greptimedb-agent` sammelt intelligent Informationen über das aktuelle System, wie beispielsweise die Maschinendetails und den vorhandenen Code, um den Kontext zu verstehen und zu entscheiden, wie Greptime DB am besten integriert werden kann.

Dieser Befehl würde Ihren Code automatisch aktualisieren, um Greptime DB zu integrieren, und würde Ihre aktuelle Datenbank in nur wenigen Schritten nahtlos durch Greptime DB ersetzen.

