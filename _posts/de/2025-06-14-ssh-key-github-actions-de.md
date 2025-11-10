---
audio: false
generated: true
lang: de
layout: post
title: SSH-Schlüssel-Einrichtung für GitHub Actions JAR-Bereitstellung
translated: true
type: note
---

Um einen SSH-Schlüssel für GitHub Actions zur Bereitstellung einer JAR-Datei zu generieren, folgen Sie diesen Schritten:

1. **SSH-Schlüsselpaar generieren**:
   - Führen Sie auf Ihrem lokalen Rechner oder in einer sicheren Umgebung aus:
     ```bash
     ssh-keygen -t ed25519 -C "your_email@example.com" -f github-actions-deploy
     ```
   - Falls Ihr System Ed25519 nicht unterstützt, verwenden Sie:
     ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f github-actions-deploy
     ```
   - Drücken Sie die Eingabetaste, um den Standardspeicherort zu übernehmen, und vergeben Sie optional eine Passphrase (empfohlen für mehr Sicherheit). Dadurch werden zwei Dateien erstellt:
     - `github-actions-deploy` (privater Schlüssel)
     - `github-actions-deploy.pub` (öffentlicher Schlüssel)

2. **Öffentlichen Schlüssel zum Zielserver hinzufügen**:
   - Kopieren Sie den öffentlichen Schlüssel:
     ```bash
     cat github-actions-deploy.pub
     ```
   - Melden Sie sich auf dem Server an, auf dem Sie die JAR-Datei bereitstellen möchten.
   - Hängen Sie den öffentlichen Schlüssel an `~/.ssh/authorized_keys` auf dem Server an:
     ```bash
     echo "your-public-key-content" >> ~/.ssh/authorized_keys
     ```
   - Stellen Sie sicher, dass die Datei `authorized_keys` die korrekten Berechtigungen hat:
     ```bash
     chmod 600 ~/.ssh/authorized_keys
     ```

3. **Privaten Schlüssel in GitHub Secrets speichern**:
   - Gehen Sie zu Ihrem GitHub-Repository: `Einstellungen > Secrets and variables > Actions > Secrets`.
   - Klicken Sie auf **New repository secret**.
   - Geben Sie dem Secret einen Namen (z.B. `SSH_PRIVATE_KEY`).
   - Fügen Sie den Inhalt des privaten Schlüssels (`github-actions-deploy`) ein:
     ```bash
     cat github-actions-deploy
     ```
   - Speichern Sie das Secret.

4. **Den GitHub Actions Workflow konfigurieren**:
   - Erstellen oder bearbeiten Sie eine Workflow-Datei (z.B. `.github/workflows/deploy.yml`).
   - Fügen Sie einen Schritt hinzu, der den SSH-Schlüssel für die Bereitstellung der JAR-Datei verwendet. Nachfolgend ein Beispiel-Workflow:

     ```yaml
     name: Deploy JAR

     on:
       push:
         branches:
           - main

     jobs:
       deploy:
         runs-on: ubuntu-latest

         steps:
         - name: Checkout code
           uses: actions/checkout@v4

         - name: Set up Java
           uses: actions/setup-java@v4
           with:
             java-version: '17' # An Ihre Java-Version anpassen
             distribution: 'temurin'

         - name: Build JAR
           run: mvn clean package # An Ihr Build-Tool anpassen (z.B. Gradle)

         - name: Install SSH Key
           uses: shimataro/ssh-key-action@v2
           with:
             key: ${{ secrets.SSH_PRIVATE_KEY }}
             known_hosts: 'optional-known-hosts' # Siehe Hinweis unten

         - name: Add Known Hosts
           run: |
             ssh-keyscan -H <server-ip-or-hostname> >> ~/.ssh/known_hosts
           # Ersetzen Sie <server-ip-or-hostname> durch die IP oder den Hostnamen Ihres Servers

         - name: Deploy JAR to Server
           run: |
             scp target/your-app.jar user@<server-ip-or-hostname>:/path/to/deploy/
             ssh user@<server-ip-or-hostname> "sudo systemctl restart your-service" # An Ihren Bereitstellungsprozess anpassen
     ```

   - **Hinweise**:
     - Ersetzen Sie `target/your-app.jar` durch den Pfad zu Ihrer JAR-Datei.
     - Ersetzen Sie `user@<server-ip-or-hostname>` durch den SSH-Benutzer und die Adresse Ihres Servers.
     - Passen Sie den Bereitstellungsbefehl (z.B. `sudo systemctl restart your-service`) an die Art und Weise an, wie Sie die JAR-Datei auf Ihrem Server starten oder bereitstellen.
     - Der `known_hosts`-Schritt ist entscheidend, um Probleme mit der SSH-Host-Verifizierung zu vermeiden. Wenn Sie den Host-Schlüssel des Servers kennen, können Sie ihn im Schritt `shimataro/ssh-key-action` vorab hinterlegen oder wie gezeigt `ssh-keyscan` verwenden.

5. **Workflow absichern**:
   - Stellen Sie sicher, dass der private Schlüssel niemals in Logs oder Ausgaben preisgegeben wird.
   - Schränken Sie die Repository-Berechtigungen ein, um unbefugten Zugriff auf Secrets zu verhindern.
   - Falls Sie eine Passphrase für den SSH-Schlüssel verwenden, fügen Sie diese als weiteres Secret hinzu und binden Sie sie in den `shimataro/ssh-key-action`-Schritt ein:
     ```yaml
     with:
       key: ${{ secrets.SSH_PRIVATE_KEY }}
       passphrase: ${{ secrets.SSH_KEY_PASSPHRASE }}
       known_hosts: 'optional-known-hosts'
     ```

6. **Workflow testen**:
   - Übertragen Sie eine Änderung an den `main`-Branch (oder den im Workflow angegebenen Branch).
   - Überwachen Sie den Workflow im Tab **Actions** Ihres GitHub-Repositorys, um sicherzustellen, dass die JAR-Datei korrekt erstellt und bereitgestellt wird.

7. **Fehlerbehebung**:
   - **Permission denied**: Überprüfen Sie, ob der SSH-Schlüssel korrekt zur `authorized_keys`-Datei des Servers hinzugefügt wurde und ob der Benutzer die Berechtigung hat, auf das Zielverzeichnis zuzugreifen.
   - **Host verification failed**: Stellen Sie sicher, dass der `known_hosts`-Schritt korrekt mit der IP oder dem Hostnamen des Servers konfiguriert ist.
   - **Build issues**: Bestätigen Sie, dass die Java-Version und die Build-Befehle zu Ihrer Projekteinrichtung passen.

Dieses Setup integriert SSH-basierte Bereitstellung sicher in Ihren GitHub Actions Workflow für die Bereitstellung einer JAR-Datei. Wenn Sie spezifische Anpassungen benötigen (z.B. für ein bestimmtes Server-Setup oder Build-Tool), lassen Sie es mich wissen!