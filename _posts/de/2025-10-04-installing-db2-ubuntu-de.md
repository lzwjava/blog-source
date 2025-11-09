---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installation von IBM Db2 auf Ubuntu
translated: true
type: note
---

### Installation von IBM Db2 12.1.2 auf Ubuntu 22.04 oder 24.04 aus `ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz`

IBM Db2 Version 12.1.2 (Fix Pack 2) wird auf aktuellen Ubuntu-Versionen, einschließlich 22.04 (Jammy) und 24.04 (Noble), unterstützt, sofern Ihr System die Hardware- und Software-Voraussetzungen erfüllt. Diese Installation verwendet den grafischen oder stillen Installer aus der tar.gz-Datei. Ich empfehle, die offizielle IBM-Dokumentation für Db2 12.1 (z.B. im IBM Knowledge Center oder auf der Db2 Downloads-Seite) für die neuesten Details zu konsultieren, da die Anforderungen je nach Edition (hier Server Edition) variieren können.

**Wichtige Hinweise vor dem Start:**
- **Systemanforderungen**:
  - 64-Bit-x86_64-Architektur (Intel/AMD).
  - Mindestens 4 GB RAM (8 GB empfohlen) und 2 GB Swap-Speicher.
  - 10 GB freier Festplattenspeicher für die Basisinstallation (mehr für Daten).
  - Root- oder sudo-Zugriff.
  - Kernel-Version: Ubuntu 22.04/24.04 sollte funktionieren, aber stellen Sie sicher, dass Ihr Kernel mindestens Version 3.10 hat (prüfen mit `uname -r`).
  - Firewall: Vorübergehend deaktivieren oder Ports öffnen (Standard-Db2: 50000 für TCP/IP).
- **Mögliche Probleme unter Ubuntu**:
  - Db2 wird primär auf RHEL/SUSE getestet, aber Ubuntu wird über Debian-Pakete unterstützt. Sie müssen möglicherweise Bibliotheksabhängigkeiten auflösen.
  - Wenn Sie Ubuntu 24.04 verwenden, ist es sehr neu – testen Sie es zuerst in einer VM, da die vollständige Zertifizierung hinterherhinken könnte.
  - Hiermit wird die Server Edition installiert. Für andere Editionen (z.B. Express-C) laden Sie die entsprechende tar.gz-Datei herunter.
- **Backup**: Erstellen Sie ein Backup Ihres Systems, bevor Sie fortfahren.
- Laden Sie die Datei von der offiziellen IBM Passport Advantage oder Db2 Downloads-Seite herunter (erfordert eine IBM ID).

#### Schritt 1: Voraussetzungen installieren
Aktualisieren Sie Ihr System und installieren Sie die erforderlichen Bibliotheken. Db2 benötigt asynchrone I/O, PAM und andere Laufzeitbibliotheken.

```bash
sudo apt update
sudo apt upgrade -y

# Installieren Sie essentielle Pakete (üblich für Db2 auf Ubuntu/Debian)
sudo apt install -y libaio1 libpam0g:i386 libncurses5 libstdc++6:i386 \
    unixodbc unixodbc-dev libxml2 libxslt1.1 wget curl

# Für Ubuntu 24.04 benötigen Sie möglicherweise auch:
sudo apt install -y libc6:i386 libgcc-s1:i386

# Überprüfen Sie die glibc-Kompatibilität (Db2 12.1 erfordert glibc 2.17+)
ldd --version  # Sollte glibc 2.35+ auf Ubuntu 22.04/24.04 anzeigen
```

Wenn Sie fehlende 32-Bit-Bibliotheken feststellen (z.B. für Java-Komponenten), aktivieren Sie Multiarch:
```bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install -y libc6:i386 libncurses5:i386 libstdc++6:i386
```

#### Schritt 2: Installationsdateien vorbereiten
1. Erstellen Sie ein temporäres Verzeichnis für die Extraktion (z.B. `/tmp/db2_install`):
   ```bash
   sudo mkdir -p /tmp/db2_install
   cd /tmp/db2_install
   ```

2. Kopieren Sie die tar.gz-Datei in dieses Verzeichnis (angenommen, Sie haben sie heruntergeladen, z.B. in `~/Downloads`):
   ```bash
   cp ~/Downloads/ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz .
   ```

3. Extrahieren Sie das Archiv:
   ```bash
   tar -xzf ibm_db2_v12.1.2_linuxx64_server_dec.tar.gz
   ```
   - Dies erstellt ein Verzeichnis wie `db2` oder `sqllib`, das die Installer-Dateien (z.B. `db2setup`) enthält.

4. Wechseln Sie in das extrahierte Verzeichnis:
   ```bash
   cd db2  # Oder wie auch immer das oberste Verzeichnis heißt – prüfen Sie mit `ls`
   ```

#### Schritt 3: Installer ausführen
Db2 bietet einen grafischen Installer (`db2setup`) oder eine Antwortdatei für stille Installationen. Führen Sie ihn als root/sudo aus.

