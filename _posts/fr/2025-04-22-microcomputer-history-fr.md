---
audio: false
generated: true
lang: fr
layout: post
title: Histoire de l'ordinateur individuel
translated: true
type: note
---

Le cours **Microcomputer and Interface Technology**, tel que décrit, se concentre sur l'architecture, la programmation et l'interfaçage des systèmes micro-informatiques, avec un accent particulier sur les microprocesseurs Intel 8086/8088 et les technologies d'interface associées (par exemple, les puces 8255, 8253, 8251). Pour fournir une histoire complète, je retracerai les origines et l'évolution des technologies clés couvertes dans le cours, identifierai les figures clés et les entreprises derrière leur développement, et explorerai les histoires de leur création. Cela inclut le micro-ordinateur lui-même, les microprocesseurs 8086/8088, la programmation en langage assembleur, les systèmes mémoire, les technologies d'interface d'E/S et les standards de bus.

---

### **1. Le Micro-ordinateur : Origines et Évolution**

#### **Qu'est-ce qu'un Micro-ordinateur ?**
Un micro-ordinateur est un petit ordinateur abordable construit autour d'un microprocesseur, intégrant un CPU, une mémoire et des capacités d'E/S. Le cours commence par une vue d'ensemble des systèmes micro-informatiques, basée sur l'**architecture de Von Neumann** (un CPU, une mémoire pour les instructions et les données, et des E/S connectées via des bus).

#### **Histoire et Découverte**
- **Avant les années 1970 : Fondations**
  - Le concept d'un ordinateur programmable remonte à la machine analytique de **Charles Babbage** (années 1830), bien qu'elle n'ait jamais été construite. Les travaux théoriques d'**Alan Turing** (1936) et le rapport de 1945 de **John von Neumann** sur l'EDVAC ont formalisé l'ordinateur à programme enregistré, où les instructions et les données partagent la mémoire. Cette **architecture de Von Neumann** est devenue le plan directeur des micro-ordinateurs.
  - Les premiers ordinateurs (par exemple, l'ENIAC, 1945) étaient massifs et utilisaient des tubes à vide. L'invention du **transistor** (1947, **John Bardeen**, **Walter Brattain**, **William Shockley** aux Bell Labs) et du **circuit intégré** (1958, **Jack Kilby** chez Texas Instruments et **Robert Noyce** chez Fairchild) a permis l'électronique compacte.

- **1971 : Le Premier Microprocesseur**
  - **Qui l'a Découvert ?** : **Intel**, spécifiquement les ingénieurs **Federico Faggin**, **Ted Hoff** et **Stan Mazor**, ont développé le **Intel 4004**, le premier microprocesseur, commercialisé en novembre 1971.
  - **Histoire** : Commandé par l'entreprise japonaise de calculatrices Busicom, Intel fut chargé de concevoir une puce pour une calculatrice programmable. Ted Hoff proposa une puce unique et généraliste au lieu de plusieurs puces spécialisées, réduisant les coûts et la complexité. Federico Faggin dirigea la conception, entassant 2 300 transistors dans un processeur 4 bits (740 kHz, bus d'adresse 12 bits). Le 4004 pouvait exécuter 60 000 instructions par seconde, un bond en avant pour l'époque.
  - **Impact** : Le 4004 alimentait la calculatrice Busicom 141-PF et inspira Intel pour le commercialiser comme un processeur généraliste, donnant naissance à l'industrie du microprocesseur.

