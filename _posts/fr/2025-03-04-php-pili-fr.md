---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque Cloud de Streaming Pili pour PHP
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser "pili-engineering/pili-sdk-php": "dev-master", vous devez l'installer via Composer et configurer les identifiants Qiniu.
- Les recherches suggèrent que le package nécessite PHP 5.3.0 ou supérieur et est destiné à Pili Streaming Cloud, lié à Qiniu.
- Les preuves indiquent qu'il faut créer un objet Hub et utiliser des opérations sur les streams comme la génération d'URLs RTMP, mais les méthodes exactes peuvent varier.

### Installation
Premièrement, assurez-vous d'avoir Composer installé. Ajoutez le package à votre fichier `composer.json` avec :
```json
"require": {
    "pili-engineering/pili-sdk-php": "dev-master"
}
```
Ensuite, exécutez `composer install` ou `composer update`. Dans votre script PHP, incluez :
```php
require 'vendor/autoload.php';
```

### Configuration et Utilisation
Vous aurez besoin d'un compte Qiniu et d'un Pili Hub. Définissez votre clé d'accès, votre clé secrète et le nom de votre hub, puis créez un objet Hub :
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
Créez ou obtenez un stream, par exemple, `$stream = $hub->createStream('your_stream_key');`, et utilisez des méthodes comme `$stream->rtmpPublishUrl(60)` pour les opérations.

### Détail Inattendu
Notez que "dev-master" est une version de développement, potentiellement instable, avec des versions taguées comme 1.5.5 disponibles pour la production.

---

### Guide Complet sur l'Utilisation de "pili-engineering/pili-sdk-php": "dev-master"

Ce guide fournit une exploration détaillée de la façon d'utiliser le package "pili-engineering/pili-sdk-php" avec la version "dev-master", basée sur la documentation et les exemples disponibles. Il couvre l'installation, la configuration, l'utilisation et des considérations supplémentaires, assurant une compréhension approfondie pour les développeurs travaillant avec les services Pili Streaming Cloud.

#### Contexte
Le package "pili-engineering/pili-sdk-php" est une bibliothèque côté serveur pour PHP, conçue pour interagir avec Pili Streaming Cloud, un service associé à Qiniu, un fournisseur de stockage cloud et CDN. La version "dev-master" fait référence à la dernière branche de développement, qui peut inclure des fonctionnalités récentes mais pourrait être moins stable que les versions taguées. Le package nécessite PHP 5.3.0 ou supérieur, le rendant accessible pour de nombreux environnements PHP au 3 mars 2025.

#### Processus d'Installation
Pour commencer, vous devez avoir Composer installé, un gestionnaire de dépendances pour PHP. L'installation implique d'ajouter le package au fichier `composer.json` de votre projet et d'exécuter une commande Composer pour le télécharger. Spécifiquement :

- Ajoutez ce qui suit à votre `composer.json` dans la section "require" :
  ```json
  "require": {
      "pili-engineering/pili-sdk-php": "dev-master"
  }
  ```
- Exécutez `composer install` ou `composer update` dans votre terminal pour récupérer le package et ses dépendances. Cela créera un répertoire `vendor` avec les fichiers nécessaires.
- Dans votre script PHP, incluez l'autoloader pour accéder aux classes du package :
  ```php
  require 'vendor/autoload.php';
  ```

Ce processus assure l'intégration du package dans votre projet, tirant parti de l'autoloading de Composer pour un accès facile aux classes.

#### Prérequis et Configuration
Avant d'utiliser le SDK, vous avez besoin d'un compte Qiniu et devez configurer un Pili Hub, car le SDK interagit avec les services Pili Streaming Cloud. Cela implique d'obtenir une Access Key et une Secret Key auprès de Qiniu et de créer un hub sur leur plateforme. La documentation suggère que ces identifiants sont essentiels pour l'authentification.

Pour configurer, définissez vos identifiants dans votre script PHP :
- Access Key : Votre Access Key Qiniu.
- Secret Key : Votre Secret Key Qiniu.
- Hub Name : Le nom de votre Pili Hub, qui doit exister préalablement.

