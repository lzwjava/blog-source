---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Git Hooks Guide Pre Commit Pre Push
translated: true
type: note
---

### Übersicht über Git Hooks

Git Hooks sind anpassbare Skripte, die Aufgaben an bestimmten Punkten im Git-Workflow automatisieren. Sie können clientseitig (laufen auf Ihrem lokalen Rechner) oder serverseitig (laufen auf dem Remote-Repository) sein. Hooks werden im Verzeichnis `.git/hooks/` eines Repositorys gespeichert. Im Folgenden werde ich Pre-Commit-, Pre-Push- und serverseitige Hooks im Zusammenhang mit Pushes aufschlüsseln und erklären, wie sie ausgeführt werden.

### Clientseitige Hooks: Pre-Commit und Pre-Push

Diese Hooks laufen lokal auf Ihrem Rechner, bevor Aktionen abgeschlossen werden, und ermöglichen es Ihnen, Regeln durchzusetzen oder Prüfungen durchzuführen.

- **Pre-Commit-Hook**:
  - **Ausführungszeitpunkt**: Wird automatisch ausgelöst, kurz bevor Sie Änderungen committen (z. B. via `git commit`).
  - **Zweck**: Nützlich für Code-Qualitätsprüfungen, wie das Ausführen von Linters, Tests oder Formatierungstools. Wenn der Hook fehlschlägt (mit einem Exit-Status ungleich Null beendet wird), wird der Commit abgebrochen.
  - **Beispiel**: Ein Beispiel-Hook könnte `eslint` für JavaScript-Dateien ausführen. Wenn Fehler auftreten, wird der Commit gestoppt.
  - **Funktionsweise**: Das Skript befindet sich in `.git/hooks/pre-commit`. Machen Sie es mit `chmod +x .git/hooks/pre-commit` ausführbar. Wenn Sie Tools wie Husky (eine beliebte Bibliothek zur Verwaltung von Git Hooks) verwenden, wird die Einrichtung vereinfacht.

- **Pre-Push-Hook**:
  - **Ausführungszeitpunkt**: Wird automatisch ausgelöst, kurz bevor Sie an einen Remote pushen (z. B. via `git push`).
  - **Zweck**: Prüft Dinge wie das Ausführen von Tests, das Überprüfen der Code-Abdeckung oder die Gewährleistung der Kompatibilität, bevor Änderungen an den Remote gesendet werden. Wenn er fehlschlägt, wird der Push blockiert.
  - **Hinweis zu "some prepush"**: Es gibt keinen standardmäßigen "prepush"-Hook in Git – ich gehe davon aus, dass Sie den "pre-push"-Hook (mit Bindestrich) meinen. Sie können benutzerdefinierte Pre-Push-Skripte erstellen, oft über Tools wie Husky, um Regeln wie "pushe nur, wenn alle Tests bestehen" durchzusetzen.
  - **Beispiel**: Ein Pre-Push-Hook könnte `npm test` ausführen und den Push abbrechen, wenn Tests fehlschlagen. Wenn er übersprungen wird (z. B. mit `git push --no-verify`), läuft der Hook nicht.
  - **Funktionsweise**: Befindet sich unter `.git/hooks/pre-push`. Ausführbare Berechtigungen sind erforderlich. Er erhält Argumente wie den Remote-Namen und den ref, der gepusht wird.

Clientseitige Hooks stellen sicher, dass Probleme frühzeitig erkannt werden, und verhindern so, dass fehlerhafte Commits oder Pushs Ihren Rechner verlassen.

### Serverseitige Hooks während eines Pushs

Wenn Sie `git push` ausführen, wird der Push an das Remote-Repository (z. B. GitHub, GitLab oder einen benutzerdefinierten Server) gesendet. Der Remote kann seine eigenen Hooks haben, die während oder nach dem Push-Vorgang ausgeführt werden. Diese werden im `.git/hooks/`-Verzeichnis des Remote-Git-Repositorys gespeichert und vom Server-Administrator verwaltet.

