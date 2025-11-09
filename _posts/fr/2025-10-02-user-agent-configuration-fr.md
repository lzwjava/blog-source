---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-code-fast-1
title: Tableaux de configuration de l'agent utilisateur CodeIgniter
translated: true
type: note
---

### Aperçu
Cet extrait de code PHP fait partie du framework CodeIgniter (un framework web PHP), spécifiquement du fichier de configuration de la classe User Agent. Il définit quatre tableaux (`$platforms`, `$browsers`, `$mobiles` et `$robots`) qui associent des fragments de chaînes de l'agent utilisateur à des noms lisibles pour les navigateurs, systèmes d'exploitation, appareils mobiles et robots d'indexation. Le code est utilisé pour analyser et identifier le type d'appareil, de navigateur ou de robot visitant un site web en fonction de l'en-tête HTTP User-Agent envoyé par les clients.

Les tableaux sont associatifs (paires clé-valeur), où les clés sont des sous-chaînes provenant des chaînes de l'agent utilisateur (correspondances insensibles à la casse), et les valeurs sont les noms d'affichage correspondants. La bibliothèque User Agent de CodeIgniter les utilise pour la détection, par exemple pour déterminer si un visiteur utilise Android, Chrome, ou s'il s'agit d'un robot de recherche.

### Tableau $platforms
Ce tableau identifie les systèmes d'exploitation ou plates-formes. Les clés sont des sous-chaînes qui peuvent apparaître dans l'en-tête User-Agent, et les valeurs sont des noms propres pour l'affichage.

- **Exemples d'entrées** :
  - `'windows nt 10.0'` → `'Windows 10'`
  - `'android'` → `'Android'`
  - `'os x'` → `'Mac OS X'`
- **Objectif** : Aide à détecter le système d'exploitation du client (par exemple, Windows, iOS, Linux) pour l'analyse, la personnalisation du contenu ou l'ajustement des fonctionnalités.
- **Remarque** : L'ordre est important pour la précision, car certaines sous-chaînes peuvent se chevaucher (par exemple, `'windows'` est une valeur générique à la fin).

### Tableau $browsers
Identifie les navigateurs web. Les navigateurs signalent souvent plusieurs identifiants, donc l'ordre priorise d'abord les sous-types (selon le commentaire).

- **Exemples d'entrées** :
  - `'Chrome'` → `'Chrome'`
  - `'MSIE'` → `'Internet Explorer'`
  - `'Firefox'` → `'Firefox'`
  - Cas spécial : `'Opera.*?Version'` (correspondance de type regex) pour les versions modernes d'Opera qui se signalent comme "Opera/9.80" avec un numéro de version.
- **Objectif** : Détermine le navigateur (par exemple, Chrome, Safari) pour fournir des fonctionnalités spécifiques au navigateur ou des redirections.
- **Remarque sur les regex** : Certaines clés utilisent des motifs regex de base (par exemple, `.*?` pour une correspondance avec des caractères génériques), gérés dans la bibliothèque.

### Tableau $mobiles
Mappe les indicateurs de l'agent utilisateur pour les appareils mobiles, les téléphones et les appareils/navigateurs associés. Il est plus volumineux et inclut les téléphones, tablettes, consoles de jeu et des catégories de repli.

- **Sections structurées** :
  - Téléphones/Fabricants : `'iphone'` → `'Apple iPhone'`, `'samsung'` → `'Samsung'`.
  - Systèmes d'exploitation : `'android'` → `'Android'`, `'symbian'` → `'Symbian'`.
  - Navigateurs : `'opera mini'` → `'Opera Mini'`, `'fennec'` → `'Firefox Mobile'`.
  - Autres/Repli : `'mobile'` → `'Generic Mobile'` pour les indicateurs mobiles non appariés.
- **Objectif** : Identifie les appareils mobiles pour la conception adaptative, les fonctionnalités réservées aux mobiles ou les redirections vers les applications. Inclut des entrées historiques (certaines commentées car obsolètes).

### Tableau $robots
Liste les robots d'indexation et les bots web courants. Les clés sont des sous-chaînes provenant des agents utilisateur des bots.

- **Exemples d'entrées** :
  - `'googlebot'` → `'Googlebot'`
  - `'bingbot'` → `'Bing'`
  - `'yandex'` → `'YandexBot'`
- **Objectif** : Identifie les robots d'indexation pour le traitement SEO, comme servir un contenu différent aux bots (par exemple, sans publicités) ou enregistrer le trafic des bots.

### Utilisation dans CodeIgniter
- La Classe User Agent charge ce fichier et utilise des méthodes comme `is_browser()`, `is_mobile()`, `is_robot()` et `platform()` pour analyser la chaîne User-Agent.
- Elle effectue des recherches insensibles à la casse dans ces tableaux pour faire correspondre les clés avec la chaîne.
- Pour les divergences (par exemple, nouveaux appareils/navigateurs non listés), vous devez mettre à jour ces tableaux manuellement ou via des extensions communautaires.

### Notes supplémentaires
- **Sécurité** : Ceci est uniquement pour la collecte de données ; cela n'exécute pas de code malveillant. Les chaînes User-Agent peuvent être falsifiées, ne vous y fiez donc pas pour des vérifications de sécurité critiques.
- **Mises à jour** : Les versions de CodeIgniter peuvent avoir ajouté/modifié des entrées ; ceci ressemble à un instantané plus ancien (par exemple, Edge comme 'Spartan' est obsolète).
- **Comment tester** : Dans un script PHP, vous pourriez charger ceci et utiliser `strpos` ou des regex pour faire correspondre avec un exemple de chaîne User-Agent.

Si vous fournissez une partie spécifique ou avez une question sur l'implémentation, faites-le-moi savoir !