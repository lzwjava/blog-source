---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide du langage de requête PromQL
translated: true
type: note
---

PromQL (Prometheus Query Language) est un langage de requête fonctionnel utilisé pour sélectionner et agréger en temps réel les données de séries temporelles dans Prometheus. Il prend en charge les requêtes instantanées (évaluées à un instant unique) et les requêtes par plage (évaluées à plusieurs pas sur une période). Les expressions PromQL peuvent renvoyer l'un des quatre types de données : **vecteur instantané**, **vecteur de plage**, **scalaire** ou **chaîne**.

---

## Introduction

PromQL permet aux utilisateurs de :
- Sélectionner des séries temporelles en utilisant des **sélecteurs de vecteur instantané**.
- Récupérer des données sur une période en utilisant des **sélecteurs de vecteur de plage**.
- Appliquer des **opérateurs** (arithmétiques, de comparaison, logiques, d'agrégation).
- Utiliser des **fonctions** comme `rate()`, `sum()`, `avg()` pour l'analyse.
- Interroger les données via l'**API HTTP**.

Les expressions sont évaluées dans l'interface utilisateur de Prometheus :
- **Onglet Tableau** : Requêtes instantanées.
- **Onglet Graphique** : Requêtes par plage.

---

## Sélecteurs de Séries Temporelles

Les sélecteurs de séries temporelles définissent quelles métriques et quels labels récupérer.

### Sélecteurs de Vecteur Instantané

Sélectionne l'échantillon le plus récent pour chaque série temporelle correspondante.

**Syntaxe** :
```
<metric_name>{<label_matchers>}
```

**Exemples** :
- Toutes les séries temporelles avec la métrique `http_requests_total` :
  ```
  http_requests_total
  ```
- Job et groupe spécifiques :
  ```
  http_requests_total{job="prometheus", group="canary"}
  ```
- Correspondance par regex sur l'environnement et exclusion de la méthode GET :
  ```
  http_requests_total{environment=~"staging|testing|development", method!="GET"}
  ```
- Correspondance sur `__name__` :
  ```
  {__name__=~"job:.*"}
  ```

**Opérateurs de Label** :
- `=` : correspondance exacte
- `!=` : différent de
- `=~` : correspondance regex (ancrée)
- `!~` : pas de correspondance regex

> Note : `{job=~".+"}` est valide ; `{}` seul est invalide.

---

### Sélecteurs de Vecteur de Plage

Sélectionne une plage d'échantillons dans le temps.

**Syntaxe** :
```
<instant_selector>[<duration>]
```

**Exemple** :
- Les 5 dernières minutes de `http_requests_total` pour le job `prometheus` :
  ```
  http_requests_total{job="prometheus"}[5m]
  ```

> La plage est **ouverte à gauche, fermée à droite** : exclut l'heure de début, inclut l'heure de fin.

---

### Modificateur `offset`

Décale le temps d'évaluation vers l'avant ou l'arrière.

**Syntaxe** :
```
<selector> offset <duration>
```

**Exemples** :
- Valeur de `http_requests_total` il y a 5 minutes :
  ```
  http_requests_total offset 5m
  ```
- Taux il y a 1 semaine :
  ```
  rate(http_requests_total[5m] offset 1w)
  ```
- Regarder en avant (offset négatif) :
  ```
  rate(http_requests_total[5m] offset -1w)
  ```

> Doit suivre immédiatement le sélecteur.

---

### Modificateur `@`

Évalue à un horodatage spécifique.

**Syntaxe** :
```
<selector> @ <timestamp>
```

**Exemples** :
- Valeur à l'horodatage Unix `1609746000` :
  ```
  http_requests_total @ 1609746000
  ```
- Taux à un moment spécifique :
  ```
  rate(http_requests_total[5m] @ 1609746000)
  ```
- Utiliser `start()` ou `end()` :
  ```
  http_requests_total @ start()
  rate(http_requests_total[5m] @ end())
  ```

> Peut être combiné avec `offset`.

---

## Taux et Agrégations

PromQL prend en charge les opérateurs de **taux** et d'**agrégation** pour calculer les métriques dans le temps ou entre les séries.

### Fonction `rate`

Calcule le taux d'augmentation moyen par seconde.

**Exemple** :
```
rate(http_requests_total[5m])
```

> Utilisé sur les **vecteurs de plage**.

---

### Opérateurs d'Agrégation

S'appliquent aux vecteurs instantanés pour combiner les séries temporelles.

**Exemples** :
- Somme de tous les `http_requests_total` :
  ```
  sum(http_requests_total)
  ```
- Moyenne par instance :
  ```
  avg by (instance)(http_requests_total)
  ```
- Nombre par job :
  ```
  count by (job)(http_requests_total)
  ```

> L'agrégation nécessite des séries correspondantes ; utilisez les clauses `by` ou `without`.

---

## Opérateurs

PromQL prend en charge plusieurs types d'opérateurs.

### Opérateurs Arithmétiques

| Opérateur | Description        | Exemple                     |
|-----------|--------------------|-----------------------------|
| `+`       | Addition           | `rate(a[5m]) + rate(b[5m])` |
| `-`       | Soustraction       | `rate(a[5m]) - rate(b[5m])` |
| `*`       | Multiplication     | `http_requests_total * 60`  |
| `/`       | Division           | `rate(a[5m]) / rate(b[5m])` |
| `%`       | Modulo             | `http_requests_total % 100` |

> Les opérandes doivent être compatibles (même type et forme).

---

### Opérateurs de Comparaison

Comparent deux vecteurs instantanés.

| Opérateur | Description        | Exemple                           |
|-----------|--------------------|-----------------------------------|
| `==`      | Égal               | `rate(a[5m]) == rate(b[5m])`      |
| `!=`      | Différent de       | `rate(a[5m]) != 0`                |
| `>`       | Supérieur à        | `http_requests_total > 100`       |
| `<`       | Inférieur à        | `http_requests_total < 10`        |
| `>=`      | Supérieur ou égal  | `rate(a[5m]) >= 2`                |
| `<=`      | Inférieur ou égal  | `http_requests_total <= 5`        |

> Renvoie un vecteur instantané booléen.

---

### Opérateurs Logiques

Combinent des expressions booléennes.

| Opérateur | Description        | Exemple                              |
|-----------|--------------------|--------------------------------------|
| `and`     | ET logique         | `rate(a[5m]) > 1 and rate(b[5m]) > 1`|
| `or`      | OU logique         | `rate(a[5m]) > 1 or rate(b[5m]) > 1` |
| `unless`  | Sauf               | `rate(a[5m]) unless rate(b[5m]) > 0` |

> Les opérandes doivent être des vecteurs booléens de même cardinalité.

---

## Fonctions

PromQL inclut des fonctions intégrées pour la transformation et l'analyse.

**Fonctions Courantes** :
- `rate(v range-vector)` – taux par seconde.
- `irate(v range-vector)` – taux instantané (deux derniers points).
- `avg(v)` – valeur moyenne.
- `sum(v)` – somme des valeurs.
- `count(v)` – nombre d'éléments.
- `min(v)`, `max(v)` – minimum/maximum.
- `quantile(v instant-vector, q)` – percentile.

**Exemple** :
```
quantile by (job)(0.95, http_request_duration_seconds_bucket[5m])
```

> Voir la [Documentation des Fonctions Prometheus](https://prometheus.io/docs/prometheus/latest/querying/functions/) pour la liste complète.

---

## API HTTP pour les Requêtes

Les requêtes PromQL peuvent être envoyées via l'API HTTP.

### Requêtes Instantanées

**Point de terminaison** : `/api/v1/query`

**Méthode** : `GET`

**Paramètres** :
- `query` : expression PromQL
- `time` : horodatage d'évaluation (secondes Unix, optionnel)
- `timeout` : délai d'expiration de la requête (ex: `30s`)

**Exemple** :
```
GET /api/v1/query?query=http_requests_total{job="prometheus"}&time=1609746000
```

**Réponse** : JSON avec `status`, `data.result` (vecteur instantané ou scalaire).

---

### Requêtes par Plage

**Point de terminaison** : `/api/v1/query_range`

**Paramètres** :
- `query` : expression PromQL
- `start` : heure de début (secondes Unix)
- `end` : heure de fin (secondes Unix)
- `step` : pas de résolution (ex: `15s`)

**Exemple** :
```
GET /api/v1/query_range?query=rate(http_requests_total[5m])&start=1609746000&end=1609746600&step=10s
```

**Réponse** : JSON avec les données des séries temporelles à chaque pas.

---

## Notes Supplémentaires

- **Littéraux** :
  - Chaînes : `"hello"`, `'world'`, `` `raw` ``
  - Flottants : `3.14`, `-2.5e-3`, `1_000`, `0xFF`
  - Durées : `5m`, `1h30m`, `500ms`

- **Commentaires** : Commencent par `#`

- **Données périmées** : Les séries deviennent périmées après 5 minutes (par défaut) sans mise à jour.

- **Sous-requête** : Exécute une requête instantanée sur une plage :
  ```
  rate(http_requests_total[10m:5m])[5m]
  ```

---

Ce guide couvre les bases de PromQL pour les utilisateurs débutants à intermédiaires. Pour une utilisation avancée, reportez-vous aux [Bases des Requêtes Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/) et aux pages liées.