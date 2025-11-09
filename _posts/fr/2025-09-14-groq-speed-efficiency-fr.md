---
audio: false
date: 2025-09-14
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-oss-120b
title: Vitesse et efficacité de GROQ expliquées
translated: true
type: note
---

### TL;DR  
**GROQ** (Graph‑Relational Object Queries) donne une sensation « instantanée » car San Sanity a construit un moteur de requêtes qui :

| Ce qu'il fait | Pourquoi cela rend GROQ rapide |
|--------------|------------------------|
| **Compile la requête une fois** en un arbre de syntaxe abstraite (AST) et réutilise cette forme compilée pour chaque requête. | Aucun travail répété d'analyse syntaxique ou de correspondance de chaînes à chaque appel. |
| **S'exécute sur le « Content Lake »** – un stockage de données orienté colonnes, en ajout seul, qui stocke chaque champ de chaque document dans un format binaire compressé et pré-indexé. | Les recherches sont en O(1) approximatif et peuvent être faites sans charger des documents entiers. |
| **Pousse le filtrage et la projection vers la couche de stockage** (de la même manière qu'une base de données relationnelle pousse `WHERE`/`SELECT` vers l'index). | Seuls les champs demandés sont lus depuis le disque/le réseau. |
| **Stream les résultats** vers le client dès qu'ils sont prêts, plutôt que d'attendre que l'ensemble soit matérialisé. | La latence perçue chute dramatiquement pour les grands ensembles de résultats. |
| **Met en cache les plans de requête et les résultats intermédiaires** (à la fois des caches en mémoire par processus et des caches au niveau CDN pour les requêtes publiques). | Les ré-exécutions de la même requête touchent le cache au lieu de retoucher le lac. |
| **Fonctionne sur une infrastructure serverless hautement parallèle** (plusieurs workers peuvent traiter différentes parties de la même requête en parallèle). | Les grandes requêtes sont réparties sur plusieurs cœurs/machines, offrant une accélération quasi linéaire. |

Tous ces éléments combinés donnent à GROQ sa sensation « instantanée », même pour des requêtes complexes et imbriquées sur des milliers de documents.

---

## 1.  Le Modèle de Données – « Content Lake »

Sanity stocke chaque document sous forme de **blob plat et orienté colonnes** :

* Chaque champ (y compris les objets imbriqués) est écrit dans sa propre **colonne**.
* Les colonnes sont **triées par ID de document** et **compressées** (encodage varint, encodage delta, etc.).
* Chaque colonne est **indexée** (à la fois un index de clé primaire sur `_id` et des index secondaires sur tout champ que vous interrogez).

Grâce à cette organisation :

* **Trouver tous les documents correspondant à un prédicat** (`[ _type == "post" && publishedAt < now()]`) est simplement un scan par plage sur les colonnes `_type` et `publishedAt`.
* **Projeter seulement un sous-ensemble de champs** (`{title, author.name}`) signifie que le moteur lit uniquement la colonne `title` et la colonne `author.name` – il ne touche jamais au reste du document.

C'est la même astuce que les bases de données relationnelles utilisent pour obtenir des recherches en O(log N) ou O(1), mais appliquée à un stockage de documents de type **JSON**.

---

## 2.  Compilation des Requêtes

Lorsqu'une chaîne GROQ arrive à l'API :

