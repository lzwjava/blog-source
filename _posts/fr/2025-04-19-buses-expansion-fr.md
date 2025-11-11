---
audio: false
generated: true
lang: fr
layout: post
title: 'Partie 5 : Bus et extension'
translated: true
type: note
---

### 1. Normes de bus système

#### Qu'est-ce qu'un bus système ?

Un bus système est une voie de communication qui relie le CPU à la mémoire et aux périphériques. Il facilite le transfert de données, la signalisation d'adresse et les signaux de contrôle entre ces composants, permettant au CPU d'interagir efficacement avec les autres parties du système informatique[^3].

---

### 2. Aperçu du bus ISA

- **ISA (Industry Standard Architecture)** est l'une des premières normes de bus système, introduite avec l'IBM PC AT dans les années 1980.
- C'est un bus 16 bits fonctionnant à 4,77 MHz, capable de débits de transfert de données allant jusqu'à environ 9 Mo/s[^5].
- ISA prend en charge plusieurs cartes d'extension, chacune avec sa propre ligne de demande d'interruption, permettant de connecter des périphériques tels que des cartes réseau, des ports série et des cartes vidéo.
- Le bus est rétrocompatible avec les anciens systèmes PC XT 8 bits et utilise un connecteur à 98 broches combinant deux connecteurs edge en un seul slot.
- ISA utilise une signalisation asynchrone et le bus mastering, mais n'accède directement qu'aux premiers 16 Mo de la mémoire principale[^5].
- En raison de son ancienneté, ISA est largement obsolète mais est historiquement important en tant que fondement des conceptions de bus ultérieures.

---

### 3. Aperçu du bus PCI

- **PCI (Peripheral Component Interconnect)** est une norme de bus parallèle synchrone plus moderne, conçue pour surmonter les limitations de l'ISA[^1][^3].
- Les bus PCI fonctionnent à 33 MHz avec un bus adresse/données multiplexé 32 bits, offrant une bande passante de base de 44 à 66 Mo/s.
- Pour les accès mémoire séquentiels, le PCI peut atteindre jusqu'à 132 Mo/s en transférant un mot 32 bits par cycle d'horloge sans avoir à renvoyer les adresses[^1].
- Le PCI utilise une interface de type pont (bridge) pour se connecter au bus du CPU, ce qui met les données en mémoire tampon et optimise l'accès à la mémoire, permettant au CPU de continuer son exécution sans états d'attente pendant la communication avec les périphériques[^1].
- Le PCI prend en charge le bus mastering et le DMA (Direct Memory Access), où les périphériques peuvent prendre le contrôle du bus pour transférer des données directement.
- Il existe une extension 64 bits du PCI pour augmenter davantage la bande passante.
- Les périphériques PCI sont identifiés par un numéro de bus, un numéro de périphérique et une fonction, avec des registres de configuration spécifiant le vendeur, le type de périphérique, les adresses mémoire et d'E/S, et les interruptions[^3].
- Les transactions PCI incluent des phases d'adresse et des phases de données, prenant en charge diverses commandes comme la lecture/écriture mémoire et la lecture/écriture d'E/S[^3].

---

### 4. Technologies d'interface modernes

La communication avec les périphériques modernes s'est orientée vers des interfaces série plus simples et plus flexibles que les bus parallèles.

---

#### USB (Universal Serial Bus)

- L'USB est une interface série haute vitesse très utilisée, conçue pour connecter des périphériques tels que claviers, souris, dispositifs de stockage, etc.
- Il prend en charge le plug-and-play et le hot-swapping, permettant de connecter et de déconnecter des périphériques sans éteindre le système.
- L'USB utilise une topologie en étoile hiérarchisée et prend en charge des débits de données allant de 1,5 Mbit/s (Low Speed) jusqu'à 10 Gbit/s (USB 3.1 et au-delà).
- Il fournit de l'énergie aux périphériques et prend en charge de multiples classes de périphériques avec des protocoles standardisés.
- Les contrôleurs USB gèrent les transferts de données en utilisant des endpoints et des pipes, avec différents types de transfert tels que contrôle, bulk, interrupt et isochrone.

---

#### SPI (Serial Peripheral Interface)

- Le SPI est un bus de communication série synchrone couramment utilisé pour la communication sur de courtes distances avec des périphériques tels que capteurs, EEPROM et écrans[^4].
- Il utilise quatre signaux : SCLK (horloge), MOSI (Master Out Slave In), MISO (Master In Slave Out) et CS (Chip Select).
- Le SPI est full-duplex, permettant une transmission et une réception simultanées des données.
- Il est simple et rapide mais nécessite une ligne de sélection (chip select) par périphérique, ce qui peut limiter l'évolutivité.
- Les paramètres de mode SPI incluent la polarité et la phase de l'horloge, qui définissent quand les données sont échantillonnées et décalées[^6].
- Le SPI est généralement utilisé dans les systèmes embarqués et les applications à microcontrôleurs.

---

#### I²C (Inter-Integrated Circuit)

