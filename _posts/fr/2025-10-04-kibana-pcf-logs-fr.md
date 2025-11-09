---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Configuration de Kibana pour les journaux PCF
translated: true
type: note
---

Il semble que "kabana" fasse probablement référence à **Kibana**, le tableau de bord open source de visualisation de données pour Elasticsearch. Dans le contexte de **Pivotal Cloud Foundry (PCF)** (maintenant rebrandé VMware Tanzu Application Service), Kibana est couramment utilisé pour rechercher, visualiser et analyser les logs via le système de logging de la plateforme (Loggregator). PCF n'exécute pas nativement Kibana de manière autonome mais l'intègre via le service **Log Search**, qui stocke les logs dans Elasticsearch et expose Kibana pour les requêtes.

Si ce n'est pas ce que vous vouliez dire, n'hésitez pas à clarifier ! Ci-dessous, j'expliquerai comment configurer et utiliser Kibana avec les logs PCF. Ceci suppose que vous êtes un administrateur avec accès à PCF Ops Manager et que vous avez un déploiement PCF en cours (version 2.0+). Notez que le logging PCF a évolué ; vérifiez la documentation de votre version pour les spécificités.

### Prérequis
- **Version PCF** : Log Search (avec Kibana) est disponible dans PCF 2.2+. Les versions antérieures utilisaient une tile "ELK" (Elasticsearch, Logstash, Kibana) séparée.
- **Tiles/Services** : Assurez-vous d'avoir la tile **Elastic Runtime** (pour Loggregator) et la tile **Log Search** installées via Pivotal Network (maintenant Broadcom Support Portal).
- **Accès** : Privilèges d'administrateur dans Ops Manager et l'outil en ligne de commande PCF (cf CLI).
- **Ressources** : Allouez des ressources suffisantes (par exemple, 4-8 Go de RAM pour Log Search, selon le volume de logs).

### Étape 1 : Installer et configurer la tile Log Search dans Ops Manager
La tile Log Search achemine les logs PCF (des applications, de la plateforme et des composants système) vers Elasticsearch, les rendant consultables via Kibana.

1. **Télécharger et importer la tile** :
   - Connectez-vous au Broadcom Support Portal (anciennement Pivotal Network).
   - Téléchargez la tile **Log Search for PCF** (par exemple, une version compatible avec votre release PCF).
   - Dans Ops Manager (interface web), allez dans **Catalog** > **Import a Product** et uploadez la tile.