- **Années 1970 : Émergence du Micro-ordinateur**
  - **1974** : Le **8080** d'Intel (8 bits, 2 MHz) alimenta l'**Altair 8800** (1975, MITS), le premier micro-ordinateur commercial réussi. Commercialisé comme un kit pour amateurs, il exécutait **CP/M** (un système d'exploitation précoce) et inspira **Bill Gates** et **Paul Allen** à fonder Microsoft, en écrivant un interpréteur BASIC pour celui-ci.
  - **1977** : L'**Apple II** (Steve Wozniak, Steve Jobs), le **Commodore PET** et le **TRS-80** ont rendu les micro-ordinateurs accessibles aux consommateurs, avec claviers, écrans et logiciels.
  - **Histoire** : Le succès de l'Altair provenait de sa conception ouverte et de sa couverture dans *Popular Electronics*. Les amateurs formèrent des clubs (par exemple, le Homebrew Computer Club), favorisant l'innovation. La conception de l'Apple II par Wozniak priorisait l'abordabilité et la facilité d'utilisation, utilisant le processeur MOS 6502.

- **Contexte du Cours** : Le cours se concentre sur le **Intel 8086/8088**, introduit en 1978, qui alimenta l'**IBM PC** (1981), standardisant les micro-ordinateurs pour les entreprises et les foyers.

#### **Figures Clés**
- **Federico Faggin** : A dirigé la conception du 4004, a ensuite cofondé Zilog (processeur Z80).
- **Ted Hoff** : A conçu le concept de microprocesseur.
- **Robert Noyce et Gordon Moore** : Fondateurs d'Intel, ont conduit le développement des circuits intégrés et des microprocesseurs.
- **Ed Roberts** : Fondateur de MITS, créateur de l'Altair 8800.

---

### **2. Le Microprocesseur Intel 8086/8088**

#### **Qu'est-ce que c'est ?**
Le 8086 (16 bits, 5-10 MHz) et le 8088 (bus externe 8 bits) sont des microprocesseurs centraux au cours, connus pour leur modèle de mémoire segmenté, leur espace d'adressage de 1 Mo et leur architecture x86, qui reste dominante aujourd'hui.

#### **Histoire et Découverte**
- **1976-1978 : Développement**
  - **Qui l'a Découvert ?** : L'équipe d'Intel, dirigée par **Stephen Morse** (architecture et jeu d'instructions), **Bruce Ravenel** (microcode) et **Jim McKevitt** (gestion de projet), a conçu le 8086, commercialisé en juin 1978. Le 8088 suivit en 1979.
  - **Histoire** : Intel visait à dépasser les processeurs 8 bits (par exemple, 8080, Z80) pour concurrencer sur un marché en croissance. Le 8086 fut conçu comme un processeur 16 bits avec un bus d'adresse 20 bits, supportant 1 Mo de mémoire (contre 64 Ko pour les puces 8 bits). Son jeu d'instructions était rétrocompatible avec le 8080, facilitant les transitions logicielles. Le 8088, avec un bus externe 8 bits, réduisait le coût du système, le rendant attractif pour IBM.
  - **Défis** : La complexité du 8086 (29 000 transistors) repoussa les limites de fabrication d'Intel. Son modèle de mémoire segmenté (segments de 64 Ko, adressage par offset) était un compromis pour équilibrer performance et compatibilité.

- **1981 : Adoption par l'IBM PC**
  - **Histoire** : IBM, entrant sur le marché des PC, choisit le 8088 pour son **IBM PC** (modèle 5150) en raison de son rapport coût-efficacité et du support d'Intel. La décision fut influencée par l'équipe de **Bill Lowe** au laboratoire d'IBM à Boca Raton, qui priorisait une architecture ouverte utilisant des composants standards. Le 8088 fonctionnait à 4,77 MHz, et le succès du PC standardisa l'architecture x86.
  - **Impact** : La conception ouverte de l'IBM PC permit les clones (par exemple, Compaq, Dell), alimentant l'industrie du PC. **MS-DOS** de Microsoft, développé pour le PC, devint le système d'exploitation dominant.

- **Héritage** : L'architecture x86 a évolué à travers le 80286 (1982), le 80386 (1985) et les processeurs modernes.

#### **Figures Clés**
- **Stephen Morse** : Architecte en chef du 8086.
- **Bill Lowe** : Responsable IBM pour le PC.
- **Intel Teams** : Ingénieurs ayant conçu le 8086/8088.

---

### **3. Programmation en Langage Assembleur**

#### **Qu'est-ce que c'est ?**
Le langage assembleur est un langage de bas niveau utilisant des mnémoniques pour représenter les instructions machine. Le cours enseigne la programmation assembleur pour le 8086/8088, couvrant les registres, les modes d'adressage et les instructions.