- **Ablauf während eines Pushs**:
  1. **Lokale Prüfungen**: Der Pre-Push-Hook läuft zuerst (falls vorhanden).
  2. **Datenübertragung**: Die Änderungen werden an den Remote gesendet.
  3. **Ausführung auf dem Remote**: Serverseitige Hooks laufen auf dem Remote-Server, nicht auf Ihrem Rechner.

- **Pre-Receive-Hook**:
  - **Ausführungszeitpunkt**: Auf dem Remote-Server, unmittelbar nach Empfang des Pushs, aber bevor irgendwelche Refs (Branches oder Tags) aktualisiert werden.
  - **Zweck**: Validiert die eingehenden Änderungen. Er kann den gesamten Push ablehnen, wenn Prüfungen fehlschlagen, z. B. beim Erzwingen von Commit-Messages, Code-Reviews oder Sicherheitsscans.
  - **Funktionsweise**: Wenn der Hook mit einem Exit-Status ungleich Null beendet wird, wird der Push abgelehnt und Sie sehen eine Fehlermeldung. Beispiel: Lehne Pushs ab, die Dateien über einer bestimmten Größe einführen.

- **Update-Hook** (ähnlich wie Pre-Receive, aber pro Ref):
  - **Ausführungszeitpunkt**: Für jeden Branch/Tag, der aktualisiert wird, nach dem Pre-Receive-Hook.
  - **Zweck**: Ermöglicht eine feingranulare Kontrolle, z. B. ob der Push von einem autorisierten Benutzer stammt oder ob der Branch Namenskonventionen folgt.
  - **Funktionsweise**: Erhält Details über den ref, der aktualisiert wird.

- **Post-Receive-Hook**:
  - **Ausführungszeitpunkt**: Auf dem Remote-Server, nachdem der Push vollständig akzeptiert und die Refs aktualisiert wurden.
  - **Zweck**: Löst nachgelagerte Aktionen aus, wie das Deployen von Code, das Senden von Benachrichtigungen (z. B. Slack-Alerts) oder das Ausführen von Post-Deployment-Skripten wie "rebuild the application".
  - **Funktionsweise**: Läuft zuverlässig nach einem erfolgreichen Push. Beispiel: Automatisches Auslösen einer CI/CD-Pipeline oder Aktualisieren eines Web-Servers.

Serverseitige Hooks bieten eine zentralisierte Durchsetzung, sodass der Remote auch dann noch validieren oder auf den Push reagieren kann, wenn Ihre lokalen Hooks umgangen wurden. Plattformen wie GitHub verwenden Webhooks (API-basierte Äquivalente) für ähnliche Zwecke, aber für bare Git-Server oder selbst gehostete Repos sind die oben genannten Hooks entscheidend.

### Wichtige Unterschiede und Best Practices

- **Client vs. Server**: Client-Hooks (wie Pre-Commit/Pre-Push) geben Ihnen schnelles Feedback lokal. Server-Hooks erzwingen repository-weite Regeln.
- **Anpassung**: Hooks sind Shell-Skripte (z. B. Bash), können aber Python, Node.js usw. aufrufen. Verwenden Sie Tools wie pre-commit (ein Framework) zu deren Verwaltung.
- **Umgehung**: Commit mit `--no-verify`, Push mit `--no-verify`, aber Server-Hooks können nicht umgangen werden, es sei denn, Sie haben Administratorzugriff.
- **Setup-Tipps**: Hooks werden nicht zwischen Repos kopiert, fügen Sie sie also zu einer Repo-Vorlage hinzu oder verwenden Sie ein Tool zu deren Installation.

Wenn Sie dies einrichten, schauen Sie in die Git-Dokumentation oder verwenden Sie Tools wie Husky für Node-Projekte. Wenn Sie ein bestimmtes Szenario haben (z. B. ein Code-Beispiel), geben Sie mehr Details für eine maßgeschneiderte Beratung an!