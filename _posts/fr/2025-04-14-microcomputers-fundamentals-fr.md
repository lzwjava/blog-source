---
audio: false
generated: true
lang: fr
layout: post
title: Fondamentaux des microordinateurs
translated: true
type: note
---

Voici un tutoriel complet pour **Partie 1 : Principes fondamentaux des micro-ordinateurs**, couvrant les sujets mentionnés dans votre requête : *Aperçu des systèmes de micro-ordinateurs, Évolution, Architecture de Von Neumann, Métriques de performance clés, Structure du microprocesseur (CPU), Registres internes du 8086/8088, et Cycles de bus et analyse temporelle*. Ce tutoriel est conçu pour être complet tout en restant accessible, en supposant une compréhension fondamentale des systèmes informatiques.

---

## Partie 1 : Principes fondamentaux des micro-ordinateurs

### 1. Aperçu des systèmes de micro-ordinateurs

Un **micro-ordinateur** est un petit ordinateur relativement peu coûteux utilisant un microprocesseur comme unité centrale de traitement (CPU). Il comprend de la mémoire, des interfaces d'entrée/sortie (E/S) et des périphériques, ce qui le rend adapté aux applications personnelles, embarquées ou industrielles.

#### Composants d'un système de micro-ordinateur
- **Microprocesseur (CPU)** : Le cerveau du système, exécutant les instructions en les chargeant, les décodant et les exécutant.
- **Mémoire** :
  - **ROM (Mémoire morte)** : Stocke le firmware ou les instructions permanentes (par exemple, le BIOS).
  - **RAM (Mémoire vive)** : Stockage temporaire pour les données et les programmes pendant l'exécution.
- **Périphériques d'Entrée/Sortie (E/S)** : Interfaces pour l'interaction utilisateur (par exemple, clavier, souris, écran).
- **Système de bus** :
  - **Bus de données** : Transfère les données entre les composants.
  - **Bus d'adresse** : Spécifie les emplacements mémoire ou d'E/S.
  - **Bus de contrôle** : Transporte les signaux de contrôle pour coordonner les opérations.
- **Périphériques** : Stockage (par exemple, disques durs), ports de communication et autres matériels.

#### Caractéristiques
- Taille compacte, faible coût et polyvalence.
- Utilisé dans les ordinateurs personnels, les systèmes embarqués (par exemple, appareils électroménagers, voitures) et les appareils IoT.
- Programmable pour diverses tâches via un logiciel.

---

### 2. Évolution des micro-ordinateurs

L'évolution des micro-ordinateurs reflète les progrès de la technologie des semi-conducteurs, des logiciels et de la conception des architectures.

#### Jalons principaux
- **1971 : Intel 4004** : Le premier microprocesseur, un CPU 4 bits avec 2 300 transistors, conçu pour les calculatrices.
- **1974 : Intel 8080** : Un microprocesseur 8 bits, considéré comme le premier véritable CPU de micro-ordinateur, utilisé dans les premiers systèmes comme l'Altair 8800.
- **1978 : Intel 8086/8088** : Processeurs 16 bits qui ont équipé le PC IBM (1981), établissant l'architecture x86.
- **Années 1980 : Ordinateurs personnels** : Apple II, IBM PC et Commodore 64 ont démocratisé l'informatique.
- **Années 1990–2000** : Processeurs 32 bits et 64 bits (par exemple, Intel Pentium, AMD Athlon) avec des performances accrues.
- **Années 2010–Présent** : Les processeurs multi-cœurs, les GPU et les micro-ordinateurs basés sur ARM (par exemple, Raspberry Pi) dominent les systèmes mobiles et embarqués.

#### Tendances
- **Loi de Moore** : Le nombre de transistors double environ tous les 18 à 24 mois, permettant des CPU plus rapides et plus petits.
- **Miniaturisation** : Des ordinateurs de la taille d'une pièce aux appareils portables.
- **Intégration** : Les conceptions System-on-Chip (SoC) combinent le CPU, le GPU et la mémoire.
- **Efficacité énergétique** : Concentration sur les processeurs à faible consommation pour les applications mobiles et IoT.

---

### 3. Architecture de Von Neumann

L'**architecture de Von Neumann** est le fondement de la plupart des ordinateurs modernes, y compris les micro-ordinateurs. Proposée par John von Neumann en 1945, elle décrit un système où une mémoire unique stocke à la fois les instructions et les données.

