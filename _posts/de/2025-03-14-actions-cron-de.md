---
audio: false
generated: true
lang: de
layout: post
title: GitHub Actions Cron Zeitplanung
translated: true
type: note
---

Ja, ein GitHub-Workflow kann so konfiguriert werden, dass er einmal täglich über einen Cron-Zeitplan in GitHub Actions ausgeführt wird.

### Erklärung
GitHub Actions ermöglicht es Ihnen, Aufgaben in Ihrem Repository durch Workflows zu automatisieren, die in YAML-Dateien im Verzeichnis `.github/workflows` definiert sind. Eine Möglichkeit, einen Workflow auszulösen, ist die Verwendung des `schedule`-Events, das eine cron-ähnliche Syntax verwendet, um festzulegen, wann der Workflow ausgeführt werden soll. Die Cron-Syntax in GitHub Actions folgt dem standardmäßigen POSIX-Format und besteht aus fünf Feldern: Minute, Stunde, Tag des Monats, Monat und Tag der Woche.

Um einen Workflow einmal täglich auszuführen, können Sie einen Cron-Ausdruck wie `0 0 * * *` verwenden, was "jeden Tag um 00:00 UTC" bedeutet. Hier die Aufschlüsselung:
- **Minute (0)**: 0 Minuten nach der vollen Stunde
- **Stunde (0)**: 00:00 (Mitternacht) UTC
- **Tag des Monats (*)**: Jeden Tag des Monats
- **Monat (*)**: Jeden Monat
- **Tag der Woche (*)**: Jeden Tag der Woche

### Beispielkonfiguration
Nachfolgend finden Sie eine Beispielkonfiguration für einen GitHub Actions Workflow, der einmal täglich ausgeführt wird:

```yaml
name: Täglicher Workflow
on:
  schedule:
    - cron: '0 0 * * *'
jobs:
  beispiel-job:
    runs-on: ubuntu-latest
    steps:
      - name: Nachricht ausgeben
        run: echo "Dies wird einmal täglich ausgeführt!"
```

Dieser Workflow wird jeden Tag um Mitternacht UTC ausgeführt.

### Wichtige Überlegungen
- **Zeitzone**: Der Zeitplan operiert in UTC, passen Sie den Cron-Ausdruck also an, wenn die Ausführung zu einer bestimmten Zeit in Ihrer lokalen Zeitzone erfolgen soll.
- **Standard-Branch**: Standardmäßig laufen geplante Workflows auf dem Standard-Branch des Repositorys (z.B. `main` oder `master`), sofern nicht anders angegeben.
- **Zuverlässigkeit**: Obwohl GitHub Actions versucht, Workflows zur angegebenen Zeit auszuführen, können aufgrund der Infrastrukturauslastung leichte Verzögerungen auftreten, was jedoch selten vorkommt.
- **Nutzungslimits**: Für kostenlose GitHub-Konten gelten Limits für die Actions-Nutzung (z.B. Minuten pro Monat), aber eine einzelne tägliche Ausführung liegt typischerweise gut innerhalb dieser Grenzen.

### Schlussfolgerung
Mit einem richtig konfigurierten Cron-Ausdruck in der Workflow-Datei kann GitHub Actions tatsächlich einen Workflow einmal täglich ausführen. Daher lautet die Antwort auf Ihre Frage **ja**.