---
audio: false
generated: true
lang: de
layout: post
title: GitHub Actions Parallelitäts-Einstellungen
translated: true
type: note
---

Ihre aktuelle GitHub Actions Workflow-Konfiguration hat bereits `cancel-in-progress: false`, was bedeutet, dass sie *laufende Jobs* für die `gh-pages`-Concurrency-Gruppe *nicht abbrechen sollte*. Wenn Jobs dennoch abgebrochen werden, könnte ein anderes Problem oder eine Fehlkonfiguration dieses Verhalten verursachen. Nachfolgend finden Sie Schritte zur Überprüfung und Behebung des Problems:

### 1. **Concurrency-Einstellungen bestätigen**
Ihre Konfiguration sieht korrekt aus, um Job-Abbrüche zu verhindern:

```yaml
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
```

- **Was dies bewirkt**: Der `concurrency`-Schlüssel mit `cancel-in-progress: false` stellt sicher, dass mehrere Workflow-Runs derselben `gh-pages`-Gruppe gleichzeitig ausgeführt werden können, ohne sich gegenseitig abzubrechen.
- **Wo er platziert werden muss**: Stellen Sie sicher, dass dieser `concurrency`-Block auf der **Workflow-Ebene** definiert ist (oberste Ebene der YAML-Datei, nicht innerhalb eines Jobs oder Schritts). Zum Beispiel:

```yaml
name: Deploy to GitHub Pages
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      # Ihre Schritte hier
```

Wenn der `concurrency`-Block falsch platziert ist (z.B. innerhalb eines Jobs), funktioniert er nicht wie erwartet. Verschieben Sie ihn bei Bedarf auf die oberste Ebene.

### 2. **Auf widersprüchliche Concurrency-Einstellungen prüfen**
- **Mehrere Workflows**: Wenn Sie mehrere Workflows haben (z.B. separate YAML-Dateien), die mit dem `gh-pages`-Branch interagieren, stellen Sie sicher, dass *alle* relevanten Workflows `cancel-in-progress: false` haben. Ein einzelner Workflow mit `cancel-in-progress: true` (oder fehlendem `concurrency`-Block) könnte Jobs aus anderen Workflows abbrechen.
- **Repository-Einstellungen**: Prüfen Sie, ob Repository-weite Einstellungen oder Drittanbieter-GitHub-Actions Abbruchverhalten erzwingen. Einige CI/CD-Integrationen oder benutzerdefinierte Actions könnten das Concurrency-Verhalten überschreiben.

### 3. **Workflow-Trigger überprüfen**
Jobs könnten scheinbar "abgebrochen" werden, wenn Trigger fehlkonfiguriert sind oder Race Conditions vorliegen. Prüfen Sie den `on`-Abschnitt Ihres Workflows:
- Stellen Sie sicher, dass der Workflow nur bei beabsichtigten Ereignissen ausgelöst wird (z.B. `on: push: branches: [ main ]` oder `on: pull_request`).
- Wenn mehrere Trigger definiert sind (z.B. `push` und `pull_request`), könnten sie überlappende Runs erzeugen. Verwenden Sie bei Bedarf eindeutige `concurrency.group`-Namen für verschiedene Trigger, wie:

```yaml
concurrency:
  group: 'gh-pages-${{ github.event_name }}'
  cancel-in-progress: false
```

Dies erzeugt separate Concurrency-Gruppen für `push`- und `pull_request`-Events und verhindert so Interferenzen.

### 4. **GitHub Actions Logs prüfen**
- Gehen Sie zum Tab **Actions** in Ihrem GitHub-Repository und überprüfen Sie die Logs der abgebrochenen Jobs.
- Suchen Sie nach Meldungen, die anzeigen, warum der Job abgebrochen wurde (z.B. "Canceled due to concurrency" oder andere Gründe wie Timeouts, manueller Abbruch oder Fehler).
- Wenn die Logs Concurrency erwähnen, überprüfen Sie doppelt, dass *alle* Workflows, die den `gh-pages`-Branch betreffen, `cancel-in-progress: false` haben.

### 5. **Manuelle Abbrüche behandeln**
Wenn jemand einen Workflow-Run manuell über die GitHub-UI abbricht, werden alle Jobs in diesem Run gestoppt, unabhängig von `cancel-in-progress: false`. Stellen Sie sicher, dass Ihr Team weiß, dass manuelle Abbrüche nur bei Bedarf durchgeführt werden sollten.

### 6. **Workflow-Abhängigkeiten berücksichtigen**
Wenn Jobs aufgrund von Abhängigkeiten oder Fehlern in früheren Schritten abgebrochen werden:
- Prüfen Sie auf `needs`-Schlüsselwörter in Ihrem Workflow. Wenn ein Job fehlschlägt, können abhängige Jobs übersprungen oder abgebrochen werden.
- Verwenden Sie `if: always()`, um sicherzustellen, dass nachfolgende Jobs auch dann ausgeführt werden, wenn frühere fehlschlagen:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Build-Schritte
  deploy:
    needs: build
    if: always()
    runs-on: ubuntu-latest
    steps:
      # Deploy-Schritte
```

### 7. **Mit einem minimalen Workflow testen**
Wenn das Problem weiterhin besteht, erstellen Sie einen minimalen Test-Workflow, um das Problem zu isolieren:

```yaml
name: Test Concurrency
on:
  push:
    branches: [ main ]
concurrency:
  group: 'gh-pages'
  cancel-in-progress: false
jobs:
  test-job:
    runs-on: ubuntu-latest
    steps:
      - name: Sleep to simulate long job
        run: sleep 60
      - name: Print message
        run: echo "Job completed!"
```

Pushen Sie mehrere Commits, um gleichzeitige Runs auszulösen, und verifizieren Sie, ob Jobs ohne Abbruch abgeschlossen werden.

### 8. **GitHub Actions Status prüfen**
In seltenen Fällen könnte GitHub Actions plattformweite Probleme haben. Prüfen Sie die [GitHub Status Seite](https://www.githubstatus.com/) oder aktuelle Posts auf X bezüglich GitHub Actions-Ausfällen.

### 9. **Debugging-Tipps**
- Fügen Sie einen Schritt hinzu, um die Workflow-Run-ID und die Concurrency-Gruppe für Debugging-Zwecke zu protokollieren:

```yaml
steps:
  - name: Log run details
    run: echo "Run ID: ${{ github.run_id }}, Concurrency Group: ${{ github.workflow }}-${{ github.event_name }}"
```

- Verwenden Sie die GitHub Actions API, um bei Bedarf laufende Workflows programmatisch zu inspizieren (erfordert erweiterte Einrichtung).

### Falls es immer noch nicht funktioniert
Wenn Jobs weiterhin abgebrochen werden:
- Teilen Sie die vollständige Workflow-YAML-Datei und einen Screenshot oder eine Beschreibung der Abbruchmeldung aus den GitHub Actions Logs.
- Lassen Sie mich wissen, ob Sie spezifische Actions verwenden (z.B. `actions/checkout`, `peaceiris/actions-gh-pages`) oder ob Sie mehrere Workflows haben, die mit `gh-pages` interagieren.

Dies wird helfen, das genaue Problem einzugrenzen. Lassen Sie mich wissen, wie ich weiter helfen kann!