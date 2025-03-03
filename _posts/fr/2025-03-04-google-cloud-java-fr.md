---
audio: false
generated: true
lang: fr
layout: post
title: Google Cloud Java Client
translated: true
---

### Points Clés
- Il semble probable que pour utiliser `com.google.cloud` en Java, il faille configurer un environnement de développement Java, inclure les dépendances de la bibliothèque cliente Google Cloud, configurer l'authentification et utiliser les bibliothèques pour interagir avec les services Google Cloud.
- La recherche suggère que l'authentification peut être gérée automatiquement sur les plateformes Google Cloud ou configurée manuellement pour le développement local en utilisant les informations d'identification du compte de service.
- Les preuves penchent en faveur de l'utilisation de Maven ou Gradle pour la gestion des dépendances, avec des exemples fournis pour le stockage en nuage comme cas d'utilisation courant.

### Configuration de Votre Environnement de Développement
Pour commencer, assurez-vous d'avoir un Kit de Développement Java (JDK) version 8 ou supérieure installé, ainsi qu'un outil de construction comme Maven ou Gradle. Ces outils aident à gérer les dépendances de votre projet et les processus de construction.

### Inclusion des Dépendances
Ajoutez les dépendances de la bibliothèque cliente Google Cloud à votre projet. Pour Maven, incluez la Liste de Matériaux (BOM) et les bibliothèques de services spécifiques dans votre fichier `pom.xml`. Par exemple, pour utiliser le stockage en nuage :

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Remplacez "latest_version" par la version réelle à partir du [dépôt GitHub des bibliothèques clientes Java Google Cloud](https://github.com/googleapis/google-cloud-java).

### Configuration de l'Authentification
L'authentification est souvent gérée automatiquement si votre application s'exécute sur des plateformes Google Cloud comme Compute Engine ou App Engine. Pour le développement local, définissez la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` pour pointer vers un fichier clé JSON d'un compte de service, ou configurez-le de manière programmatique.

### Utilisation des Bibliothèques
Une fois configuré, importez les classes nécessaires, créez un objet de service et effectuez des appels API. Par exemple, pour lister les seaux dans le stockage en nuage :

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Un détail inattendu est que les bibliothèques prennent en charge divers services Google Cloud, chacun avec son propre sous-package sous `com.google.cloud`, tel que `com.google.cloud.bigquery` pour BigQuery, offrant une fonctionnalité étendue au-delà du stockage.

---

### Note de l'Enquête : Guide Complet sur l'Utilisation de `com.google.cloud` en Java

Cette note fournit une exploration détaillée de l'utilisation des bibliothèques clientes Java Google Cloud, en se concentrant spécifiquement sur le package `com.google.cloud`, pour interagir avec les services Google Cloud. Elle développe la réponse directe en incluant tous les détails pertinents de la recherche, organisés pour la clarté et la profondeur, adaptés aux développeurs cherchant à comprendre en profondeur.

#### Introduction aux Bibliothèques Clients Java Google Cloud
Les bibliothèques clientes Java Google Cloud, accessibles sous le package `com.google.cloud`, fournissent des interfaces idiomatiques et intuitives pour interagir avec les services Google Cloud tels que le stockage en nuage, BigQuery et Compute Engine. Ces bibliothèques sont conçues pour réduire le code de remplissage, gérer les détails de communication de bas niveau et s'intégrer sans effort avec les pratiques de développement Java. Elles sont particulièrement utiles pour la construction d'applications natives au cloud, en tirant parti d'outils comme Spring, Maven et Kubernetes, comme le souligne la documentation officielle.

#### Configuration de l'Environnement de Développement
Pour commencer, un Kit de Développement Java (JDK) version 8 ou supérieure est requis, garantissant la compatibilité avec les bibliothèques. La distribution recommandée est Eclipse Temurin, une option open-source certifiée Java SE TCK, comme indiqué dans les guides de configuration. De plus, un outil d'automatisation de la construction comme Maven ou Gradle est essentiel pour gérer les dépendances. L'interface de ligne de commande Google Cloud (`gcloud`) peut également être installée pour interagir avec les ressources à partir de la ligne de commande, facilitant les tâches de déploiement et de surveillance.

#### Gestion des Dépendances
La gestion des dépendances est simplifiée à l'aide de la Liste de Matériaux (BOM) fournie par Google Cloud, qui aide à gérer les versions à travers plusieurs bibliothèques. Pour Maven, ajoutez ce qui suit à votre `pom.xml` :

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope.import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
<dependencies>
    <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-storage</artifactId>
    </dependency>
</dependencies>
```

Pour Gradle, des configurations similaires s'appliquent, garantissant la cohérence des versions. Le numéro de version doit être vérifié contre le [dépôt GitHub des bibliothèques clientes Java Google Cloud](https://github.com/googleapis/google-cloud-java) pour les dernières mises à jour. Ce dépôt détaille également les plateformes prises en charge, y compris x86_64, Mac OS X, Windows et Linux, mais note des limitations sur Android et Raspberry Pi.

#### Mécanismes d'Authentification
L'authentification est une étape critique, avec des options variant par environnement. Sur les plateformes Google Cloud comme Compute Engine, Kubernetes Engine ou App Engine, les informations d'identification sont déduites automatiquement, simplifiant le processus. Pour d'autres environnements, tels que le développement local, les méthodes suivantes sont disponibles :

- **Compte de Service (Recommandé)** : Générez un fichier clé JSON à partir de la console Google Cloud et définissez la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` sur son chemin. Alternativement, chargez-le de manière programmatique :
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **Développement Local/Test** : Utilisez l'outil SDK Google Cloud avec `gcloud auth application-default login` pour des informations d'identification temporaires.
- **Jeton OAuth2 Existants** : Utilisez `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` pour des cas d'utilisation spécifiques.

L'ordre de priorité pour la spécification de l'ID de projet inclut les options de service, la variable d'environnement `GOOGLE_CLOUD_PROJECT`, App Engine/Compute Engine, le fichier de clés JSON et l'outil SDK Google Cloud, avec `ServiceOptions.getDefaultProjectId()` aidant à déduire l'ID de projet.

#### Utilisation des Bibliothèques Clients
Une fois les dépendances et l'authentification configurées, les développeurs peuvent utiliser les bibliothèques pour interagir avec les services Google Cloud. Chaque service a son propre sous-package sous `com.google.cloud`, tel que `com.google.cloud.storage` pour le stockage en nuage ou `com.google.cloud.bigquery` pour BigQuery. Voici un exemple détaillé pour le stockage en nuage :

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Cet exemple liste tous les seaux, mais la bibliothèque prend en charge des opérations telles que le téléchargement d'objets, le téléchargement de fichiers et la gestion des politiques de seau. Pour d'autres services, des motifs similaires s'appliquent, avec des méthodes détaillées disponibles dans les javadocs respectifs, tels que ceux pour BigQuery à [Google Cloud Java reference docs](https://googleapis.dev/java/google-cloud-clients/latest/).

#### Fonctionnalités Avancées et Considérations
Les bibliothèques prennent en charge des fonctionnalités avancées telles que les opérations à long terme (LRO) à l'aide de `OperationFuture`, avec des délais de nouvelle tentative et des politiques de nouvelle tentative configurables. Par exemple, AI Platform (v3.24.0) inclut par défaut un délai de nouvelle tentative initial de 5000 ms, un multiplicateur de 1,5, un délai de nouvelle tentative maximal de 45000 ms et un délai total de 300000 ms. La configuration proxy est également prise en charge, en utilisant `https.proxyHost` et `https.proxyPort` pour HTTPS/gRPC, avec des options personnalisées pour gRPC via `ProxyDetector`.

L'authentification par clé API est disponible pour certaines API, définie manuellement via des en-têtes pour gRPC ou REST, comme montré dans les exemples pour le service Language. Le test est facilité avec les outils fournis, détaillés dans le TESTING.md du dépôt, et les plugins IDE pour IntelliJ et Eclipse améliorent le développement avec l'intégration de la bibliothèque.

#### Plateformes Prises en Charge et Limitations
Les bibliothèques sont compatibles avec diverses plateformes, avec les clients HTTP fonctionnant partout et les clients gRPC pris en charge sur x86_64, Mac OS X, Windows et Linux. Cependant, ils ne sont pas pris en charge sur Android, Raspberry Pi ou App Engine Standard Java 7, sauf pour Datastore, Storage et BigQuery. Les environnements pris en charge incluent Windows x86_64, Mac OS X x86_64, Linux x86_64, GCE, GKE, GAE Std J8, GAE Flex et Alpine Linux (Java 11+).

#### Ressources et Lectures Complémentaires
Pour des conseils supplémentaires, le [dépôt GitHub des bibliothèques clientes Java Google Cloud](https://github.com/googleapis/google-cloud-java) propose des exemples de code, des directives de contribution et des ressources de dépannage. Les tutoriels comme ceux sur [Baeldung](https://www.baeldung.com/java-google-cloud-storage) fournissent des exemples pratiques, tels que l'utilisation du stockage en nuage, tandis que la documentation officielle à [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) couvre des concepts de développement d'applications plus larges.

#### Tableau : Détails de Configuration Clés

| **Aspect**               | **Détails**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Version Java             | Nécessite Java 8 ou supérieur.                                                                       |
| Gestion des Dépendances    | Utilisez BOM pour la cohérence des versions, par exemple, Maven `libraries-bom`.                                  |
| Méthodes d'Authentification   | Automatique sur GCE/GKE/GAE, manuelle via `GOOGLE_APPLICATION_CREDENTIALS` ou programmatique.          |
| Plateformes Prises en Charge      | Clients HTTP partout, gRPC sur x86_64, Mac OS X, Windows, Linux ; pas sur Android, Raspberry Pi.|
| Service Exemple          | Stockage en nuage : `com.google.cloud.storage`, méthodes pour la liste des seaux, gestion des objets.       |

Ce guide complet garantit que les développeurs disposent de toutes les informations nécessaires pour utiliser efficacement `com.google.cloud` en Java, abordant la configuration, l'authentification, l'utilisation et les fonctionnalités avancées, avec des références vers des sources d'autorité pour une exploration plus approfondie.

#### Citations Clés
- [Dépôt GitHub des bibliothèques clientes Java Google Cloud détaillé code et configuration](https://github.com/googleapis/google-cloud-java)
- [Documentation Google Cloud pour l'aperçu du développement Java](https://cloud.google.com/products/anthos)
- [Tutoriel Baeldung sur le stockage Google Cloud avec des exemples pratiques en Java](https://www.baeldung.com/java-google-cloud-storage)