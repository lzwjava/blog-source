---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Paramiko SSH- und SFTP-Leitfaden
translated: true
type: note
---

### Installation
Paramiko ist eine Python-Bibliothek für SSH und SFTP. Installieren Sie sie über pip:

```bash
pip install paramiko
```

### Grundlegende Verwendung
Paramiko ermöglicht es Ihnen, eine Verbindung zu SSH-Servern herzustellen, Befehle auszuführen und Dateien zu übertragen. Gehen Sie immer sicher mit privaten Schlüsseln um und verwenden Sie starke Passwörter – Paramiko unterstützt schlüsselbasierte und Passwort-Authentifizierung.

Schlüsselkonzepte:
- **Client**: Verwenden Sie `paramiko.SSHClient()`, um eine Verbindung einzurichten.
- **Transport**: Für eine niedrigere Kontrollebene verwenden Sie `paramiko.Transport()`.
- Authentifizieren Sie sich über `client.connect()` mit Hostname, Benutzername und entweder Passwort oder Schlüssel (z.B. via `paramiko.RSAKey.from_private_key_file()`).

### Beispiel: Verbinden und einen Befehl ausführen
Hier ist ein vollständiges Skript, um eine Verbindung zu einem SSH-Server herzustellen, einen Befehl auszuführen und die Ausgabe zu drucken. Ersetzen Sie die Platzhalter mit Ihren Daten.

```python
import paramiko

# SSH-Client erstellen
client = paramiko.SSHClient()

# Host-Key automatisch hinzufügen (in Produktion mit Vorsicht verwenden; stattdessen known_hosts laden)
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Verbinden (Passwort oder Schlüsseldatei verwenden)
    client.connect(
        hostname='your.server.com',
        port=22,  # Standard SSH-Port
        username='your_username',
        password='your_password',  # Oder key_filename='pfad/zum/private_key.pem'
    )

    # Befehl ausführen
    stdin, stdout, stderr = client.exec_command('echo "Hello from SSH!"')

    # Ausgabe lesen
    output = stdout.read().decode('utf-8')
    error = stderr.read().decode('utf-8')

    print("Output:", output)
    print("Error:", error)

except paramiko.SSHException as e:
    print(f"SSH-Fehler: {e}")
finally:
    client.close()
```

### Erweitertes Beispiel: Verwendung von schlüsselbasierter Authentifizierung und Dateiübertragung
Für die Schlüssel-Authentifizierung generieren Sie bei Bedarf ein Schlüsselpaar (z.B. mit `ssh-keygen`), fügen Sie den öffentlichen Schlüssel auf dem Server zu `~/.ssh/authorized_keys` hinzu und verwenden Sie dann:

```python
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Schlüsselbasierte Verbindung
    client.connect(
        hostname='your.server.com',
        username='your_username',
        key_filename='~/.ssh/id_rsa',  # Pfad zum privaten Schlüssel
    )

    # Befehl ausführen
    stdin, stdout, stderr = client.exec_command('ls -la')
    print(stdout.read().decode('utf-8'))

    # SFTP-Beispiel: Datei übertragen
    sftp = client.open_sftp()
    sftp.put('local_file.txt', 'remote_file.txt')  # Hochladen
    sftp.get('remote_file.txt', 'local_copy.txt')  # Herunterladen
    sftp.close()

except Exception as e:
    print(f"Fehler: {e}")
finally:
    client.close()
```

### Tipps und Best Practices
- **Sicherheit**: Bevorzugen Sie schlüsselbasierte Authentifizierung gegenüber Passwörtern. Deaktivieren Sie `AutoAddPolicy` in der Produktion und verifizieren Sie Host-Keys über `client.load_host_keys()`.
- **Fehlerbehandlung**: Fangen Sie immer `paramiko.SSHException` ab und prüfen Sie Exit-Codes mit `exit_status = stdout.channel.recv_exit_status()`.
- **Threads**: Paramiko ist standardmäßig nicht thread-sicher; verwenden Sie bei Bedarf Locks.
- **Dokumentation**: Für mehr Informationen, siehe die [offiziellen Paramiko Docs](https://docs.paramiko.org/). Testen Sie mit Tools wie OpenSSH's `sshd` oder lokalen VMs.

Dies sollte Ihnen den Einstieg erleichtern; passen Sie es an Ihre Bedürfnisse an!