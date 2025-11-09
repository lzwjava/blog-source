---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfigurieren von Azure DevOps Branch-Triggern
translated: true
type: note
---

Azure DevOps Pipelines ermöglichen es Ihnen zu konfigurieren, welche Branches Builds und Deployments auslösen. Dies geschieht hauptsächlich über **CI-Trigger** (für Builds bei Code-Pushes) und **PR-Trigger** (für Pull Requests). Die Konfiguration unterscheidet sich leicht zwischen YAML-Pipelines (empfohlen für Versionskontrolle) und klassischen Pipelines. Im Folgenden konzentriere ich mich zuerst auf YAML, da es der moderne Ansatz ist, und gehe dann kurz auf klassische Pipelines ein. Alle Beispiele setzen ein Git-Repository voraus.

## YAML-Pipelines: Konfigurieren von Branch-Triggern

YAML-Pipelines definieren Trigger direkt in Ihrer `azure-pipelines.yml`-Datei. Standardmäßig werden Pipelines bei Pushes auf **alle Branches** ausgelöst (entspricht `trigger: branches: include: - '*'`). Sie können dies für eine feinere Steuerung anpassen.

### Schritt 1: Grundlegende Einrichtung
1. Gehen Sie in Ihrem Azure DevOps-Projekt zu **Pipelines > Builds** (oder **Releases** für CD).
2. Erstellen oder bearbeiten Sie eine Pipeline und wählen Sie **YAML** als Vorlage.
3. Fügen Sie im YAML-Editor einen `trigger`-Abschnitt auf der obersten Ebene hinzu.

### Schritt 2: Einfache Branch-Includes
Verwenden Sie eine einfache Liste, um Trigger für bestimmte Branches oder Muster zu definieren:
```yaml
trigger:
- main          # Wird bei Pushes auf 'main' ausgelöst
- develop       # Auch 'develop'
- releases/*    # Jeder Branch, der mit 'releases/' beginnt (z.B. releases/v1.0)
```
- Speichern und committen Sie die YAML-Datei in Ihr Repo. Die Pipeline wird jetzt nur noch für diese Branches ausgeführt.
- Wildcards wie `*` (null oder mehr Zeichen) und `?` (einzelnes Zeichen) werden unterstützt. Setzen Sie Muster, die mit `*` beginnen, in Anführungszeichen (z.B. `*-hotfix`).

### Schritt 3: Erweiterte Includes/Excludes
Für Ausschlüsse oder mehr Präzision:
```yaml
trigger:
  branches:
    include:
    - main
    - releases/*
    - feature/*
    exclude:
    - releases/old-*     # Schließt 'releases/old-v1' usw. aus
    - feature/*-draft    # Schließt Entwurfs-Features aus
```
- **Include**: Branches, die *auslösen können* (beginnt standardmäßig mit allen, wenn weggelassen).
- **Exclude**: Filtert Elemente aus der Include-Liste aus (wird nach Includes angewendet).
- Wenn Sie eine `branches`-Klausel angeben, überschreibt diese die Standardeinstellung (alle Branches) – nur explizite Includes lösen dann aus.
- Für Tags: Verwenden Sie `refs/tags/v1.*` in Includes.

### Schritt 4: Pfadfilter (Optional)
Kombinieren Sie mit Dateipfaden für granulare Steuerung:
```yaml
trigger:
  branches:
    include:
    - main
  paths:
    include:
    - src/*.cs          # Nur bei Änderungen im 'src'-Ordner
    exclude:
    - docs/*.md         # Ignoriert Dokumentationsänderungen
```
- Pfade sind relativ zum Repo-Stammverzeichnis und case-sensitiv.

### Schritt 5: Batching und Opt-Out
- **Batch-Ausführungen**: Um mehrere Pushes in einem Build zusammenzufassen (reduziert Rauschen):
  ```yaml
  trigger:
    batch: true
    branches:
      include:
      - main
  ```
- **Trigger deaktivieren**: Setzen Sie `trigger: none` für kein CI.
- **Pro Commit überspringen**: Fügen Sie `[skip ci]` oder `***NO_CI***` zu Commit-Nachrichten hinzu.

### PR-Trigger
Für Pull Requests fügen Sie einen `pr`-Abschnitt hinzu:
```yaml
pr:
  branches:
    include:
    - main
    - develop
  paths:
    include:
    - src/*
```
- Dies validiert PRs, die auf diese Branches abzielen.

### Testen
- Pushen Sie auf einen passenden Branch: Die Pipeline wird automatisch ausgeführt.
- Sehen Sie sich die Läufe unter **Pipelines > Runs** an und prüfen Sie die Trigger-Details.

## Klassische Pipelines: Konfigurieren von Branch-Triggern
Für Legacy-/klassische Pipelines (UI-basiert):
1. Bearbeiten Sie Ihre Pipeline unter **Pipelines > Builds**.
2. Gehen Sie zu **Triggers > Continuous integration**.
3. Aktivieren Sie **Enable continuous integration**.
4. Fügen Sie unter **Branch filters** Includes (z.B. `main`) oder Excludes (z.B. `develop`) hinzu.
5. Für Pfade: Verwenden Sie **Path filters** in demselben Tab.
6. Für PRs: Gehen Sie zu **Triggers > Pull request validation** und setzen Sie Branch-Filter.

Wechseln Sie zu YAML für bessere Wartbarkeit.

## Best Practices
- Fangen Sie einfach an: Lösen Sie nur bei `main` und `develop` aus.
- Verwenden Sie Excludes für laute Branches wie `*-hotfix`.
- Sichern Sie mit Branch-Richtlinien (Repos > Branches > Policies) für erforderliche Reviewer.
- Überwachen Sie: Verwenden Sie Pipeline-Analysen für die Trigger-Häufigkeit.

Für die neuesten Details konsultieren Sie die offizielle Dokumentation.

[Build Azure Repos Git repositories](https://learn.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml)  
[Triggers in Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops&tabs=yaml)