---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Guide de Vérification des Journaux Kibana
translated: true
type: note
---

Kibana est un outil open-source de visualisation et d'exploration de données développé par Elastic. C'est un composant clé de la **ELK Stack** (Elasticsearch, Logstash, Kibana), largement utilisée pour la centralisation des logs, la surveillance et l'analytique. Kibana fournit une interface web pour interagir avec les données stockées dans Elasticsearch, vous permettant de rechercher, visualiser et analyser les logs en temps réel. Il est particulièrement puissant pour vérifier les logs provenant d'applications, de serveurs ou de services cloud.

Ce guide se concentre sur l'utilisation de Kibana pour inspecter et interroger les logs. Nous aborderons la configuration, l'utilisation de base, les flux de travail de vérification des logs et des conseils avancés. Supposez que vous travaillez avec une configuration ELK de base ; si vous débutez avec ELK, commencez par installer Elasticsearch et Logstash en premier (Kibana nécessite Elasticsearch pour fonctionner).

## 1. Prérequis
Avant d'utiliser Kibana :
- **Elasticsearch** : Version 8.x ou ultérieure (Kibana est étroitement couplé avec les versions d'Elasticsearch). Téléchargez-le sur [elastic.co](https://www.elastic.co/downloads/elasticsearch).
- **Java** : Elasticsearch nécessite JDK 11 ou ultérieur.
- **Exigences système** : Au moins 4 Go de RAM pour le développement ; plus pour la production.
- **Source de données** : Logs ingérés via Logstash, Filebeat, ou directement dans Elasticsearch (par exemple, format JSON avec des horodatages).
- **Accès réseau** : Kibana fonctionne sur le port 5601 par défaut ; assurez-vous qu'il est accessible.

Si vous n'avez pas encore de logs, utilisez des outils comme Filebeat pour envoyer des logs d'exemple (par exemple, les logs système) vers Elasticsearch.

## 2. Installation de Kibana
L'installation de Kibana est simple et indépendante de la plateforme. Téléchargez la dernière version sur [elastic.co/downloads/kibana](https://www.elastic.co/downloads/kibana) (correspondant à votre version d'Elasticsearch).

### Sur Linux (Debian/Ubuntu) :
1. Ajoutez le dépôt d'Elastic :
   ```
   wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
   sudo apt-get install apt-transport-https
   echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
   sudo apt-get update && sudo apt-get install kibana
   ```
2. Démarrez Kibana :
   ```
   sudo systemctl start kibana
   sudo systemctl enable kibana  # Pour le démarrage automatique au boot
   ```

### Sur Windows :
1. Téléchargez l'archive ZIP et extrayez-la dans `C:\kibana-8.x.x-windows-x86_64`.
2. Ouvrez l'invite de commande en tant qu'Administrateur et naviguez vers le dossier extrait.
3. Exécutez : `bin\kibana.bat`

### Sur macOS :
1. Utilisez Homebrew : `brew tap elastic/tap && brew install elastic/tap/kibana-full`.
2. Ou téléchargez le TAR.GZ, extrayez-le et exécutez `./bin/kibana`.

Pour Docker : Utilisez l'image officielle :
```
docker run --name kibana -p 5601:5601 -e ELASTICSEARCH_HOSTS=http://elasticsearch:9200 docker.elastic.co/kibana/kibana:8.10.0
```

## 3. Configuration de base
Modifiez le fichier de configuration `kibana.yml` (situé dans `/etc/kibana/` sur Linux, ou le dossier `config/` sur les autres systèmes).

Paramètres clés pour la vérification des logs :
```yaml
# Se connecter à Elasticsearch (par défaut localhost:9200)
elasticsearch.hosts: ["http://localhost:9200"]

# Paramètres du serveur
server.port: 5601
server.host: "0.0.0.0"  # Lier à toutes les interfaces pour l'accès à distance

# Sécurité (à activer pour la production)
# elasticsearch.username: "elastic"
# elasticsearch.password: "your_password"

# Journalisation
logging.verbose: true  # Pour le débogage de Kibana lui-même

# Modèle d'index (optionnel par défaut)
defaultIndex: "logs-*"
```
- Redémarrez Kibana après les modifications : `sudo systemctl restart kibana`.
- Si vous utilisez les fonctionnalités de sécurité (X-Pack), générez des certificats ou utilisez l'authentification de base.