#### **Histoire et Découverte**
- **Années 1940 : Origines**
  - Les premiers ordinateurs étaient programmés en langage machine (binaire). L'assembleur fut développé pour simplifier ce processus en utilisant des symboles.
  - **Histoire** : Les premiers assembleurs sont apparus pour des ordinateurs comme l'EDSAC (1949), où **David Wheeler** écrivit le premier programme assembleur. Les mnémoniques (par exemple, ADD, MOV) représentaient les codes d'opération.

- **Années 1970 : Assembleur pour Microprocesseurs**
  - Avec l'avènement des microprocesseurs (par exemple, Intel 4004, 8080), les assembleurs sont devenus essentiels pour la programmation système. Intel a fourni des outils comme l'**ASM86** pour le 8086.
  - **Histoire** : Les programmeurs utilisaient l'assembleur pour écrire des systèmes d'exploitation (par exemple, MS-DOS en partie) et des pilotes, optimisant les performances sur des matériels limités. Le cours utilise probablement un émulateur ou un assembleur comme MASM.

- **Contexte du Cours** : L'assembleur 8086 est enseigné pour comprendre l'architecture matérielle, les opérations de bas niveau et l'optimisation.

#### **Figures Clés**
- **David Wheeler** : Pionnier de la programmation assembleur.
- **Intel Engineers** : Ont développé les jeux d'instructions et les outils assembleur.

---

### **4. Systèmes Mémoire**

#### **Qu'est-ce que c'est ?**
La mémoire stocke les instructions et les données. Le cours couvre la RAM, la ROM et les techniques d'expansion mémoire pour les systèmes 8086.

#### **Histoire et Découverte**
- **Années 1960-1970 : Développement de la Mémoire**
  - La **mémoire à tores magnétiques** était utilisée dans les premiers ordinateurs, mais les puces mémoire à semi-conducteurs (RAM/ROM) ont émergé avec les circuits intégrés.
  - **Histoire** : **Intel** a développé la première puce **DRAM** (1103, 1 Kbit) en 1970, basée sur des travaux de **Robert Dennard** d'IBM (brevet 1968). La DRAM stockait des bits dans des cellules à condensateur, nécessitant un rafraîchissement périodique. La RAM statique (SRAM) était plus rapide mais plus coûteuse.
  - **ROM** : Stockait le firmware, avec des variantes comme l'**EPROM** (effaçable par UV, George Perlegos, 1971) et l'**EEPROM** (effaçable électriquement, Eli Harari, 1977).
  - **Contexte du Cours** : Le cours couvre l'expansion mémoire (par exemple, le décodage d'adresse), critique pour les systèmes 8086 avec des espaces d'adressage de 1 Mo.

#### **Figures Clés**
- **Robert Noyce** : A co-inventé le circuit intégré, permettant les puces mémoire denses.
- **Ted Hoff** : Conceptions précoces de DRAM chez Intel.
- **Dov Frohman** : A inventé l'EPROM chez Intel.

---

### **5. Technologie d'E/S et d'Interface**

#### **Qu'est-ce que c'est ?**
Les interfaces d'E/S connectent le CPU aux périphériques (par exemple, claviers, imprimantes). Le cours couvre le **8255A** (parallèle), le **8253/8254** (minuterie), le **8251A** (série) et les systèmes d'interruption (par exemple, **8259A**).

#### **Histoire et Découverte**
- **Années 1970 : Besoin d'E/S**
  - Les premiers micro-ordinateurs utilisaient des ports d'E/S simples, mais les périphériques exigeaient des puces spécialisées. Intel développa une famille de contrôleurs périphériques pour le 8080 et le 8086.
  - **Histoire** : Alors que les micro-ordinateurs devenaient complexes, le contrôle direct des E/S par le CPU devint inefficace. Les puces périphériques d'Intel déléguaient les tâches, améliorant les performances.

