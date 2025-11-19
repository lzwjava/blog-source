---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: GitHub Actions Cron verwendet UTC-Zeit
translated: true
type: note
---

**GitHub Actions geplante Workflows (die den `on: schedule:`-Trigger mit Cron-Syntax verwenden) interpretieren die Cron-Zeiten immer in UTC (Koordinierte Weltzeit).**

Es gibt keine integrierte Unterstützung, um direkt in der Workflow-YAML eine andere Zeitzone anzugeben. Wenn ein Job zu einer bestimmten Ortszeit ausgeführt werden soll (z. B. 9:00 Uhr PST), müssen Sie diese in die entsprechende UTC-Zeit umrechnen und den Cron-Ausdruck entsprechend schreiben.

### Wichtige Punkte aus der offiziellen Dokumentation:
- Geplante Workflows verwenden die POSIX-Cron-Syntax und laufen zu bestimmten **UTC-Zeiten**.
- Beispiel: `cron: '0 5 * * *'` wird täglich um 5:00 Uhr UTC ausgeführt (nicht zu Ihrer Ortszeit).

Dies ist seit Jahren konsistent und bleibt auch Ende 2025 der Fall – es existiert kein nativer Zeitzonen-Parameter für das `schedule`-Event (im Gegensatz zu einigen anderen GitHub-Features wie Dependabot).

[Events that trigger workflows - GitHub Docs](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)  
[Workflow syntax for GitHub Actions - GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)