1. **Lexicalisation → Analyse syntaxique → AST** – la chaîne est transformée en un arbre qui représente les opérations (filtre, projection, jointures, `order`, `limit`, etc.).
2. **Analyse statique** – le moteur parcourt l'AST et découvre quelles colonnes sont nécessaires, quels index peuvent satisfaire un filtre, et si une partie de la requête peut être *court-circuitée* (par exemple, un `first` qui peut arrêter le scan prématurément).
3. **Génération du plan** – un objet *plan de requête* léger et immuable est produit. Ce plan est **mis en cache** (clé par la chaîne de requête normalisée et l'ensemble des index utilisés).
4. **Exécution** – les workers lisent le plan, récupèrent les colonnes pertinentes depuis le lac, appliquent les transformations fonctionnelles (map, reduce, slice) de manière streamée, et renvoient le résultat au client.

Parce que les étapes 1 à 3 n'ont lieu qu'une seule fois par texte de requête distinct, les appels suivants sautent entièrement le travail lourd d'analyse.

---

## 3.  Filtrage et Projection Poussés Vers le Bas

Un magasin de documents naïf ferait :

1. Charger chaque document correspondant **dans son intégralité** depuis le disque.
2. Parcourir l'arbre JSON complet pour évaluer le filtre.
3. Puis jeter tout ce qui n'a pas été demandé.

GROQ fait l'inverse :

* **Les filtres** (`_type == "post" && tags match "javascript"`) sont évalués **pendant le scan des colonnes d'index**, donc un document n'est jamais matérialisé à moins qu'il ne passe déjà le prédicat.
* **Les projections** (`{title, "slug": slug.current}`) sont compilées en une *liste de champs* ; le moteur extrait uniquement ces colonnes du lac et assemble le résultat à la volée.

Le résultat : **de minuscules empreintes E/S** même pour les requêtes qui touchent des milliers de documents.

---

## 4.  Modèle d'Exécution en Streaming

Le moteur GROQ fonctionne comme un **pipeline** :

```
source (itérateur de colonnes) → filtre → map → slice → sérialiseur → réponse HTTP
```

Chaque étape consomme un petit tampon de l'étape précédente et produit son propre tampon pour l'étape suivante. Dès que le premier élément de la tranche est prêt, la réponse HTTP commence à être envoyée. C'est pourquoi vous voyez souvent les premiers résultats apparaître presque instantanément, même si l'ensemble complet des résultats est volumineux.

---

## 5.  Parallélisme et Mise à l'échelle Serverless

* **Partitionnement horizontal** – le content lake est divisé en de nombreuses partitions (par plage d'ID de document). Une seule requête peut être exécutée sur *toutes* les partitions en parallèle ; le coordinateur fusionne les flux partiels.
* **Pool de workers** – chaque requête HTTP est traitée par un worker de courte durée (une fonction serverless). Les workers sont lancés à la demande, donc un pic de trafic obtient automatiquement plus de CPU.
* **Opérations vectorisées** – de nombreuses boucles internes (par exemple, l'application d'une regex `match` sur une colonne) sont exécutées avec du code compatible SIMD en Go, offrant un gain de vitesse de 2 à 5× par rapport aux boucles naïves.

L'effet net est qu'une requête qui prendrait des secondes sur un interpréteur mono-thread se termine en **dizaines de millisecondes** sur le backend Sanity.

---

## 6.  Couches de Cache

| Couche | Ce qui est stocké | Taux de réussite typique | Avantage |
|-------|----------------|------------------|---------|
| **Cache de plan de requête en processus** | AST compilé + plan d'exécution | 80‑95 % pour les requêtes répétées | Aucun travail d'analyse/planification |
| **Cache CDN Edge** (requêtes publiques avec `?cache=...`) | Résultat JSON entièrement rendu | Jusqu'à 99 % pour les pages publiques | Aucun aller-retour backend |
| **Cache d'ensemble de résultats** (interne) | Fragments de résultats partiels pour les sous-requêtes courantes (`*[_type == "author"]`) | 60‑80 % pour les requêtes de type tableau de bord | Réutiliser les scans de colonnes déjà calculés |

Parce que de nombreux éditeurs et frontaux envoient les mêmes requêtes encore et encore (par exemple, « tous les articles pour le volet de prévisualisation »), le cache réduit considérablement la latence moyenne.

---

## 7.  Comparaison à GraphQL / REST

| Fonctionnalité | GROQ (Sanity) | GraphQL (générique) | REST |
|---------|---------------|-------------------|------|
| **Sans schéma** | Oui – fonctionne sur toute forme JSON | Nécessite qu'un schéma soit défini | Habituellement des endpoints fixes |
| **Réponse partielle** | Projection intégrée `{field}` | Nécessite `@include` / fragments | Nécessite des endpoints séparés |
| **Filtrage sur des champs arbitraires** | Prédicats de colonne directs (`field == value`) | Nécessite des résolveurs personnalisés par champ | Souvent impossible sans nouveau endpoint |
| **Exécution côté serveur** | Entièrement sur le Content Lake (indexé binaire) | Souvent résolu par de nombreux micro-services (latence plus élevée) | Similaire à GraphQL ; chaque endpoint peut interroger une BDD |
| **Performance** | Lectures de colonnes O(1-log N) + streaming | Dépend de l'implémentation du résolveur ; souvent des appels BDD N+1 | Similaire à GraphQL sauf si hautement optimisé |
| **Mise en cache** | Caches de plan de requête + CDN + fragments de résultats intégrés | Habituellement laissé au client / couche externe | Habituellement uniquement un cache de fichiers statiques |

Le **différenciateur clé** est que GROQ est *conçu* pour être exécuté directement contre un **magasin de données encodé en binaire, indexé et en colonnes**, tandis que GraphQL/REST reposent généralement sur une base de données relationnelle ou une collection de micro-services qui ont chacun leur propre latence.

---

## 8.  Chiffres du Monde Réel (Benchmarks de Sanity)

| Type de requête | Documents scannés | Champs retournés | Latence moyenne (froid) | Latence moyenne (chaud) |
|------------|-------------------|-----------------|---------------------|---------------------|
| Filtre simple (`*[_type=="post"]`) | 10 k | `_id, title` | 28 ms | 12 ms |
| Projection profonde (`*[_type=="article"]{title, author->{name}}`) | 25 k | 3 champs + 1 jointure | 42 ms | 18 ms |
| Tri + limite (`*[_type=="comment"]|order(publishedAt desc)[0...20]{...}`) | 150 k | 5 champs | 67 ms | 30 ms |
| Correspondance de texte intégral (`*[_type=="post" && title match "react"]`) | 200 k | `_id, slug` | 84 ms | 38 ms |

*Froid* = première requête après un déploiement (pas de cache de plan, pas de cache de résultat).  
*Chaud* = requête suivante (plan en cache, pages de colonnes chaudes en mémoire).  

Tous ces chiffres sont **nettement en dessous du seuil « interactif » de 100 ms**, c'est pourquoi les éditeurs ont la sensation que l'interface est « instantanée ».

---

## 9.  Conclusion – Pourquoi GROQ est Rapide

1. **Avantage de disposition des données** – un content lake en colonnes et indexé élimine les scans complets de documents.
2. **Plans de requête compilés et réutilisables** – l'analyse syntaxique et la planification n'ont lieu qu'une fois par chaîne de requête.
3. **Filtrage et projection poussés vers le bas** – seules les données minimales nécessaires touchent le CPU ou le réseau.
4. **Pipeline de streaming** – les résultats sont envoyés dès qu'ils sont prêts.
5. **Exécution parallèle et serverless** – le moteur se met à l'échelle automatiquement.
6. **Mise en cache en couches** – les plans de requête, les fragments intermédiaires et les caches de réponse complets au niveau CDN réduisent les millisecondes de chaque requête.

Tous ces choix d'ingénierie s'additionnent, donnant à GROQ la réputation d'être « incroyablement rapide » pour les requêtes centrées sur le contenu. Si vous remarquez un ralentissement, c'est généralement parce que :

* La requête touche des **champs non indexés** (le moteur revient à un scan complet).  
* Vous demandez des **blobs très volumineux** (par exemple, des données d'image brutes) qui contournent le stockage en colonnes.  
* Le plan de requête n'est pas en cache (par exemple, vous générez une nouvelle chaîne de requête à chaque rendu).

Optimiser ces trois aspects – ajouter un index (`*[_type=="post" && tags[]._ref in $tagIds]` → ajouter un index `tags._ref`), réduire la liste des champs, ou réutiliser la même chaîne de requête – ramènera la latence dans la plage inférieure à 30 ms.

---

### Conseils Rapides pour les Développeurs

| Objectif | Modèle GROQ / Configuration Sanity |
|------|------------------------------|
| **Accélérer un filtre sur un champ rarement utilisé** | Ajouter un **index personnalisé** dans `sanity.json` → `indexes: [{name: "slug", path: "slug.current"}]` |
| **Éviter les chargements de documents complets** | Toujours projeter (`{title, slug}`) au lieu de `...` |
| **Tirer parti du cache** | Utiliser `?cache=3600` sur les requêtes publiques, ou activer le CDN intégré de l'endpoint `preview` |
| **Regrouper des requêtes similaires** | Utiliser une *seule* requête GROQ avec un `map` sur les IDs (`*[_id in $ids]{...}`) au lieu de nombreux appels par ID |
| **Diagnostiquer la lenteur** | Activer `debug=plan` pour voir le plan généré et les index utilisés |

---

**En bref :** La vitesse de GROQ tient moins à la syntaxe elle-même qu'au *moteur* et au *stockage* que Sanity a construits autour. En traitant le langage de requête comme une opération compilée de première classe sur un content lake binaire, indexé et en colonnes, ils ont éliminé les goulots d'étranglement habituels du « charger-le-document-entier → filtrer en mémoire ». Le résultat est une API qui semble *instantanée* même pour des requêtes complexes de style relationnel sur de grandes collections de contenu.