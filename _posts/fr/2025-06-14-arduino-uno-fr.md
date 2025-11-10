---
audio: false
generated: true
lang: fr
layout: post
title: Variantes de l'Arduino Uno
translated: true
type: note
---

L'Arduino Uno, Uno R3 et Uno Mini sont des variantes de la célèbre carte microcontrôleur Arduino, chacune présentant des différences spécifiques en matière de conception, de fonctionnalités et de cas d'utilisation. Voici une comparaison concise basée sur leurs principales différences :

### 1. **Arduino Uno (Original) vs Arduino Uno R3**
L'Arduino Uno et l'Uno R3 sont essentiellement la même carte, l'Uno R3 étant la troisième révision (R3) de l'Uno original. Les différences sont mineures et portent sur des améliorations de la facilité d'utilisation et de la compatibilité.

- **Microcontrôleur** : Les deux utilisent le **ATmega328P** (AVR 8 bits, vitesse d'horloge 16 MHz).
- **Brochage** :
  - L'Uno R3 ajoute des **broches SDA et SCL** près de la broche AREF pour la compatibilité I2C, améliorant le support des shields.
  - Le R3 inclut une **broche IOREF** pour permettre aux shields de s'adapter à la tension de la carte (5V dans ce cas).
- **Puce USB-Série** :
  - L'Uno original utilise une puce **FTDI FT232R** pour la communication USB-série.
  - L'Uno R3 passe à un microcontrôleur **ATmega16U2**, plus flexible et supportant une communication plus rapide.
- **Autres changements** :
  - Le R3 a un **circuit de reset** plus robuste et une LED tamponnée sur la broche 13 (via un ampli-op) pour éviter les interférences.
  - Le R3 ajoute deux broches supplémentaires au connecteur 6 broches près de la broche reset (l'une est IOREF, l'autre est réservée).
- **Facteur de forme** : Dimensions identiques (~6,9 cm x 5,3 cm).
- **Disponibilité** : L'Uno R3 est le standard actuel ; les anciennes révisions Uno (R1, R2) sont pour la plupart obsolètes.
- **Cas d'utilisation** : Les deux sont conviviaux pour les débutants et idéaux pour le prototypage avec des shields. Le R3 est meilleur pour les shields modernes en raison du brochage mis à jour.

**Différence clé** : L'Uno R3 est une version améliorée de l'Uno original avec une meilleure compatibilité des shields et une interface USB plus robuste. Pour la plupart des utilisateurs, le R3 est le meilleur choix car c'est le standard actuel.

### 2. **Arduino Uno R3 vs Arduino Uno Mini Limited Edition**
L'Arduino Uno Mini Limited Edition est une version compacte et édition spéciale de l'Uno R3, conçue pour les collectionneurs et les projets nécessitant un encombrement réduit.

- **Microcontrôleur** : Les deux utilisent le **ATmega328P** (AVR 8 bits, 16 MHz).
- **Facteur de forme** :
  - Uno R3 : Taille standard (~6,9 cm x 5,3 cm).
  - Uno Mini : Beaucoup plus petit (~3,3 cm x 2,5 cm), compatible breadboard, avec une **PCB plaqué or** pour un attrait esthétique.
- **Connecteurs** :
  - Uno R3 : Versions traversantes ou SMD ; borniers femelles standard pour les shields.
  - Uno Mini : Borniers mâles pré-soudés, pas de compatibilité avec les shields en raison de la taille et de la disposition.
- **Port USB** :
  - Uno R3 : Connecteur USB-B.
  - Uno Mini : **Connecteur USB-C**, plus moderne et compact.
- **Broches d'E/S** :
  - Les deux ont **14 E/S numériques** (6 PWM) et **6 entrées analogiques**, mais les broches de l'Uno Mini sont agencées différemment en raison de sa taille réduite.
- **Alimentation** :
  - Les deux fonctionnent sous **5V**, mais l'Uno Mini n'a pas de prise jack barrel (alimenté via USB-C ou la broche VIN).
- **Mémoire** : Identique (**32 Ko Flash, 2 Ko SRAM, 1 Ko EEPROM**).
- **Fonctionnalités spéciales** :
  - L'Uno Mini est une **édition limitée** avec des graphismes uniques et un emballage de collection, destiné aux passionnés.
- **Prix** : L'Uno Mini est généralement plus cher en raison de son statut d'édition limitée (~45 $ contre ~27 $ pour l'Uno R3).
- **Cas d'utilisation** :
  - Uno R3 : Prototypage à usage général, compatible shield, convivial pour les débutants.
  - Uno Mini : Projets avec contraintes d'espace, collectionneurs ou développeurs souhaitant une carte premium et compacte.

**Différence clé** : L'Uno Mini est une version plus petite et premium de l'Uno R3 avec un port USB-C et sans support de shield, idéal pour les projets compacts ou de collection.

### 3. **Tableau récapitulatif**

| Caractéristique       | Arduino Uno (Original) | Arduino Uno R3         | Arduino Uno Mini       |
|-----------------------|------------------------|------------------------|------------------------|
| **Microcontrôleur**   | ATmega328P            | ATmega328P            | ATmega328P            |
| **Vitesse d'horloge** | 16 MHz                | 16 MHz                | 16 MHz                |
| **Facteur de forme**  | ~6,9 cm x 5,3 cm      | ~6,9 cm x 5,3 cm      | ~3,3 cm x 2,5 cm      |
| **Connecteur USB**    | USB-B (FTDI)          | USB-B (ATmega16U2)    | USB-C                 |
| **Broches d'E/S**     | 14 numériques, 6 analogiques | 14 numériques, 6 analogiques | 14 numériques, 6 analogiques |
| **Compatibilité shields** | Limitée (ancienne) | Oui                    | Non                   |
| **Entrée d'alimentation** | USB, jack barrel, VIN | USB, jack barrel, VIN | USB-C, VIN            |
| **Fonctionnalités spéciales** | -                | Broches SDA/SCL, IOREF | Édition limitée, PCB or |
| **Prix (Approx.)**    | Obsolète              | ~27 $                 | ~45 $                 |
| **Idéal pour**        | Projets legacy        | Prototypage général   | Projets compacts/collection |

### Lequel choisir ?
- **Arduino Uno R3** : Le choix par défaut pour la plupart des utilisateurs. Il est largement supporté, compatible avec les shields et idéal pour les débutants ou les projets à usage général. Choisissez-le sauf si vous avez des contraintes de taille spécifiques ou si vous voulez un objet de collection.
- **Arduino Uno (Original)** : N'est pertinent que si vous travaillez avec d'anciens shields pré-R3 ou si vous avez déjà une carte. Sinon, optez pour le R3.
- **Arduino Uno Mini Limited Edition** : Choisissez-le pour les projets avec contraintes d'espace, si vous préférez l'USB-C, ou si vous êtes un passionné/collectionneur Arduino. Il est moins polyvalent en raison de l'absence de support pour les shields.

Si vous débutez, l'**Uno R3** est la meilleure option polyvalente en raison de sa compatibilité, de son support communautaire et de son prix abordable. Pour des besoins de projet spécifiques (par exemple, la taille ou l'esthétique), l'Uno Mini est une excellente alternative.

Faites-moi savoir si vous avez besoin d'aide pour un projet spécifique ou une comparaison de fonctionnalités !