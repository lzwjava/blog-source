---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Prévention de la perte d'événements lors de la mise à l'échelle AKS
translated: true
type: note
---

### Cause probable de perte d'événements
Lorsque votre service effectue un scale-up automatique de 1 à 2 pods dans Azure Kubernetes Service (AKS), le pod initial gère seul la charge croissante jusqu'à ce que le nouveau pod soit prêt (généralement 1 à 2 minutes, selon votre configuration HPA). Si le volume d'événements augmente brutalement pendant cette fenêtre de temps, votre espace de noms Event Hubs peut limiter l'entrée (par exemple, en raison d'unités de débit insuffisantes), entraînant une perte d'environ 1% (erreurs ServerBusy). Event Hubs garantit une livraison au moins une fois, mais sans nouvelles tentatives appropriées, les envois limités échouent silencieusement ou perdent des événements.

Le scale-up en lui-même n'interrompt pas la connexion du pod existant — la perte provient d'une surcharge transitoire, et non de l'arrêt du pod.

### Comment corriger et configurer
Pour gérer cela de manière fiable :

1. **Activer l'Auto-Inflate sur l'espace de noms Event Hubs**  
   Cela met automatiquement à l'échelle les unités de débit (TU) lorsque l'entrée dépasse votre ligne de base (par exemple, de 1 à 20 TU), empêchant ainsi la limitation lors de pics de charge comme les événements de mise à l'échelle.  
   - Dans le Portail Azure : Allez dans votre espace de noms Event Hubs > **Paramètres** > **Mise à l'échelle** > Cochez **Activer l'auto-inflate** > Définissez le nombre maximal de TU (par exemple, 20) > Enregistrer.  
   - CLI : `az eventhubs namespace update --resource-group <rg> --name <namespace> --enable-auto-inflate true --maximum-throughput-units 20`  
   - Coût : Facturé par heure pour le maximum atteint ; commencez avec une ligne de base de 5 à 10 TU.  
   Cela garantit que la capacité augmente de manière proactive sans intervention manuelle.

2. **Configurer le client producteur pour les nouvelles tentatives et la fiabilité**  
   Utilisez le SDK Azure Event Hubs dans votre code d'application pour implémenter des nouvelles tentatives avec backoff exponentiel sur les erreurs transitoires (limitation, timeouts). Les valeurs par défaut sont souvent de 3 nouvelles tentatives avec un timeout de 60s — ajustez selon vos besoins. Regroupez les événements (par exemple, 100 à 500 par envoi) pour réduire les appels d'API et améliorer la résilience.  
   - **Bonnes pratiques générales** :  
     - Définir le nombre maximal de nouvelles tentatives : 5-10.  
     - Backoff exponentiel : Commencer à 1s, délai maximum de 30s.  
     - Timeout de connexion : 30-60s.  
     - Utiliser des clés idempotentes (par exemple, UUID par événement) si les doublons sont tolérables (Event Hubs prend en charge cela dans les niveaux Premium/Dédié).  
     - Surveiller via Azure Monitor : Suivre les métriques `IncomingMessages` vs. `ThrottledRequests`.  

   - **Exemple : .NET (Azure.Messaging.EventHubs)**  
     ```csharp
     using Azure.Messaging.EventHubs;
     using Azure.Messaging.EventHubs.Producer;

     var connectionString = "<your-connection-string>";
     var eventHubName = "<your-eventhub-name>";

     var clientOptions = new EventHubProducerClientOptions
     {
         Retry = new EventHubsRetryOptions
         {
             TryTimeout = TimeSpan.FromSeconds(60),  // Timeout par opération
             MaximumTries = 7,  // Nouvelles tentatives max
             Delay = TimeSpan.FromSeconds(2),  // Backoff initial
             MaximumDelay = TimeSpan.FromSeconds(30),  // Backoff max
             Mode = RetryMode.Exponential  // Stratégie de backoff
         },
         ConnectionOptions = new EventHubConnectionOptions
         {
             TransportType = EventHubsTransportType.AmqpWebSockets  // Pour la mise en réseau AKS
         }
     };

     await using var producer = new EventHubProducerClient(connectionString, eventHubName, clientOptions);

     // Envoyer un lot
     using var batch = await producer.CreateBatchAsync(new CreateBatchOptions { PartitionKey = "your-key" });
     batch.TryAdd(new EventData(Encoding.UTF8.GetBytes("event-data")));
     await producer.SendAsync(batch);
     ```  
     Cela réessaie en cas de ServerBusy, garantissant que les événements sont livrés après le scale-up.

   - **Exemple : Java (Azure Event Hubs Client)**  
     ```java
     import com.azure.messaging.eventhubs.EventHubProducerAsyncClient;
     import com.azure.messaging.eventhubs.EventHubProducerClientBuilder;
     import com.azure.messaging.eventhubs.models.CreateBatchOptions;
     import com.azure.messaging.eventhubs.models.EventHubProducerAsyncClientBuilder;
     import com.azure.core.amqp.AmqpRetryOptions;

     String connectionString = "<your-connection-string>";
     String eventHubName = "<your-eventhub-name>";

     AmqpRetryOptions retryOptions = new AmqpRetryOptions()
         .setMaxRetries(7)
         .setInitialDelay(Duration.ofSeconds(2))
         .setMaxDelay(Duration.ofSeconds(30))
         .setTryTimeout(Duration.ofSeconds(60));

     EventHubProducerAsyncClient producer = new EventHubProducerClientBuilder()
         .connectionString(connectionString, eventHubName)
         .retryOptions(retryOptions)
         .transportType(TransportType.AMQP_WEB_SOCKETS)  // Pour AKS
         .buildAsyncClient();

     // Envoyer un lot
     Flux<PartitionInformation> partitions = producer.getPartitionPropertiesFlux();
     // ... logique pour envoyer un lot avec nouvelles tentatives intégrées
     ```  
     Le SDK gère les nouvelles tentatives de manière transparente sur les erreurs.

   - **Autres langages** : Modèles similaires en Python (azure-eventhub), Node.js (utiliser les options de nouvelle tentative dans EventHubProducerClient). Voir la documentation du SDK pour votre stack.

