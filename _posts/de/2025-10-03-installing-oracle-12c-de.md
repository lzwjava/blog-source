---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Installation von Oracle 12c auf Ubuntu
translated: true
type: note
---

### Installation von Oracle Database 12c Release 1 (12.1.0.2 mit Patch 12.1.2?) aus einem Tarball auf Ubuntu 22.04 x86_64

Die Datei `v12.1.2_linuxx64_server_dec.tar.gz` scheint ein Tarball für Oracle Database 12c Release 1 zu sein (wahrscheinlich Version 12.1.0.2 gebündelt mit dem Patch 12.1.2, Server Edition, möglicherweise "dec" für dekonfiguriert). Dies ist eine ältere Version von Oracle Database (aus ~2013-2014), und Oracle unterstützt Ubuntu **nicht offiziell**. Die Installation auf Ubuntu 22.04 (welches moderne Bibliotheken wie glibc 2.35 verwendet) kann funktionieren, erfordert jedoch möglicherweise Workarounds für Kompatibilitätsprobleme, wie z.B. das Verlinken von Bibliotheken oder das Anpassen von Kernel-Parametern. Rechnen Sie mit potenziellen Fehlern bei Abhängigkeiten – testen Sie zuerst in einer VM.

**Warnungen:**
- Oracle 12c ist End-of-Life für erweiterten Support (seit 2022), verwenden Sie es auf eigenes Risiko für Tests/Produktion. Ziehen Sie neuere Versionen wie 19c oder 23ai für die Produktion in Betracht.
- Sie benötigen Root-/sudo-Zugriff.
- Minimale Hardware: 2 GB RAM (8 GB empfohlen), 2 CPU-Kerne, 10 GB freier Festplattenspeicher für die Software (mehr für die Datenbank).
- Sichern Sie Ihr System, bevor Sie fortfahren.
- Wenn dieser Tarball nicht aus einer offiziellen Oracle-Quelle stammt, überprüfen Sie seine Integrität (z.B. Checksummen), um Schadsoftware zu vermeiden.

#### Schritt 1: Bereiten Sie Ihr System vor
1. **Ubuntu aktualisieren**:
   ```
   sudo apt update && sudo apt upgrade -y
   ```

2. **Erforderliche Abhängigkeiten installieren**:
   Oracle 12c benötigt bestimmte Bibliotheken. Installieren Sie sie via apt:
   ```
   sudo apt install -y oracle-java8-installer bc binutils libaio1 libaio-dev libelf-dev libnuma-dev libstdc++6 unixodbc unixodbc-dev
   ```
   - Falls `oracle-java8-installer` nicht verfügbar ist (er befindet sich in älteren Repositories), fügen Sie das Oracle Java PPA hinzu oder laden Sie JDK 8 manuell herunter:
     ```
     sudo add-apt-repository ppa:webupd8team/java -y
     sudo apt update
     sudo apt install oracle-java8-installer -y
     ```
     Akzeptieren Sie die Lizenz während der Installation. Setzen Sie JAVA_HOME:
     ```
     echo 'export JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> ~/.bashrc
     source ~/.bashrc
     ```

3. **Oracle-Benutzer und -Gruppen erstellen**:
   Führen Sie dies als root oder mit sudo aus:
   ```
   sudo groupadd -g 54321 oinstall
   sudo groupadd -g 54322 dba
   sudo useradd -u 54321 -g oinstall -G dba -s /bin/bash oracle
   sudo passwd oracle  # Setzen Sie ein Passwort für den Oracle-Benutzer
   ```

