---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque Cloud Streaming Pili pour PHP
translated: true
---

### Points Clés
- Il semble probable que pour utiliser "pili-engineering/pili-sdk-php": "dev-master", vous devez l'installer via Composer et configurer les informations d'identification Qiniu.
- La recherche suggère que le package nécessite PHP 5.3.0 ou une version supérieure et est destiné à Pili Streaming Cloud, lié à Qiniu.
- Les preuves penchent en faveur de la création d'un objet Hub et de l'utilisation d'opérations de flux comme la génération d'URL RTMP, mais les méthodes exactes peuvent varier.

### Installation
Tout d'abord, assurez-vous que Composer est installé. Ajoutez le package à votre fichier `composer.json` avec :
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
Vous aurez besoin d'un compte Qiniu et d'un Hub Pili. Définissez votre clé d'accès, votre clé secrète et le nom de votre hub, puis créez un objet Hub :
```php
use Qiniu\Credentials;
use Pili\Hub;

$credentials = new Credentials('your_access_key', 'your_secret_key');
$hub = new Hub($credentials, 'your_hub_name');
```
Créez ou obtenez un flux, par exemple, `$stream = $hub->createStream('your_stream_key');`, et utilisez des méthodes comme `$stream->rtmpPublishUrl(60)` pour les opérations.

### Détail Inattendu
Notez que "dev-master" est une version de développement, potentiellement instable, avec des versions taguées comme 1.5.5 disponibles pour la production.

---

### Guide Complet sur l'Utilisation de "pili-engineering/pili-sdk-php": "dev-master"

Ce guide fournit une exploration détaillée de l'utilisation du package "pili-engineering/pili-sdk-php" avec la version "dev-master", basée sur la documentation et les exemples disponibles. Il couvre l'installation, la configuration, l'utilisation et des considérations supplémentaires, assurant une compréhension approfondie pour les développeurs travaillant avec les services Pili Streaming Cloud.

#### Contexte et Contexte
Le package "pili-engineering/pili-sdk-php" est une bibliothèque côté serveur pour PHP, conçue pour interagir avec Pili Streaming Cloud, un service associé à Qiniu, un fournisseur de stockage cloud et CDN. La version "dev-master" fait référence à la branche de développement la plus récente, qui peut inclure des fonctionnalités récentes mais pourrait être moins stable que les versions taguées. Le package nécessite PHP 5.3.0 ou une version supérieure, le rendant accessible pour de nombreux environnements PHP jusqu'au 3 mars 2025.

#### Processus d'Installation
Pour commencer, vous devez avoir Composer installé, un gestionnaire de dépendances pour PHP. L'installation implique d'ajouter le package à votre fichier `composer.json` du projet et d'exécuter une commande Composer pour le télécharger. Plus précisément :

- Ajoutez ce qui suit à votre `composer.json` sous la section "require" :
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

Ce processus assure que le package est intégré à votre projet, tirant parti de l'autochargement de Composer pour un accès facile aux classes.

#### Prérequis et Configuration
Avant d'utiliser le SDK, vous avez besoin d'un compte Qiniu et de configurer un Hub Pili, car le SDK interagit avec les services Pili Streaming Cloud. Cela implique d'obtenir une Clé d'Accès et une Clé Secrète de Qiniu et de créer un hub sur leur plateforme. La documentation suggère que ces informations d'identification sont essentielles pour l'authentification.

Pour configurer, définissez vos informations d'identification dans votre script PHP :
- Clé d'Accès : Votre Clé d'Accès Qiniu.
- Clé Secrète : Votre Clé Secrète Qiniu.
- Nom du Hub : Le nom de votre Hub Pili, qui doit exister avant l'utilisation.

Un exemple de configuration ressemble à ceci :
```php
$accessKey = 'your_access_key';
$secretKey = 'your_secret_key';
$hubName = 'your_hub_name';
```

#### Création et Utilisation de l'Objet Hub
Le cœur du SDK est l'objet Hub, qui facilite la gestion des flux. Tout d'abord, créez un objet Credentials en utilisant vos clés Qiniu :
```php
use Qiniu\Credentials;

$credentials = new Credentials($accessKey, $secretKey);
```
Ensuite, instanciez un objet Hub avec ces informations d'identification et le nom de votre hub :
```php
use Pili\Hub;

$hub = new Hub($credentials, $hubName);
```
Cet objet Hub vous permet de réaliser diverses opérations liées aux flux, telles que la création, la récupération ou la liste des flux.

