---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: DNS expliqué simplement
translated: true
type: note
---

### Que signifie DNS ?

DNS signifie **Domain Name System** (Système de Noms de Domaine). C'est essentiellement l'"annuaire" de l'internet (et des réseaux locaux). Il traduit les noms de domaine lisibles par l'homme (comme `www.example.com` ou `google.com`) en adresses IP compréhensibles par les machines (comme `192.0.2.1` ou `8.8.8.8`). Sans le DNS, vous devriez mémoriser et taper des adresses IP brutes pour visiter des sites web, ce qui serait peu pratique.

Le DNS fonctionne de manière hiérarchique : Votre appareil interroge un serveur DNS (un serveur spécialisé qui gère ces recherches), qui soit connaît la réponse, soit transmet la requête plus haut dans la chaîne vers des serveurs faisant autorité jusqu'à ce que le nom soit résolu en une adresse IP.

### Configuration du DNS sur macOS ou Windows

Lorsque vous configurez les paramètres réseau sur macOS (dans Réglages Système > Réseau) ou Windows (dans Paramètres > Réseau et Internet > Ethernet/Wi-Fi > Propriétés), la section **DNS** vous permet de spécifier manuellement des serveurs DNS ou d'utiliser ceux fournis par défaut par votre réseau. Les serveurs par défaut courants incluent :
- Les serveurs DNS de votre FAI.
- Des serveurs publics comme ceux de Google `8.8.8.8` et `8.8.4.4`, ou ceux de Cloudflare `1.1.1.1`.

Si vous laissez le réglage sur "Automatique" (souvent via DHCP, comme vous l'avez mentionné), votre routeur ou votre réseau vous fournit ces serveurs DNS.

Les autres détails que vous avez listés :
- **192.168.1.1** : Il s'agit typiquement de l'adresse IP locale de votre routeur (la "passerelle par défaut"). C'est la porte vers l'internet extérieur depuis votre réseau domestique.
- **IPv4 Utiliser DHCP** : DHCP (Dynamic Host Configuration Protocol) est un service qui attribue automatiquement des adresses IP et d'autres informations réseau aux appareils de votre réseau. "Utiliser DHCP" signifie que votre ordinateur ne choisit pas une IP statique ; au lieu de cela, il demande une adresse IP dynamiquement au serveur DHCP (généralement votre routeur).

### Comment votre ordinateur se connecte au réseau et gère les requêtes IP/hôte

Décomposons le processus étape par étape lorsque votre ordinateur "visite le réseau" (c'est-à-dire se connecte au Wi-Fi ou à l'Ethernet) :

1. **Connexion initiale et négociation DHCP** :
   - Lorsque vous vous connectez, votre ordinateur diffuse une requête de "découverte" DHCP : "Hé, quelqu'un a une adresse IP disponible pour moi ?"
   - Votre **routeur** (agissant comme le serveur DHCP) répond avec une "offre" : "Bien sûr, voici une IP pour toi (par exemple, 192.168.1.100), plus ton masque de sous-réseau (par exemple, 255.255.255.0), ta passerelle par défaut (192.168.1.1) et les IP des serveurs DNS (par exemple, 8.8.8.8)."
   - Votre ordinateur accepte ("demande") et confirme ("accusé de réception"). Maintenant, il a tout ce qu'il faut pour communiquer sur le réseau local.
   - Cela n'implique pas encore le DNS — c'est uniquement pour l'adresse IP de votre appareil et le routage de base. Votre "hôte" (nom d'hôte, comme le nom de votre ordinateur) peut être défini localement sur votre appareil ou enregistré auprès du routeur pour la résolution de noms locale, mais c'est séparé.

2. **Résolution des hôtes (Là où le DNS intervient)** :
   - Une fois connecté, si vous essayez de visiter `www.google.com`, votre ordinateur ne connaît pas encore l'adresse IP. Il envoie une **requête DNS** au(x) serveur(s) DNS fourni(s) par le DHCP (qui peut être l'IP du routeur ou un serveur externe).
   - **Est-ce que la requête va vers le routeur ?** Souvent oui, indirectement :
     - Si votre routeur est configuré comme un proxy/redirecteur DNS (commun dans les routeurs domestiques comme ceux de TP-Link, Netgear ou Apple Airport), votre ordinateur interroge d'abord le routeur (par exemple, via 192.168.1.1 comme serveur DNS).
     - Le routeur vérifie son cache local (pour la rapidité). S'il a la réponse (d'une requête précédente), il répond directement. Sinon, il transmet la requête à un serveur DNS en amont (comme celui de votre FAI ou un serveur public que vous avez configuré).
   - Le serveur DNS en amont résout le nom (par exemple, `www.google.com` → `142.250.190.14`) et renvoie l'adresse IP à travers la chaîne jusqu'à votre ordinateur.
   - Votre ordinateur utilise ensuite cette adresse IP pour se connecter au site.

3. **Comment le routeur gère ces requêtes** :
   - **Requêtes DHCP** : Le routeur maintient un pool d'adresses IP disponibles (par exemple, 192.168.1.50 à 192.168.1.150). Lorsque vous en demandez une, il vous la loue pour une durée déterminée (par exemple, 24 heures), la suit dans sa table et la renouvelle si nécessaire. Il gère également votre nom d'hôte si vous en avez défini un (par exemple, pour un accès local comme `ping monportable.local`).
   - **Requêtes DNS** : Le routeur ne "possède" pas les enregistrements DNS — c'est un intermédiaire. Il :
     - Met en cache les réponses pour éviter les requêtes répétées en amont (améliore la vitesse et réduit la bande passante).
     - Transmet les requêtes non résolues aux serveurs en amont configurés.
     - Peut appliquer des contrôles parentaux, du blocage de publicités (via des DNS personnalisés comme Pi-hole) ou de la journalisation.
     - Si la requête concerne un appareil local (par exemple, un autre ordinateur sur votre réseau), il peut la résoudre via son fichier hosts local ou mDNS (multicast DNS, utilisé par Bonjour sur les appareils macOS/Apple).
   - Des erreurs ? Si le DNS échoue (par exemple, mauvais serveur DNS), vous ne pouvez pas résoudre les noms — les sites ne se chargeront pas, mais un ping direct des adresses IP pourrait fonctionner.

En bref : Le DHCP fournit à votre ordinateur son "adresse et ses instructions" depuis le routeur. Le DNS utilise ensuite ces instructions pour demander "Où se trouve ce site web ?" — en passant souvent par le routeur vers des résolveurs externes.

Si vous dépanez une configuration spécifique, partagez plus de détails comme votre modèle de routeur ou l'erreur exacte !