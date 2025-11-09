---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de configuration d'Azure Application Insights
translated: true
type: note
---

## Qu'est-ce qu'Azure Application Insights ?

Azure Application Insights est un service de gestion des performances des applications (APM) dans Azure Monitor qui vous aide à surveiller des applications web en direct. Il fournit des outils pour détecter les problèmes, diagnostiquer les erreurs et comprendre le comportement des utilisateurs grâce aux données de télémétrie comme les requêtes, les dépendances, les traces, les métriques et les journaux. Il est désormais basé sur OpenTelemetry pour une compatibilité plus large.

## Prérequis
- Un abonnement Azure actif.
- Des autorisations pour créer des ressources dans Azure (par exemple, le rôle Propriétaire ou Contributeur).
- Le code de votre application (prend en charge .NET, Java, Node.js, Python et plus encore).

## Étape 1 : Créer une ressource Application Insights
1. Connectez-vous au [portail Azure](https://portal.azure.com).
2. Cliquez sur **Créer une ressource** dans le menu en haut à gauche.
3. Recherchez "Application Insights" et sélectionnez-le dans les résultats sous **Surveillance + gestion**.
4. Remplissez les détails :
   - **Abonnement** : Choisissez votre abonnement Azure.
   - **Groupe de ressources** : Sélectionnez-en un existant ou créez-en un nouveau.
   - **Nom** : Donnez un nom unique à votre ressource.
   - **Région** : Choisissez une région proche de vos utilisateurs ou de votre application.
   - **Espace de travail** : Liez éventuellement à un espace de travail Log Analytics existant ; sinon, un nouveau est créé automatiquement.
5. Passez en revue et cliquez sur **Créer**. Le déploiement prend quelques minutes.
6. Une fois créée, allez sur la page **Vue d'ensemble** de votre ressource et copiez la **Chaîne de connexion** (passez la souris dessus et cliquez sur l'icône de copie). Celle-ci identifie l'endroit où votre application envoie les données de télémétrie.

**Conseil** : Utilisez des ressources distinctes pour les environnements de développement, de test et de production pour éviter de mélanger les données.

## Étape 2 : Instrumenter votre application
Ajoutez la prise en charge d'OpenTelemetry pour collecter automatiquement les données de télémétrie (requêtes, exceptions, métriques, etc.). Définissez la chaîne de connexion via une variable d'environnement nommée `APPLICATIONINSIGHTS_CONNECTION_STRING` (recommandé pour la production).

### Pour .NET (ASP.NET Core)
1. Installez le package NuGet :
   ```
   dotnet add package Azure.Monitor.OpenTelemetry.AspNetCore
   ```
2. Dans `Program.cs` :
   ```csharp
   using Azure.Monitor.OpenTelemetry.AspNetCore;

   var builder = WebApplication.CreateBuilder(args);
   builder.Services.AddOpenTelemetry().UseAzureMonitor();
   var app = builder.Build();
   app.Run();
   ```
3. Définissez la variable d'environnement avec votre chaîne de connexion et exécutez l'application.

### Pour Java
1. Téléchargez le JAR de la distribution Azure Monitor OpenTelemetry (par exemple, `applicationinsights-agent-3.x.x.jar`).
2. Créez un fichier de configuration `applicationinsights.json` dans le même répertoire :
   ```json
   {
     "connectionString": "Votre chaîne de connexion ici"
   }
   ```
3. Exécutez votre application avec l'agent : `java -javaagent:applicationinsights-agent-3.x.x.jar -jar votre-app.jar`.

### Pour Node.js
1. Installez le package :
   ```
   npm install @azure/monitor-opentelemetry
   ```
2. Configurez dans le point d'entrée de votre application :
   ```javascript
   const { AzureMonitorOpenTelemetry } = require('@azure/monitor-opentelemetry');
   const provider = new AzureMonitorOpenTelemetry({
     connectionString: process.env.APPLICATIONINSIGHTS_CONNECTION_STRING
   });
   provider.start();
   ```
3. Définissez la variable d'environnement et démarrez votre application.

### Pour Python
1. Installez le package :
   ```
   pip install azure-monitor-opentelemetry
   ```
2. Dans votre application :
   ```python
   from azure.monitor.opentelemetry import configure_azure_monitor
   configure_azure_monitor(connection_string="Votre chaîne de connexion ici")
   ```
3. Exécutez l'application.

Pour d'autres langages ou pour l'auto-instrumentation (par exemple, pour Azure App Service), consultez la documentation officielle. Testez d'abord localement.

## Étape 3 : Afficher et analyser les données
1. Exécutez votre application instrumentée et générez un peu d'activité (par exemple, envoyez des requêtes).
2. Dans le portail Azure, ouvrez votre ressource Application Insights.
3. Vérifiez la page **Vue d'ensemble** : Consultez les métriques en direct, le nombre de requêtes et les temps de réponse (les données apparaissent en ~1-2 minutes).
4. Explorez les fonctionnalités :
   - **Métriques en direct** : Flux en temps réel pour les applications en production.
   - **Défaillances** : Analysez les exceptions et les traces.
   - **Performances** : Analysez les dépendances et les requêtes lentes.
   - **Utilisation** : Suivez les sessions utilisateur et les événements personnalisés.
   - **Alertes** : Configurez des notifications pour les problèmes (par exemple, des taux d'échec élevés).
5. Interrogez les données à l'aide du langage de requête Kusto (KQL) dans **Journaux** pour une analyse personnalisée.

## Bonnes pratiques
- Commencez par la télémétrie de base ; ajoutez des événements/métriques personnalisés selon les besoins.
- Surveillez les coûts via la page **Utilisation et coûts estimés** (facturé via Log Analytics).
- Pour la surveillance du navigateur, ajoutez l'extrait du SDK JavaScript à vos pages web.

[Créer et configurer des ressources Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/create-workspace-resource)  
[Activer OpenTelemetry dans Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable)  
[Vue d'ensemble d'Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)