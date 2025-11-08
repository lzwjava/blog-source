---
audio: false
generated: true
image: false
lang: fr
layout: post
model: moonshotai/kimi-k2-thinking
title: Fiabilité du TCP et détection des pertes
translated: true
type: note
---

Permettez-moi de décomposer cette conversation sur la fiabilité de TCP en concepts clairs :

## **1. Détection des paquets perdus**

TCP utilise deux mécanismes principaux pour repérer les données manquantes :

- **Timeout** : Un simple compte à rebours démarre lorsqu'un paquet est envoyé. Si aucun accusé de réception (ACK) n'arrive avant l'expiration du timer, le paquet est déclaré perdu et retransmis. C'est la méthode de détection de "dernier recours".

- **ACKs dupliqués (Retransmission Rapide)** : Ce mécanisme est plus sophistiqué. Lorsque le récepteur reçoit des paquets *dans le désordre*, il continue d'envoyer des ACKs pour le *dernier* paquet reçu *dans l'ordre*. Par exemple :
  - S'il a reçu les paquets #1, #2, mais que #3 est manquant, il continue d'envoyer des ACKs pour #2 même s'il reçoit ensuite #4, #5, etc.
  - **Trois ACKs dupliqués** pour le même numéro de séquence (#2 dans notre exemple) signalent que le paquet #3 est probablement perdu (et pas seulement retardé), déclenchant une retransmission *immédiate*—beaucoup plus rapide que d'attendre un timeout.

## **2. Impact des performances avec un RTT élevé**

Vous avez absolument raison—un temps d'aller-retour (Round-Trip Time) élevé rend les retransmissions problématiques :
- Si RTT = 200ms (par exemple, une liaison intercontinentale), et qu'un paquet est perdu, vous attendez *au moins* 200ms pour le découvrir via un timeout
- Pendant cette période d'attente, la bande passante reste inactive, le débit chute brutalement et la connexion semble "lente"
- La retransmission rapide aide considérablement ici, réduisant le temps de détection de plusieurs secondes à quelques millisecondes

## **3. Intervalles de timeout adaptatifs**

TCP n'utilise pas une valeur de timeout fixe—il suit intelligemment les conditions du réseau :

- **Estimation du RTT** : TCP mesure continuellement le temps que prennent les accusés de réception à revenir
- **Timeout dynamique** : Le délai de retransmission (Retransmission Timeout - RTO) est calculé sur la base du RTT mesuré plus une marge de sécurité (typiquement RTT + 4×déviation)
- **Auto-ajustement** : Lorsque le RTT augmente (congestion du réseau, chemins plus longs), le timeout s'allonge automatiquement pour éviter les retransmissions *prématurées*
- **Éviter les retransmissions inutiles** : Sans cela, TCP pourrait retransmettre des paquets parfaitement valides qui étaient simplement retardés, gaspillant de la bande passante et causant des livraisons dupliquées

**Conclusion** : La fiabilité de TCP ne se résume pas à la retransmission—il s'agit de détecter *intelligemment* les pertes sans attendre trop longtemps ni agir trop hâtivement.