4. **Kernel-Parameter konfigurieren**:
   Bearbeiten Sie `/etc/sysctl.conf`:
   ```
   sudo nano /etc/sysctl.conf
   ```
   Fügen Sie diese Zeilen hinzu (passen Sie sie für Ihren RAM/Platte an; dies sind Mindestwerte):
   ```
   fs.file-max = 6815744
   kernel.sem = 250 32000 100 128
   kernel.shmmni = 4096
   kernel.shmall = 1073741824
   kernel.shmmax = 4398046511104
   kernel.panic_on_oops = 1
   net.core.rmem_default = 262144
   net.core.rmem_max = 4194304
   net.core.wmem_default = 262144
   net.core.wmem_max = 1048576
   fs.aio-max-nr = 1048576
   vm.swappiness = 0
   ```
   Änderungen übernehmen:
   ```
   sudo sysctl -p
   ```

5. **Shell-Limits für Oracle-Benutzer setzen**:
   Bearbeiten Sie `/etc/security/limits.conf`:
   ```
   sudo nano /etc/security/limits.conf
   ```
   Fügen Sie hinzu:
   ```
   oracle soft nproc 2047
   oracle hard nproc 16384
   oracle soft nofile 1024
   oracle hard nofile 65536
   oracle soft stack 10240
   oracle hard stack 32768
   ```
   Bearbeiten Sie `/etc/pam.d/login` und fügen Sie hinzu:
   ```
   sudo nano /etc/pam.d/login
   ```
   Anhängen: `session required pam_limits.so`

6. **Verzeichnisse erstellen**:
   ```
   sudo mkdir -p /u01/app/oracle/product/12.1.0/dbhome_1
   sudo mkdir -p /u01/app/oraInventory
   sudo chown -R oracle:oinstall /u01
   sudo chmod -R 775 /u01
   ```

7. **Swap-Space** (falls RAM < 8 GB, Swap hinzufügen):
   Für 2 GB RAM, erstellen Sie eine 2 GB Swap-Datei:
   ```
   sudo fallocate -l 2G /swapfile
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
   ```

8. **Firewall/SElinux deaktivieren** (falls aktiviert):
   ```
   sudo ufw disable  # Oder konfigurieren Sie die Ports 1521, 5500 falls benötigt
   sudo apt remove apparmor -y  # Falls AppArmor stört
   ```

#### Schritt 2: Tarball entpacken
Wechseln Sie zum Oracle-Benutzer:
```
su - oracle
cd ~/Downloads  # Oder wo auch immer die Datei liegt
```
Entpacken (dies erstellt die Verzeichnisstruktur des Database Home):
```
tar -xzf v12.1.2_linuxx64_server_dec.tar.gz -C /u01/app/oracle/product/12.1.0/
```
- Dies sollte `/u01/app/oracle/product/12.1.0/dbhome_1` mit Dateien wie `runInstaller` erstellen.
- Falls der Tarball eine andere Struktur extrahiert, passen Sie die Pfade entsprechend an (z.B. `database/` Verzeichnis).

#### Schritt 3: Installer ausführen
Immer noch als Oracle-Benutzer:
```
cd /u01/app/oracle/product/12.1.0/dbhome_1
./runInstaller
```
- Der GUI-Installer wird gestartet (erfordert X11 Forwarding bei SSH; verwenden Sie `ssh -X` oder aktivieren Sie X11).
- **Installationsoptionen**:
  - Wählen Sie "Create and configure a database software only" oder "Single instance database installation" (für die Server Edition).
  - ORACLE_HOME: `/u01/app/oracle/product/12.1.0/dbhome_1`
  - Inventory: `/u01/app/oraInventory`
  - Falls es nur Software ist (keine DB-Erstellung), wählen Sie "Install database software only".
- Folgen Sie dem Assistenten: Akzeptieren Sie die Standardeinstellungen wo möglich, aber setzen Sie Passwörter für SYS/SYSTEM.
- Ignorieren Sie anfänglich alle "Prereq"-Warnungen – beheben Sie diese nötigenfalls nach der Installation.

