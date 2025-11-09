---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Prueba Automatizada de Conexión WiFi
translated: true
type: note
---

```python
import subprocess
import time
import os

def obtener_interfaces_wifi():
    """Ayuda para encontrar interfaces WiFi."""
    try:
        resultado = subprocess.run("nmcli dev status | grep wifi | awk '{print $1}'", shell=True, capture_output=True, text=True)
        interfaces = [iface.strip() for iface in resultado.stdout.split('\n') if iface.strip()]
        return interfaces
    except:
        return []

def probar_conexion_wifi(ssid, password="88888888", timeout=30):
    """Prueba la conexión WiFi de forma no interactiva. Retorna tupla(éxito: bool, error: str)."""
    interfaces = obtener_interfaces_wifi()
    if not interfaces:
        return False, "No hay interfaz WiFi disponible"
    interface = interfaces[0]  # Usar primera interfaz disponible
    nombre_con = f"test-{ssid}"  # Nombre único para el perfil de prueba
    
    # Comandos
    comando_eliminar = f"nmcli connection delete '{nombre_con}'"
    comando_agregar = (
        f"nmcli connection add type wifi con-name '{nombre_con}' "
        f"ifname {interface} ssid '{ssid}' "
        f"wifi-sec.key-mgmt wpa-psk wifi-sec.psk '{password}' "
        f"-- autoconnect no"
    )
    comando_activar = f"nmcli connection up '{nombre_con}'"
    comando_desconectar = f"nmcli device disconnect {interface}"
    
    try:
        # Eliminar cualquier perfil existente (suprimir errores si no existe)
        subprocess.run(comando_eliminar, shell=True, capture_output=True, timeout=5)
        time.sleep(1)
        
        # Crear nuevo perfil con contraseña embebida (no interactivo)
        resultado_agregar = subprocess.run(comando_agregar, shell=True, capture_output=True, text=True, timeout=10)
        if resultado_agregar.returncode != 0:
            error = resultado_agregar.stderr.strip() or resultado_agregar.stdout.strip() or "Error al crear perfil de conexión"
            return False, f"Error en creación de perfil: {error}"
        
        # Activar el perfil (no interactivo)
        resultado_activar = subprocess.run(comando_activar, shell=True, capture_output=True, text=True, timeout=timeout)
        if resultado_activar.returncode != 0:
            error = resultado_activar.stderr.strip() or resultado_activar.stdout.strip() or "Activación fallida"
            if "secrets were required" in error.lower():
                error = "Contraseña incorrecta o autenticación fallida"
            elif "activation failed" in error.lower():
                error = f"Activación de conexión fallida: {error}"
            return False, f"Error nmcli: {error}"
        
        # Esperar estabilización
        time.sleep(2)
        
        # Probar internet con ping
        prueba_ping = subprocess.run("ping -c 1 -W 3 8.8.8.8", shell=True, capture_output=True, text=True, timeout=5)
        if prueba_ping.returncode == 0:
            return True, None
        else:
            error = prueba_ping.stderr.strip() or "Ping falló"
            return False, f"Conectado pero sin internet: {error}"
        
    except subprocess.TimeoutExpired:
        return False, f"Tiempo de espera agotado después de {timeout} segundos"
    except subprocess.SubprocessError as e:
        return False, f"Error de comando: {str(e)}"
    finally:
        # Limpieza: Desactivar conexión y eliminar perfil
        try:
            subprocess.run(f"nmcli connection down '{nombre_con}'", shell=True, capture_output=True, timeout=5)
            subprocess.run(comando_eliminar, shell=True, capture_output=True, timeout=5)
            subprocess.run(comando_desconectar, shell=True, capture_output=True, timeout=5)
        except subprocess.SubprocessError:
            pass  # Ignorar problemas de limpieza
```