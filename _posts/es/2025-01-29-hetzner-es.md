---
audio: true
lang: es
layout: post
title: Hetzner Nube
translated: true
---

Estoy muy emocionado de probar esta plataforma en la nube recientemente.

{: .centered }
![](assets/images/hertzner/h.jpg)
*Fuente: Hetzner*{: .caption }

Un servidor en Helsinki con una configuración de 2 AMD VCPUs, 2GB de RAM, 40GB SSD y 20TB de tráfico cuesta $4.49 USD al mes.

Una dirección IPv4 cuesta adicionalmente $0.60 USD al mes, lo que eleva el total a $5.09 USD al mes.

Ofrecen servicios en seis ubicaciones:

- Núremberg, Alemania
- Falkenstein, Alemania
- Helsinki, Finlandia
- Singapur, Singapur
- Hillsboro, OR, EE. UU.
- Ashburn, VA, EE. UU.

Es interesante que no sigan las tendencias para seleccionar ubicaciones populares. Sus ubicaciones son diferentes a las de Vultr o Digital Ocean.

Las configuraciones del firewall son fáciles de usar. Aunque esta fue mi primera vez usándolo, rápidamente configuré la configuración correcta para mi servidor proxy.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

La velocidad del servidor de Hetzner en Helsinki es muy rápida. Usando la aplicación Speedtest iOS, la velocidad de descarga es de 423 Mbps y la velocidad de subida es de 56.1 Mbps.

El ping en Shadowrocket es de 1175 ms, pero esto no es un problema significativo.

Un simple script de Python para obtener detalles de la instancia del servidor.

```python
from hcloud import Client
import os

# Obtener el token API de la variable de entorno
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Error: HERTZNER_API_KEY variable de entorno no establecida.")
    exit(1)

# Crear una instancia del cliente
client = Client(token=api_token)

# Listar todos los servidores
servers = client.servers.get_all()

# Imprimir detalles del servidor
for server in servers:
    print(f"ID del servidor: {server.id}")
    print(f"Nombre del servidor: {server.name}")
    print(f"Estado del servidor: {server.status}")
    print(f"IPv4 del servidor: {server.public_net.ipv4.ip}")
    print(f"IPv6 del servidor: {server.public_net.ipv6.ip}")
    print(f"Tipo de servidor: {server.server_type.name}")
    print(f"Ubicación del servidor: {server.datacenter.location.name}")
    print("----------------------------------")

# Para obtener un servidor específico por ID
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"ID del servidor específico: {server.id}")
print(f"Nombre del servidor específico: {server.name}")
print(f"Estado del servidor específico: {server.status}")
print(f"IPv4 del servidor específico: {server.public_net.ipv4.ip}")
print(f"IPv6 del servidor específico: {server.public_net.ipv6.ip}")
print(f"Tipo del servidor específico: {server.server_type.name}")
print(f"Ubicación del servidor específico: {server.datacenter.location.name}")
```