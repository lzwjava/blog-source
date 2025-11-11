---
audio: false
generated: true
lang: de
layout: post
title: Erstellen und Bereitstellen eines Docker-Images
translated: true
type: note
---

Hier ist eine Schritt-für-Schritt-Anleitung zum Erstellen eines Spring Boot-Applications in ein Docker-Image und zur Bereitstellung auf einem Server:

### Voraussetzungen
1. **Java** (z.B. JDK 17 oder eine kompatible Version) lokal installiert.
2. **Maven** oder **Gradle** (abhängig von Ihrem Spring Boot-Projekt-Setup).
3. **Docker** auf Ihrem lokalen Rechner und dem Server installiert.
4. **Ein Spring Boot-Projekt**, das containerisiert werden kann.
5. **Server-Zugriff** (z.B. via SSH) mit installiertem Docker.

---

### Schritt 1: Bereiten Sie Ihre Spring Boot-Anwendung vor
Stellen Sie sicher, dass Ihre Spring Boot-Anwendung lokal funktioniert. Testen Sie sie mit:
```bash
mvn spring-boot:run  # Bei Verwendung von Maven
# ODER
gradle bootRun       # Bei Verwendung von Gradle
```

Stellen Sie sicher, dass die Anwendung erfolgreich gebaut wird:
```bash
mvn clean package    # Maven
# ODER
gradle build         # Gradle
```
Dies generiert eine `.jar`-Datei (z.B. `target/myapp-1.0.0.jar`).

---

### Schritt 2: Erstellen Sie ein Dockerfile
Erstellen Sie im Stammverzeichnis Ihres Projekts (wo sich die `.jar`-Datei befindet) eine Datei namens `Dockerfile` mit folgendem Inhalt:

```dockerfile
# Verwenden Sie ein offizielles OpenJDK-Runtime-Image als Basis-Image
FROM openjdk:17-jdk-slim

# Legen Sie das Arbeitsverzeichnis im Container fest
WORKDIR /app

# Kopieren Sie die Spring Boot JAR-Datei in den Container
COPY target/myapp-1.0.0.jar app.jar

# Machen Sie den Port zugänglich, auf dem Ihre Spring Boot-App läuft (Standard ist 8080)
EXPOSE 8080

# Führen Sie die JAR-Datei aus
ENTRYPOINT ["java", "-jar", "app.jar"]
```

**Hinweise:**
- Ersetzen Sie `myapp-1.0.0.jar` mit dem tatsächlichen Namen Ihrer JAR-Datei.
- Passen Sie die Java-Version (`openjdk:17-jdk-slim`) an, wenn Ihre App eine andere Version verwendet.

---

### Schritt 3: Bauen Sie das Docker-Image
Führen Sie im Verzeichnis, das das `Dockerfile` enthält, aus:
```bash
docker build -t myapp:latest .
```
- `-t myapp:latest` taggt das Image als `myapp` mit der Version `latest`.
- Der Punkt `.` weist Docker an, das aktuelle Verzeichnis als Build-Kontext zu verwenden.

Überprüfen Sie, ob das Image erstellt wurde:
```bash
docker images
```

---

### Schritt 4: Testen Sie das Docker-Image lokal
Führen Sie den Container lokal aus, um sicherzustellen, dass er funktioniert:
```bash
docker run -p 8080:8080 myapp:latest
```
- `-p 8080:8080` bildet Port 8080 auf Ihrem Rechner auf Port 8080 im Container ab.
- Öffnen Sie einen Browser oder verwenden Sie `curl` zum Testen (z.B. `curl http://localhost:8080`).

Stoppen Sie den Container mit `Strg+C` oder finden Sie seine ID mit `docker ps` und stoppen Sie ihn:
```bash
docker stop <container-id>
```

---

### Schritt 5: Übertragen Sie das Image in eine Docker Registry (Optional)
Um auf einem Server bereitzustellen, müssen Sie das Image in eine Registry wie Docker Hub (oder eine private Registry) übertragen. Wenn Sie dies überspringen, müssen Sie das Image manuell übertragen.

1. Melden Sie sich bei Docker Hub an:
   ```bash
   docker login
   ```
2. Taggen Sie Ihr Image:
   ```bash
   docker tag myapp:latest yourusername/myapp:latest
   ```
3. Übertragen Sie das Image:
   ```bash
   docker push yourusername/myapp:latest
   ```

---

### Schritt 6: Bereitstellung auf dem Server
#### Option 1: Verwendung einer Registry
1. SSH auf Ihren Server:
   ```bash
   ssh user@server-ip
   ```
2. Laden Sie das Image herunter:
   ```bash
   docker pull yourusername/myapp:latest
   ```
