---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Plage de sous-réseau d'adresse IP expliquée
translated: true
type: note
---

Oui, c'est correct. L'adresse IP `192.168.1.35/24` appartient au sous-réseau `192.168.1.0/24`, qui couvre la plage complète de 256 adresses : de `192.168.1.0` (adresse réseau) à `192.168.1.255` (adresse de broadcast).

### Récapitulatif rapide :
- **/24** signifie un masque de sous-réseau de `255.255.255.0`, fixant les trois premiers octets (`192.168.1`) et permettant au dernier octet de varier de 0 à 255.
- Adresses hôtes utilisables : `192.168.1.1` à `192.168.1.254` (en excluant l'adresse réseau et l'adresse de broadcast).
- Votre hôte spécifique (`192.168.1.35`) est simplement une adresse dans cette plage.

Si vous avez besoin de calculer des sous-réseaux pour un préfixe différent ou de vérifier avec un outil, faites-le-moi savoir !