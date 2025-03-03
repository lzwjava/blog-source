---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser RabbitMQ en PHP
translated: true
---

### Points Clés
- Il semble probable que pour utiliser "php-amqplib/php-amqplib" version 2.6.*, il faille l'installer via Composer et suivre les étapes de base pour envoyer et recevoir des messages avec RabbitMQ.
- Le processus implique la configuration d'une connexion, la déclaration d'une file d'attente et l'utilisation de méthodes comme `basic_publish` pour l'envoi et `basic_consume` avec une boucle pour la réception, ce qui peut légèrement différer des versions plus récentes.
- La recherche suggère que pour la version 2.6.*, le processus de consommation nécessite une boucle manuelle avec `wait()`, contrairement aux versions plus récentes qui pourraient utiliser une méthode `consume()`.

---

### Installation et Configuration
Pour commencer avec "php-amqplib/php-amqplib" version 2.6.*, installez-le d'abord en utilisant Composer en exécutant :

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Assurez-vous que RabbitMQ est installé et en cours d'exécution sur votre système, généralement accessible à `localhost:5672` avec les identifiants par défaut (`guest/guest`). Ajustez ces paramètres si votre configuration diffère.

### Envoi de Messages
Pour envoyer un message, incluez les fichiers PHP nécessaires et créez une connexion :

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;
use PhpAmqpLib\Message\AMQPMessage;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
```

Déclarez une file d'attente et publiez votre message :

```php
$channel->queue_declare('hello', false, false, false, false);
$msg = new AMQPMessage('Hello World!');
$channel->basic_publish($msg, '', 'hello');
echo " [x] Sent 'Hello World!'\n";
```

Enfin, fermez la connexion :

```php
$channel->close();
$connection->close();
```

### Réception de Messages
Pour la réception, configurez de manière similaire mais définissez un rappel pour le traitement des messages :

```php
require_once __DIR__ . '/vendor/autoload.php';
use PhpAmqpLib\Connection\AMQPStreamConnection;

$connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
$channel = $connection->channel();
$channel->queue_declare('hello', false, false, false, false);

$callback = function ($msg) {
    echo ' [x] Received ', $msg->body, "\n";
};

$channel->basic_consume('hello', '', false, true, false, false, $callback);
while (count($channel->callbacks)) {
    $channel->wait();
}

$channel->close();
$connection->close();
```

Notez que pour la version 2.6.*, vous avez besoin de la boucle avec `wait()` pour continuer à consommer, ce qui est un détail inattendu par rapport aux versions plus récentes qui pourraient utiliser une méthode `consume()` plus simple.

---

### Note de l'Enquête : Utilisation Détaillée de "php-amqplib/php-amqplib" Version 2.6.*

Cette section fournit un guide complet sur l'utilisation de la bibliothèque "php-amqplib/php-amqplib", spécifiquement la version 2.6.*, pour interagir avec RabbitMQ, un système de file d'attente de messages populaire. Les informations sont dérivées de la documentation officielle, des tutoriels et des détails spécifiques à la version, assurant une compréhension approfondie pour les développeurs.

#### Contexte et Contexte
"php-amqplib/php-amqplib" est une bibliothèque PHP pour communiquer avec RabbitMQ, implémentant le protocole AMQP 0.9.1. La version 2.6.* est une version plus ancienne, et bien que la bibliothèque ait évolué vers la version 3.x.x en mars 2025, comprendre son utilisation dans cette version spécifique est crucial pour les systèmes hérités ou des exigences de projet spécifiques. La bibliothèque est maintenue par des contributeurs incluant Ramūnas Dronga et Luke Bakken, avec une implication significative des ingénieurs VMware travaillant sur RabbitMQ ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

Les tutoriels RabbitMQ, tels que ceux sur le site officiel de RabbitMQ, fournissent des exemples généralement applicables mais peuvent refléter des versions plus récentes. Pour la version 2.6.*, des ajustements sont nécessaires, en particulier dans le processus de consommation, comme détaillé ci-dessous.

#### Processus d'Installation
Pour commencer, installez la bibliothèque en utilisant Composer, le gestionnaire de dépendances PHP. Exécutez la commande suivante dans votre répertoire de projet :

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Cette commande assure que la bibliothèque est téléchargée et configurée pour une utilisation, avec Composer gérant les dépendances. Assurez-vous que RabbitMQ est installé et en cours d'exécution, généralement accessible à `localhost:5672` avec les identifiants par défaut (`guest/guest`). Pour la production, ajustez l'hôte, le port et les identifiants si nécessaire, et consultez [CloudAMQP PHP Documentation](https://www.cloudamqp.com/docs/php.html) pour les configurations de courtier gérées.

#### Envoi de Messages : Étape par Étape
L'envoi de messages implique l'établissement d'une connexion et la publication dans une file d'attente. Voici le processus :

1. **Inclure les Fichiers Nécessaires :**
   Utilisez l'auto-chargeur Composer pour inclure la bibliothèque :

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   use PhpAmqpLib\Message\AMQPMessage;
   ```

