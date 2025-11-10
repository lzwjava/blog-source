---
audio: false
generated: true
lang: fr
layout: post
title: La technologie de collaboration en temps réel de Google Docs
translated: true
type: note
---

Google Docs utilise un algorithme sophistiqué de **collaboration en temps réel** pour permettre à plusieurs utilisateurs de modifier un document simultanément. La technologie fondamentale derrière ceci est basée sur la **Transformation Opérationnelle (OT)** et a ensuite évolué pour incorporer les **Types de Données Répliqués Sans Conflit (CRDT)** dans certains systèmes. Voici une analyse des composants clés :

### 1. **Transformation Opérationnelle (OT)**
   - **Idée de base** : La TO résout les conflits en transformant (en ajustant) les opérations entrantes par rapport aux opérations précédemment appliquées.
   - **Fonctionnement** :
     1. Lorsqu'un utilisateur effectue une modification (ex : insérer du texte), le client génère une **opération** (ex : `insert("hello", pos=5)`).
     2. L'opération est envoyée au serveur, qui la **transforme** par rapport aux modifications concurrentes des autres utilisateurs pour maintenir la cohérence.
     3. Tous les clients appliquent les opérations d'une manière qui garantit une cohérence à terme.
   - **Exemple** : Si l'Utilisateur A insère "abc" à la position 5 tandis que l'Utilisateur B supprime la position 5, la TO ajuste l'opération de B pour supprimer la position 8 (après l'insertion de A).
   - **Défis** : La TO nécessite un serveur central pour gérer les transformations, ce qui la rend complexe à implémenter correctement.

### 2. **Types de Données Répliqués Sans Conflit (CRDT)**
   - **Idée de base** : Les CRDT permettent aux systèmes distribués de fusionner les modifications sans serveur central en concevant des structures de données qui convergent toujours.
   - **Fonctionnement** :
     1. Les modifications sont étiquetées avec des identifiants uniques (comme des horodatages ou des horloges vectorielles).
     2. Le système fusionne les modifications en utilisant des propriétés mathématiques (ex : opérations commutatives, associatives).
   - **Avantages par rapport à la TO** :
     - Aucun besoin d'un serveur central (fonctionne en pair-à-pair).
     - Plus robuste pour l'édition hors ligne.
   - **Exemple** : Au lieu de suivre les positions par des nombres, les CRDT peuvent utiliser l'indexation fractionnaire (ex : "A" < "A1" < "B") pour éviter les conflits.

### 3. **Implémentation de Google (Hybride Wave/OT)**
   - Google Docs était à l'origine basé sur **l'algorithme TO de Google Wave**, qui étendait la TO classique avec :
     - **Serveur Centralisé** : Garantit que toutes les opérations sont transformées correctement.
     - **Synchronisation Différentielle** : Minimise les données envoyées sur le réseau.
   - Au fil du temps, Google a probablement incorporé **des optimisations de type CRDT** pour une meilleure prise en charge hors ligne.

### 4. **Autres Technologies Clés**
   - **Synchronisation Frontend/Backend** : Utilise **WebSockets/long-polling** pour les mises à jour en temps réel.
   - **Horloges Logiques/Vecteurs de Version** : Traquent la causalité des modifications.
   - **Résolution de Conflits** : Si deux utilisateurs modifient le même texte simultanément, le système résout les conflits via les règles TO/CRDT.

### **Comparaison : TO vs CRDT**

| Caractéristique       | TO (Google Docs Classique) | CRDT (Ex : Figma, Notion) |
|-----------------------|----------------------------|---------------------------|
| Serveur Central Nécessaire | Oui                      | Non (pair-à-pair possible) |
| Support Hors Ligne    | Limité                    | Meilleur                  |
| Complexité            | Élevée (logique de transformation) | Élevée (conception de structure de données) |
| Latence               | Faible (géré par le serveur) | Dépend de l'implémentation |

### **Pourquoi Google Utilise Probablement la TO (avec des Influences CRDT)**
- La TO est bien adaptée aux services **centralisés** comme Google Docs.
- Les CRDT gagnent en popularité dans les applications décentralisées (ex : **Figma, Apple Notes**), mais l'infrastructure de Google est optimisée pour la TO.

### **Pour Approfondir**
- **Article sur la TO** : [Operational Transformation in Real-Time Group Editors](https://dl.acm.org/doi/10.1145/146486.146487) (Cormack et al.)
- **CRDTs** : [A Comprehensive Study of CRDTs](https://arxiv.org/abs/1805.06358)
- **Protocole Google Wave** : [Wave Protocol](https://wave-protocol.google.com/)

Souhaitez-vous approfondir un aspect spécifique ?