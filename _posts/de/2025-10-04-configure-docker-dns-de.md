---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Konfigurieren Sie DNS-Server für den Docker-Daemon
translated: true
type: note
---

Um DNS-Server für den Docker-Daemon zu konfigurieren (die von Containern verwendet werden, sofern nicht auf Container-Ebene überschrieben), können Sie die Datei `/etc/docker/daemon.json` bearbeiten. Diese Datei ermöglicht es Ihnen, das Laufzeitverhalten von Docker anzupassen.

### Schritte zur DNS-Konfiguration

1. **Die Datei daemon.json bearbeiten**:
   - Wenn die Datei nicht existiert, erstellen Sie sie mit Root-Rechten (z.B. mit `sudo nano /etc/docker/daemon.json` oder Ihrem bevorzugten Editor).
   - Fügen Sie den Schlüssel `dns` als Array von IP-Adressen für die DNS-Server hinzu oder aktualisieren Sie ihn. Um beispielsweise das öffentliche DNS von Google (8.8.8.8 und 8.8.4.4) zu verwenden:

     ```json
     {
       "dns": ["8.8.8.8", "8.8.4.4"]
     }
     ```

     - Sie können bei Bedarf weitere Server hinzufügen (z.B. Cloudflares 1.1.1.1).
     - Diese Einstellung gilt für alle Container, die mit dem Standardnetzwerk erstellt werden, sofern nicht anders angegeben.

2. **Die JSON-Datei validieren**:
   - Stellen Sie sicher, dass die Datei gültiges JSON ist. Sie können ein Tool wie `jq` zur Überprüfung verwenden: `jq . /etc/docker/daemon.json`. Bei Fehlern beheben Sie die Syntax.

3. **Den Docker-Dienst neu starten**:
   - Wenden Sie die Änderungen an, indem Sie Docker neu starten:
     ```
     sudo systemctl restart docker
     ```
     - Auf Nicht-systemd-Systemen (z.B. ältere Linux-Distributionen) verwenden Sie `sudo service docker restart`.
   - Überprüfen Sie den Status: `sudo systemctl status docker`.

4. **Die Konfiguration testen**:
   - Führen Sie einen Test-Container aus und prüfen Sie dessen DNS-Auflösung:
     ```
     docker run --rm busybox nslookup google.com
     ```
     - Die Auflösung sollte über Ihre konfigurierten DNS-Server erfolgen.

### Hinweise
- **Umfang**: Dies konfiguriert das DNS für den Docker-Daemon auf dem Host und beeinflusst die ausgehende Namensauflösung für Container. Es ändert nicht das systemweite DNS des Hosts.
- **Überschreibungen**: Wenn ein Container ein anderes DNS benötigt (z.B. über das `--dns`-Flag in `docker run`), überschreibt dies die Daemon-weite Einstellung.
- **Sicherheit**: Die Verwendung von öffentlichem DNS wie 8.8.8.8 ist in den meisten Fällen in Ordnung, aber erwägen Sie internes DNS für Unternehmensumgebungen.
- **Dokumentation**: Weitere Optionen (z.B. DNS-Suchdomänen) finden Sie in der [offiziellen Docker-Dokumentation zu daemon.json](https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file).

Wenn Sie Fehler encountern (z.B. Berechtigungsprobleme oder JSON-Parsing-Fehler), teilen Sie die Details für eine weitere Fehlerbehebung mit.