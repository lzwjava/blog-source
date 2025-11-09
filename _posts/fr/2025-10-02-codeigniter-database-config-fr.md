---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Vue d'ensemble de la configuration de la base de données CodeIgniter
translated: true
type: note
---

### Aperçu de la configuration de base de données CodeIgniter

Ce fichier PHP est un script de configuration pour la connectivité de base de données de CodeIgniter. Il définit les paramètres de connexion pour différents groupes de base de données (par exemple, 'default', 'lzwjava', 'leo66', 'testing'), permettant à l'application de basculer entre eux en fonction de l'environnement (développement, test, production). La variable `$active_group` détermine quel groupe de connexion est utilisé par défaut.

Composants clés :
- **$query_builder** : Défini sur `TRUE` pour activer le chargement de la classe Query Builder, qui fournit une manière orientée objet de construire des requêtes SQL.
- **$db[][]** : Un tableau associatif où chaque sous-tableau (par exemple, 'default') contient les options de configuration détaillées pour une connexion à la base de données.

La variable `$active_group` est définie dynamiquement en fonction de la constante `ENVIRONMENT` (par exemple, via une instruction switch), garantissant ainsi des paramètres différents pour les différentes étapes de déploiement. Ci-dessous, j'expliquerai chaque option de configuration en détail, en m'appuyant sur la documentation de CodeIgniter et l'utilisation standard. Notez que les valeurs sensibles réelles (comme les identifiants) sont omises ici pour des raisons de sécurité ; en pratique, elles doivent être stockées de manière sécurisée, par exemple via des variables d'environnement.

### Options de configuration détaillées

Chaque groupe de base de données est un tableau avec les clés suivantes. La plupart sont des paramètres simples, mais certains (comme `encrypt`) prennent en charge des sous-options pour des fonctionnalités avancées.

- **dsn** (string) : La chaîne Data Source Name (DSN) complète décrivant la connexion. C'est une alternative à la spécification séparée du hostname, du username, etc. Elle est utile pour des configurations complexes comme ODBC. Si elle est fournie, elle remplace les champs individuels host/credentials. Format d'exemple : `'dsn' => 'mysql:host=yourhost;dbname=yourdatabase'`.

- **hostname** (string) : L'adresse du serveur de base de données (par exemple, 'localhost' ou une IP comme '127.0.0.1'). Cela identifie l'emplacement d'exécution de la base de données, permettant des connexions via TCP/IP ou sockets.

- **username** (string) : Le nom du compte utilisé pour s'authentifier auprès du serveur de base de données. Il doit correspondre à un utilisateur valide dans le système de gestion de base de données.

- **password** (string) : La clé secrète associée au nom d'utilisateur pour l'authentification. Stockez-la toujours de manière sécurisée pour éviter son exposition.

- **database** (string) : Le nom spécifique de la base de données à laquelle vous souhaitez vous connecter sur le serveur. Toutes les requêtes cibleront cette base de données sauf indication contraire.

- **dbdriver** (string) : Spécifie le pilote de base de données à utiliser (par exemple, 'mysqli' pour MySQL). Les pilotes courants incluent 'cubrid', 'ibase', 'mssql', 'mysql', 'mysqli', 'oci8', 'odbc', 'pdo', 'postgre', 'sqlite', 'sqlite3', et 'sqlsrv'. 'mysqli' est un choix moderne et sécurisé pour MySQL.

- **dbprefix** (string) : Un préfixe optionnel ajouté aux noms de table lors de l'utilisation du Query Builder de CodeIgniter (par exemple, s'il est défini sur 'prefix_', 'mytable' devient 'prefix_mytable'). Cela aide à namespacer les tables dans un hébergement partagé ou des applications multi-locataires.

- **pconnect** (boolean) : Active les connexions persistantes (`TRUE`) ou les connexions régulières (`FALSE`). Les connexions persistantes réutilisent le même lien, améliorant les performances pour les applications à forte charge, mais elles peuvent épuiser les ressources du serveur si elles sont trop utilisées.

- **db_debug** (boolean) : Contrôle si les erreurs de base de données sont affichées (`TRUE`) pour le débogage. Désactivez (`FALSE`) en production pour éviter de divulguer des détails d'erreur sensibles aux utilisateurs.

- **cache_on** (boolean) : Active (`TRUE`) ou désactive (`FALSE`) la mise en cache des requêtes. Lorsqu'elle est activée, les résultats sont stockés pour accélérer les requêtes répétées.

