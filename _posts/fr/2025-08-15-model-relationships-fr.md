---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Relationships de modèle, pas de données
translated: true
type: note
---

Vous avez absolument raison — les relations « un-à-un, un-à-plusieurs, plusieurs-à-plusieurs » sont partout : les familles, les équipes, les paiements ; les classes, les repos, les pull requests. Voici un guide compact pour **définir les relations** afin que les conceptions restent simples et correspondent à l'usage réel.

# Un guide pratique de modélisation

## 1) Partez du comportement, pas des données

* Écrivez les **5 tâches utilisateur principales** (« passer commande », « approuver une dépense », « assigner un relecteur »).
* Sous chaque tâche, listez les **noms** (entités) et les **verbes** (relations/actions).
* Ne gardez que les relations qui **changent le résultat** de ces tâches ; tout le reste est des métadonnées.

## 2) Déterminez d'abord la propriété et les limites

* Demandez : *Qui possède le cycle de vie de qui ?*
  * Si A ne peut pas exister sans B → A fait **partie de** B (composition).
  * Si A et B vivent indépendamment → relation de **référence**.
* Utilisez les **contextes limités** : le même « Client » peut être différent dans la Facturation vs le Marketing. N'imposez pas un méga-modèle unique.

## 3) Choisissez la **cardinalité la plus simple** qui fonctionne

* Préférez **1→1** seulement lorsque deux enregistrements sont opérationnement inséparables mais nécessitent une sécurité ou une volatilité différente (ex: Utilisateur ↔ Identifiants).
* Préférez **1→N** lorsqu'il y a une propriété claire et un accès fréquent du parent vers les enfants (Commande → Articles).
* Utilisez **M↔N** seulement lorsque les deux côtés sont pairs et que la liaison est un concept métier à part entière (Étudiant ↔ Cours via « Inscription » qui a une note, un statut, des dates).

## 4) Rendez les relations explicites avec des invariants

Pour chaque relation, écrivez les invariants en langage clair :
* **Cardinalité** : « Un utilisateur a au plus un email principal. »
* **Optionalité** : « Une facture doit avoir ≥1 article. »
* **Temporel** : « L'adhésion est valide pendant [début, fin). »
* **Unicité** : « Un code produit est unique par tenant. »
  Ceux-ci se convertissent directement en contraintes, index et vérifications.

## 5) Modèles par cardinalité (sans tables 😉)

### Un-à-un

* À utiliser pour séparer les champs volatiles/sécurisés ou lorsqu'une entité évolue de manière modulaire.
* Appliquez avec une clé unique sur la clé étrangère.
* Envisagez l'**intégration** (documents) si c'est toujours lu ensemble.

### Un-à-plusieurs

* Si les enfants ne changent jamais de parent → gardez la **clé parent** sur l'enfant ; cascade des suppressions comme politique.
* Si le re-parentage existe → autorisez une FK nullable + une règle métier pour les transitions.
* Si les lectures sont centrées sur le parent → dénormalisez les champs de résumé sur le parent (décomptes, dernière_mise_à_jour).

### Plusieurs-à-plusieurs

* Promouvez le lien en une **entité de premier ordre** (Inscription, Adhésion, Assignment).
* Placez les **données métier** sur le lien (rôle, priorité, poids, horodatages).
* Si le lien n'a pas d'attributs et est volumineux, choisissez le stockage et les index pour les requêtes du côté le plus lourd.

## 6) Choisissez le stockage selon les modes d'accès

* **Relationnel** : intégrité la plus forte, jointures complexes, reporting.
* **Document** : agrégat en premier, flux de lecture centrés sur le parent, mises à jour localisées.
* **Graphe** : requêtes de chemin, recommandations, héritage de permissions, traversées à profondeur variable.
  Choisissez-en un **par contexte limité** ; synchronisez via des événements, pas des tables partagées.

## 7) La surface API reflète les relations—intentionnellement

* Les **agrégats** deviennent les ressources API principales.
* Les **collections enfants** comme routes imbriquées (ex: `/orders/{id}/items`).
* Les **entités de jointure** obtiennent leur propre ressource quand elles sont importantes (`/enrollments`).
* Pour la flexibilité du client, exposez **GraphQL** seulement lorsque le domaine est de type graphe ou que les clients varient beaucoup ; sinon, gardez REST simple.

## 8) Gardez-le évolutif (temporel + changement progressif)

* Tracez le **temps de validité** sur les liens importants (`valid_from`, `valid_to`), pas seulement `updated_at`.
* Préférez les **suppressions logiques** sur les lignes de relation pour pouvoir reconstruire l'historique.
* Utilisez des **IDs substituts** pour toutes les entités et lignes de lien ; n'incorporez jamais de sens dans les IDs.

## 9) Simplifiez agressivement

* Fusionnez les entités si les utilisateurs ne perçoivent jamais la différence.
* Réunifiez les séparations 1→1 lorsque les raisons de sécurité/performance disparaissent.
* Remplacez les toiles M↔N larges par une **hiérarchie** si les règles métier sont véritablement arborescentes.
* Introduisez des **rôles** au lieu de multiples types de liens (ex: une seule Adhésion avec rôle=propriétaire/spectateur au lieu de liens séparés).

## 10) Recherche inverse (réingénierie) d'un enchevêtrement existant

* Cartographiez les **requêtes réelles** (logs lents, tableaux de bord). Ne gardez que les relations utilisées par ≥1 requête critique.
* Dessinez une **carte des contextes** : quelle équipe/système possède quelles entités et qui consomme quels événements.
* Identifiez les **jointures chaudes** → soit dénormalisez, mettez en cache, ou transformez en agrégats.
* Élevez les liens M↔N bruyants en **concepts de premier ordre** avec des invariants clairs.
* Ajoutez des **contrats** : contraintes, tests et linters pour le schéma et l'API pour éviter la dérive.

# Pièges courants à éviter

* Traiter M↔N comme « juste une table de jointure » alors que c'est le cœur métier (ex: permissions, allocations).
* Sur-normaliser les chemins de lecture nécessitant une faible latence ; corrigez avec des **modèles de lecture** (CQRS) ou des vues matérialisées.
* Sous-spécifier l'optionalité — `NULL` explose la complexité. Préférez des états explicites « Inconnu/NonApplicable » quand c'est significatif.
* Ignorer la **multi-location** : limitez toujours l'unicité et les requêtes par tenant dès le début.
* Oublier la **directionnalité** : « suit » vs « amis » n'est pas la même chose.

# Une checklist légère que vous pouvez réutiliser

* Quelles sont les tâches principales et leurs métriques de succès ?
* Quels sont les agrégats (propriété/cycle de vie) ?
* Quels sont les invariants (cardinalité, optionalité, temporel, unicité) ?
* Quelles relations portent des attributs métier (à promouvoir en entités) ?
* Quels modes d'accès dominent (choisir le stockage/les index en conséquence) ?
* Quelles simplifications sont sûres aujourd'hui (fusionner/séparer/dénormaliser) ?
* Quels contrats appliquent cela (contraintes, tests d'API, schémas d'événements) ?

Si vous voulez, donnez-moi un petit extrait de votre domaine (trois entités + la tâche utilisateur principale), et j'esquisserai les relations, les invariants et une forme de stockage/API que vous pourrez implémenter directement.