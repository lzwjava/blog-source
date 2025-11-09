---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Automatisiertes WLAN-Verbindungstestskript
translated: true
type: note
---

```python
import subprocess
import time
import os

def get_wifi_interfaces():
    """Hilfsfunktion zum Finden von WiFi-Schnittstellen."""
    try:
        result = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in result.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def test_wifi_connection(ssid, password="88888888", timeout=30):
    """Testet WiFi-Verbindung nicht-interaktiv. Gibt Tupel zurück (success: bool, error: str)."""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return False, "Keine WiFi-Schnittstelle verfügbar"
    interface = interfaces[0]  # Verwende erste verfügbare Schnittstelle
    con_name = f"test-{ssid}"  # Eindeutiger Name für das Testprofil
    
    # Befehle
    delete_cmd = f"nmcli connection delete '{con_name}'"
    add_cmd = (
        f"nmcli connection add type wifi con-name '{con_name}' "
        f"ifname {interface} ssid '{ssid}' "
        f"wifi-sec.key-mgmt wpa-psk wifi-sec.psk '{password}' "
        f"-- autoconnect no"
    )
    up_cmd = f"nmcli connection up '{con_name}'"
    disconnect_cmd = f"nmcli device disconnect {interface}"
    
    try:
        # Lösche vorhandenes Profil (unterdrücke Fehler falls nicht vorhanden)
        subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # Erstelle neues Profil mit eingebettetem Passwort (nicht-interaktiv)
        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True, timeout=10)
        if add_result.returncode != 0:
            error = add_result.stderr.strip() or add_result.stdout.strip() or "Fehler beim Erstellen des Verbindungsprofils"
            return False, f"Profil-Erstellungsfehler: {error}"
        
        # Aktiviere das Profil (nicht-interaktiv)
        up_result = subprocess.run(up_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        if up_result.returncode != 0:
            error = up_result.stderr.strip() or up_result.stdout.strip() or "Aktivierung fehlgeschlagen"
            if "secrets were required" in error.lower():
                error = "Falsches Passwort oder Authentifizierung fehlgeschlagen"
            elif "activation failed" in error.lower():
                error = f"Verbindungsaktivierung fehlgeschlagen: {error}"
            return False, f"nmcli Fehler: {error}"
        
        # Warte auf Stabilisierung
        time.sleep(2)
        
        # Teste Internet mit Ping
        ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if ping_test.returncode == 0:
            return True, None
        else:
            error = ping_test.stderr.strip() or "Ping fehlgeschlagen"
            return False, f"Verbunden aber kein Internet: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"Timeout nach {timeout} Sekunden"
    except subprocess.SubprocessError as e:
        return False, f"Befehlfehler: {str(e)}"
    finally:
        # Aufräumen: Verbindung trennen und Profil löschen
        try:
            subprocess.run(f"nmcli connection down '{con_name}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
            subprocess.run(disconnect_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # Ignoriere Aufräumfehler
```