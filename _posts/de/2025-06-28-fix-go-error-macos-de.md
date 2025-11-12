---
audio: false
generated: true
lang: de
layout: post
title: Beheben des Fehlers „Go Command Not Found“ unter macOS
translated: true
type: note
---

Die Fehlermeldung `/bin/sh: go: command not found` zeigt an, dass die Go-Programmiersprache nicht auf Ihrem macOS-System installiert ist oder nicht korrekt in Ihrem PATH konfiguriert ist. Der `make`-Befehl versucht, einen Go-Build-Prozess auszuführen, der den Go-Compiler (`go`) benötigt. Nachfolgend finden Sie die Schritte zur Installation von Go auf macOS und zur Behebung dieses Problems.

### Schritte zur Installation von Go auf macOS

Es gibt zwei primäre Möglichkeiten, Go auf macOS zu installieren: mit dem offiziellen Go-Installer oder mit Homebrew. Ich werde beide Methoden behandeln, aber Homebrew ist für macOS-Benutzer oft einfacher. Wählen Sie eine Methode basierend auf Ihrer Präferenz.

#### Voraussetzungen
- Stellen Sie sicher, dass Ihre macOS-Version 10.10 oder neuer ist, um mit aktuellen Go-Versionen kompatibel zu sein.
- Sie benötigen Administratorzugriff, um Go zu installieren und Systemdateien zu ändern.
- Eine Terminal-Anwendung (zu finden unter Programme > Dienstprogramme > Terminal).

#### Methode 1: Go mit Homebrew installieren (Empfohlen)
Homebrew ist ein beliebter Paketmanager für macOS, der die Softwareinstallation vereinfacht.

1. **Homebrew installieren (falls noch nicht installiert)**:
   - Öffnen Sie Terminal und führen Sie aus:
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - Befolgen Sie die Anweisungen auf dem Bildschirm, um die Installation abzuschließen.

2. **Go installieren**:
   - Führen Sie den folgenden Befehl aus, um die neueste Version von Go zu installieren:
     ```bash
     brew install go
     ```
   - Dies installiert Go unter `/usr/local/Cellar/go` (oder einem ähnlichen Pfad) und fügt die Go-Binärdatei zu `/usr/local/bin` hinzu.

3. **Installation überprüfen**:
   - Überprüfen Sie die installierte Go-Version, indem Sie ausführen:
     ```bash
     go version
     ```
   - Sie sollten eine Ausgabe wie `go version go1.23.x darwin/amd64` sehen, was die Installation bestätigt.

4. **Umgebungsvariablen einrichten** (falls nötig):
   - Homebrew fügt Go normalerweise automatisch zu Ihrem PATH hinzu, aber wenn `go`-Befehle nicht funktionieren, fügen Sie den Go-Binärpfad zu Ihrem Shell-Profil hinzu:
     - Öffnen oder erstellen Sie die entsprechende Shell-Konfigurationsdatei (z.B. `~/.zshrc` für Zsh, was seit Catalina Standard auf macOS ist, oder `~/.bash_profile` für Bash):
       ```bash
       nano ~/.zshrc
       ```
     - Fügen Sie die folgenden Zeilen hinzu:
       ```bash
       export PATH=$PATH:/usr/local/go/bin
       ```
     - Speichern Sie die Datei (Strg+X, dann Y, dann Eingabe in nano) und wenden Sie die Änderungen an:
       ```bash
       source ~/.zshrc
       ```
     - Wenn Sie einen benutzerdefinierten Workspace verwenden möchten, setzen Sie `GOPATH` (optional, da Go-Module dies oft überflüssig machen):
       ```bash
       export GOPATH=$HOME/go
       export PATH=$PATH:$GOPATH/bin
       ```
     - Sourcen Sie die Datei erneut:
       ```bash
       source ~/.zshrc
       ```

