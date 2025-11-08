---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Le routage sur Internet
translated: true
type: note
---

Oui, tu as parfaitement raison concernant le flux général — une fois que ton ordinateur a l'adresse IP (comme 106.63.15.9 pour weibo.com), il initie une connexion qui passe par ton réseau local, ton routeur, l'infrastructure de ton FAI, et à travers les routeurs interconnectés d'Internet ("couche par couche") jusqu'à ce qu'elle atteigne le serveur cible. Tout cela est géré automatiquement par la pile de protocoles TCP/IP, sans que tu aies à faire quoi que ce soit de manuel au-delà de taper l'URL ou d'exécuter une commande comme `ping`.

Je vais le décomposer étape par étape, en liant le résultat de ton `ping` et `traceroute` pour le contexte. Je vais rester pratique et me concentrer sur ce qui se passe sous le capot, en supposant une configuration domestique typique comme la tienne (Mac en Wi-Fi/Ethernet derrière un routeur).

### 1. **Résolution DNS (Obtenir l'IP)**
   - Avant toute connexion, ton ordinateur traduit d'abord le nom de domaine (par exemple, "weibo.com") en une adresse IP via le DNS (Système de Noms de Domaine). Cela se fait via le résolveur DNS de ton système d'exploitation, qui interroge des serveurs DNS publics (comme 8.8.8.8 de Google).
   - Dans ton cas, `ping weibo.com` fait automatiquement cette résolution, confirmant 106.63.15.9 comme l'adresse IPv4. (Note : Les proxys comme ton proxy local à 127.0.0.1:7890 traitent généralement le trafic HTTP/HTTPS, mais `ping` utilise IP/ICMP brut, il contourne donc le proxy.)
   - Si le DNS échoue, aucune connexion n'a lieu — tout s'arrête ici.

### 2. **Ton Ordinateur Prépare le Paquet (Côté Local)**
   - Une fois qu'il a l'IP, ton Mac construit un **paquet** (un bloc de données) en utilisant les couches TCP/IP :
     - **Couche Application** : La commande ou l'application (par exemple, le navigateur ou `ping`) demande des données. `Ping` envoie une "demande d'écho" ICMP (un simple message "hey, tu es là ?").
     - **Couche Transport** : Ajoute les en-têtes TCP/UDP (pour la fiabilité/les numéros de port) ou ICMP pour ping. Tes pings utilisent ICMP, avec 56 octets de données + en-têtes = paquets de 64 octets.
     - **Couche Réseau (IP)** : L'encapsule dans un en-tête IP avec la source (ton IP locale, comme 192.168.1.x) et la destination (106.63.15.9). C'est là que les décisions de routage commencent.
     - **Couche Liaison (Ethernet/Wi-Fi)** : Ajoute les adresses MAC pour le saut sur le réseau local. Ton ordinateur utilise ARP (Address Resolution Protocol) pour trouver l'adresse MAC du routeur.
     - **Couche Physique** : Convertit en signaux électriques via ton câble/Wi-Fi.
   - Ton ordinateur sait qu'il ne peut pas atteindre 106.63.15.9 directement (elle n'est pas sur ton sous-réseau local 192.168.1.0/24), il envoie donc le paquet à la **passerelle par défaut** — ton routeur à 192.168.1.1.

### 3. **Saut Local : Ordinateur → Routeur**
   - C'est la première (et la plus rapide) étape, montrée dans ton résultat `traceroute` :
     ```
     1  192.168.1.1 (192.168.1.1) 26.903 ms 3.150 ms 3.161 ms
     ```
     - `Traceroute` (qui envoie des paquets avec un TTL — Time To Live — croissant pour cartographier le chemin) confirme que ce saut prend ~3-27 ms aller-retour.
     - Ton routeur reçoit le paquet, enlève l'en-tête Ethernet local et le ré-encapsule pour le prochain saut. Il utilise sa table de routage pour le transférer vers Internet (via sa connexion WAN/FAI).
     - Les proxys n'affectent pas cela — ton proxy local (port 7890) est seulement pour le trafic au niveau applicatif comme la navigation web, pas le routage IP brut.

