---
audio: false
generated: true
lang: de
layout: post
title: Installiere GitHub CLI
translated: true
type: note
---

Um die GitHub CLI (`gh`) auf Ubuntu zu installieren und mit dem Befehl `gh workflow run` GitHub Actions Workflows auszulösen, folgen Sie diesen Schritten:

### Installationsschritte für GitHub CLI (`gh`) auf Ubuntu

1. **GitHub CLI Repository und GPG-Schlüssel hinzufügen**:
   Führen Sie die folgenden Befehle in Ihrem Terminal aus, um das offizielle GitHub CLI Paket-Repository einzurichten:

   ```bash
   (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   ```

   Dieses Skript:
   - Installiert `wget`, falls noch nicht vorhanden.
   - Erstellt ein Verzeichnis für APT Keyrings.
   - Lädt den GitHub CLI GPG-Schlüssel herunter und fügt ihn hinzu.
   - Konfiguriert das GitHub CLI Repository für Ihr System.

2. **Paketindex aktualisieren und `gh` installieren**:
   Aktualisieren Sie Ihre Paketliste und installieren Sie das `gh` Kommandozeilen-Tool:

   ```bash
   sudo apt update
   sudo apt install gh -y
   ```

3. **Installation überprüfen**:
   Überprüfen Sie, ob `gh` korrekt installiert wurde, indem Sie ausführen:

   ```bash
   gh --version
   ```

   Sie sollten eine Ausgabe wie `gh version X.Y.Z (YYYY-MM-DD)` sehen, was die Installation bestätigt.

4. **Bei GitHub authentifizieren**:
   Authentifizieren Sie sich vor der Verwendung von `gh` mit Ihrem GitHub-Konto:

   ```bash
   gh auth login
   ```

   Folgen Sie den Anweisungen:
   - Wählen Sie `GitHub.com` (oder Ihren Enterprise Server, falls zutreffend).
   - Wählen Sie Ihr bevorzugtes Protokoll (`HTTPS` oder `SSH`; `SSH` wird empfohlen, wenn Sie einen SSH-Schlüssel eingerichtet haben).
   - Wählen Sie die Authentifizierungsmethode (Browser ist am einfachsten; es öffnet eine Webseite zum Anmelden).
   - Kopieren Sie den bereitgestellten Einmal-Code, fügen Sie ihn im Browser ein und autorisieren Sie `gh`.
   - Bestätigen Sie die Standardeinstellungen oder passen Sie sie bei Bedarf an.

   Nach erfolgreicher Authentifizierung sehen Sie eine Bestätigungsmeldung.

### Verwendung von `gh workflow run` für GitHub Actions

Der Befehl `gh workflow run` löst einen GitHub Actions Workflow aus. So verwenden Sie ihn:

1. **Navigieren Sie zu Ihrem Repository** (optional):
   Wenn Sie sich in einem lokalen Git-Repository befinden, das mit GitHub verknüpft ist, erkennt `gh` dies automatisch. Andernfalls geben Sie das Repository mit dem `--repo` Flag an.

2. **Verfügbare Workflows auflisten** (optional):
   Um die Workflow-ID oder den Dateinamen zu finden, führen Sie aus:

   ```bash
   gh workflow list
   ```

   Dies zeigt alle Workflows im Repository an, mit deren Namen, IDs und Status (z.B. `active`).

3. **Einen Workflow ausführen**:
   Verwenden Sie den Befehl `gh workflow run` mit dem Dateinamen oder der ID des Workflows. Zum Beispiel:

   ```bash
   gh workflow run workflow.yml
   ```

   Oder, unter Verwendung der Workflow-ID (z.B. `123456`):

   ```bash
   gh workflow run 123456
   ```

   Wenn der Workflow Eingaben akzeptiert, geben Sie diese mit dem `--field` Flag an:

   ```bash
   gh workflow run workflow.yml --field key=value
   ```

   Um einen Branch oder Ref anzugeben, verwenden Sie das `--ref` Flag:

   ```bash
   gh workflow run workflow.yml --ref branch-name
   ```

4. **Den Workflow überwachen**:
   Überprüfen Sie nach dem Auslösen den Status des Runs:

   ```bash
   gh run list
   ```

   Um einen bestimmten Run in Echtzeit zu beobachten, verwenden Sie:

   ```bash
   gh run watch <run-id>
   ```

   Ersetzen Sie `<run-id>` durch die Run-ID aus `gh run list`.

### Tipps zur Problembehebung

- **GPG-Signaturfehler**: Wenn Sie während `apt update` GPG-bezogene Probleme haben, konsultieren Sie den GitHub Issue Tracker für Lösungen (z.B. `cli/cli#9569`) oder wiederholen Sie den Schlüsselimport-Schritt.[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **Firewall-Probleme**: Wenn `keyserver.ubuntu.com` fehlschlägt, versuchen Sie:

   ```bash
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
   ```

   Oder installieren Sie `dirmngr`, falls benötigt:

   ```bash
   sudo apt-get install dirmngr
   ```

  [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
- **Snap-Installationswarnung**: GitHub rät von der Verwendung des Snap-Pakets für `gh` aufgrund von Laufzeitproblemen ab. Bleiben Sie bei der oben beschriebenen APT-Methode.[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **Authentifizierungs-Scopes**: Wenn `gh workflow run` aufgrund von Berechtigungen fehlschlägt, stellen Sie sicher, dass Ihr Token den `workflow` Scope hat. Authentifizieren Sie sich erneut mit:

   ```bash
   gh auth refresh -s workflow
   ```

### Zusätzliche Hinweise

- **GitHub CLI Handbuch**: Für weitere Details zu `gh` Befehlen, führen Sie `gh help` aus oder besuchen Sie das offizielle Handbuch unter [cli.github.com](https://cli.github.com).[](https://cli.github.com/manual/)
- **Workflow-Anforderungen**: Stellen Sie sicher, dass die Workflow-Datei (z.B. `workflow.yml`) im Verzeichnis `.github/workflows/` Ihres Repositorys existiert und für manuelle Trigger konfiguriert ist (z.B. `workflow_dispatch` Event).
- **Alternative Installationsmethoden**: Sie können `gh` auch via Homebrew (`brew install gh`) oder durch Herunterladen von Binärdateien von der [Releases-Seite](https://github.com/cli/cli/releases) installieren, aber die APT-Methode wird für Ubuntu empfohlen.[](https://github.com/cli/cli)

Dieses Setup ermöglicht es Ihnen, GitHub Actions Workflows effizient von der Kommandozeile unter Ubuntu aus zu verwalten. Lassen Sie mich wissen, wenn Sie Hilfe mit spezifischen `gh` Befehlen oder Workflow-Konfigurationen benötigen!