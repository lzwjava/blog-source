---
audio: false
generated: true
lang: fr
layout: post
title: Client Java Google Cloud
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser `com.google.cloud` en Java, vous devez configurer un environnement de développement Java, inclure les dépendances de la bibliothèque cliente Google Cloud, configurer l'authentification et utiliser les bibliothèques pour interagir avec les services Google Cloud.
- La recherche suggère que l'authentification peut être gérée automatiquement sur les plateformes Google Cloud ou configurée manuellement pour le développement local en utilisant des identifiants de compte de service.
- Les preuves penchent en faveur de l'utilisation de Maven ou Gradle pour gérer les dépendances, avec des exemples fournis pour Cloud Storage comme cas d'utilisation courant.

### Configuration de votre environnement de développement
Pour commencer, assurez-vous d'avoir un Java Development Kit (JDK) version 8 ou supérieure installé, ainsi qu'un outil de build comme Maven ou Gradle. Ces outils aident à gérer les dépendances de votre projet et les processus de build.

### Inclusion des dépendances
Ajoutez les dépendances de la bibliothèque cliente Google Cloud à votre projet. Pour Maven, incluez le Bill of Materials (BOM) et les bibliothèques de service spécifiques dans votre fichier `pom.xml`. Par exemple, pour utiliser Cloud Storage :

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
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

