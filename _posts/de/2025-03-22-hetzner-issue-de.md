---
audio: false
generated: true
lang: de
layout: post
title: Hetzner-API-Problem
translated: true
type: note
---

Lassen Sie uns den Fehler, auf den Sie stoßen, analysieren und erklären, was mit Ihrem Code passiert:

### Fehler:
```
Error creating snapshot for server sg5: cannot perform operation because server is locked (locked, f21b9dc9d1535310)
```

Dieser Fehler stammt von der Hetzner Cloud API (über das `hcloud` Python SDK) und zeigt an, dass der Vorgang zum Erstellen eines Snapshots für den Server mit dem Namen `sg5` fehlgeschlagen ist, weil der Server **gesperrt** ist. Ein gesperrter Server bedeutet, dass ein anderer Vorgang (z.B. ein vorheriger Snapshot, Neustart oder eine Größenänderung) gerade ausgeführt wird und der Server vorübergehend für neue Vorgänge gesperrt ist, bis dieser Prozess abgeschlossen ist.

### Code-Überblick:
Hier ist Ihr Skript mit Erklärungen und wo der Fehler entsteht:

```python
from hcloud import Client
import os

# Holt den API-Token aus der Umgebungsvariable
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# Erstellt eine Client-Instanz
client = Client(token=api_token)

def create_snapshot(server):
    try:
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")

# Listet alle Server auf
servers = client.servers.get_all()

# Gibt Serverdetails aus und erstellt Snapshots
for server in servers:
    print(f"Server ID: {server.id}")
    print(f"Server Name: {server.name}")
    print(f"Server Status: {server.status}")
    print(f"Server IPv4: {server.public_net.ipv4.ip}")
    print(f"Server IPv6: {server.public_net.ipv6.ip}")
    print(f"Server Type: {server.server_type.name}")
    print(f"Server Location: {server.datacenter.location.name}")
    print("----------------------------------")
    create_snapshot(server)
```

1.  **API-Token Einrichtung**:
    - Das Skript holt den Hetzner API-Schlüssel aus einer Umgebungsvariable (`HERTZNER_API_KEY`). Wenn sie nicht gesetzt ist, wird das Skript mit einer Fehlermeldung beendet.

2.  **Client-Initialisierung**:
    - Eine `Client`-Instanz wird mit dem API-Token erstellt, um mit der Hetzner Cloud API zu interagieren.

3.  **`create_snapshot` Funktion**:
    - Diese Funktion versucht, einen Snapshot eines gegebenen Servers mit `client.servers.create_image()` zu erstellen.
    - Parameter:
        - `server`: Das Serverobjekt, von dem ein Snapshot erstellt werden soll.
        - `description`: Ein Name für den Snapshot (z.B. `sg5-snapshot`).
        - `type="snapshot"`: Gibt an, dass es sich um einen Snapshot handelt (im Gegensatz zu einem Backup oder einer ISO).
    - Bei Erfolg wird die Snapshot-ID ausgegeben; andernfalls werden alle Exceptions abgefangen und ausgegeben (wie die, die Sie sehen).

4.  **Server-Auflistung**:
    - `client.servers.get_all()` ruft eine Liste aller Server ab, die mit Ihrem Hetzner-Account verknüpft sind.
    - Das Skript durchläuft diese Liste, gibt deren Details aus (ID, Name, Status, IPs, etc.) und ruft für jeden Server `create_snapshot()` auf.

5.  **Wo der Fehler auftritt**:
    - Innerhalb der `create_snapshot()`-Funktion schlägt der Aufruf `client.servers.create_image()` für den Server `sg5` fehl, weil er gesperrt ist. Die Fehlermeldung (`cannot perform operation because server is locked`) wird von der `hcloud`-Bibliothek basierend auf der API-Antwort ausgelöst.

### Warum ist der Server gesperrt?
Ein Server wird gesperrt, wenn bereits ein Vorgang im Gange ist. Häufige Gründe sind:
- Ein anderer Snapshot wird gerade erstellt.
- Der Server wird neu gestartet, in der Größe geändert oder neu aufgesetzt.
- Ein vorheriger Vorgang wurde noch nicht abgeschlossen.

Die Sperr-ID (`f21b9dc9d1535310`) in der Fehlermeldung ist eine eindeutige Kennung für die laufende Aktion, die den Server sperrt.

### Wie man es behebt:
Hier sind Schritte, um das Problem zu lösen und Ihr Skript zu verbessern:

#### 1. **Vor dem Fortfahren auf gesperrten Status prüfen**
Ändern Sie das Skript so, dass die Snapshot-Erstellung übersprungen wird, wenn der Server gesperrt ist. Sie können die aktuellen Aktionen des Servers mit `client.actions.get_all()` prüfen oder warten, bis die Sperre aufgehoben ist.

Aktualisierte `create_snapshot`-Funktion:
```python
def create_snapshot(server):
    try:
        # Prüft, ob der Server gesperrt ist, indem seine Aktionen überprüft werden
        actions = client.actions.get_all(server=server)
        for action in actions:
            if action.status == "running":
                print(f"Skipping snapshot for {server.name}: Server is locked by action {action.id}")
                return
        # Wenn keine laufenden Aktionen vorhanden sind, mit dem Snapshot fortfahren
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 2. **Warten, bis die Sperre aufgehoben wird**
Wenn Sie warten möchten, anstatt zu überspringen, können Sie die Aktionen des Servers abfragen, bis die Sperre aufgehoben ist:
```python
import time

def wait_for_unlock(server):
    while True:
        actions = client.actions.get_all(server=server)
        running = any(action.status == "running" for action in actions)
        if not running:
            break
        print(f"Waiting for server {server.name} to unlock...")
        time.sleep(5)  # Wartet 5 Sekunden, bevor erneut geprüft wird

def create_snapshot(server):
    try:
        wait_for_unlock(server)
        response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
        print(f"Snapshot created for server {server.name} with ID: {response.image.id}")
    except Exception as e:
        print(f"Error creating snapshot for server {server.name}: {e}")
```

#### 3. **Die Sperre manuell untersuchen**
- Verwenden Sie die Hetzner Cloud Console oder die API, um den Status der Aktion mit der ID `f21b9dc9d1535310` zu prüfen.
- Beispiel-API-Aufruf (via Python):
  ```python
  action = client.actions.get_by_id("f21b9dc9d1535310")
  print(f"Action Status: {action.status}, Command: {action.command}")
  ```
- Wenn sie hängen geblieben ist, müssen Sie möglicherweise den Hetzner-Support kontaktieren.

#### 4. **Das Skript erneut ausführen**
Sobald der Server nicht mehr gesperrt ist (die Aktion abgeschlossen ist oder Sie sie manuell gelöst haben), führen Sie das Skript erneut aus.

### Zusätzliche Hinweise:
- **Rate Limits**: Das Erstellen von Snapshots für viele Server in einer Schleife könnte die API-Rate Limits von Hetzner erreichen. Fügen Sie bei Bedarf eine Verzögerung (z.B. `time.sleep(1)`) zwischen den Anfragen ein.
- **Fehlerbehandlung**: Das aktuelle Skript stoppt beim ersten Fehler. Wenn es für andere Server fortfahren soll, stellen Sie sicher, dass die Exception die Schleife nicht anhält (was in Ihrem Fall gut ist, da sie das nicht tut).

Lassen Sie mich wissen, wenn Sie Hilfe bei der Implementierung einer dieser Lösungen oder beim weiteren Debugging benötigen!