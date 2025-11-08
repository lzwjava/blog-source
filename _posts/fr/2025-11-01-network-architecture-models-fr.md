---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Étude des architectures et modèles de réseau
translated: true
type: note
---

Ce chapitre jette les bases pour comprendre comment les réseaux informatiques sont structurés et comment les données y sont transmises. Dans le contexte du cours *Technologie des Réseaux Informatiques* (code 自考 02141 ou similaire), il met l'accent sur les modèles théoriques comme OSI et TCP/IP, qui sont au cœur des questions d'examen sur l'empilement en couches, les protocoles et le flux de données. Concentrez-vous sur la mémorisation des noms des couches, de leurs fonctions et des correspondances entre les modèles. Attendez-vous à des questions à choix multiples, à réponses courtes ou basées sur des diagrammes testant les comparaisons et les responsabilités.

## 1. Introduction aux Architectures en Couches
Les réseaux utilisent des **architectures en couches** pour simplifier la communication complexe en divisant les tâches en couches modulaires. Chaque couche :
- Gère des fonctions spécifiques (ex : contrôle d'erreur, routage).
- Interagit uniquement avec les couches adjacentes via des interfaces standardisées.
- Utilise l'**encapsulation** (ajout d'en-têtes/de trailers) lors de l'envoi de données vers le bas de la pile et la **décapsulation** lors de la réception.

**Avantages** :
- Modularité : Facile à développer, tester et mettre à jour individuellement.
- Interopérabilité : Les appareils de différents fabricants peuvent communiquer.
- Évolutivité : Les couches peuvent évoluer indépendamment (ex : nouveaux protocoles de transport).

**Responsabilités** (générales pour tous les modèles) :
- **Couches basses** : Se concentrent sur le matériel et le transfert fiable des données (transmission physique, détection d'erreurs).
- **Couches hautes** : Gèrent les tâches orientées utilisateur (ex : transfert de fichiers, navigation web).
- Les données circulent **vers le bas** dans la pile de l'émetteur (encapsulation) et **vers le haut** dans la pile du récepteur (décapsulation).

## 2. Modèle de Référence OSI
Le modèle **Open Systems Interconnection (OSI)** est un cadre conceptuel à 7 couches développé par l'ISO en 1984. Il est théorique, non implémenté directement, mais utilisé comme standard pour comprendre les protocoles. Mnémotechnique : **Please Do Not Throw Sausage Pizza Away** (Physique → Application).

| Numéro Couche | Nom Couche       | Fonctions et Protocoles Clés | PDU (Unité de Données de Protocole) | Appareils/Exemples |
|--------------|------------------|-----------------------------|--------------------------|------------------|
| 7           | Application     | Fournit des services réseau aux applications utilisateur (ex : email, transfert de fichiers). Interface avec le logiciel. | Data | HTTP, FTP, SMTP ; Navigateur web |
| 6           | Présentation    | Traduit les formats de données (ex : chiffrement, compression, ASCII vers EBCDIC). Assure la compatibilité syntaxique. | Data | JPEG, SSL/TLS |
| 5           | Session         | Gère les sessions/connexions (ex : établissement, synchronisation, contrôle du dialogue). Gère les points de contrôle pour la reprise. | Data | NetBIOS, RPC |
| 4           | Transport       | Livraison fiable de bout en bout (ex : segmentation, contrôle de flux, reprise sur erreur). | Segment (TCP) / Datagramme (UDP) | TCP, UDP ; Ports (ex : 80 pour HTTP) |
| 3           | Réseau         | Adressage logique et routage (ex : détermination du chemin à travers les réseaux). Gère la congestion. | Paquet | IP, ICMP, OSPF ; Routeurs |
| 2           | Liaison de Données       | Livraison de nœud à nœud sur le même réseau (ex : encapsulation en trames, détection d'erreur via CRC, adressage MAC). | Trame | Ethernet, PPP ; Commutateurs, Cartes réseau |
| 1           | Physique        | Transmission de bits sur support physique (ex : signalisation, câblage, topologie). Traite des spécifications matérielles. | Bit | RJ-45, Fibre optique ; Concentrateurs, Câbles |

**Points Clés** :
- Couches 1-2 : Axées sur le support (LAN/WAN).
- Couches 3-4 : Hôte à hôte (interconnexion de réseaux).
- Couches 5-7 : Orientées utilisateur (support applicatif).
- Astuce Examen : Dessinez la pile et étiquetez les PDU/en-têtes (ex : un segment TCP a un en-tête TCP + données).

## 3. Suite de Protocoles TCP/IP
Le **modèle TCP/IP** (ou Internet Protocol Suite) est un modèle pratique à 4 couches développé dans les années 1970 pour l'ARPANET (base d'Internet). Il est implémenté mondialement et correspond approximativement au modèle OSI. Mnémotechnique : **LITA** (Liaison → Application).

| Numéro Couche | Nom Couche       | Fonctions et Protocoles Clés | PDU                  | Appareils/Exemples |
|--------------|------------------|-----------------------------|----------------------|------------------|
| 4           | Application     | Combine les couches OSI 5-7 : Services utilisateur (ex : web, email). | Data/Segment | HTTP, FTP, DNS ; Applications comme les navigateurs |
| 3           | Transport       | Bout en bout (Couche OSI 4) : Livraison fiable/non fiable. | Segment/Datagramme | TCP (fiable, orienté connexion), UDP (meilleur effort) |
| 2           | Internet        | Routage et adressage (Couche OSI 3) : Chemins logiques à travers les réseaux. | Paquet | IP (IPv4/IPv6), ICMP ; Routeurs |
| 1           | Liaison (ou Accès Réseau) | Physique + Liaison de données (Couches OSI 1-2) : Livraison matérielle sur le réseau local. | Trame/Bit | Ethernet, Wi-Fi ; Commutateurs, Câbles |

**Points Clés** :
- Pas de couches session/présentation dédiées ; gérées au sein de la couche Application.
- TCP/IP est une "famille de protocoles" – ex : IP est le cœur, avec TCP/UDP au-dessus.
- Astuce Examen : Insistez sur l'usage réel (ex : TCP assure la fiabilité via des accusés de réception, tandis qu'UDP est léger pour la diffusion vidéo).