3. Führen Sie den Container aus:
   ```bash
   docker run -d -p 8080:8080 yourusername/myapp:latest
   ```
   - `-d` führt den Container im Detached Mode (Hintergrund) aus.

#### Option 2: Manuelle Übertragung
Falls Sie keine Registry verwendet haben:
1. Speichern Sie das Image lokal als `.tar`-Datei:
   ```bash
   docker save -o myapp.tar myapp:latest
   ```
2. Übertragen Sie es auf den Server (z.B. via SCP):
   ```bash
   scp myapp.tar user@server-ip:/path/to/destination
   ```
3. SSH auf den Server:
   ```bash
   ssh user@server-ip
   ```
4. Laden Sie das Image:
   ```bash
   docker load -i myapp.tar
   ```
5. Führen Sie den Container aus:
   ```bash
   docker run -d -p 8080:8080 myapp:latest
   ```

---

### Schritt 7: Überprüfen Sie die Bereitstellung
Prüfen Sie, ob der Container läuft:
```bash
docker ps
```

Testen Sie die App vom Server oder extern:
- Wenn auf dem Server: `curl http://localhost:8080`
- Wenn extern: Verwenden Sie die Server-IP (z.B. `http://server-ip:8080`), stellen Sie sicher, dass der Port in der Server-Firewall geöffnet ist.

---

### Optional: Verbesserungen
- **Umgebungsvariablen**: Übergeben Sie Konfigurationen an Ihre App:
  ```bash
  docker run -d -p 8080:8080 -e "SPRING_PROFILES_ACTIVE=prod" myapp:latest
  ```
- **Docker Compose**: Für Multi-Container-Setups verwenden Sie eine `docker-compose.yml`-Datei.
- **Neustart-Richtlinie**: Fügen Sie `--restart unless-stopped` hinzu, um sicherzustellen, dass der Container bei einem Server-Neustart wieder startet.

Lassen Sie mich wissen, wenn Sie Hilfe bei einem bestimmten Teil benötigen!

---

Anhand der von Ihnen bereitgestellten Fehlerausgabe gibt es einige Probleme, die Ihren `docker build`-Befehl verhindern. Lassen Sie uns diese aufschlüsseln und Schritt für Schritt beheben.

---

### Identifizierte Probleme
1. **Fehlendes `docker-buildx` Plugin**
   Fehler: `fork/exec /Users/lzwjava/.docker/cli-plugins/docker-buildx: no such file or directory`
   Dies deutet darauf hin, dass Docker versucht, das `buildx`-Plugin (ein modernes Build-Tool) zu verwenden, es aber nicht installiert oder korrekt konfiguriert ist.

2. **Veralteter Builder-Deprecation-Warnung**
   Warnung: `DEPRECATED: The legacy builder is deprecated...`
   Docker empfiehlt, auf BuildKit (`buildx`) umzusteigen, aber es fällt auf den veralteten Builder zurück, der fehlschlägt.

3. **Docker Daemon läuft nicht**
   Fehler: `Cannot connect to the Docker daemon at unix:///Users/lzwjava/.docker/run/docker.sock. Is the docker daemon running?`
   Der Docker-Daemon (der Hintergrunddienst, der Container verwaltet) läuft nicht auf Ihrem System.

4. **Dateizugriffsfehler**
   Fehler: `Can't add file ... to tar: io: read/write on closed pipe` und `Can't close tar writer...`
   Dies sind sekundäre Probleme, die dadurch verursacht werden, dass der Build-Prozess aufgrund des nicht laufenden Daemons fehlschlägt.

5. **Proxy-Einstellungen erkannt**
   Ihr System verwendet Proxys (`HTTP_PROXY` und `HTTPS_PROXY`). Dies könnte Docker beeinträchtigen, wenn es nicht korrekt konfiguriert ist.

---

### Schritt-für-Schritt-Fehlerbehebung

#### 1. Überprüfen Sie, ob der Docker-Daemon läuft
Das Kernproblem ist, dass der Docker-Daemon nicht läuft. So beheben Sie es:

