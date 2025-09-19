---
audio: false
generated: false
image: true
lang: es
layout: post
title: Hetzner Cloud
translated: true
---

Estoy muy emocionado de probar esta plataforma en la nube recientemente.

{: .centered }
![](assets/images/hertzner/h.jpg)
*Fuente: Hetzner*{: .caption }

Un servidor en Helsinki con una configuración de 2 AMD VCPUs, 2GB RAM, 40GB SSD y 20TB de tráfico cuesta 4.49 USD al mes.

Una dirección IPv4 cuesta un adicional de 0.60 USD al mes, llevando el total a 5.09 USD al mes.

Ofrecen servicios en seis ubicaciones:

- Núremberg, Alemania
- Falkenstein, Alemania
- Helsinki, Finlandia
- Singapur, Singapur
- Hillsboro, OR, EE.UU.
- Ashburn, VA, EE.UU.

Es interesante que no sigan las tendencias para seleccionar ubicaciones populares. Sus ubicaciones son diferentes de las de Vultr o Digital Ocean.

La configuración del firewall es fácil de usar. Aunque esto fue mi primera vez usándolo, rápidamente configuré la configuración correcta para mi servidor proxy.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

La velocidad del servidor de Hetzner en Helsinki es muy rápida. Usando la aplicación Speedtest iOS, la velocidad de descarga es de 423 Mbps y la velocidad de subida es de 56.1 Mbps.

El ping en Shadowrocket es de 1175 ms, pero esto no es un problema significativo.

Un sencillo script en Python para obtener detalles de la instancia del servidor.

```python
from hcloud import Client
import os

# Obtener la clave API desde la variable de entorno
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY environment variable not set.")
    exit(1)

# Crear una instancia del cliente
cliente = Client(token=api_token)

# Listar todos los servidores
servidores = cliente.servers.get_all()

# Imprimir detalles del servidor
for servidor in servidores:
    print(f"ID del servidor: {servidor.id}")
    print(f"Nombre del servidor: {servidor.name}")
    print(f"Estado del servidor: {servidor.status}")
    print(f"IPv4 del servidor: {servidor.public_net.ipv4.ip}")
    print(f"IPv6 del servidor: {servidor.public_net.ipv6.ip}")
    print(f"Tipo de servidor: {servidor.server_type.name}")
    print(f"Ubicación del servidor: {servidor.datacenter.location.name}")
    print("----------------------------------")

# Si desea obtener un servidor específico por ID
id_servidor = '59402674'
servidor = cliente.servers.get_by_id(id_servidor)

print(f"ID del servidor específico: {servidor.id}")
print(f"Nombre del servidor específico: {servidor.name}")
print(f"Estado del servidor específico: {servidor.status}")
print(f"IPv4 del servidor específico: {servidor.public_net.ipv4.ip}")
print(f"IPv6 del servidor específico: {servidor.public_net.ipv6.ip}")
print(f"Tipo del servidor específico: {servidor.server_type.name}")
print(f"Ubicación del servidor específico: {servidor.datacenter.location.name}")
```