---
audio: false
generated: true
image: false
lang: de
layout: post
title: Mit SSH mit GitHub verbinden
translated: true
type: note
---

Um eine Verbindung zu GitHub über SSH herzustellen, folgen Sie diesen Schritten basierend auf der bereitgestellten GitHub-Dokumentation. Diese Anleitung geht davon aus, dass Sie bei Null anfangen, und umfasst die Überprüfung auf vorhandene Schlüssel, das Generieren eines neuen Schlüssels, das Hinzufügen zu GitHub und das Testen der Verbindung.

### 1. Auf vorhandene SSH-Schlüssel prüfen
Bevor Sie einen neuen SSH-Schlüssel erstellen, prüfen Sie, ob Sie bereits einen besitzen:
- Öffnen Sie ein Terminal (unter macOS/Linux) oder Git Bash (unter Windows).
- Führen Sie aus:
  ```bash
  ls -al ~/.ssh
  ```
- Suchen Sie nach Dateien wie `id_rsa` und `id_rsa.pub` (oder ähnlichen, z.B. `id_ed25519`, `id_ed25519.pub`). Wenn sie existieren, haben Sie möglicherweise bereits einen Schlüssel. Wenn Sie einen vorhandenen Schlüssel verwenden möchten, fahren Sie mit Schritt 3 fort. Wenn nicht, fahren Sie fort, um einen neuen Schlüssel zu generieren.

### 2. Einen neuen SSH-Schlüssel generieren
Wenn Sie keinen SSH-Schlüssel besitzen oder einen neuen erstellen möchten:
- Generieren Sie in Ihrem Terminal einen neuen SSH-Schlüssel:
  ```bash
  ssh-keygen -t ed25519 -C "ihre_email@beispiel.com"
  ```
  - Ersetzen Sie `ihre_email@beispiel.com` mit der E-Mail-Adresse, die mit Ihrem GitHub-Konto verknüpft ist.
  - Falls Ihr System `ed25519` nicht unterstützt, verwenden Sie:
    ```bash
    ssh-keygen -t rsa -b 4096 -C "ihre_email@beispiel.com"
    ```
- Wenn Sie dazu aufgefordert werden, drücken Sie die Eingabetaste, um den Schlüssel am Standardspeicherort zu speichern (`~/.ssh/id_ed25519` oder `~/.ssh/id_rsa`).
- Geben Sie optional eine Passphrase für zusätzliche Sicherheit ein (oder drücken Sie die Eingabetaste für keine).

### 3. Den SSH-Schlüssel zum SSH-Agent hinzufügen
Der SSH-Agent verwaltet Ihre Schlüssel für die Authentifizierung:
- Starten Sie den SSH-Agent:
  ```bash
  eval "$(ssh-agent -s)"
  ```
- Fügen Sie Ihren privaten Schlüssel dem Agent hinzu:
  ```bash
  ssh-add ~/.ssh/id_ed25519
  ```
  - Wenn Sie RSA verwendet haben, ersetzen Sie `id_ed25519` durch `id_rsa`.
- Wenn Sie eine Passphrase festgelegt haben, werden Sie aufgefordert, diese einzugeben.

### 4. Den SSH-Schlüssel zu Ihrem GitHub-Konto hinzufügen
- Kopieren Sie Ihren öffentlichen Schlüssel in die Zwischenablage:
  - Unter macOS:
    ```bash
    pbcopy < ~/.ssh/id_ed25519.pub
    ```
  - Unter Linux:
    ```bash
    cat ~/.ssh/id_ed25519.pub
    ```
    Kopieren Sie dann die Ausgabe manuell.
  - Unter Windows (Git Bash):
    ```bash
    cat ~/.ssh/id_ed25519.pub | clip
    ```
  - Wenn Sie RSA verwendet haben, ersetzen Sie `id_ed25519.pub` durch `id_rsa.pub`.
- Gehen Sie zu GitHub:
  - Melden Sie sich bei [GitHub](https://github.com) an.
  - Klicken Sie auf Ihr Profilbild (oben rechts) → **Settings** → **SSH and GPG keys** → **New SSH key** oder **Add SSH key**.
  - Fügen Sie Ihren öffentlichen Schlüssel in das Feld "Key" ein, vergeben Sie einen Titel (z.B. "Mein Laptop") und klicken Sie auf **Add SSH key**.

### 5. Ihre SSH-Verbindung testen
Überprüfen Sie, ob Ihr SSH-Schlüssel mit GitHub funktioniert:
- Führen Sie aus:
  ```bash
  ssh -T git@github.com
  ```
- Wenn Sie dazu aufgefordert werden, bestätigen Sie mit `yes`.
- Sie sollten eine Nachricht wie die folgende sehen:
  ```
  Hi username! You've successfully authenticated, but GitHub does not provide shell access.
  ```
  Dies bestätigt, dass Ihre SSH-Verbindung funktioniert.

### 6. Git für die Verwendung von SSH konfigurieren
Stellen Sie sicher, dass Ihr Git-Repository SSH für die Authentifizierung verwendet:
- Überprüfen Sie die Remote-URL Ihres Repositorys:
  ```bash
  git remote -v
  ```
- Wenn die URL mit `https://` beginnt, ändern Sie sie zu SSH:
  ```bash
  git remote set-url origin git@github.com:username/repository.git
  ```
  - Ersetzen Sie `username/repository` mit Ihrem GitHub-Benutzernamen und Repository-Namen.

### 7. Optional: SSH-Schlüssel-Passphrasen verwalten
Wenn Sie eine Passphrase festgelegt haben, können Sie den SSH-Agent konfigurieren, um die erneute Eingabe zu vermeiden:
- Unter macOS fügen Sie Ihren Schlüssel zur Keychain hinzu:
  ```bash
  ssh-add --apple-use-keychain ~/.ssh/id_ed25519
  ```
- Unter Linux/Windows fordert der SSH-Agent die Passphrase in der Regel nur einmal pro Sitzung an.

### 8. Optional: SSH-Agent-Forwarding oder Deploy Keys verwenden
- **SSH-Agent-Forwarding**: Wenn Sie auf einem Server bereitstellen, aktivieren Sie Agent-Forwarding, um Ihre lokalen SSH-Schlüssel sicher zu verwenden. Fügen Sie Ihrer `~/.ssh/config` hinzu:
  ```bash
  Host example.com
      ForwardAgent yes
  ```
  Ersetzen Sie `example.com` mit dem Hostnamen Ihres Servers.
- **Deploy Keys**: Für automatisierte Skripte generieren Sie einen separaten SSH-Schlüssel für jeden Server und fügen ihn als Deploy Key in den Einstellungen Ihres GitHub-Repositorys hinzu.

### Problembehandlung
- Falls `ssh -T git@github.com` fehlschlägt, stellen Sie sicher:
  - Ihr öffentlicher Schlüssel ist korrekt zu GitHub hinzugefügt.
  - Der SSH-Agent läuft und Ihr Schlüssel ist hinzugefügt (`ssh-add -l` listet geladene Schlüssel auf).
  - Die Dateiberechtigungen sind korrekt:
    ```bash
    chmod 600 ~/.ssh/id_ed25519
    chmod 644 ~/.ssh/id_ed25519.pub
    ```
- Bei weiteren Problemen lesen Sie den Troubleshooting-Guide von GitHub.

Jetzt können Sie SSH verwenden, um sicher mit GitHub zu interagieren, ohne Anmeldedaten wiederholt eingeben zu müssen.

[Connecting to GitHub with SSH - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)