- **Auf macOS** (angenommen, Sie verwenden Docker Desktop):
  1. Öffnen Sie Docker Desktop aus Ihrem Applications-Ordner oder Spotlight.
  2. Stellen Sie sicher, dass es läuft (Sie sehen das Docker-Wal-Symbol in der Menüleiste grün werden).
  3. Wenn es nicht startet:
     - Beenden Sie Docker Desktop und starten Sie es neu.
     - Prüfen Sie auf Updates: Docker Desktop > Nach Updates suchen.
     - Wenn es immer noch fehlschlägt, installieren Sie Docker Desktop von [docker.com](https://www.docker.com/products/docker-desktop/) neu.

- **Überprüfung via Terminal**:
  Führen Sie aus:
  ```bash
  docker info
  ```
  Wenn der Daemon läuft, sehen Sie Systeminformationen. Wenn nicht, erhalten Sie denselben "Cannot connect"-Fehler.

- **Daemon manuell neu starten** (falls nötig):
  ```bash
  sudo launchctl stop com.docker.docker
  sudo launchctl start com.docker.docker
  ```

Sobald der Daemon läuft, fahren Sie mit den nächsten Schritten fort.

---

#### 2. Installieren Sie das `buildx`-Plugin (Optional, aber empfohlen)
Da der veraltete Builder als deprecated markiert ist, richten wir `buildx` ein:

1. **Installieren Sie `buildx`**:
   - Laden Sie die Binärdatei manuell herunter oder befolgen Sie die Anweisungen von Docker:
     ```bash
     mkdir -p ~/.docker/cli-plugins
     curl -SL https://github.com/docker/buildx/releases/download/v0.13.0/buildx-v0.13.0.darwin-amd64 -o ~/.docker/cli-plugins/docker-buildx
     chmod +x ~/.docker/cli-plugins/docker-buildx
     ```
     (Überprüfen Sie die [neueste Version](https://github.com/docker/buildx/releases) für Ihr Betriebssystem/Architektur, z.B. `darwin-arm64` für M1/M2 Macs.)

2. **Installation überprüfen**:
   ```bash
   docker buildx version
   ```

3. **Setzen Sie BuildKit als Standard** (optional):
   Fügen Sie dies zu `~/.docker/config.json` hinzu:
   ```json
   {
     "features": { "buildkit": true }
   }
   ```

Alternativ können Sie dies überspringen und vorerst den veralteten Builder verwenden (siehe Schritt 4).

---

#### 3. Behandeln Sie die Proxy-Einstellungen
Ihre Proxy-Einstellungen (`http://127.0.0.1:7890`) könnten die Fähigkeit von Docker beeinträchtigen, Images abzurufen. Konfigurieren Sie Docker für deren Verwendung:

1. **Via Docker Desktop**:
   - Öffnen Sie Docker Desktop > Einstellungen > Resources > Proxies.
   - Aktivieren Sie "Manual proxy configuration" und geben Sie ein:
     - HTTP Proxy: `http://127.0.0.1:7890`
     - HTTPS Proxy: `http://127.0.0.1:7890`
   - Anwenden & Neustarten.

2. **Via CLI** (falls Desktop nicht verwendet wird):
   Erstellen oder bearbeiten Sie `~/.docker/config.json`:
   ```json
   {
     "proxies": {
       "default": {
         "httpProxy": "http://127.0.0.1:7890",
         "httpsProxy": "http://127.0.0.1:7890"
       }
     }
   }
   ```
   Starten Sie Docker nach der Bearbeitung neu.

---

#### 4. Wiederholen Sie den Build
Jetzt, da der Daemon läuft und die Proxys konfiguriert sind, versuchen Sie erneut zu bauen:

```bash
docker build -t myapp:latest .
```

- Wenn Sie `buildx` installiert haben, wird es standardmäßig BuildKit verwenden.
- Wenn Sie `buildx` übersprungen haben, fügen Sie `--progress=plain` hinzu, um den veralteten Builder zu erzwingen:
  ```bash
  docker build --progress=plain -t myapp:latest .
  ```

---

#### 5. Beheben Sie den `.git/hooks`-Fehler (falls er bestehen bleibt)
Der `.git/hooks/pre-rebase.sample`-Fehler deutet darauf hin, dass Docker versucht, unnötige Dateien in den Build-Kontext aufzunehmen. Schließen Sie sie mit einer `.dockerignore`-Datei aus:

1. Erstellen Sie `.dockerignore` im selben Verzeichnis wie Ihr `Dockerfile`:
   ```
   .git
   .gitignore
   *.md
   target/*
   !target/*.jar
   ```
2. Dies weist Docker an, den `.git`-Ordner und alles in `target/` außer Ihrer JAR-Datei zu ignorieren.

3. Wiederholen Sie den Build:
   ```bash
   docker build -t myapp:latest .
   ```

---

### Finale Überprüfung
- Überprüfen Sie das Image:
  ```bash
  docker images
  ```
- Führen Sie es lokal aus:
  ```bash
  docker run -p 8080:8080 myapp:latest
  ```
- Testen Sie mit `curl http://localhost:8080`.

---

### Nächste Schritte
Sobald das Image erfolgreich gebaut wurde, befolgen Sie die Bereitstellungsschritte aus meiner vorherigen Antwort (z.B. Übertragung in eine Registry oder manuelle Übertragung auf einen Server). Lassen Sie mich wissen, wenn Sie auf weitere Probleme stoßen!