2. **Créer une Connexion et un Canal :**
   Initialisez une connexion à RabbitMQ et ouvrez un canal :

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

   Les paramètres sont l'hôte, le port, le nom d'utilisateur et le mot de passe, avec les valeurs par défaut comme montré. Pour SSL ou d'autres configurations, référez-vous à [RabbitMQ PHP Tutorial](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **Déclarer la File d'Attente et Publier :**
   Déclarez une file d'attente pour vous assurer qu'elle existe, puis publiez un message :

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   Ici, `queue_declare` crée une file d'attente nommée 'hello' avec les paramètres par défaut (non durable, non exclusif, auto-suppression). `basic_publish` envoie le message à la file d'attente.

4. **Fermer la Connexion :**
   Après l'envoi, fermez le canal et la connexion pour libérer les ressources :

   ```php
   $channel->close();
   $connection->close();
   ```

Ce processus est standard à travers les versions, sans changements significatifs notés dans le journal des modifications pour la version 2.6.* par rapport aux versions ultérieures.

#### Réception de Messages : Détails Spécifiques à la Version
La réception de messages dans la version 2.6.* nécessite une attention particulière, car le mécanisme de consommation diffère des versions plus récentes. Voici le processus détaillé :

1. **Inclure les Fichiers Nécessaires :**
   De manière similaire à l'envoi, incluez l'auto-chargeur et les classes nécessaires :

   ```php
   require_once __DIR__ . '/vendor/autoload.php';
   use PhpAmqpLib\Connection\AMQPStreamConnection;
   ```

2. **Créer une Connexion et un Canal :**
   Établissez la connexion et le canal comme précédemment :

   ```php
   $connection = new AMQPStreamConnection('localhost', 5672, 'guest', 'guest');
   $channel = $connection->channel();
   ```