#### Travail avec les Flux
Les flux sont centraux pour Pili Streaming Cloud, et le SDK fournit des méthodes pour les gérer via l'objet Hub. Pour créer un nouveau flux :
```php
$streamKey = 'your_stream_key'; // Doit être unique dans le hub
$stream = $hub->createStream($streamKey);
```
Pour récupérer un flux existant :
```php
$stream = $hub->getStream($streamKey);
```
L'objet flux offre ensuite diverses méthodes pour les opérations, détaillées dans le tableau suivant basé sur la documentation disponible :

| **Opération**          | **Méthode**                     | **Description**                                      |
|-------------------------|--------------------------------|------------------------------------------------------|
| Créer un Flux          | `$hub->createStream($key)`     | Crée un nouveau flux avec la clé donnée.             |
| Obtenir un Flux        | `$hub->getStream($key)`        | Récupère un flux existant par clé.                 |
| Lister les Flux        | `$hub->listStreams($marker, $limit, $prefix)` | Liste les flux avec des options de pagination.               |
| URL de Publication RTMP| `$stream->rtmpPublishUrl($expire)` | Génère une URL de publication RTMP avec un temps d'expiration.  |
| URL de Lecture RTMP    | `$stream->rtmpPlayUrl()`       | Génère une URL de lecture RTMP pour le flux.           |
| URL de Lecture HLS     | `$stream->hlsPlayUrl()`        | Génère une URL de lecture HLS pour le streaming.             |
| Désactiver le Flux     | `$stream->disable()`           | Désactive le flux.                                 |
| Activer le Flux        | `$stream->enable()`            | Active le flux.                                  |
| Statut du Flux         | `$stream->status()`            | Récupère le statut actuel du flux.          |

Par exemple, pour générer une URL de publication RTMP avec une expiration de 60 secondes :
```php
$expire = 60;
$url = $stream->rtmpPublishUrl($expire);
echo $url;
```
Cette URL peut être utilisée pour publier des flux vers Pili Streaming Cloud, l'expiration assurant un accès temporaire.

#### Considérations Supplémentaires
- **Stabilité de la Version** : La version "dev-master" est la branche de développement, potentiellement instable. Pour la production, envisagez d'utiliser une version taguée, telle que 1.5.5, disponible sur Packagist [pili-engineering/pili-sdk-php versions](https://packagist.org/p/pili-engineering/pili-sdk-php). L'historique montre des mises à jour comme des additions d'API et des raffinements de méthodes, avec des versions remontant à 2016.
- **Gestion des Erreurs** : La documentation suggère d'utiliser des blocs try-catch pour les opérations, comme vu dans les exemples de création et de récupération de flux, pour gérer les exceptions potentielles.
- **Documentation et Exemples** : Bien que des exemples spécifiques n'aient pas été détaillés de manière exhaustive, le dépôt GitHub [Pili Streaming Cloud server-side library for PHP](https://github.com/pili-engineering/pili-sdk-php) fournit des instructions d'installation et des listes de fonctionnalités, et des comparaisons avec d'autres SDK de langage (par exemple, Python) indiquent une fonctionnalité similaire, telle que la génération d'URL.

#### Perspectives Comparatives
Comparé à d'autres SDK Pili, comme la version Python, des motifs similaires apparaissent : tous nécessitent des informations d'identification, une configuration de hub et des opérations de flux. La version PHP, cependant, utilise une approche orientée objet avec des classes Hub et Stream, contrastant avec le style plus fonctionnel de Python. Cela s'aligne avec les pratiques de développement typiques de PHP, offrant une sécurité de type et un support IDE.

#### Conclusion
L'utilisation de "pili-engineering/pili-sdk-php": "dev-master" implique l'installation via Composer, la configuration des informations d'identification Qiniu, la création d'un objet Hub et la gestion des flux avec des méthodes comme `rtmpPublishUrl`. Assurez-vous que votre environnement répond aux exigences PHP 5.3.0+ et envisagez la stabilité pour une utilisation en production. Ce guide fournit un point de départ complet, avec des détails supplémentaires disponibles dans la documentation officielle et le dépôt.

### Citations Clés
- [Pili Streaming Cloud server-side library for PHP GitHub](https://github.com/pili-engineering/pili-sdk-php)
- [pili-engineering/pili-sdk-php versions Packagist](https://packagist.org/p/pili-engineering/pili-sdk-php)