Une configuration exemple ressemble à :
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Création et Utilisation de l'Objet Hub
Le cœur du SDK est l'objet Hub, qui facilite la gestion des streams. Premièrement, créez un objet Credentials en utilisant vos clés Qiniu :
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
Ensuite, instanciez un objet Hub avec ces identifiants et le nom de votre hub :
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
Cet objet Hub vous permet d'effectuer diverses opérations liées aux streams, comme créer, récupérer ou lister des streams.

#### Travail avec les Streams
Les streams sont centraux dans Pili Streaming Cloud, et le SDK fournit des méthodes pour les gérer via l'objet Hub. Pour créer un nouveau stream :
```php
$streamKey = 'your_stream_key'; // Doit être unique dans le hub
$stream = $hub->createStream($streamKey);
```
Pour récupérer un stream existant :
```php
$stream = $hub->getStream($streamKey);
```
L'objet stream offre ensuite diverses méthodes pour les opérations, détaillées dans le tableau suivant basé sur la documentation disponible :

| **Opération**          | **Méthode**                     | **Description**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| Créer un Stream         | `$hub->createStream($key)`     | Crée un nouveau stream avec la clé donnée.           |
| Obtenir un Stream       | `$hub->getStream($key)`        | Récupère un stream existant par sa clé.              |
| Lister les Streams      | `$hub->listStreams($marker, $limit, $prefix)` | Liste les streams avec des options de pagination.    |
| URL de Publication RTMP | `$stream->rtmpPublishUrl($expire)` | Génère une URL de publication RTMP avec un temps d'expiration. |
| URL de Lecture RTMP     | `$stream->rtmpPlayUrl()`       | Génère une URL de lecture RTMP pour le stream.       |
| URL de Lecture HLS      | `$stream->hlsPlayUrl()`        | Génère une URL de lecture HLS pour le streaming.     |
| Désactiver le Stream    | `$stream->disable()`           | Désactive le stream.                                 |
| Activer le Stream       | `$stream->enable()`            | Active le stream.                                    |
| Obtenir le Statut du Stream | `$stream->status()`         | Récupère le statut actuel du stream.                 |

Par exemple, pour générer une URL de publication RTMP avec une expiration de 60 secondes :
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
Cette URL peut être utilisée pour publier des streams vers Pili Streaming Cloud, avec l'expiration assurant un accès temporaire.

#### Considérations Supplémentaires
- **Stabilité de la Version** : La version "dev-master" est la branche de développement, potentiellement instable. Pour la production, envisagez d'utiliser une version taguée, telle que 1.5.5, disponible sur Packagist [versions de pili-engineering/pili-sdk-php](https://packagist.org/p/pili-engineering/pili-sdk-php). L'historique montre des mises à jour comme des ajouts d'API et des améliorations de méthodes, avec des versions remontant à 2016.
- **Gestion des Erreurs** : La documentation suggère d'utiliser des blocs try-catch pour les opérations, comme vu dans les exemples pour la création et la récupération de streams, pour gérer les exceptions potentielles.
- **Documentation et Exemples** : Bien que des exemples spécifiques n'aient pas été largement détaillés, le dépôt GitHub [Bibliothèque côté serveur Pili Streaming Cloud pour PHP](https://github.com/pili-engineering/pili-sdk-php) fournit des instructions d'installation et des listes de fonctionnalités, et des comparaisons avec d'autres SDK de langage (par exemple, Python) indiquent une fonctionnalité similaire, comme la génération d'URL.

#### Perspectives Comparatives
La comparaison avec d'autres SDK Pili, comme la version Python, révèle des modèles similaires : les deux nécessitent des identifiants, une configuration de hub et des opérations sur les streams. La version PHP, cependant, utilise une approche orientée objet avec des classes Hub et Stream, contrastant avec le style plus fonctionnel de Python. Cela correspond aux pratiques de développement typiques de PHP, offrant une sécurité de type et un support IDE.

#### Conclusion
Utiliser "pili-engineering/pili-sdk-php": "dev-master" implique une installation via Composer, la configuration des identifiants Qiniu, la création d'un objet Hub et la gestion des streams avec des méthodes comme `rtmpPublishUrl`. Assurez-vous que votre environnement répond aux exigences PHP 5.3.0+ et considérez la stabilité pour une utilisation en production. Ce guide fournit un point de départ complet, avec plus de détails disponibles dans la documentation officielle et le dépôt.

### Citations Clés
- [Bibliothèque côté serveur Pili Streaming Cloud pour PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [versions de pili-engineering/pili-sdk-php Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)