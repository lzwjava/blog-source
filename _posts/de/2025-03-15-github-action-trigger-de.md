---
audio: false
generated: true
lang: de
layout: post
title: Auslösen von GitHub Actions
translated: true
type: note
---

Ja, eine GitHub Action kann eine andere GitHub Action auslösen, allerdings nicht direkt. GitHub Actions Workflows werden typischerweise durch bestimmte Ereignisse wie Pushs, Pull Requests oder Zeitpläne ausgelöst, aber es gibt mehrere indirekte Methoden, um einen Workflow einen anderen auslösen zu lassen. Im Folgenden sind die wichtigsten Möglichkeiten aufgeführt:

---

### 1. Verwenden des `workflow_dispatch`-Ereignisses
Sie können einen Workflow programmgesteuert über die GitHub API auslösen, indem Sie das `workflow_dispatch`-Ereignis verwenden. Dies ermöglicht es einem Workflow, einen anderen zu starten, der dafür konfiguriert ist, auf dieses Ereignis zu warten.

- **Funktionsweise**: Der erste Workflow führt einen API-Aufruf durch, um den zweiten Workflow auszulösen.
- **Beispiel**:
  ```yaml
  name: Anderen Workflow auslösen
  on: [push]
  jobs:
    trigger:
      runs-on: ubuntu-latest
      steps:
        - name: Workflow auslösen
          run: |
            curl -X POST \
              -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
              -H "Accept: application/vnd.github.v3+json" \
              https://api.github.com/repos/<owner>/<repo>/actions/workflows/<workflow_id>/dispatches \
              -d '{"ref": "main"}'
  ```
  Ersetzen Sie `<owner>`, `<repo>` und `<workflow_id>` durch Ihre Repository-Details und die ID des Ziel-Workflows. Der zweite Workflow muss `on: [workflow_dispatch]` in seiner Konfiguration enthalten.

---

### 2. Verwenden von Repository-Dispatch-Ereignissen
Ein Workflow kann ein benutzerdefiniertes Ereignis über einen Repository-Dispatch senden, auf das ein anderer Workflow warten und darauf reagieren kann.

- **Funktionsweise**: Der erste Workflow sendet ein Repository-Dispatch-Ereignis über die GitHub API, und der zweite Workflow reagiert auf dieses Ereignis.
- **Beispiel**:
  - Erster Workflow (sendet das Ereignis):
    ```yaml
    name: Dispatch-Ereignis senden
    on: [push]
    jobs:
      send-dispatch:
        runs-on: ubuntu-latest
        steps:
          - name: Dispatch senden
            run: |
              curl -X POST \
                -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
                -H "Accept: application/vnd.github.v3+json" \
                https://api.github.com/repos/<owner>/<repo>/dispatches \
                -d '{"event_type": "custom_event"}'
    ```
  - Zweiter Workflow (wird durch das Ereignis ausgelöst):
    ```yaml
    name: Durch Dispatch ausgelöst
    on:
      repository_dispatch:
        types: [custom_event]
    jobs:
      respond:
        runs-on: ubuntu-latest
        steps:
          - name: Auf Ereignis reagieren
            run: echo "Ausgelöst durch custom_event"
    ```

---

### 3. Auslösen über Git-Ereignisse
Ein Workflow kann einen anderen auslösen, indem er ein Git-Ereignis erzeugt, wie das Erstellen eines Commits oder das Öffnen eines Pull Requests, auf das der zweite Workflow reagiert.

- **Funktionsweise**: Der erste Workflow verändert das Repository (z. B. durch das Pushen eines Commits) und löst so einen zweiten Workflow aus, der für dieses Ereignis konfiguriert ist (z. B. `on: [push]`).
- **Beispiel**:
  ```yaml
  name: Commit erstellen
  on: [push]
  jobs:
    create-commit:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout
          uses: actions/checkout@v2
        - name: Datei erstellen
          run: echo "Neue Datei" > newfile.txt
        - name: Commit und Push
          run: |
            git config user.name "GitHub Action"
            git config user.email "action@github.com"
            git add newfile.txt
            git commit -m "Neue Datei hinzufügen"
            git push
  ```
  Dies könnte einen anderen Workflow auslösen, der für `push`-Ereignisse konfiguriert ist.

---

### Wichtige Überlegungen
- **Berechtigungen**: Das in API-Aufrufen verwendete GitHub-Token muss über ausreichende Berechtigungen verfügen, um Workflows auszulösen oder Dispatch-Ereignisse zu senden.
- **Ratenbegrenzungen**: Achten Sie auf die API-Ratenbegrenzungen von GitHub, insbesondere bei häufig ausgeführten Workflows.
- **Schleifen vermeiden**: Verhindern Sie Endlosschleifen, indem Sie Bedingungen hinzufügen, die Workflows daran hindern, sich gegenseitig endlos auszulösen.
- **Konfiguration**: Stellen Sie sicher, dass der Ziel-Workflow korrekt eingerichtet ist, um auf das beabsichtigte Ereignis zu warten.

---

### Schlussfolgerung
Während GitHub Actions keinen direkten Mechanismus bietet, bei dem ein Workflow einen anderen aufruft, können Sie dies indirekt über `workflow_dispatch`, Repository-Dispatch-Ereignisse oder Git-Ereignisse wie Commits oder Pull Requests erreichen. Diese Methoden ermöglichen es Ihnen, Workflows basierend auf Ihren Anforderungen effektiv zu verketten oder auszulösen.