---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: LibreChat-Einrichtung ohne Docker Compose
translated: true
type: note
---

Ja, Sie können LibreChat ohne Docker Compose einrichten, indem Sie einzelne `docker run`-Befehle oder sogar eine Nicht-Docker-Methode verwenden (manuelle Installation mit Node.js, Yarn, MongoDB und MeiliSearch). Dadurch umgehen Sie den Download der `docker-compose`-Binärdatei selbst (die klein ist, ~20-30 MB, aber ich nehme an, Sie beziehen sich auf die gesamten Image-Pulls, die sich auf ~70 MB+ für LibreChats Dienste summieren). Allerdings sind die Kern-Docker-Images (z.B. für die App, MongoDB, MeiliSearch) insgesamt immer noch etwa 500 MB-1 GB, wenn sie gepullt werden – Docker Compose ist nur ein Orchestrierungstool auf Docker aufgesetzt, nicht der Hauptverursacher des Bandbreitenverbrauchs. Das Pullen von Images über langsames 4G/5G wird immer noch der Engpass sein, aber Sie können ihn mildern.

Ich skizziere unten Optionen, wobei Bandbreiten-sparende Tipps priorisiert werden. Wenn Mobilfunkdaten sehr begrenzt sind, ziehen Sie in Betracht, vorübergehend ein WLAN-Netzwerk zu tethering oder ein vorher heruntergeladenes Setup auf einem anderen Rechner zu verwenden (z.B. Export/Import von Images via `docker save`/`docker load`).

### Bandbreiten-sparende Tipps für jedes Docker-basierte Setup
- **Images vorab auf einer schnelleren Verbindung pullen**: Führen Sie auf einem anderen Gerät mit besserem Internet `docker pull node:20-alpine` (für die App), `docker pull mongo:7` (Datenbank) und `docker pull getmeili/meilisearch:v1.10` (Suche) aus. Speichern Sie sie dann in Dateien:
  ```
  docker save -o librechat-app.tar node:20-alpine
  docker save -o mongo.tar mongo:7
  docker save -o meili.tar getmeili/meilisearch:v1.10
  ```
  Übertragen Sie die .tar-Dateien via USB/Laufwerk (insgesamt ~500-800 MB komprimiert), dann auf Ihrem Ubuntu-Rechner: `docker load -i librechat-app.tar` usw. Kein Online-Pulling nötig.
- **Leichtere Alternativen verwenden**: Überspringen Sie für Tests zunächst MeiliSearch (es ist optional für die Suche; in der Config deaktivieren). Das MongoDB-Image ist ~400 MB – verwenden Sie stattdessen eine lokale MongoDB-Installation (siehe Nicht-Docker-Abschnitt unten), um ~400 MB zu sparen.
- **Nutzung überwachen**: Verwenden Sie `docker pull --quiet` oder Tools wie `watch docker images` zur Verfolgung.
- **Proxy oder Cache**: Wenn Sie einen Docker Hub Spiegel oder Proxy haben, konfigurieren Sie ihn in `/etc/docker/daemon.json`, um Pulls zu beschleunigen.

### Option 1: Reines Docker (Ohne Compose) – Entspricht dem Compose-Setup
Sie können das Verhalten von `docker-compose.yml` mit `docker run` und `docker network` replizieren. Dies lädt die gleichen Images herunter, ermöglicht Ihnen aber, jeden Schritt zu kontrollieren. Der Gesamt-Download beträgt immer noch ~700 MB+ (App-Build + DBs).

1. **Ein Docker-Netzwerk erstellen** (isoliert Dienste):
   ```
   docker network create librechat-network
   ```

2. **MongoDB ausführen** (ersetzen Sie `your_mongo_key` mit einem starken Passwort):
   ```
   docker run -d --name mongodb --network librechat-network \
     -e MONGO_INITDB_ROOT_USERNAME=librechat \
     -e MONGO_INITDB_ROOT_PASSWORD=your_mongo_key \
     -v $(pwd)/data/mongodb:/data/db \
     mongo:7
   ```
   - Erstellt `./data/mongodb` für Persistenz.

3. **MeiliSearch ausführen** (ersetzen Sie `your_meili_key`):
   ```
   docker run -d --name meilisearch --network librechat-network \
     -e MEILI_MASTER_KEY=your_meili_key \
     -p 7700:7700 \
     -v $(pwd)/data/meili:/meili_data \
     getmeili/meilisearch:v1.10
   ```
   - Überspringen, wenn Bandbreite knapp ist; später in der App-Config deaktivieren.

