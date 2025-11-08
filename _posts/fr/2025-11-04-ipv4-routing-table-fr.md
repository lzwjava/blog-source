---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre la sortie de la table de routage IPv4
translated: true
type: note
---

### Comprendre votre sortie `ip route`

Il s'agit de la table de routage IPv4 de votre système Linux (utilisant probablement la commande `ip` d'iproute2). Elle montre comment votre machine décide où envoyer les paquets en fonction des IPs de destination. Les routes sont comparées par le préfixe le plus long (le plus spécifique en premier), et la route par défaut attrape tout le reste.

Je vais la décomposer entrée par entrée dans un tableau pour plus de clarté, puis résumer ce que cela signifie globalement. Cela fait écho à notre discussion précédente : c'est un exemple concret d'une table de routage simple avec des routes connectées (sous-réseaux locaux) et une passerelle par défaut pour Internet.

| Destination       | Passerelle (Next Hop) | Interface | Protocole | Portée | IP Source     | Métrique | Notes |
|-------------------|--------------------|-----------|----------|-------|---------------|--------|-------|
| **0.0.0.0/0** (par défaut) | 192.168.1.1       | enp4s0   | dhcp    | global| (aucune)       | 100   | Tout le trafic ne correspondant pas aux autres routes va ici. Pointe vers votre routeur (probablement votre passerelle domestique) sur l'interface Ethernet enp4s0. Découverte via DHCP. |
| **169.254.0.0/16** | (direct)          | enp4s0   | kernel  | link  | (aucune)       | 1000  | Plage link-local (APIPA) pour l'auto-configuration en cas d'échec DHCP. La métrique élevée signifie que c'est une solution de repli—utilisée seulement si aucune meilleure route n'est disponible. |
| **172.17.0.0/16** | (direct)          | docker0  | kernel  | link  | 172.17.0.1   | (aucune)| Le réseau bridge par défaut de Docker. "linkdown" signifie que l'interface est inactive (aucun conteneur actif ?). Votre hôte agit comme passerelle pour ce sous-réseau. |
| **172.18.0.0/16** | (direct)          | br-c33e38e216df | kernel | link  | 172.18.0.1   | (aucune)| Un autre bridge Docker (réseau défini par l'utilisateur ?). Actif, donc les conteneurs sur ce bridge peuvent atteindre l'hôte via 172.18.0.1. |
| **192.168.1.0/24** | (direct)         | enp4s0   | kernel  | link  | 192.168.1.35 | 100   | Votre sous-réseau LAN local. Directement connecté via enp4s0—les paquets destinés à d'autres appareils sur 192.168.1.x restent locaux (par exemple, vers votre routeur en .1). L'IP de votre machine est 192.168.1.35. |

#### Points Clés
- **Routes Locales/Connectées** : Les entrées 172.x.x.x et 192.168.1.0/24 sont des routes "kernel" pour les réseaux directement attachés (aucune passerelle next-hop nécessaire). Cela correspond à l'itération simple que vous avez décrite—votre système vérifie si l'IP de destination se trouve dans ces plages et l'envoie via l'interface correspondante (par exemple, enp4s0 pour le LAN).
- **Influence de Docker** : Vous avez Docker installé/en cours d'exécution, créant des bridges virtuels (docker0 et br-...). Ceux-ci permettent aux conteneurs d'avoir leurs propres réseaux isolés. Le "linkdown" sur docker0 suggère qu'aucun conteneur n'utilise le bridge par défaut actuellement.
- **Route par Défaut** : Tout le reste (par exemple, google.com) passe par 192.168.1.1 sur enp4s0. La métrique 100 est faible (préférée) ; la route link-local a 1000 pour la déprioriser.
- **Aucune Route Distante** : Cette table est basique—aucun protocole de routage dynamique (comme OSPF) n'ajoute d'entrées pour des réseaux distants. Si vous pinguez quelque chose en dehors de 192.168.1.0/24, cela utilisera la route par défaut.

#### Tests Rapides pour Vérifier
- `ping 192.168.1.1` → Devrait utiliser la route locale sur enp4s0.
- `ping 8.8.8.8` → Utilise la route par défaut ; tracez avec `traceroute 8.8.8.8` pour voir le chemin.
- `ip addr show enp4s0` → Confirme l'IP de votre interface.
- Si Docker est impliqué : `docker network ls` pour lister les bridges.

Si cela provient de votre configuration et que quelque chose ne fonctionne pas (par exemple, pas d'Internet ?), correctifs courants : Vérifiez le câble/renouvellement DHCP (`dhclient enp4s0`), ou videz le cache des routes (`ip route flush cache`). Que se passe-t-il—dépannage de connectivité, ou simplement curieux à propos d'une entrée spécifique ?