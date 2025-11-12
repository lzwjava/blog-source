---
audio: false
generated: true
lang: fr
layout: post
title: Technologie des entrées-sorties et des interfaces
translated: true
type: note
---

Excellent ! Voici un **tutoriel complet** pour la **Partie 4 : Technologie des Entrées/Sorties et des Interfaces**, basé sur votre plan de cours. Ce tutoriel est structuré pour expliquer les concepts clairement, fournir des exemples pratiques et montrer comment les composants comme le 8255A, le 8253/8254 et le 8251A fonctionnent ensemble dans un système micro-informatique.

---

## 📘 Partie 4 : Technologie des Entrées/Sorties et des Interfaces

---

### **1. Bases des Interfaces d'E/S**

#### ✅ Adressage des Ports

Les interfaces d'E/S permettent à un microprocesseur de communiquer avec des périphériques externes. Il existe **deux principaux modes d'adressage** :

- **E/S à mémoire mappée** :
  - Les périphériques d'E/S sont traités comme des emplacements mémoire.
  - Utilise les mêmes instructions que l'accès mémoire (par exemple, `MOV`).
  - Avantages : Espace d'adressage plus large, peut utiliser toutes les instructions du CPU.
  - Inconvénients : Consomme l'espace d'adressage mémoire.

- **E/S isolées (E/S à ports mappés)** :
  - Instructions spéciales comme `IN` et `OUT`.
  - Espace d'adressage limité (généralement 256 ports).
  - Espace d'adressage séparé de la mémoire.

| Type                   | Jeu d'Instructions Utilisé | Espace d'Adressage |
|------------------------|----------------------------|--------------------|
| E/S à mémoire mappée   | `MOV`, etc.                | Fait partie de la mémoire |
| E/S isolées (à ports mappés) | `IN`, `OUT`            | Espace d'E/S séparé |

---

#### ✅ Modes de Transfert de Données

1. **E/S contrôlée par programme** :
   - Le CPU vérifie l'état du périphérique et lit/écrit les données directement.
   - Simple mais inefficace (attente active).

2. **E/S par interruption** :
   - Le périphérique notifie le CPU lorsqu'il est prêt via une **interruption**.
   - Le CPU exécute une Routine de Service d'Interruption (ISR).
   - Améliore l'efficacité.

3. **DMA (Accès Direct Mémoire)** :
   - Le périphérique transfère les données directement vers/depuis la mémoire.
   - Contourne le CPU pour les transferts de données volumineux/rapides.
   - Utilisé pour les périphériques haute vitesse comme les disques.

---

### **2. Systèmes d'Interruption**

#### ✅ Table des Vecteurs d'Interruption

- Stocke les adresses des **Routines de Service d'Interruption (ISR)**.
- Chaque type d'interruption a un **vecteur unique** (par exemple, INT 0x08 pour le Timer).
- Le CPU consulte la table pour sauter vers la bonne ISR.

#### ✅ Gestion des Priorités

- Lorsque plusieurs interruptions se produisent simultanément, la **priorité** détermine laquelle est traitée en premier.
- La priorité peut être **fixe** ou **programmable**.

#### ✅ Contrôleur d'Interruption Programmable 8259A

- Gère plusieurs sources d'interruption (jusqu'à 8).
- Peut être **cascadé** pour 64 entrées d'interruption.
- Fonctions clés :
  - Masquage des interruptions.
  - Réglage de la priorité.
  - Envoi du vecteur d'interruption au CPU.

**Registres** :
- IMR (Registre de Masquage d'Interruption)
- ISR (Registre d'Interruption en Service)
- IRR (Registre de Demande d'Interruption)

**Exemple** : Le clavier et le Timer déclenchent tous deux des interruptions — le 8259A les priorise en fonction de la priorité configurée.

---

### **3. Circuits d'Interface Courants**

---

#### ✅ Interface Périphérique Programmable 8255A (PPI)

Utilisé pour interfacer avec des périphériques parallèles externes comme des interrupteurs, LED, etc.

- Possède 3 ports : **Port A**, **Port B** et **Port C**.
- Contrôlé via un **Mot de Contrôle**.

**Modes de Fonctionnement** :

- **Mode 0** – E/S simples
  - Chaque port peut être entrée ou sortie.
- **Mode 1** – E/S avec acquittement
  - Prend en charge la synchronisation avec le périphérique.
- **Mode 2** – E/S bidirectionnelles (uniquement pour le Port A)
  - Transfert de données bidirectionnel avec acquittement.

**Exemple** :
- Port A : sortie vers un afficheur LED
- Port B : entrée depuis des interrupteurs DIP
- Port C : utilisé pour les signaux de contrôle

---

#### ✅ Minuterie à Intervalle Programmable 8253 / 8254

Utilisée pour générer des délais, des débits en bauds, etc.

- Possède 3 compteurs 16 bits indépendants.
- Chaque compteur a des modes (0–5), par exemple :

| Mode | Description                 |
|------|-----------------------------|
| 0    | Interruption sur fin de comptage |
| 2    | Générateur de taux (par ex., pour horloge) |
| 3    | Générateur d'onde carrée    |

**Applications** :
- Génération de délais
- Horloge temps réel
- Génération de débit en bauds pour les ports série

**Utilisation Typique** :
- Compteur 0 : tick du timer du système d'exploitation
- Compteur 1 : rafraîchissement DRAM
- Compteur 2 : tonalité du haut-parleur

---

#### ✅ USART 8251A (Émetteur-Récepteur Asynchrone/Synchrone Universel)

Utilisé pour la **communication série**.

- Convertit les données entre le format parallèle et série.
- Prend en charge les deux modes :
  - **Synchrone** : nécessite un signal d'horloge
  - **Asynchrone** : utilise des bits de start/stop

**Caractéristiques Clés** :
- Contrôle du débit en bauds (via 8253/8254)
- Longueur de caractère, bits d'arrêt, parité configurables
- Prend en charge la mise en mémoire tampon d'émission et de réception

**Application** : Communication par port série avec un PC ou un microcontrôleur.

---

## ✅ Tableau Récapitulatif

| Circuit | Fonction                      | Caractéristiques Principales               |
|---------|-------------------------------|--------------------------------------------|
| 8255A   | E/S parallèles                | 3 ports, 3 modes, acquittement             |
| 8253/54 | Minuterie/comptage            | 3 compteurs, multiples modes               |
| 8251A   | Communication série           | Sync/Async, contrôle du débit en bauds     |
| 8259A   | Contrôle d'interruption       | Priorité, masquage, vectorisation des ISR  |

---

## 🧠 Scénario d'Exemple Réel

Vous souhaitez concevoir un système micro-informatique simple pour :

- Contrôler une matrice de LED via le Port A (8255A Mode 0)
- Recevoir les entrées clavier via des interruptions (8259A)
- Générer un tick système périodique toutes les 1ms (8253 Mode 2)
- Envoyer les données d'un capteur vers un PC via une liaison série (8251A en mode asynchrone)

Chaque circuit serait configuré et connecté au CPU via un décodage d'adresse et des signaux de contrôle, avec un logiciel approprié écrit pour gérer la communication.

---

Faites-moi savoir si vous voulez un exemple de code, des schémas de simulation ou un quiz pour ce chapitre !