---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Vue d'ensemble du système de cache de CodeIgniter
translated: true
type: note
---

### Aperçu de la bibliothèque de cache de CodeIgniter

La classe `CI_Cache` de CodeIgniter est un système de cache flexible qui fournit une interface unifiée pour stocker et récupérer des données sur diverses plateformes (comme en mémoire, basé sur des fichiers, ou via des services externes). Elle étend `CI_Driver_Library`, qui charge les pilotes dynamiquement. La classe abstrait les opérations de cache, permettant aux développeurs de changer de plateforme facilement via la configuration sans modifier le code de l'application. Toutes les méthodes délèguent à "l'adaptateur" actif (une classe pilote), avec un support de repli pour la fiabilité.

Le système met l'accent sur les performances, la portabilité et la tolérance aux pannes—par exemple, il utilise par défaut un pilote "dummy" (sans opération) si les autres échouent, garantissant que l'application ne plante pas à cause de problèmes de cache.

### Pilotes et adaptateurs de cache pris en charge

La classe prend en charge plusieurs pilotes, définis dans `$valid_drivers` :
- **apc** : Utilise APC (Alternative PHP Cache) de PHP pour le stockage en mémoire (rapide, intégré).
- **dummy** : Un espace réservé qui ne fait rien (retourne toujours TRUE ou FALSE) ; utilisé comme solution de repli pour le développement/les tests.
- **file** : Stocke les données sous forme de fichiers sérialisés dans un répertoire (spécifié par `$_cache_path`), adapté aux sites à faible trafic.
- **memcached** : Interface vers le service Memcached pour le cache en mémoire distribué (haute performance, évolutif).
- **redis** : Interface vers Redis, un autre magasin clé-valeur en mémoire avec des fonctionnalités comme pub/sub et les opérations atomiques.
- **wincache** : Spécifique à Windows pour IIS (utilise Microsoft WinCache).

Chaque pilote est une classe distincte (par exemple, `CI_Cache_memcached`) implémentant des méthodes comme `get()`, `save()`, etc. La bibliothèque charge le pilote dynamiquement en fonction du tableau `$config['adapter']` passé au constructeur.

### Initialisation et configuration

- **Constructeur** : Prend un tableau `$config` avec des clés pour `adapter` (pilote principal), `backup` (pilote de repli) et `key_prefix` (chaîne préfixée à toutes les clés de cache pour l'isolation/le namespacing).
  - Exemple de configuration : `array('adapter' => 'redis', 'backup' => 'file', 'key_prefix' => 'myapp_')`.
- **Logique de repli** : Après l'initialisation, il vérifie si l'adaptateur principal est pris en charge en utilisant `is_supported($driver)` (qui appelle la méthode `is_supported()` du pilote, testant les extensions PHP ou services requis).
  - Si le pilote principal échoue, il bascule vers le pilote de repli. Si les deux échouent, il enregistre une erreur et utilise par défaut le pilote "dummy" (via `log_message()`).
  - Cela garantit que le cache a toujours un adaptateur fonctionnel, évitant les plantages.

Le `$_cache_path` est défini pour les pilotes basés sur des fichiers, mais il n'est pas initialisé ici—c'est probablement géré dans la classe du pilote de fichiers.

### Méthodes clés et leur fonctionnement

Les méthodes préfixent le `key_prefix` aux IDs pour une portée unique (par exemple, `'myapp_user123'`) et délèguent à l'adaptateur actif. Toutes les opérations renvoient des booléens, des tableaux ou des données mixtes en cas de succès/échec.

- **get($id)** : Récupère les données en cache par ID.
  - Exemple : `$data = $cache->get('user_profile');` —appelle la méthode `get()` de l'adaptateur.
  - Si la clé existe et n'a pas expiré, renvoie les données ; sinon, renvoie FALSE.
  - Aucune application directe du TTL ici ; gérée par le pilote (par exemple, Redis ou Memcached appliquent le TTL en interne).

- **save($id, $data, $ttl = 60, $raw = FALSE)** : Stocke les données avec un time-to-live (TTL) en secondes.
  - Exemple : `$cache->save('user_profile', $profile_data, 3600);` —stocke avec une expiration d'une heure.
  - Le drapeau `$raw` (faux par défaut) indique si les données sont sérialisées—les pilotes gèrent la sérialisation si nécessaire (par exemple, les tableaux/objets deviennent des chaînes).
  - Renvoie TRUE en cas de succès, facilitant la logique conditionnelle (par exemple, générer et mettre en cache les données si l'enregistrement échoue).

- **delete($id)** : Supprime un élément de cache spécifique.
  - Exemple : `$cache->delete('user_profile');` —suppression permanente.

- **increment($id, $offset = 1)** et **decrement($id, $offset = 1)** : Opérations atomiques pour les valeurs numériques (utiles pour les compteurs).
  - Exemple : `$new_counter = $cache->increment('hits', 5);` —incrémente de 5 si supporté par le pilote (par exemple, Redis/Memcached sont atomiques ; les pilotes basés sur des fichiers peuvent simuler).
  - Tous les pilotes ne prennent pas en charge raw/inc/dec (dummy échoue toujours) ; renvoie la nouvelle valeur ou FALSE.

- **clean()** : Efface toutes les données du cache pour le pilote actuel.
  - Exemple : `$cache->clean();` —utile pour vider après des mises à jour.
  - Le type "user" cible les données spécifiques à l'utilisateur, pas les caches système.

- **cache_info($type = 'user')** : Renvoie les métadonnées sur le cache (par exemple, les statistiques du serveur, le nombre de clés, ou les chemins de fichiers).
  - Exemple : `$info = $cache->cache_info();` —un tableau de détails provenant du pilote.

- **get_metadata($id)** : Obtient les détails sur un élément en cache spécifique (par exemple, le temps d'expiration, la taille).
  - Exemple : `$meta = $cache->get_metadata('key');` —aide au débogage ou à l'optimisation.

- **is_supported($driver)** : Vérifie la disponibilité du pilote (met en cache les résultats en utilisant un tableau statique `$support` pour éviter les vérifications répétées).

### Mécanismes supplémentaires

- **Préfixage des clés** : Appliqué automatiquement à tous les IDs (par exemple, pour l'isolation des applications ou le multi-entrant). Activé via la configuration pour éviter les collisions de clés entre les environnements.
- **Journalisation** : Utilise `log_message()` pour les messages de débogage/d'erreur (par exemple, les replis), s'intégrant au système de journalisation de CodeIgniter.
- **Flexibilité et tolérance aux pannes** : En abstraisant les plateformes, vous pouvez passer de la mise en cache fichier (économique, local) à Redis (rapide, distribué) avec des changements minimes. Le repli sur "dummy" signifie que les échecs de cache n'arrêtent pas l'application—les méthodes renvoient simplement FALSE, permettant au code de continuer (par exemple, récupérer depuis la base de données à la place).
- **Notes sur les performances** : Les pilotes comme APC/Redis sont en mémoire (accès rapide, sub-milliseconde). Ceux basés sur des fichiers sont plus lents en raison des E/S disque. Les TTL sont généralement respectés par les pilotes sauf dans de rares cas particuliers spécifiques au pilote.

Cette conception rend le cache de CodeIgniter modulaire et fiable. Pour les détails sur des pilotes spécifiques, consultez les fichiers des pilotes (par exemple, `Cache_memcached.php`). Reportez-vous toujours à la documentation officielle de CodeIgniter pour les nuances spécifiques à la version, car ce code provient d'une version plus ancienne (environ 2.0-3.x). Si vous avez une méthode ou un pilote spécifique en tête, je peux approfondir !