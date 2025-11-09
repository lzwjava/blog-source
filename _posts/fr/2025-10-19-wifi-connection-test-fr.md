---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Script de test automatisé de connexion Wi-Fi
translated: true
type: note
---

```python
import subprocess
import time
import os

def get_wifi_interfaces():
    """Helper pour trouver les interfaces WiFi."""
    try:
        result = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in result.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def test_wifi_connection(ssid, password="88888888", timeout=30):
    """Test de connexion WiFi non interactif. Retourne un tuple(success: bool, error: str)."""
    interfaces = get_wifi_interfaces()
    if not interfaces:
        return False, "Aucune interface WiFi disponible"
    interface = interfaces[0]  # Utiliser la première interface disponible
    con_name = f"test-{ssid}"  # Nom unique pour le profil de test
    
    # Commandes
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
        # Supprimer tout profil existant (ignorer les erreurs si absent)
        subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # Créer un nouveau profil avec mot de passe intégré (non interactif)
        add_result = subprocess.run(add_cmd, shell=True, capture_output=True, text=True, timeout=10)
        if add_result.returncode != 0:
            error = add_result.stderr.strip() or add_result.stdout.strip() or "Échec de création du profil de connexion"
            return False, f"Erreur de création de profil: {error}"
        
        # Activer le profil (non interactif)
        up_result = subprocess.run(up_cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        if up_result.returncode != 0:
            error = up_result.stderr.strip() or up_result.stdout.strip() or "Échec d'activation"
            if "secrets were required" in error.lower():
                error = "Mauvais mot de passe ou échec d'authentification"
            elif "activation failed" in error.lower():
                error = f"Échec d'activation de la connexion: {error}"
            return False, f"Erreur nmcli: {error}"
        
        # Attendre la stabilisation
        time.sleep(2)
        
        # Tester internet avec ping
        ping_test = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if ping_test.returncode == 0:
            return True, None
        else:
            error = ping_test.stderr.strip() or "Échec du ping"
            return False, f"Connecté mais pas d'internet: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"Timeout de l'opération après {timeout} secondes"
    except subprocess.SubprocessError as e:
        return False, f"Erreur de commande: {str(e)}"
    finally:
        # Nettoyage: Désactiver la connexion et supprimer le profil
        try:
            subprocess.run(f"nmcli connection down '{con_name}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(delete_cmd, shell=True, capture_output=True, timeout=5)
            subprocess.run(disconnect_cmd, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # Ignorer les problèmes de nettoyage
```