4. **Die LibreChat-App klonen und bauen/ausführen**:
   - Repo klonen, falls nicht geschehen: `git clone https://github.com/danny-avila/LibreChat.git && cd LibreChat` (~50 MB Download für das Repo).
   - Das Image bauen (dies pulled die Node.js-Basis ~200 MB und baut App-Layer):
     ```
     docker build -t librechat-app .
     ```
   - Es ausführen (verbindet mit DB, verwendet Env-Vars – erstellen Sie eine `.env`-Datei wie in meiner vorherigen Antwort):
     ```
     docker run -d --name librechat --network librechat-network -p 3080:3080 \
       --env-file .env \
       -v $(pwd):/app \
       librechat-app
     ```
     - In `.env` setzen: `MONGODB_URI=mongodb://librechat:your_mongo_key@mongodb:27017/LibreChat` und `MEILI_HOST=http://meilisearch:7700` usw.

5. **Zugriff**: `http://localhost:3080`. Logs: `docker logs -f librechat`.

- **Stoppen/Bereinigen**: `docker stop mongodb meilisearch librechat && docker rm them`.
- **Vor-/Nachteile**: Gleich wie Compose, aber manueller. Immer noch datenintensiv für Image-Pulls/Builds.

### Option 2: Nicht-Docker-Installation (Manuell, Keine Image-Pulls) – Empfohlen bei geringer Bandbreite
Installieren Sie die Abhängigkeiten nativ auf Ubuntu. Dies vermeidet den gesam Docker-Overhead (~0 MB für Container; nur Paket-Downloads via apt/yarn, insgesamt ~200-300 MB). Nutzt die Python/Node-Setups Ihres Systems indirekt.

#### Voraussetzungen (Einmalig installieren)
```
sudo apt update
sudo apt install nodejs npm mongodb-org redis meilisearch git curl build-essential python3-pip -y  # MongoDB offizielles Pkg; MeiliSearch ~50 MB Binärdatei
sudo systemctl start mongod redis meilisearch
sudo systemctl enable mongod redis meilisearch
```
- Node.js: Falls nicht v20+, installieren via nvm: `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`, dann `nvm install 20`.
- Yarn: `npm install -g yarn`.
- MongoDB config: Bearbeiten Sie `/etc/mongod.conf`, um an localhost zu binden, neu starten.

#### Installationsschritte
1. **Repo klonen**:
   ```
   cd ~/projects
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **Abhängigkeiten installieren**:
   ```
   yarn install  # ~100-200 MB Downloads für Pakete
   ```

3. **`.env` konfigurieren** (kopieren von `.env.example`):
   - `cp .env.example .env && nano .env`
   - Wichtige Änderungen:
     - Mongo: `MONGODB_URI=mongodb://localhost:27017/LibreChat` (DB-Benutzer bei Bedarf via `mongo` Shell erstellen).
     - Meili: `MEILI_HOST=http://localhost:7700` und `MEILI_MASTER_KEY=your_key`.
     - Suche deaktivieren, wenn Meili übersprungen wird: `SEARCH=false`.
     - AI-Schlüssel nach Bedarf hinzufügen.

4. **Bauen und Ausführen**:
   - In einem Terminal: `yarn run backend` (startet API auf Port 3090).
   - In einem anderen: `yarn run frontend` (startet UI auf Port 3080).
   - Oder PM2 für die Produktion verwenden: `yarn global add pm2 && pm2 start yarn --name backend -- run backend` usw.

5. **Zugriff**: `http://localhost:3080`. Konto erstellen und konfigurieren.

- **Daten**: MongoDB speichert in `/var/lib/mongodb`, Meili in `/var/lib/meilisearch`.
- **Fehlerbehebung**:
  - Mongo Auth: `mongo` ausführen und Benutzer erstellen: `use LibreChat; db.createUser({user: 'librechat', pwd: 'yourpass', roles: ['readWrite']})`.
  - Ports/Firewall: `sudo ufw allow 3080,3090,7700`.
  - Updates: `git pull && yarn install && Dienste neu starten`.
- **Vorteile**: Schont die Bandbreite (keine Container), nutzt Systemressourcen direkt. Nachteile: Mehr Einrichtungsaufwand, potenzielle Abhängigkeitskonflikte (z.B. mit Ihrem Python 3.13, aber Node ist separat).

Wenn Mobilfunkdaten extrem begrenzt sind, ist die Nicht-Docker-Methode am besten – führen Sie sie in Etappen durch und überwachen Sie mit `du -sh` in Verzeichnissen. Bei Fehlern teilen Sie die Logs mit (z.B. von `yarn run backend`). Offizielle Nicht-Docker-Anleitung: https://docs.librechat.ai/install/installation/manual_install.html. Wenn Sie Ollama-Integration für lokale KI benötigen (spart API-Kosten), installieren Sie es separat über deren Skript (~100 MB). Lassen Sie mich bei Anpassungen wissen!