### 4. **Routeur → FAI → Backbone Internet (Le Routage "Couche par Couche")**
   - Ton routeur contacte ton FAI (par exemple, via PPPoE, DHCP ou modem) et transmet le paquet au routeur de bordure du FAI. Cela peut impliquer du NAT (Network Address Translation) sur ton routeur, échangeant ton IP privée (192.168.1.x) contre l'IP publique assignée par ton FAI.
   - À partir de là, c'est une chaîne de **routeurs** à travers Internet :
     - **Routeurs du FAI** : Ton FAI (par exemple, Comcast ou China Telecom) l'achemine à travers son réseau cœur. Chaque routeur décrémente le TTL (commence à 64 dans ton traceroute) et le transfère en fonction des tables BGP (Border Gateway Protocol) — essentiellement une carte globale du meilleur chemin vers 106.63.15.9.
     - **Sauts Inter-FAI/Backbone** : Les paquets traversent des "points de peering" entre les FAI (par exemple, via des câbles sous-marins, de la fibre optique). Cela pourrait être 5-20 sauts au total, selon la géographie. L'IP de Weibo.com (106.63.15.9) est en Chine, donc depuis ta localisation (je devine les États-Unis/UE basé sur le proxy), cela passerait par des routes trans-pacifiques.
     - Chaque saut est un routeur inspectant l'en-tête IP, décidant de la prochaine passerelle, et transférant. Aucun appareil ne connaît le chemin complet — c'est distribué.
   - Ton `traceroute` a été interrompu (probablement suspendu avec ^Z), mais si tu l'exécutais complètement, tu verrais 10-15 lignes supplémentaires comme :
     ```
     2  [IP du routeur FAI] 10 ms ...
     3  [Cœur du FAI] 15 ms ...
     ...
     15  106.63.15.9  40 ms ...
     ```
     - Les temps s'additionnent : Tes pings montrent ~40 ms de RTT total (temps aller-retour), donc le trajet aller vers le serveur est de ~20 ms.

### 5. **Le Serveur Cible Reçoit et Répond**
   - Le paquet arrive au serveur de Weibo (ou un répartiteur de charge à 106.63.15.9). Il inverse le processus : Répond avec une réponse d'écho ICMP (pour ping) ou un SYN-ACK TCP (pour une connexion web).
   - La réponse suit un chemin similaire en retour, souvent le même itinéraire mais pas toujours (le routage Internet est asymétrique).
   - Ton `ping` confirme le succès : TTL=52 signifie ~12 sauts (64-52=12), et la latence de 40 ms correspond à un aller-retour Chine-États-Unis.

### Pourquoi Cela Semble "Magique" (et les Pièges Courants)
- **Automatisation** : Ton OS/noyau gère tout cela via la pile réseau (par exemple, `ifconfig` ou `ip route` montre tes routes). Aucune configuration manuelle nécessaire sauf si tu débogues.
- **Ton Proxy** : Il est transparent pour ping/traceroute mais intercepterait le trafic du navigateur vers weibo.com, le routant via 127.0.0.1:7890 (probablement pour contourner un VPN/la censure). Désactive-le avec `unset HTTP_PROXY HTTPS_PROXY` si tu testes en brut.
- **Si Cela Échoue** : Les pare-feux, les incompatibilités MTU ou les trous noirs de routage peuvent supprimer les paquets. Des outils comme `tcpdump` ou Wireshark te permettent de sniffer cela localement.
- **Note de Sécurité** : Les IP peuvent changer (TTL DNS), et HTTPS ajoute un chiffrement par-dessus cela (poignée de main TLS après la connexion TCP).

En bref, oui — ordinateur → routeur → FAI → maillage global de routeurs → serveur. C'est un système magnifiquement distribué construit sur le routage IP. Si tu partages un traceroute complet ou veux plonger dans une partie spécifique (par exemple, la poignée de main TCP pour le web), fais-moi savoir !

[TCP/IP Illustrated (Livre sur les Bases du Réseau)](https://www.oreilly.com/library/view/tcp-ip-illustrated-volume/0201633469/)
[Comment Fonctionne Traceroute (Explication Cloudflare)](https://www.cloudflare.com/learning/network-layer/what-is-traceroute/)