- **cachedir** (string) : Chemin d'accès au répertoire où les résultats de requêtes mis en cache sont stockés. Doit être accessible en écriture par le serveur web. Combiné avec `cache_on`, cela réduit la charge sur la base de données.

- **char_set** (string) : L'encodage des caractères pour la communication avec la base de données (par exemple, 'utf8mb4' pour une prise en charge Unicode moderne). Garantit l'intégrité des données pour les applications multilingues.

- **dbcollat** (string) : La collation pour le tri et la comparaison des caractères (par exemple, 'utf8mb4_unicode_ci' pour Unicode insensible à la casse). Cela fonctionne comme une solution de secours pour les anciennes versions de PHP/MySQL ; ignoré autrement.

- **swap_pre** (string) : Un préfixe de table pour remplacer dynamiquement `dbprefix`. Utile pour échanger les préfixes dans les applications existantes sans renommer les tables.

- **encrypt** (boolean ou array) : Pour la prise en charge du chiffrement. Pour 'mysql' (obsolète), 'sqlsrv', et 'pdo/sqlsrv', utilisez `TRUE`/`FALSE` pour activer/désactiver SSL. Pour 'mysqli' et 'pdo/mysql', utilisez un tableau avec des sous-options SSL :
  - 'ssl_key' : Chemin d'accès au fichier de clé privée (par exemple, pour les certificats clients).
  - 'ssl_cert' : Chemin d'accès au fichier de certificat de clé publique.
  - 'ssl_ca' : Chemin d'accès au fichier de l'autorité de certification (valide le certificat du serveur).
  - 'ssl_capath' : Chemin d'accès à un répertoire de certificats CA de confiance au format PEM.
  - 'ssl_cipher' : Liste des chiffrements autorisés séparés par des deux-points (par exemple, 'AES128-SHA').
  - 'ssl_verify' : Pour 'mysqli' uniquement ; `TRUE` pour vérifier les certificats du serveur, `FALSE` pour ignorer (moins sécurisé ; à utiliser pour les certificats auto-signés).

- **compress** (boolean) : Active la compression côté client pour les connexions MySQL, réduisant le trafic réseau (MySQL uniquement ; ignoré par les autres pilotes).

- **stricton** (boolean) : Force les connexions en 'Mode Strict' (`TRUE`), qui applique des règles SQL strictes pour détecter les erreurs plus tôt (par exemple, types de données invalides). Utile pendant le développement.

- **ssl_options** (array) : Options de configuration SSL avancées pour les pilotes comme 'pdo'. Permet un réglage fin des paramètres de chiffrement non couverts par `encrypt`.

- **failover** (array) : Tableau de connexions de secours pour une commutation automatique si la connexion principale échoue. Chaque élément reflète la configuration principale (par exemple, hostname/port alternatif). Exemple : `array(array('hostname' => 'backuphost', ...))`.

- **save_queries** (boolean) : Sauvegarde les requêtes exécutées en mémoire pour le débogage (`TRUE`). Fournit un accès à des méthodes comme `$this->db->last_query()` mais peut augmenter l'utilisation de la mémoire ; désactivez (`FALSE`) en production pour économiser les ressources.

### Groupes de base de données et commutation d'environnement

- **default** : Le tableau de configuration de base, servant de modèle. Il est défini sur les valeurs par défaut de 'production' (par exemple, pas de débogage, paramètres sécurisés).
- **lzwjava** : Hérite de la base mais remplace le nom d'utilisateur par une valeur différente (mot de passe laissé vide, impliquant aucune authentification ou valeur par défaut).
- **leo66** : Hérite des paramètres de base mais change le hostname en boucle locale, le username/password en valeurs par défaut, et ajoute un port (3306, standard pour MySQL).
- **testing** : Un groupe dédié pour les environnements de test ; hérite de la configuration de base.

L'instruction `switch` active le groupe approprié en fonction de `ENVIRONMENT` :
- Développement : Utilise 'lzwjava'.
- Test : Utilise 'testing'.
- Production : Utilise 'default'.

Cette configuration favorise la flexibilité pour le développement local, les tests et les déploiements en direct. Sanitisez toujours les entrées pour prévenir les injections SQL, et envisagez de déplacer les identifiants vers des variables d'environnement pour plus de sécurité. Pour la documentation complète, reportez-vous au Guide de l'utilisateur officiel de CodeIgniter sur les connexions à la base de données. Si vous avez une option ou un groupe spécifique à clarifier, faites-le moi savoir !