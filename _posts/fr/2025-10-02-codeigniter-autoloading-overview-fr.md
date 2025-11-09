---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Vue d'ensemble du système d'autochargement de CodeIgniter
translated: true
type: note
---

### Présentation du système d'auto-chargement de CodeIgniter

Dans CodeIgniter (un framework PHP), le fichier `autoload.php` (généralement situé dans `application/config/autoload.php`) vous permet de spécifier les ressources qui doivent être chargées automatiquement à chaque requête. Cela rend les composants couramment utilisés disponibles sans avoir à les charger manuellement dans chaque contrôleur ou ailleurs, améliorant ainsi l'efficacité et réduisant la duplication de code. Le framework les charge pendant son processus d'initialisation, avant le routage de la requête.

Le fichier définit un tableau `$autoload` avec des sous-tableaux pour différents types de ressources : packages, libraries, drivers, helpers, fichiers de configuration, fichiers de langue et modèles. Vous remplissez ces tableaux avec les noms des ressources que vous souhaitez charger automatiquement. Décommentez ou modifiez les lignes pour activer le chargement ; laissez-les vides pour l'ignorer.

### Fonctionnement pratique

Le processus d'amorçage de CodeIgniter (via `index.php` et le cœur de CI) vérifie ce fichier lors de l'initialisation du système. Il parcourt le tableau `$autoload` et charge chaque ressource spécifiée en :
- Trouvant le fichier dans le répertoire approprié (par exemple, `system/libraries/` pour les bibliothèques principales, `application/libraries/` pour les bibliothèques personnalisées).
- Instanciant les classes (pour les bibliothèques/modèles) ou incluant les fichiers (pour les aides/configuration).
- Les rendant disponibles globalement (par exemple, les bibliothèques sont accessibles via `$this->nom_bibliotheque` dans les contrôleurs).

Si une ressource n'est pas trouvée, cela peut provoquer des erreurs—assurez-vous que les chemins et les noms sont corrects. Vous pouvez charger des éléments supplémentaires manuellement plus tard si nécessaire en utilisant des méthodes comme `$this->load->library('session')`.

### Détail de chaque section de votre fichier

Voici une explication section par section basée sur le code fourni. J'ai inclus ce que fait chaque tableau, des notes d'utilisation et des exemples. Les valeurs par défaut sont principalement vides pour garder le framework léger.

#### 1. Auto-chargement des Packages
```php
$autoload['packages'] = array();
```
- **Objectif** : Charge les packages tiers. Il s'agit généralement d'ensembles réutilisables de bibliothèques/aides/modèles, souvent dans des sous-répertoires comme `APPPATH.'third_party'` ou des chemins personnalisés.
- **Fonctionnement** : Ajoute les répertoires spécifiés au tableau des chemins des packages. CodeIgniter recherchera ensuite ceux-ci pour les classes préfixées par `MY_` et les chargera si nécessaire.
- **Utilisation** : Exemple : `$autoload['packages'] = array(APPPATH.'third_party', '/usr/local/shared');` – Remplace les chemins dans les appels comme `$this->load->add_package_path()`.
- **Note** : Vide par défaut ; utile pour étendre le framework sans modifier le cœur.

