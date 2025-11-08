---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Comprendre les masques de sous-réseau
translated: true
type: note
---

### Qu'est-ce qu'un masque de sous-réseau ?

Un **masque de sous-réseau** (ou netmask) est un nombre 32 bits (écrit en notation décimale pointée, comme 255.255.255.0) qui divise une adresse IPv4 en deux parties :
- **Partie réseau** : Identifie le réseau global (ou sous-réseau) auquel un appareil appartient.
- **Partie hôte** : Identifie l'appareil spécifique (hôte) au sein de ce réseau.

Il fonctionne comme un filtre : lorsqu'un appareil envoie des données, le masque de sous-réseau est appliqué (via une opération ET bit à bit) à l'adresse IP pour déterminer si la destination se trouve sur le *sous-réseau local* (communication directe, aucun routeur nécessaire) ou sur un *réseau distant* (les données passent par la passerelle/le routeur par défaut).

#### Décortiquer 255.255.255.0
Votre explication est **exactement correcte**—confirmons et développons-la étape par étape.

1.  **En binaire (là où la magie opère vraiment)** :
    - Chaque octet (par exemple, 255) représente 8 bits, donc le masque complet fait 32 bits.
    - 255 = `11111111` (tous les bits sont "allumés").
    - 0 = `00000000` (tous les bits sont "éteints").
    - Ainsi, 255.255.255.0 en binaire est :  
      `11111111.11111111.11111111.00000000`
    - Cela signifie :
        - **Premiers 24 bits (les trois 255)** : Fixés comme le **préfixe réseau**. Ils ne peuvent pas changer pour les appareils du même sous-réseau—ils définissent *quel sous-réseau* vous utilisez.
        - **Derniers 8 bits (le 0)** : Variables comme la **partie hôte**. Ils *peuvent* changer pour identifier les appareils individuels.

2.  **Combien d'adresses dans ce sous-réseau ?**
    - La partie hôte a 8 bits, donc il y a \\(2^8 = 256\\) combinaisons possibles (de `00000000` à `11111111`, ou 0 à 255 en décimal).
    - Exemple avec une IP de base comme 192.168.1.0 :
        - Adresse réseau : 192.168.1.0 (tous les bits hôte = 0 ; c'est l'identifiant du sous-réseau lui-même).
        - Hôtes utilisables : 192.168.1.1 à 192.168.1.254 (254 adresses, puisque .0 est réservé pour le réseau et .255 pour la diffusion).
        - Diffusion (broadcast) : 192.168.1.255 (envoie à tout le monde dans le sous-réseau).
    - Votre routeur (par exemple, à 192.168.1.1) attribue les IPs de ce pool via le DHCP, comme le 192.168.1.100 que vous avez mentionné.

3.  **Communication au sein du sous-réseau** :
    - Oui ! Les appareils avec des IPs dans le même sous-réseau (par exemple, votre ordinateur portable à 192.168.1.100 et un téléphone à 192.168.1.50) peuvent communiquer *directement* via Ethernet/Wi-Fi—aucun saut par le routeur n'est nécessaire. Le masque de sous-réseau leur dit : "Hé, nous sommes voisins—envoyez les paquets directement à l'adresse MAC."
    - Si la destination est extérieure (par exemple, 192.168.2.50), les données sont envoyées à la passerelle par défaut (votre routeur à 192.168.1.1) pour être routées ailleurs.

#### Aperçu rapide : Exemple d'adresse IP + Masque de sous-réseau

| Adresse IP      | Masque de sous-réseau | Partie réseau | Partie hôte | Identifiant réseau complet |
|-----------------|-----------------------|---------------|-------------|----------------------------|
| 192.168.1.100 | 255.255.255.0       | 192.168.1    | .100       | 192.168.1.0              |

- Pour calculer : IP ET Masque = Identifiant réseau (par exemple, 192.168.1.100 ET 255.255.255.0 = 192.168.1.0).

Il s'agit d'une configuration domestique courante (sous-réseau /24, ou notation CIDR 192.168.1.0/24). Des masques plus grands (par exemple, 255.255.255.252) signifient des sous-réseaux plus petits avec moins d'hôtes mais une segmentation plus précise.

Si vous avez une configuration IP spécifique ou souhaitez calculer quelque chose (par exemple, via du code), partagez plus de détails !