- **8255A Interface Périphérique Programmable (1977)**
  - **Qui ?** : Intel, conçu pour les systèmes 8080/8086.
  - **Histoire** : Le 8255A fournissait trois ports 8 bits, configurables en modes pour des E/S basiques, des E/S avec strobe ou des transferts bidirectionnels. Il simplifiait l'interfaçage avec des dispositifs comme les claviers et les écrans, devenant un pilier dans les PC.
  - **Impact** : Utilisé dans les ports parallèles de l'IBM PC (par exemple, imprimantes).

- **8253/8254 Minuterie à Intervalle Programmable (1977/1982)**
  - **Qui ?** : Intel, évoluant à partir de conceptions de minuteries antérieures.
  - **Histoire** : Le 8253 offrait trois compteurs 16 bits pour le timing (par exemple, horloges système) ou le comptage (par exemple, mesure d'impulsions). Le 8254 améliora la fiabilité. Utilisé pour les haut-parleurs PC, le rafraîchissement DRAM et les horloges temps réel.
  - **Impact** : Essentiel pour les fonctions de timing du PC.

- **8251A Interface Série (1976)**
  - **Qui ?** : Intel, pour la communication série.
  - **Histoire** : Le 8251A gérait les protocoles asynchrones (par exemple, RS-232) et synchrones, permettant les modems et les terminaux. Il était critique pour les premiers réseaux.
  - **Impact** : Alimentait les ports série PC (ports COM).

- **8259A Contrôleur d'Interruption (1979)**
  - **Qui ?** : Intel, conçu pour les systèmes à interruptions.
  - **Histoire** : Le 8259A gérait jusqu'à 8 sources d'interruption, avec possibilité de cascader pour plus, permettant aux périphériques de signaler efficacement au CPU. Il était intégral au système d'interruption de l'IBM PC.
  - **Impact** : Standardisa la gestion des interruptions dans les PC.

- **Modes de Transfert de Données**
  - **E/S Programmée** : Le CPU interrogeait les dispositifs, simple mais lent.
  - **E/S par Interruption** : Les périphériques déclenchaient des interruptions, enseigné dans le cours via le 8259A.
  - **DMA** : Le contrôleur DMA **Intel 8237** (1980) permettait des transferts haute vitesse, utilisé dans les contrôleurs de disque.

#### **Figures Clés**
- **Ingénieurs d'Intel** : Des équipes non nommées ont conçu ces puces, s'appuyant sur les écosystèmes 8080/8086.
- **Gary Kildall** : Le système d'exploitation CP/M exploitait ces puces, influençant les standards d'E/S des PC.

---

### **6. Bus et Expansion**

#### **Qu'est-ce que c'est ?**
Les bus standardisent la communication CPU-mémoire-périphériques. Le cours couvre **ISA**, **PCI** et les interfaces modernes (**USB**, **SPI**, **I²C**).

#### **Histoire et Découverte**
- **Années 1970 : Premiers Bus**
  - Le **bus S-100** (1975, Ed Roberts, MITS) était un standard précoce pour les systèmes de type Altair, adopté par les amateurs.
  - **Histoire** : L'ouverture du S-100 favorisa un écosystème micro-informatique mais manquait de standardisation.

- **1981 : Bus ISA**
  - **Qui ?** : IBM, pour l'IBM PC.
  - **Histoire** : Conçu pour le 8088, le bus ISA (Industry Standard Architecture) supportait les cartes 8 bits (PC) et 16 bits (PC/AT). Sa simplicité et la dominance du marché d'IBM en firent un standard, bien que lent (8 MHz).
  - **Impact** : Utilisé pour les cartes d'expansion (par exemple, son, graphiques) jusqu'aux années 1990.

- **1992 : Bus PCI**
  - **Qui ?** : Intel, avec des contributions d'IBM et Compaq.
  - **Histoire** : Le PCI (Peripheral Component Interconnect) adressait les limitations de l'ISA, offrant une vitesse de 33 MHz, des chemins de données 32 bits et le plug-and-play. Il devint le standard pour les PC des années 1990.
  - **Impact** : A évolué vers le PCIe, utilisé aujourd'hui.

- **Interfaces Modernes**
  - **USB (1996)** : Développé par un consortium (Intel, Microsoft, Compaq, etc.), dirigé par **Ajay Bhatt** chez Intel. L'USB unifia les connexions périphériques avec le branchement à chaud et l'évolutivité (1,5 Mbps à 480 Mbps pour l'USB 2.0).
  - **SPI (années 1980)** : Bus série de Motorola pour la communication haute vitesse et courte distance (par exemple, cartes SD).
  - **I²C (1982)** : Bus à deux fils de Philips pour les périphériques basse vitesse (par exemple, capteurs).
  - **Histoire** : L'USB émergea du besoin d'un connecteur universel, remplaçant les ports série/parallèle. Le SPI et l'I²C furent conçus pour les systèmes embarqués, simplifiant la communication entre puces.

#### **Figures Clés**
- **Ajay Bhatt** : Architecte principal de l'USB.
- **Ingénieurs d'IBM** : Ont défini l'ISA pour le PC.
- **Équipes d'Intel** : Ont conduit les standards PCI et USB.

---

### **Contexte du Cours et Instructeur**

- **Yang Quansheng** : Peu d'informations publiques existent sur l'instructeur, probablement un professeur ou un ingénieur spécialisé en génie informatique. L'accent du cours sur le 8086 et les puces Intel suggère qu'il a été conçu dans les années 1980-1990, lorsque ces technologies dominaient l'éducation en Chine et mondialement, particulièrement pour les programmes de génie.
- **Histoire derrière le Cours** :
  - Dans les années 1980, la Chine priorisait l'éducation en informatique et électronique pour rattraper la technologie occidentale. Des cours comme celui-ci étaient critiques pour former les ingénieurs en conception micro-informatique, systèmes embarqués et automatisation industrielle.
  - Le 8086/8088 et les puces périphériques d'Intel étaient idéaux pour l'enseignement en raison de leur simplicité, de leur utilisation généralisée et de leur documentation. L'inclusion d'interfaces modernes (USB, SPI, I²C) reflète des mises à jour pour rester pertinent.
  - **Filières Ciblées** : Informatique, Génie Électronique et Automatisation correspondent à l'accent du cours sur la conception matérielle, la programmation et l'intégration système, compétences clés pour des industries comme la robotique, les télécommunications et l'informatique.

---

### **Signification et Héritage**

- **Micro-ordinateurs** : Ont transformé l'informatique de machines de la taille d'une pièce à des dispositifs personnels et embarqués. L'architecture x86 du 8086/8088 reste l'épine dorsale des PC et serveurs.
- **Programmation Assembleur** : Bien que moins courante, elle est vitale pour les tâches de bas niveau (par exemple, noyaux de système d'exploitation, firmware).
- **Puces d'Interface** : Les principes du 8255, 8253 et 8251 persistent dans les microcontrôleurs modernes (par exemple, Arduino, STM32).
- **Bus** : L'ISA et le PCI ont pavé la voie pour le PCIe, tandis que l'USB, le SPI et l'I²C dominent les systèmes modernes.
- **Impact Éducatif** : Des cours comme celui-ci ont formé des générations d'ingénieurs, contribuant aux avancées technologiques mondiales, particulièrement dans l'essor technologique de la Chine.

---

### **Pertinence Moderne**
- **Systèmes Embarqués** : Les systèmes basés sur microcontrôleurs utilisent des concepts similaires d'E/S, d'interruption et de timing.
- **Systèmes Hérités** : Certains systèmes industriels et militaires utilisent encore des conceptions basées sur le 8086.
- **Éducation** : La simplicité du 8086 en fait un outil d'enseignement intemporel pour l'architecture des ordinateurs.
- **Évolution x86** : Les CPU modernes (par exemple, Intel Core, AMD Ryzen) tracent leur lignée jusqu'au 8086.

---

Si vous avez besoin de détails spécifiques (par exemple, les spécifications techniques du 8255, le développement de l'USB, ou les antécédents de Yang Quansheng) ou souhaitez explorer des sujets connexes (par exemple, l'éducation technologique en Chine dans les années 1980), faites-le moi savoir !