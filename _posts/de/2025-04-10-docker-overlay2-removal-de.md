---
audio: false
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Behebung von Docker Overlay2 Löschfehlern
translated: true
type: note
---

Dieser Fehler bedeutet, dass Docker das Overlay2-Dateisystem des Containers nicht entfernen konnte – der Kernel/VM hat einen Low-Level-I/O-Fehler zurückgegeben (`readdirent merged: bad message`). Unter macOS passiert dies normalerweise, wenn die Docker-VM oder der Overlay-Speicher in einem fehlerhaften Zustand ist. Im Folgenden findest du sichere, geordnete Schritte (von am wenigsten zerstörerisch → aggressiver), die du zur Wiederherstellung versuchen kannst.

**Wichtig:** Einige der folgenden Befehle können Daten (Images/Volumes) entfernen. Ich werde zerstörerische Schritte kennzeichnen und exakte Befehle zeigen, die du kopieren/einfügen kannst, falls du möchtest.

---

# Schnellprüfungen (sicher)

Führe in einem Terminal aus:

```bash
# Container-Status und die problematische Container-ID anzeigen
docker ps -a --no-trunc | grep ccd89a3f36a1528cb923c90de8755faeb36e229c || true

# Erzwinge das Entfernen des Containers
docker rm -f ccd89a3f36a1528cb923c90de8755faeb36e229c
```

Wenn `docker rm -f` erfolgreich ist, bist du fertig. Schlägt es mit demselben Overlay-Fehler fehl, fahre fort.

---

# Docker neu starten (macOS Docker Desktop) — empfohlener nächster Schritt (sicher)

Beende Docker Desktop vollständig (über das Wal-Symbol → Quit) und starte es erneut. Oder über die Kommandozeile:

```bash
# macOS — Docker Desktop per AppleScript neu starten
osascript -e 'quit app "Docker"'
open -a Docker
```

Nachdem Docker neu gestartet wurde, versuche erneut `docker compose down` oder `docker rm -f <id>`.

---

# Den Host neu starten (sehr sicher)

Falls ein Neustart möglich ist, behebt ein Reboot von macOS oft VM-Dateisystemprobleme:

* Starte den Mac neu, starte dann Docker Desktop und versuche es erneut.

---

# Falls es weiterhin fehlschlägt — Verwende die Troubleshoot-Aktionen von Docker Desktop (sicher / mittel)

Öffne Docker Desktop → Troubleshoot:

* Klicke auf **Restart Docker** (falls noch nicht geschehen).
* Falls das fehlschlägt, versuche **Clean / Purge data** oder **Reset to factory defaults** — **Warnung:** Diese entfernen Images/Container/Volumes. Verwende sie nur, wenn du den Verlust lokaler Docker-Daten verkraften kannst.

---

# Falls du Docker Engine (Linux) verwendest oder mit manueller Bereinigung vertraut bist (zerstörerisch)

**Führe dies nur aus, wenn du das Risiko von Datenverlust verstehst.** Stoppe den Docker-Daemon, entferne das Overlay2-Verzeichnis für die problematische ID und starte Docker dann neu.

```bash
# Docker-Daemon stoppen (Linux)
sudo systemctl stop docker

# Sichere zuerst den overlay2-Ordner (optional, falls du Platz hast)
sudo cp -a /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f /root/overlay2-backup-7acbf095

# Falls das Backup erstellt / nicht benötigt wird, entferne das merged-Verzeichnis für dieses Overlay:
sudo rm -rf /var/lib/docker/overlay2/7acbf095f3537e4829397e10f2134499389c724d3378782a8882ff1299fc431f

# (Optional) Entferne die Container-Metadaten, falls nötig
# WARNUNG: Entferne nur Dateien, von denen du sicher bist, dass sie dem defekten Container entsprechen
sudo rm -rf /var/lib/docker/containers/ccd89a3f36a1528cb923c90de8755faeb36e229cab353c2285222948197b8d18

# Docker starten
sudo systemctl start docker

# Versuche dann, nicht mehr referenzierte Objekte zu bereinigen
docker system prune -a --volumes
```

Nochmals: Das Löschen von Dateien unter `/var/lib/docker` ist zerstörerisch und kann andere Container beschädigen, wenn es falsch durchgeführt wird. Verwende es nur, wenn du weißt, was du löschst.

---

# Weniger zerstörerische Bereinigung, die oft hilft

Falls du das Overlay nicht direkt löschen kannst oder einen sanfteren Ansatz bevorzugst:

```bash
# Versuche, ungenutzte Objekte zu bereinigen
docker system prune -f
docker volume prune -f

# Entferne ungenutzte Images/Container (Vorsicht)
docker image prune -a -f
docker container prune -f
```

Dies kann Speicherplatz freigeben und ermöglicht Docker manchmal, Entfernungsoperationen erfolgreich erneut auszuführen.

---

# Falls das Problem erneut auftritt und du Docker Desktop für Mac verwendest

* Erwäge, die Docker-VM-Festplattengröße zu erhöhen (Settings → Resources → Disk image size).
* Falls du dich auf wichtige lokale Daten verlässt, exportiere zuerst Volumes/Container (`docker export`, `docker save`), bevor du Reset/Purge verwendest.

---

# Diagnosedaten zum Sammeln (falls du möchtest, dass ich weiterhelfe)

Falls keiner der oben genannten Schritte das Problem behebt, teile die Ausgaben dieser (nicht zerstörerischen) Befehle und ich schlage gezielte nächste Schritte vor:

```bash
docker info
docker ps -a
docker compose version
docker version
# Overlay-Verzeichnisse auflisten (Linux)
ls -lah /var/lib/docker/overlay2 | head -n 40
```

(Wenn du macOS Docker Desktop verwendest, wird `ls /var/lib/docker` nicht die VM-Inhalte anzeigen – bevorzuge das Neustarten von Docker Desktop oder die Verwendung der Troubleshoot-UI.)

---

Falls du möchtest, teile mir mit, ob du **Docker Desktop on macOS** (höchstwahrscheinlich) oder **Docker Engine on Linux** verwendest – ich gebe dir dann eine kürzere, maßgeschneiderte Abfolge. Falls du bevorzugst, kann ich auch eine Einzeiler-Checkliste erstellen, die du der Reihe nach ausführen kannst.