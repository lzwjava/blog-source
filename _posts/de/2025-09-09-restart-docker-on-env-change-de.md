---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Docker-Container nach Umgebungsänderung neu starten
translated: true
type: note
---

Wenn Sie `.env` ändern, lädt Docker diese Umgebungsvariablen nicht automatisch neu. Sie müssen die Container neu starten, damit sie die neuen Werte übernehmen. Für Ihr LibreChat-Setup können Sie dies wie folgt tun:

1. Stellen Sie sicher, dass Sie sich im selben Verzeichnis wie Ihre `docker-compose.yml`-Datei befinden.
2. Führen Sie aus:

```bash
docker compose down
docker compose up -d
```

Dadurch werden die laufenden Container gestoppt und entfernt und dann mit den neuen `.env`-Werten neu erstellt.

---

### Alternative: Nur Neustart

Wenn Sie nicht alles vollständig herunterfahren möchten, können Sie die Container zwingen, die neuen Umgebungsvariablen zu übernehmen, indem Sie sie neu erstellen:

```bash
docker compose up -d --force-recreate
```

Oder wenn Sie auch Dockerfiles oder Abhängigkeiten geändert haben, fügen Sie `--build` hinzu:

```bash
docker compose up -d --build
```

---

✅ Kurz gesagt:

* Nach dem Bearbeiten von `.env` sollten Sie die Container immer **neu erstellen** (`down` + `up` oder `up --force-recreate`).
* Ein einfacher `docker compose restart` lädt die neuen Umgebungsvariablen nicht neu, er startet nur mit den alten Werten neu.

Möchten Sie auch, dass ich Ihnen zeige, wie Sie **überprüfen** können, ob Ihre LibreChat-Container die neuen Umgebungsvariablen verwenden (z.B. mit `docker inspect` oder `docker exec env`)?