Remplacez "latest_version" par la version actuelle du [dépôt GitHub des bibliothèques clientes Java Google Cloud](https://github.com/googleapis/google-cloud-java).

### Configuration de l'authentification
L'authentification est souvent gérée automatiquement si votre application s'exécute sur des plateformes Google Cloud comme Compute Engine ou App Engine. Pour le développement local, définissez la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` pour pointer vers un fichier de clé JSON d'un compte de service, ou configurez-la par programmation.

### Utilisation des bibliothèques
Une fois configuré, importez les classes nécessaires, créez un objet de service et effectuez des appels d'API. Par exemple, pour lister les buckets dans Cloud Storage :

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

### Note d'enquête : Guide complet sur l'utilisation de `com.google.cloud` en Java

Cette note fournit une exploration détaillée de l'utilisation des bibliothèques clientes Java Google Cloud, en se concentrant spécifiquement sur le package `com.google.cloud`, pour interagir avec les services Google Cloud. Elle développe la réponse directe en incluant tous les détails pertinents de la recherche, organisés pour la clarté et la profondeur, adaptés aux développeurs cherchant une compréhension approfondie.

#### Introduction aux bibliothèques clientes Java Google Cloud
Les bibliothèques clientes Java Google Cloud, accessibles sous le package `com.google.cloud`, fournissent des interfaces idiomatiques et intuitives pour interagir avec les services Google Cloud tels que Cloud Storage, BigQuery et Compute Engine. Ces bibliothèques sont conçues pour réduire le code boilerplate, gérer les détails de communication de bas niveau et s'intégrer de manière transparente avec les pratiques de développement Java. Elles sont particulièrement utiles pour construire des applications cloud-native, en tirant parti d'outils comme Spring, Maven et Kubernetes, comme souligné dans la documentation officielle.

#### Configuration de l'environnement de développement
Pour commencer, un Java Development Kit (JDK) version 8 ou supérieure est requis, assurant la compatibilité avec les bibliothèques. La distribution recommandée est Eclipse Temurin, une option open-source certifiée Java SE TCK, comme noté dans les guides de configuration. De plus, un outil d'automatisation de build comme Maven ou Gradle est essentiel pour gérer les dépendances. L'interface de ligne de commande Google Cloud (`gcloud`) peut également être installée pour interagir avec les ressources depuis la ligne de commande, facilitant les tâches de déploiement et de surveillance.

#### Gestion des dépendances
La gestion des dépendances est rationalisée en utilisant le Bill of Materials (BOM) fourni par Google Cloud, qui aide à gérer les versions entre plusieurs bibliothèques. Pour Maven, ajoutez ce qui suit à votre `pom.xml` :

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>com.google.cloud</groupId>
            <artifactId>libraries-bom</artifactId>
            <version>latest_version</version>
            <type>pom</type>
            <scope>import</scope>
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

Pour Gradle, des configurations similaires s'appliquent, assurant la cohérence des versions. Le numéro de version doit être vérifié par rapport au [dépôt GitHub des bibliothèques clientes Java Google Cloud](https://github.com/googleapis/google-cloud-java) pour les dernières mises à jour. Ce dépôt détaille également les plateformes prises en charge, y compris x86_64, Mac OS X, Windows et Linux, mais note des limitations sur Android et Raspberry Pi.

#### Mécanismes d'authentification
L'authentification est une étape critique, avec des options variant selon l'environnement. Sur les plateformes Google Cloud comme Compute Engine, Kubernetes Engine ou App Engine, les identifiants sont inférés automatiquement, simplifiant le processus. Pour d'autres environnements, tels que le développement local, les méthodes suivantes sont disponibles :

- **Compte de service (Recommandé) :** Générez un fichier de clé JSON depuis la Google Cloud Console et définissez la variable d'environnement `GOOGLE_APPLICATION_CREDENTIALS` sur son chemin. Alternativement, chargez-le par programmation :
  ```java
  import com.google.auth.oauth2.GoogleCredentials;
  import com.google.cloud.storage.*;
  GoogleCredentials credentials = GoogleCredentials.fromStream(new FileInputStream("path/to/key.json"));
  Storage storage = StorageOptions.newBuilder().setCredentials(credentials).build().getService();
  ```
- **Développement/Test local :** Utilisez le SDK Google Cloud avec `gcloud auth application-default login` pour des identifiants temporaires.
- **Token OAuth2 existant :** Utilisez `GoogleCredentials.create(new AccessToken(accessToken, expirationTime))` pour des cas d'utilisation spécifiques.

L'ordre de priorité pour la spécification de l'ID de projet inclut les options de service, la variable d'environnement `GOOGLE_CLOUD_PROJECT`, App Engine/Compute Engine, le fichier d'identifiants JSON et le SDK Google Cloud, avec `ServiceOptions.getDefaultProjectId()` aidant à inférer l'ID de projet.

#### Utilisation des bibliothèques clientes
Une fois les dépendances et l'authentification configurées, les développeurs peuvent utiliser les bibliothèques pour interagir avec les services Google Cloud. Chaque service a son propre sous-package sous `com.google.cloud`, tel que `com.google.cloud.storage` pour Cloud Storage ou `com.google.cloud.bigquery` pour BigQuery. Voici un exemple détaillé pour Cloud Storage :

```java
import com.google.cloud.storage.*;
Storage storage = StorageOptions.getDefaultInstance().getService();
Page<Bucket> buckets = storage.list();
for (Bucket bucket : buckets.iterateAll()) {
    System.out.println(bucket.getName());
}
```

Cet exemple liste tous les buckets, mais la bibliothèque prend en charge des opérations comme le téléversement d'objets, le téléchargement de fichiers et la gestion des politiques de bucket. Pour d'autres services, des modèles similaires s'appliquent, avec des méthodes détaillées disponibles dans les javadocs respectifs, tels que ceux pour BigQuery à [Google Cloud Java reference docs](https://googleapis.dev/java/google-cloud-clients/latest/).

#### Fonctionnalités avancées et considérations
Les bibliothèques prennent en charge des fonctionnalités avancées comme les opérations de longue durée (LROs) en utilisant `OperationFuture`, avec des délais d'attente et des politiques de nouvelle tentative configurables. Par exemple, AI Platform (v3.24.0) inclut par défaut un délai de nouvelle tentative initial de 5000ms, un multiplicateur de 1.5, un délai de nouvelle tentative max de 45000ms et un délai d'attente total de 300000ms. La configuration du proxy est également prise en charge, en utilisant `https.proxyHost` et `https.proxyPort` pour HTTPS/gRPC, avec des options personnalisées pour gRPC via `ProxyDetector`.

L'authentification par clé API est disponible pour certaines API, définie manuellement via des en-têtes pour gRPC ou REST, comme montré dans les exemples pour le service Language. Les tests sont facilités avec les outils fournis, détaillés dans le TESTING.md du dépôt, et les plugins IDE pour IntelliJ et Eclipse améliorent le développement avec l'intégration de la bibliothèque.

#### Plateformes prises en charge et limitations
Les bibliothèques sont compatibles avec diverses plateformes, les clients HTTP fonctionnant partout et les clients gRPC pris en charge sur x86_64, Mac OS X, Windows et Linux. Cependant, elles ne sont pas prises en charge sur Android, Raspberry Pi, ou App Engine Standard Java 7, sauf pour Datastore, Storage et BigQuery. Les environnements pris en charge incluent Windows x86_64, Mac OS X x86_64, Linux x86_64, GCE, GKE, GAE Std J8, GAE Flex et Alpine Linux (Java 11+).

#### Ressources et lectures complémentaires
Pour des conseils supplémentaires, le [dépôt GitHub des bibliothèques clientes Java Google Cloud](https://github.com/googleapis/google-cloud-java) offre des exemples de code, des directives de contribution et des ressources de dépannage. Les tutoriels comme ceux sur [Baeldung](https://www.baeldung.com/java-google-cloud-storage) fournissent des exemples pratiques, tels que l'utilisation de Cloud Storage, tandis que la documentation officielle sur [Google Cloud for Developers](https://developers.google.com/learn/topics/cloud-java) couvre des concepts plus larges de développement d'applications.

#### Tableau : Détails clés de configuration

| **Aspect**               | **Détails**                                                                                     |
|--------------------------|-------------------------------------------------------------------------------------------------|
| Version Java             | Requiert Java 8 ou supérieure.                                                                  |
| Gestion des dépendances  | Utilisez BOM pour la cohérence des versions, par ex. Maven `libraries-bom`.                    |
| Méthodes d'authentification | Automatique sur GCE/GKE/GAE, manuelle via `GOOGLE_APPLICATION_CREDENTIALS` ou par programmation. |
| Plateformes prises en charge | Clients HTTP partout, gRPC sur x86_64, Mac OS X, Windows, Linux ; pas sur Android, Raspberry Pi.|
| Exemple de service       | Cloud Storage : `com.google.cloud.storage`, méthodes pour lister les buckets, gérer les objets. |

Ce guide complet assure que les développeurs ont toutes les informations nécessaires pour utiliser efficacement `com.google.cloud` en Java, abordant la configuration, l'authentification, l'utilisation et les fonctionnalités avancées, avec des références à des sources autorisées pour une exploration plus poussée.

#### Citations clés
- [Dépôt GitHub des bibliothèques clientes Java Google Cloud - code détaillé et configuration](https://github.com/googleapis/google-cloud-java)
- [Documentation Google Cloud pour la vue d'ensemble du développement Java](https://cloud.google.com/products/anthos)
- [Tutoriel Baeldung sur Google Cloud Storage avec Java - exemples pratiques](https://www.baeldung.com/java-google-cloud-storage)