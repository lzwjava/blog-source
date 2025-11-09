---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast:free
title: Guide d'installation et de configuration de la pile ELG
translated: true
type: note
---

### Présentation de la pile ELG (Elasticsearch, Logstash, Grafana)

La pile ELG (souvent une variante de la pile ELK où Kibana est remplacé par Grafana pour la visualisation) est une suite open-source puissante pour collecter, traiter, stocker et visualiser de grands volumes de données, en particulier les logs d'applications, de serveurs et d'infrastructure. Elle permet la surveillance, l'analyse et l'alerte en temps réel. Composants clés :

- **Elasticsearch** : Un moteur de recherche et d'analyse distribué pour stocker, rechercher et analyser des données à grande échelle.
- **Logstash** : Un pipeline de traitement de données qui ingère des données de multiples sources, les transforme et les envoie vers Elasticsearch.
- **Grafana** : Un outil de tableau de bord de visualisation et de surveillance qui se connecte à des sources de données comme Elasticsearch pour créer des graphiques, des diagrammes et des alertes.

Ce guide suppose une connaissance basique de Linux (par exemple, Ubuntu/Debian ; adaptez pour d'autres OS). Utilisez la documentation officielle pour plus de détails. Installation via les téléchargements depuis elastic.co et grafana.com.

#### 1. Installer Elasticsearch
Elasticsearch gère le stockage et l'indexation des données.

- **Prérequis** : Java 11+ (installez via `sudo apt update && sudo apt install openjdk-11-jdk`).
- Télécharger et installer :
  ```
  wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
  echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list
  sudo apt update && sudo apt install elasticsearch
  ```
- Démarrer et activer : `sudo systemctl start elasticsearch && sudo systemctl enable elasticsearch`.
- Vérifier : Visitez `http://localhost:9200` – devrait retourner du JSON avec les infos du cluster.
- Configuration de base (éditez `/etc/elasticsearch/elasticsearch.yml`) : Définissez `network.host: 0.0.0.0` pour un accès distant (sécurisez avec TLS/firewall en production).

#### 2. Installer Logstash
Logstash récupère les données des sources (par exemple, fichiers, syslogs) et les expédie vers Elasticsearch.

- Installer aux côtés d'Elasticsearch :
  ```
  sudo apt install logstash
  ```
- Démarrer et activer : `sudo systemctl start logstash && sudo systemctl enable logstash`.
- Exemple de configuration pour ingérer des logs (`/etc/logstash/conf.d/simple.conf`) :
  ```
  input {
    file {
      path => "/var/log/syslog"
      start_position => "beginning"
    }
  }
  filter {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{SYSLOGHOST:host} %{WORD:program}: %{GREEDYDATA:message}" }
    }
  }
  output {
    elasticsearch {
      hosts => ["localhost:9200"]
    }
    stdout { codec => rubydebug }
  }
  ```
- Tester le pipeline : `sudo /usr/share/logstash/bin/logstash -f /etc/logstash/conf.d/simple.conf` (exécutez en arrière-plan pour une utilisation persistante).
- Recharger la configuration : `sudo systemctl restart logstash`.

#### 3. Installer Grafana
Grafana fournit des tableaux de bord pour visualiser les données d'Elasticsearch.

- Installer :
  ```
  wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
  sudo apt update && sudo apt install grafana
  ```
- Démarrer et activer : `sudo systemctl start grafana-server && sudo systemctl enable grafana-server`.
- Accéder : Visitez `http://localhost:3000` (identifiants par défaut : admin/admin ; changez le mot de passe).
- Se connecter à Elasticsearch :
  1. Allez dans Configuration > Data Sources > Add data source.
  2. Sélectionnez "Elasticsearch", définissez l'URL sur `http://localhost:9200`, le nom de l'index (par exemple, `logstash-*`) et le champ de temps (par exemple, `@timestamp`).
  3. Sauvegardez et testez la connexion.

#### Mise en place du pipeline ELG complet
1. **Flux de données** : Logstash collecte/analyse les logs → envoie vers Elasticsearch → Grafana interroge et visualise.
2. **Exemple de workflow** :
   - Envoyer des données d'exemple : Utilisez les plugins d'entrée Logstash ou des outils comme `stdout` pour les tests.
   - Indexer dans Elasticsearch : Les logs apparaissent comme des documents (par exemple, via l'API Kibana ou curl direct : `curl -X GET "localhost:9200/_search?pretty"`).
   - Tableau de bord dans Grafana : Créez des panneaux (par exemple, un graphique linéaire pour les erreurs de logs dans le temps en utilisant des requêtes Lucene comme `program:kern*`).
3. **Bases de la sécurité** : Utilisez HTTPS/TLS, l'authentification (par exemple, X-Pack pour Elasticsearch) et des firewalls. Pour la production, mettez à l'échelle avec plusieurs nœuds/cluser.
4. **Surveillance** : Activez la surveillance JVM dans Elasticsearch ; Grafana a des alertes intégrées pour les seuils.

#### Problèmes courants et conseils
- **Mémoire insuffisante** : Augmentez le tas JVM dans `/etc/elasticsearch/jvm.options` (par exemple, `-Xms1g -Xmx1g`).
- **Conflits de ports** : Ports par défaut : Elasticsearch 9200/9300, Logstash 5044, Grafana 3000 – vérifiez avec `netstat -tulpn`.
- **Performance** : Utilisez des beats (par exemple, Filebeat) au lieu de Logstash pour un envoi plus léger.
- **Ressources d'apprentissage** : Guides officiels d'Elastic (elastic.co/guide), documentation de Grafana (grafana.com/docs). Pratiquez avec Docker : Cherchez "ELG stack Docker Compose" sur GitHub.

Pour des configurations personnalisées ou le dépannage d'erreurs spécifiques, fournissez plus de détails. Ceci est un point de départ ; ELG excelle dans l'analyse de logs, les données IoT et la surveillance d'applications.