---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Lecture des journaux AWS CloudWatch
translated: true
type: note
---

### Introduction à la lecture des logs dans AWS CloudWatch
AWS CloudWatch Logs est un service qui centralise, surveille et stocke les fichiers de logs provenant de vos ressources AWS (comme les instances EC2, les fonctions Lambda ou les bases de données RDS) et de vos applications. Pour lire les logs, vous devez d'abord vous assurer que les logs sont envoyés vers CloudWatch (par exemple, via l'agent CloudWatch sur EC2 ou l'intégration automatique avec d'autres services). Une fois configuré, vous pouvez visualiser les logs via la Console de gestion AWS, AWS CLI, ou par programmation via les SDK.

### Prérequis
- **Autorisations AWS** : Assurez-vous que votre utilisateur ou rôle IAM dispose des autorisations `logs:DescribeLogGroups`, `logs:DescribeLogStreams`, `logs:GetLogEvents` et `logs:FilterLogEvents` (attachez la politique `CloudWatchLogsReadOnlyAccess`).
- **Configuration des Logs** : Les logs doivent être acheminés vers CloudWatch. Par exemple :
  - Installez l'agent CloudWatch Logs sur les instances EC2.
  - Activez la journalisation dans des services comme Lambda ou ECS.
- **AWS CLI (Optionnel)** : Si vous utilisez la CLI, installez-la et configurez-la avec `aws configure`.

### Visualisation des logs dans la Console de gestion AWS
1. Connectez-vous à la [Console de gestion AWS](https://console.aws.amazon.com/) et ouvrez le service CloudWatch.
2. Dans le volet de navigation gauche, choisissez **Logs** > **Groupes de logs**.
3. Sélectionnez le groupe de logs contenant vos logs (par exemple, `/aws/lambda/ma-fonction` pour les logs Lambda).
4. Dans la liste des flux de logs (sous le groupe de logs sélectionné), choisissez le flux spécifique (par exemple, un par instance ou exécution).
5. Les événements de log se chargeront. Personnalisez la vue :
   - **Développer les événements** : Cliquez sur la flèche à côté d'un événement pour le développer, ou basculez vers la vue **Texte** au-dessus de la liste pour un texte brut.
   - **Filtrer/Rechercher** : Entrez un filtre dans la zone de recherche (par exemple, "ERROR" pour afficher uniquement les lignes d'erreur).
   - **Plage horaire** : Cliquez sur le sélecteur de temps à côté de la zone de recherche. Choisissez **Relative** (par exemple, dernière heure) ou **Absolue** (dates personnalisées), et basculez entre UTC et l'heure locale.
6. Parcourez les événements ou téléchargez-les si nécessaire.

Pour des requêtes avancées sur plusieurs flux ou groupes, utilisez **CloudWatch Logs Insights** (sous Logs > Logs Insights). Écrivez des requêtes comme `fields @timestamp, @message | filter @level = "ERROR" | sort @timestamp desc` pour analyser et visualiser les logs.

### Lecture des logs à l'aide d'AWS CLI
Utilisez ces commandes pour lister et récupérer les logs par programmation. Remplacez les espaces réservés comme `my-log-group` par vos noms réels.

1. **Lister les groupes de logs** :
   ```
   aws logs describe-log-groups --log-group-name-prefix my-log-group
   ```
   Cela renvoie des métadonnées comme l'ARN, la rétention et les octets stockés.

2. **Lister les flux de logs dans un groupe** :
   ```
   aws logs describe-log-streams --log-group-name my-log-group --log-stream-name-prefix 2025
   ```
   Filtre les flux par préfixe (par exemple, des noms basés sur la date) et affiche l'heure de création et la taille.

3. **Obtenir les événements de log d'un flux** :
   ```
   aws logs get-log-events --log-group-name my-log-group --log-stream-name my-stream --start-time 1730137600000
   ```
   - `--start-time` et `--end-time` : Horodatages Unix (millisecondes) pour la plage horaire.
   - `--limit` : Nombre maximum d'événements à retourner (par défaut 1 000).
   - La sortie inclut les horodatages, l'heure d'ingestion et le texte du message.
   - Utilisez `--next-token` de la réponse pour paginer.

Pour des recherches filtrées sur plusieurs flux, utilisez `filter-log-events` :
```
aws logs filter-log-events --log-group-name my-log-group --filter-pattern "ERROR" --start-time 1730137600000
```

### Conseils et bonnes pratiques
- **Rétention** : Les logs sont conservés indéfiniment par défaut ; ajustez par groupe pour gérer les coûts (par exemple, 30 jours).
- **Coûts** : La visualisation est gratuite, mais l'ingestion et le stockage entraînent des frais—surveillez via les métriques CloudWatch.
- **Dépannage** : Si aucun log n'apparaît, vérifiez l'installation de l'agent ou que la journalisation du service est activée.
- Pour une surveillance en temps réel, configurez des filtres de métriques ou des alarmes sur les modèles de logs.

[Working with log groups and log streams - Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html)  
[CloudWatch Logs examples using AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli_cloudwatch-logs_code_examples.html)  
[Analyzing log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)