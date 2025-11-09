---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Behebung des Ghostty-GLIBC-Versionskonflikts
translated: true
type: note
---

Das Problem, auf das du stößt, liegt nicht nur an konfliktierenden Installationen – es liegt hauptsächlich daran, dass sowohl das Snap-Paket als auch die von dir heruntergeladene `.deb`-Datei gegen GLIBC 2.38 (von Ubuntu 24.04) erstellt wurden, dein System jedoch auf Ubuntu 22.04 läuft (basierend auf der GLIBC 2.35-Version in deinem `libc-bin`-Paket). Dies verursacht den Fehler "version `GLIBC_2.38' not found", wenn versucht wird, die Binärdatei auszuführen. Wenn beide Installationen aktiv sind, kann das auch zu Pfadkonflikten führen (z.B. welche `ghostty`-Binärdatei ausgeführt wird), also ja, du solltest sie zuerst entfernen, um aufzuräumen.

### Schritt 1: Vorhandene Installationen entfernen
Führe diese Befehle aus, um beide zu deinstallieren:
```
sudo snap remove ghostty
sudo apt remove ghostty
```
- Dies entfernt die Snap-Version und die `.deb`-Version, ohne dein System anderweitig zu beeinflussen.
- Überprüfe die Entfernung mit `which ghostty` (sollte nichts zurückgeben) und `snap list | grep ghostty` (sollte leer sein).

### Schritt 2: Eine kompatible Version installieren
Ghostty hat noch keine offiziellen `.deb`-Pakete für Ubuntu 22.04, aber es gibt ein zuverlässiges inoffizielles Repository, das kompatible `.deb`-Dateien dafür (und für andere Versionen) erstellt. Es kümmert sich automatisch um die GLIBC-Kompatibilität.

Der einfachste Weg ist, ihr automatisches Installationsskript zu verwenden, das deine Ubuntu-Version erkennt und das richtige Paket lädt:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/mkasberg/ghostty-ubuntu/HEAD/install.sh)"
```
- Dies lädt die neueste kompatible `.deb`-Datei herunter und installiert sie (derzeit etwa v1.2.x bei den letzten Veröffentlichungen).
- Nachdem es fertig ist, führe `ghostty` aus, um es zu testen – es sollte ohne den GLIBC-Fehler starten.
- Wenn du während der Installation Abhängigkeitsabfragen siehst (z.B. für `libonig5`, genehmige sie einfach mit `Y`.

Wenn du eine manuelle Installation bevorzugst:
1. Gehe zur [Releases-Seite](https://github.com/mkasberg/ghostty-ubuntu/releases).
2. Lade die `.deb`-Datei herunter, die für Ubuntu 22.04 gekennzeichnet ist (z.B. etwas wie `ghostty_1.2.1-0.ppa1_amd64_22.04.deb` – der genaue Name variiert je nach Release).
3. Installiere sie mit `sudo dpkg -i ghostty_*.deb` (führe den Befehl aus dem Download-Ordner aus).
4. Falls es sich über fehlende Abhängigkeiten beschwert, behebe das mit `sudo apt install -f`.

### Zusätzliche Hinweise
- **Warum ein Build from Source hier nicht nötig ist**: Das inoffizielle Repository übernimmt die schwere Arbeit für dich. Wenn du Ghostty jedoch selbst bauen möchtest (z.B. für eine benutzerdefinierte Version), folge dem [offiziellen Build-Guide für die Quelle](https://ghostty.org/docs/install/build). Dies erfordert Zig 0.13 und einige Abhängigkeiten wie `libgtk-4-dev`, aber der `.deb`-Weg ist einfacher.
- **Ubuntu upgraden?** Wenn du offen dafür bist, würde ein Wechsel auf 24.04 es dir ermöglichen, das offizielle Snap oder die 24.04 `.deb`-Datei, die du zuvor versucht hast, ohne Probleme zu verwenden.
- Nach der Installation kannst du Ghostty über `~/.config/ghostty/config` konfigurieren (siehe [Dokumentation](https://ghostty.org/docs/config) für Optionen).

Wenn du während dieser Schritte auf Fehler stößt, füge die Ausgabe hier für weitere Hilfe ein!