---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser RabbitMQ en PHP
translated: true
type: note
---

### Points Clés
- Il semble probable que pour utiliser "php-amqplib/php-amqplib" version 2.6.*, vous devez l'installer via Composer et suivre les étapes de base pour envoyer et recevoir des messages avec RabbitMQ.
- Le processus implique d'établir une connexion, de déclarer une file d'attente et d'utiliser des méthodes comme `basic_publish` pour l'envoi et `basic_consume` avec une boucle pour la réception, ce qui peut différer légèrement des versions plus récentes.
- Les recherches suggèrent que pour la version 2.6.*, le processus de consommation nécessite une boucle manuelle avec `wait()`, contrairement aux versions plus récentes qui pourraient utiliser une méthode `consume()`.

---

### Installation et Configuration
Pour commencer avec "php-amqplib/php-amqplib" version 2.6.*, installez-le d'abord en utilisant Composer en exécutant :

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Assurez-vous que RabbitMQ est installé et fonctionne sur votre système, généralement accessible à `localhost:5672` avec les identifiants par défaut (`guest/guest`). Ajustez ces paramètres si votre configuration est différente.

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
Pour la réception, configurez de manière similaire mais définissez une fonction de rappel pour le traitement des messages :

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

### Note d'Enquête : Utilisation Détaillée de "php-amqplib/php-amqplib" Version 2.6.*

Cette section fournit un guide complet sur l'utilisation de la bibliothèque "php-amqplib/php-amqplib", spécifiquement la version 2.6.*, pour interagir avec RabbitMQ, un système de file d'attente de messages populaire. Les informations proviennent de la documentation officielle, de tutoriels et de détails spécifiques à la version, assurant une compréhension approfondie pour les développeurs.

#### Contexte
"php-amqplib/php-amqplib" est une bibliothèque PHP pour communiquer avec RabbitMQ, implémentant le protocole AMQP 0.9.1. La version 2.6.* est une version plus ancienne, et bien que la bibliothèque ait évolué vers la version 3.x.x en mars 2025, comprendre son utilisation dans cette version spécifique est crucial pour les systèmes hérités ou les besoins projet spécifiques. La bibliothèque est maintenue par des contributeurs incluant Ramūnas Dronga et Luke Bakken, avec une implication significative d'ingénieurs VMware travaillant sur RabbitMQ ([GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib)).

Les tutoriels RabbitMQ, comme ceux sur le site officiel de RabbitMQ, fournissent des exemples généralement applicables mais peuvent refléter des versions plus récentes. Pour la version 2.6.*, des ajustements sont nécessaires, particulièrement dans le processus de consommation, comme détaillé ci-dessous.

#### Processus d'Installation
Pour commencer, installez la bibliothèque en utilisant Composer, le gestionnaire de dépendances PHP. Exécutez la commande suivante dans votre répertoire de projet :

```bash
composer require "php-amqplib/php-amqplib:2.6.*"
```

Cette commande assure que la bibliothèque est téléchargée et configurée pour utilisation, avec Composer gérant les dépendances. Assurez-vous que RabbitMQ est installé et fonctionne, généralement accessible à `localhost:5672` avec les identifiants par défaut (`guest/guest`). Pour la production, ajustez l'hôte, le port et les identifiants si nécessaire, et consultez la [Documentation CloudAMQP PHP](https://www.cloudamqp.com/docs/php.html) pour les configurations de broker managé.

#### Envoi de Messages : Étapes Détaillées
L'envoi de messages implique d'établir une connexion et de publier dans une file d'attente. Voici le processus :

1. **Inclure les Fichiers Requis :**
   Utilisez l'autoloader de Composer pour inclure la bibliothèque :

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

   Les paramètres sont l'hôte, le port, le nom d'utilisateur et le mot de passe, avec les valeurs par défaut comme indiqué. Pour les configurations SSL ou autres, référez-vous au [Tutoriel PHP RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-php).

3. **Déclarer la File d'Attente et Publier :**
   Déclarez une file d'attente pour vous assurer de son existence, puis publiez un message :

   ```php
   $channel->queue_declare('hello', false, false, false, false);
   $msg = new AMQPMessage('Hello World!');
   $channel->basic_publish($msg, '', 'hello');
   echo " [x] Sent 'Hello World!'\n";
   ```

   Ici, `queue_declare` crée une file d'attente nommée 'hello' avec les paramètres par défaut (non durable, non exclusive, auto-suppression). `basic_publish` envoie le message à la file d'attente.

4. **Fermer la Connexion :**
   Après l'envoi, fermez le canal et la connexion pour libérer les ressources :

   ```php
   $channel->close();
   $connection->close();
   ```

Ce processus est standard à travers les versions, sans changement significatif noté dans le journal des modifications pour la version 2.6.* par rapport aux versions ultérieures.

#### Réception de Messages : Détails Spécifiques à la Version
La réception de messages dans la version 2.6.* nécessite une attention particulière, car le mécanisme de consommation diffère des versions plus récentes. Voici le processus détaillé :

1. **Inclure les Fichiers Requis :**
   Similaire à l'envoi, incluez l'autoloader et les classes nécessaires :

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

4. **Définir la Fonction de Rappel :**
   Créez une fonction de rappel pour traiter les messages reçus :

   ```php
   $callback = function ($msg) {
       echo ' [x] Received ', $msg->body, "\n";
   };
   ```

   Cette fonction sera appelée pour chaque message, affichant le corps dans cet exemple.

