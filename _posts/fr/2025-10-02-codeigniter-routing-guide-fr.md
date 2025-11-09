---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Guide de Routage CodeIgniter
translated: true
type: note
---

### Aperçu du routage CodeIgniter

Le système de routage de CodeIgniter vous permet de mapper des URLs (URIs) vers des classes contrôleur et des méthodes spécifiques, contournant le modèle d'URL par défaut `example.com/controller/method/id/`. Ceci est utile pour créer des URLs optimisées pour le SEO, gérer des APIs RESTful, ou simplement personnaliser la façon dont les requêtes sont traitées.

L'extrait de code fourni provient du fichier de configuration `routes.php` de CodeIgniter. Il définit un tableau associatif `$route` où chaque clé est un modèle d'URI, et la valeur est soit une chaîne de caractères (`controller/method`), soit un tableau spécifiant différents comportements par méthode HTTP (par exemple, GET, POST). Cette configuration prend en charge à la fois le routage standard et le routage spécifique à la méthode.

Je vais détailler **comment les routes sont définies**, **comment elles fonctionnent**, et **comment les utiliser**, en me basant sur le comportement standard de CodeIgniter et l'exemple dans votre code. Pour plus de détails, reportez-vous au guide officiel de l'utilisateur CodeIgniter sur le routage : https://codeigniter.com/userguide4/general/routing.html.

#### 1. **Comment définir les routes**
Les routes sont définies dans `application/config/routes.php` sous forme de tableau. Vous ajoutez des entrées à `$route[]`. Voici la syntaxe :

- **Route de base** : Mappe n'importe quelle méthode HTTP vers un contrôleur/méthode.
  ```
  $route['uri_segment'] = 'controller/method';
  ```
  - Exemple : `$route['login'] = 'users/login';` signifie que toute requête vers `/login` est routée vers `Users::login()`.

- **Route spécifique à la méthode** : Pour les APIs RESTful, vous pouvez spécifier différents contrôleurs/méthodes par méthode HTTP (GET, POST, PUT, etc.). Cela utilise un tableau.
  ```
  $route['uri_segment'] = array(
      'METHOD1' => 'controller/method1',
      'METHOD2' => 'controller/method2'
  );
  ```
  - Exemple tiré de votre code : `$route['self'] = array('POST' => 'users/update', 'GET' => 'users/self');` signifie :
    - POST vers `/self` → `Users::update()`.
    - GET vers `/self` → `Users::self()`.

- **Caractères génériques (Placeholders)** : Utilisez des motifs de type regex pour capturer des parties dynamiques de l'URL (passées comme paramètres à la méthode).
  - `(:any)` : Correspond à n'importe quel caractère (sauf les barres obliques) – par exemple, pour des slugs ou des chaînes de caractères.
  - `(:num)` ou `(\d+)` : Correspond uniquement aux chiffres – pour les IDs.
  - Regex personnalisée : Entourez de parenthèses, par exemple `(foo|bar)` pour des correspondances spécifiques.
  - Exemples tirés de votre code :
    - `$route['users/(\d+)']['GET'] = 'users/one/$1';` : GET `/users/123` route vers `Users::one(123)`.
    - `$route['lives/(\d+)/notify'] = 'lives/notifyLiveStart/$1';` : Toute méthode vers `/lives/123/notify` route vers `Lives::notifyLiveStart(123)`.

- **Routes réservées** :
  - `$route['default_controller'] = 'welcome';` : Le contrôleur chargé si aucune URI n'est donnée (par exemple, URL racine → contrôleur `Welcome`).
  - `$route['404_override'] = 'errors/page_missing';` : Le contrôleur/méthode pour les routes non trouvées (erreur 404 personnalisée).
  - `$route['translate_uri_dashes'] = FALSE;` : Si TRUE, convertit les tirets dans les URIs en underscores pour les noms de contrôleurs/méthodes (par exemple, `my-controller` → `my_controller`).

- **L'ordre compte** : Les routes sont comparées dans l'ordre où elles apparaissent. Définissez les routes spécifiques (avec caractères génériques) avant les générales pour éviter les conflits.
- **Méthodes HTTP** : Si non spécifiée, une route s'applique à toutes les méthodes. Votre code utilise des tableaux pour la spécificité, ce qui est excellent pour les APIs.

