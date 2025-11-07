---
audio: false
generated: false
image: false
lang: es
layout: post
title: IP en la Nube, Interfaz de Red y Optimización de WiFi
translated: true
type: post
---

### Tabla de Contenidos

1. [IPs Flotantes en Hetzner Cloud](#ips-flotantes-en-hetzner-cloud)
   - Comandos de Configuración de IP
   - Configuración de Netplan
   - Archivos de Configuración de Red

2. [Gestión de Interfaces de Red](#gestión-de-interfaces-de-red)
   - Eliminación de Interfaces TUN
   - Monitoreo del Estado de Interfaces
   - Solución de Problemas de Red

3. [Escáner de IPs en LAN](#escáner-de-ips-en-lan)
   - Script de Escaneo de Red en Python
   - Descubrimiento de Hosts Multihilo
   - Capacidades de Escaneo de Puertos
   - Identificación de Dispositivos en Redes Locales

4. [Omitir IPs Locales](#omitir-ips-locales)
   - Configuración de Proxy para Redes Locales
   - Cálculos de Máscara de Subred
   - Planificación de Rangos de Red

5. [Conexión SSH usando Dirección IPv6](#conexión-ssh-usando-dirección-ipv6)
   - Configuración SSH para IPv6
   - Gestión del Archivo de Configuración SSH
   - Configuración de Comandos Proxy para Diferentes Tipos de Direcciones
   - Optimización de Rendimiento

6. [Mejorar la Velocidad del Wifi](#mejorar-la-velocidad-del-wifi)
   - Rendimiento del Módem Antiguo vs. Nuevo
   - Configuraciones de Red
   - Modos Puente: Cableado vs. Inalámbrico
   - Solución de Cuellos de Botella en la Red

7. [Reinicio de OpenWrt](#reinicio-de-openwrt)
   - Métodos de Reinicio mediante Interfaz Web
   - Procedimientos de Reinicio mediante Línea de Comandos
   - Restauración de Valores de Fábrica

---

## IPs Flotantes en Hetzner Cloud

### IP

```bash
sudo ip addr add 78.47.144.0 dev eth0
```

### Netplan

```bash
touch /etc/netplan/60-floating-ip.yaml
nano /etc/netplan/60-floating-ip.yaml
```

```yaml
network:
   version: 2
   renderer: networkd
   ethernets:
     eth0:
       addresses:
       - 78.47.144.0/32
```

```bash
sudo netplan apply
```

---

## Gestión de Interfaces de Red

Elimina la interfaz `tun`.

```bash
$ ipconfig

outline-tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.0.85.1  netmask 255.255.255.255  destination 10.0.85.1
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 500  (UNSPEC)
        RX packets 208  bytes 8712 (8.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 385  bytes 23322 (23.3 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

$ sudo ip link delete outline-tun0
```

---

## Escáner de IPs en LAN

Este script en Python escanea una red local en busca de direcciones IP activas. Utiliza el comando `ping` para verificar si un host es accesible y emplea multihilo para acelerar el proceso de escaneo. Un semáforo limita el número de hilos concurrentes para evitar sobrecargar el sistema. El script toma una dirección de red (por ejemplo, "192.168.1.0/24") como entrada y muestra si cada dirección IP en la red está activa o inactiva.

Este script ayuda a identificar dispositivos en la red, como un enrutador TP-LINK mesh operando en modo puente cableado, mediante el escaneo de direcciones IP activas.

```python
import subprocess
import ipaddress
import threading
import os
import socket
import argparse

MAX_THREADS = 50  # Número máximo de hilos a utilizar

def is_host_up(host, port=None):
    """
    Verifica si un host está activo usando ping o telnet.
    Si se especifica un puerto, usa telnet para verificar si el puerto está abierto.
    De lo contrario, usa ping.
    Devuelve True si el host está activo, False en caso contrario.
    """
    if port:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                return True
            else:
                return False
        except socket.error as e:
            return False
        finally:
            sock.close()
    else:
        try:
            # -c 1: Envía solo 1 paquete
            # -W 1: Espera 1 segundo por una respuesta
            subprocess.check_output(["ping", "-c", "1", "-W", "1", host], timeout=1)
            return True
        except subprocess.CalledProcessError:
            return False
        except subprocess.TimeoutExpired:
            return False

def scan_ip(ip_str, up_ips, port=None):
    """
    Escanea una única dirección IP y muestra su estado.
    """
    if is_host_up(ip_str, port):
        print(f"{ip_str} está activo")
        up_ips.append(ip_str)
    else:
        print(f"{ip_str} está inactivo")

def scan_network(network, port=None):
    """
    Escanea una red en busca de hosts activos usando hilos, limitando el número de hilos concurrentes.
    """
    print(f"Escaneando red: {network}")
    threads = []
    semaphore = threading.Semaphore(MAX_THREADS)  # Limita el número de hilos concurrentes
    up_ips = []

    def scan_ip_with_semaphore(ip_str):
        semaphore.acquire()
        try:
            scan_ip(ip_str, up_ips, port)
        finally:
            semaphore.release()

    for ip in ipaddress.IPv4Network(network):
        ip_str = str(ip)
        thread = threading.Thread(target=scan_ip_with_semaphore, args=(ip_str,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return up_ips

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Escanea una red en busca de hosts activos.")
    parser.add_argument("network", nargs='?', default="192.168.1.0/24", help="La red a escanear (ejemplo: 192.168.1.0/24)")
    parser.add_argument("-p", "--port", type=int, help="El puerto a verificar (opcional)")
    args = parser.parse_args()

    network_to_scan = args.network
    port_to_scan = args.port

    up_ips = scan_network(network_to_scan, port_to_scan)
    print("\nIPs activas:")
    for ip in up_ips:
        print(ip)
```

---

## Omitir IPs Locales

El script identifica direcciones IP activas. Para garantizar una comunicación de red adecuada, verifica que la configuración del proxy esté configurada para omitir estas IPs locales.

```bash
192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,127.0.0.1,localhost,*.local,timestamp.apple.com,sequoia.apple.com,seed-sequoia.siri.apple.com, 192.168.1.0/16
```

---

## Máscaras de Subred

Mi segunda máquina suele estar en 192.168.1.16.

Por lo tanto, funciona usando el siguiente comando.

```bash
python scripts/ip_scan.py 192.168.1.0/27 -p 22
```

Porque 32 - 27 = 5, 2^5 = 32, por lo que intentará desde `192.168.1.0` hasta `192.168.1.31`.

Pero no funciona al usar `192.168.1.0/28`, porque 2^4 = 16, por lo que intentará desde `192.168.1.0` hasta `192.168.1.15`, lo que no cubre `192.168.1.16`.

---

## Conexión SSH usando Dirección IPv6

Estoy intentando conectarme a una máquina en Hetzner Cloud usando IPv6. `ssh 2a01:4f8:c17:2000::/64` no funciona, pero `ssh root@2a01:4f8:c17:2000::1` sí.

La dirección IPv6 fue copiada desde la consola de Hetzner Cloud.

El archivo `~/.ssh/config` se puede configurar para aplicar diferentes reglas de proxy a direcciones IPv4 e IPv6. Esta configuración permite especificar un comando proxy para direcciones IPv4 mientras se manejan las direcciones IPv6 de manera diferente.

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

Al ejecutar `ssh root@192.168.1.3`, la siguiente salida muestra cómo el cliente SSH aplica las opciones de configuración del archivo `~/.ssh/config`:

```bash
debug1: Leyendo datos de configuración /Users/lzwjava/.ssh/config
debug1: /Users/lzwjava/.ssh/config línea 1: Aplicando opciones para 192.168.1.*
debug1: /Users/lzwjava/.ssh/config línea 5: Aplicando opciones para *.*.*.*
debug2: add_identity_file: ignorando clave duplicada ~/.ssh/id_rsa
debug1: /Users/lzwjava/.ssh/config línea 10: Aplicando opciones para *
debug2: add_identity_file: ignorando clave duplicada ~/.ssh/id_rsa
debug1: Leyendo datos de configuración /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config línea 21: include /etc/ssh/ssh_config.d/* no coincidió con ningún archivo
debug1: /etc/ssh/ssh_config línea 54: Aplicando opciones para *
debug2: resolve_canonicalize: el nombre de host 192.168.1.3 es una dirección
debug3: expandido UserKnownHostsFile '~/.ssh/known_hosts' -> '/Users/lzwjava/.ssh/known_hosts'
debug3: expandido UserKnownHostsFile '~/.ssh/known_hosts2' -> '/Users/lzwjava/.ssh/known_hosts2'
debug1: El proveedor de autenticación $SSH_SK_PROVIDER no se resolvió; deshabilitando
debug3: channel_clear_timeouts: limpiando
debug1: Ejecutando comando proxy: exec corkscrew localhost 7890 192.168.1.3 22
```

La velocidad de la conexión SSH era notablemente lenta, por lo que volví a la siguiente configuración más simple:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
```

El problema surge al usar direcciones IPv6 con la directiva `ProxyCommand corkscrew localhost 7890 %h %p`, ya que este comando proxy puede no manejar correctamente las direcciones IPv6.

La configuración anterior sigue sin funcionar. Sin embargo, la siguiente sí funciona:

```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
Host !192.*.*.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```

---

## Mejorar la Velocidad del Wifi

### Problemas con el Módem Antiguo

En la casa de mis padres, el módem es bastante antiguo, probablemente de unos 10 años. La configuración inicial de la red era:

módem -> 3m inalámbrico -> TP-Link AX3000 (modo puente inalámbrico) -> 2m, una pared, inalámbrico -> Portátil

Esto resultó en una baja velocidad de descarga, con un resultado en Speedtest de solo 10 Mbps.

Una configuración mejorada implicó el uso de una conexión por cable:

módem -> 2m cable -> TP-Link AX3000 (modo puente cableado) -> 4m inalámbrico, una pared -> Portátil

Esto mejoró la velocidad de descarga hasta 90 Mbps.

### Rendimiento del Nuevo Módem

En mi propia casa, el módem es nuevo y el enrutador TP-Link funciona bien en modo puente inalámbrico. La configuración de la red es:

módem -> 4m inalámbrico -> TP-Link AX3000 (modo puente inalámbrico) -> 2m inalámbrico -> Portátil

La calidad de la red es buena.

### Consejos para Solución de Problemas

No hay una única solución para mejorar la velocidad del Wi-Fi. Un buen enfoque es usar un cable para probar cada parte de la red e identificar cuellos de botella. Compara las velocidades al usar una conexión por cable versus Wi-Fi. También, intenta conectar dispositivos directamente con un cable para ver si mejora el rendimiento.

---

## Reinicio de OpenWrt

### Reinicio mediante la Interfaz Web

Se recomienda conectarse al enrutador mediante un cable Ethernet. Después de un reinicio, el SSID del Wi-Fi volverá a sus configuraciones predeterminadas, lo que puede no ser lo que esperas.

### Reinicio mediante Línea de Comandos (SSH)

Puedes restablecer OpenWrt a sus configuraciones predeterminadas usando la interfaz de línea de comandos (SSH). Así es cómo:

1. Conéctate a tu enrutador OpenWrt mediante SSH.
2. Ejecuta el siguiente comando:

    ```bash
    root@OpenWrt:~# firstboot
    Esto borrará todas las configuraciones y eliminará cualquier paquete instalado. ¿Estás seguro? [N/y]
    y
    /dev/ubi0_1 está montado como /overlay, solo se borrarán los archivos
    root@OpenWrt:~# reboot
    ```
3. El enrutador se reiniciará con los valores predeterminados.

**Explicación de los comandos:**

* `firstboot`: Este comando inicia el proceso de reinicio, borrando todas las configuraciones y paquetes instalados.
* `reboot`: Este comando reinicia el enrutador, aplicando el reinicio.