- L'I²C est un bus série à deux fils utilisé pour la communication entre des microcontrôleurs et des périphériques tels que capteurs et EEPROM[^4].
- Il utilise deux lignes bidirectionnelles : SDA (données) et SCL (horloge).
- L'I²C prend en charge plusieurs maîtres et esclaves sur le même bus, les périphériques étant adressés par des adresses uniques de 7 ou 10 bits.
- Il prend en charge la communication half-duplex et utilise des sorties open-drain / open-collector avec des résistances de pull-up.
- L'I²C est plus lent que le SPI mais nécessite moins de broches et prend en charge la communication multi-périphérique avec un câblage simple.
- Les débits typiques sont de 100 kHz (mode Standard), 400 kHz (mode Fast) et plus dans les spécifications plus récentes.

---

### Tableau récapitulatif : ISA vs PCI vs USB vs SPI vs I²C

| Caractéristique | ISA | PCI | USB | SPI | I²C |
| :-- | :-- | :-- | :-- | :-- | :-- |
| Type de bus | Parallèle, asynchrone | Parallèle, synchrone | Série, asynchrone | Série, synchrone | Série, synchrone |
| Largeur de données | 8 ou 16 bits | 32 ou 64 bits multiplexés | Série (1 bit) | 1 bit par ligne, full duplex | 1 bit par ligne, half duplex |
| Fréquence d'horloge | 4,77 MHz | 33 MHz (PCI de base) | Jusqu'à 10 Gbit/s (USB 3.1) | Typiquement jusqu'à plusieurs MHz | Typiquement jusqu'à 400 kHz et plus |
| Bande passante max | ~9 Mo/s | 44-132 Mo/s | Varie selon la version USB | Dépend de la fréquence d'horloge | Inférieure au SPI |
| Nombre de fils | Beaucoup (adresse, données, ctrl) | Beaucoup (lignes multiplexées) | 4 (alimentation, masse, D+, D-) | 4 (SCLK, MOSI, MISO, CS) | 2 (SDA, SCL) |
| Adressage des périphériques | Basé sur le slot | Numéro de bus/périphérique/fonction | Énumération des périphériques | Sélection (chip select) par périphérique | Périphériques adressés |
| Cas d'utilisation typiques | Cartes d'extension héritées | Cartes d'extension modernes | Périphériques externes | Périphériques embarqués | Périphériques embarqués |
| Bus Mastering | Oui | Oui | Géré par le contrôleur hôte | Maître/esclave | Multi-maître pris en charge |

---

### Notes pratiques sur l'utilisation du SPI et de l'I²C

- Sur des plateformes comme le Raspberry Pi, les interfaces SPI et I²C ne sont pas activées par défaut et nécessitent une configuration via les paramètres système (par exemple, `raspi-config`)[^4].
- Des bibliothèques telles que `wiringPi`, `spidev` (pour SPI) et `smbus` (pour I²C) fournissent des interfaces de programmation en C/C++ et Python pour communiquer avec les périphériques sur ces bus.
- La configuration du SPI implique de définir le mode (polarité et phase de l'horloge), l'ordre des bits (MSB ou LSB en premier) et de sélectionner la broche de sélection (chip select) correcte[^6].
- La communication I²C implique de spécifier les adresses des périphériques et de gérer les conditions de start/stop pour le transfert de données.

---

Ce tutoriel décrit les concepts fondamentaux et les aspects pratiques des bus système et des interfaces périphériques modernes, fournissant une base solide pour comprendre les architectures de bus des micro-ordinateurs et les technologies d'extension.

<div style="text-align: center">⁂</div>

[^1]: https://people.ece.ubc.ca/~edc/464/lectures/lec17.pdf

[^2]: https://spotpear.com/wiki/USB-TO-UART-I2C-SPI-JTAG-Wiki.html

[^3]: https://home.mit.bme.hu/~rtamas/rendszerarchitekturak/eloadas/08_bus_introduction.pdf

[^4]: https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all

[^5]: https://www.techtarget.com/searchwindowsserver/definition/ISA-Industry-Standard-Architecture

[^6]: https://www.ratocsystems.com/english/download/pdffiles/usb61_e_10.pdf

[^7]: https://webstor.srmist.edu.in/web_assets/srm_mainsite/files/files/PCI.pdf

[^8]: https://www.infineon.com/dgdl/Infineon-USB-Serial_VCP_I2CSPI_API_Guide-Software-v01_00-EN.pdf?fileId=8ac78c8c7d0d8da4017d0f6a8b015fe6\&da=t

[^9]: https://network.nvidia.com/pdf/whitepapers/PCI_3GIO_IB_WP_120.pdf

[^10]: https://people.scs.carleton.ca/~sivarama/org_book/org_book_web/slides/chap_1_versions/ch5_1.pdf

[^11]: https://www.youtube.com/watch?v=BBobCtfOjbM

[^12]: https://www.sciencedirect.com/topics/engineering/peripheral-component-interconnect-bus

[^13]: http://mcatutorials.com/mca-tutorials-bus-standards-and-types.php

[^14]: https://www.youtube.com/watch?v=YRJ9gWaxfJY

[^15]: https://docs.nxp.com/bundle/UM12018/page/topics/connecting_to_a_target_through_a_usb-to-spi_or_usb.html

[^16]: https://www.i2ctools.com/Downloads/USBtoI2Cpro/USB-to-SPI_Software_Users_Manual.pdf

[^17]: https://www.youtube.com/watch?v=WIIR77fCHYc

[^18]: https://ftdichip.com/wp-content/uploads/2021/08/AN_255_USB-to-I2C-Example-using-the-FT232H-and-FT201X-devices.pdf

[^19]: https://www.youtube.com/watch?v=IyGwvGzrqp8