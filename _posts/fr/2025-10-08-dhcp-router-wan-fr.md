---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Journaux DHCP pour l'interface WAN du routeur
translated: true
type: note
---

### Comprendre les entrées de log DHCP dans le routeur Wi-Fi 360 T7

Cet extrait de log de votre routeur 360 T7 (probablement extrait de la section **Système > Log** dans l'interface web) montre l'interface WAN du routeur agissant comme un client DHCP pour obtenir et renouveler son adresse IP publique auprès du serveur DHCP de votre FAI. Le DHCP (Dynamic Host Configuration Protocol) est le protocole standard pour l'attribution automatique d'adresses IP sur les réseaux. Le routeur demande ou renouvelle périodiquement un bail IP pour maintenir la connectivité Internet—généralement toutes les 12 à 24 heures, selon la durée du bail définie par votre FAI.

Ces entrées sont **normales et indiquent un fonctionnement sain**, et non une erreur. Elles représentent le processus DORA standard (Discover, Offer, Request, ACK) pour l'attribution initiale de l'IP, suivi des renouvellements de bail. Voici une explication de chaque ligne dans l'ordre chronologique (note : les horodatages sont dans l'ordre inverse dans votre log, mais je les ai réorganisés pour plus de clarté ; les dates sont au format AAAA/MM/JJ-HH:MM:SS) :

| ID Log | Horodatage         | Message                  | Explication |
|--------|--------------------|--------------------------|-------------|
| 148   | 2025/09/19-03:44:57 | Envoi de la découverte DHCP | Le routeur diffuse un message **DHCP Discover** sur le côté WAN pour localiser un serveur DHCP disponible (celui de votre FAI). C'est la première étape lorsque le bail expire ou que le routeur redémarre. (Il réessaie rapidement à la ligne suivante.) |
| 147   | 2025/09/19-03:45:00 | Envoi de la découverte DHCP | Une nouvelle tentative du message Discover (courant s'il n'y a pas de réponse immédiate ; les routeurs envoient 2 à 4 nouvelles tentatives avec un backoff exponentiel). |
| 146   | 2025/09/19-03:45:02 | Offre DHCP reçue     | Le serveur DHCP du FAI répond avec une **DHCP Offer**, proposant une adresse IP disponible, un masque de sous-réseau, une passerelle, des serveurs DNS et une durée de bail (par exemple, 24 heures). |
| 145   | 2025/09/19-03:45:02 | Envoi de la requête DHCP    | Le routeur envoie une **DHCP Request** pour accepter l'IP offerte et demander formellement au serveur de l'attribuer (diffusion pour que les autres serveurs puissent retirer leurs offres le cas échéant). |
| 144   | 2025/09/19-03:45:02 | ACK DHCP reçu       | Le serveur envoie un **DHCP ACK** (Accusé de réception), confirmant l'attribution de l'IP. Le routeur a maintenant une IP WAN valide et peut se connecter à Internet. Ceci termine l'acquisition initiale du bail (~5 secondes au total ici). |
| 143   | 2025/09/19-15:45:02 | Envoi du renouvellement DHCP      | ~12 heures plus tard (à mi-parcours d'un bail typique de 24 heures), le routeur envoie proactivement un **DHCP Renew** (une Request unicast au serveur connu) pour étendre le bail sans redécouverte complète. |
| 142   | 2025/09/19-15:45:02 | ACK DHCP reçu       | Le serveur accuse réception du renouvellement—le bail est prolongé de manière transparente. |
| 141   | 2025/09/20-03:45:02 | Envoi du renouvellement DHCP      | Un autre renouvellement ~12 heures plus tard (maintenant le jour suivant). Si aucun ACK ne suit (non montré ici), il pourrait escalader vers un rebind complet ou une redécouverte. |

#### Pourquoi cela se produit
- **Cycle de bail** : Les FAI définissent des durées de bail (par exemple, 24 heures). À 50% du temps écoulé, le client renouvelle pour éviter les interruptions. Si le renouvellement échoue à 87,5%, il effectue un rebind (Request en diffusion) ; à 100%, il redémarre le processus DORA complet.
- **Dans le contexte du 360 T7** : Ceci est journalisé sous les événements de connexion WAN. Le T7 utilise un client DHCP léger (probablement basé sur udhcpc) dans son firmware, qui génère ces messages exacts. Aucun problème à moins que vous ne voyiez des échecs comme "DHCP NAK received" (IP rejetée) ou des Discover répétés sans ACK (pourrait indiquer des problèmes de FAI ou de câble).
- **Conseils de dépannage** :
  - Si Internet se coupe autour de ces heures, vérifiez le statut WAN dans l'interface (**Statut > WAN**) pour des changements d'IP ou des erreurs.
  - Exportez les logs complets via l'interface pour analyser les modèles.
  - Pour forcer un renouvellement : Libérez/renouvelez le WAN dans **Réseau > WAN** ou redémarrez le routeur.

Il s'agit d'un comportement de routine—votre routeur maintient simplement son "ticket Internet" valide.

[Comprendre les bases du DHCP (Microsoft)](https://learn.microsoft.com/en-us/windows-server/troubleshoot/dynamic-host-configuration-protocol-basics)  
[Aperçu du processus DHCP (Netmanias)](https://www.netmanias.com/en/post/techdocs/5998/dhcp-network-protocol/understanding-the-basic-operations-of-dhcp)