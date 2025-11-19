---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: GitHub Actions Cron Utilise l'Heure UTC
translated: true
type: note
---

**Les workflows planifiés GitHub Actions (utilisant le déclencheur `on: schedule:` avec la syntaxe cron) interprètent toujours les heures cron en UTC (Temps Universel Coordonné).**

Il n'existe pas de support intégré pour spécifier un fuseau horaire différent directement dans le YAML du workflow. Si vous souhaitez qu'une tâche s'exécute à une heure locale spécifique (par exemple, 9h00 PST), vous devez la convertir en heure UTC équivalente et écrire l'expression cron en conséquence.

### Points clés de la documentation officielle :
- Les workflows planifiés utilisent la syntaxe cron POSIX et s'exécutent à des **heures UTC** spécifiques.
- Exemple : `cron: '0 5 * * *'` s'exécute quotidiennement à 5h00 UTC (et non à votre heure locale).

Ce comportement est constant depuis des années et reste d'actualité fin 2025 — aucun paramètre de fuseau horaire natif n'existe pour l'événement `schedule` (contrairement à certaines autres fonctionnalités GitHub comme Dependabot).

[Événements qui déclenchent des workflows - Documentation GitHub](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule)  
[Syntaxe de workflow pour GitHub Actions - Documentation GitHub](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on-schedule)