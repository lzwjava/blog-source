---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Limitations de vitesse de la topologie en bus expliquées
translated: true
type: note
---

### Limitations de la topologie en bus

Vous avez parfaitement raison sur les caractéristiques clés : la topologie en bus utilise un câble partagé unique (comme le coaxial dans les configurations Ethernet classiques) qui est simple et économique, mais vulnérable aux collisions. Lorsque plusieurs appareils tentent de transmettre en même temps, les signaux se chevauchent, provoquant des "collisions" qui nécessitent une retransmission via des protocoles comme CSMA/CD (Carrier Sense Multiple Access with Collision Detection).

#### Pourquoi ~100 Mbps semble être une limite pratique (même si le câble peut faire plus)
Les câbles eux-mêmes—qu'ils soient en cuivre (par exemple, paire torsadée ou coaxial) ou optiques/fibre—ne sont pas le goulot d'étranglement ici. La fibre optique peut facilement gérer des gigabits par seconde (ou des térabits dans les configurations modernes) sur de longues distances avec une perte minimale. Les véritables limites proviennent de la **nature du support partagé du bus** et de la physique/surcharge protocolaire. Voici ce qui plafonne les vitesses autour de 10–100 Mbps dans les conceptions de bus traditionnelles :

1. **Délai de propagation et détection de collision** :
   - Les signaux mettent du temps à parcourir le câble (par exemple, ~5 ns/mètre dans le coaxial ou ~5 ns/km dans la fibre).
   - Dans un bus, chaque appareil doit "écouter" les collisions sur *toute la longueur du réseau*. Le protocole définit un "temps de slot" (temps minimum pour détecter une collision), qui doit être plus long que le délai de propagation aller-retour (RTT) pour le pire scénario (signal d'une extrémité à l'autre et retour).
   - Pour l'Ethernet 10 Mbps (bus classique), la longueur maximale de segment était d'environ 500m pour maintenir le RTT en dessous de 51,2 μs (temps de slot de 512 bits).
   - À 100 Mbps, le temps de slot diminue proportionnellement (à ~5,12 μs), forçant les longueurs maximales à descendre à ~100m. Au-delà, les collisions ne sont pas détectées, entraînant des erreurs sans fin.
   - Passer à 1 Gbps ? Le temps de slot tombe à ~0,512 μs, limitant les segments à ~10–20m—impraticable pour un "bus" connectant plusieurs appareils.

2. **Surcharge des collisions et efficacité** :
   - CSMA/CD ajoute des nouvelles tentatives : une collision gaspille de la bande passante (jusqu'à 50 % de perte d'efficacité sous charge lourde).
   - Des vitesses plus élevées amplifient ceci—des collisions plus fréquentes signifient plus de cycles gaspillés, réduisant le débit effectif.
   - Le support partagé signifie que la bande passante totale est divisée entre tous les appareils ; aucune dédicace par port.

3. **Intégrité du signal et bruit** :
   - Bien que la fibre résiste mieux aux interférences électromagnétiques (EMI) que le cuivre, les configurations en bus nécessitent toujours un timing précis pour la détection de porteuse.
   - À des vitesses élevées, les réflexions, l'atténuation ou la diaphonie sur une ligne partagée dégradent les signaux plus rapidement, nécessitant plus de répéteurs (qui ajoutent du délai et du coût).

#### Pourquoi abandonner le bus pour des vitesses plus élevées ?
C'est pourquoi Ethernet a évolué : après 100 Mbps (Fast Ethernet), ils ont abandonné le bus pur pour une **topologie en étoile avec des switches** (par exemple, 1 Gbps+). Les switches créent des liaisons point à point full-duplex—pas de collisions, bande passante totale par appareil, et des portées plus longues. Le bus est maintenant rare en dehors des utilisations de niche/industrielles.

Si vous pensez à une configuration spécifique (par exemple, le bus CAN dans les voitures ou le vieux 10BASE-T), les principes sont similaires : protocole + physique > capacité du câble.

Pour des analyses plus approfondies :  
[Ethernet Bus Topology Basics](https://en.wikipedia.org/wiki/Bus_network)  
[CSMA/CD Limitations](https://www.cisco.com/c/en/us/support/docs/lan-switching/ethernet/10561-3.html)