#### 2. Auto-chargement des Bibliothèques
```php
$autoload['libraries'] = array();
```
- **Objectif** : Charge les bibliothèques de classes (par exemple, gestion de session, email, etc.).
- **Fonctionnement** : Charge et instancie les classes depuis `system/libraries/` ou `application/libraries/`. Les plus courantes incluent 'database', 'session', 'email'.
- **Utilisation** : Exemple : `$autoload['libraries'] = array('database', 'email', 'session');` ou avec des alias comme `$autoload['libraries'] = array('user_agent' => 'ua');` (permet d'utiliser `$this->ua` au lieu de `$this->user_agent`).
- **Note** : La base de données est spéciale—la charger établit automatiquement une connexion. Évitez de trop charger automatiquement pour minimiser l'utilisation de la mémoire.

#### 3. Auto-chargement des Pilotes
```php
$autoload['drivers'] = array();
```
- **Objectif** : Charge les bibliothèques basées sur des pilotes qui offrent plusieurs implémentations interchangeables (par exemple, mise en cache, manipulation d'image).
- **Fonctionnement** : Sous-classes de `CI_Driver_Library`. Charge la classe du pilote et son sous-répertoire.
- **Utilisation** : Exemple : `$autoload['drivers'] = array('cache');` – Charge `system/libraries/Cache/drivers/cache_apc_driver.php` ou similaire.
- **Note** : Les pilotes sont modulaires ; vous spécifiez quel pilote utiliser à l'exécution (par exemple, `$this->cache->apc->save()`).

#### 4. Auto-chargement des Fichiers d'Aide
```php
$autoload['helper'] = array('base');
```
- **Objectif** : Charge les fonctions d'aide (bibliothèques de fonctions PHP, par exemple pour les URLs, les fichiers, les formulaires).
- **Fonctionnement** : Inclut le fichier (par exemple, `application/helpers/base_helper.php`), rendant ses fonctions globales.
- **Utilisation** : Exemple : `$autoload['helper'] = array('url', 'file');` – Permet d'appeler `site_url()` sans charger l'aide manuellement.
- **Note** : Dans votre fichier, 'base' est chargé automatiquement—assurez-vous que `base_helper.php` existe.

#### 5. Auto-chargement des Fichiers de Configuration
```php
$autoload['config'] = array();
```
- **Objectif** : Charge les fichiers de configuration personnalisés au-delà du fichier par défaut `config.php`.
- **Fonctionnement** : Fusionne les configurations supplémentaires (par exemple, `application/config/custom.php`) dans le tableau de configuration global.
- **Utilisation** : Exemple : `$autoload['config'] = array('custom', 'seo');` – Charge `custom.php` et `seo.php` en tant que configurations.
- **Note** : Laissez vide si vous utilisez les valeurs par défaut ; utile pour les paramètres spécifiques au site.

#### 6. Auto-chargement des Fichiers de Langue
```php
$autoload['language'] = array();
```
- **Objectif** : Charge les tableaux de langue pour l'internationalisation.
- **Fonctionnement** : Charge les fichiers depuis `application/language/english/` (ou la langue actuelle), par exemple `form_lang.php`.
- **Utilisation** : Exemple : `$autoload['language'] = array('form', 'calendar');` – Charge `form_lang.php` sans le suffixe '_lang'.
- **Note** : La langue est auto-détectée depuis la configuration ; rarement nécessaire pour les éléments globaux.

#### 7. Auto-chargement des Modèles
```php
$autoload['model'] = array('BaseDao');
```
- **Objectif** : Charge les classes de modèle pour les interactions avec la base de données.
- **Fonctionnement** : Charge et instancie depuis `application/models/`, par exemple `BaseDao.php`.
- **Utilisation** : Exemple : `$autoload['model'] = array('user_model', 'BaseDao' => 'base');` – Permet d'utiliser `$this->base` comme alias.
- **Note** : Dans votre fichier, 'BaseDao' est chargé automatiquement—assurez-vous que c'est une classe de modèle valide.

### Conseils d'utilisation
- **Modification du Fichier** : Modifiez `autoload.php` pour ajouter des éléments. Testez après les modifications pour vous assurer qu'il n'y a pas de conflits.
- **Performances** : Tout charger automatiquement peut ralentir les requêtes ; chargez uniquement ce qui est nécessaire globalement.
- **Chargement Manuel** : Si quelque chose n'est pas chargé automatiquement, utilisez `$this->load->library('nom');` ou similaire dans les contrôleurs.
- **Notes de Version** : Ceci s'applique à CodeIgniter 2.x/3.x. Dans la version 4.x, l'auto-chargement est passé à un système basé sur Composer (namespaces), mais les fichiers de configuration comme celui-ci sont toujours utilisés dans les versions antérieures.

Si vous avez des questions spécifiques sur l'ajout d'éléments ou la résolution d'erreurs, fournissez plus de détails !