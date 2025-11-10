---
audio: false
generated: true
lang: de
layout: post
title: Go über APT auf Debian installieren
translated: true
type: note
---

Um Go mit `apt` auf einem Debian-basierten Linux-System (z.B. Ubuntu) zu installieren, folge diesen Schritten. Beachte, dass `apt` möglicherweise eine ältere Version von Go installiert (z.B. 1.18 auf Ubuntu 22.04). Du solltest prüfen, ob diese den Anforderungen deines Projekts entspricht (überprüfe die erforderliche Go-Version in der `go.mod` Datei in `~/Projects/clash-core`).

### Schritte zur Installation von Go mit APT

1. **Paketindex aktualisieren**
   - Stelle sicher, dass deine Paketlisten auf dem neuesten Stand sind:
     ```bash
     sudo apt update
     ```

2. **Go installieren**
   - Installiere das Go-Paket:
     ```bash
     sudo apt install golang-go
     ```
   - Dies installiert den Go-Compiler, Tools und die Standardbibliothek.

3. **Installation überprüfen**
   - Überprüfe die installierte Go-Version:
     ```bash
     go version
     ```
   - Du solltest eine Ausgabe ähnlich wie diese sehen:
     ```
     go version go1.18.1 linux/amd64
     ```
     (Die Version hängt vom Paketrepository deiner Distribution ab.)

4. **GOPATH einrichten (Optional)**
   - Moderne Go-Versionen (1.13+) verwenden Module, daher ist `GOPATH` optional, aber das Setzen kann für einige Projekte nützlich sein.
   - Bearbeite dein Shell-Profil (z.B. `~/.bashrc` oder `~/.zshrc`):
     ```bash
     nano ~/.bashrc
     ```
   - Füge Folgendes hinzu:
     ```bash
     export GOPATH=$HOME/go
     export PATH=$PATH:$GOPATH/bin
     ```
   - Speichere und lade die Shell-Konfiguration neu:
     ```bash
     source ~/.bashrc
     ```

5. **Build erneut versuchen**
   - Wechsle in dein Projektverzeichnis:
     ```bash
     cd ~/Projects/clash-core
     ```
   - Führe den `make`-Befehl erneut aus:
     ```bash
     make
     ```

### Hinweise
- **Versionsprüfung**: Falls dein Projekt eine neuere Go-Version erfordert (z.B. 1.20 oder höher), könnte die `apt`-Version veraltet sein. Überprüfe die erforderliche Version in `go.mod` oder der Projektdokumentation. Installiere bei Bedarf manuell eine neuere Version, indem du das Tarball von [https://go.dev/dl/](https://go.dev/dl/) herunterlädst (wie in der vorherigen Antwort beschrieben).
- **Alternative Repositories**: Für eine neuere Version über `apt` kannst du ein Drittanbieter-PPA hinzufügen (z.B. `ppa:longsleep/golang-backports` auf Ubuntu). Führe aus:
  ```bash
  sudo add-apt-repository ppa:longsleep/golang-backports
  sudo apt update
  sudo apt install golang-go
  ```
- **Fehlerbehebung**:
  - Falls `go` nicht gefunden wird, stelle sicher, dass `/usr/bin/go` existiert (`ls /usr/bin/go`). Falls nicht, installiere mit `sudo apt install --reinstall golang-go` neu.
  - Bei Abhängigkeitsfehlern, führe `sudo apt install -f` aus, um diese zu beheben.
  - Bei Berechtigungsproblemen stelle sicher, dass du `sudo`-Berechtigungen hast.

### Quellen
- Ubuntu Go-Installationsanleitung: [https://ubuntu.com/server/docs/programming-go](https://ubuntu.com/server/docs/programming-go)
- Allgemeine apt-Verwendung: [https://help.ubuntu.com/community/AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)

Falls die installierte Version zu alt ist oder du auf Probleme stößt, teile mir bitte deine Linux-Distribution (z.B. Ubuntu 22.04) und die erforderliche Go-Version mit, und ich werde dich weiter unterstützen!