---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-code-fast-1
title: Prozess auf Port mit Psutil beenden
translated: true
type: note
---

### Verwendung von psutil zur Erkennung und Beendigung eines Prozesses auf einem bestimmten Port (Windows)

Psutil ist eine plattformübergreifende Python-Bibliothek zum Abrufen von Informationen über laufende Prozesse und die Systemauslastung. Sie können sie verwenden, um Prozesse zu finden, die auf einem bestimmten Port lauschen (z. B. um festzustellen, ob etwas wie ein npm-Dev-Server auf diesem Port läuft), und dann den Prozess zu beenden. Dies funktioniert unter Windows, aber beachten Sie:

-   **Berechtigungen**: Unter Windows ist für das Beenden von Prozessen häufig Administratorberechtigung erforderlich (führen Sie Ihr Python-Skript als Administrator aus). Andernfalls kann eine `AccessDenied`-Ausnahme auftreten.
-   **Port-Erkennung**: Wir konzentrieren uns auf TCP-Verbindungen mit der Art "inet" (die IPv4 und IPv6 abdeckt). Dies ist üblich für Webserver wie die von `npm run dev` oder ähnlichen gestarteten.
-   **Annahmen**: Wir gehen davon aus, dass Sie nach einem lauschenden (Server-)Port suchen möchten (z. B. etwas, das lokal gebunden ist). Wenn Sie ausgehende Verbindungen zu einem Port meinen, unterscheidet sich der Ansatz leicht – lassen Sie es mich zur Klärung wissen.

#### Schritt 1: psutil installieren
Falls noch nicht geschehen:
```bash
pip install psutil
```

#### Schritt 2: Beispielcode zur Erkennung und Beendigung
Hier ist ein vollständiges Python-Skript. Es definiert eine Funktion, um die PID des Prozesses zu finden, der auf einem bestimmten Port lauscht (unter Verwendung von `kind='inet'`, wie Sie angegeben haben), und beendet ihn dann. Unter Windows ist `terminate()` gegenüber `kill()` zu bevorzugen, da es ein ordnungsgemäßes Herunterfahren ermöglicht (entspricht SIGTERM unter Unix).

```python
import psutil
import time  # Für optionale Verzögerung

def get_pid_listening_on_port(port, kind='inet'):
    """
    Scannt Netzwerkverbindungen nach Prozessen, die auf dem angegebenen Port lauschen.
    Gibt eine Liste von PIDs zurück (normalerweise eine, könnte aber bei seltenen Fällen mehrere sein).
    """
    pids = []
    for conn in psutil.net_connections(kind=kind):
        # Prüft, ob es sich um eine lauschende Verbindung (status='LISTEN') handelt und der lokale Adressport übereinstimmt
        if conn.status == 'LISTEN' and conn.laddr and conn.laddr.port == port:
            if conn.pid:
                pids.append(conn.pid)
    return pids

def kill_process_on_port(port, kind='inet'):
    """
    Findet und beendet den Prozess, der auf dem angegebenen Port lauscht.
    Falls mehrere Prozesse vorhanden sind, werden alle beendet (mit einer Warnung).
    """
    pids = get_pid_listening_on_port(port, kind)
    if not pids:
        print(f"Kein Prozess gefunden, der auf Port {port} lauscht.")
        return
    
    for pid in pids:
        try:
            proc = psutil.Process(pid)
            print(f"Beende Prozess {proc.name()} (PID {pid}) auf Port {port}...")
            # Verwende terminate() für ordnungsgemäßes Herunterfahren; es sendet ein SIGTERM-ähnliches Signal
            proc.terminate()
            # Optional: Warte einen Moment und erzwinge das Beenden, falls er nicht beendet wird
            gone, still_alive = psutil.wait_procs([proc], timeout=3)
            if still_alive:
                print(f"Erzwinge das Beenden von PID {pid}...")
                still_alive[0].kill()
        except psutil.AccessDenied:
            print(f"Zugriff verweigert: Kann PID {pid} nicht beenden. Als Administrator ausführen?")
        except psutil.NoSuchProcess:
            print(f"Prozess {pid} existiert nicht mehr.")

# Beispielverwendung: Ersetzen Sie 3000 durch Ihren Zielport (z. B. npm-Dev-Server verwenden oft 3000)
if __name__ == "__main__":
    kill_process_on_port(3000)  # Passen Sie kind bei Bedarf an (z. B. 'inet4' nur für IPv4)
```

#### Wichtige Erklärungen
-   **`psutil.net_connections(kind='inet')`**: Dies ruft Netzwerkverbindungen der Art 'inet' ab (umfasst IPv4 und IPv6). Jede Verbindung ist ein Namedtuple mit Feldern wie:
    -   `laddr`: Lokale Adresse (z. B. ('0.0.0.0', 8080) – IP und Port).
    -   `status`: 'LISTEN' für Server, die auf Verbindungen warten.
    -   `pid`: Prozess-ID des Eigentümers.
    -   Wir filtern nach `status == 'LISTEN'`, um Server (wie den npm-Dev-Port) zu finden, nicht Client-Verbindungen.
-   **PID-Abruf**: Das Skript holt sich die PID direkt aus dem Verbindungstupel. Wenn Sie nur erkennen, aber nicht beenden möchten, verwenden Sie `get_pid_listening_on_port(port)`, das die PID(s) zurückgibt.
-   **Beenden des Prozesses**:
    -   `psutil.Process(pid).terminate()`: Sendet ein Beendigungssignal. Unter Windows entspricht dies STRG+C.
    -   Falls es nicht beendet wird, erzwingen wir optional das Beenden mit `kill()` (entspricht SIGKILL).
    -   Psutils `wait_procs()` wartet darauf, dass der Prozess stirbt.
-   **Spezifität der inet-Art**: 'inet' schließt sowohl IPv4 als auch IPv6 ein. Wenn Sie wissen, dass es sich um IPv4 handelt, ändern Sie zu `kind='inet4'`. DIESERNAME adressiert Ihre "inet kind"-Anfrage direkt.
-   **Windows-spezifische Hinweise**:
    -   Psutil handhabt Windows-Interna gut, aber Netzwerkinformationen erfordern in einigen Fällen möglicherweise erhöhte Berechtigungen.
    -   Für Ports unter 1024 (privilegiert) können nur Systemdienste binden, aber die Erkennung sollte trotzdem funktionieren.
-   **Fehlerbehandlung**: Grundlegende Prüfungen für "Kein Prozess" oder Zugriffsprobleme wurden hinzugefügt.
-   **Testen**: Führen Sie etwas wie `npm run dev` aus, um Port 3000 zu belegen, und führen Sie dann dieses Skript aus.

Wenn dies nicht Ihren genauen Anforderungen entspricht (z. B. wenn "npm run port" etwas anderes bedeutet oder Sie nicht-lauschende Verbindungen erkennen möchten), geben Sie weitere Details zur Verfeinerung an! Aus Sicherheitsgründen stellen Sie bitte sicher, dass Sie nur beabsichtigte Prozesse beenden.