2. **Configurer la tile** :
   - Dans Ops Manager, allez dans la tile **Elastic Runtime** > onglet **Loggregator** :
     - Activez **Loggregator forwarding to external systems** (par exemple, configurez le forwarding syslog ou HTTP si nécessaire, mais pour Log Search, c'est interne).
     - Définissez **Loggregator log retention** sur une valeur comme 5-30 jours.
   - Allez dans la tile **Log Search** :
     - **Assign Availability Zones** : Sélectionnez au moins une AZ pour la haute disponibilité.
     - **Elasticsearch Configuration** :
       - Définissez le nombre d'instances (commencez par 3 pour la production).
       - Configurez le stockage (par exemple, disques persistants de 100 Go).
       - Activez la sécurité (par exemple, TLS pour Elasticsearch).
     - **Kibana Configuration** :
       - Activez Kibana (il est inclus).
       - Définissez les identifiants administrateur (nom d'utilisateur/mot de passe).
     - **Loggregator Integration** :
       - Définissez le nombre maximum de lignes de log par seconde (par exemple, 1000-5000 basé sur votre charge).
       - Définissez les modèles d'index (par exemple, conservez les logs pendant 7-30 jours).
     - **Networking** : Exposez Kibana via une route (par exemple, `kibana.VOTRE-DOMAINE-PCF.com`).
   - Cliquez sur **Apply Changes** pour déployer. Cela peut prendre 30-60 minutes.

3. **Vérifier le déploiement** :
   - Exécutez `cf tiles` ou vérifiez dans Ops Manager le succès.
   - SSH dans une VM Log Search (en utilisant BOSH CLI : `bosh ssh log-search/0`) et confirmez qu'Elasticsearch fonctionne (`curl localhost:9200`).

### Étape 2 : Accéder à Kibana
Une fois déployé :

1. **Via PCF Apps Manager (GUI)** :
   - Connectez-vous à Apps Manager (par exemple, `https://apps.VOTRE-DOMAINE-PCF.com`).
   - Recherchez l'instance de service "Log Search" (elle en crée une automatiquement).
   - Cliquez sur l'instance de service > onglet **Logs**. Cela ouvre une vue Kibana intégrée pour des recherches rapides de logs.

2. **Accès direct à Kibana** :
   - Accédez à l'URL Kibana configurée dans la tile (par exemple, `https://kibana.VOTRE-DOMAINE-PCF.com`).
   - Connectez-vous avec les identifiants administrateur que vous avez définis.
   - Si vous utilisez un domaine personnalisé, assurez-vous que le DNS est correctement pointé et que les routes sont enregistrées (`cf routes` pour vérifier).

3. **Accès CLI (Optionnel)** :
   - Utilisez `cf logs NOM-APP` pour les logs basiques, mais pour des requêtes avancées, utilisez l'interface Kibana ou l'API.
   - Liez Log Search à vos applications : `cf create-service log-search standard my-log-search` puis `cf bind-service NOM-APP my-log-search`.

### Étape 3 : Utiliser Kibana pour les logs PCF
Kibana fournit une interface web pour interroger, filtrer et visualiser les logs des composants PCF (par exemple, logs d'applications, cellules Diego, Gorouter, etc.).

1. **Navigation de base** :
   - **Onglet Discover** : Recherchez des logs en utilisant la syntaxe de requête Lucene.
     - Exemple : Recherchez les erreurs dans une application spécifique : `source_id:APP:nom-de-votre-app AND json.message:ERROR`.
     - Champs disponibles : `timestamp`, `source_id` (par exemple, `APP:votre-app`, `RTR:router`), `message`, `deployment`, etc.
   - **Onglet Visualize** : Créez des tableaux de bord pour des graphiques (par exemple, volume de logs dans le temps, taux d'erreurs).
     - Visualisation exemple : Graphique à barres des logs par source_id.
   - **Onglet Dashboard** : Sauvegardez et partagez des tableaux de bord prédéfinis (Log Search inclut des modèles par défaut pour les logs PCF).

2. **Requêtes courantes et conseils** :
   - **Filtrer par application** : `source_id:APP:nom-de-votre-app` (remplacez par le GUID ou le nom réel de l'application).
   - **Filtrer par temps** : Utilisez le sélecteur de temps (par exemple, dernières 24 heures).
   - **Logs système** : `source_id:DEA` (pour les cellules Diego) ou `source_id:LOGGREGATOR`.
   - **Exporter les logs** : Téléchargez en CSV/JSON depuis Discover.
   - **Avancé** : Utilisez les Dev Tools (console) de Kibana pour interroger Elasticsearch directement, par exemple :
     ```
     GET /logstash-*/_search
     {
       "query": { "match": { "message": "error" } },
       "sort": [ { "timestamp": { "order": "desc" } } ]
     }
     ```
   - **Rétention et indexation** : Les logs sont indexés par jour (par exemple, `logstash-YYYY.MM.DD`). Configurez le rollover dans la tile pour gérer le stockage.

3. **Dépannage des logs** :
   - **Aucun log n'apparaît ?** Vérifiez les règles de forwarding dans Loggregator (Ops Manager > Elastic Runtime > Loggregator). Assurez-vous que les applications émettent des logs (par exemple, via `console.log` dans Node.js).
   - **Problèmes de performance ?** Augmentez le nombre d'instances Elasticsearch ou ajustez les limites de débit des logs.
   - **Sécurité** : Activez l'intégration UAA dans Log Search pour la connexion SSO à Kibana.
   - **Erreurs** : Vérifiez les logs PCF avec `cf logs log-search` ou les logs des errands Ops Manager.

### Ressources supplémentaires
- **Documentation officielle** : VMware Tanzu docs sur [Log Search](https://docs.vmware.com/en/VMware-Tanzu-Application-Service/10.0/tas/GUID-log-search-index.html) (recherchez votre version).
- **Outils CLI** : Installez `uaac` pour l'authentification UAA si nécessaire, ou utilisez `cf curl` pour l'accès API.
- **Alternatives** : Pour des besoins plus simples, utilisez **Log Cache** intégré à PCF (cf CLI : `cf tail NOM-APP`) ou intégrez avec des outils externes comme Splunk via le forwarding syslog.
- **Mises à niveau** : Si vous êtes sur une version legacy de PCF, migrez vers la tile ELK ou contactez le support Broadcom.

Si vous fournissez plus de détails (par exemple, votre version PCF, les messages d'erreur, ou un cas d'utilisation spécifique), je peux affiner davantage !