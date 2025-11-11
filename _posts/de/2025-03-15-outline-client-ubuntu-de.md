---
audio: false
generated: true
lang: de
layout: post
title: Installation des Outline Clients unter Ubuntu
translated: true
type: note
---

Ja, Sie können den Outline Client auf Ubuntu installieren, da es sich um eine Debian-basierte Linux-Distribution handelt und der Outline Client als Debian-Paket bereitgestellt wird, das mit Ubuntu kompatibel ist. Es gibt zwei Installationsmethoden: die empfohlene Methode unter Verwendung des Repositorys und eine alternative Methode durch direkten Download des Debian-Pakets. Im Folgenden wird erläutert, wie Sie dies mit der empfohlenen Repository-Methode durchführen, die vorzuziehen ist, da sie in den Paketmanager von Ubuntu integriert wird und Updates einfacher zu verwalten sind.

### Schritte zur Installation des Outline Clients unter Ubuntu (Empfohlene Methode)

Befolgen Sie diese Schritte, um den Outline Client auf Ihrem Ubuntu-System zu installieren:

1. **Öffnen Sie ein Terminal**  
   Starten Sie die Terminal-Anwendung auf Ihrem Ubuntu-System. Sie können dies tun, indem Sie im Anwendungsmenü nach "Terminal" suchen oder `Strg + Alt + T` drücken.

2. **Installieren Sie den Repository-Schlüssel von Outline**  
   Führen Sie den folgenden Befehl aus, um den Signaturschlüssel des Repositorys herunterzuladen und zu den vertrauenswürdigen Schlüsseln Ihres Systems hinzuzufügen. Dies stellt sicher, dass Pakete aus dem Repository auf Authentizität überprüft werden:
   ```bash
   wget -qO- https://us-apt.pkg.dev/doc/repo-signing-key.gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/gcloud-artifact-registry-us.gpg
   ```

3. **Fügen Sie das Outline Client Repository hinzu**  
   Fügen Sie das Outline Client Repository zur Quellenliste Ihres Systems hinzu, indem Sie diesen Befehl ausführen. Dies teilt Ubuntu mit, wo es das Outline Client Paket finden kann:
   ```bash
   echo "deb [arch=amd64] https://us-apt.pkg.dev/projects/jigsaw-outline-apps outline-client main" | sudo tee /etc/apt/sources.list.d/outline-client.list
   ```
   - Hinweis: Der Teil `[arch=amd64]` gibt an, dass dies für 64-Bit-Systeme ist. Die meisten modernen Ubuntu-Installationen sind 64-Bit, aber Sie können die Architektur Ihres Systems mit `uname -m` überprüfen. Wenn die Ausgabe `x86_64` lautet, verwenden Sie ein 64-Bit-System und dieser Befehl funktioniert wie angegeben.

4. **Aktualisieren Sie die Paketliste**  
   Aktualisieren Sie die Paketliste Ihres Systems, um das neu hinzugefügte Outline Repository einzubeziehen:
   ```bash
   sudo apt update
   ```

5. **Installieren Sie den Outline Client**  
   Installieren Sie die neueste Version des Outline Clients mit diesem Befehl:
   ```bash
   sudo apt install outline-client
   ```

### Nach der Installation

- **Starten des Outline Clients**: Nach der Installation finden Sie den Outline Client im Anwendungsmenü oder starten ihn vom Terminal aus durch Eingabe von `outline-client`.
- **Aktualisieren**: Um nach Updates zu suchen und diese zu installieren, verwenden Sie die standardmäßigen Update-Befehle von Ubuntu:
  ```bash
  sudo apt update
  sudo apt upgrade
  ```
  Diese Befehle aktualisieren alle installierten Pakete, einschließlich des Outline Clients, da er über das Repository verwaltet wird. Beachten Sie, dass automatische In-App-Updates für den Outline Client unter Linux ab Version 1.15 deaktiviert sind, daher ist die Verwendung des Paketmanagers der beste Weg, um auf dem neuesten Stand zu bleiben.
- **Deinstallation**: Wenn Sie den Outline Client entfernen müssen, führen Sie aus:
  ```bash
  sudo apt purge outline-client
  ```

### Warum die empfohlene Methode verwenden?

Die Repository-Methode wird empfohlen, weil:
- Sie in den `apt`-Paketmanager von Ubuntu integriert ist, sodass Sie den Outline Client zusammen mit anderen Systempaketen aktualisieren können.
- Sie keine neuen Versionen manuell herunterladen und installieren müssen, anders als bei der alternativen Methode, bei der Sie den Download- und Installationsvorgang für jedes Update wiederholen müssten.

### Voraussetzungen

- **Ubuntu-Version**: Die Anweisungen geben keine minimale Ubuntu-Version an, aber da Ubuntu Debian-basiert ist und das Paket auf 64-Bit-Systeme abzielt, sollte jede aktuelle 64-Bit Ubuntu-Version funktionieren. Stellen Sie zur Sicherheit sicher, dass Ihr System aktuell ist, indem Sie vor Beginn `sudo apt update && sudo apt upgrade` ausführen.
- **Architektur**: Diese Anweisungen gehen von einem 64-Bit-System (amd64) aus. Wenn Sie eine andere Architektur verwenden (z.B. 32-Bit oder ARM), funktioniert diese Methode wie angegeben nicht, und Sie müssten nach alternativen Paketen suchen oder den Outline Support kontaktieren.

### Alternative Methode (Optional)

Wenn Sie kein Repository hinzufügen möchten, können Sie das Debian-Paket direkt herunterladen und installieren:
1. Laden Sie das Paket herunter:
   ```bash
   wget -O ./outline-client.deb https://s3.amazonaws.com/outline-releases/client/linux/stable/outline-client_amd64.deb
   ```
2. Installieren Sie es:
   ```bash
   sudo apt install ./outline-client.deb
   ```
Allerdings müssen Sie diesen Prozess für Updates manuell wiederholen, was weniger komfortabel ist.

### Fazit

Mit der empfohlenen Repository-Methode können Sie den Outline Client einfach auf Ubuntu installieren und warten. Befolgen Sie einfach die oben genannten Schritte, und Sie werden ihn einsatzbereit haben, wobei Sie ihn mühelos über den Systempaketmanager auf dem neuesten Stand halten können.