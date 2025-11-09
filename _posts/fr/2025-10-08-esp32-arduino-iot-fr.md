---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: ESP32 pour les projets IoT Arduino
translated: true
type: note
---

L'ESP32 est un microcontrôleur économique et à faible consommation développé par Espressif Systems, intégrant une connectivité Wi-Fi et Bluetooth double mode. Il s'agit essentiellement d'un système sur une puce (SoC) largement utilisé pour les projets IoT (Internet des Objets), les capteurs et les applications sans fil en raison de sa polyvalence et de ses performances.

Dans le contexte d'Arduino, l'ESP32 n'est pas "à l'intérieur" d'Arduino mais est entièrement compatible avec l'écosystème Arduino. Vous pouvez programmer les cartes ESP32 (comme la populaire NodeMCU ou l'officielle Arduino Nano ESP32) en utilisant le logiciel gratuit Arduino IDE. Cela implique d'installer le package de carte ESP32 via le Gestionnaire de cartes de l'IDE, puis d'écrire des sketches en C/C++ (comme avec les cartes Arduino traditionnelles telles que l'Uno). L'ESP32 offre des avantages par rapport aux Arduinos de base, tels qu'un traitement plus rapide (double cœur jusqu'à 240 MHz), plus de broches GPIO et des fonctionnalités sans fil, ce qui le rend idéal pour les projets connectés sans avoir besoin de shields supplémentaires.

Si vous débutez, commencez par télécharger l'IDE Arduino et recherchez "ESP32 board package" dans le menu Outils > Type de carte > Gestionnaire de cartes.

### Références
- [ESP32 - Wikipedia](https://en.wikipedia.org/wiki/ESP32)
- [Arduino Nano ESP32 Documentation](https://docs.arduino.cc/nano-esp32)
- [Arduino Nano ESP32 Product Page](https://store-usa.arduino.cc/products/nano-esp32)