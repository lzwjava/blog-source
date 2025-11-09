---
audio: false
date: 2025-09-09
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Konfiguration von OPENAI_REVERSE_PROXY in LibreChat
translated: true
type: note
---

Alles klar 👍 Du bearbeitest die `.env`-Datei von LibreChat.
Genau in dieser Datei setzt du `OPENAI_REVERSE_PROXY`.

---

### 1. Was die Variable bewirkt

`OPENAI_REVERSE_PROXY` wird verwendet, wenn du möchtest, dass LibreChat OpenAI-API-Anfragen über einen Proxy-Server leitet (zum Beispiel, wenn du einen selbst gehosteten Reverse-Proxy betreibst, um Logging, Caching, regionale Routing oder das Umgehen von Einschränkungen zu ermöglichen).

---

### 2. Wie man sie setzt

Weise ihr in deiner `.env`-Datei einfach die Basis-URL deines Reverse-Proxy zu. Zum Beispiel:

```ini
OPENAI_REVERSE_PROXY=https://dein-proxy.beispiel.com/v1
```

Hinweise:

* Die URL sollte auf deinen Proxy-Endpunkt zeigen, der die `/v1`-API von OpenAI nachbildet.
* Schließe keinen nachgestellten Schrägstrich (`/`) ein, es sei denn, dein Proxy erfordert dies.
* Lasse das Feld leer (`OPENAI_REVERSE_PROXY=`), wenn du keinen Proxy verwendest.

---

### 3. Änderungen übernehmen

Nach dem Bearbeiten der `.env`-Datei starte deine LibreChat-Container neu, damit sie den neuen Wert übernehmen:

```bash
docker compose down
docker compose up -d --force-recreate
```

---

### 4. Überprüfen

Du kannst dies im laufenden Container überprüfen:

```bash
docker compose exec librechat env | grep OPENAI_REVERSE_PROXY
```

Es sollte der von dir gesetzte Wert angezeigt werden.

---

Hast du bereits eine Reverse-Proxy-URL (wie `https://openrouter.ai/api/v1` oder deine eigene Nginx-Instanz), oder möchtest du, dass ich dir zeige, wie man einen **für LibreChat einrichtet**?