## 4. Démarrage et accès à Kibana
- Démarrez d'abord Elasticsearch (par exemple, `sudo systemctl start elasticsearch`).
- Démarrez Kibana comme indiqué ci-dessus.
- Ouvrez un navigateur web et allez à `http://localhost:5601` (ou l'IP de votre serveur:5601).
- Lors de la première connexion, vous verrez l'assistant de configuration. Créez un utilisateur admin si demandé (par défaut : elastic/changeme).

L'interface comprend des applications comme **Discover** (pour les logs), **Visualize**, **Dashboard**, **Dev Tools** et **Management**.

## 5. Préparation des données : Modèles d'index
Les logs dans Elasticsearch sont stockés dans des **indices** (par exemple, `logs-2023-10-01`). Pour les interroger dans Kibana, créez un **modèle d'index**.

1. Allez dans **Stack Management** > **Index Patterns** (barre latérale gauche, menu hamburger > Management).
2. Cliquez sur **Create index pattern**.
3. Entrez un modèle comme `logs-*` (correspond à tous les indices de logs) ou `filebeat-*` (pour les logs Filebeat).
4. Sélectionnez le **Time field** (par exemple, `@timestamp` pour les horodatages des logs—crucial pour les requêtes basées sur le temps).
5. Cliquez sur **Create index pattern**.
   - Cela mappe les champs comme `message` (texte du log), `host.name`, `level` (error/warn/info), etc.

Actualisez les champs si vos logs changent. Utilisez **Discover** pour prévisualiser.

## 6. Utilisation de Discover pour vérifier les logs
L'application **Discover** est votre outil principal pour inspecter les logs. C'est comme un visualisateur de logs interrogeable.

### Navigation de base :
1. Cliquez sur **Discover** dans la barre latérale gauche.
2. Sélectionnez votre modèle d'index dans la liste déroulante (en haut à gauche).
3. Définissez la plage de temps (en haut à droite) : Utilisez les options rapides comme "Last 15 minutes" ou personnalisée (par exemple, Last 7 days). Cela filtre les logs par `@timestamp`.

### Visualisation des logs :
- **Hit Count** : Affiche le nombre total de logs correspondants (par exemple, 1 234 hits).
- **Document Table** : Affiche les entrées de logs brutes au format JSON ou texte formaté.
  - Colonnes : Par défaut `@timestamp` et `_source` (log complet). Glissez-déposez les champs de la barre latérale gauche (par exemple, `message`, `host.name`) pour ajouter des colonnes.
  - Développez une ligne (cliquez sur la flèche) pour voir le document JSON complet.
- **Histogramme** : Le graphique du haut montre le volume de logs dans le temps. Zoomez en glissant.

### Recherche dans les logs :
Utilisez la barre de recherche (en haut) pour les requêtes. Kibana utilise par défaut **KQL (Kibana Query Language)**—simple et intuitive.

- **Recherche de base** :
  - Rechercher un mot-clé : `error` (trouve les logs contenant "error").
  - Spécifique à un champ : `host.name:webserver AND level:error` (logs de "webserver" avec le niveau error).
  - Phrases : `"user login failed"` (correspondance exacte).

- **Filtres** :
  - Ajoutez depuis la barre latérale : Cliquez sur une valeur de champ (par exemple, `level: ERROR`) > Add filter (l'épingle à la requête).
  - Logique booléenne : `+error -info` (doit avoir "error", exclure "info").
  - Plage : Pour les nombres/temps, par exemple, `bytes:>1000` (champ > 1000).

- **Requêtes avancées** :
  - Passez à la **syntaxe de requête Lucene** (via la liste déroulante du langage de requête) pour les besoins complexes : `message:(error OR warn) AND host.name:prod*`.
  - Utilisez **Query DSL** dans Dev Tools pour les requêtes natives Elasticsearch (par exemple, POST /logs-*/_search avec un corps JSON).

### Sauvegarde des recherches :
- Cliquez sur **Save** (en haut à droite) pour enregistrer une recherche pour une réutilisation.
- Partagez via **Share** > CSV/URL pour les exports.

Exemple de flux de travail : Vérification des logs d'application
1. Ingérez les logs (par exemple, via Logstash : fichier d'entrée > filtre grok/parse > sortie Elasticsearch).
2. Dans Discover : Plage de temps "Last 24 hours".
3. Recherche : `app.name:myapp AND level:ERROR`.
4. Ajoutez des filtres : `host.name` = serveur spécifique.
5. Inspectez : Regardez `message` pour les stack traces, corrélez avec `@timestamp`.

## 7. Visualisation des logs
Alors que Discover sert à la vérification brute, Visualize sert pour les modèles.

### Créer des visualisations :
1. Allez dans **Visualize Library** > **Create new visualization**.
2. Choisissez le type :
   - **Lens** (facile) : Glissez-déposez les champs dans les buckets (par exemple, Axe X : `@timestamp`, Axe Y : nombre d'erreurs).
   - **Area/Line Chart** : Pour le volume de logs dans le temps (Metrics : Count, Buckets : Date Histogram sur `@timestamp`).
   - **Data Table** : Résumé tabulaire des logs.
   - **Pie Chart** : Répartition par `level` (error 40%, info 60%).
3. Appliquez les filtres/recherches de Discover.
4. Sauvegardez et ajoutez à un **Dashboard** (Analytics > Dashboard > Create new > Add visualization).

Exemple : Tableau de bord du taux d'erreurs
- Visualisez : Graphique linéaire des logs d'erreur par heure.
- Filtre : Plage de temps globale.
- Intégrez dans un Dashboard pour la surveillance.

## 8. Fonctionnalités avancées pour l'analyse des logs
- **Alertes et surveillance** :
  - Utilisez **Alerts** (Stack Management > Rules) pour notifier sur des modèles de logs (par exemple, email si "critical" apparaît >5 fois/heure).
  - **Uptime Monitoring** ou **APM** pour les logs d'applications.

- **Machine Learning** :
  - Activez les jobs ML (Stack Management > Machine Learning) pour détecter les anomalies dans les volumes de logs.

- **Dev Tools** :
  - Console pour les requêtes Elasticsearch brutes : par exemple,
    ```
    GET logs-*/_search
    {
      "query": { "match": { "message": "error" } },
      "sort": [ { "@timestamp": "desc" } ]
    }
    ```
  - Testez les modèles d'index ou ingérez des données.

- **Rôles et sécurité** :
  - En production, utilisez **Spaces** pour isoler les vues de logs (par exemple, dev/prod).
  - Accès basé sur les rôles : Restreignez les utilisateurs à des indices spécifiques.

- **Export/Import** :
  - Exportez les recherches/dashboards au format NDJSON via **Stack Management > Saved Objects**.
  - Importez les logs via **Console** ou Beats.

- **Conseils de performance** :
  - Utilisez **Field Analyzer** (Index Patterns > field) pour les mappings personnalisés.
  - Paginez les grands résultats : Ajustez le nombre de hits par page (paramètres de Discover).
  - Pour les grosses données, fragmentez les indices et utilisez ILM (Index Lifecycle Management).

## 9. Intégration avec les sources de logs
- **Filebeat/Logstash** : Expédiez les logs vers Elasticsearch.
  - Exemple de configuration Filebeat (`filebeat.yml`) :
    ```yaml
    filebeat.inputs:
    - type: log
      paths: [/var/log/*.log]
      fields:
        app: myapp
    output.elasticsearch:
      hosts: ["localhost:9200"]
      index: "logs-%{+yyyy.MM.dd}"
    ```
  - Exécutez : `./filebeat -e`.
- **Logs Cloud** : Intégrez avec AWS S3, Azure ou Elastic Cloud pour les configurations managées.

## 10. Dépannage des problèmes courants
- **Aucune donnée dans Discover** :
  - Vérifiez la connexion Elasticsearch : `curl localhost:9200/_cat/indices`.
  - Vérifiez que le modèle d'index correspond aux indices (par exemple, pas d'erreur de `*`).
  - Assurez-vous que `@timestamp` est mappé en tant que date.

- **Kibana ne démarre pas** :
  - Logs : Vérifiez `/var/log/kibana/kibana.log` ou la sortie console.
  - Courant : Port 5601 utilisé, ou Elasticsearch non démarré/sécurisé.

- **Requêtes lentes** :
  - Optimisez : Utilisez les champs keyword pour les filtres, évitez les wildcards sur les grands textes.
  - Augmentez le heap : Modifiez `jvm.options` pour Elasticsearch (par exemple, `-Xms4g -Xmx4g`).

- **Erreurs dans les logs** :
  - 403/401 : Problèmes d'authentification—activez la sécurité dans `elasticsearch.yml`.
  - Incompatibilité de version : Assurez-vous que Kibana == version d'Elasticsearch.

- **Ressources** :
  - Documentation officielle : [elastic.co/guide/en/kibana/current](https://www.elastic.co/guide/en/kibana/current/index.html).
  - Forums : Elastic Discuss ou Stack Overflow.
  - Données d'exemple : Chargez via Kibana (Stack Management > Kibana > Sample Data).

Ce guide devrait vous aider à démarrer avec Kibana pour la vérification des logs. Commencez petit : Configurez une stack ELK locale, ingérez des logs d'exemple et expérimentez dans Discover. Pour la production, envisagez Elastic Cloud pour plus de facilité. Si vous avez une configuration spécifique (par exemple, Docker, AWS), fournissez plus de détails pour des conseils adaptés !