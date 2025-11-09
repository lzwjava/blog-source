---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Exemples avancés du langage de requête Kusto
translated: true
type: note
---

Le langage de requête Kusto (KQL) est un outil puissant pour interroger de grands jeux de données dans des services Azure comme Azure Data Explorer et Azure Monitor. Vous trouverez ci-dessous plusieurs exemples complexes qui combinent de multiples opérateurs, fonctions et fonctionnalités avancées telles que l'analyse de séries temporelles, la détection d'anomalies, le pivotage et les fonctions définies par l'utilisateur. Ils sont tirés de scénarios réels comme l'analyse d'événements météorologiques ou de données de ventes. Chacun inclut la requête et une brève explication.

### 1. Détection d'anomalies dans des données de séries temporelles
Cette requête agrège les moyennes quotidiennes d'une table de métriques et utilise la décomposition de séries pour identifier les anomalies, idéale pour surveiller les modèles inhabituels dans les journaux d'activité ou la télémétrie.

```
TableName
| make-series Metric = avg(Value) on Timestamp step 1d
| extend Anomalies = series_decompose_anomalies(Metric)
```

### 2. Fonction définie par l'utilisateur pour un filtrage paramétré et une synthèse
Ici, une fonction réutilisable filtre les données de vente par région et seuil, puis calcule les totaux—utile pour les rapports dynamiques dans les tableaux de bord Azure Data Explorer.

```
let CalculateSales = (region: string, minSales: int) {
    SalesData
    | where Region == region and Sales > minSales
    | summarize TotalSales = sum(Sales)
};
CalculateSales("North America", 1000)
```

### 3. Pivotage de données agrégées pour une analyse croisée
Ceci agrège les valeurs par catégorie et région, puis pivote les régions en colonnes pour une comparaison plus facile, courant dans les requêtes de business intelligence.

```
TableName
| summarize Total = sum(Value) by Category, Region
| evaluate pivot(Region, sum(Total))
```

### 4. Analyse de corrélation entre des métriques de séries temporelles
Utilisant les données d'événements météorologiques, ceci crée des séries quotidiennes pour deux métriques et calcule leur corrélation pour découvrir des relations, comme entre les dommages matériels et les décès.

```
StormEvents
| make-series PropertyDamage = avg(DamageProperty), Fatalities = avg(Fatalities) on BeginTime step 1d
| extend Correlation = series_correlation(PropertyDamage, Fatalities)
```

### 5. Filtrage, sélection des principaux éléments et calcul de la durée pour l'analyse d'événements
Ceci filtre les événements d'inondation au Texas, sélectionne les 5 principaux par dommage et ajoute une colonne de durée calculée—excellent pour la réponse aux incidents dans Azure Sentinel.

```
StormEvents
| where State == 'TEXAS' and EventType == 'Flood'
| top 5 by DamageProperty
| project StartTime, EndTime, Duration = EndTime - StartTime, DamageProperty
```

### 6. Mappage de valeurs statiques avec une instruction Let pour la transformation des données
Définit un dictionnaire pour mapper les types de sources, filtre les événements et projette des noms conviviaux—utile pour normaliser les données catégorielles dans les journaux.

```
let sourceMapping = dynamic(
  {
    "Emergency Manager" : "Public",
    "Utility Company" : "Private"
  });
StormEvents
| where Source == "Emergency Manager" or Source == "Utility Company"
| project EventId, Source, FriendlyName = sourceMapping[Source]
```

Ces exemples peuvent être exécutés directement dans l'interface web Azure Data Explorer ou Log Analytics. Pour en savoir plus, explorez la galerie d'exemples officielle.

[Guide complet du langage de requête Kusto (KQL)](https://medium.com/@danushidk507/comprehensive-guide-to-kusto-query-language-kql-from-beginner-to-advanced-8dff3bd7568e)  
[Tutoriel : Apprendre les opérateurs courants du langage de requête Kusto](https://learn.microsoft.com/fr-fr/kusto/query/tutorials/learn-common-operators?view=microsoft-fabric)