**Conseils pour définir les routes dans votre code** :
- Ajoutez de nouvelles routes à la fin, avant `$route['translate_uri_dashes']`.
- Testez avec des outils comme Postman pour les routes API afin de vous assurer que le bon contrôleur/méthode est atteint.
- Pour les applications complexes, regroupez les routes par section (comme vous l'avez fait avec des commentaires comme `// users`).

#### 2. **Comment fonctionnent les routes**
Le routeur de CodeIgniter traite chaque requête entrante dans cet ordre :
1. **Analyser l'URI** : Décompose l'URL en segments (par exemple, `/users/123/edit` → segments : `users`, `123`, `edit`).
2. **Comparer aux Routes** : Vérifie le tableau `$route` de haut en bas. Il cherche d'abord les correspondances exactes, puis les modèles avec caractères génériques.
   - Si une correspondance est trouvée, elle est mappée vers le contrôleur/méthode spécifié, en passant les parties dynamiques (par exemple, `123`) comme arguments de la méthode.
   - Si aucune correspondance n'est trouvée, il revient au modèle par défaut (`Controller::method/id/`).
3. **Charger le Contrôleur & la Méthode** : CodeIgniter instancie le contrôleur, appelle la méthode et transmet les segments d'URI ou les groupes capturés.
4. **Gestion spécifique à la Méthode** : Si la route est un tableau (comme dans votre code), il vérifie la méthode HTTP (GET, POST, etc.) de la requête.
5. **Solution de repli (Fallback)** : Les requêtes non trouvées déclenchent une erreur 404, ou le `$route['404_override']` s'il est défini.

**Exemple de déroulement** :
- Requête : `POST https://example.com/lives`
- Correspondance : `$route['lives']['POST'] = 'lives/create';`
- Résultat : Appelle `Lives::create()` sans argument.
- Si la requête était `GET https://example.com/lives/456`, elle correspondrait à `$route['lives/(\d+)']['GET'] = 'lives/one/$1';` → `Lives::one(456)`.

**Mécanismes clés** :
- **Paramètres dynamiques** : Les groupes capturés (par exemple, `$1`) sont passés comme arguments à la méthode. Assurez-vous que votre méthode de contrôleur les attend.
- **Sécurité** : Les routes aident à empêcher l'accès direct aux contrôleurs sensibles en obscurcissant les URLs.
- **Performance** : Recherches simples dans un tableau ; pas de surcharge importante sauf si vous avez des centaines de routes.

#### 3. **Comment utiliser les routes**
Utiliser les routes signifie les configurer comme ci-dessus, puis les exploiter dans votre application (contrôleurs, vues, etc.).

- **Dans les Contrôleurs** : Supposez que la route gère le mappage d'URL ; écrivez des méthodes attendant les requêtes routées.
  - Exemple : Pour `$route['login']['POST'] = 'users/login';`, créez un contrôleur `Users.php` avec une méthode `login()` qui gère les données POST (par exemple, via `$this->input->post()`).

- **Générer des URLs** : Utilisez `site_url()` ou `base_url()` de CodeIgniter avec vos clés de route pour les liens/boutons.
  - Exemple : Dans une vue, `<a href="<?= site_url('login'); ?>">Login</a>` pointe vers l'URL routée, mais votre code définit quel contrôleur elle atteint.

- **Tester les Routes** :
  - Utilisez votre navigateur web ou des outils API (par exemple, Postman) pour accéder à des URLs comme `/users/register`.
  - Vérifiez `application/logs/log-{date}.php` pour les erreurs si les routes échouent.
  - Ajoutez du débogage : Réinitialisez temporairement `$route['404_override']` et utilisez var_dump dans un contrôleur de test pour voir les paramètres.

- **Utilisation RESTful (Comme dans votre code)** : Vos routes sont configurées pour une structure de type API. Par exemple :
  - Créer une ressource : Envoyer POST vers `/lives` → Crée un événement en direct.
  - Lecture : GET `/lives/123` → Récupère l'événement en direct #123.
  - Mise à jour : POST `/lives/123` → Met à jour l'événement en direct #123.

- **Pièges courants & Conseils** :
  - **Doublons** : Évitez les routes qui se chevauchent (par exemple, `lives` et `lives/(\d+)`) ; mettez les spécifiques en premier.
  - **Méthodes non spécifiées** : Si une route est une chaîne, elle fonctionne pour toutes les méthodes HTTP. Utilisez des tableaux pour la précision.
  - **Pour le Développement** : Activez le Profileur de CodeIgniter (`$this->output->enable_profiler(TRUE);`) dans un contrôleur pour déboguer le routage.
  - **Gestion de version** : Votre routes.php est sous gestion de version – les modifications affectent le routage en direct.
  - **Extensions** : Si vous avez besoin de fonctionnalités avancées (par exemple, le support des namespaces), envisagez CodeIgniter 4 ou des bibliothèques tierces, car CI 3 (votre code) est plus ancien.

Si vous avez des questions spécifiques sur une route dans votre fichier (par exemple, pourquoi `(\d+)` est utilisé ou comment en ajouter une nouvelle), fournissez plus de détails ! Pour la configuration de CodeIgniter, assurez-vous que `CI_VERSION` est défini dans votre index.php.