#### Caractéristiques principales
- **Mémoire unique** : Les programmes (instructions) et les données partagent le même espace mémoire, accessible via le même bus.
- **Composants** :
  - **CPU** : Contient :
    - **Unité Arithmétique et Logique (UAL)** : Effectue les calculs.
    - **Unité de Contrôle (UC)** : Gère le chargement, le décodage et l'exécution des instructions.
    - **Registres** : Petit stockage rapide pour les données temporaires (par exemple, Compteur Ordinal, Accumulateur).
  - **Mémoire** : Stocke les instructions et les données.
  - **Système d'E/S** : Interfaces avec les périphériques externes.
  - **Bus** : Connecte les composants pour les données, les adresses et les signaux de contrôle.
- **Concept de programme enregistré** : Les instructions sont stockées en mémoire, permettant aux programmes d'être modifiés dynamiquement.
- **Exécution séquentielle** : Les instructions sont chargées, décodées et exécutées une à la fois.

#### Goulot d'étranglement de Von Neumann
- Le bus partagé entre le CPU et la mémoire limite les performances, car les données et les instructions ne peuvent pas être chargées simultanément.
- Solutions : Mémoire cache, pipeline et architecture Harvard (mémoire d'instructions et de données séparées, utilisée dans certains microcontrôleurs).

#### Exemple
Dans un micro-ordinateur basé sur le 8086 :
- Les instructions (par exemple, `MOV AX, BX`) et les données (par exemple, les valeurs dans AX, BX) résident dans la RAM.
- Le CPU charge les instructions via le bus d'adresse, les traite et stocke les résultats en mémoire ou dans les registres.

---

### 4. Métriques de performance clés

La performance d'un micro-ordinateur dépend de plusieurs métriques qui définissent sa capacité de traitement et son efficacité.

#### a. Longueur de mot
- **Définition** : Le nombre de bits que le CPU peut traiter en une seule opération (par exemple, 8 bits, 16 bits, 32 bits, 64 bits).
- **Impact** :
  - Des longueurs de mot plus grandes permettent de traiter plus de données à la fois, améliorant les performances.
  - Détermine la plage de mémoire adressable (par exemple, bus d'adresse 16 bits = 64 Ko, 32 bits = 4 Go).
- **Exemple** : L'Intel 8086 a une longueur de mot de 16 bits, tandis que les CPU modernes utilisent des architectures 64 bits.

#### b. Fréquence d'horloge
- **Définition** : La fréquence à laquelle le CPU exécute les instructions, mesurée en Hertz (Hz), généralement en MHz ou GHz.
- **Impact** :
  - Des fréquences d'horloge plus élevées signifient plus de cycles par seconde, augmentant le débit.
  - Limité par la consommation d'énergie et la dissipation thermique.
- **Exemple** : Le 8086 fonctionnait à 4,77–10 MHz ; les CPU modernes dépassent 5 GHz avec le turbo boost.

#### c. Capacité mémoire
- **Définition** : La quantité de RAM et de ROM disponible pour stocker les données et les programmes.
- **Impact** :
  - Une mémoire plus grande prend en charge des applications complexes et le multitâche.
  - La mémoire cache (par exemple, L1, L2) réduit la latence d'accès.
- **Exemple** : Les premiers systèmes 8086 avaient 64 Ko–1 Mo de RAM ; les systèmes modernes ont 16–128 Go.

#### Autres métriques
- **Complexité du jeu d'instructions** : CISC (par exemple, x86) vs RISC (par exemple, ARM) affecte l'efficacité.
- **Largeur du bus** : Des bus plus larges (par exemple, 32 bits vs 16 bits) améliorent les taux de transfert de données.
- **MIPS/FLOPS** : Mesure le nombre d'instructions ou d'opérations en virgule flottante par seconde.

---

### 5. Structure du microprocesseur (CPU)

Le microprocesseur est le cœur d'un micro-ordinateur, responsable de l'exécution des instructions. Sa structure comprend des unités fonctionnelles et des interconnexions.

#### Composants généraux du CPU
- **Unité Arithmétique et Logique (UAL)** : Effectue les opérations arithmétiques (par exemple, l'addition) et logiques (par exemple, ET, OU).
- **Unité de Contrôle (UC)** : Coordonne le chargement, le décodage et l'exécution des instructions.
- **Registres** : Mémoire haute vitesse pour les données temporaires (par exemple, accumulateurs, registres d'index).
- **Compteur Ordinal (CO)** : Contient l'adresse de la prochaine instruction.
- **Registre d'Instruction (RI)** : Stocke l'instruction en cours.
- **Unité d'Interface de Bus (BIU)** : Gère la communication avec la mémoire et les E/S.

#### Structure du CPU 8086/8088
L'Intel 8086 (16 bits) et le 8088 (bus de données externe 8 bits) partagent une structure interne similaire, divisée en :
- **Unité d'Interface de Bus (BIU)** :
  - Gère les opérations mémoire et E/S.
  - Contient les registres de segment (CS, DS, SS, ES) pour adresser jusqu'à 1 Mo de mémoire.
  - Génère les adresses physiques en utilisant l'adressage segment:offset.
- **Unité d'Exécution (EU)** :
  - Exécute les instructions en utilisant l'UAL et les registres généraux.
  - Inclut un registre d'état pour les flags (par exemple, zéro, retenue, signe).

---

### 6. Registres internes du 8086/8088

Les registres sont de petites unités de stockage rapides à l'intérieur du CPU. Le 8086/8088 possède 14 registres 16 bits, catégorisés comme suit :

#### a. Registres généraux
Utilisés pour la manipulation des données et l'arithmétique.
- **AX (Accumulateur)** : Registre principal pour l'arithmétique, les E/S et le transfert de données.
  - Divisé en AH (octet haut) et AL (octet bas).
- **BX (Base)** : Contient les adresses de base ou les données.
- **CX (Compteur)** : Utilisé dans les boucles et les opérations sur les chaînes.
- **DX (Données)** : Stocke les données ou les adresses de ports E/S.

#### b. Registres de segment
Utilisés pour l'adressage mémoire (espace d'adressage de 1 Mo).
- **CS (Segment de Code)** : Pointe vers le segment de code pour les instructions.
- **DS (Segment de Données)** : Pointe vers le segment de données.
- **SS (Segment de Pile)** : Pointe vers la pile pour les appels de fonction et les interruptions.
- **ES (Segment Extra)** : Utilisé pour les segments de données supplémentaires.

#### c. Registres pointeur et index
Gèrent les pointeurs mémoire et l'indexation.
- **SP (Pointeur de Pile)** : Pointe vers le haut de la pile.
- **BP (Pointeur de Base)** : Accède aux données de la pile (par exemple, paramètres de fonction).
- **SI (Index Source)** : Pointe vers les données source dans les opérations sur les chaînes.
- **DI (Index Destination)** : Pointe vers les données de destination dans les opérations sur les chaînes.

#### d. Pointeur d'instruction
- **IP** : Contient l'offset de la prochaine instruction dans le segment de code.

#### e. Registre d'état
Un registre 16 bits avec des flags d'état et de contrôle :
- **Flags d'état** :
  - **ZF (Flag Zéro)** : Défini si le résultat est zéro.
  - **SF (Flag Signe)** : Défini si le résultat est négatif.
  - **CF (Flag de Retenue)** : Défini s'il y a une retenue/emprunt.
  - **OF (Flag de Débordement)** : Défini en cas de débordement arithmétique.
  - **AF (Retenue Auxiliaire)** : Utilisé pour l'arithmétique BCD.
  - **PF (Flag de Parité)** : Défini si le résultat a une parité paire.
- **Flags de contrôle** :
  - **DF (Flag de Direction)** : Contrôle la direction des opérations sur les chaînes.
  - **IF (Flag d'Interruption)** : Active/désactive les interruptions.
  - **TF (Flag de Piste)** : Active le débogage pas à pas.

#### Adressage dans le 8086/8088
- **Adresse Physique** = Registre de Segment × 16 + Offset.
- Exemple : Si CS = 1000h et IP = 0100h, l'adresse de l'instruction est 1000h × 16 + 0100h = 10100h.

---

### 7. Cycles de bus et analyse temporelle

Le 8086/8088 communique avec la mémoire et les périphériques E/S via des **cycles de bus**, synchronisés par l'horloge du CPU. Un cycle de bus définit le processus de lecture ou d'écriture de données.

#### Types de cycles de bus
- **Lecture mémoire** : Charge les instructions ou les données depuis la mémoire.
- **Écriture mémoire** : Stocke les données en mémoire.
- **Lecture E/S** : Lit les données depuis un périphérique E/S.
- **Écriture E/S** : Envoie les données à un périphérique E/S.

#### Structure d'un cycle de bus
Chaque cycle de bus consiste en **4 états T** (cycles d'horloge) :
1. **T1** : L'adresse est placée sur le bus d'adresse ; le signal ALE (Address Latch Enable) est activé.
2. **T2** : Les signaux de contrôle (par exemple, RD pour la lecture, WR pour l'écriture) sont émis.
3. **T3** : Les données sont transférées sur le bus de données.
4. **T4** : Le cycle de bus se termine ; les signaux d'état sont mis à jour.

#### Analyse temporelle
- **Fréquence d'horloge** : Détermine la durée d'un état T (par exemple, à 5 MHz, 1 état T = 200 ns).
- **États d'attente** : Ajoutés si la mémoire/les périphériques sont plus lents que le CPU, prolongeant T3.
- **Exemple** :
  - Pour une lecture mémoire à 5 MHz :
    - T1 : Configuration de l'adresse (200 ns).
    - T2 : Signal RD actif (200 ns).
    - T3 : Échantillonnage des données (200 ns, ou plus long avec des états d'attente).
    - T4 : Bus libéré (200 ns).
    - Total = 800 ns sans états d'attente.
- **Différence du 8088** : Le 8088 utilise un bus de données 8 bits, nécessitant deux cycles de bus pour les transferts de données 16 bits, réduisant les performances par rapport au bus 16 bits du 8086.

#### Signaux de bus
- **ALE** : Verrouille l'adresse depuis le bus adresse/données multiplexé.
- **RD/WR** : Indique une opération de lecture ou d'écriture.
- **M/IO** : Distingue l'accès mémoire de l'accès E/S.
- **DT/R** : Définit la direction du bus de données (transmettre/recevoir).
- **DEN** : Active les transcepteurs du bus de données.

#### Considérations pratiques
- **Temps d'accès mémoire** : Doit être inférieur à la durée du cycle de bus pour éviter les états d'attente.
- **Interruptions** : Peuvent interrompre les cycles de bus pour gérer des événements externes.
- **DMA (Accès Direct Mémoire)** : Interrompt temporairement l'accès au bus par le CPU pour des transferts de données plus rapides.

---

### Exemple : Exécution d'une instruction du 8086
Traçons une instruction simple, `MOV AX, [1234h]`, en supposant DS = 1000h :
1. **Chargement** :
   - La BIU calcule l'adresse : 1000h × 16 + 1234h = 11234h.
   - L'instruction est chargée via un cycle de lecture mémoire (4 états T).
2. **Décodage** :
   - L'EU décode `MOV` comme un transfert mémoire-vers-registre.
3. **Exécution** :
   - La BIU effectue une autre lecture mémoire à 11234h pour charger les données 16 bits.
   - Les données sont chargées dans AX.
4. **Cycles de bus** :
   - Chargement de l'instruction : 4 états T.
   - Chargement des données : 4 états T.
   - Total : ~8 états T (1,6 µs à 5 MHz, sans états d'attente).

---

### Résumé
- **Systèmes de micro-ordinateurs** : Intègrent CPU, mémoire, E/S et bus pour une informatique polyvalente.
- **Évolution** : Du Intel 4004 4 bits aux processeurs multi-cœurs 64 bits modernes.
- **Architecture de Von Neumann** : Mémoire unifiée pour les instructions et les données, avec un modèle d'exécution séquentielle.
- **Métriques de performance** : La longueur de mot, la fréquence d'horloge et la capacité mémoire déterminent les capacités.
- **Structure du 8086/8088** : BIU et EU avec des registres spécialisés pour l'adressage et l'exécution.
- **Registres** : Les registres généraux, de segment, pointeurs et d'état permettent une programmation flexible.
- **Cycles de bus** : 4 états T pour les opérations mémoire/E/S, critiques pour le timing et les performances.

---

### Questions pratiques
1. Expliquez le goulot d'étranglement de Von Neumann et comment les CPU modernes l'atténuent.
2. Calculez l'adresse physique pour CS = 2000h, IP = 0500h.
3. Décrivez le rôle de chaque registre de segment du 8086.
4. Comment le bus de données 8 bits du 8088 affecte-t-il les performances par rapport au 8086 ?
5. Simulez le cycle de bus pour une opération d'écriture mémoire à 8 MHz.

---

Ce tutoriel fournit une base solide pour comprendre les principes fondamentaux des micro-ordinateurs, en se concentrant sur l'architecture 8086/8088. Si vous souhaitez approfondir des sujets spécifiques (par exemple, la programmation assembleur, la gestion des interruptions), faites-le moi savoir !