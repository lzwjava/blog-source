---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Déploiement en Production Gunicorn
translated: true
type: note
---

Gunicorn (Green Unicorn) est un serveur HTTP WSGI populaire pour les applications web Python. Il est largement utilisé en production pour servir des applications construites avec des frameworks comme Flask, Django, FastAPI, ou toute application conforme WSGI. Contrairement aux serveurs de développement (par exemple, le serveur intégré de Flask), Gunicorn est robuste, efficace et conçu pour un déploiement réel.

---

## Qu'est-ce que WSGI ?

**WSGI** (Web Server Gateway Interface) est un standard Python (PEP 333) qui définit comment les serveurs web communiquent avec les applications web Python. Gunicorn agit comme un serveur WSGI — il reçoit les requêtes HTTP des clients (via un proxy inverse comme Nginx) et les transmet à votre application Python.

```
Client → Nginx (proxy inverse) → Gunicorn → Votre application WSGI (par ex. Flask/Django)
```

---

## Pourquoi utiliser Gunicorn ?

| Fonctionnalité | Avantage |
|-------|--------|
| **Prêt pour la production** | Gère efficacement de multiples requêtes concurrentes |
| **Modèles de workers** | Prend en charge les workers sync, async, threading et gevent |
| **Modèle pre-fork** | Lance des processus workers pour traiter les requêtes en parallèle |
| **Rechargement sans interruption** | Redémarrages gracieux avec `SIGHUP` |
| **Intégration** | Fonctionne parfaitement avec Nginx, systemd, Docker |

> **Remarque** : Gunicorn ne sert **pas** efficacement les fichiers statiques — utilisez Nginx ou un CDN pour cela.

---

## Installation

```bash
pip install gunicorn
```

Pour le support async :
```bash
pip install gunicorn[gevent]    # ou [eventlet], [tornado]
```

---

## Utilisation de base

### Ligne de commande

```bash
gunicorn [OPTIONS] NOM_MODULE:NOM_VARIABLE
```

Exemple avec Flask :
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 run:app
```

- `run:app` → fichier `run.py`, `app` est l'instance Flask/FastAPI
- `--workers 3` → 3 processus workers
- `--bind 0.0.0.0:8000` → écouter sur toutes les interfaces, port 8000

---

## Types de Workers

Gunicorn prend en charge différentes classes de workers selon les besoins de votre application :

| Type de Worker | Commande | Cas d'utilisation |
|-----------|--------|---------|
| **sync** (par défaut) | `gunicorn -k sync` | Applications liées au CPU ou simples |
| **gevent** | `gunicorn -k gevent` | Haute concurrence, forte intensité d'E/S (par ex. APIs, websockets) |
| **eventlet** | `gunicorn -k eventlet` | Similaire à gevent, bon pour l'async |
| **tornado** | `gunicorn -k tornado` | Applications en temps réel |
| **threads** | `gunicorn -k sync --threads 4` | E/S + CPU mixtes, mais attention au GIL |

> **Recommandation** : Utilisez `gevent` ou `eventlet` pour la plupart des APIs web.

---

## Options de configuration clés

| Option | Description | Exemple |
|------|-------------|--------|
| `--bind` | Hôte et port | `--bind 0.0.0.0:8000` |
| `--workers` | Nombre de processus workers | `--workers 4` |
| `--worker-class` | Type de worker | `-k gevent` |
| `--threads` | Threads par worker sync | `--threads 2` |
| `--timeout` | Time