3. **Déclarer la File d'Attente :**
   Assurez-vous que la file d'attente existe, correspondant à la déclaration de l'expéditeur :

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   ```

4. **Définir un Rappel :**
   Créez une fonction de rappel pour traiter les messages reçus :

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   Cette fonction sera appelée pour chaque message, imprimant le corps dans cet exemple.

5. **Consommer les Messages :**
   Pour la version 2.6.*, utilisez `basic_consume` pour enregistrer le rappel, puis entrez dans une boucle pour continuer à consommer :

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   La méthode `basic_consume` prend des paramètres pour le nom de la file d'attente, l'étiquette du consommateur, no-local, no-ack, exclusif, no-wait et rappel. La boucle avec `wait()` garde le consommateur en cours d'exécution, vérifiant les messages. C'est un détail important, car les versions plus récentes (par exemple, 3.2) pourraient utiliser une méthode `consume()`, qui n'était pas disponible dans 2.6.* selon la revue de la documentation de l'API.

6. **Fermer la Connexion :**
   Après la consommation, fermez les ressources :

   ```php
   $channel->close();
   $connection->close();
   ```

Un détail inattendu est le besoin de la boucle manuelle dans la version 2.6.*, qui pourrait nécessiter un traitement supplémentaire des erreurs pour une utilisation en production, comme la capture des exceptions pour les problèmes de connexion.

#### Considérations Spécifiques à la Version
La version 2.6.* fait partie des versions plus anciennes, et bien que le journal des modifications ne l'énumère pas explicitement, les versions autour de 2.5 à 2.7 montrent des améliorations comme le support de heartbeat et la compatibilité avec PHP 5.3. Pour les grands messages, la version 2.6.* prend en charge `setBodySizeLimit` sur le canal pour gérer les limites de mémoire, tronquant les messages si nécessaire, avec des détails dans [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

En comparaison avec la version 3.2, les changements incluent le support de PHP 8 et de nouvelles méthodes comme `consume()`, mais la fonctionnalité de base pour l'envoi et la consommation de base reste similaire. Les utilisateurs doivent tester la compatibilité, en particulier avec les versions de PHP, car 2.6.* prend probablement en charge PHP 5.3 à 7.x, selon les entrées du journal des modifications.

#### Dépannage et Meilleures Pratiques
- Si l'envoi échoue, vérifiez les journaux RabbitMQ pour les alarmes de ressources, telles que l'espace disque en dessous de 50 Mo, et ajustez les paramètres via [RabbitMQ Configuration Guide](https://www.rabbitmq.com/configure.html#config-items).
- Pour la consommation, assurez-vous que le consommateur s'exécute en continu ; utilisez des outils comme Supervisor pour la démonisation en production.
- Listez les files d'attente en utilisant `rabbitmqctl list_queues` sur Linux ou `rabbitmqctl.bat list_queues` sur Windows en tant qu'utilisateur privilégié, selon [RabbitMQ Command Line Tools](https://www.rabbitmq.com/cli.html).

#### Tableau : Comparaison des Versions pour les Méthodes Clés

| Méthode             | Comportement Version 2.6.*                          | Comportement Version 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | Standard, publie dans la file d'attente                    | Inchangé, même utilisation                        |
| `basic_consume`    | Nécessite une boucle avec `wait()` pour la consommation       | Similaire, mais méthode `consume()` disponible     |
| `setBodySizeLimit` | Pris en charge pour les grands messages, tronque si défini | Pris en charge, même fonctionnalité                |
| Compatibilité PHP  | Probablement 5.3 à 7.x                               | Prend en charge PHP 7.x et 8.x                     |

Ce tableau met en évidence la différence clé dans la consommation, qui est cruciale pour les utilisateurs de la version 2.6.*.

#### Conclusion
L'utilisation de "php-amqplib/php-amqplib" version 2.6.* implique une installation standard de Composer, avec l'envoi de messages via `basic_publish` et la réception via `basic_consume` avec une boucle manuelle. Bien que similaire aux versions plus récentes, le processus de consommation nécessite une attention supplémentaire, rendant essentiel pour les développeurs de tester et d'ajuster pour les systèmes hérités. Pour plus de détails, consultez les tutoriels officiels RabbitMQ et le dépôt GitHub.

---

### Citations Clés
- [GitHub - php-amqplib/php-amqplib Le client PHP le plus largement utilisé pour RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [Tutoriel RabbitMQ - Exemple "Hello World!" PHP](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [Documentation CloudAMQP PHP Commencez avec CloudAMQP et PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Anciennement videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib Fichier CHANGELOG](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [Guide de Configuration RabbitMQ Éléments de configuration et paramètres](https://www.rabbitmq.com/configure.html#config-items)
- [Outils en Ligne de Commande RabbitMQ Référence et utilisation CLI](https://www.rabbitmq.com/cli.html)