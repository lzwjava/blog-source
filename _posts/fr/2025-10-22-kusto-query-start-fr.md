---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Prise en main du langage de requête Kusto
translated: true
type: note
---

### Démarrer avec KQL (Kusto Query Language) dans Azure

KQL est un langage de requête puissant et en lecture seule conçu pour analyser de grands volumes de données structurées, semi-structurées et non structurées dans des services Azure comme Azure Data Explorer, Azure Monitor (Log Analytics) et Microsoft Sentinel. Il est intuitif, basé sur des pipes (utilisant `|` pour le flux de données) et optimisé pour les scénarios de big data comme l'analyse de journaux, la télémétrie et la détection de menaces. Voici un guide étape par étape pour l'utiliser.

#### Prérequis
- Un abonnement Azure actif avec accès à un service pertinent (par exemple, un cluster Azure Data Explorer, un espace de travail Log Analytics ou une instance Sentinel).
- Des autorisations appropriées : Au minimum, un accès en lecture aux bases de données, tables ou espaces de travail.
- Une familiarité basique avec les concepts de données (comme les tables et le filtrage) est utile, mais KQL est convivial pour les débutants.
- Optionnel : Installez l'application Azure Data Explorer ou utilisez l'interface web pour un démarrage rapide — aucun environnement de codage n'est nécessaire initialement.

#### Étape 1 : Choisir où exécuter vos requêtes
KQL s'exécute dans plusieurs services Azure. Commencez par celui qui correspond à votre source de données :
- **Azure Data Explorer** : Idéal pour l'exploration de big data. Accédez à l'interface web sur [dataexplorer.azure.com](https://dataexplorer.azure.com/). Sélectionnez un cluster et une base de données, puis ouvrez l'éditeur de requêtes.
- **Azure Monitor / Log Analytics** : Pour les journaux et les métriques. Dans le portail Azure (portal.azure.com), allez dans **Monitor > Logs**, sélectionnez un espace de travail et utilisez l'éditeur de requêtes.
- **Microsoft Sentinel** : Pour l'analyse de sécurité. Dans le portail Azure, naviguez vers **Microsoft Sentinel > Logs** dans votre espace de travail.
- **Autres options** : Microsoft Fabric (via l'éditeur de requêtes KQL) ou intégrez avec des outils comme Power BI pour la visualisation.

Les données sont organisées en une hiérarchie : bases de données > tables > colonnes. Les requêtes sont en lecture seule ; utilisez les commandes de gestion (commençant par `.`) pour les modifications de schéma.

#### Étape 2 : Comprendre la syntaxe de base
Les requêtes KQL sont des instructions en texte brut séparées par des points-virgules (`;`). Elles utilisent un modèle de flux de données :
- Commencez par un nom de table (par exemple, `StormEvents`).
- Faites passer (`|`) les données à travers des opérateurs pour le filtrage, l'agrégation, etc.
- Terminez par une sortie comme `count` ou `summarize`.
- Sensible à la casse pour les noms/opérateurs ; encadrez les mots-clés par `['mot-clé']` si nécessaire.

Une structure de requête simple :
```
TableName
| where Condition
| summarize Count = count() by GroupByColumn
```

Les commandes de gestion (pas les requêtes) commencent par `.` (par exemple, `.show tables` pour lister les tables).

#### Étape 3 : Écrire et exécuter votre première requête
1. Ouvrez l'éditeur de requêtes dans le service choisi (par exemple, l'interface web d'Azure Data Explorer).
2. Saisissez une requête basique. Exemple utilisant des données d'exemple (table StormEvents, disponible dans la plupart des environnements) :
   ```
   StormEvents
   | where StartTime between (datetime(2007-11-01) .. datetime(2007-12-01))
   | where State == "FLORIDA"
   | count
   ```
   - Ceci filtre les tempêtes en Floride pour novembre 2007 et renvoie le décompte (par exemple, 28).
3. Cliquez sur **Exécuter** pour lancer la requête. Les résultats apparaissent sous forme de tableau ; utilisez l'interface utilisateur pour visualiser sous forme de graphiques ou exporter.
4. Itérez : Ajoutez des opérateurs comme `project` (sélectionner des colonnes), `summarize` (agréger) ou `extend` (ajouter des colonnes calculées).

Opérateurs courants à apprendre en premier :
- `where` : Filtrer les lignes (par exemple, `| where Level == "Error"`).
- `summarize` : Agréger (par exemple, `| summarize avg(Duration) by User`).
- `join` : Combiner des tables.
- `search` : Recherche en texte intégral dans les tables.

#### Étape 4 : Explorer les fonctionnalités avancées et les bonnes pratiques
- **Séries temporelles et analytique** : Utilisez des fonctions comme `make-series` pour les tendances ou `detect-anomalies` pour les valeurs aberrantes.
- **Visualisation** : Dans l'éditeur, passez aux vues grille/graphique. Exportez vers Power BI pour les tableaux de bord.
- **Conseils de performance** : Ordonnez les opérateurs logiquement (filtrez tôt), limitez les résultats avec `take 100`, et testez sur de petits jeux de données.
- **Cas d'utilisation courants** :
  - **Analyse de journaux** : Interrogez les erreurs dans les applications (`| where Level == "Error" | take 50`).
  - **Chasse aux menaces** : Dans Sentinel, recherchez les menaces (`search "connexion suspecte"`).
  - **Exploration de données** : Résumez les métriques (`| summarize count() by bin(TimeGenerated, 1h)`).

#### Dépannage
- Des erreurs ? Vérifiez la syntaxe dans l'éditeur (il met en évidence les problèmes). Assurez-vous que les noms de table/colonne correspondent exactement.
- Aucune donnée ? Vérifiez que votre espace de travail a ingéré des journaux ou utilisez des jeux de données d'exemple.
- Apprenez-en plus via les tutoriels interactifs dans le portail Azure ou la documentation.

Pour une pratique concrète, chargez des données d'exemple dans Azure Data Explorer et expérimentez.

[Références]  
[Vue d'ensemble du langage de requête Kusto (KQL)](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/)  
[Écrire et exécuter votre première requête KQL](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster)  
[Opérateurs KQL courants](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/tutorial?pivots=azuredataexplorer-cluster&tabs=beginner)