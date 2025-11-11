---
audio: false
generated: true
lang: fr
layout: post
title: Micro-ordinateur et technologie d'interface - Aperçu
translated: true
type: note
---

Voici une version française du plan de cours **« Technologie des micro-ordinateurs et des interfaces »**, probablement basée sur le syllabus du **Professeur Yang Quansheng** (note : le contenu réel peut varier selon le programme de l'établissement) :

---

### **Technologie des micro-ordinateurs et des interfaces**
**Enseignant :** Yang Quansheng
**Filières ciblées :** Informatique, Génie électronique, Automatique, etc.

---

#### **1. Objectifs du cours**
1. Maîtriser l'architecture de base et les principes de fonctionnement des systèmes micro-informatiques.
2. Comprendre les technologies d'interface entre le CPU et les périphériques, ainsi que les méthodes de transfert de données.
3. Appliquer les circuits intégrés d'interface courants (ex. : 8255, 8253, 8251) dans la conception matérielle.
4. Développer des compétences en programmation en langage d'assemblage et en techniques de débogage des interfaces.

---

#### **2. Contenu du cours**
**Partie 1 : Fondements des micro-ordinateurs**
1. Aperçu des systèmes micro-informatiques
   - Évolution, architecture de Von Neumann
   - Métriques de performance clés (longueur de mot, fréquence d'horloge, capacité mémoire)
2. Structure du microprocesseur (CPU)
   - Registres internes du 8086/8088
   - Cycles de bus et analyse des temporisations

**Partie 2 : Programmation en langage d'assemblage**
1. Jeu d'instructions du 8086
   - Instructions de transfert de données, arithmétiques et logiques
   - Instructions de contrôle de flux (sauts, boucles, sous-routines)
2. Programmation en langage d'assemblage
   - Structures séquentielles/conditionnelles/itératives
   - Routines de service d'interruption

**Partie 3 : Systèmes mémoire**
1. Classification et extension de la mémoire
   - Principes de fonctionnement de la RAM/ROM
   - Techniques de décodage d'adresse (sélection linéaire, basée sur un décodeur)

**Partie 4 : Entrées/Sorties et technologie des interfaces**
1. Bases des interfaces d'E/S
   - Adressage des ports (E/S isolée vs. mappée en mémoire)
   - Modes de transfert de données (programmé, par interruption, DMA)
2. Systèmes d'interruption
   - Table des vecteurs d'interruption, gestion des priorités
   - Applications du contrôleur d'interruption 8259A
3. Circuits intégrés d'interface courants
   - **Interface parallèle 8255A** : Modes (0/1/2) et applications
   - **Minuterie 8253/8254** : Configurations de comptage/minuterie
   - **Interface série 8251A** : Protocoles synchrone/asynchrone

**Partie 5 : Bus et extension**
1. Normes de bus système
   - Aperçu des bus ISA, PCI
2. Technologies d'interface modernes
   - Brève introduction à l'USB, SPI, I²C

---

#### **3. Travaux pratiques et séances de laboratoire**
1. **TP fondamentaux**
   - Programmation assembleur (ex. : entrée clavier/sortie affichage)
   - Expériences de commande de LED/clavier via le 8255A
2. **TP complets**
   - Système de contrôle de feux de circulation basé sur les interruptions
   - Communication série (émission/réception de données)

---

#### **4. Évaluation**
1. **Examen théorique (60%)** : Sous surveillance, portant sur les principes des interfaces et l'analyse de conception.
2. **Évaluation des TP (30%)** : Expériences pratiques et rapports.
3. **Participation (10%)** : Devoirs et implication en classe.

---

#### **5. Références bibliographiques**
1. **Manuel principal :**
   *Microcomputer Principles and Interface Technology* (Yang Quansheng, si applicable)
2. **Textes complémentaires :**
   - *Microcomputer Principles and Interfaces* (Zhou Heqin, Feng Huanqing)
   - *The Intel Microprocessors* (Barry B. Brey)

---

#### **6. Prérequis**
- Circuits logiques numériques
- Architecture des ordinateurs
- Programmation en C

---

**Remarque :** Le syllabus réel peut être ajusté par l'enseignant. Pour la dernière version, veuillez consulter les documents de cours officiels ou contacter l'équipe pédagogique.