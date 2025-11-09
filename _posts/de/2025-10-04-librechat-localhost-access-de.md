---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Fehlerbehebung beim Zugriff auf LibreChat Localhost
translated: true
type: note
---

### Fehlerbehebung beim Zugriff auf LibreChat unter localhost:3080

Laut Ihren Logs wurden die Docker-Images erfolgreich gepullt (nach anfänglichen Timeouts und Wiederholungsversuchen), und 6 Komponenten wurden gestartet: das Standard-Netzwerk, `vectordb`, `chat-mongodb`, `chat-meilisearch`, `rag_api` und `LibreChat`. Der `api`-Service (der typischerweise das Backend auf Port 3080 bereitstellt) wird jedoch nicht in der Liste der gestarteten Container aufgeführt – das ist wahrscheinlich der Grund, warum Sie nicht auf die Seite zugreifen können. Der `LibreChat`-Container ist vermutlich das Frontend, welches vom `api`-Backend abhängt.

Die UID/GID-Warnungen deuten auf potenzielle Berechtigungsprobleme hin, die das Starten des `api`-Containers verhindern könnten. Hier ist eine Schritt-für-Schritt-Anleitung zur Diagnose und Behebung.

#### 1. **Überprüfen Sie die laufenden Container und Ports**
   Führen Sie diesen Befehl aus, um alle aktiven Container, deren Status und Port-Zuordnungen zu sehen:
   ```
   docker ps
   ```
   - Suchen Sie nach einem `api`-Container (er könnte `librechat_api` oder ähnlich heißen). Wenn er fehlt oder beendet ist, ist das das Problem.
   - Bestätigen Sie, ob Port `3080` gemappt ist (z.B. `0.0.0.0:3080->3080/tcp`). Wenn nicht, stellt der Service ihn nicht bereit.
   - Wenn kein Container Port 3080 anzeigt, fahren Sie mit den nächsten Schritten fort.

#### 2. **Überprüfen Sie die Container-Logs**
   Untersuchen Sie die Logs auf Fehler beim Start, insbesondere für die `api`- und `LibreChat`-Services:
   ```
   docker logs LibreChat
   docker logs api  # Oder docker logs librechat_api, falls anders benannt
   docker logs rag_api  # Für den Fall von Abhängigkeitsproblemen
   ```
   - Häufige Fehler: Permission denied (aufgrund von UID/GID), MongoDB/Meilisearch-Verbindungsfehler oder Bind-Probleme (z.B. nicht an 0.0.0.0 lauschend).
   - Wenn die Logs zeigen, dass der Server startet, aber nur an localhost innerhalb des Containers bindet, fügen Sie `HOST=0.0.0.0` zu Ihrer `.env`-Datei hinzu.

#### 3. **Setzen Sie UID und GID, um Berechtigungswarnungen zu beheben**
   Ihre `.env`-Datei (kopiert von `.env.example`) hat diese Variablen wahrscheinlich auskommentiert. Nicht gesetzte Variablen können dazu führen, dass Container aufgrund von Dateiberechtigungskonflikten stillschweigend fehlschlagen.
   - Bearbeiten Sie `.env`:
     ```
     UID=1000  # Führen Sie `id -u` aus, um Ihre Benutzer-ID zu erhalten
     GID=1000  # Führen Sie `id -g` aus, um Ihre Gruppen-ID zu erhalten
     ```
   - Speichern Sie und starten Sie dann neu:
     ```
     docker compose down
     docker compose up -d
     ```
   Dies stellt sicher, dass Volumes (wie config/logs) Ihrem Benutzer gehören.

#### 4. **Testen Sie die Konnektivität**
   - Prüfen Sie, ob Port 3080 lokal lauscht:
     ```
     curl -v http://localhost:3080
     ```
     - Wenn es zu einem Timeout oder Verbindungsabbruch kommt, läuft der Service nicht oder ist nicht exponiert.
   - Wenn `docker ps` den Port als gemappt anzeigt, aber curl fehlschlägt, prüfen Sie die Firewall (z.B. `sudo ufw status`) oder versuchen Sie `http://127.0.0.1:3080`.

#### 5. **Zusätzliche Behebungen falls nötig**
   - **Image Pull Probleme**: Ihr erster Versuch hatte einen "denied"-Fehler für `ghcr.io/v2/librechat/librechat/manifests/latest`. Wenn Pulls erneut fehlschlagen, authentifizieren Sie sich bei GitHub Container Registry:
     ```
     echo $YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
     ```
     (Erstellen Sie ein Personal Access Token unter github.com/settings/tokens mit `read:packages` Scope.)
   - **Verwenden Sie die empfohlene Compose-Datei**: Die Standard-`docker-compose.yml` ist für lokale Builds, die problematisch sein können. Wechseln Sie zu `deploy-compose.yml` für stabile Remote-Images:
     - Benennen Sie Ihre aktuelle `docker-compose.yml` um oder sichern Sie sie.
     - Verwenden Sie stattdessen `deploy-compose.yml`: `docker compose -f deploy-compose.yml up -d`.
     - Stellen Sie sicher, dass `.env` `HOST=0.0.0.0` und `NODE_ENV=production` enthält.
   - **Kompletter Neustart mit Prune**: Wenn nichts hilft, räumen Sie auf:
     ```
     docker compose down -v  # Entfernt auch Volumes
     docker system prune -f
     docker compose up -d
     ```
   - **Abhängigkeiten**: Bestätigen Sie, dass MongoDB und Meilisearch fehlerfrei laufen (`docker logs chat-mongodb`, etc.). Der `api`-Service hängt von ihnen ab.

Nach diesen Schritten versuchen Sie erneut, auf http://localhost:3080 zuzugreifen. Wenn die Logs spezifische Fehler anzeigen (z.B. Mongo-Verbindung), teilen Sie diese für gezieltere Hilfe mit. Dieses Setup funktioniert für die meisten Benutzer, sobald UID/GID und Abhängigkeiten korrekt eingerichtet sind.

[Local Docker Build Fails to Serve on localhost:3080](https://github.com/danny-avila/LibreChat/discussions/3425)  
[LibreChat Docker Docs](https://www.librechat.ai/docs/local/docker)  
[Env File Configuration (UID/GID)](https://www.librechat.ai/docs/configuration/dotenv)