Falls die GUI fehlschlägt (z.B. DISPLAY-Fehler), führen Sie eine Silent-Installation durch:
```
./runInstaller -silent -responseFile /path/to/responsefile.rsp
```
Sie müssen eine Response-Datei vorbereiten (Beispiel im extrahierten Verzeichnis, z.B. `db_install.rsp`). Bearbeiten Sie sie mit Ihren Einstellungen (ORACLE_HOME, etc.) und führen Sie sie aus.

#### Schritt 4: Nach der Installation
1. **root.sh ausführen** (als root):
   ```
   sudo /u01/app/oraInventory/orainstRoot.sh
   sudo /u01/app/oracle/product/12.1.0/dbhome_1/root.sh
   ```

2. **Umgebungsvariablen setzen** (für Oracle-Benutzer, zu `~/.bash_profile` hinzufügen):
   ```
   export ORACLE_HOME=/u01/app/oracle/product/12.1.0/dbhome_1
   export PATH=$ORACLE_HOME/bin:$PATH
   export ORACLE_SID=orcl  # Ändern Sie zu Ihrer SID
   export LD_LIBRARY_PATH=$ORACLE_HOME/lib:/lib:/usr/lib
   export CLASSPATH=$ORACLE_HOME/jlib:$ORACLE_HOME/rdbms/jlib
   ```
   ```
   source ~/.bash_profile
   ```

3. **Eine Datenbank erstellen** (falls nicht während der Installation geschehen):
   ```
   dbca  # Database Configuration Assistant (GUI/silent)
   ```
   Oder verwenden Sie SQL*Plus für die manuelle Erstellung.

4. **Dienste starten/stoppen**:
   ```
   sqlplus / as sysdba
   STARTUP;  # Oder shutdown
   ```
   Für Auto-Start zu systemd hinzufügen (erstellen Sie `/etc/systemd/system/oracle.service` mit exec zu `dbstart`).

#### Fehlerbehebung bei häufigen Problemen auf Ubuntu 22.04
- **Glibc/Abhängigkeitsfehler**: Oracle 12c erwartet glibc <=2.17. Ubuntu 22.04 hat 2.35 – verwenden Sie `ldd` zur Überprüfung, oder installieren Sie Kompatibilitäts-Bibliotheken:
  ```
  sudo apt install libc6:i386 libncurses5:i386 libstdc++6:i386
  ```
  Falls Linker-Fehler auftreten, setzen Sie `LD_PRELOAD` oder verwenden Sie einen Docker-Container mit Oracle Linux.
- **Java/Display-Probleme**: Stellen Sie sicher, dass JDK 8 gesetzt ist (`java -version` sollte 1.8 anzeigen). Für Headless: `export DISPLAY=:0`.
- **Speichermangel**: Erhöhen Sie ulimit oder RAM. Bearbeiten Sie ggf. `runInstaller` Parameter.
- **Patch 12.1.2**: Falls nicht gebündelt, laden Sie ihn von My Oracle Support herunter und wenden Sie ihn nach der Installation mit `opatch` an.
- **Logs**: Überprüfen Sie `/u01/app/oraInventory/logs/installActions*.log` auf Fehler.
- **Kompatibilitätsfix**: Einige Benutzer verlinken Bibliotheken symbolisch (z.B. `sudo ln -s /lib/x86_64-linux-gnu/libpthread.so.0 /u01/app/oracle/product/12.1.0/dbhome_1/lib/libpthread_nonshared.a` – recherchieren Sie je nach Fehler).

#### Verifizierung
- Führen Sie `sqlplus / as sysdba` aus und führen Sie `SELECT * FROM v$version;` aus.
- Listener: `lsnrctl start`.

Falls Sie auf spezifische Fehler stoßen, geben Sie die Log-Ausgabe für weitere Hilfe an. Für offizielle (wenn auch RHEL-fokussierte) Dokumentation, siehe Oracle's 12c Installationshandbuch. Falls dies für ein anderes Produkt (nicht DB) ist, klären Sie den Inhalt des Tarballs!