---
audio: false
generated: true
lang: fr
layout: post
title: 'Introduction au Raspberry Pi Pico : Un Microcontrôleur Polyvalent'
translated: true
type: note
---

Le **Raspberry Pi Pico** est une carte microcontrôleur polyvalente et à faible coût développée par la Raspberry Pi Foundation, conçue pour les systèmes embarqués, le prototypage et les projets d'électronique DIY. Contrairement aux ordinateurs monocarte (SBC) Raspberry Pi comme le Raspberry Pi 4, le Pico est un microcontrôleur, ce qui signifie qu'il est optimisé pour contrôler du matériel, exécuter des programmes légers et interfacer des capteurs, des moteurs et d'autres composants. Lancé en janvier 2021, il a marqué l'entrée de la Fondation sur le marché des microcontrôleurs, offrant une plateforme abordable mais puissante pour les amateurs, les éducateurs et les professionnels.

Voici une introduction complète au Raspberry Pi Pico, couvrant ses caractéristiques, ses spécifications, ses capacités de programmation, ses applications et plus encore.

---

### **Aperçu**
Le Raspberry Pi Pico est construit autour du **RP2040**, une puce microcontrôleur conçue sur mesure par la Raspberry Pi Foundation. Prix d'environ 4 $ USD, il rivalise avec des plateformes comme Arduino et ESP32 mais se distingue par ses hautes performances, son faible coût et son vaste support communautaire. Le Pico est compact, mesurant seulement 51 mm x 21 mm, et est conçu à la fois pour les débutants et les utilisateurs avancés travaillant sur des projets allant du simple clignotement de LED à des applications complexes d'IoT et de robotique.

---

### **Caractéristiques Principales**
1. **Microcontrôleur RP2040** :
   - Processeur dual-core **Arm Cortex-M0+** fonctionnant jusqu'à **133 MHz** (overclockable).
   - **264 Ko de SRAM** et **2 Mo de mémoire flash QSPI intégrée** pour le stockage des programmes.
   - Faible consommation d'énergie avec des modes veille et dormant pour les applications sur batterie.
   - Configuration d'horloge flexible pour l'optimisation des performances.

2. **Broches GPIO** :
   - 26 broches **General Purpose Input/Output (GPIO)** multifonctions.
   - Prend en charge les interfaces **I2C**, **SPI**, **UART** et **PWM** pour connecter des périphériques.
   - 2x UART, 2x contrôleurs SPI, 2x contrôleurs I2C et 16x canaux PWM.
   - 3x Convertisseurs Analogique-Numérique (ADC) 12 bits pour les entrées de capteurs analogiques.
   - 8x blocs d'E/S programmables (PIO) pour les protocoles personnalisés (par exemple, contrôle de LED WS2812, sortie VGA).

3. **Alimentation et Connectivité** :
   - Alimenté via **USB micro-B** (5V) ou alimentation externe (1,8–5,5V).
   - **Niveau logique 3,3V** pour les broches GPIO.
   - **Capteur de température** intégré sur le RP2040.
   - Contrôleur USB 1.1 pour les modes périphérique et hôte (utilisé pour la programmation et le débogage).

4. **Conception Physique** :
   - Taille compacte : 51 mm x 21 mm.
   - Format à 40 broches style DIP avec **bords crénelés**, permettant de le souder directement sur un PCB ou de l'utiliser avec une plaque d'essai.
   - Placement des composants sur un seul côté pour une soudure facile.

5. **Faible Coût** :
   - Prix d'environ 4 $, ce qui en fait l'un des microcontrôleurs les plus abordables disponibles.

---

