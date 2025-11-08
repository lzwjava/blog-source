---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Traduction d'adresse réseau expliquée brièvement
translated: true
type: note
---

### Qu'est-ce que la NAT (Network Address Translation) ?

La NAT est une technique de mise en réseau utilisée pour modifier les adresses IP (et parfois les numéros de port) dans les en-têtes des paquets lorsqu'ils traversent un routeur ou un pare-feu. Son objectif principal est de permettre à plusieurs appareils sur un réseau privé (local) de partager une seule adresse IP publique lors de la connexion à Internet. Cela permet de préserver les adresses IP publiques, d'améliorer la sécurité en masquant les détails du réseau interne et de permettre aux réseaux privés de communiquer avec l'Internet public.

Il existe quelques types courants de NAT :
- **Source NAT (SNAT)** : Traduit l'adresse IP source des paquets sortants (par exemple, d'une IP privée à une IP publique).
- **Destination NAT (DNAT)** : Traduit l'adresse IP de destination des paquets entrants (par exemple, pour acheminer le trafic vers un serveur interne spécifique).
- **Port Address Translation (PAT)** : Une variante de la SNAT qui remappe également les ports, permettant à de nombreux appareils privés de partager une seule IP publique.

La NAT est généralement mise en œuvre sur des routeurs, des pare-feux ou des passerelles.

### La NAT traduit-elle les adresses locales (par exemple, 192.168.0.x) vers un autre sous-réseau ?

Oui, exactement — c'est l'une de ses fonctions principales. Les plages d'adresses IP privées comme 192.168.0.x (ou 10.0.0.x, 172.16-31.x.x) ne sont pas routables sur l'Internet public (selon la RFC 1918). Lorsqu'un appareil sur votre réseau local domestique ou de bureau (par exemple, 192.168.0.10) envoie du trafic sortant :

1.  Le dispositif NAT (comme votre routeur) change l'adresse IP source de l'adresse privée (192.168.0.10) pour sa propre adresse IP publique (par exemple, quelque chose comme 203.0.113.5 dans un sous-réseau différent).
2.  Il suit également la combinaison IP/port d'origine pour réécrire correctement les réponses entrantes.
3.  Cette « traduction » se produit dynamiquement pour le trafic sortant, donnant l'impression que tous vos appareils proviennent d'une seule adresse publique.

Pour le trafic entrant (par exemple, pour héberger un serveur), vous auriez besoin d'une configuration supplémentaire comme la redirection de port (une forme de DNAT) pour mapper l'adresse IP publique vers une adresse IP privée spécifique.

### La NAT dans Windows XP

Vous avez tout à fait raison — Windows XP incluait une prise en charge intégrée de la NAT via le **Partage de connexion Internet (ICS)**. Cela vous permettait de partager une connexion Internet d'un PC (agissant comme une passerelle) vers d'autres sur un réseau local. L'ICS utilisait la NAT pour traduire les adresses IP privées (par exemple, du réseau partagé) en l'adresse IP publique du PC hôte. C'était un moyen simple de configurer un mini-réseau domestique avant que les routeurs grand public ne deviennent omniprésents. Vous pouviez l'activer dans les paramètres des Connexions réseau, et il attribuait même automatiquement des adresses IP DHCP comme 192.168.0.x.

### Le programme "Huasheng Ke" en Chine (Exposer les serveurs locaux)

Je pense que vous faites référence à **花生壳 (Huāshēngké)**, communément appelé **Peanut Shell** — un service populaire de DNS dynamique (DDNS) en Chine (et dans le monde). Ce n'est pas la NAT elle-même, mais il fonctionne *avec* la NAT pour résoudre le problème « d'exposition de l'ordinateur local en tant que serveur » que vous avez mentionné.

-   Derrière une NAT (par exemple, sur un routeur domestique), votre serveur local (disons, un serveur web sur 192.168.0.50:80) n'est pas directement accessible depuis Internet en raison de l'adresse IP privée.
-   Peanut Shell fournit un nom de domaine (par exemple, yourserver.peanuthull.com) qui se met à jour dynamiquement pour pointer vers votre adresse IP publique. Combiné à la redirection de port sur votre routeur, il « perce » la NAT pour permettre à votre machine locale de servir de serveur public (pour des sites web, des jeux, le partage de fichiers, etc.).
-   C'est particulièrement utile dans les régions où les adresses IP publiques sont dynamiques ou où les configurations NAT sont strictes, et cela existe depuis le début des années 2000, à l'instar de services comme No-IP ou DynDNS.

Si ce n'est pas le programme exact auquel vous pensiez, n'hésitez pas à clarifier !

### La NAT dans AWS

AWS utilise largement la NAT pour la mise en réseau dans le cloud :
- **NAT Gateway** : Un service managé dans un sous-réseau public qui permet aux instances dans des sous-réseaux privés (par exemple, avec des adresses IP privées comme 10.0.1.x) d'initier un accès Internet sortant (par exemple, pour des mises à jour logicielles) sans les exposer directement. Il traduit les adresses IP sources privées en l'adresse IP publique élastique (Elastic IP) de la passerelle.
- **NAT Instance** : Une alternative DIY utilisant une instance EC2 comme routeur NAT (moins courant aujourd'hui).
- Cela permet de garder vos ressources privées sécurisées tout en permettant un trafic sortant unidirectionnel — parfait pour les VPC (Virtual Private Clouds).

En bref, la NAT est omniprésente dans les réseaux modernes pour relier efficacement les mondes privé et public. Si vous avez une configuration ou un scénario spécifique en tête (par exemple, du dépannage), je peux approfondir !