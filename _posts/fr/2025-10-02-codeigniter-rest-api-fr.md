---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Configuration de l'API REST CodeIgniter
translated: true
type: note
---

Voici un guide clair et détaillé pour comprendre et utiliser le fichier de configuration de l'API REST CodeIgniter que vous avez partagé (`application/config/rest.php`). Ce fichier configure le comportement de la bibliothèque REST_Controller (une bibliothèque PHP populaire pour créer des API RESTful dans CodeIgniter), comme la bibliothèque REST de Phil Sturgeon (maintenant maintenue dans certaines versions du framework CodeIgniter).

J'expliquerai :
- Ce que fait la bibliothèque et les prérequis clés.
- Comment la configurer et l'utiliser.
- Les options de configuration principales de votre fichier (avec des exemples).
- Un exemple d'utilisation simple.
- Des conseils pour les pièges courants et la sécurité.

Si votre question concerne spécifiquement un aspect (par exemple, l'authentification ou les limites), n'hésitez pas à préciser pour obtenir des conseils plus ciblés !

### 1. **Prérequis et Configuration**
   - **Qu'est-ce que c'est ?** Il s'agit de la bibliothèque REST_Controller pour CodeIgniter (un framework PHP). Elle vous permet de créer des API RESTful (par exemple, des points de terminaison qui répondent en JSON/XML aux requêtes GET/POST) en étendant vos contrôleurs à partir de `REST_Controller`. Votre fichier de configuration contrôle les paramètres globaux comme l'authentification, les formats de réponse, la limitation du débit et la sécurité.

   - **Exigences :**
     - CodeIgniter 3.x (ou une version compatible ; cette configuration est pour les versions antérieures autour de la 3.x).
     - Installez la bibliothèque REST_Controller si elle n'est pas déjà dans votre installation CodeIgniter (vous pouvez la télécharger depuis GitHub : `chriskacerguis/codeigniter-restserver`). Placez les fichiers de la bibliothèque dans `application/libraries/` et chargez-la automatiquement dans `application/config/autoload.php` :
       ```php
       $autoload['libraries'] = ['rest_controller'];
       ```
     - Configuration de la base de données (optionnelle ; nécessaire pour des fonctionnalités comme les clés API, la journalisation ou les limites). Exécutez les schémas SQL fournis dans les commentaires du fichier de configuration (par exemple, pour les tables `keys`, `logs`, `access`, `limits`).
     - Activez les URLs simplifiées dans CodeIgniter (`application/config/routes.php`) pour des points de terminaison d'API propres comme `/api/users`.
     - Votre fichier de configuration `rest.php` doit être placé dans `application/config/` et chargé automatiquement dans `application/config/autoload.php` :
       ```php
       $autoload['config'] = ['rest'];
       ```

   - **Étapes d'installation de base :**
     1. Téléchargez et décompressez CodeIgniter.
     2. Ajoutez les fichiers de la bibliothèque REST_Controller.
     3. Copiez votre `rest.php` fourni dans `application/config/`.
     4. Configurez les routes dans `routes.php` (par exemple, `$route['api/(:any)'] = 'api/$1';` pour mapper `/api/users` vers un contrôleur).
     5. Créez des contrôleurs d'API (voir l'exemple ci-dessous).
     6. Testez avec un outil comme Postman ou curl.

### 2. **Options de Configuration Clés**
Je vais résumer les principaux paramètres de votre fichier de configuration, regroupés par objectif. Ceux-ci contrôlent le comportement global. Vous pouvez les modifier selon vos besoins (par exemple, activer HTTPS ou changer les formats par défaut).

- **Protocole et Sortie :**
  - `$config['force_https'] = FALSE;` : Force tous les appels d'API à utiliser HTTPS. Définissez à `TRUE` pour la sécurité en production.
  - `$config['rest_default_format'] = 'json';` : Format de réponse par défaut (options : json, xml, csv, etc.). Les requêtes peuvent le remplacer via l'URL (par exemple, `/api/users.format=xml`).
  - `$config['rest_supported_formats']` : Liste des formats autorisés. Supprimez ceux qui ne sont pas souhaités pour des raisons de sécurité.
  - `$config['rest_ignore_http_accept'] = FALSE;` : Ignore les en-têtes HTTP Accept du client pour accélérer les réponses (utile si vous utilisez toujours `$this->rest_format` dans le code).

