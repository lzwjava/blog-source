---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast:free
title: Docker Compose Installation für Ubuntu
translated: true
type: note
---

Basierend auf Ihren Systeminformationen verwenden Sie **Ubuntu 24.04.2 LTS** auf einer **x86_64**-Architektur. Um die passende **Docker Compose**-Binärdatei für Ihr System von der bereitgestellten GitHub-Release (v2.39.4) herunterzuladen, sollten Sie die mit Linux auf x86_64 kompatible Binärdatei auswählen.

### Empfohlener Download
Sie sollten die **docker-compose-linux-x86_64**-Binärdatei herunterladen, die in den bereitgestellten Assets nicht explizit aufgeführt ist, aber in Docker Compose-Releases als Standardbinärdatei für Linux-x86_64-Systeme impliziert wird. Aus den aufgeführten Assets ist die passendste Option für Ihr System jedoch:

- **docker-compose-linux-aarch64** ist **nicht** geeignet, da es für die ARM64 (aarch64)-Architektur ist und Ihr System x86_64 ist.
- Die **darwin**-Binärdateien (z.B. `docker-compose-darwin-x86_64`) sind für macOS, nicht für Linux.
- Die Quellcode-Optionen (`Source code (zip)` oder `Source code (tar.gz)`) erfordern eine manuelle Kompilierung, was unnötig ist, da in der Regel eine vorkompilierte Binärdatei verfügbar ist.

Da die **docker-compose-linux-x86_64**-Binärdatei in Ihren bereitgestellten Assets nicht explizit aufgeführt ist, aber für Docker Compose-Releases standardmäßig vorhanden sein sollte, können Sie sie wahrscheinlich in der vollständigen Liste der Assets auf der GitHub-Release-Seite finden. Wenn sie nicht verfügbar ist, können Sie den Quellcode verwenden oder Docker Compose über eine alternative Methode installieren (z.B. über den Paketmanager oder pip).

### Schritte zum Herunterladen und Installieren
1. **Binärdatei bestätigen**: Besuchen Sie die GitHub-Release-Seite für v2.39.4, um die Verfügbarkeit von `docker-compose-linux-x86_64` zu bestätigen. Die Release-Seite befindet sich typischerweise unter:
   [Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)

2. **Binärdatei herunterladen**:
   Wenn `docker-compose-linux-x86_64` verfügbar ist, laden Sie es herunter. Zum Beispiel:
   ```bash
   curl -L "https://github.com/docker/compose/releases/download/v2.39.4/docker-compose-linux-x86_64" -o docker-compose
   ```

3. **Download verifizieren**:
   Verwenden Sie die bereitgestellte Prüfsumme, um die Integrität der heruntergeladenen Datei zu überprüfen. Wenn die Datei `docker-compose-linux-x86_64.sha256` verfügbar ist:
   ```bash
   echo "<sha256> docker-compose" | sha256sum --check
   ```
   Ersetzen Sie `<sha256>` durch den entsprechenden Hash aus den Release-Assets (z.B. `df7ff3dd8080134b851e1e49265028697d27de71f9bdc187e3d833357b934f36` für `docker-compose-darwin-x86_64.sha256`, aber Sie benötigen das Linux-Äquivalent).

4. **Binärdatei installieren**:
   Verschieben Sie die Binärdatei in ein Verzeichnis in Ihrem PATH, wie z.B. `/usr/local/bin`:
   ```bash
   chmod +x docker-compose
   sudo mv docker-compose /usr/local/bin/docker-compose
   ```

5. **Installation überprüfen**:
   Überprüfen Sie die installierte Version:
   ```bash
   docker-compose --version
   ```
   Die Ausgabe sollte `Docker Compose version v2.39.4` lauten.

### Alternative Installationsmethode
Wenn die `docker-compose-linux-x86_64`-Binärdatei nicht verfügbar ist oder Sie eine einfachere Methode bevorzugen, können Sie Docker Compose über den Paketmanager oder pip installieren, da auf Ihrem System Python 3.13.4 installiert ist:

#### Über Paketmanager (Empfohlen für Ubuntu)
Docker Compose ist oft in den Repositorys von Ubuntu oder dem offiziellen Docker-Repository verfügbar:
```bash
sudo apt update
sudo apt install docker-compose-plugin
```
Dies installiert das Docker Compose-Plugin, was die moderne Art ist, Docker Compose zu verwenden (als `docker compose` anstelle von `docker-compose`). Beachten Sie, dass die Version in Ubuntus Repository möglicherweise nicht exakt v2.39.4 entspricht. Überprüfen Sie dies mit:
```bash
docker compose version
```

#### Über pip (Python)
Da Sie Python 3.13.4 haben, können Sie Docker Compose über pip installieren:
```bash
pip3 install docker-compose==2.39.4
```
Dies installiert die spezifische Version. Verifizieren Sie mit:
```bash
docker-compose --version
```

### Hinweise
- Die Datei `checksums.txt` (SHA256: `1a9c3370b88825ab2b229bb90eda6f703d84018ea1d56b5ba573f8893c9ab6b4`) kann verwendet werden, um die Integrität der heruntergeladenen Dateien zu überprüfen.
- Wenn Sie sich entscheiden, aus dem Quellcode zu kompilieren (`Source code (zip)` oder `Source code (tar.gz)`), benötigen Sie Go (nicht in Ihren Systeminformationen aufgeführt) und zusätzliches Setup, was komplexer ist und nur bei Bedarf empfohlen wird.
- Das Release enthält Verbesserungen und Fehlerbehebungen (z.B. Unterstützung für `develop.watch.initial_sync`, volume ls ohne ein Projekt und TLS für bake), die relevant sind, wenn Sie diese Funktionen verwenden.

Wenn Sie Hilfe beim Finden der exakten `docker-compose-linux-x86_64`-Binärdatei benötigen oder auf Probleme stoßen, lassen Sie es mich wissen, ich kann Sie weiter unterstützen!

[Docker Compose v2.39.4 Release](https://github.com/docker/compose/releases/tag/v2.39.4)