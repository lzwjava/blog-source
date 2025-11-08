---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre la sortie de ip addr show enp4s0
translated: true
type: note
---

### Décortiquer votre sortie `ip addr show enp4s0`

Cette commande affiche des informations détaillées sur votre interface Ethernet (enp4s0), celle qui gère votre connexion LAN locale d'après la table de routage dont nous avons parlé. Elle est active et fonctionne correctement—parfait pour la connectivité de base. Je vais l'analyser ligne par ligne, puis résumer.

#### Sections Clés Expliquées
- **État de l'Interface** :  
  `2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000`  
  - Index 2 (deuxième interface, après lo).  
  - Drapeaux : Prend en charge la diffusion/broadcast et multidiffusion/multicast, complètement UP (lien détecté et opérationnel).  
  - MTU : 1500 octets (taille de trame Ethernet standard—pas de jumbo frames).  
  - Discipline de file d'attente : fq_codel (file d'attente équitable pour un trafic à faible latence, courant sur les systèmes Linux modernes).  
  - État : UP (prête à envoyer/recevoir).

- **Couche de Liaison (Adresse MAC)** :  
  `link/ether 04:7c:16:d9:54:5b brd ff:ff:ff:ff:ff:ff`  
  - Votre adresse MAC matérielle : 04:7c:16:d9:54:5b (unique à cette carte réseau).  
  - Broadcast : ff:ff:ff:ff:ff:ff (tous les bits à 1 pour les broadcasts Ethernet).

- **Adresse IPv4** :  
  `inet 192.168.1.35/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0`  
  `valid_lft 4790sec preferred_lft 4790sec`  
  - IP : 192.168.1.35 avec un sous-réseau /24 (masque 255.255.255.0). Correspond au "src 192.168.1.35" dans votre table de routage.  
  - Broadcast : 192.168.1.255 (pour les broadcasts à l'échelle du sous-réseau).  
  - Portée/Scope : global (routable au-delà de cet hôte).  
  - Dynamique : Attribuée via DHCP (par votre routeur à 192.168.1.1).  
  - No prefix route : N'ajoute pas automatiquement une route connectée (mais le noyau l'a fait quand même, comme vu dans `ip route`).  
  - Bail : Environ 79 minutes restantes (4790 secondes) avant le renouvellement.

- **Adresse IPv6** :  
  `inet6 fe80::a884:a0f6:e8b4:4a7d/64 scope link noprefixroute`  
  `valid_lft forever preferred_lft forever`  
  - IPv6 link-local : fe80::... (générée automatiquement à partir de l'adresse MAC ; uniquement pour la communication locale sur le lien, comme la découverte de voisins).  
  - Préfixe /64, portée/scope link (non routable en dehors de cette interface).  
  - Permanente (pas d'expiration).

#### Tableau Récapitulatif Rapide

| Aspect       | Valeur/Détails                  | Signification |
|--------------|--------------------------------|---------------|
| **Statut**  | UP, MTU 1500                  | L'interface est active et traite les paquets standard. |
| **MAC**     | 04:7c:16:d9:54:5b             | L'adresse matérielle de votre appareil sur le câble. |
| **IPv4**    | 192.168.1.35/24 (DHCP)        | IP LAN locale ; les routes vers ce sous-réseau restent sur enp4s0. |
| **IPv6**    | fe80::a884:a0f6:e8b4:4a7d/64  | IPv6 locale uniquement ; utile pour les fonctions voisines IPv6. |
| **Bail**   | ~79 min restantes             | Le DHCP va bientôt actualiser—vérifiez avec `dhclient -r enp4s0 && dhclient enp4s0` si nécessaire. |

Cette configuration explique pourquoi votre route par défaut pointe ici pour l'accès à Internet et pourquoi le trafic local 192.168.1.x est direct. Si vous effectuez un ping dans le LAN, il utilisera ARP pour trouver l'adresse MAC et enverra les trames via cette interface.

Est-ce que tout semble bon, ou y a-t-il un problème (par exemple, pas d'adresse IPv6 globale, ou des coupures de connectivité) ? Si vous partagez `ip addr` pour d'autres interfaces ou les résultats d'un `ping`, je peux creuser davantage. Quelle est la suite—tester les bridges Docker, ou autre chose ?