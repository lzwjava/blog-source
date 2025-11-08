---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Rôles client et serveur DHCP
translated: true
type: note
---

Non, c'est une confusion fréquente, mais DHCP n'a pas besoin de "fonctionner" de la même manière sur le client et le routeur — c'est un protocole client-serveur avec des rôles distincts de chaque côté. Laissez-moi vous l'expliquer simplement.

### Aperçu Rapide de DHCP
DHCP (Dynamic Host Configuration Protocol) automatise l'attribution des adresses IP et d'autres paramètres réseau (comme le masque de sous-réseau, la passerelle, le DNS) aux appareils sur un réseau. Il élimine la configuration manuelle.

### Rôles dans une Configuration Typique
- **Routeur (ou Serveur DHCP)** : Exécute le logiciel **serveur DHCP**. C'est le "patron" qui distribue les adresses IP à partir d'un pool qu'il gère. La plupart des routeurs domestiques/SOHO (par exemple, de TP-Link, Netgear) l'ont intégré et activé par défaut.
- **Client (par exemple, votre ordinateur portable, téléphone, PC)** : Exécute un **client DHCP** (intégré au système d'exploitation, comme `dhclient` sur Linux ou la configuration IP automatique de Windows). Celui-ci demande une IP au serveur mais ne sert pas d'IP aux autres.

Les deux côtés sont essentiels pour la poignée de main, mais ils n'exécutent pas des processus "DHCP" identiques — l'un sert, l'autre demande.

### Comment Cela Fonctionne (Flux de Base)
1. **Le client diffuse "DISCOVER"** : Un nouvel appareil rejoint le réseau et crie, "Hé, quelqu'un a une IP pour moi ?"
2. **Le serveur (routeur) propose "OFFER"** : "Bien sûr, voici une IP disponible et les paramètres."
3. **Le client demande "REQUEST"** : "Je prends celle-là, s'il vous plaît."
4. **Le serveur accuse réception "ACK"** : "Fait — utilisez-la."

Si le serveur DHCP du routeur est désactivé, les clients peuvent avoir besoin d'IP statiques ou d'un autre serveur (par exemple, sur un Pi-hole ou dans un environnement d'entreprise).

### Scénarios Courants

| Configuration | Emplacement du Serveur DHCP | Comportement du Client |
|-------|----------------------|-----------------|
| **Réseau Domestique** | Routeur (activé) | Configure tout automatiquement |
| **Pas de DHCP sur le Routeur** | IPs manuelles/statiques ou serveur externe | Le client revient à APIPA (169.254.x.x) s'il n'y a pas de réponse |
| **Entreprise** | Serveur DHCP dédié (pas le routeur) | Même processus de demande du client |

Si vous dépannez un problème spécifique (par exemple, "Mon appareil n'obtient pas d'IP"), partagez plus de détails — je peux aider à déboguer ! Pour une lecture plus approfondie, consultez le RFC officiel : [RFC 2131: Dynamic Host Configuration Protocol](https://datatracker.ietf.org/doc/html/rfc2131).