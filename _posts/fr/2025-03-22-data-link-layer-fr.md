---
audio: false
generated: true
lang: fr
layout: post
title: Couche de liaison de données
translated: true
type: note
---

Voici un tutoriel détaillé pour vous aider à apprendre le chapitre sur la **Couche de Liaison de Données** dans le cours **Technologie des Réseaux Informatiques** (référence 02141 dans le système chinois d'Examen en Autodidacte).

---

## **1. Aperçu de la Couche de Liaison de Données**
La Couche de Liaison de Données est la **deuxième couche** du **modèle OSI**, responsable de fournir un **transfert de données fiable** entre des nœuds directement connectés. Elle assure que les trames (paquets de données à cette couche) sont correctement formatées, transmises et reçues.

### **Responsabilités Clés :**
- **Encadrement (Framing)** – Encapsule les données en trames pour la transmission.
- **Détection et Correction d'Erreurs** – Identifie et corrige les erreurs de transmission.
- **Contrôle de Flux** – Assure que l'émetteur ne submerge pas le récepteur.
- **Contrôle d'Accès au Support (MAC)** – Détermine comment plusieurs appareils partagent le support de transmission.
- **Techniques de Commutation** – Gère le déplacement des données à travers les réseaux.

---

## **2. Encadrement (Framing)**
L'encadrement consiste à diviser un flux continu de données en unités plus petites, appelées **trames**, qui incluent des informations de synchronisation.

### **Types de Méthodes d'Encadrement :**
1. **Méthode du Comptage de Caractères** – Le premier champ de la trame spécifie le nombre de caractères.
2. **Encadrement basé sur des Drapeaux (Bit Stuffing)** – Utilise des bits drapeaux spéciaux (par exemple, `01111110` dans HDLC) pour marquer le début et la fin.
3. **Encadrement basé sur des Caractères (Byte Stuffing)** – Utilise des séquences d'échappement pour différencier les caractères de contrôle des données.

---

## **3. Détection et Correction d'Erreurs**
La gestion des erreurs garantit que la transmission des données est précise.

### **Techniques de Détection d'Erreurs :**
- **Bits de Parité** – Une méthode simple ajoutant un bit supplémentaire pour la détection d'erreurs.
- **Contrôle de Redondance Cyclique (CRC)** – Utilise une division polynomiale pour détecter les erreurs.
- **Somme de Contrôle (Checksum)** – Une valeur mathématique calculée à partir des données pour vérifier leur exactitude.

### **Techniques de Correction d'Erreurs :**
- **Correction d'Erreurs Prospectives (FEC)** – Utilise des données redondantes pour corriger les erreurs sans retransmission.
- **Demande de Répétition Automatique (ARQ)** – Utilise des accusés de réception et des retransmissions.
  - **ARQ Stop-and-Wait** – Attend un accusé de réception avant d'envoyer la trame suivante.
  - **ARQ Go-Back-N** – Envoie plusieurs trames mais retransmet à partir de la première erreur.
  - **ARQ Selective Repeat** – Retransmet uniquement les trames erronées.

---

## **4. Contrôle de Flux**
Le contrôle de flux empêche l'émetteur de submerger le récepteur.

### **Méthodes de Contrôle de Flux :**
- **Stop-and-Wait** – L'émetteur attend un accusé de réception avant d'envoyer la trame suivante.
- **Protocole de Fenêtre Glissante** – L'émetteur peut envoyer plusieurs trames avant d'avoir besoin d'un accusé de réception.

---

## **5. Protocoles de la Couche de Liaison de Données**

### **5.1 Ethernet (IEEE 802.3)**
**Ethernet** est une technologie LAN largement utilisée basée sur la **norme IEEE 802.3**.

#### **Structure de Trame Ethernet :**

| Champ | Description |
|--------|------------|
| Préambule | Synchronisation |
| Adresse de Destination | Adresse MAC du récepteur |
| Adresse Source | Adresse MAC de l'émetteur |
| Type/Longueur | Identifie le type de protocole (IPv4, IPv6, etc.) |
| Données | Charge utile réelle |
| CRC | Valeur de contrôle d'erreur |

#### **Modes de Transmission Ethernet :**
- **Half-duplex** – Les appareils transmettent des données à tour de rôle.
- **Full-duplex** – Les appareils peuvent envoyer et recevoir des données simultanément.

---

### **5.2 Point-to-Point Protocol (PPP)**
PPP est utilisé dans les **connexions dial-up et haut débit**.

#### **Caractéristiques du PPP :**
- **Supporte l'authentification** (par exemple, PAP, CHAP).
- **Support multiprotocole** (par exemple, IPv4, IPv6).
- **Détection d'erreurs** via CRC.

#### **Structure de Trame PPP :**

| Champ | Description |
|--------|------------|
| Drapeau (Flag) | Marque le début et la fin de la trame |
| Adresse | Généralement `0xFF` (Broadcast) |
| Contrôle | Généralement `0x03` (Information Non Numérotée) |
| Protocole | Indique le protocole utilisé (IPv4, IPv6, etc.) |
| Données | Charge utile de données réelle |
| CRC | Contrôle d'erreur |

---

## **6. Méthodes de Contrôle d'Accès au Support (MAC)**

### **6.1 Carrier Sense Multiple Access with Collision Detection (CSMA/CD)**
- Utilisé dans les **réseaux Ethernet filaires**.
- Les appareils vérifient si le support est libre avant de transmettre.
- **Si une collision se produit**, les appareils arrêtent de transmettre et réessayent après un délai aléatoire.

### **6.2 Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA)**
- Utilisé dans les **réseaux sans fil (Wi-Fi)**.
- Les appareils tentent d'éviter les collisions en attendant avant d'envoyer des données.
- Utilise les mécanismes **Request-to-Send (RTS) et Clear-to-Send (CTS)**.

---

## **7. Techniques de Commutation**
La commutation détermine comment les données sont acheminées dans un réseau.

### **7.1 Commutation de Circuit**
- Un chemin de communication **dédié** est établi (par exemple, réseaux téléphoniques).
- **Avantages** : Transfert de données fiable et continu.
- **Inconvénients** : Inefficace pour un transfert de données intermittent.

### **7.2 Commutation de Paquets**
- Les données sont **divisées en paquets** et envoyées indépendamment.
- Utilisée dans les **réseaux IP** (par exemple, Internet).
- **Avantages** : Efficace, supporte de multiples utilisateurs.
- **Inconvénients** : Les paquets peuvent arriver dans le désordre.

### **7.3 Commutation de Message**
- Des messages entiers sont stockés et acheminés.
- **Avantage** : Aucun besoin d'une connexion dédiée.
- **Inconvénient** : Plus lent que la commutation de paquets.

---

## **8. Introduction aux Technologies LAN**
Les technologies LAN (Réseau Local) définissent comment les appareils communiquent dans un réseau local.

### **Types de Technologies LAN :**
1. **Ethernet (IEEE 802.3)** – Utilise CSMA/CD, supporte des débits de 10 Mbps à 100 Gbps.
2. **Wi-Fi (IEEE 802.11)** – Utilise CSMA/CA, transmission sans fil.
3. **Token Ring (IEEE 802.5)** – Utilise une méthode de passage de jeton pour contrôler l'accès.
4. **FDDI (Fiber Distributed Data Interface)** – Utilise des câbles à fibres optiques pour la mise en réseau haut débit.

---

## **9. Résumé**
- La **Couche de Liaison de Données** assure une **transmission fiable** entre des appareils directement connectés.
- **L'encadrement (Framing)** organise les données en unités gérables.
- **La détection et correction d'erreurs** maintiennent l'intégrité des données.
- **Le contrôle de flux** empêche la surcharge de données.
- **Ethernet et PPP** sont les principaux protocoles de la Couche de Liaison de Données.
- **CSMA/CD et CSMA/CA** gèrent l'accès au support.
- **Les techniques de commutation** déterminent les méthodes d'acheminement des données.
- **Les technologies LAN** incluent Ethernet, Wi-Fi, Token Ring et FDDI.

---

## **10. Questions de Pratique**
1. Quelle est la fonction principale de la Couche de Liaison de Données dans le modèle OSI ?
2. Comparez CSMA/CD et CSMA/CA.
3. Expliquez la différence entre la commutation de circuit et la commutation de paquets.
4. Quelles sont les différences clés entre Ethernet et PPP ?
5. Comment fonctionne la détection d'erreurs utilisant le CRC ?

---

Ce tutoriel fournit une base solide pour maîtriser la **Couche de Liaison de Données** dans votre cours **Technologie des Réseaux Informatiques (02141)**. Si vous avez besoin d'explications supplémentaires, de questions pratiques ou d'exemples concrets, n'hésitez pas à demander ! 🚀