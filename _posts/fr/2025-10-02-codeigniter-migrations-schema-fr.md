---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Gestion du Schéma de Base de Données avec les Migrations CodeIgniter
translated: true
type: note
---

### Que sont les migrations CodeIgniter ?

Les migrations CodeIgniter (CI) sont une fonctionnalité qui aide à gérer les modifications du schéma de base de données de manière versionnée, de façon similaire à des outils comme Flyway ou Liquibase. Elles vous permettent d'écrire des scripts PHP qui définissent des altérations de la base de données (par exemple, créer des tables, ajouter des colonnes ou modifier des données), puis de les exécuter en séquence pour maintenir votre schéma à jour dans tous les environnements. Cela permet d'éviter les erreurs SQL manuelles et prend en charge la restauration.

Les migrations fonctionnent en :
- Stockant les fichiers de migration dans un répertoire (par défaut : `application/migrations/`).
- Suivant les "versions" dans une table de base de données pour savoir quelles migrations ont été appliquées.
- Exécutant les scripts en avant (up) ou en arrière (down) selon vos besoins.

Le fichier de configuration que vous avez partagé (`migration.php`) contrôle le comportement des migrations. Il utilise des tableaux PHP pour définir les options. Ci-dessous, j'expliquerai les paramètres clés avec des exemples.

### Paramètres de configuration clés

| Paramètre | Valeur dans votre code | Explication | Fonctionnement |
|-----------|------------------------|-------------|----------------|
| `migration_enabled` | `FALSE` | Active ou désactive les migrations globalement. Lorsque `FALSE`, vous ne pouvez pas exécuter de migrations (pour des raisons de sécurité, car elles modifient la base de données). | CI vérifie ce paramètre avant d'exécuter toute commande de migration. Définissez sur `TRUE` pendant le développement, puis remettez sur `FALSE` en production. Exemple : Si activé, exécutez via `$this->migration->current()` dans un contrôleur. |
| `migration_type` | `'timestamp'` | Style de nommage des fichiers : `'sequential'` (ex. `001_add_blog.php`) ou `'timestamp'` (ex. `20121031104401_add_blog.php`). L'horodatage est recommandé pour un meilleur contrôle de version. | Les fichiers sont chargés dans l'ordre chronologique. L'horodatage utilise le format `AAAAMMJJHHMMSS` (ex. `20121031104401` pour le 31 octobre 2012, 10:44:01). |
| `migration_table` | `'migrations'` | Nom de la table de base de données qui suit les migrations appliquées. Requis. | CI crée cette table si elle n'existe pas. Elle stocke la version de migration la plus récente. Supprimer ou mettre à jour cette table réinitialise l'historique des migrations. |
| `migration_auto_latest` | `FALSE` | Si `TRUE` et que `migration_enabled` est `TRUE`, exécute automatiquement les migrations vers la dernière version lorsque la bibliothèque Migration se charge (ex. au chargement de la page). | Utile pour les environnements de développement afin de synchroniser automatiquement les schémas. Définissez sur `FALSE` pour exécuter les migrations manuellement pour plus de contrôle (plus sûr en production). |
| `migration_version` | `0` | La version/cible vers laquelle migrer. Définissez-la sur le préfixe du nom de fichier (ex. `20121031104401`). `0` signifie qu'aucune migration n'a été appliquée. | Exécuter `$this->migration->version(20121031104401)` migre jusqu'à ce point. Utilisé pour des restaurations ciblées — les nombres négatifs rétrogradent. |
| `migration_path` | `APPPATH.'migrations/'` | Répertoire où les fichiers de migration sont stockés. `APPPATH` est une constante CI pointant vers `application/`. | CI scanne ce dossier pour les fichiers PHP correspondant à la convention de nommage. Doit être accessible en écriture par le serveur web. Des chemins personnalisés comme `BASEPATH.'custom/migrations/'` sont possibles. |

### Comment utiliser les migrations (Étape par étape)

1. **Activer les migrations** : Définissez temporairement `$config['migration_enabled'] = TRUE;` dans le fichier de configuration.

2. **Créer un fichier de migration** : Ajoutez un fichier PHP dans `application/migrations/` avec un nom comme `20121031104401_add_blog.php`. À l'intérieur, utilisez la classe Migration de CI :
   ```php
   defined('BASEPATH') OR exit('No direct script access allowed');

   class Migration_Add_blog extends CI_Migration {
       public function up() {
           $this->dbforge->add_field('id');
           $this->dbforge->create_table('blogs');
       }

       public function down() {
           $this->dbforge->drop_table('blogs');
       }
   }
   ```
   - `up()` applique les changements (ex. créer une table).
   - `down()` les annule (ex. supprimer une table).

3. **Exécuter les migrations** :
   - Chargez la bibliothèque : `$this->load->library('migration');`
   - Vers la dernière version : `$this->migration->current();`
   - Vers une version spécifique : `$this->migration->version('20121031104401');`
   - Depuis la ligne de commande (si CLI activé) : `php index.php migrate current`

4. **Commandes courantes** :
   - `$this->migration->latest()` : Alias de `current()`.
   - `$this->migration->find_migratables()` : Liste les fichiers disponibles.
   Les erreurs sont enregistrées dans les fichiers de log de CI ou lèvent des exceptions.

5. **Bonnes pratiques** :
   - Gardez les migrations idempotentes (sûres à ré-exécuter).
   - Testez d'abord en développement ; évitez d'activer l'auto-migration en production pour éviter des modifications accidentelles du schéma.
   - Utilisez les transactions si votre base de données les prend en charge pour des changements atomiques.
   - Désactivez après utilisation : Remettez sur `FALSE` pour la sécurité.

Si vous rencontrez des problèmes (ex. permissions sur le chemin), vérifiez les logs de CI ou la documentation sur [codeigniter.com/user_guide/libraries/migration.html](https://codeigniter.com/user_guide/libraries/migration.html). Précisez votre version de CI pour des conseils plus adaptés !