3. **Gestion spécifique à AKS pour la mise à l'échelle**  
   - **Mise à l'échelle proactive** : Ajustez le HPA pour qu'il mette à l'échelle plus tôt (par exemple, CPU cible à 60% vs 80%) pour réduire la fenêtre de surcharge :  
     ```yaml
     apiVersion: autoscaling/v2
     kind: HorizontalPodAutoscaler
     metadata:
       name: your-app-hpa
     spec:
       scaleTargetRef:
         apiVersion: apps/v1
         kind: Deployment
         name: your-app
       minReplicas: 1
       maxReplicas: 10
       metrics:
       - type: Resource
         resource:
           name: cpu
           target:
             type: Utilization
             averageUtilization: 60  # Mise à l'échelle à 60% CPU
     ```  
     Appliquez avec `kubectl apply -f hpa.yaml`.  
   - **Comportement gracieux des pods** : Définissez `terminationGracePeriodSeconds: 30` dans votre YAML de Déploiement pour permettre aux événements mis en mémoire tampon d'être vidés lors des futurs scale-down (pas directement pour le scale-up, mais bonne pratique).  
   - **Mise en réseau** : Utilisez WebSockets (AMQP over WebSockets) dans les options du client pour une meilleure gestion de la sortie AKS.  
   - **Surveillance** : Activez les diagnostics AKS vers Log Analytics ; interrogez les événements de pod pendant la mise à l'échelle (par exemple, `KubePodInventory | where TimeGenerated > ago(1h)`).

4. **Protections supplémentaires**  
   - **Espace de noms redondant inter-zone** : Activez-le lors de la création de l'espace de noms (par défaut dans les régions prises en charge) pour un SLA de 99,99% et aucune perte lors des défaillances de zone.  
   - **Partitions** : Utilisez 4 à 32 partitions en fonction de la charge (par exemple, correspondre aux producteurs parallèles attendus) ; attribuez des clés de partition pour le regroupement ordonné.  
   - **Fonctionnalité Capture** : Activez Event Hubs Capture vers Blob Storage comme sauvegarde pour toute perte rare (niveau Premium).  
   - **Test** : Simulez la charge avec des outils comme Apache JMeter ; surveillez l'absence de limitation après la configuration.

Cette configuration devrait réduire la perte à presque zéro. Commencez par l'auto-inflate + les nouvelles tentatives du client pour des résultats rapides.

### Références
- [Fiabilité dans Azure Event Hubs](https://learn.microsoft.com/en-us/azure/reliability/reliability-event-hubs)  
- [Mise à l'échelle avec Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-scalability)  
- [Options de nouvelle tentative du SDK .NET Event Hubs](https://learn.microsoft.com/en-us/dotnet/api/azure.messaging.eventhubs.producer.eventhubproducerclientoptions.retryoptions)  
- [Concepts de mise à l'échelle AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-scale)