---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Aperçu des Hooks CodeIgniter
translated: true
type: note
---

### Que sont les hooks dans CodeIgniter ?

Les hooks dans CodeIgniter sont un moyen d'étendre les fonctionnalités du framework sans modifier ses fichiers de base. Ils vous permettent d'exécuter du code personnalisé à des points spécifiques du cycle d'exécution, tels qu'avant ou après le chargement des contrôleurs, pour remplacer la sortie ou pour la mise en cache. Cela préserve la possibilité de mise à niveau en séparant votre code de la base de code officielle.

Les hooks sont définis dans `application/config/hooks.php` et activés dans `application/config/config.php` en définissant `$config['enable_hooks'] = TRUE;`.

### Activation des hooks

1. Ouvrez `application/config/config.php`.
2. Définissez la variable de configuration :
   ```php
   $config['enable_hooks'] = TRUE;
   ```
   Cela indique à CodeIgniter de vérifier et d'exécuter le fichier de hooks.

### Définition des hooks

Les hooks sont configurés comme un tableau de tableaux dans `application/config/hooks.php`. Chaque tableau de hook spécifie :
- `class` : (Obligatoire) Le nom de la classe (doit correspondre au nom du fichier).
- `function` : (Obligatoire) Le nom de la méthode dans la classe.
- `filename` : (Obligatoire) Le nom du fichier de la classe (sans .php).
- `filepath` : (Optionnel) Le chemin du dossier vers le fichier, par défaut `application/hooks/`.
- `params` : (Optionnel) Un tableau de paramètres à passer à la méthode.

Placez vos classes de hook dans `application/hooks/`.

### Points de hook

CodeIgniter fournit ces points prédéfinis où les hooks peuvent s'exécuter :
- **pre_system** : S'exécute avant le chargement du système (rien d'autre n'a encore été exécuté).
- **pre_controller** : S'exécute juste avant l'appel du contrôleur.
- **post_controller_constructor** : S'exécute après l'instanciation du contrôleur mais avant l'exécution de ses méthodes.
- **post_controller** : S'exécute après la fin du contrôleur.
- **display_override** : S'exécute au lieu d'envoyer la sortie au navigateur (remplace `_display`).
- **cache_override** : S'exécute au lieu de charger le cache (remplace `_display` pour le cache).
- **post_system** : S'exécute après l'envoi complet de la page web au navigateur.

### Exemple d'utilisation

Supposons que vous souhaitiez journaliser chaque requête avant l'exécution du contrôleur. Créez un hook pour `pre_controller`.

1. Créez le fichier `application/hooks/my_hook.php` :
   ```php
   <?php
   class My_hook {
       public function log_request() {
           // Exemple : Journaliser dans un fichier ou une base de données
           log_message('info', 'Controller sur le point d\'être appelé : ' . $this->uri->uri_string());
       }
   }
   ```

2. Dans `application/config/hooks.php`, ajoutez :
   ```php
   $hook['pre_controller'] = array(
       'class' => 'My_hook',
       'function' => 'log_request',
       'filename' => 'my_hook.php',
       'filepath' => 'hooks', // Optionnel, par défaut application/hooks/
       'params' => array() // Paramètres optionnels
   );
   ```

Maintenant, chaque fois qu'un contrôleur est sur le point de s'exécuter, `log_request` sera exécuté.

### Bonnes pratiques
- Utilisez les hooks avec parcimonie ; si possible, étendez les contrôleurs ou utilisez des bibliothèques à la place.
- Testez toujours les hooks dans un environnement de développement pour vous assurer qu'ils n'interfèrent pas avec la logique de base.
- Pour plus de détails, reportez-vous au guide officiel de l'utilisateur CodeIgniter sur les hooks.