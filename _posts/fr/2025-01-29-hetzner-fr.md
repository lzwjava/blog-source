---
audio: false
generated: true
lang: fr
layout: post
title: Hetzner Cloud
translated: true
---

Je suis très enthousiaste à l'idée d'essayer cette plateforme cloud récemment.

{: .centered }
![](assets/images/hertzner/h.jpg)
*Source: Hetzner*{: .caption }

Un serveur à Helsinki avec une configuration de 2 AMD VCPUs, 2 Go de RAM, 40 Go SSD, et 20 To de trafic coûte 4,49 USD par mois.

Une adresse IPv4 coûte 0,60 USD supplémentaire par mois, portant le total à 5,09 USD par mois.

Ils fournissent des services dans six emplacements :

- Nuremberg, Allemagne
- Falkenstein, Allemagne
- Helsinki, Finlande
- Singapour, Singapour
- Hillsboro, OR, USA
- Ashburn, VA, USA

Il est intéressant de noter qu'ils ne suivent pas les tendances pour sélectionner des emplacements populaires. Leurs emplacements sont différents de ceux de Vultr ou Digital Ocean.

Les paramètres de pare-feu sont faciles à utiliser. Bien que ce soit la première fois que je les utilise, j'ai rapidement configuré la configuration correcte pour mon serveur proxy.

> sudo bash -c "$(wget -qO- https://raw.githubusercontent.com/Jigsaw-Code/outline-server/master/src/server_manager/install_scripts/install_server.sh)"

La vitesse du serveur Hetzner à Helsinki est très rapide. En utilisant l'application Speedtest iOS, la vitesse de téléchargement est de 423 Mbps et la vitesse de téléchargement de 56,1 Mbps.

Le ping dans Shadowrocket est de 1175 ms, mais ce n'est pas un problème significatif.

Un script Python simple pour obtenir les détails de l'instance du serveur.

```python
from hcloud import Client
import os

# Récupérer le jeton API à partir de la variable d'environnement
api_token = os.environ.get('HERTZNER_API_KEY')

if not api_token:
    print("Erreur: la variable d'environnement HERTZNER_API_KEY n'est pas définie.")
    exit(1)

# Créer une instance de client
client = Client(token=api_token)

# Lister tous les serveurs
servers = client.servers.get_all()

# Imprimer les détails du serveur
for server in servers:
    print(f"ID du serveur: {server.id}")
    print(f"Nom du serveur: {server.name}")
    print(f"Statut du serveur: {server.status}")
    print(f"IPv4 du serveur: {server.public_net.ipv4.ip}")
    print(f"IPv6 du serveur: {server.public_net.ipv6.ip}")
    print(f"Type de serveur: {server.server_type.name}")
    print(f"Emplacement du serveur: {server.datacenter.location.name}")
    print("----------------------------------")

# Pour obtenir un serveur spécifique par ID
server_id = '59402674'
server = client.servers.get_by_id(server_id)

print(f"ID du serveur spécifique: {server.id}")
print(f"Nom du serveur spécifique: {server.name}")
print(f"Statut du serveur spécifique: {server.status}")
print(f"IPv4 du serveur spécifique: {server.public_net.ipv4.ip}")
print(f"IPv6 du serveur spécifique: {server.public_net.ipv6.ip}")
print(f"Type de serveur spécifique: {server.server_type.name}")
print(f"Emplacement du serveur spécifique: {server.datacenter.location.name}")

```