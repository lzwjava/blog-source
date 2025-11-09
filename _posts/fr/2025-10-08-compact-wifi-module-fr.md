---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Module Wi-Fi compact pour l'IdO
translated: true
type: note
---

L'ESP-01S est un module WiFi compact basé sur la puce microcontrôleur ESP8266 d'Espressif Systems. C'est une version améliorée de l'ESP-01 originale, conçue principalement pour les applications IoT (Internet des Objets) où vous devez ajouter une connectivité sans fil à d'autres microcontrôleurs comme Arduino ou Raspberry Pi.

### Caractéristiques principales :
- **Capacités WiFi** : Prend en charge les standards 802.11 b/g/n, pouvant agir comme un point d'accès WiFi autonome, une station, ou les deux à la fois. Il inclut une pile de protocoles TCP/IP intégrée pour une intégration réseau facile.
- **Processeur et Mémoire** : Fonctionne avec un CPU Tensilica L106 32-bit RISC à 80 MHz (overclockable à 160 MHz). Dispose de 1 Mo (ou parfois 4 Mo selon les variantes) de mémoire flash SPI pour le stockage du code et des données.
- **Broches d'E/S** : Configuration à 8 broches (VCC, GND, CH_PD, RST, TX, RX, GPIO0, GPIO2) pour la communication série (UART) et le contrôle GPIO de base, comme la commande de LED ou de relais.
- **Alimentation et Taille** : Fonctionne sous 3,3 V (non tolérant au 5 V), consomme peu d'énergie (environ 80 mA pendant la transmission) et mesure environ 24,75 x 14,5 mm—ce qui le rend idéal pour les petits projets.
- **Améliorations par rapport à l'ESP-01** : Meilleure conception de PCB pour une force du signal WiFi améliorée, plus de mémoire flash (1 Mo contre 512 Ko), et une LED d'état bleue sur GPIO2 au lieu de TX.

### Utilisations courantes :
- Connecter des capteurs ou des appareils à internet pour une surveillance/commande à distance.
- Programmation via l'IDE Arduino (avec le support de carte ESP8266) ou par commandes AT via série.
- Prototypage de gadgets pour la maison connectée, comme des interrupteurs compatibles WiFi ou des stations météo.

Pour commencer, vous aurez besoin d'un adaptateur USB-série (comme FTDI) pour flasher le firmware, car il ne dispose pas de port USB intégré. Il est peu coûteux (moins de 5 $) et largement disponible, mais manipulez-le avec précaution pour éviter d'endommager les broches.

[Comment utiliser un module ESP-01S](https://www.taydaelectronics.com/datasheets/files/ESP-01S.pdf)
[Débuter avec l'ESP8266 ESP-01](https://www.instructables.com/Getting-Started-With-the-ESP8266-ESP-01/)
[Introduction à l'ESP-01S](https://lonelybinary.com/en-us/blogs/learn/what-is-esp-01s)
[Module ESP-01S / ESP01S ESP8266](https://hobbycomponents.com/esp8266/1176-esp-01s-esp01s-esp8266-module)