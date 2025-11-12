---
audio: false
generated: true
lang: fr
layout: post
title: 'Micro-ordinateur et technologie d''interface : travaux pratiques et séances'
translated: true
type: note
---

Voici un guide complet sur la section **Travaux Pratiques et Laboratoires** pour le cours **Technologie des Microordinateurs et Interfaces**, en se concentrant sur les laboratoires de base et les laboratoires complets mentionnés dans votre plan :

---

### **3. Travaux Pratiques et Laboratoires**

#### **Laboratoires de Base**

**1. Programmation Assembleur (Entrée Clavier / Sortie Affichage)**

- **Objectif** :
   L'objectif principal de ce laboratoire est d'apprendre à écrire des programmes en assembleur qui gèrent les opérations d'entrée et de sortie de base sur un microordinateur.

- **Concepts Clés** :
   - Comprendre la **syntaxe du langage assembleur**.
   - Interaction avec les ports d'E/S pour **l'entrée clavier** et **la sortie affichage**.
   - Utilisation des **interruptions** pour traiter les entrées.

- **Tâches du Laboratoire** :
   - **Entrée Clavier** : Écrire un programme assembleur qui capture une touche pressée au clavier et la stocke dans un registre.
   - **Sortie Affichage** : Programmer le système pour afficher la touche capturée sur un afficheur LED 7 segments ou un écran LCD.
   - **Contrôle du Programme** : Implémenter un flux de programme simple comme des boucles ou des sauts conditionnels basés sur l'entrée utilisateur.

- **Outils** : Microcontrôleur (ex. 8051, PIC), environnements de développement comme **Keil** ou **MPLAB**, interfaces matérielles comme **afficheurs LED** ou **LCD**, et **interfaces clavier**.

---

**2. Expériences avec LED/Clavier contrôlés par 8255A**

- **Objectif** :
   Ce laboratoire se concentre sur l'interfaçage du **Périphérique d'Interface Programmable (PPI) 8255A** avec des LED et un clavier. Cette puce aide à gérer les opérations d'entrée/sortie, ce qui est essentiel pour des systèmes micro-informatiques efficaces.

- **Concepts Clés** :
   - **Interface 8255A** : Apprendre à programmer et interfacer la puce 8255A pour contrôler les périphériques d'entrée/sortie.
   - **Modes de Port** : Le 8255A offre trois modes de fonctionnement — **Mode Entrée**, **Mode Sortie** et **Mode Bidirectionnel**. Le laboratoire met l'accent sur la configuration de la puce pour utiliser ces modes efficacement.
   - **Contrôle LED** : Implémenter l'utilisation de LED pour visualiser les résultats des entrées traitées par le système.

- **Tâches du Laboratoire** :
   - **Contrôle LED** : Développer un programme qui allume/éteint des LED spécifiques connectées à la puce 8255A.
   - **Interface Clavier** : Interfacer un **clavier** ou une **matrice de clavier** au système, permettant à l'utilisateur de saisir des données, qui peuvent ensuite être affichées via des LED ou traitées ultérieurement.
   - **Contrôle du Programme** : Apprendre à gérer le **balayage du clavier** et l'**anti-rebond**, garantissant une détection précise des touches.

- **Outils** : Puce 8255A, **kits de développement microcontrôleur**, clavier, réseaux de LED, et **logiciel pour configurer et programmer la puce 8255A** (ex. **Keil** ou **MPLAB**).

---

#### **Laboratoires Complets**

**1. Système de Contrôle de Feux de Circulation par Interruptions**

- **Objectif** :
   L'objectif principal ici est de construire un système de feux de circulation contrôlé par **interruptions**. Ce laboratoire se concentre sur le contrôle en temps réel, en utilisant les interruptions pour gérer efficacement les différents états des feux.

- **Concepts Clés** :
   - **Gestion des Interruptions** : Apprendre à implémenter des routines de service d'interruption (ISR) pour gérer les transitions des feux de circulation.
   - **Contrôle des Feux** : Contrôler plusieurs LED représentant les feux rouge, orange et vert.
   - **Interruptions Temporisées** : Utiliser les **interruptions de temporisateur** pour basculer entre les différents états des feux à des intervalles prédéfinis.

- **Tâches du Laboratoire** :
   - **Concevoir le Système de Feux** : Utiliser des microcontrôleurs et des LED pour concevoir un système de feux de circulation fonctionnel avec plusieurs phases (ex. rouge, orange, vert).
   - **Routines de Service d'Interruption (ISR)** : Développer des ISR pour changer les feux en fonction du temps ou de déclencheurs externes (ex. bouton de demande piéton).
   - **Synchronisation** : S'assurer que les transitions entre les feux se produisent de manière fluide, évitant les intersections dangereuses.

- **Outils** : Microcontrôleur, **réseaux de LED** (pour les feux de circulation), **temporisateurs**, **contrôleurs d'interruption**, et environnements de développement (ex. **Keil**, **MPLAB**).

---

**2. Communication Série (Transmission/Réception de Données)**

- **Objectif** :
   Ce laboratoire introduit la **communication série**, essentielle pour l'échange de données entre microcontrôleurs ou entre ordinateurs et périphériques externes.

- **Concepts Clés** :
   - **UART (Universal Asynchronous Receiver-Transmitter)** : Comprendre le fonctionnement du **protocole UART** pour la communication série.
   - **Trames de Données** : Apprendre la structure des paquets de données en communication série (bit de start, bits de données, bit de stop, parité).
   - **Protocoles de Communication** : Implémenter des protocoles comme **RS232**, **RS485**, ou la **communication niveau TTL** pour envoyer et recevoir des données.

- **Tâches du Laboratoire** :
   - **Implémenter la Communication UART** : Écrire des programmes en assembleur ou en C pour envoyer et recevoir des données en série entre deux microcontrôleurs ou entre un microcontrôleur et un ordinateur.
   - **Détection d'Erreur** : Apprendre à implémenter la **vérification de parité**, les **erreurs de trame** et les **erreurs de dépassement** dans le processus de communication.
   - **Transfert de Données** : Utiliser la communication série pour transférer des données simples comme du texte, des nombres ou des signaux de contrôle entre les appareils.

- **Outils** : Microcontrôleur avec support UART intégré (ex. **8051**, **PIC**, ou **AVR**), **modules d'interface série** (ex. **MAX232** pour RS232), environnements de développement (**Keil**, **MPLAB**, etc.).

---

### **Sécurité et Dépannage en Laboratoire**

- **Sécurité** : Lorsque vous travaillez avec des microcontrôleurs et des périphériques d'interfaçage, assurez-vous toujours de manipuler l'alimentation correctement et évitez les courts-circuits. Comprenez les caractéristiques électriques des composants (ex. niveaux de tension pour les microcontrôleurs).

- **Dépannage** : Les problèmes courants incluent le câblage incorrect, les connexions défectueuses et la programmation inadéquate. Utilisez des outils de débogage comme les **oscilloscopes** et les **analyseurs logiques** pour surveiller les signaux et dépanner les problèmes de communication ou de temporisation.

---

### **Conclusion**

Les laboratoires de ce cours offrent une expérience pratique en technologie des microordinateurs et des interfaces, faisant le lien entre les connaissances théoriques et les applications pratiques. Vous travaillerez sur la construction de systèmes clés comme les contrôleurs de feux de circulation et les systèmes de communication série, acquérant des compétences précieuses pour les systèmes embarqués et la programmation de microcontrôleurs.