5. **Go-Installation testen**:
   - Führen Sie erneut `go version` aus, um sicherzustellen, dass der Befehl erkannt wird.
   - Optional können Sie ein einfaches Go-Programm erstellen, um zu bestätigen, dass alles funktioniert:
     ```bash
     mkdir -p ~/go/src/hello
     nano ~/go/src/hello/main.go
     ```
     - Fügen Sie den folgenden Code hinzu:
       ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("Hello, World!")
       }
       ```
     - Speichern und verlassen Sie (Strg+X, Y, Eingabe), dann kompilieren und führen Sie aus:
       ```bash
       cd ~/go/src/hello
       go run main.go
       ```
     - Sie sollten `Hello, World!` als Ausgabe sehen.

#### Methode 2: Go mit dem offiziellen Installer installieren
Wenn Sie Homebrew nicht verwenden möchten, können Sie Go mit dem offiziellen macOS-Paket installieren.

1. **Go-Installer herunterladen**:
   - Besuchen Sie die offizielle Go-Download-Seite: https://go.dev/dl/
   - Laden Sie das macOS-Paket (`.pkg`) für Ihre Systemarchitektur herunter (z.B. `go1.23.x.darwin-amd64.pkg` für Intel Macs oder `go1.23.x.darwin-arm64.pkg` für Apple Silicon).

2. **Installer ausführen**:
   - Doppelklicken Sie auf die heruntergeladene `.pkg`-Datei im Finder.
   - Befolgen Sie die Anweisungen auf dem Bildschirm, um Go zu installieren. Es wird standardmäßig unter `/usr/local/go` installiert.
   - Möglicherweise müssen Sie Ihr Administrator-Passwort eingeben.

3. **Umgebungsvariablen einrichten**:
   - Öffnen Sie Terminal und bearbeiten Sie Ihre Shell-Konfigurationsdatei (z.B. `~/.zshrc` oder `~/.bash_profile`):
     ```bash
     nano ~/.zshrc
     ```
   - Fügen Sie die folgenden Zeilen hinzu:
     ```bash
     export GOROOT=/usr/local/go
     export GOPATH=$HOME/go
     export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
     ```
   - Speichern und wenden Sie die Änderungen an:
     ```bash
     source ~/.zshrc
     ```
   - Hinweis: `GOROOT` ist optional, es sei denn, Sie entwickeln Go selbst oder benötigen einen nicht standardmäßigen Installationspfad. Moderne Go-Versionen erfordern oft kein Setzen von `GOROOT`.

4. **Installation überprüfen**:
   - Führen Sie aus:
     ```bash
     go version
     ```
   - Sie sollten die installierte Go-Version sehen (z.B. `go version go1.23.x darwin/amd64`).

5. **Go-Installation testen**:
   - Befolgen Sie die gleichen Schritte wie in Methode 1, Schritt 5, um ein "Hello, World!"-Programm zu erstellen und auszuführen.

#### Fehlerbehebung des ursprünglichen Problems
Nach der Installation von Go navigieren Sie zurück zu Ihrem `clash-core`-Verzeichnis und versuchen den `make`-Befehl erneut:
```bash
cd /path/to/clash-core
make
```

Wenn Sie auf Probleme stoßen:
- **Proxy-Einstellungen**: Ihre Terminal-Ausgabe zeigt, dass `HTTP_PROXY` und `HTTPS_PROXY` auf `http://127.0.0.1:7890` gesetzt sind. Stellen Sie sicher, dass Ihr Proxy aktiv ist und nicht den Netzwerkzugriff von Go beeinträchtigt (z.B. beim Herunterladen von Abhängigkeiten). Sie können den Proxy vorübergehend deaktivieren, um zu testen:
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **Berechtigungen**: Wenn Sie Berechtigungsfehler erhalten, stellen Sie sicher, dass Sie Schreibzugriff auf das Projektverzeichnis und den Go-Workspace (`$GOPATH` oder `$HOME/go`) haben.
- **Go-Module**: Das `clash-core`-Projekt verwendet wahrscheinlich Go-Module. Stellen Sie sicher, dass Sie sich im richtigen Verzeichnis befinden, das `go.mod` enthält, und führen Sie `go mod tidy` aus, um Abhängigkeiten vor `make` abzurufen:
  ```bash
  go mod tidy
  make
  ```
- **Architektur-Konflikt**: Der `make`-Befehl baut für `linux-amd64` (`GOOS=linux GOARCH=amd64`). Wenn Sie die Binärdatei auf macOS ausführen möchten, müssen Sie möglicherweise die Makefile oder den Build-Befehl anpassen, um `darwin-amd64` (für Intel Macs) oder `darwin-arm64` (für Apple Silicon) als Ziel zu verwenden. Überprüfen Sie die Makefile auf das `linux-amd64`-Target und passen Sie es an, oder führen Sie aus:
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  Ersetzen Sie `amd64` durch `arm64`, wenn Sie Apple Silicon verwenden.

#### Zusätzliche Hinweise
- **Deinstallation vorheriger Go-Versionen**: Wenn Go zuvor installiert war, entfernen Sie es, um Konflikte zu vermeiden:
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  Installieren Sie dann mit einer der oben genannten Methoden neu.
- **Go-Workspace**: Wenn Sie `GOPATH` setzen, erstellen Sie das Verzeichnis:
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  Allerdings ist `GOPATH` mit Go-Modulen (die von den meisten modernen Projekten wie `clash-core` verwendet werden) weniger kritisch.
- **Xcode Command Line Tools**: Einige Go-Projekte benötigen C-Abhängigkeiten (z.B. `CGO_ENABLED=1`). Installieren Sie die Xcode Command Line Tools falls nötig:
  ```bash
  xcode-select --install
  ```
- **Mehrere Go-Versionen**: Wenn Sie mehrere Go-Versionen benötigen, ziehen Sie die Verwendung eines Versionsmanagers wie `gvm` in Betracht (installierbar über Homebrew oder ein Skript).

#### Überprüfung
Sobald Go installiert ist und der `make`-Befehl erfolgreich ausgeführt wird, sollte die `clash-core`-Binärdatei im `bin/`-Verzeichnis erscheinen (z.B. `bin/clash-linux-amd64` oder `bin/clash-darwin-amd64`). Überprüfen Sie, ob sie funktioniert, indem Sie ausführen:
```bash
./bin/clash-darwin-amd64 --version
```

Wenn Sie weitere Hilfe benötigen oder auf spezifische Fehler stoßen, teilen Sie mir die genaue Fehlermeldung oder den Kontext mit, und ich kann gezieltere Hilfe anbieten!