5. **Consommer les Messages :**
   Pour la version 2.6.*, utilisez `basic_consume` pour enregistrer la fonction de rappel, puis entrez dans une boucle pour continuer à consommer :

   ```php
   $channel->basic_consume('hello', '', false, true, false, false, $callback);
   while (count($channel->callbacks)) {
       $channel->wait();
   }
   ```

   La méthode `basic_consume` prend des paramètres pour le nom de la file d'attente, l'étiquette du consommateur, no-local, no-ack, exclusif, no-wait et la fonction de rappel. La boucle avec `wait()` maintient le consommateur actif, vérifiant les messages. C'est un détail important, car les versions plus récentes (par exemple, 3.2) pourraient utiliser une méthode `consume()`, qui n'était pas disponible dans la version 2.6.* selon l'examen de la documentation de l'API.

6. **Fermer la Connexion :**
   Après consommation, fermez les ressources :

   ```php
   $channel->close();
   $connection->close();
   ```

Un détail inattendu est le besoin de la boucle manuelle dans la version 2.6.*, ce qui peut nécessiter une gestion d'erreur supplémentaire pour une utilisation en production, comme la capture d'exceptions pour les problèmes de connexion.

#### Considérations Spécifiques à la Version
La version 2.6.* fait partie des versions plus anciennes, et bien que le journal des modifications ne la liste pas explicitement, les versions autour de 2.5 à 2.7 montrent des améliorations comme le support des battements de cœur et la compatibilité PHP 5.3. Pour les messages volumineux, la version 2.6.* supporte `setBodySizeLimit` sur le canal pour gérer les limites de mémoire, tronquant les messages si nécessaire, avec des détails dans [GitHub - php-amqplib/php-amqplib](https://github.com/php-amqplib/php-amqplib).

En comparaison avec la version 3.2, les changements incluent le support de PHP 8 et de nouvelles méthodes comme `consume()`, mais la fonctionnalité de base pour l'envoi et la consommation de base reste similaire. Les utilisateurs doivent tester pour la compatibilité, surtout avec les versions de PHP, car la version 2.6.* supporte probablement PHP 5.3 à 7.x, selon les entrées du journal des modifications.

#### Dépannage et Bonnes Pratiques
- Si l'envoi échoue, vérifiez les journaux RabbitMQ pour les alarmes de ressources, comme l'espace disque en dessous de 50 Mo, et ajustez les paramètres via le [Guide de Configuration RabbitMQ](https://www.rabbitmq.com/configure.html#config-items).
- Pour la consommation, assurez-vous que le consommateur fonctionne continuellement ; utilisez des outils comme Supervisor pour le démoniser en production.
- Listez les files d'attente en utilisant `rabbitmqctl list_queues` sur Linux ou `rabbitmqctl.bat list_queues` sur Windows en tant qu'utilisateur privilégié, selon les [Outils en Ligne de Commande RabbitMQ](https://www.rabbitmq.com/cli.html).

#### Tableau : Comparaison des Versions pour les Méthodes Clés

| Méthode             | Comportement Version 2.6.*                          | Comportement Version 3.2                          |
|--------------------|------------------------------------------------|----------------------------------------------|
| `basic_publish`    | Standard, publie dans la file d'attente                    | Inchangé, même utilisation                        |
| `basic_consume`    | Nécessite une boucle avec `wait()` pour la consommation       | Similaire, mais méthode `consume()` disponible     |
| `setBodySizeLimit` | Supporté pour les messages volumineux, tronque si défini | Supporté, même fonctionnalité                |
| Compatibilité PHP  | Probablement 5.3 à 7.x                               | Supporte PHP 7.x et 8.x                     |

Ce tableau met en évidence la différence clé dans la consommation, ce qui est critique pour les utilisateurs de la version 2.6.*.

#### Conclusion
Utiliser "php-amqplib/php-amqplib" version 2.6.* implique une installation standard via Composer, avec l'envoi de messages via `basic_publish` et la réception via `basic_consume` avec une boucle manuelle. Bien que similaire aux versions plus récentes, le processus de consommation nécessite une attention supplémentaire, ce qui est essentiel pour les développeurs afin de tester et ajuster pour les systèmes hérités. Pour plus de détails, consultez les tutoriels officiels RabbitMQ et le dépôt GitHub.

---

### Citations Clés
- [GitHub - php-amqplib/php-amqplib Le client PHP le plus utilisé pour RabbitMQ](https://github.com/php-amqplib/php-amqplib)
- [Tutoriel RabbitMQ - Exemple PHP "Hello World!"](https://www.rabbitmq.com/tutorials/tutorial-one-php)
- [Documentation CloudAMQP PHP Commencer avec CloudAMQP et PHP](https://www.cloudamqp.com/docs/php.html)
- [php-amqplib/php-amqplib Packagist Anciennement videlalvaro/php-amqplib](https://packagist.org/packages/php-amqplib/php-amqplib)
- [GitHub - php-amqplib/php-amqplib Fichier CHANGELOG](https://github.com/php-amqplib/php-amqplib/blob/master/CHANGELOG.md)
- [Guide de Configuration RabbitMQ Éléments de configuration et paramètres](https://www.rabbitmq.com/configure.html#config-items)
- [Outils en Ligne de Commande RabbitMQ Référence et utilisation CLI](https://www.rabbitmq.com/cli.html)