- **Authentification (Sécurité) :**
  - `$config['rest_auth'] = FALSE;` : Mode d'authentification principal. Options :
    - `FALSE` : Aucune authentification requise.
    - `'basic'` : Authentification HTTP Basic (nom d'utilisateur/mot de passe dans les en-têtes base64).
    - `'digest'` : Authentification digest plus sécurisée.
    - `'session'` : Vérifie une variable de session PHP.
  - `$config['auth_source'] = 'ldap';` : Où vérifier les identifiants (par exemple, tableau de configuration, LDAP, bibliothèque personnalisée).
  - `$config['rest_valid_logins'] = ['admin' => '1234'];` : Tableau simple nom d'utilisateur/mot de passe (ignoré si LDAP est utilisé).
  - `$config['auth_override_class_method']` : Remplace l'authentification pour des contrôleurs/méthodes spécifiques (par exemple, `'users' => 'view' => 'basic'`).
  - `$config['auth_library_class/function']` : Si vous utilisez une bibliothèque personnalisée, spécifiez la classe/méthode pour la validation.
  - Contrôles d'IP :
    - `$config['rest_ip_whitelist_enabled/blacklist_enabled']` : Filtrage d'IP de base pour votre API.
    - Utile pour restreindre l'accès (par exemple, liste blanche des IP de votre application).

- **Clés API (Couche de Sécurité Optionnelle) :**
  - `$config['rest_enable_keys'] = FALSE;` : Active la vérification des clés API (stockées dans la table de base de données `keys`). Les clients doivent envoyer les clés dans les en-têtes (par exemple, `X-API-KEY`).
  - `$config['rest_key_column/name/length']` : Personnalisez les champs de clé et le nom de l'en-tête.
  - Associez avec `$config['rest_enable_access']` pour restreindre les clés à des contrôleurs/méthodes spécifiques.

- **Journalisation et Limites :**
  - `$config['rest_enable_logging/limits'] = FALSE;` : Active la journalisation basée sur la base de données des requêtes (URI, paramètres, etc.) ou la limitation du débit (par exemple, X appels par heure par clé).
  - Tables : `logs`, `limits` (exécutez le SQL dans les commentaires pour les créer).
  - `$config['rest_limits_method']` : Comment appliquer les limites (par clé API, URL, etc.).
  - Personnalisez par méthode dans les contrôleurs (par exemple, `$this->method['get']['limit'] = 100;`).

- **Autres :**
  - `$config['rest_ajax_only'] = FALSE;` : Restreint aux requêtes AJAX uniquement (retourne une erreur 505 sinon).
  - `$config['rest_language'] = 'english';` : Langue pour les messages d'erreur.

Pour modifier : Éditez `rest.php` et redémarrez votre application. Testez les changements soigneusement !

### 3. **Comment l'Utiliser : Utilisation Étape par Étape**
Une fois configuré, créez des points de terminaison d'API en créant des contrôleurs qui étendent `REST_Controller`. Voici un processus de haut niveau :

1. **Créez un Contrôleur :**
   - Dans `application/controllers/`, créez `Api.php` (ou par exemple `Users.php` pour une ressource spécifique) :
     ```php
     <?php
     defined('BASEPATH') OR exit('No direct script access allowed');
     require_once(APPPATH . 'libraries/REST_Controller.php');

     class Api extends REST_Controller {
         public function __construct() {
             parent::__construct();
             // Optionnel : Définir l'authentification, les limites par méthode
             $this->load->database();
             $this->method['index_get']['limit'] = 100; // 100 requêtes/heure
         }

         // GET /api
         public function index_get() {
             $data = ['message' => 'Bienvenue sur l\'API', 'status' => 'success'];
             $this->response($data, REST_Controller::HTTP_OK);
         }

         // POST /api/users
         public function users_post() {
             $data = $this->input->post(); // Obtenir les données POST
             if (empty($data['name'])) {
                 $this->response(['error' => 'Le nom est requis'], REST_Controller::HTTP_BAD_REQUEST);
             }
             // Traiter (par exemple, insérer dans la base de données)
             $this->response(['message' => 'Utilisateur créé'], REST_Controller::HTTP_CREATED);
         }

         // PUT /api/users/{id}
         public function users_put($id) {
             $data = $this->put(); // Obtenir les données PUT
             // Mettre à jour l'utilisateur avec $id
             $this->response(['message' => 'Utilisateur mis à jour'], REST_Controller::HTTP_OK);
         }

         // etc. pour DELETE
     }
     ```

2. **Envoyez des Requêtes :**
   - Utilisez n'importe quel client HTTP :
     - GET : `curl http://votredomaine.com/api` → Retourne JSON {"message": "Bienvenue sur l'API", "status": "success"}
     - POST : `curl -X POST http://votredomaine.com/api/users -d "name=John"` → Crée un utilisateur.
   - Incluez les en-têtes si vous utilisez l'authentification/les clés (par exemple, `Authorization: Basic base64(utilisateur:motdepasse)` ou `X-API-KEY: votreclé`).

3. **Testez et Déboguez :**
   - Vérifiez les journaux de CodeIgniter pour les erreurs.
   - Si l'authentification échoue, assurez-vous que les identifiants sont correctement définis.
   - Pour les limites/la journalisation, interrogez vos tables de base de données.

### 4. **Conseils Courants et Bonnes Pratiques**
- **Sécurité :** Utilisez toujours HTTPS en production (`force_https = TRUE`). Activez les clés si vous exposez à des clients externes. Assainissez les entrées pour prévenir l'injection SQL.
- **Erreurs :** Les réponses incluent des champs `status` et `error` (personnalisables dans la configuration). Utilisez le profileur de CodeIgniter pour le débogage.
- **Performance :** Si la journalisation/les limites sont activées, votre base de données gérera les requêtes—surveillez les performances lentes.
- **Mise à niveau :** Cette configuration est pour les anciennes versions de CodeIgniter. Pour CI 4, utilisez leurs ressources d'API intégrées (cette configuration peut nécessiter des ajustements).
- **Dépannage :**
  - "Pas de réponse" ? Vérifiez les routes, le chargement automatique et les chemins de la bibliothèque.
  - Problèmes d'authentification ? Vérifiez `$auth_source` et les identifiants.
  - Erreurs de format ? Assurez-vous que votre format est dans `rest_supported_formats`.
- **Ressources :** Documentation sur codeigniter-restserver.org. Pour la migration vers CI4, consultez la documentation officielle.

Si cela ne répond pas exactement à votre question ou si vous avez besoin de code pour un cas d'utilisation spécifique (par exemple, activer OAuth), fournissez plus de détails !