**Option A: Grafischer Installer (Empfohlen für das erste Setup)**
1. Stellen Sie sicher, dass Sie eine Anzeige haben (wenn Sie auf einem Server ohne GUI sind, verwenden Sie X-Forwarding mit SSH: `ssh -X user@host`).
2. Führen Sie den Installer aus:
   ```bash
   sudo ./db2setup
   ```
   - Der Assistent führt Sie durch:
     - Lizenzbedingungen akzeptieren.
     - Wählen Sie "Typical" Installation für die Server Edition.
     - Wählen Sie den Installationspfad (Standard: `/opt/ibm/db2/V12.1` – stellen Sie sicher, dass `/opt/ibm` existiert und beschreibbar ist; erstellen Sie es mit `sudo mkdir -p /opt/ibm` falls nötig).
     - Erstellen Sie eine Db2-Instanz (z.B. "db2inst1") – dies richtet den Datenbankadministrator-Benutzer ein.
     - Authentifizierung festlegen (z.B. lokal oder LDAP).
     - Funktionen wie SQL Procedural Language aktivieren, falls benötigt.
   - Der Installer kompiliert und richtet die Instanz ein.

**Option B: Stille Installation (Nicht-interaktiv)**
Wenn Sie Skripte bevorzugen:
1. Generieren Sie eine Antwortdatei während eines Probelaufs:
   ```bash
   sudo ./db2setup -g  # Generiert `db2setup.rsp` im aktuellen Verzeichnis
   ```
   Bearbeiten Sie `db2setup.rsp` (z.B. setzen Sie `LIC_AGREEMENT=ACCEPT`, `INSTALL_TYPE=TYPICAL`, `CREATE_DB2_INSTANCE=YES`, etc.).

2. Führen Sie die stille Installation aus:
   ```bash
   sudo ./db2setup -u db2setup.rsp
   ```

- Die Installation dauert 10-30 Minuten. Achten Sie auf Fehler in `/tmp/db2setup.log`.

#### Schritt 4: Einrichtung nach der Installation
1. **Installation überprüfen**:
   - Melden Sie sich als Instanz-Besitzer an (z.B. `db2inst1` – während der Installation erstellt):
     ```bash
     su - db2inst1
     ```
   - Überprüfen Sie die Db2-Version:
     ```bash
     db2level
     ```
   - Starten Sie die Instanz:
     ```bash
     db2start
     ```
   - Verbindung testen:
     ```bash
     db2 connect to sample  # Erstellt eine Beispiel-DB, falls keine existiert
     db2 "select * from sysibm.sysdummy1"
     db2 disconnect all
     db2stop  # Wenn fertig
     ```

2. **Datenbank erstellen (falls nicht während der Installation geschehen)**:
   ```bash
   su - db2inst1
   db2sampl  # Optional: Erstellt Beispiel-DB
   # Oder erstellen Sie eine benutzerdefinierte DB:
   db2 "create database MYDB"
   db2 connect to MYDB
   ```

3. **Umgebung einrichten**:
   - Fügen Sie Db2 zum PATH für den Instanz-Benutzer hinzu (fügen Sie zu `~/.bashrc` hinzu):
     ```bash
     export PATH=/opt/ibm/db2/V12.1/bin:$PATH
     export DB2INSTANCE=db2inst1
     ```
   - Neu laden: `source ~/.bashrc`.

4. **Fernzugriff aktivieren (Optional)**:
   - Dienste aktualisieren:
     ```bash
     su - db2inst1
     db2 update dbm cfg using SVCENAME db2i  # Oder Ihren Port
     db2set DB2COMM=TCPIP
     db2start
     ```
   - Bearbeiten Sie `/etc/services` (als root) und fügen Sie hinzu:
     ```
     db2i          50000/tcp
     ```
   - Starten Sie die Instanz neu.

5. **Firewall-Konfiguration**:
   ```bash
   sudo ufw allow 50000/tcp  # Für Db2 Standard-Port
   sudo ufw reload
   ```

#### Schritt 5: Updates anwenden (Empfohlen)
- Laden Sie das neueste Fix Pack herunter und wenden Sie es an, falls benötigt (12.1.2 ist FP2; prüfen Sie auf FP3+):
  - Verwenden Sie das `db2iupdt`-Tool oder den IBM Update Installer.
- Überwachen Sie Logs: `/tmp/db2` oder `/opt/ibm/db2/V12.1/instance/db2inst1/sqllib/db2dump`.

#### Fehlerbehebung bei häufigen Problemen
- **"No suitable Java runtime"**: Installieren Sie OpenJDK: `sudo apt install openjdk-11-jre-headless`.
- **Bibliotheksfehler (z.B. libaio.so)**: Stellen Sie sicher, dass `libaio1` installiert ist und führen Sie `sudo ldconfig` aus.
- **Zugriff verweigert**: Führen Sie den Installer als root aus; stellen Sie sicher, dass `/opt/ibm` den richtigen Besitzer hat: `sudo chown -R db2inst1:db2iadm1 /opt/ibm/db2`.
- **Glibc-Inkompatibilität**: Unwahrscheinlich auf Ubuntu 22.04/24.04, aber falls Probleme auftreten, erwägen Sie eine Container- (Docker-) Installation.
- **Stille Installation schlägt fehl**: Überprüfen Sie `db2setup.log` für Hinweise.
- **Ubuntu 24.04 spezifisch**: Wenn Bibliotheksabhängigkeiten fehlschlagen, müssen Sie möglicherweise PPAs hinzufügen oder fehlende Bibliotheken kompilieren. Testen Sie zuerst auf 22.04.
- Fehler? Durchsuchen Sie die IBM-Support-Foren oder führen Sie `db2diag` als Instanz-Benutzer aus.

Wenn Sie auf spezifische Fehler stoßen, geben Sie Details für gezieltere Hilfe an. Für den Produktionseinsatz erwägen Sie IBMs zertifizierte Umgebungen oder Support-Beratung. Erfolg! Ihre Db2-Instanz sollte jetzt bereit für die Datenbankerstellung und Nutzung sein.