---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Installation von LibreChat auf Ubuntu
translated: true
type: note
---

### Installation von LibreChat auf Ubuntu 24.04 LTS

LibreChat ist eine Open-Source-KI-Chat-Plattform, die mehrere KI-Modelle (z.B. OpenAI, Gemini, Ollama) über eine Weboberfläche unterstützt. Die empfohlene Installationsmethode ist die Verwendung von Docker Compose, da sie einfach ist, Abhängigkeiten wie MongoDB und MeiliSearch automatisch handhabt und zuverlässig auf Ubuntu funktioniert. Ihr System (Ubuntu 24.04.2 LTS mit Python 3.13.4) erfüllt die Anforderungen, aber Sie müssen zuerst Docker und Git installieren.

#### Voraussetzungen
1. **Aktualisieren Sie Ihr System**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Installieren Sie Git** (falls noch nicht installiert):
   ```
   sudo apt install git -y
   ```

3. **Installieren Sie Docker und Docker Compose**:
   - Installieren Sie Docker:
     ```
     sudo apt install docker.io -y
     sudo systemctl start docker
     sudo systemctl enable docker
     sudo usermod -aG docker $USER
     ```
     Melden Sie sich ab und wieder an (oder führen Sie `newgrp docker` aus), damit die Gruppenänderungen wirksam werden.
   - Installieren Sie Docker Compose (neueste Version):
     ```
     sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```
     Überprüfen Sie die Installation mit `docker-compose --version`.

#### Installationsschritte
1. **Klonen Sie das LibreChat-Repository**:
   ```
   cd ~/projects  # Oder Ihr bevorzugtes Verzeichnis
   git clone https://github.com/danny-avila/LibreChat.git
   cd LibreChat
   ```

2. **Kopieren und konfigurieren Sie die Umgebungsdatei**:
   - Kopieren Sie die Beispiel-Datei:
     ```
     cp .env.example .env
     ```
   - Bearbeiten Sie `.env` mit einem Texteditor (z.B. `nano .env`). Wichtige Einstellungen, die zu aktualisieren sind:
     - Setzen Sie einen MongoDB-Hauptschlüssel: Generieren Sie ein starkes Passwort und setzen Sie `MONGODB_URI=mongodb://mongodb:27017/LibreChat?authSource=admin` und `MONGODB_MASTER_KEY=Ihr_generierter_Schluessel_hier`.
     - Für MeiliSearch: Setzen Sie `MEILI_MASTER_KEY=Ihr_generierter_Schluessel_hier` (generieren Sie einen starken Schlüssel).
     - Fügen Sie bei Bedarf KI-API-Schlüssel hinzu (z.B. `OPENAI_API_KEY=Ihr_openai_schluessel`). Für lokale Modelle wie Ollama ist zunächst kein Schlüssel erforderlich.
     - Speichern Sie und beenden Sie den Editor. Für alle Konfigurationsoptionen lesen Sie bitte die Dokumentation.

3. **Starten Sie LibreChat mit Docker Compose**:
   ```
   docker-compose up -d
   ```
   - Dies lädt die Images, startet die Dienste (LibreChat-App, MongoDB, MeiliSearch) und führt sie im getrennten Modus aus.
   - Warten Sie, bis es vollständig gestartet ist (überprüfen Sie mit `docker-compose logs -f`).

4. **Greifen Sie auf LibreChat zu**:
   - Öffnen Sie Ihren Browser und gehen Sie zu `http://localhost:3080`.
   - Erstellen Sie ein Konto auf der Anmeldeseite.
   - Wählen Sie ein KI-Modell aus (konfigurieren Sie Endpunkte in den Einstellungen) und beginnen Sie zu chatten.

#### Tipps nach der Installation
- **Stoppen/Aktualisieren**: Führen Sie `docker-compose down` aus, um zu stoppen, dann `git pull` und `docker-compose up -d --build`, um zu aktualisieren.
- **Datenpersistenz**: Volumes werden automatisch für MongoDB-Daten erstellt (in `./data/mongodb`).
- **Fehlerbehebung**:
  - Bei Port-Konflikten bearbeiten Sie `docker-compose.yml`, um `3080:3080` zu ändern.
  - Für Headless-/Server-Zugriff verwenden Sie die IP Ihres Servers (z.B. `http://Ihre-Server-IP:3080`) und stellen Sie sicher, dass die Firewall Port 3080 erlaubt (`sudo ufw allow 3080`).
  - Wenn Sie lokale LLMs verwenden, installieren Sie Ollama separat und fügen Sie es als Endpunkt in `.env` hinzu.
- **Alternative: NPM-Methode** (ohne Docker): Wenn Sie bevorzugen, installieren Sie Node.js 18+, Yarn, MongoDB und MeiliSearch manuell und führen Sie dann `yarn install` und `yarn run frontend` + `yarn run backend` aus. Aber Docker wird dringend für die Einfachheit empfohlen.

Dies sollte Sie schnell zum Laufen bringen. Wenn Sie auf Fehler stoßen, teilen Sie die Ausgabe für weitere Hilfe!

[LibreChat Offizielle Dokumentation](https://docs.librechat.ai/install/installation/docker_compose.html)  
[Ubuntu Docker-Anleitung](https://docs.librechat.ai/install/installation/docker_ubuntu.html)  
[It's FOSS Tutorial](https://itsfoss.com/librechat-linux/)