### **Variantes**
Depuis son lancement, la Raspberry Pi Foundation et ses partenaires ont publié des variantes du Pico :
- **Raspberry Pi Pico W** (2022) : Ajoute le **Wi-Fi** (2,4 GHz 802.11n) et le **Bluetooth 5.2** via une puce Infineon CYW43439, permettant des applications IoT sans fil. Prix d'environ 6 $.
- **Raspberry Pi Pico H** : Inclut un connecteur à 40 broches pré-soudé pour un prototypage plus facile.
- **Raspberry Pi Pico WH** : Combine les capacités sans fil du Pico W avec des connecteurs pré-soudés.
- **Pico 2** (2024) : Dispose du microcontrôleur **RP2350**, une version améliorée du RP2040 avec des cœurs dual **Arm Cortex-M33** ou **RISC-V Hazard3** (sélectionnable par l'utilisateur), 520 Ko de SRAM, une efficacité énergétique améliorée et des fonctionnalités de sécurité renforcées (par exemple, Arm TrustZone, accélération SHA-256).

---

### **Programmer le Raspberry Pi Pico**
Le Pico prend en charge plusieurs langages de programmation et environnements, le rendant accessible à un large éventail d'utilisateurs :

1. **MicroPython** :
   - Le choix le plus populaire pour les débutants et le prototypage rapide.
   - Microprogramme MicroPython officiel fourni par la Raspberry Pi Foundation.
   - Prend en charge les bibliothèques pour GPIO, I2C, SPI, PWM, ADC et PIO.
   - REPL interactif (Read-Eval-Print Loop) via USB pour le codage en temps réel.

2. **C/C++** :
   - Offre un contrôle total sur les fonctionnalités du RP2040 en utilisant le **Pico SDK** officiel (Software Development Kit).
   - Convient aux applications critiques en termes de performances et au contrôle matériel de bas niveau.
   - Prend en charge les fonctionnalités avancées comme la programmation PIO et le traitement multi-cœur.
   - Des outils comme CMake et GCC sont utilisés pour la compilation.

3. **Autres Langages** :
   - **CircuitPython** : Un fork de MicroPython par Adafruit, optimisé pour l'éducation et la facilité d'utilisation.
   - **Rust** : Support communautaire pour la programmation Rust sur le RP2040.
   - **Arduino** : Le Pico peut être programmé en utilisant l'IDE Arduino avec le package de carte RP2040 officiel.
   - Support expérimental pour d'autres langages comme JavaScript (via Espruino) et Lua.

4. **Outils de Développement** :
   - **Programmation par glisser-déposer** : Téléversez les fichiers de microprogramme .uf2 MicroPython ou CircuitPython via USB en maintenant le bouton BOOTSEL.
   - **Débogage** : Prend en charge SWD (Serial Wire Debug) pour un débogage avancé avec des outils comme une Raspberry Pi Debug Probe.
   - Les environnements de développement intégrés comme **Thonny** (pour Python) et **Visual Studio Code** (pour C/C++) sont couramment utilisés.

---

### **Applications**
La flexibilité du Raspberry Pi Pico le rend adapté à un large éventail de projets, notamment :
- **Prototypage et Éducation** : Idéal pour apprendre les systèmes embarqués, la programmation et l'électronique.
- **Projets IoT** : Avec le Pico W, les utilisateurs peuvent créer des appareils compatibles Wi-Fi comme des contrôleurs domestiques intelligents ou des stations météo.
- **Robotique** : Contrôler des moteurs, des servos et des capteurs pour des applications robotiques.
- **Interfaces Personnalisées** : Utiliser PIO pour implémenter des protocoles comme le contrôle de LED WS2812 (NeoPixel), la sortie VGA ou DVI.
- **Enregistrement de Données** : Interfacer avec des capteurs (par exemple, température, humidité, lumière) pour la surveillance environnementale.
- **Wearables et Systèmes Embarqués** : La taille compacte et la faible consommation d'énergie conviennent aux technologies portables et aux appareils alimentés par batterie.

---

### **Écosystème et Communauté**
Le Raspberry Pi Pico bénéficie d'un écosystème robuste :
- **Documentation Officielle** : La Raspberry Pi Foundation fournit des guides détaillés, incluant le guide *Pico Getting Started*, la datasheet du RP2040 et les fichiers de conception matérielle.
- **Support Communautaire** : Une grande communauté sur des plateformes comme X, Reddit et les forums Raspberry Pi partage des projets, des tutoriels et des astuces de dépannage.
- **Accessoires Tiers** : De nombreux accessoires sont disponibles, tels que des cartes de relais de capteurs, des afficheurs et des shields provenant de sociétés comme Adafruit, SparkFun et Pimoroni.
- **Matériel Open-Source** : La conception du RP2040 est bien documentée, encourageant le développement de cartes personnalisées.

---

### **Comparaison avec les Alternatives**
- **Arduino** : Le Pico est plus rapide (dual-core, 133 MHz contre 16 MHz pour l'Arduino Uno) et moins cher, avec plus de GPIO et des fonctionnalités avancées comme PIO. Cependant, Arduino a un plus grand écosystème de shields et de bibliothèques.
- **ESP32** : L'ESP32 offre le Wi-Fi et le Bluetooth intégrés, mais le Pico W égalise cela à un coût inférieur. Le PIO du Pico est unique pour les protocoles personnalisés.
- **STM32** : Le Pico est plus facile à programmer pour les débutants (par exemple, avec MicroPython) et plus abordable que de nombreuses cartes STM32.

---

### **Limitations**
- **Pas de Sans Fil Intégré (Modèle de Base)** : Le Pico original manque de Wi-Fi/Bluetooth, bien que le Pico W résolve ce problème.
- **Stockage Intégré Limité** : 2 Mo de flash sont suffisants pour la plupart des projets mais peuvent limiter les applications complexes.
- **Logique 3,3V** : Nécessite des convertisseurs de niveau pour les périphériques 5V.
- **Pas de Bouton de Réinitialisation Intégré** : Un inconvénient mineur pour certains utilisateurs.

---

### **Pour Commencer**
Pour débuter avec le Raspberry Pi Pico :
1. **Configuration Matérielle** : Connectez le Pico à un ordinateur via USB ou alimentez-le externe.
2. **Installer le Microprogramme** : Téléchargez le microprogramme MicroPython ou CircuitPython depuis le site Web de Raspberry Pi ou Adafruit et téléversez-le en maintenant BOOTSEL et en connectant le Pico.
3. **Programmation** : Utilisez Thonny pour Python ou configurez le Pico SDK pour le développement C/C++.
4. **Projets** : Commencez par des projets simples comme faire clignoter une LED ou lire un capteur, puis explorez des applications avancées comme l'IoT ou la robotique.

---

### **Conclusion**
Le Raspberry Pi Pico est un microcontrôleur puissant, abordable et convivial qui a démocratisé le développement de systèmes embarqués. Sa puce RP2040 personnalisée, ses capacités GPIO étendues et son support pour plusieurs langages de programmation en font un choix privilégié pour les amateurs, les éducateurs et les professionnels. Avec des variantes comme le Pico W et le Pico 2, il continue d'évoluer, offrant une connectivité sans fil et des performances améliorées pour les applications modernes. Soutenu par l'excellente documentation de la Raspberry Pi Foundation et une communauté dynamique, le Pico est une plateforme idéale pour apprendre, prototyper et construire des projets innovants.

Si vous souhaitez des détails spécifiques sur la programmation du Pico, des idées de projets ou des comparaisons avec d'autres microcontrôleurs, faites-le moi savoir !