## 4. Comparaison des Modèles OSI et TCP/IP
Utilisez ce tableau pour une révision rapide. OSI est théorique (référence), TCP/IP est pratique (implémentation).

| Aspect              | Modèle OSI                          | Modèle TCP/IP                       |
|---------------------|------------------------------------|------------------------------------|
| **Couches**         | 7 (détaillé, conceptuel)          | 4 (simplifié, pratique)         |
| **Développement**    | ISO (1984), conception descendante       | DoD/Internet (années 1970), conception ascendante   |
| **Focus**          | Standards généraux de réseau      | Protocoles spécifiques à Internet       |
| **Implémentation** | Non implémenté directement ; référence pour les standards | Large utilisation (base d'Internet moderne) |
| **Correspondance des Couches**  | 1: Physique → Liaison<br>2: Liaison de données → Liaison<br>3: Réseau → Internet<br>4: Transport → Transport<br>5-6-7: Session/Présentation/Application → Application | Application absorbe OSI 5-7 ; Liaison absorbe 1-2 |
| **Protocoles**      | Théoriques (ex : pas de protocole IP unique)  | Spécifiques (ex : IP, TCP, HTTP)    |
| **Flux PDU**       | En-têtes stricts par couche          | Flexible (ex : le paquet IP inclut les données de transport) |
| **Points Forts**      | Complet, facile à enseigner      | Efficace, évolutif, neutre vis-à-vis des fournisseurs |
| **Points Faibles**     | Trop complexe, pas pratique     | Moins détaillé pour les couches hautes    |

**Différences Clés** :
- **Granularité** : OSI sépare session/présentation ; TCP/IP les fusionne dans Application pour plus de simplicité.
- **Adressage** : OSI utilise des points d'accès au service (SAP) ; TCP/IP utilise des ports/adresses IP.
- **Fiabilité** : Les deux ont une fiabilité au niveau transport, mais le TCP de TCP/IP est orienté connexion comme la couche Transport d'OSI.
- Astuce Examen : Les questions portent souvent sur les correspondances (ex : "Quelle couche OSI correspond à TCP ?") ou les avantages (ex : L'adaptabilité de TCP/IP a conduit à la croissance d'Internet).

## 5. Fonctions et Responsabilités de l'Architecture en Couches
**Principes Fondamentaux** :
- **Abstraction** : Chaque couche masque les détails des couches inférieures (ex : la couche Transport ne se soucie pas des câbles physiques).
- **Primitives de Service** : Les couches fournissent des services comme CONNECT, DATA, DISCONNECT aux couches supérieures.
- **Gestion des Erreurs** : Les couches basses détectent les erreurs ; les couches hautes les corrigent (ex : la couche Transport retransmet les paquets perdus).
- **Adressage** : Hiérarchique – physique (MAC), logique (IP), service (ports).

**Exemple de Transmission de Données** :
1. Données Application → Transport ajoute un en-tête de segment (ports, numéro de séq.) → Réseau ajoute un en-tête de paquet (adresses IP) → Liaison ajoute un en-tête/trailer de trame (MAC) → Physique envoie les bits.
2. Processus inverse au récepteur.

**Pièges Courants** :
- Ne confondez pas les couches : Physique concerne les bits/signaux ; Liaison de données concerne les trames/trames sans erreur.
- La couche Liaison de TCP/IP = Couches OSI 1+2 combinées.

## Conseils d'Étude pour l'Examen 自考
- **Mémorisation** : Utilisez des moyens mnémotechniques et dessinez des diagrammes en couches quotidiennement. Concentrez-vous sur les 80% de poids de l'examen portant sur les descriptions OSI/TCP/IP.
- **Pratique** :
  - Comparez les couches dans des dissertations (200-300 mots).
  - QCM : "Quelle couche gère le routage ? (A) Réseau".
  - Diagrammes : Étiquetez un parcours de PDU.
- **Ressources** : Revoyez les figures du manuel pour l'encapsulation. Chronométrez-vous : 30 min pour le tableau de comparaison.
- **Questions Courantes** : Expliquez pourquoi OSI a 7 couches contre 4 pour TCP/IP ; Décrivez les devoirs de la couche Transport.

Maîtrisez ce chapitre pour un bon départ – il est référencé dans les sujets suivants comme les protocoles (ex : IP dans le Chapitre 3). Ensuite, abordez les détails de la couche physique.

**Références**:
- [Computer Networking: A Top-Down Approach by Kurose & Ross](https://www.pearson.com/us/higher-education/program/Kurose-Computer-Networking-A-Top-Down-Approach-8th-Edition/PGM1836378.html) (pour approfondir TCP/IP).
- [OSI Model Explained - GeeksforGeeks](https://www.geeksforgeeks.org/open-systems-interconnection-model-osi/) (aides visuelles).